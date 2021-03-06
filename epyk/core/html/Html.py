#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import json
import collections
import functools
import logging

from epyk.core.js import JsUtils
from epyk.core.js import Js
from epyk.core.js import Imports
from epyk.core.js.html import JsHtml
from epyk.core.js import packages
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import packageImport

from epyk.core.css.styles import GrpCls
from epyk.core.css import Defaults as Defaults_css

from epyk.core.html import Aria
from epyk.core.html import Component
from epyk.core.html import KeyCodes
from epyk.core.html.options import Options

try:  # For python 3
  import urllib.request as urllib2
  import urllib.parse as parse
except:  # For Python 2
  import urllib2
  import urllib as parse


regex = re.compile('[^a-zA-Z0-9_]')


def cleanData(value):
  """ Function to clean the javascript data to allow the use of variables """
  return regex.sub('', value.strip())


# ---------------------------------------------------------------------------------------------------------
#                                          FRAMEWORK DECORATORS
#
# ---------------------------------------------------------------------------------------------------------
def deprecated(func):
  """
  Description:
  -----------
  This is a decorator which can be used to mark functions
  as deprecated. It will result in a warning being emitted
  when the function is used.

  Attributes:
  ----------
  :param func: Function. A python function.
  """

  @functools.wraps(func)
  def new_func(*args, **kwargs):
    logging.warn('#########################################')
    logging.warn("Call to deprecated function {}.".format(func.__name__))
    logging.warn('#########################################')
    return func(*args, **kwargs)
  return new_func


def inprogress(func):
  """
  Description:
  -----------
  Decorator to specify a function is still in development so the result might not be fully tested yet.

  Attributes:
  ----------
  :param func: Function. A python function.
  """
  @functools.wraps(func)
  def new_func(*args, **kwargs):
    # warnings.simplefilter('always', DeprecationWarning)  # turn off filter
    # warnings.warn('############################################################################')
    # warnings.warn("Call to a test function {}.".format(func.__name__), category=DeprecationWarning, stacklevel=2)
    # warnings.warn('############################################################################')
    # warnings.simplefilter('default', DeprecationWarning)  # reset filter
    return func(*args, **kwargs)

  return new_func


def css_skin():
  """
  Description:
  ------------
  In dev. Transversal way to change the skin of all the HTML Interfaces.
  This override is done just after the interface call in order to allow specific style definition in the reports.
  
  """
  def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      html_obj = func(*args, **kwargs)
      if html_obj._report.ui.components_skin is not None:
        if "button" in html_obj._report.ui.components_skin:
          html_obj._report.ui.components_skin["buttons.button"] = html_obj._report.ui.components_skin["button"]
        alias = func.__qualname__.lower()
        if alias in html_obj._report.ui.components_skin:
          comp_skin = html_obj._report.ui.components_skin[alias]
          if 'clear' in comp_skin:
            if comp_skin["clear"].get("css"):
              html_obj.style.clear_style()
            if comp_skin["clear"].get("cls"):
              html_obj.style.clear(True)
          html_obj.css(html_obj._report.ui.components_skin[alias].get('css', {}))
          for cls in comp_skin.get("cls", []):
            html_obj.attr["class"].add(cls)
      return html_obj

    return decorated

  return decorator


class Required(object):
  js, css = None, None

  def __init__(self, page):
    self.js, self.css = {}, {}
    self._page = page

  def add(self, package, version=None, verbose=True):
    """
    Description:
    -----------
    Add the package to the main page context.

    TODO: Use the version number

    Usage:
    -----


    Attributes:
    ----------
    :param package: String. The package alias.
    :param version: String. Optional. The package version number.
    :param verbose: Boolean. Optional. Display version details (default True).
    """
    html_types = set()
    if package in Imports.JS_IMPORTS:
      self.js[package] = version or '*'
      self._page.jsImports.add(package)
      html_types.add('js')
    if package in Imports.CSS_IMPORTS:
      self.css[package] = version or '*'
      self._page.cssImport.add(package)
      html_types.add('css')
    if not html_types and verbose:
      logging.warning("%s - Not defined in neither JS nor CSS configurations" % package)


