#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Any
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class CM(JsPackage):
  lib_alias = {"js": 'codemirror', 'css': 'codemirror'}
  lib_set_var = False

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = False,
               page: primitives.PageModel = None):
    super(CM, self).__init__(
      component=component, js_code=js_code, selector=component.editorId, data=None, set_var=set_var, page=page)

  def setSize(self, width: Union[tuple, int, primitives.JsDataModel] = None,
              height: Union[tuple, int, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Programmatically set the size of the editor (overriding the applicable CSS rules).
    width and height can be either numbers (interpreted as pixels) or CSS units ("100%", for example).
    You can pass null for either of them to indicate that that dimension should not be changed.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    Attributes:
    ----------
    :param Union[tuple, int, primitives.JsDataModel] width: The width of the component.
    :param Union[tuple, int, primitives.JsDataModel] height: The height of the component.

    :return: The Javascript string fragment
    """
    width = JsUtils.jsConvertData(width, None)
    height = JsUtils.jsConvertData(height, None)
    return self.fnc_closure("setSize(%s, %s)" % (width, height))

  def scrollTo(self, x: int = None, y: int = None):
    """
    Description:
    -----------
    Scroll the editor to a given (pixel) position. Both arguments may be left as null or undefined to have no effect.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    Attributes:
    ----------
    :param int x: The x position of the scrollbar.
    :param int y: The y position of the scrollbar.

    :return: The Javascript string fragment
    """
    return self.fnc_closure("scrollTo(%s, %s)" % (x, y))

  def hasFocus(self):
    """
    Description:
    -----------
    Tells you whether the editor currently has focus.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    :return: A Boolean
    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.hasFocus()" % self.varId)

  def setOption(self, option: Union[dict, primitives.JsDataModel], value: Any):
    """
    Description:
    -----------
    Change the configuration of the editor.
    option should the name of an option, and value should be a valid value for that option.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    Attributes:
    ----------
    :param Union[dict, primitives.JsDataModel] option: The editor option name.
    :param Any value: The editor option value

    :return: The Javascript string fragment
    """
    option = JsUtils.jsConvertData(option, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.setOption(%s, %s)" % (self.varId, option, value))

  def getOption(self):
    """
    Description:
    -----------
    Retrieves the current value of the given option for this editor instance.

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :return: The Javascript object
    """
    return JsObjects.JsObjects.get("%s.getOption()" % self.varId)

  def refresh(self):
    """
    Description:
    -----------
    If your code does something to change the size of the editor element (window resizes are already listened for),
    or unhides it, you should probably follow up by calling this method to ensure CodeMirror is still looking as
    intended. See also the autorefresh addon.

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :return: The Javascript string fragment
    """
    return self.fnc_closure("refresh()")

  def execCommand(self, command: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Runs the command with the given name on the editor.

    Related Pages:

      https://codemirror.net/doc/manual.html#commands

    :return: The Javascript string fragment

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] command:
    """
    command = JsUtils.jsConvertData(command, None)
    return self.fnc_closure("execCommand(%s)" % command)

  def focus(self):
    """
    Description:
    -----------
    Give the editor focus.

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :return: The Javascript string fragment
    """
    return self.fnc_closure("focus()")

  def undo(self):
    """
    Description:
    -----------

    """
    return self.fnc_closure("undo()")

  def redo(self):
    """
    Description:
    -----------

    """
    return self.fnc_closure("redo()")
