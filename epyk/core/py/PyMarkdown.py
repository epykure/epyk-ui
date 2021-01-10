#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import json


RULES = {
  '\!\[(.*)\]\((.*)\)': {'cls': 'page.ui.img', 'attrs': ["tooltip", "text"], 'pattern': "![%s](%s)"},
  '\[(.*)\]\((.*)\)': {'cls': 'page.ui.link', 'attrs': ["text", "url"], 'pattern': "[%s](%s)"},
  '\*\*\((.*)\)\*\*': {'cls': 'page.ui.tags.i', 'attrs': ["text"], 'pattern': "**%s**"},
  '\_\_\((.*)\)\_\_': {'cls': 'page.ui.tags.b', 'attrs': ["text"], 'pattern': "__%s__"},
  '^## (.*)(.*)$': {'cls': 'page.ui.subtitle', 'attrs': ["text"], 'pattern': "## %s%s"},
  '^# (.*)(.*)$': {'cls': 'page.ui.title', 'attrs': ["text"], 'pattern': "# %s%s"},
  '^___$': {'cls': 'page.ui.layouts.hr', 'attrs': [], 'pattern': "___"},
}


PARAMS = {
  "text": {"type": "String", "Optional": True, "value": "The value to be displayed to the button."},
  "angle": {"type": "Integer", "value": "The rotation angle."},
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

  Attributes:
  ----------
  :param func: Function. A python function.
  """
  for arg in func.__code__.co_varnames:
    if arg == "self":
      continue

    if arg in PARAMS:
      required = "Required" if PARAMS[arg].get('Optional', True) else "Optional"
      print(":param %s: %s. %s. %s" % (arg, PARAMS[arg]["type"], required, PARAMS[arg]["value"]))
    else:
      print(":param %s:" % arg)


class MarkDown(object):

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
          map_objs["%s_%s" % (interface['cls'], count)] = "%s(%s)" % (interface['cls'], ", ".join(["%s=%s" % (k, json.dumps(v)) for k, v in attrs.items()]))
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

    Attributes:
    ----------
    :param data:
    :param css_attrs:
    """
    CLS_MAPPING = {
      '\[(.*)\]\((.*)\)': self.page.ui.link,
      '^## (.*)(.*)$': self.page.ui.subtitle,
      '^# (.*)(.*)$': self.page.ui.title,
    }
    convert_data = data
    count, map_objs = 0, {}
    for r, cls in RULES.items():
      m = re.findall(r, data, re.MULTILINE)
      if m is not None:
        for g in m:
          attrs = dict(zip(cls['attrs'], g))
          interface = CLS_MAPPING[r]
          map_objs["%s_%s" % (interface.__name__, count)] = interface(**attrs)
          if css_attrs is not None and map_objs["%s_%s" % (interface.__name__, count)].name in css_attrs:
            map_objs["%s_%s" % (interface.__name__, count)].css(css_attrs[map_objs["%s_%s" % (interface.__name__, count)].name])
          convert_data = convert_data.replace(cls['pattern'] % g, "||%s_%s||" % (interface.__name__, count))
          count += 1
    resolved_data = []
    for rec in convert_data.split("||"):
      resolved_data.append(map_objs.get(rec, rec))
    return resolved_data


# if __name__ == '__main__':
#   data = '''
# ![rgrhr](rhrhr)
# [rgrhr](rhrhr)
# # This is a title
# ___
# This is a text **with an extra** on this
#
# [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
# '''
#
#   trans_data = MarkDown.translate(data)
#   print(trans_data)