class EventTouch(object):

  def __init__(self, page):
    self._page = page

  def start(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchstart event occurs when the user touches an element.

    Note: The touchstart event will only work on devices with a touch screen.

    Tip: Other events related to the touchstart event are:

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_touchstart.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchstart", js_funcs, profile)
    return self._page

  def move(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchmove event occurs when the user moves the finger across the screen.

    The touchmove event will be triggered once for each movement, and will continue to be triggered until the finger is released.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_touchmove.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchmove", js_funcs, profile)
    return self._page

  def cancel(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchcancel event occurs when the touch event gets interrupted.

    Different devices will interrupt a touch event at different actions, and it is considered good practice to include this event to clean up code if this "error" should occur.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_touchcancel.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchcancel", js_funcs, profile)
    return self._page

  def end(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchend event occurs when the user removes the finger from an element.

    Note: The touchend event will only work on devices with a touch screen.

    Tip: Other events related to the touchend event are:

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_touchend.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchend", js_funcs, profile)
    return self._page

  def swap(self, js_funcsLeft, js_funcsRight, profile=False, source_event=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcsLeft: List | String. Javascript functions.
    :param js_funcsRight: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self.start(["window.longTouch = event.touches[0].clientX || event.originalEvent.touches[0].clientX"])
    self.move(self._page.js.if_("window.longTouch != null", ["let swap =  (event.touches[0].clientX || event.originalEvent.touches[0].clientX) - window.longTouch",
      "window.longTouch = null", self._page.js.if_("swap < 0", js_funcsLeft).else_(js_funcsRight)]))
    return self


class Html(object):
  """
  Description:
  -----------
  Parent class for all the HTML components. All the function defined here are available in the children classes.
  Child class can from time to time re implement the logic but the function will always get the same meaning (namely the same signature and return)
  """
  #cssCls = None
  # Those variables should not be used anymore and should be replaced by the __ ones
  # This is done in order to avoid having users to change them. Thanks to the name
  # mangling technique Python will make the change more difficult and easier to see
  requirements = None
  builder_name, _js__builder__ = None, None

  def __init__(self, report, vals, htmlCode=None, options=None, profile=None, css_attrs=None):
    """ Create an python HTML object """
    self.components = collections.OrderedDict() # Child component for this component
    self.require = Required(report)
    for package in self.requirements or []:
      if isinstance(package, tuple):
        self.require.add(package[0], package[1])
      else:
        self.require.add(package)

    self.profile = profile
    self._report = report # Should be renamed by page / and component
    self._on_ready_js, self._sort_propagate, self._sort_options = {}, False, None # For sortable items
    self._dom, self._sub_htmls, self._js, self.helper, self._styleObj, self.__htmlCode = None, [], None, "", None, None

    self._browser_data = {"mouse": collections.OrderedDict(), 'component_ready': [],
                          'page_ready': collections.OrderedDict(), 'keys': collections.OrderedDict()}

    self.jsImports = report.jsImports # to be deleted - because changed should be done only on the component self.require
    self.cssImport = report.cssImport # to be deleted - because changed should be done only on the component self.require

    self._jsStyles = {}  # to be deleted - because code => htmlCode, _jsStyles should be renamed

    self.innerPyHTML = None  # to be reviewed - not sure this is still usefull

    self.__options = Options(self, options)

    self.attr = {'class': self.style.classList['main'], 'css': self.style.css.attrs}
    if css_attrs is not None:
      self.css(css_attrs)

    if htmlCode is not None:
      if htmlCode[0].isdigit() or cleanData(htmlCode) != htmlCode:
        raise Exception("htmlCode %s cannot start with a number or contain, suggestion %s " % (htmlCode, cleanData(htmlCode)))

      if htmlCode in self._report.components:
        raise Exception("Duplicated Html code %s in the script !" % htmlCode)

      self.__htmlCode = htmlCode
      # self._report.jsGlobal.reportHtmlCode.add(htmlCode)
      if htmlCode in self._report.inputs:
        vals = self._report.inputs[htmlCode]

    self._report.components[self.htmlCode] = self
    self._vals = vals
    self.builder_name = self.builder_name if self.builder_name is not None else self.__class__.__name__
    self._internal_components = [self.htmlCode]

  def add(self, component):
    """
    Description:
    -----------
    Add items to a container.

    The added HTML component will not be managed by the page by default. This means it might not be visible on the
    JavaScript page if it is not by default managed by the main HTML component.

    For example containers are designed to handle sub components.

    Usage:
    -----

      div = page.ui.div()
      div.add(page.ui.button("Run"))

    Attributes:
    ----------
    :param component: HTML. Component added to the val main component.
    """
    return self.__add__(component)

  def __add__(self, component):
    """ Add items to a container """
    if hasattr(component, 'options'):
      component.options.managed = False
    self.val.append(component)
    return self

  def __getitem__(self, i):
    if not isinstance(i, int) and i in self.components:
      return list(self.components.items())[i][1]

    return self.val[i]

  @property
  def style(self):
    """
    Description:
    -----------
    The CSS style (class and attributes) of the HTML component.
    This property will allow to custom any component in the page.

    Usage:
    -----

      div = page.ui.div()
      div.style.css.background = 'black'

    :rtype: GrpCls.ClassHtml
    """
    if self._styleObj is None:
      self._styleObj = GrpCls.ClassHtml(self)
    return self._styleObj

  @property
  def htmlCode(self):
    """
    Description:
    -----------
    Unique reference for any HTML component in the framework. This must be defined in the interface and cannot be changed
    in the report.

    This reference can be used in the Python to get the html object from components in the page but it is also
    used in any web framework by the JavaScript to get the DOM object and apply the necessary transformations.

    There is not setter for this property in order to ensure a consistancy in Python and JavaScript.

    Usage:
    -----

      div = page.ui.div(htmlCode="testDiv")
      print(div.htmlCode)
    """
    if self.__htmlCode is not None:
      return self.__htmlCode

    return "%s_%s" % (self.__class__.__name__.lower(), id(self))

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage:
    -----

      div = page.ui.div(htmlCode="testDiv")
      div.click([
        div.js.alert("Hello")
      ])

    :return: A Javascript object

    :rtype: Js.JsBase
    """
    if self._js is None:
      self._js = Js.JsBase(self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.
    
    Usage:
    -----

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a button.
    
    Usage:
    -----

      div = page.ui.div(htmlCode="testDiv")
      div.options.inline = True

    :rtype: Options
    """
    return self.__options

  def prepend_child(self, component):
    """
    Description:
    -----------
    Wrapper to the Javascript method insertChild to add an HTML component.

    Usage:
    -----

      for i in range(10):
        comp = rptObj.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
        select.prepend_child(comp)

    Related Pages:

      https://www.w3schools.com/jsref/met_node_insertbefore.asp

    Attributes:
    ----------
    :param component: HTML. The html component.

    :return: The htmlObj
    """
    self._sub_htmls.append(component)
    self.components[component.htmlCode] = component
    #htmlObj.options.managed = False
    # add a flag to propagate on the Javascript the fact that some child nodes will be added
    # in this case innerHYML cannot be used anymore
    self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
    self._report._props.setdefault('js', {}).setdefault('builders', []).add(JsUtils.jsConvertFncs([self.dom.insertBefore(component.dom)], toStr=True))
    return self

  def append_child(self, component):
    """
    Description:
    -----------
    Wrapper to the Javascript method appendChild to append an HTML component

    Usage:
    -----

      for i in range(10):
        component = rptObj.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
        select.append_child(component)

    Related Pages:

      https://www.w3schools.com/jsref/met_node_appendchild.asp

    Attributes:
    ----------
    :param component: HTML. The html component.

    :return: The htmlObj
    """
    self._sub_htmls.append(component)
    #htmlObj.options.managed = False
    # add a flag to propagate on the Javascript the fact that some child nodes will be added
    # in this case innerHYML cannot be used anymore
    self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
    self._report._props.setdefault('js', {}).setdefault('builders', []).add(JsUtils.jsConvertFncs([self.dom.appendChild(component.dom)], toStr=True))
    return self

  def onReady(self, js_funcs):
    """
    Description:
    -----------
    Add set of event / actions which will be triggered after the build of the object.
    Usually this can be used to add js functions on a chart or a table.

    Usage:
    -----

      network = rptObj.ui.charts.vis.network()
      network.onReady([
        network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []}),
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._browser_data['component_ready'].extend(JsUtils.jsConvertFncs(js_funcs))

  def add_menu(self, context_menu):
    """
    Description:
    -----------
    Attach a context menu to an existing component. A context menu must have a component attached to otherwise
    the report will not be triggered.

    Usage:
    -----

    Attributes:
    ----------
    :param context_menu: ContextMenu. A Python context menu object.
    """
    context_menu.source = self
    self._report._contextMenu[self.dom.jquery.varName] = context_menu
    return self

  def add_icon(self, text, css=None, position="before", family=None, htmlCode=None):
    """
    Description:
    ------------
    Add an icon to the HTML object.

    Usage:
    -----

      checks.title.add_icon("fas fa-align-center")

    Related Pages:


    Attributes:
    ----------
    :param text: String. The icon reference from font-awesome website.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param family: String. Optional. The icon framework to be used (preferred one is font-awesome).
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).

    :return: The Html object
    """
    self.icon = ""
    defined_families = ('office-ui-fabric-core', 'material-design-icons')
    if family is not None and self.options.verbose and family not in defined_families:
      logging.warning("Family %s not defined in %s" % (family, defined_families))

    if text is not None:
      self.icon = self._report.ui.images.icon(text, htmlCode="%s_icon" % htmlCode if htmlCode is not None else htmlCode,
                                              family=family).css({"margin-right": '5px', 'font-size': 'inherit'})
      if position == "before":
        self.prepend_child(self.icon)
      else:
        self.append_child(self.icon)
      if css is not None:
        self.icon.css(css)
    return self

  def add_label(self, text, css=None, position="before", for_=None, htmlCode=None, options=None):
    """
    Description:
    -----------
    Add an elementary label component.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
    :param text: String. The label content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param for_: String. Optional. Specifies which form element a label is bound to.
    """
    self.label = ""
    if text is not None:
      self.label = self._report.ui.texts.label(text, options=options, htmlCode="%s_label" % htmlCode if htmlCode is not None else htmlCode)
      if for_ is not None:
        # Attach the label to another HTML component based on the ID
        self.label.attr['for'] = for_
      if position == "before":
        self.prepend_child(self.label)
      else:
        self.append_child(self.label)
      if css == False:
        self.label.attr['css'] = {}
      elif css is not None:
        self.label.css(css)
    return self

  def add_span(self, text, css=None, position="before", htmlCode=None, i=None):
    """
    Description:
    -----------
    Add an elementary span component.

    Usage:
    -----

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/layering

    Attributes:
    ----------
    :param text: String. The Span content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param i: Integer. Optional.
    """
    if i is not None:
      key_attr = 'span_%s' % i
    else:
      key_attr = 'span'
    setattr(self, key_attr, '')
    if text is not None:
      setattr(self, key_attr, self._report.ui.texts.span(text, htmlCode="%s_span" % htmlCode if htmlCode is not None else htmlCode))
      span = getattr(self, key_attr)
      if position == "before":
        self.prepend_child(span)
      else:
        self.append_child(span)
      if css == False:
        span.attr['css'] = {}
      elif css is not None:
        span.css(css)
    return self

  def add_link(self, text, url=None, script_name=None, report_name=None, name=None, icon=None, css=None,
               position="before", options=None):
    """
    Description:
    -----------
    Add an elementary label component

    Usage:
    -----

      div = rptObj.ui.div()
      div.add_link("test.py", name="Click to go to the test report")

    Attributes:
    ----------
    :param text: String. The value of the link displayed in the page.
    :param url: String. Optional. The URL path.
    :param script_name:
    :param report_name:
    :param name:
    :param icon:
    :param css: Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    """
    self.link = ""
    if url is not None or script_name is not None:
      dflt_options = {"name": name} if name is not None else {}
      if options is not None:
        dflt_options.update(options)
      if url is not None:
        self.link = self._report.ui.links.external(text, url, options=dflt_options)
      else:
        self.link = self._report.ui.links.script(text, script_name, report_name, icon=icon, options=dflt_options)
      if position == "before":
        self.prepend_child(self.link)
      else:
        self.append_child(self.link)
      if css is not None:
        self.link.css(css)
    return self

  def add_title(self, text, level=None, css=None, position="before", options=None):
    """
    Description:
    -----------
    Add an elementary title component.

    Usage:
    -----


    Attributes:
    ----------
    :param text: String. The title content.
    :param level: Integer. Optional. The level of title.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    self.title = ""
    if text is not None:
      self.title = self._report.ui.texts.title(text, level=level, options=options)
      if options.get('managed', True):
        if position == "before":
          self.prepend_child(self.title)
        else:
          self.append_child(self.title)
      else:
        self.title.options.managed = False
      if css == False:
        self.title.attr['css'] = {}
      elif css is not None:
        self.title.css(css)
    return self

  def add_input(self, text, css=None, attrs=None, position="before", options=None):
    """
    Description:
    -----------
    Add an elementary input component.

    Usage:
    -----


    Attributes:
    ----------
    :param text: String. The title content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param attrs: Dictionary. Optional. The HTML tag attributes.
    :param position: Dictionary. Optional. Specific Python options available for this component.
    """
    self.input = ""
    if text is not None:
      self.input = self._report.ui.inputs.input(text, options=options)
      if position == "before":
        self.prepend_child(self.input)
      else:
        self.append_child(self.input)
      if css is not None:
        self.input.css(css)
      if attrs is not None:
        self.input.set_attrs(attrs=attrs)
    return self

  def add_checkbox(self, flag, css=None, attrs=None, position="before"):
    """
    Description:
    -----------
    Add an elementary checkbox component.

    Usage:
    -----

    Attributes:
    ----------
    :param flag: Boolean. The state of the checkbox component.
    :param css: Optional. A dictionary with the CSS style to be added to the component.
    :param attrs: Dictionary. Optional. The HTML tag attributes.
    :param position: Dictionary. Optional. Specific Python options available for this component.
    """
    self.checkbox = ""
    if flag is not None:
      self.checkbox = self._report.ui.inputs.checkbox(flag)
      if position == "before":
        self.prepend_child(self.checkbox)
      else:
        self.append_child(self.checkbox)
      if css is not None:
        self.checkbox.css(css)
      if attrs is not None:
        self.checkbox.set_attrs(attrs=attrs)
    return self

  def add_helper(self, text, css=None):
    """
    Description:
    -----------
    Add an elementary helper icon.

    The helper is not managed by the main page and should be written in the component.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. The helper content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.

    :rtype: self._report.ui.rich.info
    """
    if text is not None:
      self.helper = self._report.ui.rich.info(text)
      self.helper.options.managed = False
      if css is not None:
        self.helper.css(css)
    return self

  @property
  def keydown(self):
    """
    Description:
    -----------
    The onkeydown event occurs when the user is pressing a key (on the keyboard).

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeydown.asp

    :rtype: KeyCodes.KeyCode
    """
    if self._browser_data.get('keys', {}).get('keydown') is None:
      self._browser_data['keys']['keydown'] = KeyCodes.KeyCode(component=self)
    return self._browser_data['keys']['keydown']

  @property
  def keypress(self):
    """
    Description:
    -----------
    The onkeypress event occurs when the user presses a key (on the keyboard).

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :rtype: KeyCodes.KeyCode
    """
    if self._browser_data.get('keys', {}).get('keypress') is None:
      self._browser_data['keys']['keypress'] = keypress = KeyCodes.KeyCode(component=self)
    return self._browser_data['keys']['keypress']

  @property
  def keyup(self):
    """
    Description:
    -----------
    The onkeypress event occurs when the user presses a key (on the keyboard).

    Usage:
    -----


    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :rtype: KeyCodes.KeyCode
    """
    if self._browser_data.get('keys', {}).get('keyup') is None:
      self._browser_data['keys']['keyup'] = KeyCodes.KeyCode(component=self)
    return self._browser_data['keys']['keyup']

  @property
  def aria(self):
    """
    Accessible Rich Internet Applications is a [HTML] specification module.
    Web developers MAY use the ARIA role and aria-* attributes on HTML elements.

    Usage:
    -----

    Related Pages:

      https://www.w3.org/TR/html-aria/#allowed-aria-roles-states-and-properties
    """
    return Aria.Aria(self)

  @property
  def val(self):
    """
    Description:
    -----------
    Property to get the jquery value of the HTML object in a python HTML object.
    This method can be used in any jsFunction to get the value of a component in the browser.
    This method will only be used on the javascript side, so please do not consider it in your algorithm in Python.

    Usage:
    -----

    :returns: Javascript string with the function to get the current value of the component
    """
    return self._vals

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    if self.innerPyHTML is not None:
      if isinstance(self.innerPyHTML, list):
        return "".join([h.html() for h in self.innerPyHTML])

      return self.innerPyHTML.html()

    return self.val if not hasattr(self.val, "html") else self.val.html()

  def move(self):
    """
    Description:
    -----------
    Move the component to this position in the page.

    Usage:
    -----

    """
    self._report.components.move_to_end(self.htmlCode)

  def css(self, key=None, value=None, reset=False):
    """
    Description:
    -----------
    Change the CSS Style of a main component. This is trying to mimic the signature of the Jquery css function.

    Usage:
    -----

    Related Pages:

      http://api.jquery.com/css/

    Attributes:
    ----------
    :param key: String. Optional. The key style in the CSS attributes (Can also be a dictionary).
    :param value: String. Optional. The value corresponding to the key style.
    :param reset: Boolean. Optional. Specify if the CSS styles need to be emptied first.

    :return: The python object itself
    """
    if key is None and value is None:
      return self.attr['css']

    if reset:
      self.style.css.attrs = {}
      self.attr['css'] = self.style.css.attrs
    if value is None and isinstance(key, dict):
      # Do not add None value to the CSS otherwise it will break the page on the front end side
      css_vals = key if isinstance(key, dict) else {}
    elif value is None and not isinstance(key, dict):
      return self.attr['css'].get(key)

    else:
      if isinstance(value, tuple):
        value = value[0] if value[0] is None else "%s%s" % (value[0], value[1])
      css_vals = {key: value}
    if 'css' not in self.attr:
      self.attr['css'] = self.style.css.attrs
    for key, value in css_vals.items():
      if isinstance(value, tuple):
        if value[0] is None:
          continue

        value = "%s%s" % (value[0], value[1])
      if value is None:
        continue

      self.attr['css'][key] = value if isinstance(value, str) else json.dumps(value)
    return self

  @packages.packageImport('bootstrap', 'bootstrap')
  def tooltip(self, value, location='top', options=None):
    """
    Description:
    -----------
    Add the Tooltip feature when the mouse is over the component.
    This tooltip version is coming from Bootstrap.

    Usage:
    -----

      htmlObj.tooltip("My tooltip", location="bottom")

    Related Pages:

      https://getbootstrap.com/docs/4.1/components/tooltips/

    TODO Change background color

    Attributes:
    ----------
    :param value: String. The tooltip text.
    :param location: String. Optional. The position of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.

    :return: The Python object self
    """
    if value is not None:
      self.attr.update({'data-toggle': 'tooltip', 'data-html': 'true', 'data-placement': location})
      if options is not None:
        self.attr.update(options)
      self._report._props['js']['onReady'].add("%s.tooltip()" % JsQuery.decorate_var("'[data-toggle=tooltip]'", convert_var=False))
      if hasattr(value, 'toStr'):
        self.onReady(self.dom.setattr("title", value))
      else:
        self.attr.update({'title': value})
    return self

  @packages.packageImport('bootstrap', 'bootstrap')
  def popover(self, content, title=None, options=None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/popovers/

    Attributes:
    ----------
    :param content: String. The tooltip content.
    :param title: String. Optional. The tooltip title.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    if content is not None:
      self.attr["data-content"] = content
      if title is not None:
        self.attr["data-title"] = title
      if options is not None:
        for k, v in options.items():
          self.attr["data-%s" % k] = title
      self.attr["data-toggle"] = 'popover'
      self._report._props['js']['onReady'].add("%s.popover()" % JsQuery.decorate_var("'[data-toggle=popover]'", convert_var=False))
    return self

  def draggable(self, js_funcs=None, options=None, profile=False, source_event=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.attr["draggable"] = True
    return self.on("dragstart", js_funcs + ['event.dataTransfer.setData("text", event.target.innerHTML)'], profile=profile, source_event=source_event)

  def add_options(self, options=None, name=None, value=None):
    """
    Description:
    -----------
    Change the Javascript options of the component.
    This will change the options sent to the Javascript.

    Usage:
    -----

    Attributes:
    ----------
    :param options: Dictionary. Optional. the extra options to be added to the component.
    :param name: String. Optional. The key.
    :param value: String. Optional. The value.

    :return: self to allow the chains
    """
    if options is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if options is None:
      options = {name: value}
    for k, v in options.items():
      self._jsStyles[k] = v
    return self

  def set_attrs(self, attrs=None, name=None, value=None):
    """
    Description:
    -----------
    Function to update the internal dictionary of object attributes. Those attributes will be used when the HTML component will be defined.
    Basically all sort of attributes can be defined here: CSS attributes, but also data, name...
    Either the attrs or the tuple (name, value) can be used to add information to the dom object.

    All the attributes should be Python object which are ready to use on the Javascript side.
    For example True should be written 'true'.

    Tips: It is possible to use the data- attributes to store any kind of information in the dom.

    Usage:
    -----

    Attributes:
    ----------
    :param attrs: Dictionary. Optional. A python dictionary with the attributes.
    :param name: String. Optional. A python string with the name of the attribute.
    :param value: String. Optional. A python string with the value of the attribute.
    """
    if attrs is None and name is None:
      raise Exception("Either the attrs or the name should be specified")

    if attrs is None:
      attrs = {name: value}
    for k, v in attrs.items():
      if k == 'css':
        # Section for the Style attributes
        if v is None:
          self.style.clear_style()
          continue

        if 'css' not in self.attr:
          self.attr['css'] = dict(v)
        else:
          self.attr['css'].update(v)
      elif k == 'class':
        self.style.clear()
        if v is None:
          continue

        if not isinstance(v, set):
          v = set(v.split(" "))
        for c in v:
          self.attr['class'].add(c)
      else:
        # Section for all the other attributes#
        if v is not None:
          self.attr[k] = v
    return self

  def get_attrs(self, withId=True, pyClassNames=None):
    """
    Description:
    -----------
    Return the string line with all the attributes.

    All the attributes in the div should use double quote and not simple quote to be consistent everywhere in the framework
    and also in the javascript. If there is an inconsistency, the aggregation of the string fragments will not work

    Usage:
    -----

    Attributes:
    ----------
    :param withId: Boolean. Optional. Add the ID tag. This is handled by the framework. (Default true)
    :param pyClassNames: List. Optional. The Python class names.

    :return: A string with the dom attributes
    """
    cssStyle, cssClass, classData = '', '', ''
    if 'css' in self.attr:
      styles = ";".join(["%s:%s" % (key, val) for key, val in self.attr["css"].items()])
      if styles:
        cssStyle = 'style="%s"' % styles
    if 'class' in self.attr and len(self.attr['class']) > 0 and classData:
      if pyClassNames is not None:
        # Need to merge in the class attribute some static classes coming from external CSS Styles sheets
        # and the static python classes defined on demand in the header of your report
        # self._report.cssObj.getClsTag(pyClassNames)[:-1] to remove the ' generated in the module automatically
        cssClass = self._report.style.getClsTag(pyClassNames.clsMap).replace('class="', 'class="%s ')
        if cssClass:
          cssClass %= classData
        else:
          cssClass = 'class="%s"' % classData
      else:
        cssClass = 'class="%s"' % classData
    elif pyClassNames is not None:
      pyClsNames = [cls.get_ref() if hasattr(cls, 'get_ref') else cls for cls in pyClassNames['main']]
      cssClass = 'class="%s"' % " ".join(pyClsNames) if len(pyClsNames) > 0 else ""

    if withId:
      self.attr['id'] = self.htmlCode
    html_tags = ['%s="%s"' % (key, str(val).replace('"', "'")) if val is not None else key for key, val in self.attr.items() if key not in ('css', 'class')]
    for tag in [cssStyle, cssClass]:
      if tag:
        html_tags.append(tag)
    str_tag = " ".join(html_tags)
    return str_tag.strip()

  def on(self, event, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    Add an event to the document ready function.
    This is to mimic the Jquery on function.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jquery/event_on.asp
      https://www.w3schools.com/js/js_htmldom_eventlistener.asp
      https://www.w3schools.com/jsref/dom_obj_event.asp

    Attributes:
    ----------
    :param event: String. A string with the Javascript event type from the dom_obj_event.asp.
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. A String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: self to allow the chains
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    # JsUtils.jsConvertFncs needs to be applied in order to freeze the function
    # span.on("mouseover", span.dom.css("color", "red").r)
    # span.on("mouseleave", span.dom.css("color", "blue"))
    source_event = source_event or self.dom.varId
    if event not in self._browser_data['mouse']:
      self._browser_data['mouse'][event] = {}
    self._browser_data['mouse'][event].setdefault(source_event, {}).setdefault("content", []).extend(JsUtils.jsConvertFncs(js_funcs))
    self._browser_data['mouse'][event][source_event]['profile'] = profile
    if onReady:
      self._report.body.onReady([self.dom.events.trigger(event)])
    return self

  def drop(self, js_funcs, prevent_default=True, profile=False):
    """
    Description:
    -----------
    Add a drag and drop property to the element.

    Usage:
    -----

      d = rptObj.ui.div()
      d.drop([rptObj.js.objects.data.toRecord([1, 2, 3, 4], "result")])

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param prevent_default: Boolean. Optional. Specify if the event should have a default behaviour on the page.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.

    :return: Return self to allow the chaining
    """
    dft_fnc = ""
    if prevent_default:
      dft_fnc = self._report.js.objects.event.preventDefault()
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_fncs = JsUtils.jsConvertFncs(["var data = %s" % self._report.js.objects.event.dataTransfer.text] + js_funcs, toStr=True)
    # By default change the box shadow of this component
    self.attr["ondrop"] = "(function(event){%s; %s; %s; return false})(event)" % (dft_fnc, str_fncs, self.dom.css('box-shadow', 'none').r)
    self.attr["ondragover"] = "(function(event){%s; %s})(event)" % (dft_fnc, self.dom.css('box-shadow', 'inset 0px 0px 0px 2px %s' % self._report.theme.success[1]).r)
    self.attr["ondragleave"] = "(function(event){%s; %s})(event)" % (dft_fnc, self.dom.css('box-shadow', 'none').r)
    return self

  def hover(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------
    Add an mouse hover event on the component.

    Usage:
    -----

      div = page.ui.div()
      div.hover([
        page.js.alert("This is a test")
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. A String. Optional. The source target for the event.
    """
    return self.on("mouseover", js_funcs, profile, source_event)

  def click(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.

    Usage:
    -----

      div = page.ui.div()
      div.click([
        page.js.alert("This is a test")
      ])

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if onReady:
      self._report.body.onReady([self.dom.events.trigger("click")])
    return self.on("click", js_funcs, profile, source_event)

  def dblclick(self, js_funcs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------
    The ondblclick event occurs when the user double-clicks on an element.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_ondblclick.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if onReady:
      self._report.body.onReady([self.dom.events.trigger("dblclick")])
    return self.on("dblclick", js_funcs, profile, source_event)

  def scroll(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:


    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    """
    return self.on("scroll", js_funcs, profile, source_event)

  def mouse(self, on_funcs=None, out_funcs=None, profile=False, source_event=None):
    """
    Description:
    -----------
    Wrapper function fot the mouse event.
    This function will cover the on mouse hover event and mouse out.

    More specific events are possible using the generic out function.

    Tip: As function are defined to be chaining in most of the components use .r to get the string representation and clean the cache.

    Usage:
    -----

      span.mouse([
      span.dom.css("color", "red"),
      span.dom.css("cursor", "pointer").r],
      span.dom.css("color", "blue").r)

    Attributes:
    ----------
    :param on_funcs: List | String. The Javascript events.
    :param out_funcs: List | String. The Javascript events.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.

    :return: self to allow the chains
    """
    self.style.css.cursor = 'pointer'
    if on_funcs is not None:
      self.on("mouseenter", on_funcs, profile, source_event)
    if out_funcs is not None:
      self.on("mouseleave", out_funcs, profile, source_event)
    return self

  def paste(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------
    Add a paste event to the component.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. A String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_fncs = JsUtils.jsConvertFncs(["var data = %s" % self._report.js.objects.event.clipboardData.text] + js_funcs, toStr=True)
    return self.on("paste", str_fncs, profile, source_event)

  def contextMenu(self, menu, js_funcs=None, profile=False):
    """
    Description:
    -----------
    Attach a context menu to a component and set a function to called before the display.

    Usage:
    -----

    Attributes:
    ----------
    :param menu:
    :param js_funcs: List | String. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not hasattr(menu, 'source'):
      menu = self._report.ui.menus.contextual(menu)
    self.context_menu = menu
    menu.source = self
    new_js_funcs = (js_funcs or []) + [self._report.js.objects.mouseEvent.stopPropagation(),
                                    self.context_menu.dom.css({"display": 'block', 'left': self._report.js.objects.mouseEvent.clientX + "'px'",
                                  'top': self._report.js.objects.mouseEvent.clientY + "'px'"}),
                   self._report.js.objects.mouseEvent.preventDefault()]
    self.on("contextmenu", new_js_funcs, profile)
    return self

  @property
  def touch(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return EventTouch(self)

  def build(self, data=None, options=None, profile=False):
    """
    Description:
    -----------
    Return the JavaScript fragment to refresh the component content.

    Usage:
    -----

    Attributes:
    ----------
    :param data: String | object. The component expected content.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not self.builder_name or self._js__builder__ is None:
      raise Exception("No builder defined for this HTML component %s" % self.__class__.__name__)

    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[self.builder_name] = "function %s(htmlObj, data, options){%s}" % (self.builder_name, self._js__builder__)
    self.options.builder = self.builder_name
    if isinstance(data, dict):
      # check if there is no nested HTML components in the data
      tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in data.items()]
      js_data = "{%s}" % ",".join(tmp_data)
    else:
      js_data = JsUtils.jsConvertData(data, None)
    options, js_options = options or self._jsStyles, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("'%s': {%s}" % (k, ", ".join(row)))
      else:
        if self.options.isJsContent(k) or str(v).strip().startswith("function"):
          js_options.append("%s: %s" % (k, v))
        else:
          js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    fnc_call = "%s(%s, %s, %s)" % (self.builder_name, self.dom.varId, js_data, "{%s}" % ",".join(js_options))
    if profile:
      if isinstance(profile, dict):
        return "(function(){var t0 = performance.now(); %s; console.log('%s: ' + (performance.now() - t0) + ' ms' )})()" % (fnc_call, profile['name'])

      return "(function(){var t0 = performance.now(); %s; console.log(performance.now() - t0)})()" % fnc_call

    return fnc_call

  def refresh(self):
    """
    Description:
    -----------
    Component refresh function. Javascript function which can be called in any Javascript event.

    Usage:
    -----

    """
    return self.build(self.val, self._jsStyles)

  def subscribe(self, socket, channel, data=None, options=None, js_funcs=None, profile=False):
    """
    Description:
    ------------
    Subscribe to a socket channel.
    Data received from the socket are defined as a dictionary with a field data.

    The content of data will be used by this component.

    Usage:
    -----

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param socket: Socket. A python socket object.
    :param channel: String. The channel on which events will be received.
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if data is None:
      data = socket.message
    js_funcs = js_funcs if js_funcs is not None else []
    socket.on(channel, [self.build(data, options, profile)] + js_funcs)
    return self

  @packageImport('sortablejs')
  def sortable(self, options=None, propagate=True, propagate_only=False):
    """
    Description:
    ------------
    Sortable is a JavaScript library for reorderable drag-and-drop lists.

    Usage:
    -----

    Related Pages:

      https://github.com/SortableJS/Sortable

    Attributes:
    ----------
    :param options: Dictionary. The sortable options.
    :param propagate: Boolean. Specify if the sub children should get the draggable property.
    :param propagate_only: Boolean. Specify if the first level of child is draggable.

    :rtype: JsSortable.Sortable
    """
    from epyk.core.js.packages import JsSortable

    self._sort_propagate = propagate
    if not propagate_only:
      if 'sortable' not in self._on_ready_js:
        self._on_ready_js['sortable'] = JsSortable.Sortable(self, varName="%s_sortable" % self.htmlCode, selector=self.dom.varId, parent=self._report)
        dflt_options = {"group": self.htmlCode}
        dflt_options.update(options or {})
        self._sort_options = dflt_options
        self._on_ready_js['sortable'].create(self.dom.varId, dflt_options)
      return self._on_ready_js['sortable']

  # def filter(self, jsId, colName, allSelected=True, filterGrp=None, operation="=", itemType="string"):
  #   filterObj = {"operation": operation, 'itemType': itemType, 'allIfEmpty': allSelected, 'colName': colName, 'val': self.val, 'typeVal': 'js'}
  #   self._report.jsSources.setdefault(jsId, {}).setdefault('_filters', {})[self.htmlCode] = filterObj
  #   return self

  # -------------------------------------------------------------------------------------------------------------------
  #                    OUTPUT METHODS
  # -------------------------------------------------------------------------------------------------------------------
  def __str__(self):
    """
    Description:
    -----------
    Apply the corresponding function to build the HTML result.
    This function is very specific and it has to be defined in each class.
    """
    raise NotImplementedError('subclasses must override __str__()!')

  @property
  def component(self):
    """
    Description:
    -----------
    The static component definition on the Javascript Side.

    This will be then used by the different framework to define the elementary bricks on which the complex component
    will be based on.

    Usage:
    -----

    """
    return Component.Component(self)

  def html(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    str_result = []
    if self._on_ready_js:
      self.onReady(list(self._on_ready_js.values()))
    if self.helper != "":
      self.helper.html()

    # Propagate the external requirements to the page
    for js in self.require.js:
      self._report.jsImports.add(js)
    for css in self.require.css:
      self._report.cssImport.add(css)

    str_result.append(str(self))
    return "".join(str_result)

  def export(self, mode):
    return {'folder': self.__class__.__name__.lower(), 'class': "%sComponent" % self.__class__.__name__,
            'styleUrls': "", "externalVars": "", "componentFunctions": [], 'htmlTag': "app-epyk-%s" % self.__class__.__name__.lower()}


class Body(Html):
  name = "Body"

  def __init__(self, report, vals, htmlCode=None, options=None, profile=None, css_attrs=None):
    super(Body, self).__init__(report, vals, htmlCode, options, profile, css_attrs)
    if Defaults_css.BODY_STYLE is not None:
      for attrs in Defaults_css.BODY_STYLE.split(";"):
        k, v = attrs.split(":")
        self.css(key=k, value=v)

  @property
  def style(self):
    """
    Description:
    -----------
    A property to the CSS style of the DOM component.
    Each component will have default CSS style but they can be overridden.

    Usage:
    -----

    :rtype: GrpCls.ClassPage
    """
    if self._styleObj is None:
      self._styleObj = GrpCls.ClassPage(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(self, report=self._report)
      self._dom.varName = "document.body"
    return self._dom

  def scroll(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._report.js.onReady(self._report.js.window.events.addScrollListener(JsUtils.jsConvertFncs(js_funcs, toStr=True)))

  def onReady(self, js_funcs):
    """
    Description:
    -----------
    Add set of event / actions which will be triggered after the build of the object.
    usually this can be used to add js functions on a chart or a table.

    Usage:
    -----

      network = rptObj.ui.charts.vis.network()
      network.onReady([
        network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []}),
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript function to be added once the object is built.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._report.js.onReady(js_funcs)

  def onLoad(self, js_funcs):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(JsUtils.jsConvertFncs(js_funcs, toStr=True))

  def fromConfig(self, js_funcs=None, components=None, lang="eng", end_point="/static/configs", sync=True):
    """
    Description:
    -----------
    Load teh configuration file in order to fill the templates with static data.
    This will allow to externalise the configuration and design rich web templates.

    Do not forget to use CTRL+F5 in order to refresh the browser cache to get the updates.

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. Optional. The various transformations to be triggered from the configuration data.
    :param components: List. Optional. The various HTML Components to be updated fro the configuration file.
    :param lang: String. Optional. The default lang for the configuration.
    :param end_point: String. Optional. The url for the configuration files.
    :param sync: Boolean. Optional. Specify if the type of loading event.
    """
    if self._report.json_config_file is None:
      raise Exception("json_config_file must be attached to the page to load the corresponding configuration")

    js_funcs = js_funcs or []
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]

    return '''
      if (typeof window['page_config'] === 'undefined'){
        var rawFile = new XMLHttpRequest(); const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString); var lang = urlParams.get('lang') || '%(lang)s'; 
        rawFile.overrideMimeType("application/json"); rawFile.open("GET", "%(url)s/"+ lang +"/%(json)s.json", %(sync)s);
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
               var data = JSON.parse(rawFile.responseText); window['page_config'] = data; %(fncs)s}}
        rawFile.send(null)} 
      else {var data = window['page_config']; %(fncs)s}''' % {"sync": JsUtils.jsConvertData(not sync, None), "lang": lang, 'url': end_point, 'json': self._report.json_config_file,
            'fncs': JsUtils.jsConvertFncs(js_funcs + [c.build(self._report.js.objects.get("data['%s']" % c.htmlCode)) for c in components], toStr=True)}

  def set_content(self, report, page_content):
    """
    Description:
    ------------
    Function to allow the templating of the report.
    This can be overridden by a generic class which can be shared within a set of report

    Usage:
    -----

    Attributes:
    ----------
    :param report: Report. The main report object.
    :param page_content: String. The html content of the page.

    :return: The Body HTML object
    """
    self._html_content = page_content
    return self

  def set_background(self, start_color=None, end_color=None, from_theme=False):
    """
    Description:
    ------------
    Change the body background color.

    Usage:
    -----

      rptObj.body.set_background("#101626", "#374F67")

    Attributes:
    ----------
    :param start_color: String. Optional.
    :param end_color: String. Optional.
    """
    if from_theme or (start_color is None and end_color is None):
      self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (self._report.theme.colors[-1], self._report.theme.colors[2])
    elif end_color is not None:
      self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (start_color, end_color)
    else:
      self.style.css.background = start_color
    self.style.css.background_repeat = "no-repeat"
    self.style.css.background_color = self._report.theme.colors[2]

  def loading(self, status=True):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param status: Boolean. Optional. A flag to specify the status of the loading event.
    """
    if status:
      return ''' 
        if (typeof window['popup_loading_body'] === 'undefined'){
          window['popup_loading_body'] = document.createElement("div"); 
          window['popup_loading_body'].style.width = '100%'; window['popup_loading_body'].style.height = '100%'; window['popup_loading_body'].style.opacity = 0.3;
          window['popup_loading_body'].style.position = 'fixed'; window['popup_loading_body'].style.top = 0; window['popup_loading_body'].style.left = 0; window['popup_loading_body'].style.zIndex = 410;
          window['popup_loading_body'].style.background = 'green'; window['popup_loading_body'].style.color = 'white'; window['popup_loading_body'].style.textAlign = 'center'; window['popup_loading_body'].style.paddingTop = '50vh';
          window['popup_loading_body'].innerHTML = "<div style='font-size:50px'><i class='fas fa-spinner fa-spin' style='margin-right:10px'></i>Loading...</div>";
          document.body.appendChild(window['popup_loading_body'])
        } '''

    return '''if (typeof window['popup_loading_body'] !== 'undefined'){document.body.removeChild(window['popup_loading_body']); window['popup_loading_body'] = undefined}'''

  def add_template(self, css):
    """
    Description:
    ------------
    Add an extra layer

    Usage:
    -----

    Attributes:
    ----------
    :param css: Dictionary.
    """
    self.header = self._report.ui.div()
    self.header.options.managed = False
    self.header.style.clear_all()
    self.footer = self._report.ui.div()
    self.footer.options.managed = False
    self.footer.style.clear_all()
    self.template = self._report.ui.div()
    self.template.options.managed = False
    self.template.style.clear_all()
    self.template.css(css)
    return self

  def __str__(self):
    if hasattr(self, 'template'):
      self.template._vals = str(self._html_content)
      return '<body %s>%s%s%s</body>' % (self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self.header.html(), self.template.html(), self.footer.html())

    return '<body %s>%s</body>' % (self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self._html_content)
