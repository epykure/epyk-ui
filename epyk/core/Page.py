
import json
import collections
import time
import inspect

try:
  basestring
except NameError:
  basestring = str

from epyk.core.js import Imports
from epyk.interfaces import Interface
from epyk.core.css import themes
from epyk.core.css import Classes

from epyk.core import html
from epyk.core import js
from epyk.core import data
from epyk.core import auth

from epyk.core.html import symboles
from epyk.core.html import entities
from epyk.core.html import skins
from epyk.core.py import OrderedSet
from epyk.core.py import PyOuts
from epyk.core.py import PyExt

from epyk.web import apps


class JsProperties:

  def __init__(self, context):
    self._context = context

  @property
  def frgs(self):
    """
    Description:
    ------------
    Return the extra JavaScript function manually added.
    """
    return self._context["text"]

  def add_text(self, text):
    """
    Description:
    ------------
    Add JavaScript fragments from String.

    Attributes:
    ----------
    :param text: String. JavaScript fragments to be directly included to the page.
    """
    self._context["text"].append(text)

  def add_builders(self, builder_def):
    """
    Description:
    ------------
    This will use add or extend according to the builder_def type.

    Attributes:
    ----------
    :param builder_def: String. The builder definition.
    """
    if isinstance(builder_def, list):
      for builder in builder_def:
        self.add_builders(builder)
    else:
      if hasattr(builder_def, 'toStr'):
        self._context['builders'].append(builder_def.toStr())
      else:
        self._context['builders'].append(builder_def)

  def add_on_ready(self, builder_def):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param builder_def:
    """
    self._context['onReady'].add(builder_def)

  def add_constructor(self, name, content):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param content:
    """
    self._context['constructors'][name] = content

  def has_constructor(self, name):
    """

    :param name:
    """
    return name in self._context['constructors']


class CssProperties:

  def __init__(self, context):
    self._context = context

  @property
  def text(self):
    """
    Description:
    ------------
    Return the extra CSS styles manually added.
    """
    return "\n".join(self._context['css']["text"])

  def add_text(self, text):
    """
    Description:
    ------------
    Add CSS style from String.

    Attributes:
    ----------
    :param text: String. CSS Style to be directly included to the page.
    """
    self._context['css']["text"].append(text)

  def add_builders(self, builder_def):
    """
    Description:
    ------------
    This will use add or extend to the CSS JavaScript builders according to the builder_def type.

    Attributes:
    ----------
    :param builder_def: String. The builder definition.
    """
    if 'builders_css' not in self._context['js']:
      self._context['js']['builders_css'] = OrderedSet()
    if isinstance(builder_def, list):
      self._context['js']['builders_css'].extend(builder_def)
    else:
      self._context['js']['builders_css'].append(builder_def)

  def container_style(self, css):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. The CSS attributes to be applied.
    """
    self._context['css']['container'].update(css)

  def font_face(self, font_family, src, stretch="normal", style="normal", weight="normal"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param font_family: String. Required. Defines the name of the font.
    :param src: String. Required. Defines the URL(s) where the font should be downloaded from.
    :param stretch: String. Optional. Defines how the font should be stretched. Default value is "normal".
    :param style: String. Optional. Defines how the font should be styled. Default value is "normal".
    :param weight: String. Optional. Defines the boldness of the font. Default value is "normal".
    """
    self._context['css']["font-face"][font_family] = {
      'src': "url(%s)" % src, 'font-stretch': stretch, 'font-style': style, 'font-weight': weight}


class Properties:

  def __init__(self, context):
    self._context = context

  @property
  def js(self):
    """
    Description:
    ------------
    The JavaScript page properties.
    This will keep track of all the global functions used by the components.
    """
    return JsProperties(self._context['js'])

  @property
  def css(self):
    """
    Description:
    ------------
    The Css page properties.
    This will keep track of all the global functions used by the components.

    CSS Properties will work on both the CSS and JS section of the underlying prop dictionary.
    """
    return CssProperties(self._context)


