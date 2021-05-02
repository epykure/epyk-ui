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
except ImportError:  # For Python 2
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
def deprecated(comment):
  """
  Description:
  -----------
  This is a decorator which can be used to mark functions as deprecated. It will result in a warning being emitted
  when the function is used.

  Attributes:
  ----------
  :param func: Function. A python function.
  """

  def decorator(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
      logging.warn('#########################################')
      logging.warn("Call to deprecated function {}.".format(func.__name__))
      logging.warn("Action => {}.".format(comment))
      logging.warn('#########################################')
      return func(*args, **kwargs)

    return new_func
  return decorator


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
      component = func(*args, **kwargs)
      if component.page.ui.components_skin is not None:
        shortcuts = {"button": "buttons.button", "title": "texts.title"}
        for sc, msc in shortcuts.items():
          if sc in component.page.ui.components_skin:
            component.page.ui.components_skin[msc] = component.page.ui.components_skin[sc]
        alias = func.__qualname__.lower()
        if alias in component.page.ui.components_skin:
          comp_skin = component.page.ui.components_skin[alias]
          if 'clear' in comp_skin:
            if comp_skin["clear"].get("css"):
              component.style.clear_style()
            if comp_skin["clear"].get("cls"):
              component.style.clear(True)
          component.css(component.page.ui.components_skin[alias].get('css', {}))
          for cls in comp_skin.get("cls", []):
            component.attr["class"].add(cls)
      return component

    return decorated

  return decorator


class Required:
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

    Usage::


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


class EventTouch:

  def __init__(self, page):
    self._page = page

  def start(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchstart event occurs when the user touches an element.

    Note: The touchstart event will only work on devices with a touch screen.

    Tip: Other events related to the touchstart event are:

    Usage::

      start([page.js.alert("Test")])

    Related Pages:

      https://www.w3schools.com/jsref/event_touchstart.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchstart", js_funcs, profile, source_event=source_event)
    return self._page

  def move(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchmove event occurs when the user moves the finger across the screen.

    The touchmove event will be triggered once for each movement, and will continue to be triggered until the finger
    is released.

    Usage::

        move([page.js.alert("Test")])

    Related Pages:

      https://www.w3schools.com/jsref/event_touchmove.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchmove", js_funcs, profile, source_event=source_event)
    return self._page

  def cancel(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchcancel event occurs when the touch event gets interrupted.

    Different devices will interrupt a touch event at different actions, and it is considered good practice to include
    this event to clean up code if this "error" should occur.

    Usage::

        cancel([page.js.alert("Test")])

    Related Pages:

      https://www.w3schools.com/jsref/event_touchcancel.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchcancel", js_funcs, profile, source_event=source_event)
    return self._page

  def end(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    ------------
    The touchend event occurs when the user removes the finger from an element.

    Note: The touchend event will only work on devices with a touch screen.

    Tip: Other events related to the touchend event are:

    Usage::

        end([page.js.alert("Test")])

    Related Pages:

      https://www.w3schools.com/jsref/event_touchend.asp

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self._page.on("touchend", js_funcs, profile, source_event=source_event)
    return self._page

  def swap(self, js_funcs_left, js_funcs_right, profile=False, source_event=None):
    """
    Description:
    ------------
    Add swap event functions.

    Attributes:
    ----------
    :param js_funcs_left: List | String. Javascript functions.
    :param js_funcs_right: List | String. Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    self.start(["window.longTouch = event.touches[0].clientX || event.originalEvent.touches[0].clientX"],
               profile=profile, source_event=source_event)
    self.move(self._page.js.if_("window.longTouch != null", [
      "let swap =  (event.touches[0].clientX || event.originalEvent.touches[0].clientX) - window.longTouch",
      "window.longTouch = null", self._page.js.if_("swap < 0", js_funcs_left).else_(js_funcs_right)], profile=profile),
              source_event=source_event)
    return self


class Components(collections.OrderedDict):

  def css(self, attrs):
    """
    Description:
    -----------
    Set the CSS style for all the inner components.

    Attributes:
    ----------
    :param attrs: Dictionary. The CSS attributes.
    """
    for component in self.values():
      if hasattr(component, "css"):
        component.css(attrs)


class Html:
  """
  Description:
  -----------
  Parent class for all the HTML components. All the function defined here are available in the children classes.
  Child class can from time to time re implement the logic but the function will always get the same meaning (namely
  the same signature and return).
  """
  requirements = None
  builder_name, _js__builder__ = None, None
  _option_cls = Options

  def __init__(self, report, vals, html_code=None, options=None, profile=None, css_attrs=None):
    """ Create an python HTML object """
    # Child component for this component
    self.components = Components()
    self.require = Required(report)
    for package in self.requirements or []:
      if isinstance(package, tuple):
        self.require.add(package[0], package[1])
      else:
        self.require.add(package)

    self.profile = profile
    # Should be renamed by page / and component
    self._report = report
    self._on_ready_js, self._sort_propagate, self._sort_options = {}, False, None
    self._dom, self._sub_htmls, self._js, self.helper, self._styleObj, self.__htmlCode = None, [], None, "", None, None

    self._browser_data = {"mouse": collections.OrderedDict(), 'component_ready': [],
                          'page_ready': collections.OrderedDict(), 'keys': collections.OrderedDict()}

    # to be deleted - because changed should be done only on the component self.require
    self.jsImports = report.jsImports
    self.cssImport = report.cssImport

    self._jsStyles = {}  # to be deleted - because code => htmlCode, _jsStyles should be renamed

    self.innerPyHTML = None  # to be reviewed - not sure this is still useful

    self.__options = self._option_cls(self, options)

    self.attr = {'class': self.style.classList['main'], 'css': self.style.css.attrs}
    if css_attrs is not None:
      self.css(css_attrs)

    if html_code is not None:
      if html_code[0].isdigit() or cleanData(html_code) != html_code:
        raise Exception("htmlCode %s cannot start with a number or contain, suggestion %s " % (
          html_code, cleanData(html_code)))

      if html_code in self._report.components:
        if html_code in ["content", "content_page", "page_nav_bar"]:
          raise Exception("Duplicated Html code '%s', this is used internally in the framework !" % html_code)

        raise Exception("Duplicated Html code '%s' in the script !" % html_code)

      self.__htmlCode = html_code
      if html_code in self._report.inputs:
        vals = self._report.inputs[html_code]

    self._report.components[self.htmlCode] = self
    self._vals = vals
    self.builder_name = self.builder_name if self.builder_name is not None else self.__class__.__name__
    self._internal_components = [self.htmlCode]

  def with_profile(self, profile, event=None, element_id=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param event: String. Optional. The event name.
    :param element_id: String. Optional. A DOM component reference in the page.
    """
    if profile is None and self.profile:
      if event is None:
        return {"name": element_id or self.htmlCode}

      return {"name": "%s[%s]" % (element_id or self.htmlCode, event)}

    if profile is None and self.page.profile:
      if event is None:
        return {"name": element_id or self.htmlCode}

      return {"name": "%s[%s]" % (element_id or self.htmlCode, event)}

    return profile

  def add(self, component):
    """
    Description:
    -----------
    Add items to a container.

    The added HTML component will not be managed by the page by default. This means it might not be visible on the
    JavaScript page if it is not by default managed by the main HTML component.

    For example containers are designed to handle sub components.

    Usage::

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

    Usage::

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
    Unique reference for any HTML component in the framework. This must be defined in the interface and cannot be
    changed in the report.

    This reference can be used in the Python to get the html object from components in the page but it is also
    used in any web framework by the JavaScript to get the DOM object and apply the necessary transformations.

    There is not setter for this property in order to ensure a consistency in Python and JavaScript.

    Usage::

      div = page.ui.div(htmlCode="testDiv")
      print(div.htmlCode)
    """
    if self.__htmlCode is not None:
      return self.__htmlCode

    return "%s_%s" % (self.__class__.__name__.lower(), id(self))

  @property
  def page(self):
    """
    Description:
    -----------
    The unique page on which all the components will be attached to.

    :rtype: Page
    """
    return self._report

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function.

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

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
    Those functions will use plain javascript available for a DOM element by default.
    
    Usage::

      div = page.ui.div(htmlCode="testDiv")
      print(div.dom.content)

    :return: A Javascript Dom object.

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
    
    Usage::

      div = page.ui.div(htmlCode="testDiv")
      div.options.inline = True

    :rtype: Options
    """
    return self.__options

  def prepend_child(self, component, profile=None):
    """
    Description:
    -----------
    Wrapper to the Javascript method insertChild to add an HTML component.

    Usage::

      for i in range(10):
        comp = page.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
        select.prepend_child(comp)

    Related Pages:

      https://www.w3schools.com/jsref/met_node_insertbefore.asp

    Attributes:
    ----------
    :param component: HTML. The html component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: The HTML component.
    """
    self._sub_htmls.append(component)
    self.components[component.htmlCode] = component
    # add a flag to propagate on the Javascript the fact that some child nodes will be added
    # in this case innerHYML cannot be used anymore
    self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
    self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
      self.dom.insertBefore(component.dom)], toStr=True, profile=profile))
    return self

  def append_child(self, component, profile=None):
    """
    Description:
    -----------
    Wrapper to the Javascript method appendChild to append an HTML component.

    Usage::

      for i in range(10):
        component = page.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
        select.append_child(component)

    Related Pages:

      https://www.w3schools.com/jsref/met_node_appendchild.asp

    Attributes:
    ----------
    :param component: HTML. The html component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: The HTML component.
    """
    self._sub_htmls.append(component)
    # add a flag to propagate on the Javascript the fact that some child nodes will be added
    # in this case innerHYML cannot be used anymore
    self._jsStyles["_children"] = self._jsStyles.get("_children", 0) + 1
    self.page.properties.js.add_builders(JsUtils.jsConvertFncs([
      self.dom.appendChild(component.dom)], toStr=True, profile=profile))
    return self

  def onReady(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Add set of event / actions which will be triggered after the build of the object.
    Usually this can be used to add js functions on a chart or a table.

    Usage::

      network = page.ui.charts.vis.network()
      network.onReady([
        network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []}),
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not profile and self.page.profile:
      profile = {"name": "%s[onReady" % self.htmlCode}
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._browser_data['component_ready'].extend(JsUtils.jsConvertFncs(js_funcs, profile=profile))

  def add_menu(self, context_menu):
    """
    Description:
    -----------
    Attach a context menu to an existing component. A context menu must have a component attached to otherwise
    the report will not be triggered.

    Attributes:
    ----------
    :param context_menu: ContextMenu. A Python context menu object.
    """
    context_menu.source = self
    self._report._contextMenu[self.dom.jquery.varName] = context_menu
    return self

  def add_icon(self, text, css=None, position="before", family=None, html_code=None):
    """
    Description:
    ------------
    Add an icon to the HTML object.

    Usage::

      checks.title.add_icon("fas fa-align-center")

    Attributes:
    ----------
    :param text: String. The icon reference from font-awesome website.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param family: String. Optional. The icon framework to be used (preferred one is font-awesome).
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).

    :return: The Html object.
    """
    self.icon = ""
    defined_families = ('office-ui-fabric-core', 'material-design-icons', 'font-awesome', 'bootstrap-icons')
    if family is not None and self.options.verbose and family not in defined_families:
      logging.warning("Family %s not defined in %s" % (family, defined_families))

    if text is not None:
      html_code_icon = "%s_icon" % html_code if html_code is not None else html_code
      self.icon = self._report.ui.images.icon(
        text, html_code=html_code_icon, family=family).css({"margin-right": '5px', 'font-size': 'inherit'})
      if position == "before":
        self.prepend_child(self.icon)
      else:
        self.append_child(self.icon)
      if css is not None:
        self.icon.css(css)
    return self

  def add_label(self, text, css=None, position="before", for_=None, html_code=None, options=None):
    """
    Description:
    -----------
    Add an elementary label component.

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
    :param text: String. The label content.
    :param css: Dictionary. Optional. A dictionary with the CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param for_: String. Optional. Specifies which form element a label is bound to.
    """
    self.label = ""
    if text is not None:
      html_code_label = "%s_label" % html_code if html_code is not None else html_code
      self.label = self._report.ui.texts.label(text, options=options, html_code=html_code_label)
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

  def add_span(self, text, css=None, position="before", html_code=None, i=None):
    """
    Description:
    -----------
    Add an elementary span component.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/layering

    Attributes:
    ----------
    :param text: String. The Span content.
    :param css: Dictionary. Optional. The CSS style to be added to the component.
    :param position: String. Optional. The position compared to the main component tag.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param i: Integer. Optional. The index of the span element to be created.
    """
    key_attr = 'span_%s' % i if i is not None else 'span'
    setattr(self, key_attr, '')
    if text is not None:
      html_code_span = "%s_span" % html_code if html_code is not None else html_code
      setattr(self, key_attr, self._report.ui.texts.span(text, html_code=html_code_span))
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
    Add an elementary label component.

    Usage::

      div = page.ui.div()
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
    :param options:
    """
    self.link = ""
    if url is not None or script_name is not None:
      dfl_options = {"name": name} if name is not None else {}
      if options is not None:
        dfl_options.update(options)
      if url is not None:
        self.link = self._report.ui.links.external(text, url, options=dfl_options)
      else:
        self.link = self._report.ui.links.script(text, script_name, report_name, icon=icon, options=dfl_options)
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

    Attributes:
    ----------
    :param text: String. The title content.
    :param level: Integer. Optional. The level of title.
    :param css: Dictionary. Optional. The CSS style to be added to the component.
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

    Attributes:
    ----------
    :param text: String. The title content.
    :param css: Dictionary. Optional. The CSS style to be added to the component.
    :param attrs: Dictionary. Optional. The HTML tag attributes.
    :param position: Dictionary. Optional. Specific Python options available for this component.
    :param options:
    """
    self.input = ""
    if text is not None:
      if options is not None and options.get("autocomplete"):
        input_options = dict(options)
        if 'position' in input_options:
          del input_options['position']
        del input_options['autocomplete']

        self.input = self._report.ui.inputs.autocomplete(text, width=(100, '%'), options=input_options)
        self.input.options.appendTo = "#%s" % self.htmlCode
        self.input.options.position()
      else:
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

    Attributes:
    ----------
    :param flag: Boolean. The state of the checkbox component.
    :param css: Dictionary. Optional. The CSS style to be added to the component.
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

    Attributes:
    ----------
    :param text: String. The helper content.
    :param css: Dictionary. Optional. The CSS style to be added to the component.

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

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :rtype: KeyCodes.KeyCode
    """
    if self._browser_data.get('keys', {}).get('keypress') is None:
      self._browser_data['keys']['keypress'] = KeyCodes.KeyCode(component=self)
    return self._browser_data['keys']['keypress']

  @property
  def keyup(self):
    """
    Description:
    -----------
    The onkeypress event occurs when the user presses a key (on the keyboard).

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
    Description:
    -----------
    Accessible Rich Internet Applications is a [HTML] specification module.
    Web developers MAY use the ARIA role and aria-* attributes on HTML elements.

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

    :returns: Javascript string with the function to get the current value of the component
    """
    return self._vals

  @property
  def content(self):
    """
    Description:
    -----------
    Get the HTML content of the component as a string.
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
    """
    self._report.components.move_to_end(self.htmlCode)

  def css(self, key=None, value=None, reset=False):
    """
    Description:
    -----------
    Change the CSS Style of a main component. This is trying to mimic the signature of the Jquery css function.

    Related Pages:

      http://api.jquery.com/css/

    Attributes:
    ----------
    :param key: String. Optional. The key style in the CSS attributes (Can also be a dictionary).
    :param value: String. Optional. The value corresponding to the key style.
    :param reset: Boolean. Optional. Specify if the CSS styles need to be emptied first.

    :return: The python object itself.
    """
    if key is None and value is None:
      return self.attr['css']

    if reset:
      self.style.css.attrs = {}
      self.attr['css'] = self.style.css.attrs
    # Do not add None value to the CSS otherwise it will break the page on the front end side
    if value is None and isinstance(key, dict):
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

    Usage::

      htmlObj.tooltip("My tooltip", location="bottom")

    Related Pages:

      https://getbootstrap.com/docs/4.1/components/tooltips/

    TODO Change background color

    Attributes:
    ----------
    :param value: String. The tooltip text.
    :param location: String. Optional. The position of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.

    :return: The Python object self.
    """
    if value is not None:
      self.attr.update({'data-toggle': 'tooltip', 'data-html': 'true', 'data-placement': location})
      if options is not None:
        self.attr.update(options)
      self.page.properties.js.add_on_ready(
        "%s.tooltip()" % JsQuery.decorate_var("'[data-toggle=tooltip]'", convert_var=False))
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
    Add a tooltip using Bootstrap Popover feature.

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
      self.page.properties.js.add_on_ready(
        "%s.popover()" % JsQuery.decorate_var("'[data-toggle=popover]'", convert_var=False))
    return self

  def draggable(self, js_funcs=None, options=None, profile=None, source_event=None):
    """
    Description:
    ------------
    Set the component as a draggable item.

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
    return self.on("dragstart", js_funcs + [
      'event.dataTransfer.setData("text", event.target.innerHTML)'], profile=profile, source_event=source_event)

  def sticky(self, anchor, css_attrs=None):
    """
    Description:
    -----------
    Change the CSS style of the component to be sticky on the page.

    This will add a class to the component. It is possible to set some attributes in order to
    change its style.

    Attributes:
    ----------
    :param anchor: Component. the component which will be used to check the position.
    :param css_attrs: Dictionary. Optional. The CSS attributes of the component once sticky.
    """
    if anchor.htmlCode == self.htmlCode:
      raise Exception("Anchor cannot be the moving component")

    css_attrs = css_attrs or {"bottom": "10px", "left": "10px", "height": "200px !IMPORTANT"}
    css_attrs["position"] = "fixed"
    css_vals = "{%s}" % "; ".join(["%s: %s" % (k, v) for k, v in css_attrs.items()])
    cls_name = "sticky_component_%s" % self.page.py.hash(css_vals)
    self.page.properties.css.add_text(".%s %s\n" % (cls_name, css_vals))
    self.page.body.scroll([
      self.page.js.if_(anchor.dom.isInViewPort, [
        self.dom.classList.remove(cls_name)
      ]).else_([
        self.page.js.if_(self.dom.classList.is_missing(cls_name), [
          self.dom.classList.add(cls_name)])])
    ])

  def add_options(self, options=None, name=None, value=None):
    """
    Description:
    -----------
    Change the Javascript options of the component.
    This will change the options sent to the Javascript.

    Attributes:
    ----------
    :param options: Dictionary. Optional. the extra options to be added to the component.
    :param name: String. Optional. The key. The option name.
    :param value: String. Optional. The value. The option value.

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
    Function to update the internal dictionary of object attributes. Those attributes will be used when the HTML
    component will be defined.
    Basically all sort of attributes can be defined here: CSS attributes, but also data, name...
    Either the attrs or the tuple (name, value) can be used to add information to the dom object.

    All the attributes should be Python object which are ready to use on the Javascript side.
    For example True should be written 'true'.

    Tips: It is possible to use the data- attributes to store any kind of information in the dom.

    Related Pages:

      https://www.w3schools.com/html/html_attributes.asp

    Attributes:
    ----------
    :param attrs: Dictionary. Optional. All the HTML tags attributes.
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

    Attributes:
    ----------
    :param withId: Boolean. Optional. Add the ID tag. This is handled by the framework. (Default true)
    :param pyClassNames: List. Optional. The Python class names.

    :return: A string with the dom attributes
    """
    css_style, css_class, class_data = '', '', ''
    if 'css' in self.attr:
      styles = ";".join(["%s:%s" % (key, val) for key, val in self.attr["css"].items()])
      if styles:
        css_style = 'style="%s"' % styles
    if 'class' in self.attr and len(self.attr['class']) > 0 and class_data:
      if pyClassNames is not None:
        # Need to merge in the class attribute some static classes coming from external CSS Styles sheets
        # and the static python classes defined on demand in the header of your report
        # self._report.cssObj.getClsTag(pyClassNames)[:-1] to remove the ' generated in the module automatically
        css_class = self._report.style.getClsTag(pyClassNames.clsMap).replace('class="', 'class="%s ')
        if css_class:
          css_class %= class_data
        else:
          css_class = 'class="%s"' % class_data
      else:
        css_class = 'class="%s"' % class_data
    elif pyClassNames is not None:
      py_cls_names = [cls.get_ref() if hasattr(cls, 'get_ref') else cls for cls in pyClassNames['main']]
      css_class = 'class="%s"' % " ".join(py_cls_names) if len(py_cls_names) > 0 else ""

    if withId:
      self.attr['id'] = self.htmlCode
    html_tags = ['%s="%s"' % (key, str(val).replace('"', "'")) if val is not None else key for key, val in self.attr.items() if key not in ('css', 'class')]
    for tag in [css_style, css_class]:
      if tag:
        html_tags.append(tag)
    str_tag = " ".join(html_tags)
    return str_tag.strip()

  def on(self, event, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    Add an event to the document ready function.
    This is to mimic the Jquery on function.

    Tip: use the r function to not have side effects when Python is building the JavaScript:
      span.on("mouseover", span.dom.css("color", "red").r)
      span.on("mouseleave", span.dom.css("color", "blue"))

    Related Pages:

      https://www.w3schools.com/jquery/event_on.asp
      https://www.w3schools.com/js/js_htmldom_eventlistener.asp
      https://www.w3schools.com/jsref/dom_obj_event.asp

    Attributes:
    ----------
    :param event: String. The Javascript event type from the dom_obj_event.asp.
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.

    :return: self to allow the chains.
    """
    profile = self.with_profile(profile, event=event)
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    source_event = source_event or self.dom.varId
    if event not in self._browser_data['mouse']:
      self._browser_data['mouse'][event] = {}
    self._browser_data['mouse'][event].setdefault(source_event, {}).setdefault("content", []).extend(
      JsUtils.jsConvertFncs(js_funcs))
    self._browser_data['mouse'][event][source_event]['profile'] = profile
    if on_ready:
      self._report.body.onReady([self.dom.events.trigger(event)])
    return self

  def event_fnc(self, event):
    """
    Description:
    ------------
    Function to get the generated JavaScript method in order to then reuse it in other components.
    This will return the event function in a string already transpiled.

    Attributes:
    ----------
    :param event: String. The event function.
    """
    return list(self._browser_data['mouse'][event][self.dom.varId]["content"])

  def drop(self, js_funcs, prevent_default=True, profile=None):
    """
    Description:
    -----------
    Add a drag and drop property to the element.

    Usage::

      d = page.ui.div()
      d.drop([page.js.objects.data.toRecord([1, 2, 3, 4], "result")])

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param prevent_default: Boolean. Optional. Specify if the event should have a default behaviour on the page.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.

    :return: Return self to allow the chaining
    """
    if not profile and self.page.profile:
      profile = {"name": "%s[drop]" % self.htmlCode}
    dft_fnc = ""
    if prevent_default:
      dft_fnc = self._report.js.objects.event.preventDefault()
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_funcs = JsUtils.jsConvertFncs(
      ["var data = %s" % self._report.js.objects.event.dataTransfer.text] + js_funcs, toStr=True, profile=profile)
    # By default change the box shadow of this component
    self.attr["ondrop"] = "(function(event){%s; %s; %s; return false})(event)" % (
      dft_fnc, str_funcs, self.dom.css('box-shadow', 'none').r)
    self.attr["ondragover"] = "(function(event){%s; %s})(event)" % (
      dft_fnc, self.dom.css('box-shadow', 'inset 0px 0px 0px 2px %s' % self._report.theme.success[1]).r)
    self.attr["ondragleave"] = "(function(event){%s; %s})(event)" % (
      dft_fnc, self.dom.css('box-shadow', 'none').r)
    return self

  def hover(self, js_funcs, profile=None, source_event=None):
    """
    Description:
    -----------
    Add an mouse hover event on the component.

    Usage::

      div = page.ui.div()
      div.hover([
        page.js.alert("This is a test")
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    return self.on("mouseover", js_funcs, profile, source_event)

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.

    Usage::

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
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if on_ready:
      self._report.body.onReady([self.dom.events.trigger("click")])
    return self.on("click", js_funcs, profile, source_event)

  def focusout(self, js_funcs, profile=None, source_event=None):
    """
    Description:
    -----------
    The onfocusout event occurs when the user select an element.

    Usage::

      div = page.ui.div()
      div.focusout([
        page.js.alert("This is a test")
      ])

    Related Pages:

      https://www.w3schools.com/jsref/event_onfocusout.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    js_funcs.insert(0, "if(%(dom)s.contains(event.relatedTarget)) {return ;}" % {"dom": source_event or self.dom.varId})
    return self.on("focusout", js_funcs, profile, source_event)

  def dblclick(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    -----------
    The ondblclick event occurs when the user double-clicks on an element.

    Related Pages:

      https://www.w3schools.com/jsref/event_ondblclick.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    :param on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if on_ready:
      self._report.body.onReady([self.dom.events.trigger("dblclick")])
    return self.on("dblclick", js_funcs, profile, source_event)

  def scroll(self, js_funcs, profile=None, source_event=None):
    """
    Description:
    -----------
    The onscroll event occurs when an element's scrollbar is being scrolled.

    Related Pages:

      https://www.w3schools.com/jsref/event_onscroll.asp

    Attributes:
    ----------
    :param js_funcs: List | String. A Javascript Python function.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: String. Optional. The source target for the event.
    """
    return self.on("scroll", js_funcs, profile, source_event)

  def mouse(self, on_funcs=None, out_funcs=None, profile=None, source_event=None):
    """
    Description:
    -----------
    Wrapper function fot the mouse event.
    This function will cover the on mouse hover event and mouse out.

    More specific events are possible using the generic out function.

    Tip: As function are defined to be chaining in most of the components use .r to get the string representation and
    clean the cache.

    Usage::

      span.mouse([
          span.dom.css("color", "red"),
          span.dom.css("cursor", "pointer").r],
        span.dom.css("color", "blue").r)

    Attributes:
    ----------
    :param on_funcs: List | String. Optional. The Javascript events.
    :param out_funcs: List | String. Optional. The Javascript events.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.

    :return: self to allow the chains.
    """
    self.style.css.cursor = 'pointer'
    if on_funcs is not None:
      self.on("mouseenter", on_funcs, profile, source_event)
    if out_funcs is not None:
      self.on("mouseleave", out_funcs, profile, source_event)
    return self

  def paste(self, js_funcs, profile=None, source_event=None):
    """
    Description:
    -----------
    Add a paste event to the component.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | String. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_fncs = JsUtils.jsConvertFncs(
      ["var data = %s" % self._report.js.objects.event.clipboardData.text] + js_funcs, toStr=True)
    return self.on("paste", str_fncs, profile, source_event)

  def contextMenu(self, menu, js_funcs=None, profile=None):
    """
    Description:
    -----------
    Attach a context menu to a component and set a function to called before the display.

    TODO Test context menu

    Attributes:
    ----------
    :param menu:
    :param js_funcs: List | String. Optional. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not hasattr(menu, 'source'):
      menu = self._report.ui.menus.contextual(menu)
    self.context_menu = menu
    menu.source = self
    new_js_funcs = (js_funcs or []) + [
      self._report.js.objects.mouseEvent.stopPropagation(),
      self.context_menu.dom.css({"display": 'block', 'left': self._report.js.objects.mouseEvent.clientX + "'px'",
                                 'top': self._report.js.objects.mouseEvent.clientY + "'px'"}),
      self._report.js.objects.mouseEvent.preventDefault()]
    self.on("contextmenu", new_js_funcs, profile)
    return menu

  @property
  def touch(self):
    """
    Description:
    -----------
    Shortcut property to all the Touch event.

    Events that occur when user touches a touch-based device, belongs to the TouchEvent Object.

    Related Pages:

      https://www.w3schools.com/jsref/obj_touchevent.asp

    Usage::

      component.touch.
    """
    return EventTouch(self)

  def build(self, data=None, options=None, profile=None, component_id=None):
    if not self.builder_name or self._js__builder__ is None:
      raise Exception("No builder defined for this HTML component %s" % self.__class__.__name__)

    self.page.properties.js.add_constructor(self.builder_name, "function %s(htmlObj, data, options){%s}" % (
      self.builder_name, self._js__builder__))
    self.options.builder = self.builder_name

    # check if there is no nested HTML components in the data
    if isinstance(data, dict):
      tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in data.items()]
      js_data = "{%s}" % ",".join(tmp_data)
    else:
      js_data = JsUtils.jsConvertData(data, None)
    fnc_call = "%s(%s, %s, %s)" % (self.builder_name, component_id or self.dom.varId, js_data, self.options.config_js(options))
    profile = self.with_profile(profile, event="Builder")
    if profile:
      fnc_call = JsUtils.jsConvertFncs(
        ["var result = %s(htmlObj, data, options)" % self.builder_name], toStr=True, profile=profile)
      fnc_call = "(function(htmlObj, data, options){%s; return result})(%s, %s, %s)" % (
        fnc_call, self.dom.varId, js_data, self.options.config_js(options))
    return fnc_call

  def refresh(self):
    """
    Description:
    -----------
    Component refresh function. Javascript function which can be called in any Javascript event.

    Tip: This function cannot be used in a plan Python section but in a JavaScript one defined in an event for example.

    """
    return self.build(self.val, None)

  def subscribe(self, socket, channel, data=None, options=None, js_funcs=None, profile=None):
    """
    Description:
    ------------
    Subscribe to a socket channel.
    Data received from the socket are defined as a dictionary with a field data.

    The content of data will be used by this component.

    Related Pages:

      https://timepicker.co/options/

    Attributes:
    ----------
    :param socket: Socket. A python socket object.
    :param channel: String. The channel on which events will be received.
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param js_funcs: List | String. Optional. Javascript functions.
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
        self._on_ready_js['sortable'] = JsSortable.Sortable(
          self, varName="%s_sortable" % self.htmlCode, selector=self.dom.varId, parent=self._report)
        dflt_options = {"group": self.htmlCode}
        dflt_options.update(options or {})
        self._sort_options = dflt_options
        self._on_ready_js['sortable'].create(self.dom.varId, dflt_options)
      return self._on_ready_js['sortable']

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
    """
    return Component.Component(self)

  def html(self):
    """
    Description:
    -----------
    Rendrer the HTML component to the JavaScript.
    This will be the main function called by the page to render all the component.s

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
            'styleUrls': "", "externalVars": "", "componentFunctions": [],
            'htmlTag': "app-epyk-%s" % self.__class__.__name__.lower()}


class Body(Html):
  name = "Body"

  def __init__(self, report, vals, html_code=None, options=None, profile=None, css_attrs=None):
    super(Body, self).__init__(report, vals, html_code, options, profile, css_attrs)
    if Defaults_css.BODY_STYLE is not None:
      for attrs in Defaults_css.BODY_STYLE.split(";"):
        k, v = attrs.split(":")
        self.css(key=k, value=v)
    self._template = None

  @property
  def style(self):
    """
    Description:
    -----------
    A property to the CSS style of the DOM component.
    Each component will have default CSS style but they can be overridden.

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

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(self, report=self._report)
      self._dom.varName = "document.body"
    return self._dom

  def scroll(self, js_funcs, profile=None, source_event=None):
    """
    Description:
    -----------
    The onscroll event occurs when an element's scrollbar is being scrolled.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source target for the event.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._report.js.onReady(
      self._report.js.window.events.addScrollListener(JsUtils.jsConvertFncs(js_funcs, toStr=True)))

  def onReady(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Add set of event / actions which will be triggered after the build of the object.
    usually this can be used to add js functions on a chart or a table.

    Usage::

      network = page.ui.charts.vis.network()
      network.onReady([
        network.js.setData({"nodes": [{"id": 0, "label": "test"}], "edges": []}),
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript function to be added once the object is built.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady(js_funcs)

  def onLoad(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Add a JavaScript function in the builder section which correspond to the JavaScript onload.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.properties.js.add_builders(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))

  def fromConfig(self, js_funcs=None, components=None, lang="eng", end_point="/static/configs", sync=True):
    """
    Description:
    -----------
    Load teh configuration file in order to fill the templates with static data.
    This will allow to externalise the configuration and design rich web templates.

    Do not forget to use CTRL+F5 in order to refresh the browser cache to get the updates.

    Usage::

      title = page.ui.title(html_code="title")
      page.body.onReady([
        page.body.fromConfig(components=[title], end_point="/static", lang=None)
      ])

    Attributes:
    ----------
    :param js_funcs: List | String. Optional. The various transformations to be triggered from the configuration data.
    :param components: List. Optional. The various HTML Components to be updated from the configuration file.
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
        const urlParams = new URLSearchParams(queryString); var lang = urlParams.get('lang') || %(lang)s; 
        rawFile.overrideMimeType("application/json"); 
        if(lang != null){ rawFile.open("GET", "%(url)s/"+ lang +"/%(json)s.json", %(sync)s)}
        else{rawFile.open("GET", "%(url)s/%(json)s.json", %(sync)s)};
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
               var data = JSON.parse(rawFile.responseText); window['page_config'] = data; %(fncs)s}}
        rawFile.send(null)} 
      else {var data = window['page_config']; %(fncs)s}''' % {
      "sync": JsUtils.jsConvertData(not sync, None), "lang": JsUtils.jsConvertData(lang, None), 'url': end_point,
      'json': self._report.json_config_file,
      'fncs': JsUtils.jsConvertFncs(js_funcs + [c.build(self._report.js.objects.get("data['%s']" % c.htmlCode)) for c in components], toStr=True)}

  def set_content(self, page, page_content):
    """
    Description:
    ------------
    Function to allow the templating of the report.
    This can be overridden by a generic class which can be shared within a set of report

    Attributes:
    ----------
    :param page: Report. The main report object.
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

    Usage::

      page.body.set_background("#101626", "#374F67")

    Attributes:
    ----------
    :param start_color: String. Optional. The first code color.
    :param end_color: String. Optional. The last code color.
    :param from_theme: Boolean. Optional. Default to the code colors defined in the theme.
    """
    if from_theme or (start_color is None and end_color is None):
      self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (
        self._report.theme.colors[-1], self._report.theme.colors[2])
    elif end_color is not None:
      self.style.css.background = "linear-gradient(%s 0%%, %s 100%%)" % (start_color, end_color)
    else:
      self.style.css.background = start_color
    self.style.css.background_repeat = "no-repeat"
    self.style.css.background_color = self._report.theme.colors[2]

  def loading(self, status=True, z_index=500):
    """
    Description:
    -----------
    Display a loading page.

    Usage::

      page.body.loading(),
      ...
      page.body.loading(False)

    Attributes:
    ----------
    :param status: Boolean. Optional. A flag to specify the status of the loading event.
    :param z_index: Integer. Optional. Specifies the stack order of an element.
    """
    if status:
      return ''' 
        if (typeof window['popup_loading_body'] === 'undefined'){
          window['popup_loading_body'] = document.createElement("div"); 
          window['popup_loading_body'].style.width = '100%%'; window['popup_loading_body'].style.height = '100%%'; window['popup_loading_body'].style.opacity = 0.3;
          window['popup_loading_body'].style.position = 'fixed'; window['popup_loading_body'].style.top = 0; window['popup_loading_body'].style.left = 0; window['popup_loading_body'].style.zIndex = %s;
          window['popup_loading_body'].style.background = '%s'; window['popup_loading_body'].style.color = 'white'; window['popup_loading_body'].style.textAlign = 'center'; window['popup_loading_body'].style.paddingTop = '50vh';
          window['popup_loading_body'].innerHTML = "<div style='font-size:50px'><i class='fas fa-spinner fa-spin' style='margin-right:10px'></i>Loading...</div>";
          document.body.appendChild(window['popup_loading_body'])
        } ''' % (z_index, self.page.theme.notch())

    return '''if (typeof window['popup_loading_body'] !== 'undefined'){document.body.removeChild(window['popup_loading_body']); window['popup_loading_body'] = undefined}'''

  def add_template(self, css=None, defined_style=None):
    """
    Description:
    ------------
    Add an extra layer.

    Usage::

      page = pk.Page()
      template = page.body.add_template(defined_style="margins")
      template.style.css.background = "white"

    Attributes:
    ----------
    :param css: Dictionary. Optional. The CSS attributes to be added to the HTML component.
    :param defined_style: String. Optional. A predefined style attached to the style property.
    """
    if css is not None:
      self.template.css(css)
    if defined_style is not None:
      getattr(self.template.style.configs, defined_style)()
    return self._template

  @property
  def template(self):
    """
    Description:
    ------------
    Shortcut to the body template component.
    This will just be an intermediate div tag on which all the component will be attached.

    Usage::

      page = pk.Page()
      page.body.template.margins(5)
      page.body.template.style.css.background = "white"
    """
    if self._template is None:
      self.header = self.page.ui.div()
      self.header.options.managed = False
      self.header.style.clear_all()
      self.footer = self.page.ui.div()
      self.footer.options.managed = False
      self.footer.style.clear_all()
      self._template = self.page.ui.div()
      self._template.options.managed = False
      self._template.style.clear_all()
    return self._template

  def __str__(self):
    if getattr(self, '_template', None) is not None:
      self._template._vals = str(self._html_content)
      return '<body %s>%s%s%s</body>' % (
        self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self.header.html(), self.template.html(),
        self.footer.html())

    return '<body %s>%s</body>' % (
      self.get_attrs(pyClassNames=self.style.get_classes(), withId=False), self._html_content)
