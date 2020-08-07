
from epyk.core.js import JsUtils


class Effects(object):

  def __init__(self, report, htmlObj, ovrs_attrs=None):
    self._report, self._htmlObj = report, htmlObj
    if ovrs_attrs is not None:
      self.attrs = dict(self.attrs)
      self.attrs.update(ovrs_attrs)

  def get_attrs(self):
    """
    Description:
    ------------
    Return the effect CSS attributes
    """
    return self.attrs

  def glow(self, color, radius=50):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    :param radius: Integer. The lenght of the radius to display in the animate
    """
    keyframe_name = "glow_%s" % color
    self._htmlObj.style.css.animation = "%s 1s ease-in-out infinite alternate" % keyframe_name
    color_effects = []
    for i in range(1, int(radius / 10)+1):
      color_effects.append("0 0 %s0px %s" % (i, color))
    if not color_effects:
      color_effects.append("0 0 %spx %s" % (radius, color))
    attrs = {"from": {"text-shadow": color_effects}, "to": {"text-shadow": color_effects}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def blink(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    """
    keyframe_name = "blink_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"opacity": 0}, "to": {"opacity": 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def shiny_text(self, color):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    """
    keyframe_name = "shiny_text"
    self._htmlObj.style.css.animation = "%s 1s ease-in-out infinite alternate" % keyframe_name
    attrs = {"from": {"color": color}, "to": {"color": "none"}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def shiny_border(self, color, duration=1):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    :param duration:
    """
    keyframe_name = "shiny_border"
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"border": "1px solid %s" % color}, "to": {"border": "1px solid %s" % color}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def spin(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    """
    keyframe_name = "spin_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"transform": "rotate(0deg)"}, "to": {"transform": "rotate(360deg)"}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def translate(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:

    """
    keyframe_name = "trans_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"transform": "translateY(-100%)"}, "to": {"transform": "translateY(0)"}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def down(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:

    """
    keyframe_name = "trans_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out alternate" % (keyframe_name, duration)
    attrs = {"from": {"transform": "translateY(-100%)"}, "to": {"transform": "translateY(0)"}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def up(self, duration=1, bottom=(20, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param bottom:
    """
    keyframe_name = "up_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out alternate" % (keyframe_name, duration)
    attrs = {"0%": {"bottom": "-%s%s" % (bottom[0], bottom[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"bottom": 0, 'position': 'relative', 'opacity': 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def left(self, duration=1, left=(100, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param left:
    """
    keyframe_name = "left_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out" % (keyframe_name, duration)
    attrs = {"0%": {"left": "-%s%s" % (left[0], left[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"left": 0, 'position': 'relative', 'opacity': 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def right(self, duration=1, right=(100, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    :param right:
    """
    keyframe_name = "right_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out" % (keyframe_name, duration)
    attrs = {"0%": {"right": "-%s%s" % (right[0], right[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"right": 0, 'position': 'relative', 'opacity': 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def appear(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    """
    keyframe_name = "appear_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out" % (keyframe_name, duration)
    attrs = {"0%": {'opacity': 0}, "100%": {'opacity': 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def disappear(self, duration=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration:
    """
    keyframe_name = "disappear_%s" % duration
    self._htmlObj.style.css.opacity = 0
    self._htmlObj.style.css.animation = "%s %ss ease-in-out" % (keyframe_name, duration)
    attrs = {"0%": {'opacity': 1}, "100%": {'opacity': 0}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def animate(self, name, targ_css_attrs, orig_css_attrs=None, delay=0, duration=1, timing_function="ease-in-out",
              iteration_count="infinite", directions="alternate"):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Attributes:
    ----------
    htmlObj.style.effects.animate("pink", {"color": "blue", "width": "400px"})

    Related Pages:

      https://www.w3schools.com/cssref/css_animatable.asp

    :param name: String. The animation name
    :param targ_css_attrs: Dictionary. The different CSS attributes to animate
    :param orig_css_attrs: Dictionary. The initial state of the attributes to animate
    :param delay: Integer. The delay in second before starting the animation
    :param timing_function: String. The animation-timing-function property specifies the speed curve of the animation.
    :param duration: Integer. The animation duration in second
    :param iteration_count: Integer. The animation count
    :param directions: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = JsUtils.getJsValid(name, fail=False)
    keyframe_name = "animate_%s" % name
    self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s" % (keyframe_name, duration, timing_function, delay, iteration_count, directions)
    if orig_css_attrs is None:
      attrs = {"to": targ_css_attrs}
    else:
      attrs = {"from": orig_css_attrs, "to": targ_css_attrs}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self
