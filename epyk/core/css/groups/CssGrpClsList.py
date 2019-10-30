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
  CssBasicListItemsSelected = CssStylesList.CssBasicListItemsSelected
  __map, __alt_map = ['CssBasicListItemsSelected'], []


class CssClassListDropDown(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssDropDownSubMenu = CssStyleDropdown.CssDropDownSubMenu
  CssDropDownAfterMenu = CssStyleDropdown.CssDropDownAfterMenu
  CssDropDownMenuAAfter = CssStyleDropdown.CssDropDownMenuAAfter
  CssDropDownMenuHoverAAfter = CssStyleDropdown.CssDropDownMenuHoverAAfter
  CssDropDownSubMenuPullLeft = CssStyleDropdown.CssDropDownSubMenuPullLeft
  CssDropDownSubMenuPullLeftMenu = CssStyleDropdown.CssDropDownSubMenuPullLeftMenu
  __map, __alt_map = ['CssDivNoBorder', 'CssDropDownSubMenu', 'CssDropDownAfterMenu', 'CssDropDownMenuAAfter',
                      'CssDropDownMenuHoverAAfter', 'CssDropDownSubMenuPullLeft', 'CssDropDownSubMenuPullLeftMenu'], []


class CssClassList(CssGrpCls.CssGrpClass):
  CssTitle4 = CssStylesText.CssTitle4
  CssBasicList = CssStylesList.CssBasicList
  CssBasicListItems = CssStylesList.CssBasicListItems
  CssBasicListItemsDisabled = CssStylesList.CssBasicListItemsDisabled
  __map, __alt_map = ['CssBasicList', 'CssBasicListItems', 'CssBasicListItemsDisabled'], ['CssTitle4']


class CssClassListSelect(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssSelectButton = CssStylesSelect.CssSelectButton
  CssSelectFilterOption = CssStylesSelect.CssSelectFilterOption
  CssSelectOption = CssStylesSelect.CssSelectOption
  CssSelectOptionHover = CssStylesSelect.CssSelectOptionHover
  CssSelectOptionActive = CssStylesSelect.CssSelectOptionActive
  CssSelectStyle = CssStylesSelect.CssSelectStyle
  __map, __alt_map = ['CssDivNoBorder', 'CssSelectButton', 'CssSelectFilterOption', 'CssSelectOption',
                      'CssSelectOptionHover', 'CssSelectOptionActive', 'CssSelectStyle'], []


class CssClassSwitch(CssGrpCls.CssGrpClass):
  CssRadioSwitch = CssStylesRadio.CssRadioSwitch
  CssRadioSwitchLabel = CssStylesRadio.CssRadioSwitchLabel
  CssRadioSwitchChecked = CssStylesRadio.CssRadioSwitchChecked
  __map, __alt_map = ['CssRadioSwitch', 'CssRadioSwitchLabel', 'CssRadioSwitchChecked'], []


class CssClassListAccordeon(CssGrpCls.CssGrpClass):
  CsssDivBoxMargin = CssStylesDiv.CsssDivBoxMargin
  CssHreftMenu = CssStylesHref.CssHreftMenu
  CssHrefSubMenu = CssStylesHref.CssHrefSubMenu
  CssListNoDecoration = CssStylesList.CssListNoDecoration
  CssListLiSubItem = CssStylesList.CssListLiSubItem
  CssListLiUlContainer = CssStylesList.CssListLiUlContainer
  __map, __alt_map = ['CsssDivBoxMargin'], ['CssHreftMenu', 'CssHrefSubMenu', 'CssListNoDecoration',
                                            'CssListLiSubItem', 'CssListLiUlContainer']


class CssClassListSquare(CssGrpCls.CssGrpClass):
  CssSquareList = CssStylesList.CssSquareList
  __map, __alt_map = [], []


class CssClassListFilters(CssGrpCls.CssGrpClass):
  CssDivFilter = CssStylesDiv.CssDivFilter
  __map, __alt_map = ['CssDivFilter'], []