class Report:
  """
  Main entry point for any web UI.

  This class will store all the HTML components, JavaScript fragments and CSS definition in order to then render
  a rich web page.

  This will allow Python to access the components before the JavaScript on the fly computation to change then
  according to the input data.

  This class will also interface with plain Vanilla JavaScript feature to allow the design and definition of events
  and / or interactions. Most of the Web documentation in this framework is either coming from w3School or from the
  various external packages.
  """
  showNavMenu, withContainer = False, False
  ext_packages = None    # For extension modules
  _node_modules = None    # Path for the external packages (default to the CDNJS is not available)

  def __init__(self, inputs=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param inputs: Dictionary. The global input data for the defined components in the page.
                               Passing data for a given component with an htmlCode will override the value.
    """
    self._css = {}
    self._ui, self._js, self._py, self._theme, self._auth, self.__body = None, None, None, None, None, None
    self._tags, self._header_obj, self.__import_manage = None, None, None
    self._props = {'js': {
          # JavaScript framework triggered after the HTML. Impact the entire page
          'onReady': OrderedSet(),
          'events': {},
          # Local worker sections
          'workers': {},
          # Static and generic builders
          'constructors': {},
          # Input data used in the various component (Page global variables)
          'datasets': {},
          # Global server configurations used for connection to the backend
          'configs': {},
          # Trigger the component generation using the Js Constructor
          'builders': OrderedSet(),
          'text': [],
        },
        # Used on the Python side to make some decisions
        'context': {'framework': 'JS'},
        # Add report font-face CSS definition
        'css': {
          "font-face": {},
          "container": {},
          "text": []}
    }
    # Components for the entire page
    self.components = collections.OrderedDict()
    self.start_time, self.inputs, self._propagate = time.time(), inputs or {}, []
    self._scroll, self._contextMenu, self.verbose, self.profile = set(), {}, False, False
    # to be reviewed
    self.logo, self._dbSettings, self.dbsDef = None, None, {}
    self.jsImports, self.jsLocalImports, self.cssImport, self.cssLocalImports = set(), set(), set(), set()

    # Section dedicated to load the static json configuration files
    frame_records = inspect.stack()[1]
    calling_module = inspect.getmodulename(frame_records[1])
    self.json_config_file = calling_module

  @property
  def properties(self):
    """
    Description:
    ------------
    Property to the different Page properties JavaScript and CSS.
    """
    return Properties(self._props)

  @property
  def body(self):
    """
    Description:
    ------------
    Property that returns the Body element of the HTML page.

    Usage::

      page = Report()
      page.body.onReady([
        page.js.alert("Loading started")
      ])

    :rtype: html.Html.Body
    """
    if self.__body is None:
      self.__body = html.Html.Body(self, None, html_code='body')
      self.__body.style.css.background = self.theme.greys[0]
      self.__body.style.css.color = self.theme.greys[-1]
    return self.__body

  @body.setter
  def body(self, calc):
    self.__body = calc(self, None)

  @property
  def theme(self):
    """
    Description:
    ------------
    Return the currently used :doc:`report/theme` for the report.

    Usage::

      page = Report()
      page.theme = themes.ThemeBlue.Blue

    :rtype: Theme.ThemeDefault
    """
    if self._theme is None:
      self._theme = themes.Theme.ThemeDefault()
    return self._theme

  @theme.setter
  def theme(self, theme):
    if isinstance(theme, dict):
      self._theme = themes.Theme.ThemeCustom()
      self._theme = theme
    else:
      self._theme = theme

  @property
  def themes(self):
    return themes.RegisteredThemes(self)

  @property
  def skins(self):
    """
    Description:
    ------------
    Add a special skin to the page.
    This could be used for special event or season during the year (Christmas for example).

    rtype: skins.Skins
    """
    return skins.Skins(self)

  def node_modules(self, path, alias=None, install=False, update=False):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param path: String. Optional.
    :param alias: String. Optional.
    :param install: Boolean. Optional.
    :param update: Boolean. Optional.
    """
    if path is not None:
      self._node_modules = (path, alias or path, install, update)

  @property
  def imports(self):
    """
    Description:
    ------------
    Return the :doc:`report/import_manager`, which allows to import automatically packages for certain components to
    run.
    By default the imports are retrieved online from CDNJS paths.

    This can be changed by loading the packages locally and switching off the online mode.

    Usage::

      page = Report()
      page.imports

    :rtype: Imports.ImportManager
    """
    if self.__import_manage is None:
      self.__import_manage = Imports.ImportManager(report=self)
    return self.__import_manage

  @property
  def symbols(self):
    """
    Description:
    ------------
    Shortcut to the HTML symbols.

    Those can be added in string in order to improve the render of a text.

    Usage::

      page = Report()
      page.ui.text(page.symbols.shapes.BLACK_SQUARE)

    Related Pages:

      https://www.w3schools.com/html/html_symbols.asp
      https://www.w3schools.com/charsets/ref_utf_math.asp

    :rtype: symboles.Symboles
    """
    return symboles.Symboles()

  @property
  def entities(self):
    """
    Description:
    ------------
    Shortcut to the HTML Entities.

    Those can be added in string in order to improve the render of a text.

    Usage::

      page = Report()
      page.ui.text(page.entities.non_breaking_space)

    Related Pages:

      https://www.w3schools.com/html/html_entities.asp
    """
    return entities.Entities()

  @property
  def ui(self):
    """
    Description:
    ------------
    User Interface section.

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...).

    Usage::

      page = Report()
      page.ui.text("This is a text")

    Related Pages:

      https://www.w3schools.com/html/default.asp

    :rtype: Interface.Components
    """
    return self.web.std

  @property
  def web(self):
    """
    Description:
    ------------
    User Interface section.

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...).

    Usage::

      page = Report()
      page.web

    Related Pages:

      https://www.w3schools.com/html/default.asp

    :rtype: Interface.WebComponents
    """
    if self._ui is None:
      self._ui = Interface.WebComponents(self)
    return self._ui

  @property
  def css(self):
    """
    Description:
    ------------
    Returns the set of :doc:`CSS Classes <css>` for the HTML report.

    Usage::

      page = Report()
      page.css.

    :rtyype: Classes.Catalog
    """
    cls_obj = Classes.Catalog(self, {'other': set()})
    cls_obj.other
    return cls_obj

  @property
  def js(self):
    """
    Description:
    ------------
    Go to the Javascript section. Property to get all the JavaScript features.
    Most of the standard modules will be available in order to add event and interaction to the Js transpiled.

    Usage::

      page = Report()
      page.js.console.log("test")

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :rtype: js.Js.JsBase

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
    Those are pre defined Python function to simplify the use of the various components.

    Usage::

      page = Report()
      page.py.dates.today()

    Related Pages:

      https://www.w3schools.com/js/default.asp

    :rtype: PyExt.PyExt

    :return: Python HTML object
    """
    if self._py is None:
      self._py = PyExt.PyExt(self)
    return self._py

  @property
  def auth(self):
    """
    Description:
    ------------
    Auth interface to allow easy sign-in pages.

    Usage::

      page = Report()
      page.auth.

    Related Pages:

      https://developers.google.com/identity/sign-in/web/sign-in

    :rtype: auth.Auth

    :return: Python Auth Object.
    """
    if self._auth is None:
      self._auth = auth.Auth(self)
    return self._auth

  @property
  def data(self):
    """
    Description:
    ------------
    Python internal data source management.

    This can be extended by inheriting from this epyk.core.data.DataSrc.DataSrc and adding extra entry points.

    Usage::

      page = Report()

    :return: The framework available data source

    :rtype: data.Data.DataSrc
    """
    return data.Data.DataSrc(self)

  def register(self, ext_components):
    """
    Description:
    ------------
    This function allows you to register external Components (namely coming from Pyk Reports)
    by registering them you this will engrave the object within your report.

    The example below will add obj1 and obj2 from an external pyk report previously required,
    then create a div and then add obj3 from an external file.

    Usage::

      page = Report()
      page.register([obj1, obj2])
      page.ui.div('this is a div')
      page.register(obj3)

    Attributes:
    ----------
    :param ext_components: List | HTML. The external components to be added.
    """
    if type(ext_components) != list:
      ext_components = [ext_components]

    for comp in ext_components:

      if comp.htmlCode in self.components:
        raise Exception("Duplicated Html Code %s in the script !" % comp.htmlCode)

      self.components[comp.htmlCode] = comp

  def get_components(self, html_codes):
    """
    Description:
    ------------
    retrieve the components based on their ID.
    This should be used when the htmlCode is defined for a component.

    Usage::

      page = Report()
      page.ui.button(htmlCode="Button")
      but = page.get_components(["Button"])

    Attributes:
    ----------
    :param html_codes: List | String. The reference of the HTML components loaded on the page.
    """
    if not isinstance(html_codes, list):
      return self.components[html_codes]

    return [self.components[html_code] for html_code in html_codes]

  def framework(self, name):
    """
    Description:
    ------------
    Flag to change the way code is transpiled in order to fit with the destination framework.

    By default the code transpiled will be used from a browser in plain Vanilla Js but this will be extended to then
    be compatible with other framework in order to simplify the path to production and the collaboration between teams.

    Many framework will be compatible like React, Angular, Vue but also some features will be exposed to Kotlin for
    mobile generation.

    This work is still in progress.

    Usage::

      page = Report()
      page.ui.text("This is an example")
      page.framework("Vue")

    Attributes:
    ----------
    :param name: String. The destination framework for the page.
    """
    self._props['context']['framework'] = name.upper()

  @property
  def outs(self):
    """
    Description:
    ------------
    Link to the possible output formats for a page.
    This will transpile the Python code to web artifacts. Those outputs are standard outputs files in web development.

    The property framework should be used to link to other web framework.

    Usage::

      page = Report()
      page.ui.text("This is an example")
      page.outs.html()
    """
    return PyOuts.PyOuts(self)

  @property
  def headers(self):
    """
    Description:
    ------------
    Property to the HTML page header.

    Usage::

      page = Report()
      page.headers.meta.viewport({"width": "device-width"})

    :rtype: html.Header.Header
    """
    if self._header_obj is None:
      self._header_obj = html.Header.Header(self)
    return self._header_obj

  def dumps(self, result):
    """
    Description:
    ------------
    Function used to dump the data before being sent to the Javascript layer.

    This function relies on json.dumps with a special encoder in order to work with Numpy array and Pandas data
    structures.

    As NaN is not valid on the Json side those object are not allowed during the dump.
    It is advised to use fillna() in your script before returning the data to the framework to avoid this issue.

    Usage::

      page = Report()
      page.dumps(result)

    Related Pages:

      https://docs.python.org/2/library/json.html

    Attributes:
    ----------
    :param result: Dictionary. The python dictionary or data structure.

    :return: The serialised data
    """
    return json.dumps(data, cls=js.JsEncoder.Encoder, allow_nan=False)

  @property
  def apps(self):
    """
    Description:
    ------------
    Change the report to a web application.

    This will add extra features available on the target framework.
    For example this HTML page can be transformed to an Angular app, a React App or a Vue one.

    Usage::

      page = Report()

    :rtype: apps.AppRoute
    """
    self._props['web'] = {
      'modules': {}
    }
    return apps.AppRoute(self)
