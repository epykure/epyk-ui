"""
Common module for all the static data used in the different tests
"""
import os
import json
import webbrowser

# Deduce the \outs folder based on this module path
# the \outs folder is excluded from Git
TESTS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATHS = r"%s\outs" % TESTS_PATH

# Extra static information with the links of the different external websites
URL_w3c = r"https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic"
URL_CODEPEN = r"https://codepen.io/"
URL_JSFIDDLE = r"https://jsfiddle.net/"

# Example files definition
MAP_COLS = {'flights.txt': {"distance": float, 'delay': float}}


def open_url(url):
  """
  Small utilities to open the browser to a specific web page.
  Some url are predefined and they are there to facilitate the testing of the generated Html pages

  :param url: A url

  """
  webbrowser.open(url)


def get_data(name, n=None, map_cols_type=None):
  """
  Load the static files used to test the different function.
  Files can be json or txt file (with header and delimited with a ,)

  :param name: THe filename
  :param n: Integer the max number of records
  :param map_cols_type: Dictionary. Special column type mapping

  :return: A record (A list of dictionaries)
  """
  if name.endswith(".json"):
    return json.load(open(os.path.join(TESTS_PATH, "data", name)))

  map_cols_type = map_cols_type or MAP_COLS.get(name, {})
  records = []
  with open(os.path.join(TESTS_PATH, "data", name)) as file:
    header = file.readline().strip().split(",")
    for i, line in enumerate(file):
      if n is not None and i > n:
        return records

      rec = dict(zip(header, line.strip().split(",")))
      for c, t in map_cols_type.items():
        rec[c] = t(rec[c])
      records.append(rec)
  return records
