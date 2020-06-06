
import collections

from epyk.core.html import Html

from epyk.core.js import expr
from epyk.core.css import Selector

# The list of CSS classes
from epyk.core.css.styles import GrpClsMenu
from epyk.core.html.HtmlList import Li
from epyk.core.html.options import OptList


class HtmlNavBar(Html.Html):
  name = 'Nav Bar'

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
    htmlObj.options.managed = False # Has to be defined here otherwise it is set to late
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
    htmlObj.options.managed = False # Has to be defined here otherwise it is set to late
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
  name = 'Context Menu'
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
    htmlObj.options.managed = False
    li_obj = Li(self._report, htmlObj) if not isinstance(htmlObj, Li) else htmlObj
    li_obj.css({"padding": "5px", 'cursor': 'pointer'})
    if hasattr(htmlObj, 'inReport'):
      htmlObj.options.managed = False
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


class PanelsBar(Html.Html):
  name = 'Pabel'

  def __init__(self, report, width, height, options, helper, profile):
    super(PanelsBar, self).__init__(report, None, css_attrs={"width": width, "height": height})
    self.menus = report.ui.div(options={'inline': True})
    self.menus.options.managed = False
    self.panels = report.ui.div()
    self.panels.options.managed = False
    self.menu_mapping = collections.OrderedDict()
    #
    self.panels.style.css.display = False
    self.panels.style.css.position = 'absolute'
    #
    self.style.css.position = 'relative'
    self.__options = options
    if options.get('position', 'top') == 'top':
      self.panels.style.css.padding_bottom = 10
      self.menus.style.css.top = 0
      self.panels.style.css.border_bottom = '1px solid %s' % report.theme.colors[-1]
    else:
      self.style.css.position = 'relative'
      self.panels.style.css.border_top = '1px solid %s' % report.theme.colors[-1]
      self.panels.style.css.bottom = 0
      self.menus.style.css.bottom = 0

    self.menus.style.css.position = 'absolute'
    self.menus.style.css.background = report.theme.colors[-1]
    self.menus.style.css.color = report.theme.colors[0]
    self.menus.style.css.padding = '5px 0'

  def add_panel(self, text, content):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param content:
    """
    content.style.css.padding = "0 5px"
    if not hasattr(text, 'htmlCode'):
      text = self._report.ui.div(text)
    text.style.css.display = 'inline-block'
    text.style.css.width = 'auto'
    text.style.css.cursor = 'pointer'
    text.style.css.padding = '0 5px'
    self.menu_mapping[text] = content
    self.menus += text
    self.panels += content
    return self

  def __str__(self):
    css_menu = {"height": "auto", 'display': 'block', 'margin-top': '30px'} if self.__options['position'] == 'top' else {"height": "auto", 'display': 'block', 'margin-bottom': '30px'}
    for menu_item, panel in self.menu_mapping.items():
      menu_item.click([
        self._report.js.querySelectorAll(Selector.Selector(self.panels).with_child_element("div").excluding(panel)).css({"display": 'none'}),
        #
        expr.if_(self._report.js.querySelector(Selector.Selector(self.panels)).getAttribute("data-panel") == menu_item.htmlCode, [
          self._report.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel", ""),
          self._report.js.querySelector(Selector.Selector(self.panels)).css({"display": 'none'})
        ]).else_([
          self._report.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel", menu_item.htmlCode),
          self._report.js.querySelector(Selector.Selector(self.panels)).css(css_menu),
          self._report.js.querySelector(Selector.Selector(panel)).css({'display': 'block'})
        ])
      ])

    return "<div %s>%s%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.menus.html(), self.panels.html())
