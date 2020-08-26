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
    self.__max_height, self.width, self.__title = (100, "%"), width, None
    self.__options = OptPanel.OptionPopup(self, options)
    if not isinstance(components, list):
      components = [components]
    for component in components:
      self.__add__(component)
    if self.options.background:
      self.frameWidth = "%s%s" % (width[0], width[1])
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)', 'left': 0, 'top': 0, 'margin': 'auto'})
      self.css({'display': 'none', 'z-index': '10000', 'text-align': 'center', 'padding-left': self.options.margin, 'padding-right': self.options.margin})
    else:
      self.frameWidth = "100%"
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': '10000'})

    if self.options.draggable:
      self.draggable(source_event=JsQuery.decorate_var(self.dom.querySelector("#%s_content" % self.htmlCode)))
    self.set_attrs(name="name", value="report_popup")
    self.keyup.escape(self.dom.hide().r, source_event="document")

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionPopup
    """
    return self.__options

  def container_max_height(self, size, unit="px"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param size:
    :param unit:
    """
    self.__max_height = (size, unit)
    return self

  def add_title(self, text, level=None, css=None, position="before", options=None):
    """

    :param text:
    :param level:
    :param css:
    :param position:
    :param options:
    """
    if not hasattr(text, 'options'):
      self.__title = self._report.ui.texts.title(text, level=level, options=options)
    else:
      self.__title = text
    return self

  def html(self):
    closePopup = ""
    if self.options.background:
      self.style.css.padding_top = self.options.top
    if self.__options.closure:
      icon = self._report.ui.icon(self.__options.closure)
      icon.style.css.font_factor(5)
      icon.style.css.background_color = self._report.theme.greys[0]
      icon.style.css.border_radius = 20
      icon.options.managed = False
      icon.click([self.dom.hide()])
      closePopup = icon.html()
    trTitle = ''
    if self.__title is not None:
      self.__title.options.managed = False
      self.__title.style.css.color = self._report.theme.greys[0]
      trTitle = self.__title.html()
    str_html = "\n".join([val.html() if hasattr(val, 'html') else str(val) for val in self.val])
    content = '''
      <table id="%(htmlCode)s_table" style="width:%(frameWidth)s;margin:auto">
        %(title)s
        <tr>
          <td style="padding:10px;background:%(bgcolor)s">
            <div style="position:relative;float:right;right:-15px;top:-20px">%(closePopup)s</div>
            <div  class='scroll_content' id="%(htmlCode)s_content" style="overflow:auto;width:100%%;max-height:%(height)s">%(objects)s</div>
          </td>
        </tr>
      </table>''' % {'title': trTitle, 'htmlCode': self.htmlCode, 'objects': str_html, 'height': "%s%s" % (self.__max_height[0], self.__max_height[1]),
                     "frameWidth": self.frameWidth, 'closePopup': closePopup, 'bgcolor': self._report.theme.greys[0]}
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.style.get_classes()), content)
