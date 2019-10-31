"""
Group CSS class for all the Image components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesImg
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesIcon


class CssClassImage(CssGrpCls.CssGrpClass):
  """

  """
  css_img_basic = CssStylesImg.CssImgBasic
  __map, __alt_map = ['CssImgBasic'], []


class CssClassIcon(CssGrpCls.CssGrpClass):
  """

  """
  css_icon = CssStylesIcon.CssIcon
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder'], ['CssIcon']


class CssClassImageAnimated(CssGrpCls.CssGrpClass):
  """

  """
  css_img = CssStylesImg.CssImg
  css_img_a_info = CssStylesImg.CssImgAInfo
  css_img_mask = CssStylesImg.CssImgMask
  css_img_H2 = CssStylesImg.CssImgH2
  css_img_paragraph = CssStylesImg.CssImgParagraph
  css_content = CssStylesImg.CssContent
  css_view = CssStylesImg.CssView
  __map, __alt_map = ['CssImg', 'CssImgAInfo', 'CssImgMask', 'CssImgH2', 'CssImgParagraph', 'CssContent', 'CssView'], []


class CssClassImageCarrousel(CssGrpCls.CssGrpClass):
  """

  """
  css_img = CssStylesImg.CssImgBasic
  css_carrousel_li = CssStylesImg.CssCarrouselLi
  css_carrousel_H2 = CssStylesImg.CssCarrouselH2
  css_div_label_point = CssStylesDiv.CssDivLabelPoint
  css_div_box_center = CssStylesDiv.CssDivBoxCenter
  __map, __alt_map = ['CssImgBasic', 'CssCarrouselLi', 'CssCarrouselH2'], ['CssDivLabelPoint', 'CssDivBoxCenter']
