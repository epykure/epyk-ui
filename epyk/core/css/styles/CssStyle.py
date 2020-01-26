"""
Base class for the CSS Style modules
"""

import os
import sys
import logging
import inspect
import importlib

from epyk.core.css import Defaults


# The CSS module factory in charge of storing all the available styles in the framework
factory = None


def get_style(css_attrs):
  """
  Return the CSS String to be added to the tag of an HTML component

  :param css_attrs: A python dictionary with the CSS attributes

  :return: The css style string
  """
  return "; ".join(["%s:%s" % (k, v) for k, v in css_attrs.items()])


def cssName(cssRef):
  """
  CSS Framework

  Standard classname convention used in the framework internally.
  Basically before creating a CSS class, and in order to avoid clashes the framework will add a prefix py_.

  :param cssRef: The original classname

  :return: The classname string

  #TODO: Check that all the HTML Objects are using self.pyStyle instead of self.__pyStyle
  """
  cssName = cssRef.lower()
  if cssName.startswith("py_"):
    return cssName

  return "py_%s" % cssName


def load(reset=False):
  """
  CSS Factory

  Load the factory with the all the different CSS classes defined in the framework

  :param reset: Boolean to force the factory to be reloaded
  :return: The CSS factory
  """
  global factory

  if factory is None or reset:
    path = os.path.abspath(__file__)
    dirPath = os.path.dirname(path)
    sys.path.append(dirPath)
    tmpFactory = {}
    for pyFile in os.listdir(dirPath):
      if pyFile == 'CssStyle.py':
        continue

      if pyFile.endswith(".py") and pyFile != '__init__.py':
        try:
          pyMod = importlib.import_module("epyk.core.css.styles.%s" % pyFile.replace(".py", ""))
          for name in dir(pyMod):
            clssName = getattr(pyMod, name)
            if inspect.isclass(clssName):
              if clssName.__name__.startswith("Css"):
                tmpFactory[str(name)] = {'class': clssName, 'file': pyFile}
        except Exception as e:
          # unexpected issue in the factor (A new class might be wrong)
          logging.warning(e)

    # TODO: Think about a better implementation
    # Atomic action to update the factor
    # the above if statement should remain very quick as it might be a source of synchronisation issues in the future
    factory = tmpFactory
  return factory


def getCssObj(clsName, context=None, colors=None):
  """
  Load a CSS Python class from the Factory

  Example:
    - getCssObj('CssButtonBasic')
    - getCssObj('CssButtonBasic', colors={'colors': {9: 'orange'}}) # -1 can be used as well

  :param clsName: The CSS Python class Name
  :param context: The underlying Framework object
  :param colors: The color rules to be overridden
  :return: The CSS Python object
  """
  global factory

  load()
  cls = factory.get(clsName)
  if cls is not None:
    if 'class' in cls:
      return cls['class'](context, colors=colors, theme=context.theme)
    if 'object' in cls:
      return cls['object']

  return None


def setCssObj(clsName, css_attrs, context, force_reload=False):
  """
  CSS Factory

  Load the CSS object factory from the available CSS classes and return the one requested.
  This will also provide some options in order to override the object attributes.

  All the different overrides should be done according to the CSS official definition.
  Indeed this will be directly converted to CSS and added to the result page

  :param clsName: The CSS classname as a string
  :param css_attrs: A Python dictionary with all the CSS attributes
  :param context: The context object
  :param force_reload:

  :return:
  """
  global factory

  load()
  if not clsName in factory or force_reload:
    factory[clsName] = {'object': css_attrs}
  return getCssObj(clsName, context)


