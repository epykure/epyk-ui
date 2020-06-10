
import json
import collections
import time

try:
  basestring
except NameError:
  basestring = str

from epyk.core.js import Imports
from epyk.interfaces import Components
from epyk.core.css.themes import Theme
from epyk.core.css import Classes

from epyk.core import html
from epyk.core import js
from epyk.core import data

from epyk.core.html import symboles
from epyk.core.html import entities
from epyk.core.py import OrderedSet
from epyk.core.py import PyOuts
from epyk.core.py import PyExt


class Report(object):
  showNavMenu, withContainer = False, False
  ext_packages = None # For extension modules

  def __init__(self, inputs=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param inputs: Dictionary. The global input data for the defined components in the page.
                               Passing data for a given component with an htmlCode will override the value.
    """
    self._css, self._ui, self._js, self._py, self._theme, self.__body = {}, None, None, None, None, None
    self._tags, self._header_obj, self.__import_manage = None, None, None
    self._props = {'js': {'onReady': OrderedSet(), 'events': {}, 'datasets': {}, 'builders': OrderedSet()},
                   'context': {'framework': 'JS'}}
    self.components = collections.OrderedDict() # Components for the entire page
    self.start_time, self.inputs, self._propagate = time.time(), inputs or {}, []
    self._scroll, self._contextMenu = set(), {}
    self.logo, self._dbSettings, self.dbsDef, self._cssText, self._jsText = None, None, {}, [], [] # to be reviewed

    self.jsImports, self.jsLocalImports, self.cssImport, self.cssLocalImports = set(), set(), set(), set()

  @property
  def body(self):
    """
    Description:
    ------------
    Property that returns the Body element of the HTML page
    """
    if self.__body is None:
      self.__body = html.Html.Body(self, None, htmlCode='body')
    return self.__body

  @body.setter
  def body(self, calc):
    self.__body = calc(self, None)

  @property
  def theme(self):
    """
    Description:
    ------------
    Return the currently used :doc:`report/theme` for the report
    """
    if self._theme is None:
      self._theme = Theme.ThemeDefault()
    return self._theme

  @theme.setter
  def theme(self, theme):
    if isinstance(theme, dict):
      self._theme = Theme.ThemeCustome()
      self._theme = theme
    else:
      self._theme = theme

  def imports(self, online=False):
    """
    Description:
    ------------
    Return the :doc:`report/import_manager`, which allows to import automatically packages for certain components to run.
    """
    if self.__import_manage is None:
      self.__import_manage = Imports.ImportManager(online, report=self)
    return self.__import_manage

  @property
  def symbols(self):
    """
    Description:
    ------------
    Shortcut to the HTML symbols

    Related Pages:

      https://www.w3schools.com/html/html_symbols.asp
      https://www.w3schools.com/charsets/ref_utf_math.asp

    Those can be added in string in order to improve the render of a text.
    """
    return symboles.Symboles()

  @property
  def entities(self):
    """
    Description:
    ------------
    Shortcut to the HTML Entities

    Related Pages:

      https://www.w3schools.com/html/html_entities.asp

    Those can be added in string in order to improve the render of a text.
    """
    return entities.Entities()

  @property
  def ui(self):
    """
    Description:
    ------------
    User Interface section.

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...)

    Related Pages:

	    https://www.w3schools.com/html/default.asp

    :rtype: :doc:`Components.Components <report/ui>`

    :return: Python HTML object
    """
    if self._ui is None:
      self._ui = Components.Components(self)
    return self._ui

  @property
  def css(self):
    """
    Returns the set of :doc:`CSS Classes <css>` for the HTML report
    """
    return Classes.Catalog(self, {'other': set()})._class_type('other')

  @property
  def js(self):
    """
    Description:
    ------------
    Go to the Javascript section. Property to get all the JavaScript features.
    Most of the standard modules will be available in order to add event and interaction to the Js transpiled

    Usage::

      js.console.log("test")

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._js is None:
      self._js = js.Js.JsBase(self)
    return self._js

  @property
  def py(self):
    """
    Description:
    ------------
    Python external module section.

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :return: Python HTML object
    """
    if self._py is None:
      self._py = PyExt.PyExt(self)
    return self._py

  @property
  def data(self):
    """
    Description:
    ------------
    Python internal data source management

    This can be extended by inheriting from this epyk.core.data.DataSrc.DataSrc
    and adding extra entry points

    :return: The framework available data source
    """
    return data.Data.DataSrc(self)

  def register(self, ext_components):
    """
    Description:
    ------------

      This function allows you to register external epyk objects (namely coming from Pyk Reports)
      by registering them you this will engrave the object within your report
      The example below will add obj1 and obj2 from an external pyk report previously required,
      then create a div and then add obj3 from an external file

    Usage:
    ------

      rptObj.register([obj1, obj2])
      rptObj.ui.div('this is a div')
      rptObj.register(obj3)
    """
    if type(ext_components) != list:
      ext_components = [ext_components]

    for comp in ext_components:

      if comp.htmlCode in self.components:
        raise Exception("Duplicated Html Code %s in the script !" % comp.htmlCode)

      self.components[comp.htmlCode] = comp

  def get_components(self, htmlcodes):
    """
    Description:
    ------------
    retrieve the components based on their ID.
    This should be used when the htmlCode is defined for a component.

    Attributes:
    ----------
    :param htmlcodes:
    """
    if not isinstance(htmlcodes, list):
      return self.components[htmlcodes]

    return [self.components[htmlcode] for htmlcode in htmlcodes]

  def framework(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    self._props['context']['framework'] = name.upper()

  @property
  def outs(self):
    """
    Description:
    ------------

    """
    return PyOuts.PyOuts(self)

  @property
  def headers(self):
    """
    Property to the HTML page header
    """
    if self._header_obj is None:
      self._header_obj = html.Header.Header(self)
    return self._header_obj

  def dumps(self, data):
    """
    Description:
    ------------
    Function used to dump the data before being sent to the Javascript layer
    This function relies on json.dumps with a special encoder in order to work with Numpy array and Pandas data structures.

    As NaN is not valid on the Json side those object are not allowed during the dump.
    It is advised to use fillna() in your script before returning the data to the framework to avoid this issue.

    Example::

      report.dumps(result)

    Related Pages:

			https://docs.python.org/2/library/json.html

    Attributes:
    ----------
    :param data: The python dictionary or data structure

    :return: The serialised data
    """
    return json.dumps(data, cls=js.JsEncoder.Encoder, allow_nan=False)
