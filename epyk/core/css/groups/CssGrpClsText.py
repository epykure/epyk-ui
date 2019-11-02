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
  """

  """
  css_text = CssStylesText.CssText
  __map, __alt_map = ['CssText'], []


class CssClassTextItem(CssGrpCls.CssGrpClass):
  """

  """
  css_text_item = CssStylesText.CssTextItem
  __map, __alt_map = ['CssTextItem'], []


class CssClassTextNoBorder(CssGrpCls.CssGrpClass):
  """

  """
  css_text = CssStylesText.CssText
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder', 'CssText'], []


class CssClassHref(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_href_no_decoration = CssStylesHref.CssHrefNoDecoration
  __map, __alt_map = ['CssDivNoBorder', 'CssHrefNoDecoration'], []


class CssClassTextBubble(CssGrpCls.CssGrpClass):
  """

  """
  css_div_chart = CssStylesChart.CssDivChart
  css_div_bubble = CssStylesDiv.CssDivBubble
  __map, __alt_map = ['CssDivChart'], ['CssDivBubble']


class CssClassTextVignet(CssGrpCls.CssGrpClass):
  """

  """
  css_div_chart = CssStylesChart.CssDivChart
  css_text = CssStylesText.CssText
  css_number_center = CssStylesText.CssNumberCenter
  __map, __alt_map = ['CssDivChart'], ['CssText', 'CssNumberCenter']


class CssClassTitle(CssGrpCls.CssGrpClass):
  """

  """
  css_href_no_decoration = CssStylesHref.CssHrefNoDecoration
  __map, __alt_map = ['CssHrefNoDecoration'], []


class CssClassTextBlock(CssGrpCls.CssGrpClass):
  """

  """
  css_title = CssStylesText.CssTitle
  css_text = CssStylesText.CssText
  csss_div_box_margin = CssStylesDiv.CsssDivBoxMargin
  css_href_no_decoration = CssStylesHref.CssHrefNoDecoration
  css_button_basic = CssStylesButton.CssButtonBasic
  __map, __alt_map = ['CsssDivBoxMargin'], ['CssTitle', 'CssHrefNoDecoration', 'CssButtonBasic', 'CssText']


class CssClassComment(CssGrpCls.CssGrpClass):
  """

  """
  css_comm_header = CssStylesDivComms.CssCommHeader
  css_comm_input = CssStylesDivComms.CssCommInput
  __map, __alt_map = ['CssCommHeader', 'CssCommInput'], []


class CssClassEditor(CssGrpCls.CssGrpClass):
  """

  """
  css_div_editor = CssStylesDiv.CssDivEditor
  __map, __alt_map = ['CssDivEditor'], []
