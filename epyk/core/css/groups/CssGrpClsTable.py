"""
Group CSS class for all the Charts components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv


class CssClassTableContent(CssGrpCls.CssGrpClass):
  CssDivTableContent = CssStylesDiv.CssDivTableContent
  __map, __alt_map = ["CssDivTableContent"], []

