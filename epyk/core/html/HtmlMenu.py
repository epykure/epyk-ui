
from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.styles import GrpClsMenu
from epyk.core.html.HtmlList import Li
from epyk.core.html.options import OptList


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


class ContextMenu(Html.Html):
  name, category, callFnc = 'Context Menu', None, 'contextmenu'
  source = None # The container

  def __init__(self, report, recordSet, width, height, visible, options, profile):
    super(ContextMenu, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptList.OptionsLi(self, options)
    self.css({'display': 'block' if visible else 'none', 'position': 'absolute', 'z-index': 200,
              'padding': 0, 'margin': 0, 'background-color': self._report.theme.greys[0],
              'border': '1px solid %s' % self._report.theme.success[0], 'border-radius': '2px'
              }
             )
    self.style.css.shadow_box()
    for rec in recordSet:
      self += rec

  @property
  def options(self):
    """

    :rtype: OptList.OptionsLi
    """
    return self.__options

  def add_item(self, value, icon=None):
    """

    :param value:
    :param icon:
    """
    self += {"value": value, 'icon': icon}
    return self

  def __add__(self, htmlObj):
    """

    :param d:
    """
    if not hasattr(htmlObj, 'inReport'):
      if isinstance(htmlObj, dict):
        if htmlObj['icon'] is not None:
          i = self._report.ui.icon(htmlObj['icon'])
          i.css({'display': 'inline', 'margin-right': '5px'})
          v = self._report.ui.text(htmlObj['value'])
          v.css({'display': 'inline'})
          htmlObj = self._report.ui.div([i, v])
        else:
          htmlObj = self._report.ui.div(htmlObj['value'])
      else:
        htmlObj = self._report.ui.div(htmlObj)
    htmlObj.inReport = False
    li_obj = Li(self._report, htmlObj) if not isinstance(htmlObj, Li) else htmlObj
    li_obj.css({"padding": "5px", 'cursor': 'pointer'})
    if hasattr(htmlObj, 'inReport'):
      htmlObj.inReport = False
    self.val.append(li_obj)
    return self

  def __getitem__(self, i):
    return self.val[i].val

  def __str__(self):
    #self._report._scroll.add("$('nav[name=context_menus]').hide()")
    # TODO: Add a condition in the init to display the context menu only for some columns or rows when table for example
    if getattr(self, 'source') is None:
      raise Exception("Context Menu should be added to a component with the function contextMenu")

    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    self.mouse(out_fncs=[self.dom.hide()]) # hide when mouse leave the component
    return '''
      <nav %(attr)s name='context_menus'>
        <ul style='list-style:none;padding:0px;margin:0'>%(val)s</ul>
      </nav>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': str_vals}
