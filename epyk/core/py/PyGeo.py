
from epyk.core.py import primitives
from math import cos, asin, sqrt, pi


class PyGeo:

  def __init__(self, page: primitives.PageModel = None):
    self.page = page

  @staticmethod
  def distance(lat1: float, lon1: float, lat2: float, lon2: float, unit: str = "km"):
    """ Calculate the great circle distance between two points on the earth (specified in decimal degrees)
    3956

    Related Pages:

      https://en.wikipedia.org/wiki/Haversine_formula

    :param lat1: Float.
    :param lon1: Float.
    :param lat2: Float.
    :param lon2: Float.
    :param unit: String. mi / km. Default km
    """
    p = pi / 180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 7912 * asin(sqrt(a)) if unit == 'mi' else 12742 * asin(sqrt(a))
