#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from epyk.core.py import primitives


def indent(level: int = 0, spaces: Optional[int] = None):
  """
  Description:
  ------------
  Add the number of spaces according to the indent level.

  Attributes:
  ----------
  :param int level: Optional. The level for the line indent.
  :param Optional[int] spaces: Optional. The number of spaces. (Default 2).
  """
  spaces = spaces or 2
  return "".join((level * spaces) * [" "])


def parse_statements(line: str, level: int, delimiter: str = ";", spaces: Optional[int] = None):
  """
  Description:
  ------------
  Parse and format a JavaScript line.

  Attributes:
  ----------
  :param str line: The JavaScript statements.
  :param int level: The level of indent to be added to this line.
  :param str delimiter: Optional. The statement delimiter. Default ;.
  :param Optional[int] spaces: Optional. The number of spaces. (Default 2).
  """
  row = []
  one_liner = "".join([l.strip() for l in line.split("\n")])
  split_line = one_liner.split(delimiter)
  for i, l in enumerate(split_line):
    r = l.strip()
    if r:
      if r == "{" or r == "}" or i == len(split_line)-1:
        row.append("%s%s" % (indent(level, spaces=spaces), r))
      else:
        row.append("%s%s;" % (indent(level, spaces=spaces), r))
  return row


def parse(data: str, minify: Optional[bool] = None, toStr: bool = True, spaces: Optional[int] = None):
  """
  Description:
  ------------
  Parse and format a JavaScript string full statement.

  Attributes:
  ----------
  :param str data: The Javascript statements.
  :param Optional[bool] minify: Optional. Specify the type of formatting. (Default minify True).
  :param bool toStr: Optional. Specify the type of data returned by this function (string or list).
  :param Optional[int] spaces: Optional. The number of spaces. (Default 2).
  """
  level, frgs, k = 0, [], 0
  if minify:
    for l in data.split("\n"):
      frgs.append(l.strip())
    return "".join(frgs)

  openings = data.split("{")
  for i, opening in enumerate(openings):
    closings = opening.split("}")
    if i > 0:
      level += 1
    for j, closing in enumerate(closings):
      if i > 0 and i != k:
        k = i
        frgs.extend(parse_statements("{", level-1, spaces=spaces))
        #level += 1
      #elif len(closing) == 0 or (len(closing) == 1 and closing[0] == ""):
      #  print(parse_statements("}", level-1))
      #  level -= 1
      if closing:
        frgs.extend(parse_statements(closing, level, spaces=spaces))
      #if j > 0:
      #  level -= 1
      #if i > 0 and len(closings) > 1 and i != k:
      if i > 0 and j < len(closings)-1:
        level -= 1
        frgs.extend(parse_statements("}", level, spaces=spaces))
  return "\n".join(frgs) if toStr else frgs


def builder(cls, minify: Optional[bool] = None, toStr: bool = True, spaces: Optional[int] = None):
  """
  Description:
  ------------
  Extract the builder function from the HTML component.

  Attributes:
  ----------
  :param cls: Class. An internal HTML component class.
  :param Optional[bool] minify: Optional. Specify the type of formatting. (Default minify True).
  :param bool toStr: Optional. Specify the type of data returned by this function (string or list).
  :param Optional[int] spaces: Optional. The number of spaces. (Default 2).
  """
  builder_name = cls.builder_name if cls.builder_name is not None else cls.__name__
  return parse(
    "function %s(htmlObj, data, options){%s}" % (builder_name, cls._js__builder__), minify, toStr, spaces=spaces)


def events(component: primitives.HtmlModel, minify: Optional[bool] = None, toStr: bool = True, spaces: Optional[int] = None) -> str:
  """
  Description:
  ------------
  Extract the JavaScript events from an HTML component.

  Usage::

    but = page.ui.button()
    but.click([page.js.alert("test1"), page.js.alert("test2")])
    but.hover([page.js.alert("test3"), page.js.alert("test4")])

    results = JsLinter.events(but)

  Attributes:
  ----------
  :param primitives.HtmlModel component: An internal component in the framework.
  :param Optional[bool] minify: Optional. Specify the type of formatting. (Default minify True).
  :param bool toStr: Optional. Specify the type of data returned by this function (string or list).
  :param Optional[int] spaces: Optional. The number of spaces. (Default 2).
  """
  results = []
  for event_type, fnc_details in component._browser_data.get('mouse', {}).items():
    for src, fnc_content in fnc_details.items():
      results.append(parse(
        "function %s_%s(){%s}" % (
          component.htmlCode, event_type, ";".join(fnc_content['content'])), minify=minify, toStr=toStr, spaces=spaces))
  return "\n\n".join(results)
