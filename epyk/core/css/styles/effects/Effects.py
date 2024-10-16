
from typing import Optional
from epyk.core.py import primitives
from epyk.core.js import JsUtils


class Effects:
  attrs = None

  def __init__(self, page: primitives.PageModel, component: primitives.HtmlModel = None,
               ovrs_attrs: Optional[dict] = None):
    """

    :param page:
    :param component:
    :param Optional[dict] ovrs_attrs:
    """
    self.page, self.component = page, component
    if self.attrs is None:
      self.attrs = {}
    if ovrs_attrs is not None:
      self.attrs = dict(self.attrs)
      self.attrs.update(ovrs_attrs)

  def get_attrs(self) -> dict:
    """
    Return the effect CSS attributes.
    """
    return self.attrs

  def glow(self, color: str, radius: int = 50, duration: int = 1, timing_fnc: str = "ease-in-out",
           delay: int = 0, iteration_count: str = "infinite", direction: str = "alternate",
           fill_mode: str = 'forwards') -> str:
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to
    add the repeatedly glowing effect.

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param str color: The color to use fin the effect
    :param int radius: The length of the radius to display in the animate
    :param int duration: The animation-duration property defines how long time an animation should take to complete.
    :param str timing_fnc: The animation-timing-function property specifies the speed curve of the animation.
    :param int delay: The animation-delay property specifies a delay for the start of an animation.
    :param str iteration_count: The animation-iteration-count property specifies the number of times an animation
    should run.
    :param str direction: The animation-direction property specifies whether an animation should be played forwards,
    backwards or in alternate cycles.
    :param str fill_mode:

    :return: The classname of the animation keyframes
    """
    name = "glow_%s_%s" % (color, radius)
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    color_effects = ["0 0 %s0px %s" % (i, color) for i in range(1, int(radius / 10)+1)]
    if not color_effects:
      color_effects.append("0 0 %spx %s" % (radius, color))
    self.page.body.style.css_class.keyframes(name, {
      "from": {"text-shadow": color_effects}, "to": {"text-shadow": color_effects}})
    return name

  def blink(self, duration: int = 1, timing_fnc: str = "ease-in-out", delay: int = 0,
            iteration_count="infinite", direction="alternate",
            fill_mode='forwards') -> str:
    """

    Related Pages:

      https://www.w3schools.com/css/css3_animations.asp

    :param int duration: The animation-duration property defines how long time an animation should take to complete.
    :param str timing_fnc: The animation-timing-function property specifies the speed curve of the animation.
    :param int delay: The animation-delay property specifies a delay for the start of an animation.
    :param str iteration_count: The animation-iteration-count property specifies the number of times an animation
    should run.
    :param str direction: The animation-direction property specifies whether an animation should be played forwards,
    backwards or in alternate cycles.
    :param str fill_mode:

    :return: The classname of the animation keyframes
    """
    name = "blink"
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    self.page.body.style.css_class.keyframes(name, {"from": {"opacity": 0}, "to": {"opacity": 1}})
    return name

  def shiny_text(self, color, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
                 direction="alternate", fill_mode='forwards'):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to add
    the repeatedly glowing effect

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param color: String. The color to use fin the effect
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    :return: The classname of the animation keyframes
    """
    name = "shiny_text_%s" % color
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    self.page.body.style.css_class.keyframes(name, {"from": {"color": color}, "to": {"color": "none"}})
    return name

  def shiny_border(self, color, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
                   direction="alternate", fill_mode='forwards'):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to
    add the repeatedly glowing effect.

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param color: String. The color to use fin the effect
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    :return: The classname of the animation keyframes
    """
    name = "shiny_border_%s" % color
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"border": "1px solid %s" % color}, "to": {"border": "1px solid %s" % color}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def spin(self, degree=360, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
           direction="alternate", fill_mode='forwards'):
    """

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param degree: Integer.
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    :return: The classname of the animation keyframes.
    """
    name = "spin_%s"
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "rotate(0deg)"}, "to": {"transform": "rotate(%sdeg)" % degree}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def translate(self, start=-100, end=0, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
                direction="alternate", fill_mode='forwards'):
    """

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param start:
    :param end:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    """
    name = "translation_%s_%s" % (start, end)
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "translateY(%s%%)" % start}, "to": {"transform": "translateY(%s)" % end}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def down(self, start=-100, end=0, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
           direction="alternate", fill_mode='forwards'):
    """

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param start:
    :param end:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    :return: The string CSS classname for the animation
    """
    name = "down_%s_%s" % (start, end)
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"from": {"transform": "translateY(%s%%)" % start}, "to": {"transform": "translateY(0)"}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def up(self, bottom=(20, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
         direction="alternate", fill_mode='forwards'):
    """

    Related Pages:

      https://www.w3schools.com/howto/howto_css_glowing_text.asp
      https://www.w3schools.com/css/css3_animations.asp

    :param bottom:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    """
    name = "up_%s_%s" % (bottom[0], bottom[1])
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"bottom": "-%s%s" % (bottom[0], bottom[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"bottom": 0, 'position': 'relative', 'opacity': 1}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def left(self, left=(100, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
           direction="alternate", fill_mode='forwards'):
    """

    :param left:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    """
    name = "left_%s_%s" % (left[0], left[1])
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"left": "-%s%s" % (left[0], left[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"left": 0, 'position': 'relative', 'opacity': 1}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def right(self, right=(100, 'px'), duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
            direction="alternate", fill_mode='forwards'):
    """

    :param right:
    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:

    """
    name = "right_%s_%s" % (right[0], right[1])
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {"right": "-%s%s" % (right[0], right[1]), 'position': 'relative', 'opacity': 0},
             "100%": {"right": 0, 'position': 'relative', 'opacity': 1}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def appear(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite", direction="alternate",
             fill_mode='forwards'):
    """

    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = "appear"
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction)
    self.page.body.style.css_class.keyframes(name, {"0%": {'opacity': 0}, "100%": {'opacity': 1}})
    return name

  def fade_out(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal",
               fill_mode='forwards'):
    """

    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = "fade_out"
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
      self.component.style.css.animation_fill_mode = "forwards"
    self.page.body.style.css_class.keyframes(name, {"0%": {'opacity': 1}, "100%": {'opacity': 0}})
    return name

  def fade_in(self, duration=5, timing_fnc="ease-in-out", delay=0, iteration_count=1, direction="normal",
              fill_mode='forwards'):
    """

    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = "fade_in"
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
      self.component.style.css.animation_fill_mode = "forwards"
    attrs = {"0%": {'opacity': 0}, "100%": {'opacity': 1}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def reduce(self):
    """
    Reduce the component size when the mouse is hover.
    """
    self.component.style.add_classes.layout.hover_reduce()
    return self

  def zoom(self, large: bool = False):
    """
    Zoom on the component when the mouse is hover.

    :param bool large:
    """
    if large:
      self.component.style.add_classes.layout.hover_large_zoom()
    else:
      self.component.style.add_classes.layout.hover_zoom()
    return self

  def rotate(self):
    """
    Rotate the component when the mouse is hover.
    """
    self.component.style.add_classes.layout.hover_rotate()
    return self

  def colored(self):
    """
    Display the color component when the mouse is hover.
    """
    self.component.style.add_classes.layout.hover_colored()
    return self

  def disappear(self, duration=1, timing_fnc="ease-in-out", delay=0, iteration_count="infinite",
                direction="alternate", fill_mode='forwards'):
    """

    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = "disappear"
    if self.component is not None:
      self.component.style.css.opacity = 0
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction, fill_mode)
    attrs = {"0%": {'opacity': 1}, "100%": {'opacity': 0}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def sliding(self, duration=15, timing_fnc="linear", delay=0, iteration_count="infinite", direction=None,
              fill_mode=None):
    """

    :param duration: Integer. The animation-duration property defines how long time an animation should take to complete.
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param delay: Integer. The animation-delay property specifies a delay for the start of an animation.
    :param iteration_count: String. The animation-iteration-count property specifies the number of times an animation should run.
    :param direction: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = "sliding"
    if self.component is not None:
      self.component.style.css.padding_right = "2em"
      self.component.style.css.padding_left = "100%"
      self.component.style.css.white_space = "nowrap"
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        name, duration, timing_fnc, delay, iteration_count, direction or "", fill_mode or "")
    attrs = {"0%": {'transform': "translate3d(0,0,0)"}, "100%": {'transform': "translate3d(-100%,0,0)"}}
    self.page.body.style.css_class.keyframes(name, attrs)
    return name

  def animate(self, name, targ_css_attrs, orig_css_attrs=None, delay=0, duration=1, timing_fnc="ease-in-out",
              iteration_count="infinite", directions="alternate", fill_mode='forwards'):
    """
    Use the text-shadow property to create the neon light effect, and then use animation together with keyframes to
    add the repeatedly glowing effect

    htmlObj.style.effects.animate("pink", {"color": "blue", "width": "400px"})

    Related Pages:

      https://www.w3schools.com/cssref/css_animatable.asp

    :param name: String. The animation name
    :param targ_css_attrs: Dictionary. The different CSS attributes to animate
    :param orig_css_attrs: Dictionary. The initial state of the attributes to animate
    :param delay: Integer. The delay in second before starting the animation
    :param timing_fnc: String. The animation-timing-function property specifies the speed curve of the animation.
    :param duration: Integer. The animation duration in second
    :param iteration_count: Integer. The animation count
    :param directions: String. The animation-direction property specifies whether an animation should be played forwards, backwards or in alternate cycles.
    :param fill_mode:
    """
    name = JsUtils.getJsValid(name, fail=False)
    keyframe_name = "animate_%s" % name
    if self.component is not None:
      self.component.style.css.animation = "%s %ss %s %ss %s %s %s" % (
        keyframe_name, duration, timing_fnc, delay, iteration_count, directions, fill_mode)
    if orig_css_attrs is None:
      attrs = {"to": targ_css_attrs}
    else:
      attrs = {"from": orig_css_attrs, "to": targ_css_attrs}
    self.page.body.style.css_class.keyframes(keyframe_name, attrs)
    return name
