"""
Python entry point for the different internal Python wrappers
"""

import sys
import importlib

from epyk.core.py import PyCrypto
from epyk.core.py import PyHash
from epyk.core.py import PyRest
from epyk.core.py import PyDates
from epyk.core.py import PyMarkdown

from epyk.core.js.Imports import requires

#
# http://www.web-source.net/symbols.htm#.XiyBZuBzw2w
ENTITY_MAP = {"é": "&#233;", "È": "&#200;", "à": "&agrave;"}


class PyExt(object):
  class __internal(object):
    _props = {}

  def __init__(self, report=None):
    self._report = report if report is not None else self.__internal()
    self.hash = PyHash.SipHash().hashId
    self.today = self.dates.today
    self.now = self.dates.now
    self.cob = self.dates.cob
    self.request = self.requests.request
    if not 'py' in self._report._props:
      self._report._props['py'] = {}

  @property
  def dates(self):
    """
    This is a simple wrapper to the datetime Python module.

    No external package is required to use this interface.
    :return: A PyDate object
    """
    return PyDates.PyDates(self._report)

  @property
  def requests(self):
    """
    This is a simple wrapper to the internal Python modules to run REST calls.

    No external package is required to use this interface.
    :return: A PyRest object
    """
    return PyRest.PyRest(self._report)

  @property
  def crypto(self):
    """
    Property to the internal cryptography module.

    This will rely on the package cryptography. This should be added to the python environment before using it.
    This package can be installed using the usual pip install function.

    Documentation
    https://pypi.org/project/cryptography/
    https://cryptography.io/en/latest/

    :return:
    """
    return PyCrypto.PyCrypto(self._report)

  @property
  def markdown(self):
    """ Property to the Markdown String conversion """
    return PyMarkdown.Convertor(self._report)

  def import_lib(self, lib_name, folder="libs", report_name=None, path=None):
    """
    Import dynamically a python module

    Example
    rptObj.py.import_lib("test.py", folder="tables", path=r"filePath")

    :param lib_name: The python module name
    :param folder: The internal folder with the libraries to be imported
    :param report_name: Optional, the report name in which the library is defined. Default current folder
    :param path: Optional, the path to be added to the classpath

    :return: The imported Python module
    """
    lib_name = lib_name.replace(".py", "")
    if path is not None:
      if path not in sys.path:
        sys.path.append(path)
      return importlib.import_module('%s.%s' % (folder, lib_name))

    else:
      if report_name is None:
        return importlib.import_module('%s.%s.%s' % (self._report.run.report_name, folder, lib_name))

      return importlib.import_module('%s.%s.%s' % (report_name, folder, lib_name))

  def import_package(self, package, sub_module=None):
    """
    Install the external Python package.
    This can automatically installed it from the Python Index online repository is missing

    Example
    >>> PyExt().import_package("sqlalchemy").__name__
    'sqlalchemy'

    :param package: The Python Package Name
    :param sub_module: The sub module or class within the package

    :return: The installed Python module
    """
    package_alias = "%s_%s" % (package, sub_module) if sub_module is not None else package
    if not package_alias in self._report._props:
      self._report._props[package_alias] = requires(package, reason='Missing Package', package=sub_module, install=package)
    return self._report._props[package_alias]

  def clean(self, text):
    """
    Replace the special characters by the corresponding HTML entities

    :param text:
    :return:
    """
    for c, t in ENTITY_MAP.items():
      if c in text:
        text = text.replace(c, t)
    return text
