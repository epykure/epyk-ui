#!/usr/bin/python
# -*- coding: utf-8 -*-

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

  def __init__(self, report, components, width, height, options, html_code, profile):
    super(HtmlNavBar, self).__init__(report, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                     profile=profile, options=options)
    self.scroll, self.background = None, True
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)
    self.buttons = []

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: GrpClsMenu.ClassNav
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassNav(self)
    return self._styleObj

  def move(self):
    """
    Description:
    -----------
    Move the object to this position in the final page.
    """
    super(HtmlNavBar, self).move()
    self.style.css.position = None
    self._report.body.style.css.padding_top = 0

  def __add__(self, component):
    """ Add items to the footer """
    if not hasattr(component, 'options'):
      component = self._report.ui.div(component)
      component.style.add_classes.div.color_hover()
      component.style.css.user_select = "none"
      component.style.css.margin_left = 5
      component.style.css.margin_right = 5
      component.style.css.cursor = "pointer"
    # Has to be defined here otherwise it is set to late
    component.options.managed = False
    component.style.css.display = 'inline'
    if component.css('height') is None:
      component.style.css.vertical_align = 'middle'
    if component.css('width') == '100%':
      component.style.css.width = None
    self.val.append(component)
    if hasattr(self, 'buttons'):
      self.buttons.append(component)
    return self

  def no_background(self, to_top=True):
    """
    Description:
    -----------
    remove the default navigation bar background and remove the padding.

    Attributes:
    ----------
    :param to_top: Boolean. Optional. To define if the padding must be removed.
    """
    self.background = False
    self.style.css.background_color = "#11ffee00"
    self.style.css.border_bottom = None
    if to_top:
      self._report.body.style.css.padding_top = 0
    return self

  def set_theme(self):
    """
    Description:
    -----------

    """
    self.style.css.background_color = self._report.theme.colors[0]
    self.style.css.border_bottom = "1px solid %s" % self._report.theme.greys[0]

  def add_right(self, component, css=None):
    """
    Description:
    -----------
    Add component to the right.

    Attributes:
    ----------
    :param component: HTML. Internal component to the framework
    :param css: Dictionary. Optional. The CSS attributes
    """
    if not hasattr(component, 'options'):
      component = self._report.ui.text(component, width=("auto", ''))
      component.style.add_classes.div.color_hover()
      component.style.css.margin_left = 5
      component.style.css.user_select = "none"
      component.style.css.margin_right = 5
      component.style.css.cursor = "pointer"
      component.options.managed = False
      if css is not None:
        component.css(css)
    if not hasattr(self, '_right'):
      self._right = self._report.ui.div(width=("auto", ''))
      self._right.style.css.display = 'inline-block'
      self._right.style.css.float = 'right'
      self._right.style.css.font_factor(0)
      self._right.options.managed = False
      self._vals.append(self._right)
    self._right.add(component)
    self.buttons.append(component)
    return self

  def add_text(self, text):
    """
    Description:
    -----------
    Add an item to the nav bar.

    Attributes:
    ----------
    :param text: String | HTML. The link to be added to the navbar.
    """
    if not hasattr(text, 'options'):
      text = self._report.ui.text(text)
      text.style.css.height = "100%"
      text.style.css.vertical_align = 'middle'
    self.__add__(text)
    return text

  def __str__(self):
    if self.scroll is not None:
      self.val.append(self.scroll)
      if self.scroll.css('width') == '100%':
        self.scroll.style.css.width = None
    str_h = "".join([h.html() for h in self.val])
    if self.style.css.position != 'fixed':
      self._report.body.style.css.padding_top = 0
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_h)


