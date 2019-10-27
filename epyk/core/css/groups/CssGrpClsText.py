"""

"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesHref
from epyk.core.css.styles import CssStylesChart
from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStylesButton


class CssClassHref(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssHrefNoDecoration = CssStylesHref.CssHrefNoDecoration
  __map, __alt_map = ['CssDivNoBorder', 'CssHrefNoDecoration'], []


class CssClassTextBubble(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  CssDivBubble = CssStylesDiv.CssDivBubble
  __map, __alt_map = ['CssDivChart'], ['CssDivBubble']


class CssClassTextBlock(CssGrpCls.CssGrpClass):
  CssTitle = CssStylesText.CssTitle
  CssText = CssStylesText.CssText
  CsssDivBoxMargin = CssStylesDiv.CsssDivBoxMargin
  CssHrefNoDecoration = CssStylesHref.CssHrefNoDecoration
  CssButtonBasic = CssStylesButton.CssButtonBasic
  __map, __alt_map = ['CsssDivBoxMargin'], ['CssTitle', 'CssHrefNoDecoration', 'CssButtonBasic', 'CssText']
