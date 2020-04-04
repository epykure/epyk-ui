
from epyk.core.css.styles.classes import CssStyle


class CssDropDownSubMenu(CssStyle.Style):
  _attrs = {'position': 'relative', 'text-decoration': 'none'}
  classname = "dropdown-submenu"


class CssDropDownMenu(CssStyle.Style):
  _attrs = {'top': 0, 'left': '100%', 'margin-top': '-6px',
            'margin-left': '-1px', '-webkit-border-radius': '0 6px 6px 6px',
            '-moz-border-radius': '0 6px 6px', 'border-radius': '0 6px 6px'}
  classname = "dropdown-submenu>.dropdown-menu"


class CssDropDownAfterMenu(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "dropdown-submenu:hover > a"


class CssDropDownMenuAAfter(CssStyle.Style):
  _attrs = {'display': 'block', 'content':  '" "', 'float': 'right', 'width': 0, 'height': 0, 'border-color': 'transparent',
            'border-style': 'solid', 'border-width': '5px 0 5px 5px', 'border-left-color': '#ccc', 'margin-top': '5px',
            'margin-right': '-10px'}
  classname = 'dropdown-submenu>a:after'


class CssDropDownMenuHoverAAfter(CssStyle.Style):
  _attrs = {'border-left-color': '#fff'}
  classname = "dropdown-submenu:hover>a:after"


class CssDropDownSubMenuPullLeft(CssStyle.Style):
  _attrs = {'float': 'none'}
  classname = "dropdown-submenu.pull-left"


class CssDropDownSubMenuPullRight(CssStyle.Style):
  _attrs = {'margin-left': 0, 'right': 'inherit !important', 'left': 'auto'}
  classname = "dropdown-submenu.pull-right"


class CssDropDownSubMenuPullLeftMenu(CssStyle.Style):
  _attrs = {'left': '-100%', 'margin-left': '10px', '-webkit-border-radius': '6px 0 6px 6px',
            '-moz-border-radius': '6px 0 6px 6px', 'border-radius': '6px 0 6px 6px'}

  @property
  def classname(self):
    return "dropdown-submenu.pull-left>.dropdown-menu"
