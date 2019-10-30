"""
Group CSS class for all the Image components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesImg
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesIcon


class CssClassImage(CssGrpCls.CssGrpClass):
  CssImgBasic = CssStylesImg.CssImgBasic
  __map, __alt_map = ['CssImgBasic'], []


class CssClassIcon(CssGrpCls.CssGrpClass):
  CssIcon = CssStylesIcon.CssIcon
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  __map, __alt_map = ['CssDivNoBorder'], ['CssIcon']


class CssClassImageAnimated(CssGrpCls.CssGrpClass):
  CssImg = CssStylesImg.CssImg
  CssImgAInfo = CssStylesImg.CssImgAInfo
  CssImgMask = CssStylesImg.CssImgMask
  CssImgH2 = CssStylesImg.CssImgH2
  CssImgParagraph = CssStylesImg.CssImgParagraph
  CssContent = CssStylesImg.CssContent
  CssView = CssStylesImg.CssView
  __map, __alt_map = ['CssImg', 'CssImgAInfo', 'CssImgMask', 'CssImgH2', 'CssImgParagraph', 'CssContent', 'CssView'], []


class CssClassImageCarrousel(CssGrpCls.CssGrpClass):
  CssImg = CssStylesImg.CssImgBasic
  CssCarrouselLi = CssStylesImg.CssCarrouselLi
  CssCarrouselH2 = CssStylesImg.CssCarrouselH2
  CssDivLabelPoint = CssStylesDiv.CssDivLabelPoint
  CssDivBoxCenter = CssStylesDiv.CssDivBoxCenter
  __map, __alt_map = ['CssImgBasic', 'CssCarrouselLi', 'CssCarrouselH2'], ['CssDivLabelPoint', 'CssDivBoxCenter']
