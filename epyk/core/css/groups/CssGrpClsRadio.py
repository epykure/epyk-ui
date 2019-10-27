"""

"""

from epyk.core.css.groups import CssGrpCls
from epyk.core.css.styles import CssStylesRadio


class CssClassSwitch(CssGrpCls.CssGrpClass):
  CssRadioSwitch = CssStylesRadio.CssRadioSwitch
  CssRadioSwitchLabel = CssStylesRadio.CssRadioSwitchLabel
  CssRadioSwitchChecked = CssStylesRadio.CssRadioSwitchChecked

  __map, __alt_map = ['CssRadioSwitch', 'CssRadioSwitchLabel', 'CssRadioSwitchChecked'], []
