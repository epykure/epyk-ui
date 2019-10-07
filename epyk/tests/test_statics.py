"""
Common module for all the static data used in the different tests
"""
import os
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
