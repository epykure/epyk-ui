"""

"""

from epyk.core.css.effects import Effects


class EffectsSpin(Effects.Effects):
  attrs = {
      "from": {"transform": "rotate(0deg)"},
      "to": {"transform": "rotate(360deg)"}
  }


class EffectsTranslate(Effects.Effects):
  attrs = {
    "0%": {
      "-webkit-transform": "translateY(-100 %)",
      "opacity": 1},
    "100%": {
      "-webkit-transform": "translateY(0)",
      "opacity": 0}
  }