class CssCls(object):
  """
  CSS Base class of all the derived styles

  Main class to create from the Python CSS Framework well defined CSS Fragment which will be added to the page.
  Each CSS Class create will produce a Class Name and it will be the one used in all the HTML components to set the Style.
  This module will only consider the Static CSS classes and all the bespoke CSS Style used to defined more specifically a component will
  be defined either in the string method of the component (old way) or in the jsStyle variable of the component (new way)

  :TODO:
    work on a way to optimize the CSS String generated in the header
    example: http://www.cssportal.com/css-optimize/
  """
  attrs, reqCssCls, cssId, name = None, None, None, None

  preceedTag, parentTag, childrenTag, directChildrenTag, htmlTag = None, None, None, None, None
  childKinds, _is_media = None, False

  # Default values for the style in the web portal
  fontSize, headerFontSize, fontFamily = '12px', '14px', 'Calibri'

  def __init__(self, context=None, colors=None, theme=None):
    self.rptObj = context
    self.setId({} if self.cssId is None else self.cssId)
    self.style, self.colorsCalc, self.theme = {}, colors, theme
    if self.reqCssCls is not None:
      for css in self.reqCssCls:
        self.style.update(getattr(css, 'attrs', {}))
    self.style.update(dict(self.attrs) if self.attrs is not None else {})
    self.eventsStyles = {}
    for state in ['hover', 'active', 'checked', 'disabled', 'empty', 'enabled', 'focus', 'link', 'visited', 'after', 'before']:
      self.eventsStyles[state] = getattr(self, state, {})
    if self.childKinds is not None: # To add CSS Style link tr:nth-child(even)
      if not isinstance(self.childKinds, list):
        self.childKinds = [self.childKinds]
      for childKind in self.childKinds:
        self.eventsStyles["%(type)s%(value)s" % childKind] = childKind['style']
    self.customize(self.style, self.eventsStyles)

  def customize(self, style, events_styles):
    """
    CSS Style Builder

    Function defined to override or define the static CSS parameters when an CSS Style python object is instanciated.
    This will allow for example to define the color according to the standard ones without hard coding them.
    In the base class this method is not defined

    :param style: A dictionary with the CSS attributes used to define the class
    :param events_styles: A dictionary of dictionary with all the CSS special attributes
    """
    pass

  def media(self, style, events_styles):
    """
    CSS style specific for the smaller screens like tablets and smartphones

    Example:
    def media(self, style, eventsStyles):
      return {
        'attrs': {'border': "1px solid green"},
        'hover': {"background-color": 'yellow'}
      }

    :param style: A python dictionary. The CSS Styles
    :param events_styles: A nested python dictionary. The event CSS Styles

    :return: A dictionary with the specific styles
    """
    pass

  def events(self):
    """
    CSS Style Builder

    Function used to define for a given class name all the different mouse and event properties that the CSS could allowed.
    This private method will check the static definition and create the entry in the Python CSS Class.
    This will allow to define in the framework some events like hover, focus...
    Only the following selector are defined so far ('hover', 'active', 'checked', 'disabled', 'empty', 'enabled', 'focus', 'link', 'visited', 'after', 'before')

    Documentation
    https://www.w3schools.com/cssref/css_selectors.asp

    :return: A python dictionary with all the Css class object events
    """
    css_event = {}
    for state, cssRecord in self.eventsStyles.items():
      if cssRecord is None or len(cssRecord) == 0:
        continue

      css_event[state] = self.toCss(cssRecord)
    return css_event

  # -------------------------------------------------------------------------------
  #                                    CSS ID SYNTHAX
  #
  # https://www.w3schools.com/css/css_syntax.asp
  # -------------------------------------------------------------------------------
  @property
  def classname(self):
    """
    CSS function

    Property to convert the CSS Class Name to a standardized Class Name within this Python Framework

    :return: A string with the converted name
    """
    if self.name is None:
      self.name = cssName(self.__class__.__name__)
    return self.name

  def setId(self, cssId):
    """
    CSS function

    Global method to define the CSS ID for a given CSS Configuration class

    :return: The CSS Id as a String
    """
    if 'reference' in cssId: # Shortcut to set directly the name of the CSS class
      self.cssId = cssId['reference']
      return self.cssId

    css_id_parts = []
    if 'parent' in cssId:
      css_id_parts.append("%s > " % cssId['parent'])
    elif 'preceed' in cssId:
      css_id_parts.append("%s ~ " % cssId['preceed'])

    if 'id' in cssId:
      css_id_parts.append("#%s" % cssId['id'])
    else:
      if 'tag' in cssId:
        if cssId['tag'].startswith(":"):
          css_id_parts.append(".%s%s" % (self.classname, cssId['tag']))
        else:
          css_id_parts.append("%s.%s" % (cssId['tag'], self.classname))
      elif 'direct' in cssId:
        css_id_parts.append(".%s > %s" % (self.classname, cssId['direct']))
      elif 'child' in cssId:
        css_id_parts.append(".%s %s" % (self.classname, cssId['child']))
      else:
        css_id_parts.append(".%s" % self.classname)
    if 'type' in cssId:
      css_id_parts.append("[%s=%s]" % (cssId['type'][0], cssId['type'][1]))
    self.cssId = ''.join(css_id_parts)
    return self.cssId

  def getStyles(self, media=False, to_str=True):
    """
    CSS Style Builder.

    This will always return the original CSS styles. No override will be applied at this level.

    To get the current value of a style, the getStyles() of the CSS object should be used instead

    Example
    >>> cssCls = getCssObj('CssButtonBasic', colors={'colors': {9: 'orange'}})
    >>> cssCls.getStyles()['.py_cssbuttonbasic:focus']
    '{ outline: 0; }'

    Function to process the Static CSS Python configuration and to convert it to String fragments following the CSS Web standard.

    :param media: Optional. Boolean
    :param to_str: Optional. Flag to convert the CSS style to a valid CSS string object. Default True

    :return: A Python dictionary with all the different styles and selector to be written to the page for a given Python CSS Class
    """
    res = {}
    if media:
      media_event_styles = {}
      for evt, val in self.eventsStyles.items():
        media_event_styles[evt] = dict(val)
      media_styles = self.media(dict(self.style), media_event_styles)
      if media_styles is not None:
        if 'attrs' in media_styles:
          res[self.cssId] = self.toCss(media_styles['attrs'])
          del media_styles['attrs']

        for key, val in media_styles.items():
          skey = "::" if "::" in ['before', 'after'] else ":"
          res["%s%s%s" % (self.cssId, skey, key)] = self.toCss(val)
    else:
      if self.childrenTag is not None:
        res["%s %s" % (self.cssId, self.childrenTag)] = self.toCss(self.style)
        for key, val in self.events().items():
          skey = "::" if "::" in ['before', 'after'] else ":"
          res["%s %s%s%s" % (self.cssId, self.childrenTag, skey, key)] = val
      elif self.directChildrenTag is not None:
        res["%s > %s" % (self.cssId, self.directChildrenTag)] = self.toCss(self.style)
        for key, val in self.events().items():
          skey = "::" if "::" in ['before', 'after'] else ":"
          res["%s > %s%s%s" % (self.cssId, self.directChildrenTag, skey, key)] = val
      else:
        if len(self.style) > 0:
          # Remove the CSS Python classes without main CSS definition (e.g: [contenteditable])
          res[self.cssId] = self.toCss(self.style) if to_str else self.style
        for key, val in self.events().items():
          skey = "::" if "::" in ['before', 'after'] else ":"
          res["%s%s%s" % (self.cssId, skey, key)] = val
    return res

  def getStyleId(self, html_reference):
    """
    CSS Style Builder

    Produce based on the CSS Python classes the correct CSS Name

    :param html_reference:

    return: Returns the CSS part to be written in the page by HTML tag
    """
    htmlId = "#%s" % html_reference
    css_data = str(self)
    if htmlId in self.cssObj.cssStyles:
      if self.cssObj.cssStyles[htmlId] != css_data:
        raise Exception("CSS style conflict for %s" % html_reference)

    self.cssObj.cssStyles[htmlId] = css_data

  def getStyleTag(self, html_tag):
    """
    CSS Style Builder

    Produce based on the CSS Python classes the correct CSS Name

    :param html_tag:

    return: Returns the CSS part to be written in the page by HTML tag
    """
    self.cssObj.cssStyles[html_tag] = self.toCss(self.style)

  def getStyleCls(self, clss, html_type=None):
    """
    CSS Style Builder

    Produce based on the CSS Python classes the correct CSS Name with the right class selector

    Documentation
    https://www.w3schools.com/cssref/sel_class.asp

    :param html_type:

    return: Returns the CSS part to be written in the page by class name
    """
    if html_type is not None:
      self.cssObj.cssStyles["%s.%s" % (html_type, clss)] = self.toCss(self.style)
    else:
      self.cssObj.cssStyles[".%s" % clss] = self.toCss(self.style)

  def getStyleName(self, html_type, name):
    """
    CSS Style Builder

    Add the CSS Fragment for a very bespoke CSS configuration based on HTML item names.
    This can be used when only some components with the tag (or not) are impacting by a CSS Style

    :param html_type:

    :return: Returns the CSS part to be written in the page by class name
    """
    self.cssObj.cssStyles["%s[name='%s']" % (html_type, name)] = self.toCss(self.style)

  def css(self, attr, value=None, event_attrs=None):
    """
    Update a pre defined CSS style. This function is working in the same way than the css jquery function.

    Example:
    cssCls.css('color', 'blue')
    cssCls.css({'color': 'blue'}, eventAttrs={'color': 'red'})

    :param attr: The CSS key or the CSS dictionary to add to the class
    :param value: The CSS value for the given key
    :param event_attrs:

    :return: The cssCls Object
    """
    if isinstance(attr, dict) and value is None:
      self.style.update(dict([(k, v) for k, v in attr.items() if v if not None]))
    else:
      self.style[attr] = value
    if event_attrs is not None:
      for event, cssDef in event_attrs.items():
        self.eventsStyles[event].update(cssDef)
    return self

  def __add__(self, css_style):
    """
    CSS Style Builder

    Override the CSS style attributes with the new CSS object

    :param css_style: A Python CSS Style object

    :return: The cssCls Object
    """
    self.style.update(css_style.style)
    for event, css in css_style.eventsStyles.items():
      self.eventsStyles[event].update(css)
    return self

  # def getColor(self, name, index):
  #   """
  #   CSS Color definition
  #
  #   Function dedicated to get a specific hexadecimal color code defined in the active theme
  #
  #   :param name: The color label
  #   :param index: The color index in the list
  #
  #   :return: The hexadecimal color code
  #   """
  #   if self.theme is not None:
  #     color_obj = Color.ColorMaker(self.rptObj, theme=self.theme)
  #   else:
  #     color_obj = Color.ColorMaker(self.rptObj)
  #   if self.colorsCalc is not None and name in self.colorsCalc:
  #     count_category = len(color_obj.get(name))
  #     if index > 0:
  #       inv_index = index - count_category - 1
  #       if index in self.colorsCalc[name]:
  #         return self.colorsCalc[name][index]
  #
  #       elif inv_index in self.colorsCalc[name]:
  #         return self.colorsCalc[name][inv_index]
  #
  #     if index < 0:
  #       inv_index = count_category + index + 1
  #       if index in self.colorsCalc[name]:
  #         return self.colorsCalc[name][index]
  #
  #       elif inv_index in self.colorsCalc[name]:
  #         return self.colorsCalc[name][inv_index]
  #
  #   return color_obj.get(name, index)

  # def color(self, category, index=None, color=None):
  #   """
  #   CSS Color definition
  #
  #   :param category: The color category
  #   :param index: The color index in the list
  #   :param color: The hexadecimal color code
  #
  #   :return: The hexadecimal color code
  #   """
  #   color_obj = Color.ColorMaker(self.rptObj, theme=self.theme)
  #   return color_obj.get(category, index, color)

  @classmethod
  def important(cls, params_css):
    """
    Add the !IMPORTANT flag to all the CSS attributes

    :param params_css: A python dictionary with the CSS attributes

    :return: The CSS attributes with the !IMPORTANT flag
    """
    return dict([(k, "%s !IMPORTANT" % v)for k, v in params_css.items()])

  @classmethod
  def toCss(cls, params_css):
    """
    Convert a Python CSS Class to a well defined CSS Class

    Example:
    CssCls().toCss({"text-align": 'right'})

    :param params_css: A Python dictionary with the CSS content

    :return: the Python String in a CSS format
    """
    return "{ %s; }" % get_style(params_css)

  def clone(self, name):
    """
    CSS Object function

    Create a new CSS object derived from the existing one.

    :param name: The new CSS reference

    :return: The CSS Class
    """
    cls_virtual = type(name, (self.__class__,), {})
    cls_virtual.name = name
    return cls_virtual

  @classmethod
  def delete(self, html_obj):
    """
    Remove the css class from the component defined list of classes

    Return: html_obj.defined to allow the chains
    """
    html_obj.defined.remove([self.__name__])
    return html_obj.defined
