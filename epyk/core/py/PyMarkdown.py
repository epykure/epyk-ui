#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import json


RULES = {
  '\!\[(.*)\]\((.*)\)': {'cls': 'ui.img', 'attrs': ["tooltip", "text"], 'pattern': "![%s](%s)"},
  '\[(.*)\]\((.*)\)': {'cls': 'ui.link', 'attrs': ["text", "url"], 'pattern': "[%s](%s)", 'tag': "<a href='%s'>%s</a>"},
  '\*(.*)\*': {'cls': 'ui.tags.i', 'attrs': ["text"], 'pattern': "*%s*", 'tag': "<i>%s</i>"},
  '\*\*(.*)\*\*': {'cls': 'ui.tags.i', 'attrs': ["text"], 'pattern': "**%s**", 'tag': "<b>%s</b>"},
  '\_\_(.*)\_\_': {'cls': 'ui.tags.b', 'attrs': ["text"], 'pattern': "__%s__"},
  '``(.*)``': {'cls': 'ui.texts.code', 'attrs': ["text"], 'pattern': "``%s``", 'tag': "<code>%s</code>"},
  '^## (.*)$': {'cls': 'ui.subtitle', 'attrs': ["text"], 'pattern': "## %s"},
  '^=======': {'cls': 'ui.layouts.underline', 'attrs': None, 'pattern': "======="},
  '^------': {'cls': 'ui.layouts.accentuate', 'attrs': None, 'pattern': "------"},
  '^# (.*)$': {'cls': 'ui.title', 'attrs': ["text"], 'pattern': "# %s"},
  '^___$': {'cls': 'ui.layouts.hr', 'attrs': [], 'pattern': "___"},
}


PARAMS = {
  "text": {"type": "String", "Optional": True, "value": "The value to be displayed to the button."},
  "angle": {"type": "Integer", "value": "The rotation angle."},
  "i": {"type": "Integer", "value": "An Index number."},
  "width": {"type": "Tuple", "Optional": True, "value": "A tuple with the integer for the component width and its unit."},
  "height": {"type": "Tuple", "Optional": True, "value": "A tuple with the integer for the component height and its unit."},
  "icon": {"type": "String", "Optional": True, "value": "A string with the value of the icon to display from font-awesome."},
  "htmlCode": {"type": "String", "Optional": True, "value": "An identifier for this component (on both Python and Javascript side)."},
  "tooltip": {"type": "String", "Optional": True, "value": "A string with the value of the tooltip."},
  "profile": {"type": "Boolean | Dictionary", "Optional": True, "value": "A flag to set the component performance storage."},
  "options": {"type": "Dictionary", "Optional": True, "value": "Specific Python options available for this component."},
  "top": {"type": "Tuple", "Optional": True, "value": "A tuple with the integer for the component's distance to the top of the page."},
  "left": {"type": "Tuple", "Optional": True, "value": "A tuple with the integer for the component's distance to the left of the page."},
  "align": {"type": "String", "Optional": True, "value": "The text-align property within this component."},
  "image": {"type": "String", "Optional": True, "value": "The url of the image."},
  "position": {"type": "String", "Optional": True, "value": "The position compared to the main component tag."},
  "js_funcs": {"type": "List | String", "Optional": True, "value": "Javascript functions."},
  "status": {"type": "Boolean", "Optional": True, "value": "A flag to specify the status of the loading event."},
  "source_event": {"type": "String", "Optional": True, "value": "The source target for the event."},
  "onReady": {"type": "Boolean", "Optional": True, "value": "Specify if the event needs to be trigger when the page is loaded."},
  "green": {"type": "String", "Optional": True, "value": "The color used in case of result true."},
  "red": {"type": "String", "Optional": True, "value": "The color used in case of result false."},
  "neutral": {"type": "String", "Optional": True, "value": "The color used in case of null."},
  "weekend": {"type": "Boolean", "Optional": True, "value": "Flag to specify if the weekends should be considered."},
}


