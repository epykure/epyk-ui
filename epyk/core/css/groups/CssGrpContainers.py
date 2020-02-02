"""
Group CSS class for all the containers components
"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesDiv


class CssGrpClassModal(CssGrpCls.CssGrpClass):
  """
  Set attributes to defaults but will change in the future
  """

  css_div_modal = CssStylesDiv.CssDivModalTest #CssDivModal
  __map, __alt_map = ['CssDivModalTest'], []


class CssGrpClassModalContent(CssGrpCls.CssGrpClass):
  """
  """
  css_div_modal_content = CssStylesDiv.CssDivModalContent
  __map, __alt_map = ['CssDivModalContent'], []