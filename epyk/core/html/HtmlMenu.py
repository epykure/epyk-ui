
import json
import logging

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.styles import GrpClsMenu
from epyk.core.css import Defaults_css


class HtmlNavBar(Html.Html):
  name, category = 'Nav Bar', 'System'

  def __init__(self, report, components, width, height, options, profile):
    super(HtmlNavBar, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component

    :rtype: GrpClsMenu.ClassNav
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassNav(self)
    return self._styleObj

  def move(self):
    """

    """
    super(HtmlNavBar, self).move()
    self.style.css.position = None
    self._report.body.style.css.padding_top = 0

  def __add__(self, htmlObj):
    """ Add items to the footer """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    htmlObj.style.css.display = 'inline'
    if htmlObj.css('height') is None:
      htmlObj.style.css.vertical_align = 'middle'
    if htmlObj.css('width') == '100%':
      htmlObj.style.css.width = None
    self.val.append(htmlObj)
    return self

  def add_text(self, text):
    """

    :param text:
    :return:
    """
    val = self._report.ui.text(text)
    self.__add__(val)
    val.style.css.height = "100%"
    val.style.css.vertical_align = 'middle'
    return val

  def __str__(self):
    str_h = "".join([h.html() for h in self.val])
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_h)


class HtmlFooter(Html.Html):

  def __init__(self, report, components, width, height, profile):
    super(HtmlFooter, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__col_lst = None
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)

  @property
  def sections(self):
    if not self.__col_lst:
      self.__col_lst = []
    return self.__col_lst

  @sections.setter
  def sections(self, col_lst):
    self.__col_lst = col_lst

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component

    :rtype: GrpClsMenu.ClassFooter
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassFooter(self)
    return self._styleObj

  def __add__(self, htmlObj):
    """ Add items to the footer """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.val.append(htmlObj)
    return self

  def __getitem__(self, i):
    """
    Return the internal column in the row for the given index

    :param i: the column index
    """
    return self.val[i]

  def add_menu(self):
    pass

  def __str__(self):
    str_h = "".join([val.html() for val in self.val])
    return "<footer %s>%s</footer>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_h)
