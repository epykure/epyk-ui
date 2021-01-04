#!/usr/bin/python
# -*- coding: utf-8 -*-


def indent(level=0, spaces=None):
  """
  Description:
  ------------
  Add the number of spaces according to the indent level.

  Usage:


  Attributes:
  ----------
  :param level: Integer. Optional. The level for the line indent.
  :param spaces: Integer. Optional. The number of spaces. (Default 2).
  """
  spaces = spaces or 2
  return "".join((level * spaces) * [" "])


def parse_statements(line, level, delimiter=";", spaces=None):
  """
  Description:
  ------------
  Parse and format a JavaScript line.

  Usage:


  Attributes:
  ----------
  :param line: String. The JavaScript statements.
  :param level: Integer. The level of indent to be added to this line.
  :param delimiter: String. Optional. The statement delimiter. Default ;.
  :param spaces: Integer. Optional. The number of spaces. (Default 2).
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


def parse(data, minify=None, toStr=True, spaces=None):
  """
  Description:
  ------------
  Parse and format a JavaScript string full statement.

  Usage:


  Attributes:
  ----------
  :param data: String. The Javascript statements.
  :param minify: Boolean. Optional. Specify the type of formatting. (Default minify True).
  :param toStr: Boolean. Optional. Specify the type of data returned by this function (string or list).
  :param spaces: Integer. Optional. The number of spaces. (Default 2).
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


def builder(cls, minify=None, toStr=True, spaces=None):
  """
  Description:
  ------------
  Extract the builder function from the HTML component.

  Usage:


  Attributes:
  ----------
  :param cls: Class. An internal HTML component class.
  :param minify: Boolean. Optional. Specify the type of formatting. (Default minify True).
  :param toStr: Boolean. Optional. Specify the type of data returned by this function (string or list).
  :param spaces: Integer. Optional. The number of spaces. (Default 2).
  """
  builder_name = cls.builder_name if cls.builder_name is not None else cls.__name__
  return parse("function %s(htmlObj, data, options){%s}" % (builder_name, cls._js__builder__), minify, toStr, spaces=spaces)


def events(component, minify=None, toStr=True, spaces=None):
  """
  Description:
  ------------
  Extract the JavaSscript events from an HTML component.

  Usage:

    but = page.ui.button()
    but.click([page.js.alert("test1"), page.js.alert("test2")])
    but.hover([page.js.alert("test3"), page.js.alert("test4")])

    results = JsLinter.events(but)

  Attributes:
  ----------
  :param component: HTML Component. An internal component in the framework.
  :param minify: Boolean. Optional. Specify the type of formatting. (Default minify True).
  :param toStr: Boolean. Optional. Specify the type of data returned by this function (string or list).
  :param spaces: Integer. Optional. The number of spaces. (Default 2).
  """
  results = []
  for event_type, fnc_details in component._browser_data.get('mouse', {}).items():
    for src, fnc_content in fnc_details.items():
      results.append(parse("function %s_%s(){%s}" % (component.htmlCode, event_type, ";".join(fnc_content['content'])), minify=minify, toStr=toStr, spaces=spaces))
  return "\n\n".join(results)
