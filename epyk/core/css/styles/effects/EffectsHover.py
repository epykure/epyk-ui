"""

"""

from epyk.core.css.styles.effects import Effects


class EffectsHoverEcho(Effects.Effects):
  attrs = {
      "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
      "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
      "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
    }

