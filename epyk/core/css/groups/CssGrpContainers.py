"""
Group CSS class for all the containers components
"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesDiv


class CssGrpClassModal(CssGrpCls.CssGrpClass):
  """
  Set attributes to defaults but will change in the future
  """

  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_div_hidden = CssStylesDiv.CssDivHidden
  __map, __alt_map = ['CssDivNoBorder', 'CssDivHidden'], []
