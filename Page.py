
import logging
import json
import collections
import time
import inspect
from typing import Union, Optional

try:
  basestring
except NameError:
  basestring = str

from epyk.core.js import Imports
from epyk.interfaces import Interface
from epyk.core.css import themes
from epyk.core.css import Classes
from epyk.core.css import Icons

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
    """ Return the extra JavaScript function manually added. """
    return self._context["text"]

  @property
  def constructors(self):
    """ Get the list of needed contractors """
    return self._context['constructors'].keys()

  @property
  def functions(self):
    """ Get the list of needed javasScript functions """
    return self._context['functions'].keys()

  def add_text(self, text: str):
    """
    Add JavaScript fragments from String.

    Usage::

      page = pk.Page()
      page.properties.js.add_text('''alert(new Date())''')
      page.outs.html_file(name="test", print_paths=True)

    :param text: JavaScript fragments to be directly included to the page
    """
    self._context["text"].append(text)

  def add_event(self, event: str, value):
    """
    Add JavaScript fragments from String.

    :param event: JavaScript fragments to be directly included to the page
    :param value:
    """
    self._context["events"][event] = value

  def add_builders(self, builder_def: str, func_dsc: str = None):
    """
    This will use add or extend according to the builder_def type.

    #TODO implement func_dsc

    :param builder_def: The builder definition.
    :param func_dsc:
    """
    if isinstance(builder_def, list):
      for builder in builder_def:
        self.add_builders(builder)
    else:
      if hasattr(builder_def, 'toStr'):
        self._context['builders'].append(builder_def.toStr())
      else:
        self._context['builders'].append(builder_def)

  def add_on_ready(self, builder_def: str):
    """
    Add JavaScript expression in the onReady selection of the HTML page.

    Usage::

      page = pk.Page()
      page.properties.js.add_on_ready("alert('Hello World!')")
      page.outs.html_file(name="test", print_paths=True)

    :param builder_def: The builder definition function
    """
    self._context['onReady'].add(builder_def)

  def add_constructor(self, name: str, content: str, override: bool = False, verbose: bool = False) -> str:
    """
    Register the constructor function and return its reference.

    :param name: The constructor name
    :param content: The entire definition
    :param override: Override the method if already defined if set to true
    :param verbose: Display extra messages if set to true
    """
    if not override and name in self._context['constructors']:
      if verbose:
        logging.warning("[add_constructor] Function %s already defined" % name)
      return name

    self._context['constructors'][name] = content
    return name

  def has_constructor(self, name: str):
    """
    Check if a constructor is already defined.

    :param name: The constructor name
    """
    return name in self._context['constructors']

  def get_constructor(self, name: str):
    """ Get the constructor definition. """
    return self._context['constructors'].get(name)

  def set_constructor(self, name: str, content: str = None, func_ref: bool = False):
    """
    Set a constructor.

    Usage::

      page = pk.Page()
      page.properties.js.set_constructor("Button", "htmlObj.innerHTML = 'Test'")
      btn = page.ui.button("click")
      btn.click([btn.build("Clicked")])

    :param name: The constructor alias (must of the same name than the function)
    :param content: The constructor expression in JavaScript
    :param func_ref:
    """
    if content is None:
      self._context['constructors'][name] = None
    elif not content.startswith("function ") and not func_ref:
      self._context['constructors'][name] = "function %s(htmlObj, data, options){%s}" % (name, content)
    else:
      self._context['constructors'][name] = content

  def add_function(self, name: str, js_funcs: Union[list, str], pmts: list) -> dict:
    """
    Add a JavaScript function to the page.

    This method will build the JavaScript method and it will be in charge during the conversion to JavaScript to
    write function [name] ( [pmts] ){ [js_funcs] }

    Usage::

      page = pk.Page()
      page.properties.js.add_function("testJs", "alert('Hello ' + name)", ["name='world'"])
      btn = page.ui.button("click")
      btn.click(["testJs('click')"])
      page.outs.html_file(name="test", print_paths=True)

    :param name: The function name
    :param js_funcs: The function definition (JavaScript expression)
    :param pmts: The function's parameters
    """
    self._context['functions'][name] = {'content': js_funcs, 'pmt': pmts}
    return self._context['functions'][name]

  def get_function(self, name: str) -> str:
    """ Get an existing function definition. """
    if name in self._context['functions']:
      func = self._context['functions'][name]
      return "function %s(%s){%s}" % (name, ", ".join(func['pmt']), func['content'])


