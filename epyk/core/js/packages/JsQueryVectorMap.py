
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class _Export:

  @property
  def region(self):
    """

    """
    return JsObjects.JsString.JsString.get("region")

  @property
  def code(self):
    """

    """
    return JsObjects.JsString.JsString.get("code")

  @property
  def element(self):
    """

    """
    return JsObjects.JsString.JsString.get("element")


class JQVMap(JsPackage):

  lib_alias = {"js": 'jqvmap', 'css': 'jqvmap'}
  lib_set_var = False

  def zoomIn(self):
    """   Zoom one step in.

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('zoomIn')" % self.varName)

  def zoomOut(self):
    """   Zoom one step out.

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('zoomOut')" % self.varName)

  def getPin(self, alias):
    """   Returns the html attribute "id" of the pin placed on the country whose country code is provided in "cc".

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('getPin', %s)" % (self.varName, JsUtils.jsConvertData(alias, None)))

  def removePin(self, alias):
    """   Removes the pin from the country whose country code is specified in "cc".

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('getPin', %s)" % (self.varName, JsUtils.jsConvertData(alias, None)))

  def getPins(self):
    """   Returns an associative JSON string containing stringified HTML of all the pins.

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('getPins')" % self.varName)

  def removePins(self):
    """   Removes all the pins from the map.

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/
    """
    return JsUtils.jsWrap("%s.vectorMap('removePins')" % self.varName)

  def set(self, key, value):
    """

    :param key:
    :param value:
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.vectorMap('set', %s, %s)" % (self.varName, key, value))
