"""

"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesButton
from epyk.core.css.styles import CssStylesLabel
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesText


class CssClassButton(CssGrpCls.CssGrpClass):
  CssButtonBasic = CssStylesButton.CssButtonBasic
  __map, __alt_map = ["CssButtonBasic"], []


class CssClassButtonCheckBox(CssGrpCls.CssGrpClass):
  CssButtonBasic = CssStylesLabel.CssLabelContainer
  CssLabelContainerDisabled = CssStylesLabel.CssLabelContainerDisabled
  CssLabelCheckMarkHover = CssStylesLabel.CssLabelCheckMarkHover
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssCheckMark = CssStylesText.CssCheckMark
  __map, __alt_map = ['CssButtonBasic', 'CssLabelCheckMarkHover', 'CssDivNoBorder', 'CssCheckMark',
                      'CssLabelContainerDisabled'], []
