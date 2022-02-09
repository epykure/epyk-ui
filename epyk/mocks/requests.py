
from epyk.core.py import PyRest
from . import urls


def demo_country(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  return PyRest.PyRest.csv(urls.DEMO_COUNTRY, delimiter, encoding, with_header, store_location)
