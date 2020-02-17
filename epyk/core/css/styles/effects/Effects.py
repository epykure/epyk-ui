"""

"""


class Effects(object):
  """

  """

  def __init__(self, report, htmlObj, ovrs_attrs=None):
    self._report, self._htmlObj = report, htmlObj
    if ovrs_attrs is not None:
      self.attrs = dict(self.attrs)
      self.attrs.update(ovrs_attrs)

  def get_attrs(self):
    """ Return the effect CSS attributes """
    return self.attrs

  def glow(self, color, radius=50):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Documentation
    https://www.w3schools.com/howto/howto_css_glowing_text.asp

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

    Documentation

    :param duration:
    """
    keyframe_name = "blink_%s" % duration
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"opacity": 0}, "to": {"opacity": 1}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def shiny_text(self, color):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Documentation
    https://www.w3schools.com/howto/howto_css_glowing_text.asp

    :param color: String. The color to use fin the effect
    """
    keyframe_name = "shiny_text"
    self._htmlObj.style.css.animation = "%s 1s ease-in-out infinite alternate" % keyframe_name
    attrs = {"from": {"color": color}, "to": {"color": "none"}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def shiny_border(self, color, duration=1):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Documentation
    https://www.w3schools.com/howto/howto_css_glowing_text.asp

    :param color: String. The color to use fin the effect
    """
    keyframe_name = "shiny_border"
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": {"border": "1px solid %s" % color}, "to": {"border": "1px solid %s" % color}}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self

  def animate(self, name, css_attrs, duration=1):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Example
    htmlObj.style.effects.animate("pink", {"color": "blue", "width": "400px"})

    Documentation
    https://www.w3schools.com/cssref/css_animatable.asp

    :param color: String. The color to use fin the effect
    """
    keyframe_name = "animate_%s" % name
    self._htmlObj.style.css.animation = "%s %ss ease-in-out infinite alternate" % (keyframe_name, duration)
    attrs = {"from": css_attrs, "to": css_attrs}
    self._htmlObj.style.css_class.keyframes(keyframe_name, attrs)
    return self
