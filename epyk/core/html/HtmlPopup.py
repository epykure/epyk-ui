#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptPanel
from epyk.core.js.packages import JsQuery


class Popup(Html.Html):
  name = 'Popup Container'

  def __init__(self, report, components, width, height, options, profile):
    super(Popup, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptPanel.OptionPopup(self, options)
    if self.options.background:
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)', 'left': 0, 'top': 0})
      self.css({'display': 'none', 'z-index': self.options.z_index, 'text-align': 'center'})
    else:
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': self.options.z_index})
    self.set_attrs(name="name", value="report_popup")
    self.window = self._report.ui.div(width="auto")
    self.window.options.managed = False
    self.window.style.css.padding = 10
    self.window.style.css.border = "3px solid %s" % report.theme.greys[3]
    self.window.style.css.top = "100px"
    self.window.style.css.min_width = "300px"
    self.window.style.css.left = "50%"
    self.window.style.css.transform = "translate(-50%, -50%)"
    self.window.style.css.position = "fixed"
    self.window.style.css.background = "white"
    self.container = report.ui.div(components, width=(100, '%'), height=(100, '%'))
    self.container.options.managed = False
    self.container.style.css.position = 'relative'
    self.container.style.css.overflow = "auto"
    self.container.style.css.padding = "auto"
    self.container.style.css.vertical_align = "middle"
    self.window.add(self.container)
    if not self.options.background and self.options.draggable:
      report.body.onReady([self.window.dom.jquery_ui.draggable()])

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

  def add_title(self, text, align='center', level=None, css=None, position="before", options=None):
    """
    Description:
    ------------
    Add a title to the popup.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String.
    :param align: String. Optional.
    :param level: Integer. Optional
    :param css: Dictionary. Optional.
    :param position: String. Optional.
    :param options:
    """
    if not hasattr(text, 'options'):
      title = self._report.ui.title(text, align=align, level=level, options=options)
      title.style.css.margin_top = -3
    else:
      title = text
    self.container.insert(0, title)
    return self

  def __str__(self):
    if self.options.background:
      self.style.css.padding_top = self.options.top
    if self.options.closure:
      self.close.style.css.font_factor(3)
      self.close.style.css.background_color = self._report.theme.greys[0]
      self.close.style.css.border_radius = 20
      self.close.style.css.top = 5
      self.close.style.css.z_index = self.options.z_index + 10
      self.close.style.css.right = 5
      self.close.style.css.position = 'absolute'
      self.close.click([self.dom.hide()])
      self.window.add(self.close)
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.window.html())
