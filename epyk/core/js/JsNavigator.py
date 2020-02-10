"""
https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_geolocation
"""

from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsBoolean


class JsGeolocation(object):
  """

  """
  def __init__(self, rptObj):
    self._rptObj = rptObj

  def getCurrentPosition(self, success, error, options ):
    """

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/Geolocation/getCurrentPosition

    :return:
    """

  def watchPosition(self):
    pass

  def clearWatch(self):
    pass


class JsNavigator(object):

  def __init__(self, rptObj):
    self._rptObj = rptObj

  @property
  def geolocation(self):
    """

    Documentation
    https://w3c.github.io/geolocation-api/#navi-geo
    """
    return JsGeolocation(self._rptObj)

  @property
  def language(self):
    """
    The language property returns the language version of the browser.

    Documentation
    https://www.w3schools.com/jsref/prop_nav_language.asp

    :return:
    """
    return JsString.JsString("navigator.language", isPyData=False)

  @property
  def browserLanguage(self):
    """
    The language property returns the language version of the browser.
    For IE10 and earlier versions, you can use the browserLanguage property

    Documentation
    https://www.w3schools.com/jsref/prop_nav_language.asp

    :return:
    """
    return JsString.JsString("navigator.browserLanguage", isPyData=False)

  @property
  def appCodeName(self):
    """
    """
    return JsString.JsString("navigator.appCodeName", isPyData=False)

  @property
  def appName(self):
    """
    """
    return JsString.JsString("navigator.appName", isPyData=False)

  @property
  def appVersion(self):
    """
    """
    return JsString.JsString("navigator.appVersion", isPyData=False)

  @property
  def cookieEnabled(self):
    """
    """
    return JsString.JsString("navigator.cookieEnabled", isPyData=False)

  @property
  def onLine(self):
    """
    """
    return JsString.JsString("navigator.onLine", isPyData=False)

  @property
  def platform(self):
    """
    """
    return JsString.JsString("navigator.platform", isPyData=False)

  @property
  def userAgent(self):
    """
    """
    return JsString.JsString("navigator.userAgent", isPyData=False)

  def javaEnabled(self):
    """
    The javaEnabled() method returns a Boolean value that specifies whether the browser has Java enabled.

    Documentation
    https://www.w3schools.com/jsref/met_nav_javaenabled.asp

    :return:
    """
    return JsBoolean.JsBoolean("navigator.javaEnabled()", isPyData=False)
