"""
CS Style module for all the DropDown components
"""


from epyk.core.css.styles import CssStyle


class CssDropDownSubMenu(CssStyle.Style):
  _attrs = {'position': 'relative'}
  classname = "dropdown-submenu"


class CssDropDownMenu(CssStyle.Style):
  _attrs = {'top': 0, 'left': '100%', 'margin-top': '-6px',
            'margin-left': '-1px', '-webkit-border-radius': '0 6px 6px 6px',
            '-moz-border-radius': '0 6px 6px', 'border-radius': '0 6px 6px'}

  @property
  def classname(self):
    return 'dropdown-submenu>.dropdown-menu'


class CssDropDownAfterMenu(CssStyle.Style):
  _attrs = {'display': 'inherit'}

  @property
  def classname(self):
    return 'dropdown-submenu:hover>.dropdown-menu'


class CssDropDownMenuAAfter(CssStyle.Style):
  _attrs = {'display': 'block', 'content':  '" "', 'float': 'right', 'width': 0, 'height': 0, 'border-color': 'transparent',
            'border-style': 'solid', 'border-width': '5px 0 5px 5px', 'border-left-color': '#ccc', 'margin-top': '5px',
            'margin-right': '-10px'}

  @property
  def classname(self):
    return 'dropdown-submenu>a:after'


class CssDropDownMenuHoverAAfter(CssStyle.Style):
  _attrs = {'border-left-color': '#fff'}

  @property
  def classname(self):
    return "dropdown-submenu:hover>a:after"


class CssDropDownSubMenuPullLeft(CssStyle.Style):
  _attrs = {'float': 'none'}

  @property
  def classname(self):
    return "dropdown-submenu.pull-left"


class CssDropDownSubMenuRight(CssStyle.Style):
  _attrs = {'margin-left': 0, 'right': 'inherit !important', 'left': 'auto'}

  @property
  def classname(self):
    return "dropdown-menu-right"


class CssDropDownSubMenuPullLeftMenu(CssStyle.Style):
  _attrs = {'left': '-100%', 'margin-left': '10px', '-webkit-border-radius': '6px 0 6px 6px',
            '-moz-border-radius': '6px 0 6px 6px', 'border-radius': '6px 0 6px 6px'}

  @property
  def classname(self):
    return "dropdown-submenu.pull-left>.dropdown-menu"