def doc_string_attrs(func):
  """
  Description:
  ------------
  Write the attribute section in the framework documentation.

  Usage::


  Attributes:
  ----------
  :param func: Function. A python function.
  """
  dflt_vals = {}
  if func.__defaults__ is not None:
    for i, k in enumerate(list(func.__code__.co_varnames)[::-1]):
      if i >= len(func.__defaults__):
        break

      dflt_vals[k] = func.__defaults__[i]
  for arg in func.__code__.co_varnames:
    if arg == "self":
      continue

    if arg in PARAMS:
      dfl_val = ""
      if arg in dflt_vals:
        required = "Optional"
        dfl_val = "(Default = %s)" % dflt_vals[arg]
      else:
        required = "Required" if PARAMS[arg].get('Optional', True) else "Optional"
      print(":param %s: %s. %s. %s %s" % (arg, PARAMS[arg]["type"], required, PARAMS[arg]["value"], dfl_val))
    else:
      print(":param %s:" % arg)


class MarkDown:

  def __init__(self, page):
    self.page = page

  @classmethod
  def translate(cls, data):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    """
    convert_data = data
    count, map_objs = 0, {}
    for r, interface in RULES.items():
      m = re.findall(r, data, re.MULTILINE)
      if m is not None:
        for g in m:
          attrs = dict(zip(interface['attrs'], g))
          map_objs["%s_%s" % (interface['cls'], count)] = "%s(%s)" % (
            interface['cls'], ", ".join(["%s=%s" % (k, json.dumps(v)) for k, v in attrs.items()]))
          if "%s" in interface['pattern']:
            convert_data = convert_data.replace(interface['pattern'] % g, "||%s_%s||" % (interface['cls'], count))
          else:
            convert_data = convert_data.replace(interface['pattern'], "||%s_%s||" % (interface['cls'], count))
          count += 1
    resolved_data = []
    for rec in convert_data.split("||"):
      resolved_data.append(map_objs.get(rec, rec))
    return resolved_data

  def resolve(self, data, css_attrs=None):
    """
    Description:
    -----------
    Convert a string to a markdown file.

    Attributes:
    ----------
    :param data: String. Data to be converted.
    :param css_attrs: Dictionary. Optional. The CSS Style to be applied to the component.
    """
    components, css = [], css_attrs
    for line in data.split("\n"):
      if line.startswith("$STYLE|"):
        css = {}
        for attr in line.split("|")[-1].strip().split(";"):
          k, v = attr.split(":")
          css[k] = v
        continue

      if line == "$STYLE":
        css = css_attrs
        continue

      for r, cls in RULES.items():
        m = re.findall(r, line, re.MULTILINE)
        if m:
          comp_cls = self.page
          for sub in cls['cls'].split("."):
            comp_cls = getattr(comp_cls, sub)
          attrs = cls['attrs']
          if attrs is not None:
            if len(attrs) > 1:
              attrs = dict(zip(cls['attrs'], m[0]))
            else:
              attrs = dict(zip(cls['attrs'], m))
            components.append(comp_cls(**attrs))
          else:
            components.append(comp_cls())
          if css is not None:
            components[-1].css(css)
          break

      else:
        if line:
          components.append(self.page.ui.texts.paragraph(line, options={"markdown": True}))
          if css_attrs is not None:
            components[-1].css(css_attrs)
        else:
          components.append(self.page.ui.layouts.br())
    return components

  def all(self, data):
    """
    Description:
    -----------

    TODO: Improve this function.

    Attributes:
    ----------
    :param data: String. The data to be parsed.
    """
    for r, interface in RULES.items():
      if 'tag' not in interface:
        continue

      m = re.findall(r, data, re.MULTILINE)
      for v in m:
        data = data.replace(interface["pattern"] % v, interface["tag"] % v)

    multi_lines_component = None
    converted_data = []
    for rec in data.split("\n"):
      if rec.startswith("-"):
        if multi_lines_component is None:
          multi_lines_component = {"type": 'list', "records": []}
        multi_lines_component["records"].append({"text": rec[1:].strip()})
      elif multi_lines_component is not None and multi_lines_component["type"] == "list":
        converted_data.append("<ul style='margin:5px 0'>")
        for li in multi_lines_component["records"]:
          converted_data.append("<li>%s</li>" % li["text"])
        converted_data.append("</ul>")
        multi_lines_component = None
      if multi_lines_component is None:
        converted_data.append(rec)
    return "\n".join(converted_data)
