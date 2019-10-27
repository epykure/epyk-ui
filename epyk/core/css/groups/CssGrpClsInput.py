"""

"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesDates


class CssClassDatePicker(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssDatePicker = CssStylesDates.CssDatePicker
  __map, __alt_map = ['CssDivNoBorder', 'CssDatePicker'], []
