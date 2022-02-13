
from typing import Union, Optional
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Timepicker(JsPackage):

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page=None):
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % component.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def value(self, value=None):
    """
    Description:
    ------------
    Set the timepicker object value

    Related Pages:

      https://stackoverflow.com/questions/32378842/setting-the-hour-and-minute-of-timepicker-dynamically

    Attributes:
    ----------
    :param value: String or Js Object
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get('%s.timepicker("setTime", %s)' % (self.component.dom.jquery.varId, value))

  def getTime(self):
    """
    Description:
    ------------
    Get the time using a Javascript Date object, relative to a Date object (default: today's date).

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('getTime')" % self.component.dom.jquery.varId)

  def getSecondsFromMidnight(self):
    """
    Description:
    ------------
    Get the time as an integer, expressed as seconds from 12am.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('getSecondsFromMidnight')" % self.component.dom.jquery.varId)

  def isVisible(self):
    """
    Description:
    ------------
    Check if the timepicker attached to a specific input is visible. Not compatible with the useSelect option.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('isVisible')" % self.component.dom.jquery.varId)

  def remove(self):
    """
    Description:
    ------------
    Unbind an existing timepicker element.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('remove')" % self.component.dom.jquery.varId)

  def option(self,  key=None,  value=None):
    """
    Description:
    ------------
    Change the settings of an existing timepicker.
    Calling option on a visible timepicker will cause the picker to be hidden.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param key: String or Js Object
    :param value: String or Js Object
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.timepicker('option', %s, %s)" % (self.component.dom.jquery.varId, key, value))

  def setTime(self, value=None):
    """
    Description:
    ------------
    Set the time using a Javascript Date object.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param value: String or Js Object
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.timepicker('setTime', %s)" % (self.component.dom.jquery.varId, value))

  def change(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    The native onChange event will fire any time the input value is updated, whether by selection from the timepicker
    list or manual entry into the text input.
    Your code should bind to change after initializing timepicker, or use event delegation.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('change', function() {%s})" % (self.component.dom.jquery.varId, js_funcs))

  def changeTime(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called after a valid time value is entered or selected. See timeFormatError and timeRangeError for error events.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('changeTime', function() {%s})" % (self.component.dom.jquery.varId, js_funcs))

  def hideTimepicker(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called after the timepicker is closed.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('hideTimepicker', function() {%s})" % (
      self.component.dom.jquery.varId, js_funcs))

  def selectTime(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called after a time value is selected from the timepicker list. Fires before change event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('selectTime', function() {%s})" % (self.component.dom.jquery.varId, js_funcs))

  def showTimepicker(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called after the timepicker is shown.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('showTimepicker', function() {%s})" % (
      self.component.dom.jquery.varId, js_funcs))

  def timeFormatError(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called if an unparseable time string is manually entered into the timepicker input. Fires before change event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('timeFormatError', function() {%s})" % (
      self.component.dom.jquery.varId, js_funcs))

  def timeRangeError(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Called if maxTime and minTime, or disableTimeRanges is set and an invalid time is manually entered into the
    timepicker input.

    Fires before change event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('timeRangeError', function() {%s})" % (
      self.component.dom.jquery.varId, js_funcs))
