"""
CSS Style module for the HR components
"""

from epyk.core.css.styles.classes import CssStyle


class CssHr(CssStyle.Style):
  _attrs = {'display': 'block', 'border-style': 'inset', 'border-width': '1px', 'margin': '5px'}
  classname = False
  _selector = 'hr'
