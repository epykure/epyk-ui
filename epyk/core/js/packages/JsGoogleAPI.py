
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class TravelMode():
  pass


class DirectionsStatus():
  pass


class DirectionsService():
  pass


class DirectionsRenderer():
  pass


class Marker():

  @property
  def id(self):
    """
    """
    return self._config_get(10)

  @id.setter
  def id(self, num):
    self._config(num)

  @property
  def html(self):
    """
    """
    return self._config_get(10)

  @html.setter
  def html(self, num):
    self._config(num)


class GoogleMapsAPI(JsPackage):
  lib_alias = {'js': 'google-maps'}
  lib_set_var = False

  def marker(self, latitude, longitude):
    """

    :param latitude:
    :param longitude:
    """
    Marker({"lat": latitude, 'lng': longitude})
    return

  def setMapTypeId(self, mapTypeId):
    """

    https://developers.google.com/maps/documentation/javascript/maptypes

    :param mapTypeId:
    """
    mapTypeId = JsUtils.jsConvertData(mapTypeId, None)
    return JsObjects.JsVoid("%s.setMapTypeId(%s)" % (self.varId, mapTypeId))

  def setTilt(self, value):
    """
    https://developers.google.com/maps/documentation/javascript/maptypes

    :param value:
    :return:
    """
    return JsObjects.JsVoid("%s.setTilt(%s)" % (self.varId, value))

  def getTile(self, value):
    """
    is called whenever the API determines that the map needs to display new tiles for the given viewport.
    The getTile() method must have the following signature:

    https://developers.google.com/maps/documentation/javascript/maptypes

    :param value:
    :return:
    """
    return JsObjects.JsVoid("%s.getTile(%s)" % (self.varId, value))

  def setHeading(self, value):
    """
    https://developers.google.com/maps/documentation/javascript/maptypes

    :param value:
    :return:
    """
    return JsObjects.JsVoid("%s.setHeading(%s)" % (self.varId, value))

  def getHeading(self):
    """

    https://developers.google.com/maps/documentation/javascript/maptypes

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.getHeading()" % self.varId)
