"""
Group CSS class for all the buttons components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesButton
from epyk.core.css.styles import CssStylesLabel
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesText


class CssClassButton(CssGrpCls.CssGrpClass):
  """

  """
  css_button_basic = CssStylesButton.CssButtonBasic
  __map, __alt_map = ["CssButtonBasic"], []


class CssClassButtonCheckBox(CssGrpCls.CssGrpClass):
  """

  """
  css_button_basic = CssStylesLabel.CssLabelContainer
  css_label_container_disabled = CssStylesLabel.CssLabelContainerDisabled
  css_label_check_mark_hover = CssStylesLabel.CssLabelCheckMarkHover
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_check_mark = CssStylesText.CssCheckMark
  __map, __alt_map = ['CssButtonBasic', 'CssLabelCheckMarkHover', 'CssDivNoBorder', 'CssCheckMark',
                      'CssLabelContainerDisabled'], []
