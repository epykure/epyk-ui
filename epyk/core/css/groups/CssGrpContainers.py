"""
Group CSS class for all the containers components
"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesDiv


class CssGrpClassModal(object):
  """
  Set attributes to defaults but will change in the future
  """

  css_div_modal = CssStylesDiv.CssDivModal
  __map, __alt_map = ['CssDivModal'], []


class CssGrpClassModalContent(object):
  """
  """
  css_div_modal_content = CssStylesDiv.CssDivModalContent
  __map, __alt_map = ['CssDivModalContent'], []