"""
CSS Style module for the HR components
"""


from epyk.core.css.styles import CssStyle


class CssHr(CssStyle.CssCls):
  attrs = {'display': 'block', 'border-style': 'inset', 'border-width': '1px', 'margin': '5px'}
  cssId = {'direct': 'hr'}
