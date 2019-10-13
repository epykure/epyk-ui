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

#
URL_w3c = r"https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic"
URL_CODEPEN = r"https://codepen.io/"
URL_JSFIDDLE = r"https://jsfiddle.net/"


def open_url(url):
  """
  Small utilities to open the browser to a specific web page.
  Some url are predefined and they are there to facilitate the testing of the generated Html pages

  :param url: A url

  """
  webbrowser.open(url)


def get_data(name):
  """
  Load the static files used to test the different function.
  Files can be json or txt file (with header and delimited with a ,)

  :param name: THe filename

  :return: A record (A list of dictionaries)
  """
  if name.endswith(".json"):
    return json.load(open(os.path.join(TESTS_PATH, "data", name)))

  records = []
  with open(os.path.join(TESTS_PATH, "data", name)) as file:
    header = file.readline().strip().split(",")
    for line in file:
      records.append(dict(zip(header, line.strip().split(","))))
  return records
