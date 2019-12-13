"""
Group CSS class for all the List and Selection components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesHref
from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStyleDropdown
from epyk.core.css.styles import CssStylesList
from epyk.core.css.styles import CssStylesSelect
from epyk.core.css.styles import CssStylesRadio


class CssClassListTree(CssGrpCls.CssGrpClass):
  """

  """
  css_basic_list_items_selected = CssStylesList.CssBasicListItemsSelected
  __map, __alt_map = ['CssBasicListItemsSelected'], []


class CssClassListDropDown(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_dropdown_sub_menu = CssStyleDropdown.CssDropDownSubMenu
  css_dropdown_after_menu = CssStyleDropdown.CssDropDownAfterMenu
  css_dropdown_menu_a_after = CssStyleDropdown.CssDropDownMenuAAfter
  css_dropdown_menu_hover_a_after = CssStyleDropdown.CssDropDownMenuHoverAAfter
  css_dropdown_sub_menu_pull_left = CssStyleDropdown.CssDropDownSubMenuPullLeft
  css_dropdown_sub_menu_right = CssStyleDropdown.CssDropDownSubMenuRight
  css_dropdown_sub_menu_pull_left_menu = CssStyleDropdown.CssDropDownSubMenuPullLeftMenu
  __map, __alt_map = ['CssDivNoBorder', 'CssDropDownSubMenu', 'CssDropDownAfterMenu', 'CssDropDownMenuAAfter',
                      'CssDropDownMenuHoverAAfter', 'CssDropDownSubMenuPullLeft', 'CssDropDownSubMenuPullLeftMenu',
                      'CssDropDownSubMenuRight'], []


class CssClassList(CssGrpCls.CssGrpClass):
  """

  """
  css_title_4 = CssStylesText.CssTitle4
  css_basic_list = CssStylesList.CssBasicList
  css_basic_list_items = CssStylesList.CssBasicListItems
  css_basic_list_items_disabled = CssStylesList.CssBasicListItemsDisabled
  __map, __alt_map = ['CssBasicList', 'CssBasicListItems', 'CssBasicListItemsDisabled'], ['CssTitle4']


class CssClassListSelect(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_select_button = CssStylesSelect.CssSelectButton
  css_select_filter_option = CssStylesSelect.CssSelectFilterOption
  css_select_option = CssStylesSelect.CssSelectOption
  css_select_option_hover = CssStylesSelect.CssSelectOptionHover
  css_select_option_active = CssStylesSelect.CssSelectOptionActive
  css_select_style = CssStylesSelect.CssSelectStyle
  __map, __alt_map = ['CssDivNoBorder', 'CssSelectButton', 'CssSelectFilterOption', 'CssSelectOption',
                      'CssSelectOptionHover', 'CssSelectOptionActive', 'CssSelectStyle'], []


class CssClassListSelectMin(CssGrpCls.CssGrpClass):
  """

  """
  css_select_style = CssStylesSelect.CssSelectStyle
  __map, __alt_map = ['CssSelectStyle'], []


class CssClassSwitch(CssGrpCls.CssGrpClass):
  """

  """
  css_radio_switch = CssStylesRadio.CssRadioSwitch
  css_radio_switch_label = CssStylesRadio.CssRadioSwitchLabel
  css_radio_switch_checked = CssStylesRadio.CssRadioSwitchChecked
  __map, __alt_map = ['CssRadioSwitch', 'CssRadioSwitchLabel', 'CssRadioSwitchChecked'], []


class CssClassListAccordeon(CssGrpCls.CssGrpClass):
  """

  """
  css_div_box_margin = CssStylesDiv.CsssDivBoxMargin
  css_href_menu = CssStylesHref.CssHreftMenu
  css_href_sub_menu = CssStylesHref.CssHrefSubMenu
  css_list_no_decoration = CssStylesList.CssListNoDecoration
  css_list_li_sub_item = CssStylesList.CssListLiSubItem
  css_list_li_Ul_container = CssStylesList.CssListLiUlContainer
  __map, __alt_map = ['CsssDivBoxMargin'], ['CssHreftMenu', 'CssHrefSubMenu', 'CssListNoDecoration',
                                            'CssListLiSubItem', 'CssListLiUlContainer']


class CssClassListSquare(CssGrpCls.CssGrpClass):
  """

  """
  css_square_list = CssStylesList.CssSquareList
  __map, __alt_map = [], []


class CssClassListFilters(CssGrpCls.CssGrpClass):
  """

  """
  css_div_filter = CssStylesDiv.CssDivFilter
  __map, __alt_map = ['CssDivFilter'], []
