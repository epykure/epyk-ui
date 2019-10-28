"""
Group CSS class for all the File components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDrop


class CssClassButton(CssGrpCls.CssGrpClass):
  CssButtonBasic = CssStylesDrop.CssDropFile
  __map, __alt_map = ["CssDropFile"], []
