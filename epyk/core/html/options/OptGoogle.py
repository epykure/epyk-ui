
from epyk.core.html.options import Options


class OptionMaps(Options):

  @property
  def zoom(self):
    """
    Description:
    ------------
    The starting value of the editor. Can be a string, or a document object.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(10)

  @zoom.setter
  def zoom(self, num):
    self._config(num)

  @property
  def center(self):
    """
    Description:
    ------------
    The starting value of the editor. Can be a string, or a document object.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get(None)

  @center.setter
  def center(self, point):
    if isinstance(point, tuple):
      self._config("new google.maps.LatLng(%s, %s)" % (point[0], point[1]))
    else:
      self._config("new google.maps.LatLng(%s)" % point)

  @property
  def mapTypeId(self):
    """
    Description:
    ------------
    The starting value of the editor. Can be a string, or a document object.

    Related Pages:

      https://codemirror.net/doc/manual.html#config
    """
    return self._config_get("google.maps.MapTypeId.ROADMAP")

  @mapTypeId.setter
  def mapTypeId(self, type_map):
    self._config("google.maps.MapTypeId.%s" % type_map.upper())