class CssProperties:

  def __init__(self, context):
    self._context = context

  @property
  def text(self) -> str:
    """ Return the extra CSS styles manually added. """
    return "\n".join(self._context['css']["text"])

  def add_text(self, text: str):
    """ Add CSS style from String.

    Usage::

      page = pk.Page()
      page.properties.css.add_text('''.redCls {color: red}''')
      text = page.ui.text("Hello World !")
      text.style.add_class("redCls")
      page.outs.html_file(name="test", print_paths=True)

    :param text: CSS Style to be directly included to the page
    """
    self._context['css']["text"].append(text)

  def add_builders(self, builder_def: str):
    """ This will use add or extend to the CSS JavaScript builders according to the builder_def type.

    :param builder_def: The builder definition.
    """
    if 'builders_css' not in self._context['js']:
      self._context['js']['builders_css'] = OrderedSet()
    if isinstance(builder_def, list):
      self._context['js']['builders_css'].extend(builder_def)
    else:
      self._context['js']['builders_css'].append(builder_def)

  def container_style(self, css: dict):
    """ Set the container CSS style.

    :param css: The CSS attributes to be applied.
    """
    self._context['css']['container'].update(css)

  def font_face(self, font_family: str, src, stretch: str = "normal", style: str = "normal", weight: str = "normal"):
    """ Set the font.

    :param font_family: Defines the name of the font
    :param src: Defines the URL(s) where the font should be downloaded from
    :param stretch: Optional. Defines how the font should be stretched. Default value is "normal"
    :param style: Optional. Defines how the font should be styled. Default value is "normal"
    :param weight: Optional. Defines the boldness of the font. Default value is "normal"
    """
    self._context['css']["font-face"][font_family] = {
      'src': "url(%s)" % src, 'font-stretch': stretch, 'font-style': style, 'font-weight': weight}


class Properties:

  def __init__(self, context):
    self._context = context

  @property
  def context(self):
    """ Return the common Page context. """
    return self._context['context']

  @property
  def icon(self):
    """ Return the page icons definition. """
    return self._context['icon']

  @property
  def js(self) -> JsProperties:
    """
    The JavaScript page properties.

    This will keep track of all the global functions used by the components.
    """
    return JsProperties(self._context['js'])

  @property
  def css(self) -> CssProperties:
    """ The Css page properties.

    This will keep track of all the global functions used by the components.
    CSS Properties will work on both the CSS and JS section of the underlying prop dictionary.
    """
    return CssProperties(self._context)

  @property
  def data(self) -> data.DataProperties:
    """ Get the predefined data structures.

    Those data structures are mainly helper to input the different libraries available in this UI framework.
    """
    if "data" in self._context:
      self._context["data"] = {"sources": {}, "schema": {}}
    return data.DataProperties(self._context["data"])

  def to_json(self):
    return self._context


