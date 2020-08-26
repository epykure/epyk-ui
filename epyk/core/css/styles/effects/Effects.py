
from epyk.core.js import JsUtils


class Effects(object):

  def __init__(self, report, htmlObj=None, ovrs_attrs=None):
    """

    :param report:
    :param htmlObj:
    :param ovrs_attrs:
    """
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

  def glow(self, color, radius=50, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    :param radius: Integer. The length of the radius to display in the animate
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The classname of the animation keyframes
    """
    name = "glow_%s_%s" % (color, radius)
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    color_effects = ["0 0 %s0px %s" % (i, color) for i in range(1, int(radius / 10)+1)]
    if not color_effects:
      color_effects.append("0 0 %spx %s" % (radius, color))
    self._report.body.style.css_class.keyframes(name, {"from": {"text-shadow": color_effects}, "to": {"text-shadow": color_effects}})
    return name

  def blink(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The classname of the animation keyframes
    """
    name = "blink"
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    self._report.body.style.css_class.keyframes(name, {"from": {"opacity": 0}, "to": {"opacity": 1}})
    return name

  def shiny_text(self, color, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The classname of the animation keyframes
    """
    name = "shiny_text_%s" % color
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    self._report.body.style.css_class.keyframes(name, {"from": {"color": color}, "to": {"color": "none"}})
    return name

  def shiny_border(self, color, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param color: String. The color to use fin the effect
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The classname of the animation keyframes
    """
    name = "shiny_border_%s" % color
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"border": "1px solid %s" % color}, "to": {"border": "1px solid %s" % color}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def spin(self, degree=360, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param degree: Integer.
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The classname of the animation keyframes
    """
    name = "spin_%s"
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "rotate(0deg)"}, "to": {"transform": "rotate(%sdeg)" % degree}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def translate(self, start=-100, end=0, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "translation_%s_%s" % (start, end)
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "translateY(%s%%)" % start}, "to": {"transform": "translateY(%s)" % end}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def down(self, start=-100, end=0, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.

    :return: The string CSS classname for the animation
    """
    name = "down_%s_%s" % (start, end)
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "translateY(-100%)"}, "to": {"transform": "translateY(0)"}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def up(self, bottom=(20, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
    :param bottom:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "up_%s_%s" % (bottom[0], bottom[1])
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"bottom": "-%s%s" % (bottom[0], bottom[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"bottom": 0, 'position': 'relative', 'opacity': 1}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def left(self, left=(100, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param left:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "left_%s_%s" % (left[0], left[1])
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"left": "-%s%s" % (left[0], left[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"left": 0, 'position': 'relative', 'opacity': 1}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def right(self, right=(100, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param right:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "right_%s_%s" % (right[0], right[1])
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"right": "-%s%s" % (right[0], right[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"right": 0, 'position': 'relative', 'opacity': 1}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def appear(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "appear"
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction)
    self._report.body.style.css_class.keyframes(name, {"0%": {'opacity': 0}, "100%": {'opacity': 1}})
    return name

  def fade_out(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "fade_out"
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
      self._htmlObj.style.css.animation_fill_mode = "forwards"
    self._report.body.style.css_class.keyframes(name, {"0%": {'opacity': 1}, "100%": {'opacity': 0}})
    return name

  def fade_in(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "fade_in"
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
      self._htmlObj.style.css.animation_fill_mode = "forwards"
    attrs = {"0%": {'opacity': 0}, "100%": {'opacity': 1}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def reduce(self):
    """
    Description:
    ------------
    Reduce the component size when the mouse is hover
    """
    self._htmlObj.style.add_classes.layout.hover_reduce()
    return self

  def zoom(self):
    """
    Description:
    ------------
    Zoom on the component when the mouse is hover
    """
    self._htmlObj.style.add_classes.layout.hover_zoom()
    return self

  def rotate(self):
    """
    Description:
    ------------
    Rotate the component when the mouse is hover
    """
    self._htmlObj.style.add_classes.layout.hover_rotate()
    return self

  def colored(self):
    """
    Description:
    ------------
    Display the color component when the mouse is hover
    """
    self._htmlObj.style.add_classes.layout.hover_colored()
    return self

  def disappear(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate", fill_mode='forwards'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "disappear"
    if self._htmlObj is not None:
      self._htmlObj.style.css.opacity = 0
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {'opacity': 1}, "100%": {'opacity': 0}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def sliding(self, duration=15, timing_fnc="linear", delay=0, iteration_count="infinite", direction=None, fill_mode=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = "sliding"
    if self._htmlObj is not None:
      self._htmlObj.style.css.padding_right = "2em"
      self._htmlObj.style.css.padding_left = "100%"
      self._htmlObj.style.css.white_space = "nowrap"
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (name, duration, timing_fnc, delay, iteration_count, direction or "", fill_mode or "")
    attrs = {"0%": {'transform': "translate3d(0,0,0)"}, "100%": {'transform': "translate3d(-100%,0,0)"}}
    self._report.body.style.css_class.keyframes(name, attrs)
    return name

  def animate(self, name, targ_css_attrs, orig_css_attrs=None, delay=0, duration=1, timing_fnc="ease-in-out",
              iteration_count="infinite", directions="alternate", fill_mode='forwards'):
    """
    Description:
    ------------
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add the repeatedly glowing effect

    htmlObj.style.effects.animate("pink", {"color": "blue", "width": "400px"})

    Related Pages:

      https://www.w3schools.com/cssref/css_animatable.asp

    Attributes:
    ----------
    :param name: String. The animation name
    :param targ_css_attrs: Dictionary. The different CSS attributes to animate
    :param orig_css_attrs: Dictionary. The initial state of the attributes to animate
    :param delay: Integer. The delay in second before starting the animation
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param duration: Integer. The animation duration in second
    :param iteration_count: Integer. The animation count
    :param directions: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    """
    name = JsUtils.getJsValid(name, fail=False)
    keyframe_name = "animate_%s" % name
    if self._htmlObj is not None:
      self._htmlObj.style.css.animation = "%s %ss %s %ss %s %s %s" % (keyframe_name, duration, timing_fnc, delay, iteration_count, directions, fill_mode)
    if orig_css_attrs is None:
      attrs = {"to": targ_css_attrs}
    else:
      attrs = {"from": orig_css_attrs, "to": targ_css_attrs}
    self._report.body.style.css_class.keyframes(keyframe_name, attrs)
    return name