class HtmlFooter(Html.Html):
  name = 'footer'

  def __init__(self, report, components, width, height, options, profile):
    super(HtmlFooter, self).__init__(report, [], css_attrs={"width": width, "height": height},
                                     options=options, profile=profile)
    self.__col_lst = None
    if components is not None:
      if not isinstance(components, list):
        components = [components]
      for c in components:
        self.__add__(c)

    # Set the colors
    self.style.css.background_color = report.theme.greys[0]
    self.style.css.border_top = "1px solid %s" % report.theme.greys[4]
    self.style.css.color = report.theme.greys[6]

  @property
  def sections(self):
    """
    Description:
    -----------

    """
    if not self.__col_lst:
      self.__col_lst = []
    return self.__col_lst

  @sections.setter
  def sections(self, col_lst):
    """
    Description:
    -----------

    :param col_lst:
    """
    self.__col_lst = col_lst

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: GrpClsMenu.ClassFooter
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassFooter(self)
    return self._styleObj

  def __add__(self, component):
    """ Add items to the footer """
    if not hasattr(component, 'options'):
      component = self._report.ui.div(component)
    # Has to be defined here otherwise it is set to late
    component.options.managed = False
    self.val.append(component)
    return self

  def __getitem__(self, i):
    """
    Description:
    -----------
    Return the internal column in the row for the given index.

    Attributes:
    ----------
    :param i: Integer. the column index
    """
    return self.val[i]

  def add_menu(self, context_menu):
    pass

  def __str__(self):
    str_h = "".join([val.html() for val in self.val])
    return "<footer %s>%s</footer>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_h)


