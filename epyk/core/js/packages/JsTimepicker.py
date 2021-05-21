
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Timepicker(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def value(self, jsValue=None):
    """
    Description:
    ------------
    Set the timepicker object value

    Related Pages:

      https://stackoverflow.com/questions/32378842/setting-the-hour-and-minute-of-timepicker-dynamically

    Attributes:
    ----------
    :param jsValue: String or Js Object
    """
    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.timepicker("setTime", %s)' % (self._src.dom.jquery.varId, jsValue))

  def getTime(self):
    """
    Description:
    ------------
    Get the time using a Javascript Date object, relative to a Date object (default: today's date).

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('getTime')" % self._src.dom.jquery.varId)

  def getSecondsFromMidnight(self):
    """
    Description:
    ------------
    Get the time as an integer, expressed as seconds from 12am.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('getSecondsFromMidnight')" % self._src.dom.jquery.varId)

  def isVisible(self):
    """
    Description:
    ------------
    Check if the timepicker attached to a specific input is visible. Not compatible with the useSelect option.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('isVisible')" % self._src.dom.jquery.varId)

  def remove(self):
    """
    Description:
    ------------
    Unbind an existing timepicker element.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return JsObjects.JsObjects.get("%s.timepicker('remove')" % self._src.dom.jquery.varId)

  def option(self,  jsKey=None,  jsValue=None):
    """
    Description:
    ------------
    Change the settings of an existing timepicker.
    Calling option on a visible timepicker will cause the picker to be hidden.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param jsKey: String or Js Object
    :param jsValue: String or Js Object
    """
    jsKey = JsUtils.jsConvertData(jsKey, None)
    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get("%s.timepicker('option', %s, %s)" % (self._src.dom.jquery.varId, jsKey, jsValue))

  def setTime(self, jsValue=None):
    """
    Description:
    ------------
    Set the time using a Javascript Date object.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param jsValue: String or Js Object
    """
    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get("%s.timepicker('setTime', %s)" % (self._src.dom.jquery.varId, jsValue))

  def change(self, js_funcs, profile=None):
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
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('change', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def changeTime(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Called after a valid time value is entered or selected. See timeFormatError and timeRangeError for error events.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('changeTime', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def hideTimepicker(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Called after the timepicker is closed.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('hideTimepicker', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def selectTime(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Called after a time value is selected from the timepicker list. Fires before change event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('selectTime', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def showTimepicker(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Called after the timepicker is shown.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('showTimepicker', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def timeFormatError(self, js_funcs, profile=None):
    """
    Description:
    ------------
    Called if an unparseable time string is manually entered into the timepicker input. Fires before change event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('timeFormatError', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))

  def timeRangeError(self, js_funcs, profile=None):
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
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    return JsObjects.JsObjects.get("%s.on('timeRangeError', function() {%s})" % (self._src.dom.jquery.varId, js_funcs))