class Report:
  """ Main entry point for any web UI.

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

  def __init__(self, inputs: dict = None, script: str = None):
    """ Create a Report object.

    This is the starting point for any web resource.
    This interface will create a generic ui schema which will be then converted.
    For the moment only few output formats are available and web UI are preferred.

    The target of this components is not to replaced libraries but only to easy the use of the most popular ones without
    having to change languages, This module will help with the versioning, the interactivity and the documentation.

    Indeed libraries interfaces will point to the real documentation to allow you to learn by using it.

    Usage::

      import epyk as pk
      page = pk.Page()
      page.ui.text("Hello World !")
      page.outs.html_file(name="test", print_paths=True)

    :param inputs: Optional. The global input data for the defined components in the page.
      Passing data for a given component with an htmlCode will override the value.
    :param script: Optional. The origin script for building the page (for investigation purposes)
    """
    self._css = {}
    self._ui, self._js, self._py, self._theme, self._auth, self.__body = None, None, None, None, None, None
    self._tags, self._header_obj, self.__import_manage, self.__icons = None, None, None, None
    if script is None:
      frame = inspect.stack()[1]
      if inspect.getmodule(frame[0]) is not None:
        # Bug fixes for Google Collab
        script = inspect.getmodule(frame[0]).__file__
    self._props = {'js': {
          # JavaScript framework triggered after the HTML. Impact the entire page
          'onReady': OrderedSet(),
          'events': {},
          'functions': {},
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
        'context': {'framework': 'JS', "script": script},
        # Add report font-face CSS definition
        'css': {
          "font-face": {},
          "container": {},
          "text": []},
        # Add icons properties
        "icon": {"family": None}
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
    """ Property to the different Page properties JavaScript and CSS. """
    return Properties(self._props)

  @property
  def root__script(self) -> str:
    """ Return the name of the script creating the Page object. """
    return self._props["context"]["script"]

  @property
  def body(self) -> html.Html.Body:
    """ Property that returns the Body element of the HTML page.

    Usage::

      page = Report()
      page.body.onReady([page.js.alert("Loading started")])
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
  def theme(self) -> themes.Theme:
    """ Return the currently used :doc:`report/theme` for the report.

    Usage::

      page = Report()
      page.theme = themes.ThemeBlue.Blue
    """
    if self._theme is None:
      self._theme = themes.Theme.ThemeDefault()
    return self._theme

  @theme.setter
  def theme(self, theme: themes.Theme.ThemeDefault):
    if isinstance(theme, dict):
      self._theme = themes.Theme.ThemeCustom()
      self._theme = theme
    else:
      self._theme = theme

  @property
  def themes(self) -> themes.RegisteredThemes:
    return themes.RegisteredThemes(self)

  @property
  def skins(self) -> skins.Skins:
    """ Add a special skin to the page.

    This could be used for special event or season during the year (Christmas for example).

    Usage::

      page = pk.Page()
      page.ui.text("Hello World !")
      page.skins.rains()
      page.outs.html_file(name="test", print_paths=True)
    """
    return skins.Skins(self)

  def node_modules(self, path: str, alias: Optional[str] = None, install: bool = False, update: bool = False):
    """

    Usage::


    :param path: Optional. The nodeJs path.
    :param alias: Optional.
    :param install: Optional.
    :param update: Optional.
    """
    if path is not None:
      self._node_modules = (path, alias or path, install, update)

  @property
  def imports(self) -> Imports.ImportManager:
    """ Return the :doc:`report/import_manager`, which allows to import automatically packages for certain components to
    run.

    By default the imports are retrieved online from CDNJS paths.
    This can be changed by loading the packages locally and switching off the online mode.

    Usage::

      page = Report()
      page.imports.setVersion(page.imports.pkgs.popper_js.alias, "1.00.0")

    """
    if self.__import_manage is None:
      self.__import_manage = Imports.ImportManager(page=self)
    return self.__import_manage

  @property
  def symbols(self) -> symboles.Symboles:
    """ Shortcut to the HTML symbols.

    Those can be added in string in order to improve the render of a text.

    Usage::

      page = Report()
      page.ui.text(page.symbols.shapes.BLACK_SQUARE)

    Related Pages:

      https://www.w3schools.com/html/html_symbols.asp
      https://www.w3schools.com/charsets/ref_utf_math.asp
    """
    return symboles.Symboles()

  @property
  def entities(self) -> entities.Entities:
    """ Shortcut to the HTML Entities.

    Those can be added in string in order to improve the render of a text.

    Usage::

      page = Report()
      page.ui.text(page.entities.non_breaking_space)

    Related Pages:

      https://www.w3schools.com/html/html_entities.asp
    """
    return entities.Entities()

  @property
  def ui(self) -> Interface.Components:
    """ User Interface section.

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...).

    Usage::

      page = Report()
      page.ui.text("This is a text")

    Related Pages:

      https://www.w3schools.com/html/default.asp
    """
    return self.web.std

  @property
  def web(self) -> Interface.WebComponents:
    """ User Interface section.

    All the :doc:`components <report/ui>` which can be used in the dashboard to display the data.
    Within this object different categories of items can be used like (list, simple text, charts...).

    Usage::

      page = Report()
      page.web

    Related Pages:

      https://www.w3schools.com/html/default.asp
    """
    if self._ui is None:
      self._ui = Interface.WebComponents(self)
    return self._ui

  @property
  def css(self) -> Classes.Catalog:
    """ Returns the set of :doc:`CSS Classes <css>` for the HTML report.

    Usage::

      page = Report()
      page.css.
    """
    cls_obj = Classes.Catalog(self, {'other': set()})
    cls_obj.other
    return cls_obj

  @property
  def js(self) -> js.Js.JsBase:
    """ Go to the Javascript section. Property to get all the JavaScript features.

    Most of the standard modules will be available in order to add event and interaction to the Js transpiled.

    Usage::

      page = Report()
      page.js.console.log("test")

      page.js.accounting.add_to_imports()
      page.js.moment.add_to_imports()

    Related Pages:

      https://www.w3schools.com/js/default.asp
    """
    if self._js is None:
      self._js = js.Js.JsBase(self)
    return self._js

  @property
  def py(self) -> PyExt.PyExt:
    """ Python external module section.

    Those are pre-defined Python function to simplify the use of the various components.

    Usage::

      page = Report()
      page.py.dates.today()

    Related Pages:

      https://www.w3schools.com/js/default.asp
    """
    if self._py is None:
      self._py = PyExt.PyExt(self)
    return self._py

  @property
  def auth(self) -> auth.Auth:
    """ Auth interface to allow easy sign-in pages.

    Usage::

      page = Report()
      page.auth.

    Related Pages:

      https://developers.google.com/identity/sign-in/web/sign-in

    :return: Python Auth Object.
    """
    if self._auth is None:
      self._auth = auth.Auth(self)
    return self._auth

  @property
  def data(self) -> data.Data.DataSrc:
    """ Python internal data source management.

    This can be extended by inheriting from this epyk.core.data.DataSrc.DataSrc and adding extra entry points.

    Usage::

      page = Report()

    :return: The framework available data source
    """
    return data.Data.DataSrc(self)

  def register(self, ext_components: list):
    """ This function allows you to register external Components (namely coming from Pyk Reports)
    by registering them you this will engrave the object within your report.

    The example below will add obj1 and obj2 from an external pyk report previously required,
    then create a div and then add obj3 from an external file.

    Usage::

      page = Report()
      page.register([obj1, obj2])
      page.ui.div('this is a div')
      page.register(obj3)

    :param ext_components: The external components to be added
    """
    if type(ext_components) != list:
      ext_components = [ext_components]

    for comp in ext_components:

      if comp.html_code in self.components:
        raise ValueError("Duplicated Html Code %s in the script !" % comp.html_code)

      self.components[comp.html_code] = comp

  def get_components(self, html_codes: Union[list, str]):
    """ Retrieve the components based on their ID.

    This should be used when the htmlCode is defined for a component.

    Usage::

      page = Report()
      page.ui.button(htmlCode="Button")
      but = page.get_components(["Button"])

    :param html_codes: The reference of the HTML components loaded on the page
    """
    if not isinstance(html_codes, list):
      return self.components[html_codes]

    return [self.components[html_code] for html_code in html_codes]

  def framework(self, name: str):
    """ Flag to change the way code is transpiled in order to fit with the destination framework.

    By default the code transpiled will be used from a browser in plain Vanilla Js but this will be extended to then
    be compatible with other framework in order to simplify the path to production and the collaboration between teams.

    Many framework will be compatible like React, Angular, Vue but also some features will be exposed to Kotlin for
    mobile generation.

    This work is still in progress.

    Usage::

      page = Report()
      page.ui.text("This is an example")
      page.framework("Vue")

    :param name: The destination framework for the page
    """
    self._props['context']['framework'] = name.upper()

  @property
  def outs(self) -> PyOuts.PyOuts:
    """ Link to the possible output formats for a page.

    This will transpile the Python code to web artifacts. Those outputs are standard outputs files in web development.

    The property framework should be used to link to other web framework.

    Usage::

      page = Report()
      page.ui.text("This is an example")
      page.outs.html()
    """
    return PyOuts.PyOuts(self)

  @property
  def headers(self) -> html.Header.Header:
    """ Property to the HTML page header.

    Usage::

      page = pk.Page()
      page.headers.meta.viewport({"width": "device-width"})

      # Use the default DEV icon.
      page.headers.dev()
    """
    if self._header_obj is None:
      self._header_obj = html.Header.Header(self)
    return self._header_obj

  def dumps(self, result: dict):
    """ Function used to dump the data before being sent to the Javascript layer.

    This function relies on json.dumps with a special encoder in order to work with Numpy array and Pandas data
    structures.

    As NaN is not valid on the Json side those object are not allowed during the dump.
    It is advised to use fillna() in your script before returning the data to the framework to avoid this issue.

    Usage::

      page = Report()
      page.dumps(result)

    Related Pages:

      https://docs.python.org/2/library/json.html

    :param result: The python dictionary or data structure

    :return: The serialised data
    """
    return json.dumps(data, cls=js.JsEncoder.Encoder, allow_nan=False)

  @property
  def apps(self) -> apps.AppRoute:
    """ Change the report to a web application.

    This will add extra features available on the target framework.
    For example this HTML page can be transformed to an Angular app, a React App or a Vue one.

    Usage::

      page = Report()
    """
    self._props['web'] = {
      'modules': {}
    }
    return apps.AppRoute(self)

  @property
  def icons(self) -> Icons.IconModel:
    """ Change the icons framework used in the page.
    Defaults.py in the CSS module is to change the framework for all the page generated by the framework.

    Usage::

      page = pk.Page()
      page.icons.family = "bootstrap-icons"
      icons = page.ui.menus.icons([
          "bi-1-circle-fill",
          "bi-search-heart-fill",
          "bi-x-circle-fill",
      ])
    """
    if self.__icons is None:
      self.__icons = Icons.IconModel(self)
    return self.__icons