class ContextMenu(Html.Html):

  name = 'Context Menu'
  source = None
  _option_cls = OptList.OptionsLi

  def __init__(self, report, components, width, height, visible, options, profile):
    super(ContextMenu, self).__init__(report, [], css_attrs={"width": width, "height": height},
                                      profile=profile, options=options)
    self.css({'display': 'block' if visible else 'none', 'position': 'absolute', 'z-index': 200,
              'padding': 0, 'margin': 0, 'background-color': self._report.theme.greys[0],
              'border': '1px solid %s' % self._report.theme.success[0], 'border-radius': '2px'})
    self.style.configs.shadow()
    for component in components:
      self.__add__(component)

  @property
  def options(self):
    """
    Description:
    -----------
    Component options.

    :rtype: OptList.OptionsLi
    """
    return super().options

  _js__builder__ = '''
      var contextMenu = htmlObj.querySelector('ul'); contextMenu.innerHTML = '';
      data.forEach(function(rec){
        var li = document.createElement("li"); var item = document.createElement("DIV");  
        item.innerHTML = rec; li.appendChild(item)})
      contextMenu.appendChild(li)
      '''

  def add_item(self, value, icon=None):
    """
    Description:
    ------------
    Add Item to the context menu.

    Attributes:
    ----------
    :param value: String.
    :param icon: String. Optional. The Font awesome icon.
    """
    self += {"value": value, 'icon': icon}
    return self

  def add(self, component):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component: HTML. Internal component to the framework.
    """
    self.__add__(component)
    return self.val[-1].val

  def __add__(self, component):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param component: HTML. The new HTML component to be added to the main component.
    """
    if not hasattr(component, 'options'):
      if isinstance(component, dict):
        if component.get('icon') is not None:
          i = self._report.ui.icon(component['icon'])
          i.css({'display': 'inline', 'margin-right': '5px'})
          v = self._report.ui.text(component['value'])
          v.css({'display': 'inline'})
          component = self._report.ui.div([i, v])
        else:
          component = self._report.ui.div(component['value'])
      else:
        component = self._report.ui.div(component)
    li_obj = Li(self._report, component) if not isinstance(component, Li) else component
    li_obj.css({"padding": "5px", 'cursor': 'pointer'})
    li_obj.options.managed = False
    component.options.managed = False
    self.val.append(li_obj)
    return self

  def __getitem__(self, i):
    return self.val[i].val

  def __str__(self):
    # TODO: Add a condition in the init to display the context menu only for some columns or rows when table for example
    if getattr(self, 'source') is None:
      raise Exception("Context Menu should be added to a component with the function contextMenu")

    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    # hide when mouse leave the component
    self.mouse(out_funcs=[self.dom.hide()])
    return '''
      <nav %(attr)s name='context_menus'>
        <ul style='list-style:none;padding:0px;margin:0'>%(val)s</ul>
      </nav>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': str_vals}


class PanelsBar(Html.Html):
  name = 'Panel Bar'

  def __init__(self, report, width, height, options, helper, profile):
    super(PanelsBar, self).__init__(report, None, profile=profile, css_attrs={"width": width, "height": height})
    self.add_helper(helper)
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
    Add a panel to the panel bar.

    Attributes:
    ----------
    :param text: String. Required. The anchor visible linked to a panel.
    :param content: HTML. Required. The panel.
    """
    content.style.css.padding = "0 5px"
    if not hasattr(text, 'options'):
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
        self._report.js.querySelectorAll(Selector.Selector(self.panels).with_child_element("div").excluding(panel)).css(
          {"display": 'none'}),
        #
        expr.if_(self._report.js.querySelector(
          Selector.Selector(self.panels)).getAttribute("data-panel") == menu_item.htmlCode, [
          self._report.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel", ""),
          self._report.js.querySelector(Selector.Selector(self.panels)).css({"display": 'none'})
        ]).else_([
          self._report.js.querySelector(Selector.Selector(self.panels)).setAttribute("data-panel", menu_item.htmlCode),
          self._report.js.querySelector(Selector.Selector(self.panels)).css(css_menu),
          self._report.js.querySelector(Selector.Selector(panel)).css({'display': 'block'})
        ])
      ])

    return "<div %s>%s%s</div>%s" % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.menus.html(), self.panels.html(), self.helper)


class Shortcut(Html.Html):
  name = 'shortcut'

  def __init__(self, report, components, logo, width, height, html_code, options, profile):
    super(Shortcut, self).__init__(report, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                   profile=profile)
    self.logo = logo
    if hasattr(self.logo, 'options'):
      self.logo.options.managed = False
    self.__options = options
    for component in components:
      self.__add__(component)
    self.css({"background": report.theme.colors[1], "position": 'fixed', 'overflow': 'hidden', 'z-index': 20})
    self.style.css.padding = 0
    if options['position'] in ['left', 'right']:
      self.css({'text-align': 'center'})
    elif options['position'] == 'top':
      self.css({'top': '0'})
    elif options['position'] == 'bottom':
      self.css({'bottom': '0'})

  @property
  def style(self):
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    :rtype: GrpClsMenu.ClassShortcut
    """
    if self._styleObj is None:
      self._styleObj = GrpClsMenu.ClassShortcut(self)
    return self._styleObj

  def __add__(self, component):
    """ Add items to a container """
    if not hasattr(component, 'options'):
      component = self._report.ui.icons.awesome(component)
      component.icon.style.css.font_size = 20
      component.style.css.margin_bottom = 5
      component.style.css.margin_top = 5
    component.options.managed = False

    if self.__options['position'] in ['left', 'right']:
      component.style.css.text_align = component.style.css.text_align or 'center'
      component.style.css.display = 'block'
      component.style.css.margin_bottom = 5

    if self.__options['position'] == 'top':
      component.style.css.line_height = self.css("height")
      component.style.css.height = self.css("height")
      component.style.css.vertical_align = 'top'
      if component.style.css.position is None:
        component.style.css.position = 'relative'
      component.style.css.top = -3
      component.style.css.display = 'inline-block'

    component.style.css.margin = 'auto'
    self.val.append(component)
    return self

  def add_logo(self, icon, path=None, align="center", width=(32, 'px'), height=(32, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param path: String. Optional.
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    """
    self.logo = self._report.ui.img(icon, path=path, align=align, width=width, height=height)
    self.logo.options.managed = False
    return self

  def __str__(self):
    if self.logo is None:
      self.logo = self._report.ui.icons.epyk()
    else:
      self.logo.style.css.margin_top = 5
      self.logo.style.css.display = 'block'
      self.logo.style.css.margin = 'auto'
      if self.__options['position'] in ['left', 'right']:
        self.logo.style.css.margin_bottom = 15
        self.logo.style.css.margin_right = 0
      else:
        self.logo.style.css.margin_right = 10
    self.logo.options.managed = False
    self.logo.style.css.margin_bottom = 40
    self.page.body.style.css.padding_left = "%spx" % (int(self.css("width")[:-2]) + 5)
    str_div = "".join([self.logo.html()] + [v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), str_div)
