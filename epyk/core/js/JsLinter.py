#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from epyk.core.py import primitives


def indent(level: int = 0, spaces: Optional[int] = None):
    """  Add the number of spaces according to the indent level.

    :param level: Optional. The level for the line indent
    :param spaces: Optional. The number of spaces. (Default 2)
    """
    spaces = spaces or 2
    return "".join((level * spaces) * [" "])


def parse_statements(content: str, level: int, delimiter: str = ";", spaces: Optional[int] = None):
    """  Parse and format a JavaScript line.

    :param content: The JavaScript statements
    :param level: The level of indent to be added to this line
    :param delimiter: Optional. The statement delimiter. Default ;
    :param spaces: Optional. The number of spaces. (Default 2)
    """
    row = []
    one_liner = "".join([line.strip() for line in content.split("\n")])
    split_line = one_liner.split(delimiter)
    for i, l in enumerate(split_line):
        r = l.strip()
        if r:
            if r == "{" or r == "}" or i == len(split_line) - 1:
                row.append("%s%s" % (indent(level, spaces=spaces), r))
            else:
                row.append("%s%s;" % (indent(level, spaces=spaces), r))
    return row


def parse(data: str, minify: Optional[bool] = None, to_str: bool = True, spaces: Optional[int] = None) -> str:
    """Parse and format a JavaScript string full statement.

    :param data: The Javascript statements
    :param minify: Optional. Specify the type of formatting. (Default minify True)
    :param to_str: Optional. Specify the type of data returned by this function (string or list)
    :param spaces: Optional. The number of spaces. (Default 2)
    """
    if not data:
        return ""

    level, frags, k = 0, [], 0
    if minify:
        for line in data.split("\n"):
            frags.append(line.strip())
        return "".join(frags)

    openings = data.split("{")
    for i, opening in enumerate(openings):
        closings = opening.split("}")
        if i > 0:
            level += 1
        for j, closing in enumerate(closings):
            if i > 0 and i != k:
                k = i
                frags.extend(parse_statements("{", level - 1, spaces=spaces))
                #level += 1
            #elif len(closing) == 0 or (len(closing) == 1 and closing[0] == ""):
            #  print(parse_statements("}", level-1))
            #  level -= 1
            if closing:
                frags.extend(parse_statements(closing, level, spaces=spaces))
            #if j > 0:
            #  level -= 1
            #if i > 0 and len(closings) > 1 and i != k:
            if i > 0 and j < len(closings) - 1:
                level -= 1
                frags.extend(parse_statements("}", level, spaces=spaces))
    return "\n".join(frags) if to_str else frags


def builder(cls, minify: Optional[bool] = None, to_str: bool = True, spaces: Optional[int] = None):
    """Extract the builder function from the HTML component.

    :param cls: Class. An internal HTML component class
    :param minify: Optional. Specify the type of formatting. (Default minify True)
    :param to_str: Optional. Specify the type of data returned by this function (string or list)
    :param spaces: Optional. The number of spaces. (Default 2)
    """
    builder_name = cls.builder_name if cls.builder_name is not None else cls.__name__
    return parse(
        "function %s(htmlObj, data, options){%s}" % (builder_name, cls._js__builder__), minify, to_str, spaces=spaces)


def events(component: primitives.HtmlModel, minify: Optional[bool] = None, to_str: bool = True,
           spaces: Optional[int] = None) -> str:
    """Extract the JavaScript events from an HTML component.

    Usage::

      but = page.ui.button()
      but.click([page.js.alert("test1"), page.js.alert("test2")])
      but.hover([page.js.alert("test3"), page.js.alert("test4")])

      results = JsLinter.events(but)

    :param component: An internal component in the framework
    :param minify: Optional. Specify the type of formatting. (Default minify True)
    :param to_str: Optional. Specify the type of data returned by this function (string or list)
    :param spaces: Optional. The number of spaces. (Default 2)
    """
    results = []
    for event_type, fnc_details in component._browser_data.get('mouse', {}).items():
        for src, fnc_content in fnc_details.items():
            results.append(parse(
                "function %s_%s(){%s}" % (component.html_code, event_type, ";".join(fnc_content['content'])),
                minify=minify,
                to_str=to_str, spaces=spaces))
    return "\n\n".join(results)
