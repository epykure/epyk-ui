
from epyk.core.css.styles.classes import CssStyle


class CssDropDownSubMenu(CssStyle.Style):
  _attrs = {'display': 'none'}
  classname = "menu .submenu"


class CssDropDownMenuHLi(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu li.dropdown:hover > .submenu"


class CssDropDownMenuHoverAAfter(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu ul.submenu > li.dropdown:hover > .submenu"


class CssDropDownSubMenuPullLeft(CssStyle.Style):
  _attrs = {'position': 'absolute', 'top': '0px', 'list-style-type': 'none', 'white-space': 'nowrap', 'margin': 0, 'padding': 0} # 'left': '0px',
  classname = "menu .submenu .submenu"


class CssDropDownMenu(CssStyle.Style):
  _attrs = {'position': 'absolute', 'top': '0px', 'list-style-type': 'none', 'white-space': 'nowrap', 'margin': 0, 'padding': 0} # 'left': '0px',
  classname = "menu ul.submenu"


class CssDropDownAfterMenu(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu li a"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], 'background': self.rptObj.theme.greys[0]})
