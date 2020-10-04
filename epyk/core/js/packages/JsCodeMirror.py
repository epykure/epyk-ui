
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class CM(JsPackage):
  lib_alias = {"js": 'codemirror', 'css': 'codemirror'}
  lib_set_var = False

  def __init__(self, htmlObj, varName=None, setVar=False, report=None):
    super(CM, self).__init__(htmlObj, varName=varName, selector=htmlObj.editorId, data=None, setVar=setVar, parent=None)
    self._src, self._report = htmlObj, report

  def setSize(self, width=None, height=None):
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
    :param width: String or integer. The width of the component
    :param height: String or integer. The height of the component

    :return: The Javascript string fragment
    """
    width = JsUtils.jsConvertData(width, None)
    height = JsUtils.jsConvertData(height, None)
    return self.fnc_closure("setSize(%s, %s)" % (width, height))

  def scrollTo(self, x=None, y=None):
    """
    Description:
    -----------
    Scroll the editor to a given (pixel) position. Both arguments may be left as null or undefined to have no effect.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    Attributes:
    ----------
    :param x: Integer. The x position of the scrollbar
    :param y: Integer. The y position of the scrollbar

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

  def setOption(self, option, value):
    """
    Description:
    -----------
    Change the configuration of the editor.
    option should the name of an option, and value should be a valid value for that option.

    Related Pages:

      https://codemirror.net/doc/manual.html#option_viewportMargin

    Attributes:
    ----------
    :param option: String. The editor option name
    :param value: Object. The editor option value

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
    If your code does something to change the size of the editor element (window resizes are already listened for), or unhides it, you should probably follow up by calling this method to ensure CodeMirror is still looking as intended. See also the autorefresh addon.

    Related Pages:

      https://codemirror.net/doc/manual.html#api

    :return: The Javascript string fragment
    """
    return self.fnc_closure("refresh()")

  def execCommand(self, command):
    """
    Description:
    -----------
    Runs the command with the given name on the editor.

    Related Pages:

      https://codemirror.net/doc/manual.html#commands

    :return: The Javascript string fragment
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

    :return:
    """
    return self.fnc_closure("undo()")

  def redo(self):
    """
    Description:
    -----------

    :return:
    """
    return self.fnc_closure("redo()")
