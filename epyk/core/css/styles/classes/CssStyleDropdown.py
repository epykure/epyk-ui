from epyk.core.css.styles.classes import CssStyle


class CssDropDownSubMenu(CssStyle.Style):
  _attrs = {'display': 'none', 'border': '1px solid rgba(0,0,0,.15)', 'border-radius': '4px',
            'box-shadow': '0 6px 12px rgba(0,0,0,.175)', '-webkit-box-shadow': '0 6px 12px rgba(0,0,0,.175)'}
  classname = "menu .submenu"


class CssDropDownMenuHLi(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu li.dropdown:hover > .submenu"


class CssDropDownMenuHoverAAfter(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu ul.submenu > li.dropdown:hover > .submenu"


class CssDropDownSubMenuPullLeft(CssStyle.Style):
  _attrs = {'position': 'absolute', 'top': '0px', 'list-style-type': 'none', 'white-space': 'nowrap', 'margin': 0,
            'padding': 0}  # 'left': '0px',
  classname = "menu .submenu .submenu"


class CssDropDownMenu(CssStyle.Style):
  _attrs = {'position': 'absolute', 'top': '0px', 'list-style-type': 'none', 'white-space': 'nowrap', 'margin': 0,
            'padding': 0}  # 'left': '0px',
  classname = "menu ul.submenu"


class CssDropDownAfterMenu(CssStyle.Style):
  _attrs = {'display': 'block'}
  classname = "menu li a"

  def customize(self):
    self.css({'color': self.page.theme.greys[-1], 'background': self.page.theme.greys[0]})


class CssDropDownCaret(CssStyle.Style):
  _attrs = {'display': 'inline-block', "width": 0, "height": 0, 'margin-left': '2px', 'vertical-align': 'middle',
            'border-top': '4px dashed', 'border-right': '4px solid transparent', 'border-left': '4px solid transparent'}
  classname = "caret"
