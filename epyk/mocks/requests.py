
from epyk.core.py import PyRest
from . import urls


def demo_country(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """

    [{'Country Name': 'Bangladesh', 'Country Code': 'BGD', 'Year': '2011', 'Value': '149273778'}
      ...]

  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.DEMO_COUNTRY, delimiter, encoding, with_header, store_location)


def demo_covid_cty(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.GEO_COVID19_COUNTRIES, delimiter, encoding, with_header, store_location)


def demo_airport_traffic(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.AIRPORT_TRAFFIC, delimiter, encoding, with_header, store_location)


def demo_banking_data(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.BANKING_DATA, delimiter, encoding, with_header, store_location)


def demo_netflix_title(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.NETFLIX_TITLE, delimiter, encoding, with_header, store_location)


def demo_co2(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.CO2_DATA, delimiter, encoding, with_header, store_location)


def demo_energy(delimiter: str = ",", encoding: str = 'utf-8', with_header: bool = True, store_location: str = None):
  """


  Usage::


  :param delimiter:
  :param encoding:
  :param with_header:
  :param store_location:
  :return:
  """
  return PyRest.PyRest.csv(urls.ENERGY_DATA, delimiter, encoding, with_header, store_location)
