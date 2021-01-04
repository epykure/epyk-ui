#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptPanel
from epyk.core.js.packages import JsQuery


class Popup(Html.Html):
  requirements = ('bootstrap', )
  name = 'Popup Container'

  def __init__(self, report, components, width, height, options, profile):
    super(Popup, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__max_height, self.width, self.title = (100, "%"), width, None
    self.__options = OptPanel.OptionPopup(self, options)
    if not isinstance(components, list):
      components = [components]
    for component in components:
      self.__add__(component)
    if self.options.background:
      #self.frameWidth = "%s%s" % (width[0], width[1])
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)', 'left': 0, 'top': 0})
      self.css({'display': 'none', 'z-index': '1000', 'text-align': 'center', #'padding-left': self.options.margin, 'padding-right': self.options.margin
                })
    else:
      #self.frameWidth = "100%"
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': '10000'})

    if self.options.draggable:
      self.draggable(source_event=JsQuery.decorate_var(self.dom.querySelector("#%s_content" % self.htmlCode)))
    self.set_attrs(name="name", value="report_popup")
    self.keyup.escape(self.dom.hide().r, source_event="document")
    self.window = self._report.ui.div()
    self.window.options.managed = False
    self.window.style.background = "white"
    self.window.style.position = "absolute"
    self.window.style.margin = "auto"
    self.window.style.height = "80%"
    self.window.style.width = "80%"
    self.window.style.top = 0
    self.window.style.bottom = 0
    self.window.style.left = 0
    self.window.style.right = 0

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptPanel.OptionPopup
    """
    return self.__options

  def container_max_height(self, size, unit="px"):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param size:
    :param unit: String. Optional.
    """
    self.__max_height = (size, unit)
    return self

  def add_title(self, text, align='center', level=None, css=None, position="before", options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param text: String.
    :param align: String. Optional.
    :param level: Integer. Optional
    :param css:
    :param position:
    :param options:
    """
    if not hasattr(text, 'options'):
      self.title = self._report.ui.texts.title(text, align=align, level=level, options=options)
      self.title.style.css.margin_top = -3
    else:
      self.title = text
    return self

  def html(self):
    """
    Description:
    ------------


    Usage:
    -----

    """
    if self.options.background:
      self.style.css.padding_top = self.options.top
    if self.__options.closure:
      icon = self._report.ui.icon(self.__options.closure)
      icon.style.css.font_factor(5)
      icon.style.css.background_color = self._report.theme.greys[0]
      icon.style.css.border_radius = 20
      icon.style.css.top = -10
      icon.style.css.z_index = 1010
      icon.style.css.right = -7
      icon.style.css.position = 'absolute'
      icon.options.managed = False
      icon.click([self.dom.hide()])
      self.window.add(icon)
    container = self._report.ui.div(width=(100, '%'), height=(100, '%'))
    if self.title is not None:
      self.title.options.managed = False
      container.add(self.title)
    container.options.managed = False
    container.style.css.position = 'relative'
    container.style.css.overflow = "auto"
    container.style.css.padding = "auto"
    container.style.css.vertical_align = "middle"
    for val in self.val:
      if hasattr(val, 'options'):
        container.add(val)
    self.window.add(container)
    content = self.window.html()
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), content)
