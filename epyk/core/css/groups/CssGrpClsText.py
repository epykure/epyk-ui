"""
Group CSS class for all the Text components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesDivComms
from epyk.core.css.styles import CssStylesHref
from epyk.core.css.styles import CssStylesChart
from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStylesButton


class CssClassText(CssGrpCls.CssGrpClass):
  CssText = CssStylesText.CssText
  __map, __alt_map = ['CssText'], []


class CssClassTextNoBorder(CssGrpCls.CssGrpClass):
  CssText = CssStylesText.CssText
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder', 'CssText'], []


class CssClassHref(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssHrefNoDecoration = CssStylesHref.CssHrefNoDecoration
  __map, __alt_map = ['CssDivNoBorder', 'CssHrefNoDecoration'], []


class CssClassTextBubble(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  CssDivBubble = CssStylesDiv.CssDivBubble
  __map, __alt_map = ['CssDivChart'], ['CssDivBubble']


class CssClassTextVignet(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  CssText = CssStylesText.CssText
  CssNumberCenter = CssStylesText.CssNumberCenter
  __map, __alt_map = ['CssDivChart'], ['CssText', 'CssNumberCenter']


class CssClassTextBlock(CssGrpCls.CssGrpClass):
  CssTitle = CssStylesText.CssTitle
  CssText = CssStylesText.CssText
  CsssDivBoxMargin = CssStylesDiv.CsssDivBoxMargin
  CssHrefNoDecoration = CssStylesHref.CssHrefNoDecoration
  CssButtonBasic = CssStylesButton.CssButtonBasic
  __map, __alt_map = ['CsssDivBoxMargin'], ['CssTitle', 'CssHrefNoDecoration', 'CssButtonBasic', 'CssText']


class CssClassComment(CssGrpCls.CssGrpClass):
  CssCommHeader = CssStylesDivComms.CssCommHeader
  CssCommInput = CssStylesDivComms.CssCommInput
  __map, __alt_map = ['CssCommHeader', 'CssCommInput'], []


class CssClassEditor(CssGrpCls.CssGrpClass):
  CssDivEditor = CssStylesDiv.CssDivEditor
  __map, __alt_map = ['CssDivEditor'], []
