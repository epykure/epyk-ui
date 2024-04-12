
from typing import Union, Optional, Any
from epyk.core.py import types
from epyk.core.css import Defaults_css
from epyk.core.css import FontFamily
from epyk.interfaces import Arguments


def autoPrefixer(prop: str):
  """
  CSS Style function to return the different attributes names for the compatibility with the main browsers.
  This function is used everytime there is a need for a CSS extension.

  The main browsers supported are IE, Chrome, Firefox and Opera

  Related Pages::

    https://www.w3schools.com/cssref/css3_browsersupport.asp

  :param prop: The CSS Attribute key.

  :return: A generator function with the different keys to be added to the style.
  """
  map = {
    'animation': ['-webkit-', '-moz-', '-o-'],
    'animation-direction': ['-webkit-', '-moz-', '-o-'],
    'animation-duration': ['-webkit-', '-moz-', '-o-'],
    'animation-iteration-count': ['-webkit-', '-moz-', '-o-'],
    'animation-timing-function': ['-webkit-', '-moz-', '-o-'],
    'animation-name': ['-webkit-', '-moz-', '-o-'],
    'appearance': ['-webkit-', '-moz-'],
    'backface-visibility': ['-webkit-'],
    'box-decoration-break': ['-webkit-'],
    'font-kerning': ['-webkit-'],
    'font-variant-ligatures': ['-webkit-'],
    'hyphens': ['-webkit-'],
    'image-rendering': ['-moz-'],
    'mask': ['-webkit-'],
    'mask-type': ['-webkit-'],
    'tab-size': ['-moz-'],
    'text-combine-upright': ['-webkit-'],
    'text-decoration-color': ['-webkit-'],
    'text-decoration-line': ['-webkit-'],
    'text-emphasis': ['-webkit-'],
    'text-emphasis-color': ['-webkit-'],
    'text-emphasis-position': ['-webkit-'],
    'text-emphasis-style': ['-webkit-'],
    'text-orientation': ['-webkit-'],
    'transform': ['-webkit-', '-moz-', '-o-'],
    'transition': ['-webkit-', '-moz-', '-o-'],
    'transition-property': ['-webkit-', '-moz-', '-o-'],
    'transition-duration': ['-webkit-', '-moz-', '-o-'],
    'transition-timing-function': ['-webkit-', '-moz-', '-o-'],
    'transition-delay': ['-webkit-', '-moz-', '-o-'],
    'user-select': ['-webkit-', '-moz-', '-o-', '-khtml-', '-ms-'],
      }
  for pref in map.get(prop, []):
    yield "%s%s" % (pref, prop)


class CssMixin:

  @property
  def align_content(self): return self.css("align-content")

  @align_content.setter
  def align_content(self, val):
    val = val if val is not None else 'None'
    self.css({"align-content": val})

  @property
  def align_items(self): return self.css("align-items")

  @align_items.setter
  def align_items(self, val):
    val = val if val is not None else 'None'
    self.css({"align-items": val})

  @property
  def align_self(self): return self.css("align-self")

  @align_self.setter
  def align_self(self, val):
    val = val if val is not None else 'None'
    self.css({"align-self": val})

  @property
  def all(self): return self.css("all")

  @all.setter
  def all(self, val):
    val = val if val is not None else 'None'
    self.css({"all": val})

  @property
  def animation(self):
    """	CSS allows animation of HTML elements without using JavaScript or Flash!

    Related Pages:

      https://www.w3schools.com/css/css3_animations.asp
    """
    return self.css("animation")

  @animation.setter
  def animation(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation"):
      self.css({m_val: val})
    self.css({"animation": val})

  @property
  def animation_delay(self): return self.css("animation-delay")

  @animation_delay.setter
  def animation_delay(self, val):
    val = val if val is not None else 'None'
    self.css({"animation-delay": val})

  @property
  def animation_direction(self):
    """	The animation-direction property defines whether an animation should be played forwards, backwards or in
    alternate cycles.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-direction.asp
    """
    return self.css("animation-direction")

  @animation_direction.setter
  def animation_direction(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation-direction"):
      self.css({m_val: val})
    self.css({"animation-direction": val})

  @property
  def animation_duration(self):
    """	The animation-duration property defines how long an animation should take to complete one cycle.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-duration.asp
    """
    return self.css("animation-duration")

  @animation_duration.setter
  def animation_duration(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation-duration"):
      self.css({m_val: val})
    self.css({"animation-duration": val})

  @property
  def animation_fill_mode(self):
    """	The animation-fill-mode property specifies a style for the target element when the animation is not playing
    (before it starts, after it ends, or both). The animation-fill-mode property can have the following values:

    none - Default value. Animation will not apply any styles to the element before or after it is executing
    forwards - The element will retain the style values that is set by the last keyframe
      (depends on animation-direction and animation-iteration-count)
    backwards - The element will get the style values that is set by the first keyframe
      (depends on animation-direction), and retain this during the animation-delay period
    both - The animation will follow the rules for both forwards and backwards,
      extending the animation properties in both directions

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-fill-mode.asp
    """
    return self.css("animation-fill-mode")

  @animation_fill_mode.setter
  def animation_fill_mode(self, val):
    val = val if val is not None else 'None'
    self.css({"animation-fill-mode": val})

  @property
  def animation_iteration_count(self):
    """	The animation-iteration-count property specifies the number of times an animation should be played.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-iteration-count.asp
    """
    return self.css("animation-iteration-count")

  @animation_iteration_count.setter
  def animation_iteration_count(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation-iteration-count"):
      self.css({m_val: val})
    self.css({"animation-iteration-count": val})

  @property
  def animation_name(self):
    """	The animation-name property specifies a name for the @keyframes animation.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-name.asp
    """
    return self.css("animation-name")

  @animation_name.setter
  def animation_name(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation-name"):
      self.css({m_val: val})
    self.css({"animation-name": val})

  @property
  def animation_play_state(self): return self.css("animation-play-state")

  @animation_play_state.setter
  def animation_play_state(self, val):
    val = val if val is not None else 'None'
    self.css({"animation-play-state": val})

  @property
  def animation_timing_function(self):
    """	The animation-timing-function specifies the speed curve of an animation.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-timing-function.asp
    """
    return self.css("animation-timing-function")

  @animation_timing_function.setter
  def animation_timing_function(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("animation-timing-function"):
      self.css({m_val: val})
    self.css({"animation-timing-function": val})

  @property
  def appearance(self):
    """	This property is frequently used in XUL stylesheets to design custom widgets with platform-appropriate styling.
    It is also used in the XBL implementations of the widgets that ship with the Mozilla platform.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/appearance
    """
    return self.css(autoPrefixer("appearance")[0])

  @appearance.setter
  def appearance(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("appearance"):
      self.css({m_val: val})

  @property
  def backface_visibility(self):
    """	Hide and show the back face of two rotated <div> elements:

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_backface-visibility.asp
    """
    return self.css("backface-visibility")

  @backface_visibility.setter
  def backface_visibility(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("backface-visibility"):
      self.css({m_val: val})
    self.css({"backface-visibility": val})

  @property
  def background(self):
    """	Set different background properties in one declaration

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_background.asp
    """
    return self.css("background")

  @background.setter
  def background(self, val):
    val = val if val is not None else 'None'
    self.css({"background": val})

  @property
  def background_attachment(self): return self.css("background-attachment")

  @background_attachment.setter
  def background_attachment(self, val):
    val = val if val is not None else 'None'
    self.css({"background-attachment": val})

  @property
  def background_blend_mode(self): return self.css("background-blend-mode")

  @background_blend_mode.setter
  def background_blend_mode(self, val):
    val = val if val is not None else 'None'
    self.css({"background-blend-mode": val})

  @property
  def background_clip(self): return self.css("background-clip")

  @background_clip.setter
  def background_clip(self, val):
    val = val if val is not None else 'None'
    self.css({"background-clip": val})

  @property
  def background_color(self):
    """	The background-color property sets the background color of an element.

    The background of an element is the total size of the element, including padding and border (but not the margin).

    Related Pages:

      https://www.w3schools.com/cssref/pr_background-color.asp
    """
    return self.css("background-color")

  @background_color.setter
  def background_color(self, val):
    val = val if val is not None else 'None'
    self.css({"background-color": val})

  @property
  def background_image(self): return self.css("background-image")

  @background_image.setter
  def background_image(self, val):
    val = val if val is not None else 'None'
    self.css({"background-image": val})

  def background_url(self, val: str, size: str = "contain", repeat: str = "no-repeat", position="relative",
                     margin: Union[str, int] = "auto", background_position: str = "center"):
    """	Set the container background from an url.
    This will also set some default usual property.

    :param val: Optional. The picture CSS url.
    :param size: Optional. The CSS background size property.
    :param repeat: Optional. The CSS repeat property.
    :param position: Optional. The CSS position.
    :param margin: Optional. The CSS margin.
    :param background_position: Optional. The CSS background position.
    """
    if val is not None:
      self.css({"background-image": "url(%a)" % val})
    if size is not None:
      self.css({"background-size": size})
    self.css({"background-position": background_position})
    #self.css({"background-attachment": "fixed"})
    self.css({"background-repeat": repeat})
    self.css({"position": position})
    self.css({"margin": margin})

  @property
  def background_origin(self): return self.css("background-origin")

  @background_origin.setter
  def background_origin(self, val):
    val = val if val is not None else 'None'
    self.css({"background-origin": val})

  @property
  def background_position(self):
    """	The background-position property sets the starting position of a background image.

    Related Pages:

      https://www.w3schools.com/cssref/pr_background-position.asp
    """
    return self.css("background-position")

  @background_position.setter
  def background_position(self, val):
    val = val if val is not None else 'None'
    self.css({"background-position": val})

  @property
  def background_repeat(self):
    """	The background-repeat property sets if/how a background image will be repeated.

    Related Pages:

      https://www.w3schools.com/cssref/pr_background-repeat.asp
    """
    return self.css("background-repeat")

  @background_repeat.setter
  def background_repeat(self, val):
    val = val if val is not None else 'None'
    self.css({"background-repeat": val})

  @property
  def background_size(self): return self.css("background-size")

  @background_size.setter
  def background_size(self, val):
    val = val if val is not None else 'None'
    self.css({"background-size": val})

  @property
  def border(self):
    """	The border property is a shorthand property for:
    - border-width
    - border-style (required)
    - border-color

    Related Pages:

      https://www.w3schools.com/cssref/pr_border.asp
    """
    return self.css("border")

  @border.setter
  def border(self, val):
    val = val if val is not None else 'None'
    if val is True:
      val = "1px solid %s" % self.component.page.theme.greys[3]
    self.css({"border": val})

  @property
  def border_bottom(self): return self.css("border-bottom")

  @border_bottom.setter
  def border_bottom(self, val):
    val = val if val is not None else 'None'
    self.css({"border-bottom": val})

  @property
  def border_bottom_color(self): return self.css("border-bottom-color")

  @border_bottom_color.setter
  def border_bottom_color(self, val):
    val = val if val is not None else 'None'
    self.css({"border-bottom-color": val})

  @property
  def border_bottom_left_radius(self): return self.css("border-bottom-left-radius")

  @border_bottom_left_radius.setter
  def border_bottom_left_radius(self, val):
    val = val if val is not None else 'None'
    self.css({"border-bottom-left-radius": val})

  @property
  def border_bottom_right_radius(self): return self.css("border-bottom-right-radius")

  @border_bottom_right_radius.setter
  def border_bottom_right_radius(self, val):
    val = val if val is not None else 'None'
    self.css({"border-bottom-right-radius": val})

  @property
  def border_bottom_style(self): return self.css("border-bottom-style")

  @border_bottom_style.setter
  def border_bottom_style(self, val):
    val = val if val is not None else 'None'
    self.css({"border-bottom-style": val})

  @property
  def border_bottom_width(self): return self.css("border-bottom-width")

  @border_bottom_width.setter
  def border_bottom_width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-bottom-width": val})

  @property
  def border_collapse(self):
    """	The border-collapse property sets whether table borders should collapse into a single border or be separated as
    in standard HTML.

    Related Pages:

      https://www.w3schools.com/cssref/pr_border-collapse.asp
    """
    return self.css("border-collapse")

  @border_collapse.setter
  def border_collapse(self, val):
    val = val if val is not None else 'None'
    self.css({"border-collapse": val})

  @property
  def border_color(self): return self.css("border-color")

  @border_color.setter
  def border_color(self, val):
    val = val if val is not None else 'None'
    self.css({"border-color": val})

  @property
  def border_image(self): return self.css("border-image")

  @border_image.setter
  def border_image(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image": val})

  @property
  def border_image_outset(self): return self.css("border-image-outset")

  @border_image_outset.setter
  def border_image_outset(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image-outset": val})

  @property
  def border_image_repeat(self): return self.css("border-image-repeat")

  @border_image_repeat.setter
  def border_image_repeat(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image-repeat": val})

  @property
  def border_image_slice(self): return self.css("border-image-slice")

  @border_image_slice.setter
  def border_image_slice(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image-slice": val})

  @property
  def border_image_source(self): return self.css("border-image-source")

  @border_image_source.setter
  def border_image_source(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image-source": val})

  @property
  def border_image_width(self): return self.css("border-image-width")

  @border_image_width.setter
  def border_image_width(self, val):
    val = val if val is not None else 'None'
    self.css({"border-image-width": val})

  @property
  def border_left(self): return self.css("border-left")

  @border_left.setter
  def border_left(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      self.css({"border-left": "%spx" % val})
    else:
      self.css({"border-left": val})

  @property
  def border_left_color(self): return self.css("border-left-color")

  @border_left_color.setter
  def border_left_color(self, val):
    val = val if val is not None else 'None'
    self.css({"border-left-color": val})

  @property
  def border_left_style(self): return self.css("border-left-style")

  @border_left_style.setter
  def border_left_style(self, val):
    val = val if val is not None else 'None'
    self.css({"border-left-style": val})

  @property
  def border_left_width(self): return self.css("border-left-width")

  @border_left_width.setter
  def border_left_width(self, val):
    val = val if val is not None else 'None'
    self.css({"border-left-width": val})

  def border_line(self, size: Union[tuple, int] = (1, "px"), color: str = "black"):
    """ Shortcut for border line.

    Usage::

      div = page.ui.div([icons])
      div.style.css.border_line(color="black", size=(2, 'px'))

    :param size: Set the border size
    :param color: Set the border color
    """
    if not isinstance(size, tuple):
      size = (size, "px")
    self.border = "%s%s solid %s" % (size[0], size[1], color)
    return self

  @property
  def border_radius(self):
    """	The border-radius property defines the radius of the element's corners.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_border-radius.asp
    """
    return self.css("border-radius")

  @border_radius.setter
  def border_radius(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-radius": val})

  @property
  def border_right(self): return self.css("border-right")

  @border_right.setter
  def border_right(self, val):
    val = val if val is not None else 'None'
    self.css({"border-right": val})

  @property
  def border_right_color(self): return self.css("border-right-color")

  @border_right_color.setter
  def border_right_color(self, val):
    val = val if val is not None else 'None'
    self.css({"border-right-color": val})

  @property
  def border_right_style(self): return self.css("border-right-style")

  @border_right_style.setter
  def border_right_style(self, val):
    val = val if val is not None else 'None'
    self.css({"border-right-style": val})

  @property
  def border_right_width(self): return self.css("border-right-width")

  @border_right_width.setter
  def border_right_width(self, val):
    val = val if val is not None else 'None'
    self.css({"border-right-width": val})

  @property
  def border_spacing(self):
    """	The border-spacing property sets the distance between the borders of adjacent cells.

    Related Pages:

      https://www.w3schools.com/cssref/pr_border-spacing.asp
    """
    return self.css("border-spacing")

  @border_spacing.setter
  def border_spacing(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-spacing": val})

  @property
  def border_style(self): return self.css("border-style")

  @border_style.setter
  def border_style(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-style": val})

  @property
  def border_top(self): return self.css("border-top")

  @border_top.setter
  def border_top(self, val):
    val = val if val is not None else 'None'
    self.css({"border-top": val})

  @property
  def border_top_color(self): return self.css("border-top-color")

  @border_top_color.setter
  def border_top_color(self, val):
    val = val if val is not None else 'None'
    self.css({"border-top-color": val})

  @property
  def border_top_left_radius(self): return self.css("border-top-left-radius")

  @border_top_left_radius.setter
  def border_top_left_radius(self, val):
    val = val if val is not None else 'None'
    self.css({"border-top-left-radius": val})

  @property
  def border_top_right_radius(self): return self.css("border-top-right-radius")

  @border_top_right_radius.setter
  def border_top_right_radius(self, val):
    val = val if val is not None else 'None'
    self.css({"border-top-right-radius": val})

  @property
  def border_top_style(self): return self.css("border-top-style")

  @border_top_style.setter
  def border_top_style(self, val):
    val = val if val is not None else 'None'
    self.css({"border-top-style": val})

  @property
  def border_top_width(self): return self.css("border-top-width")

  @border_top_width.setter
  def border_top_width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-top-width": val})

  @property
  def border_width(self): return self.css("border-width")

  @border_width.setter
  def border_width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"border-width": val})

  @property
  def bottom(self):
    """	The bottom property affects the vertical position of a positioned element. This property has no effect on
    non-positioned elements.

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_bottom.asp
    """
    return self.css("bottom")

  @bottom.setter
  def bottom(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"bottom": val})

  @property
  def box_decoration_break(self):
    """	The box-decoration-break property specifies how the background, padding, border, border-image, box-shadow, margin,
    and clip-path of an element is applied when the box for the element is fragmented.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_box-decoration-break.asp
    """
    return self.css("box-decoration-break")

  @box_decoration_break.setter
  def box_decoration_break(self, val):
    val = val if val is not None else 'None'
    self.css({"box-decoration-break": val})

  @property
  def box_shadow(self):
    """	The box-shadow property attaches one or more shadows to an element.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_box-shadow.asp
    """
    return self.css("box-shadow")

  @box_shadow.setter
  def box_shadow(self, val):
    val = val if val is not None else 'None'
    self.css({"box-shadow": val})

  @property
  def box_sizing(self): return self.css("box-sizing")

  @box_sizing.setter
  def box_sizing(self, val):
    val = val if val is not None else 'None'
    self.css({"box-sizing": val})

  @property
  def caption_side(self): return self.css("caption-side")

  @caption_side.setter
  def caption_side(self, val):
    val = val if val is not None else 'None'
    self.css({"caption-side": val})

  @property
  def caret_color(self): return self.css("caret-color")

  @caret_color.setter
  def caret_color(self, val):
    val = val if val is not None else 'None'
    self.css({"caret-color": val})

  @property
  def clear(self): return self.css("clear")

  @clear.setter
  def clear(self, val):
    val = val if val is not None else 'None'
    self.css({"clear": val})

  @property
  def clip(self):
    """	What happens if an image is larger than its containing element?

    The clip property lets you specify a rectangle to clip an absolutely positioned element. The rectangle is specified
    as four coordinates, all from the top-left corner of the element to be clipped.

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_clip.asp
    """
    return self.css("clip")

  @clip.setter
  def clip(self, val):
    val = val if val is not None else 'None'
    self.css({"clip": val})

  @property
  def clip_path(self): return self.css("clip-path")

  @clip_path.setter
  def clip_path(self, val):
    val = val if val is not None else 'None'
    self.css({"clip-path": val})

  @property
  def color(self):
    """	The color property specifies the color of text.

    Tip: Use a background color combined with a text color that makes the text easy to read.

    Related Pages:

      https://www.w3schools.com/cssref/pr_text_color.asp
    """
    return self.css("color")

  @color.setter
  def color(self, val):
    val = val if val is not None else 'None'
    self.css({"color": val})

  @property
  def column_count(self): return self.css("column-count")

  @column_count.setter
  def column_count(self, val):
    val = val if val is not None else 'None'
    self.css({"column-count": val})

  @property
  def column_fill(self): return self.css("column-fill")

  @column_fill.setter
  def column_fill(self, val):
    val = val if val is not None else 'None'
    self.css({"column-fill": val})

  @property
  def column_gap(self): return self.css("column-gap")

  @column_gap.setter
  def column_gap(self, val):
    val = val if val is not None else 'None'
    self.css({"column-gap": val})

  @property
  def column_rule(self): return self.css("column-rule")

  @column_rule.setter
  def column_rule(self, val):
    val = val if val is not None else 'None'
    self.css({"column-rule": val})

  @property
  def column_rule_color(self): return self.css("column-rule-color")

  @column_rule_color.setter
  def column_rule_color(self, val):
    val = val if val is not None else 'None'
    self.css({"column-rule-color": val})

  @property
  def column_rule_style(self): return self.css("column-rule-style")

  @column_rule_style.setter
  def column_rule_style(self, val):
    val = val if val is not None else 'None'
    self.css({"column-rule-style": val})

  @property
  def column_rule_width(self): return self.css("column-rule-width")

  @column_rule_width.setter
  def column_rule_width(self, val):
    val = val if val is not None else 'None'
    self.css({"column-rule-width": val})

  @property
  def column_span(self): return self.css("column-span")

  @column_span.setter
  def column_span(self, val):
    val = val if val is not None else 'None'
    self.css({"column-span": val})

  @property
  def column_width(self): return self.css("column-width")

  @column_width.setter
  def column_width(self, val):
    val = val if val is not None else 'None'
    self.css({"column-width": val})

  @property
  def columns(self): return self.css("columns")

  @columns.setter
  def columns(self, val):
    val = val if val is not None else 'None'
    self.css({"columns": val})

  @property
  def content(self): return self.css("content")

  @content.setter
  def content(self, val):
    val = val if val is not None else 'None'
    self.css({"content": val})

  @property
  def counter_increment(self): return self.css("counter-increment")

  @counter_increment.setter
  def counter_increment(self, val):
    val = val if val is not None else 'None'
    self.css({"counter-increment": val})

  @property
  def counter_reset(self): return self.css("counter-reset")

  @counter_reset.setter
  def counter_reset(self, val):
    val = val if val is not None else 'None'
    self.css({"counter-reset": val})

  @property
  def cursor(self):
    """	The cursor property specifies the mouse cursor to be displayed when pointing over an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_cursor.asp
    """
    return self.css("cursor")

  @cursor.setter
  def cursor(self, val):
    val = val if val is not None else 'None'
    self.css({"cursor": val})

  def dark(self, flag: bool = True):
    """Set the dark mode based on the theme definition for the component.

    :param flag: Flag to enable / disable the dark mode
    """
    if flag:
      self.css({"background": self.page.theme.black, "color": self.page.theme.white})
    else:
      self.css({"background": self.page.theme.white, "color": self.page.theme.black})

  @property
  def direction(self): return self.css("direction")

  @direction.setter
  def direction(self, val):
    val = val if val is not None else 'None'
    self.css({"direction": val})

  @property
  def display(self):
    """	The display property specifies the display behavior (the type of rendering box) of an element.

    In HTML, the default display property value is taken from the HTML specifications or from the browser/user default
    style sheet. The default value in XML is inline, including SVG elements.

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_display.asp
    """
    return self.css("display")

  @display.setter
  def display(self, val):
    val = val if val is not None else 'None'
    if val is False:
      val = 'None'
    self.css({"display": val})

  @property
  def empty_cells(self): return self.css("empty-cells")

  @empty_cells.setter
  def empty_cells(self, val):
    val = val if val is not None else 'None'
    self.css({"empty-cells": val})

  @property
  def filter(self): return self.css("filter")

  @filter.setter
  def filter(self, val):
    val = val if val is not None else 'None'
    self.css({"filter": val})

  @property
  def flex(self): return self.css("flex")

  @flex.setter
  def flex(self, val):
    val = val if val is not None else 'None'
    self.css({"flex": val})

  @property
  def flex_basis(self): return self.css("flex-basis")

  @flex_basis.setter
  def flex_basis(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-basis": val})

  @property
  def flex_direction(self): return self.css("flex-direction")

  @flex_direction.setter
  def flex_direction(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-direction": val})

  @property
  def flex_flow(self): return self.css("flex-flow")

  @flex_flow.setter
  def flex_flow(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-flow": val})

  @property
  def flex_grow(self): return self.css("flex-grow")

  @flex_grow.setter
  def flex_grow(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-grow": val})

  @property
  def flex_shrink(self): return self.css("flex-shrink")

  @flex_shrink.setter
  def flex_shrink(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-shrink": val})

  @property
  def flex_wrap(self): return self.css("flex-wrap")

  @flex_wrap.setter
  def flex_wrap(self, val):
    val = val if val is not None else 'None'
    self.css({"flex-wrap": val})

  @property
  def float(self):
    """	The float property specifies how an element should float

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_float.asp
    """
    return self.css("float")

  @float.setter
  def float(self, val):
    val = val if val is not None else 'none'
    defined_vals = set(['none', 'left', 'right', 'initial', 'inherit'])
    if Defaults_css.CSS_EXCEPTIONS and val not in defined_vals:
      raise ValueError(Defaults_css.CSS_EXCEPTIONS_FORMAT % ("float", val))

    self.css({"float": val})

  @property
  def font(self): return self.css("font")

  @font.setter
  def font(self, val):
    val = val if val is not None else 'None'
    self.css({"font": val})

  @property
  def font_family(self):
    """	The font-family property specifies the font for an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_font_font-family.asp
    """
    return self.css("font-family")

  @font_family.setter
  def font_family(self, val):
    val = val if val is not None else 'None'
    if val not in self.component.page._props['css']["font-face"] and val in FontFamily.GoogleFonts.fonts:
      self.component.page.headers.links.stylesheet(FontFamily.GoogleFonts.href % val)
    self.css({"font-family": val})

  @property
  def font_kerning(self): return self.css("font-kerning")

  @font_kerning.setter
  def font_kerning(self, val):
    val = val if val is not None else 'None'
    self.css({"font-kerning": val})

  @property
  def font_size(self):
    """	The font-size property sets the size of a font.

    Related Pages:

      https://www.w3schools.com/cssref/pr_font_font-size.asp
    """
    return self.css("font-size")

  @font_size.setter
  def font_size(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val if val is not None else 'None'
    self.css({"font-size": val})

  @property
  def font_size_adjust(self): return self.css("font-size-adjust")

  @font_size_adjust.setter
  def font_size_adjust(self, val):
    val = val if val is not None else 'None'
    self.css({"font-size-adjust": val})

  @property
  def font_stretch(self): return self.css("font-stretch")

  @font_stretch.setter
  def font_stretch(self, val):
    val = val if val is not None else 'None'
    self.css({"font-stretch": val})

  @property
  def font_style(self): return self.css("font-style")

  @font_style.setter
  def font_style(self, val):
    val = val if val is not None else 'None'
    self.css({"font-style": val})

  @property
  def font_variant(self): return self.css("font-variant")

  @font_variant.setter
  def font_variant(self, val):
    val = val if val is not None else 'None'
    self.css({"font-variant": val})

  @property
  def font_weight(self):
    """	The font-weight property sets how thick or thin characters in text should be displayed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_font_weight.asp
    """
    return self.css("font-weight")

  @font_weight.setter
  def font_weight(self, val):
    val = val if val is not None else 'None'
    self.css({"font-weight": val})

  @property
  def grid(self): return self.css("grid")

  @grid.setter
  def grid(self, val):
    val = val if val is not None else 'None'
    self.css({"grid": val})

  @property
  def grid_area(self): return self.css("grid-area")

  @grid_area.setter
  def grid_area(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-area": val})

  @property
  def grid_auto_columns(self): return self.css("grid-auto-columns")

  @grid_auto_columns.setter
  def grid_auto_columns(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-auto-columns": val})

  @property
  def grid_auto_flow(self): return self.css("grid-auto-flow")

  @grid_auto_flow.setter
  def grid_auto_flow(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-auto-flow": val})

  @property
  def grid_auto_rows(self): return self.css("grid-auto-rows")

  @grid_auto_rows.setter
  def grid_auto_rows(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-auto-rows": val})

  @property
  def grid_column(self): return self.css("grid-column")

  @grid_column.setter
  def grid_column(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-column": val})

  @property
  def grid_column_end(self): return self.css("grid-column-end")

  @grid_column_end.setter
  def grid_column_end(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-column-end": val})

  @property
  def grid_column_gap(self): return self.css("grid-column-gap")

  @grid_column_gap.setter
  def grid_column_gap(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-column-gap": val})

  @property
  def grid_column_start(self): return self.css("grid-column-start")

  @grid_column_start.setter
  def grid_column_start(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-column-start": val})

  @property
  def grid_gap(self): return self.css("grid-gap")

  @grid_gap.setter
  def grid_gap(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-gap": val})

  @property
  def grid_row(self): return self.css("grid-row")

  @grid_row.setter
  def grid_row(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-row": val})

  @property
  def grid_row_end(self): return self.css("grid-row-end")

  @grid_row_end.setter
  def grid_row_end(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-row-end": val})

  @property
  def grid_row_gap(self): return self.css("grid-row-gap")

  @grid_row_gap.setter
  def grid_row_gap(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-row-gap": val})

  @property
  def grid_row_start(self): return self.css("grid-row-start")

  @grid_row_start.setter
  def grid_row_start(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-row-start": val})

  @property
  def grid_template(self): return self.css("grid-template")

  @grid_template.setter
  def grid_template(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-template": val})

  @property
  def grid_template_areas(self): return self.css("grid-template-areas")

  @grid_template_areas.setter
  def grid_template_areas(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-template-areas": val})

  @property
  def grid_template_columns(self): return self.css("grid-template-columns")

  @grid_template_columns.setter
  def grid_template_columns(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-template-columns": val})

  @property
  def grid_template_rows(self): return self.css("grid-template-rows")

  @grid_template_rows.setter
  def grid_template_rows(self, val):
    val = val if val is not None else 'None'
    self.css({"grid-template-rows": val})

  @property
  def hanging_punctuation(self): return self.css("hanging-punctuation")

  @hanging_punctuation.setter
  def hanging_punctuation(self, val):
    val = val if val is not None else 'None'
    self.css({"hanging-punctuation": val})

  @property
  def height(self):
    """	The height property sets the height of an element.

    The height of an element does not include padding, borders, or margins!

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_height.asp
    """
    return self.css("height")

  @height.setter
  def height(self, val):
    if val is False:
      if "height" in self.attrs:
        del self.attrs['height']
      if "height" in self.component.attr["css"]:
        del self.component.attr["css"]["height"]
    else:
      val = val if val is not None else 'None'
      if isinstance(val, int):
        val = "%spx" % val
      self.css({"height": val})

  @property
  def hyphens(self): return self.css("hyphens")

  @hyphens.setter
  def hyphens(self, val):
    val = val if val is not None else 'None'
    self.css({"hyphens": val})

  @property
  def isolation(self): return self.css("isolation")

  @isolation.setter
  def isolation(self, val):
    val = val if val is not None else 'None'
    self.css({"isolation": val})

  @property
  def inline_size(self):
    return self.css("inline-size")

  @inline_size.setter
  def inline_size(self, val):
    val = val if val is not None else 'None'
    self.css({"inline-size": val})
    
  @property
  def justify_content(self):
    """	The justify-content property aligns the flexible container's items when the items do not use all available space on
    the main-axis (horizontally). This property is not inherited.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_justify-content.asp
    """
    return self.css("justify-content")

  @justify_content.setter
  def justify_content(self, val):
    vals = set(["flex-start", "flex-end", "center", "space-between", "space-around", "initial", "inherit"])
    val = val if val is not None else 'None'
    self.css({"justify-content": val})

  @property
  def left(self):
    """	The left property affects the horizontal position of a positioned element. This property has no effect on
    non-positioned elements.

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_left.asp
    """
    return self.css("left")

  @left.setter
  def left(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val if val is not None else 'None'
    self.css({"left": val})

  @property
  def letter_spacing(self): return self.css("letter-spacing")

  @letter_spacing.setter
  def letter_spacing(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"letter-spacing": val})

  @property
  def line_height(self):
    """	The line-height property specifies the height of a line.

    Note: Negative values are not allowed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_line-height.asp
    """
    return self.css("line-height")

  @line_height.setter
  def line_height(self, val):
    if val is False:
      self.remove()
    else:
      if isinstance(val, int):
        val = "%spx" % val
      val = val if val is not None else 'None'
      self.css({"line-height": val})

  @property
  def list_style(self): return self.css("list-style")

  @list_style.setter
  def list_style(self, val):
    val = val if val is not None else 'None'
    self.css({"list-style": val})

  @property
  def list_style_image(self): return self.css("list-style-image")

  @list_style_image.setter
  def list_style_image(self, val):
    val = val if val is not None else 'None'
    self.css({"list-style-image": val})

  @property
  def list_style_position(self): return self.css("list-style-position")

  @list_style_position.setter
  def list_style_position(self, val):
    val = val if val is not None else 'None'
    self.css({"list-style-position": val})

  @property
  def list_style_type(self): return self.css("list-style-type")

  @list_style_type.setter
  def list_style_type(self, val):
    val = val if val is not None else 'None'
    self.css({"list-style-type": val})

  @property
  def margin(self):
    """	The margin property sets the margins for an element, and is a shorthand property for the following properties:
    - margin-top
    - margin-right
    - margin-bottom
    - margin-left

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin.asp
    """
    return self.css("margin")

  @margin.setter
  def margin(self, val):
    if val is False:
      self.remove()
    else:
      if isinstance(val, int):
        val = "%spx" % val
      val = val if val is not None else 'None'
      self.css({"margin": val})

  @property
  def margin_bottom(self):
    """	The margin-bottom property sets the bottom margin of an element.

    Note: Negative values are allowed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-bottom.asp
    """
    return self.css("margin-bottom")

  @margin_bottom.setter
  def margin_bottom(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"margin-bottom": val})

  @property
  def margin_h(self):
    """	Set the margin left and right with the same value.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-left.asp
      https://www.w3schools.com/cssref/pr_margin-right.asp
    """
    return self.margin_left, self.margin_right

  @margin_h.setter
  def margin_h(self, val):
    self.margin_left = val
    self.margin_right = val
    if self.component is not None and isinstance(val, int) and self.component.style.css.width is not None and self.component.style.css.width.endswith("%"):
      self.component.style.css.width = "calc(%s - %spx)" % (self.component.style.css.width, 2*val)

  @property
  def margin_v(self):
    """	Set the margin top and bottom with the same value.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-top.asp
      https://www.w3schools.com/cssref/pr_margin-bottom.asp
    """
    return self.margin_top, self.margin_bottom

  @margin_v.setter
  def margin_v(self, val):
    self.margin_top = val
    self.margin_bottom = val

  @property
  def margin_left(self):
    """	The margin-left property sets the left margin of an element.

    Note: Negative values are allowed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-left.asp
    """
    return self.css("margin-left")

  @margin_left.setter
  def margin_left(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val if val is not None else 'None'
    self.css({"margin-left": val})

  @property
  def margin_right(self):
    """	The margin-right property sets the right margin of an element.

    Note: Negative values are allowed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-right.asp
    """
    return self.css("margin-right")

  @margin_right.setter
  def margin_right(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"margin-right": val})

  @property
  def margin_top(self):
    """	The margin-top property sets the top margin of an element.

    Note: Negative values are allowed.

    Related Pages:

      https://www.w3schools.com/cssref/pr_margin-top.asp
    """
    return self.css("margin-top")

  @margin_top.setter
  def margin_top(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val if val is not None else 'None'
    self.css({"margin-top": val})

  @property
  def max_height(self): return self.css("max-height")

  @max_height.setter
  def max_height(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.overflow_y = "auto"
    self.css({"max-height": val})

  @property
  def max_width(self): return self.css("max-width")

  @max_width.setter
  def max_width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"max-width": val})

  @property
  def min_height(self):
    """	The min-height property defines the minimum height of an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_min-height.asp
    """
    return self.css("min-height")

  @min_height.setter
  def min_height(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"min-height": val})

  @property
  def min_width(self): return self.css("min-width")

  @min_width.setter
  def min_width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"min-width": val})

  @property
  def mix_blend_mode(self): return self.css("mix-blend-mode")

  @mix_blend_mode.setter
  def mix_blend_mode(self, val):
    val = val if val is not None else 'None'
    self.css({"mix-blend-mode": val})

  @property
  def object_fit(self): return self.css("object-fit")

  @object_fit.setter
  def object_fit(self, val):
    val = val if val is not None else 'None'
    self.css({"object-fit": val})

  @property
  def object_position(self): return self.css("object-position")

  @object_position.setter
  def object_position(self, val):
    val = val if val is not None else 'None'
    self.css({"object-position": val})

  @property
  def opacity(self):
    """	The opacity property sets the opacity level for an element.

    The opacity-level describes the transparency-level, where 1 is not transparent at all, 0.5 is 50% see-through,
    and 0 is completely transparent.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_opacity.asp
    """
    return self.css("opacity")

  @opacity.setter
  def opacity(self, val):
    val = val if val is not None else 'None'
    self.css({"opacity": val})

  @property
  def order(self): return self.css("order")

  @order.setter
  def order(self, val):
    val = val if val is not None else 'None'
    self.css({"order": val})

  @property
  def outline(self): return self.css("outline")

  @outline.setter
  def outline(self, val):
    val = val if val is not None else 'None'
    self.css({"outline": val})

  @property
  def outline_color(self): return self.css("outline-color")

  @outline_color.setter
  def outline_color(self, val):
    val = val if val is not None else 'None'
    self.css({"outline-color": val})

  @property
  def outline_offset(self): return self.css("outline-offset")

  @outline_offset.setter
  def outline_offset(self, val):
    val = val if val is not None else 'None'
    self.css({"outline-offset": val})

  @property
  def outline_style(self): return self.css("outline-style")

  @outline_style.setter
  def outline_style(self, val):
    val = val if val is not None else 'None'
    self.css({"outline-style": val})

  @property
  def outline_width(self): return self.css("outline-width")

  @outline_width.setter
  def outline_width(self, val):
    val = val if val is not None else 'None'
    self.css({"outline-width": val})

  @property
  def overflow(self):
    """	The overflow property specifies what should happen if content overflows an element's box.

    This property specifies whether to clip content or to add scrollbars when an element's content is too big to fit
    in a specified area.

    Note: The overflow property only works for block elements with a specified height.

    Values: visible|hidden|scroll|auto|initial|inherit

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_overflow.asp
    """
    return self.css("overflow")

  @overflow.setter
  def overflow(self, val):
    val = val if val is not None else 'None'
    self.css({"overflow": val})

  @property
  def overflow_wrap(self):
    """	The overflow-wrap property specifies whether or not the browser can break lines with long words,
    if they overflow the container.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_overflow-wrap.asp
    """
    return self.css("overflow-wrap")

  @overflow_wrap.setter
  def overflow_wrap(self, val):
    val = val if val is not None else 'None'
    self.css({"overflow-wrap": val})
    self.css({"word-wrap": val})

  @property
  def overflow_x(self):
    """	The overflow-x property specifies whether to clip the content, add a scroll bar, or display overflow content of a
    block-level element, when it overflows at the left and right edges.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_overflow-x.asp
    """
    return self.css("overflow-x")

  @overflow_x.setter
  def overflow_x(self, val):
    val = val if val is not None else 'None'
    self.css({"overflow-x": val})

  @property
  def overflow_y(self):
    """	The overflow-y property specifies whether to clip the content, add a scroll bar, or display overflow content of
    a block-level element, when it overflows at the top and bottom edges.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_overflow-y.asp
    """
    return self.css("overflow-y")

  @overflow_y.setter
  def overflow_y(self, val):
    val = val if val is not None else 'None'
    self.css({"overflow-y": val})

  @property
  def padding(self):
    """	The CSS padding properties are used to generate space around an element's content, inside of any defined borders.

    Related Pages:

      https://www.w3schools.com/css/css_padding.asp
    """
    return self.css("padding")

  @padding.setter
  def padding(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"padding": val})

  @property
  def padding_bottom(self):
    """	An element's padding is the space between its content and its border.

    The padding-bottom property sets the bottom padding (space) of an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-bottom.asp
    """
    return self.css("padding-bottom")

  @padding_bottom.setter
  def padding_bottom(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"padding-bottom": val})

  @property
  def padding_h(self):
    """	Set the padding left and right with the same value.

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-left.asp
      https://www.w3schools.com/cssref/pr_padding-right.asp
    """
    return self.padding_left, self.padding_right

  @padding_h.setter
  def padding_h(self, val):
    self.padding_left = val
    self.padding_right = val

  @property
  def padding_v(self):
    """	Set the padding top and bottom with the same value.

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-left.asp
      https://www.w3schools.com/cssref/pr_padding-right.asp
    """
    return self.padding_top, self.padding_bottom

  @padding_v.setter
  def padding_v(self, val):
    self.padding_top = val
    self.padding_bottom = val

  @property
  def padding_left(self):
    """	An element's padding is the space between its content and its border.

    The padding-left property sets the left padding (space) of an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-left.asp
    """
    return self.css("padding-left")

  @padding_left.setter
  def padding_left(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"padding-left": val})

  @property
  def padding_right(self):
    """	An element's padding is the space between its content and its border

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-right.asp
    """
    return self.css("padding-right")

  @padding_right.setter
  def padding_right(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"padding-right": val})

  @property
  def padding_top(self):
    """	An element's padding is the space between its content and its border.

    The padding-top property sets the top padding (space) of an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_padding-top.asp
    """
    return self.css("padding-top")

  @padding_top.setter
  def padding_top(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val if val is not None else 'None'
    self.css({"padding-top": val})

  @property
  def page_break_after(self): return self.css("page-break-after")

  @page_break_after.setter
  def page_break_after(self, val):
    val = val if val is not None else 'None'
    self.css({"page-break-after": val})

  @property
  def page_break_before(self): return self.css("page-break-before")

  @page_break_before.setter
  def page_break_before(self, val):
    val = val if val is not None else 'None'
    self.css({"page-break-before": val})

  @property
  def page_break_inside(self): return self.css("page-break-inside")

  @page_break_inside.setter
  def page_break_inside(self, val):
    val = val if val is not None else 'None'
    self.css({"page-break-inside": val})

  @property
  def perspective(self): return self.css("perspective")

  @perspective.setter
  def perspective(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"perspective": val})

  @property
  def perspective_origin(self): return self.css("perspective-origin")

  @perspective_origin.setter
  def perspective_origin(self, val):
    val = val if val is not None else 'None'
    self.css({"perspective-origin": val})

  @property
  def pointer_events(self): return self.css("pointer-events")

  @pointer_events.setter
  def pointer_events(self, val):
    val = val if val is not None else 'None'
    self.css({"pointer-events": val})

  @property
  def position(self):
    """	The position property specifies the type of positioning method used for an element (static, relative, absolute,
    fixed, or sticky).

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_position.asp
    """
    return self.css("position")

  @position.setter
  def position(self, val):
    val = val if val is not None else 'None'
    if val in ["sticky"]:
      self.css({"position": "-webkit-%s" % val})
    self.css({"position": val})

  @property
  def quotes(self): return self.css("quotes")

  @quotes.setter
  def quotes(self, val: str):
    val = val if val is not None else 'None'
    self.css({"quotes": val})

  @property
  def resize(self): return self.css("resize")

  @resize.setter
  def resize(self, val):
    val = val if val is not None else 'None'
    self.css({"resize": val})

  @property
  def right(self):
    """	The right property affects the horizontal position of a positioned element.
    This property has no effect on non-positioned elements.

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_right.asp
    """
    return self.css("right")

  @right.setter
  def right(self, val):
    val = val if val is not None else 'None'
    if isinstance(val , int):
      val = "%spx" % val
    self.css({"right": val})

  @property
  def scroll_behavior(self): return self.css("scroll-behavior")

  @scroll_behavior.setter
  def scroll_behavior(self, val):
    val = val if val is not None else 'None'
    self.css({"scroll-behavior": val})

  @property
  def tab_size(self): return self.css("tab-size")

  @tab_size.setter
  def tab_size(self, val):
    val = val if val is not None else 'None'
    self.css({"tab-size": val})

  @property
  def table_layout(self): return self.css("table-layout")

  @table_layout.setter
  def table_layout(self, val):
    val = val if val is not None else 'None'
    self.css({"table-layout": val})

  @property
  def text_align(self):
    """	The text-align property specifies the horizontal alignment of text in an element.

    Related Pages:

      https://www.w3schools.com/cssref/pr_text_text-align.ASP
    """
    return self.css("text-align")

  @text_align.setter
  def text_align(self, val):
    val = val if val is not None else 'None'
    vals = ['center', 'None', 'left', 'right', 'justify', 'inherit', 'initial']
    first_val = val.split(" ")[0]
    if Defaults_css.CSS_EXCEPTIONS and first_val not in vals:
      raise ValueError(Defaults_css.CSS_EXCEPTIONS_FORMAT % ("text_align", val))

    self.css({"text-align": val})

  @property
  def text_align_last(self): return self.css("text-align-last")

  @text_align_last.setter
  def text_align_last(self, val):
    val = val if val is not None else 'None'
    self.css({"text-align-last": val})

  @property
  def text_decoration(self): return self.css("text-decoration")

  @text_decoration.setter
  def text_decoration(self, val):
    val = val if val is not None else 'None'
    self.css({"text-decoration": val})

  @property
  def text_decoration_color(self): return self.css("text-decoration-color")

  @text_decoration_color.setter
  def text_decoration_color(self, val):
    val = val if val is not None else 'None'
    self.css({"text-decoration-color": val})

  @property
  def text_decoration_line(self): return self.css("text-decoration-line")

  @text_decoration_line.setter
  def text_decoration_line(self, val):
    val = val if val is not None else 'None'
    self.css({"text-decoration-line": val})

  @property
  def text_decoration_style(self): return self.css("text-decoration-style")

  @text_decoration_style.setter
  def text_decoration_style(self, val):
    val = val if val is not None else 'None'
    self.css({"text-decoration-style": val})

  @property
  def text_indent(self): return self.css("text-indent")

  @text_indent.setter
  def text_indent(self, val):
    val = val if val is not None else 'None'
    self.css({"text-indent": val})

  @property
  def text_justify(self): return self.css("text-justify")

  @text_justify.setter
  def text_justify(self, val):
    val = val if val is not None else 'None'
    self.css({"text-justify": val})

  @property
  def text_overflow(self): return self.css("text-overflow")

  @text_overflow.setter
  def text_overflow(self, val):
    val = val if val is not None else 'None'
    self.css({"text-overflow": val})

  @property
  def text_shadow(self):
    """	The text-shadow property adds shadow to text.

    This property accepts a comma-separated list of shadows to be applied to the text.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_text-shadow.asp
    """
    return self.css("text-shadow")

  @text_shadow.setter
  def text_shadow(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, list):
      val = ",".join(val)
    self.css({"text-shadow": val})

  @property
  def text_transform(self):
    """	The text-transform property controls the capitalization of text.

    Related Pages:

      https://www.w3schools.com/cssref/pr_text_text-transform.asp
    """
    return self.css("text-transform")

  @text_transform.setter
  def text_transform(self, val):
    val = val if val is not None else 'None'
    self.css({"text-transform": val})

  @property
  def text_stoke(self):
    """	The -webkit-text-stroke CSS property specifies the width and color of strokes for text characters.
    This is a shorthand property for the longhand properties -webkit-text-stroke-width and -webkit-text-stroke-color.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-stroke
    """
    return self.css("-webkit-text-stroke")

  @text_stoke.setter
  def text_stoke(self, val):
    val = val if val is not None else 'None'
    self.css({"-webkit-text-stroke": val})

  @property
  def text_stoke_width(self):
    """	The -webkit-text-stroke-width CSS property specifies the width of the stroke for text.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-stroke-width
    """
    return self.css("-webkit-text-stroke-width")

  @text_stoke_width.setter
  def text_stoke_width(self, val):
    val = val if val is not None else 'None'
    self.css({"-webkit-text-stroke-width": val})

  @property
  def text_stoke_color(self):
    """	The -webkit-text-stroke-color CSS property specifies the stroke color of characters of text.
    If this property is not set, the value of the color property is used.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-text-stroke-color
    """
    return self.css("-webkit-text-stroke-color")

  @text_stoke_color.setter
  def text_stoke_color(self, val):
    val = val if val is not None else 'None'
    self.css({"-webkit-text-stroke-color": val})

  @property
  def top(self):
    """	The top property affects the vertical position of a positioned element.
    This property has no effect on non-positioned elements.

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_top.asp
    """
    return self.css("top")

  @top.setter
  def top(self, val):
    if val is None:
      val = 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.css({"top": val})

  @property
  def transform(self):
    """	The transform property applies a 2D or 3D transformation to an element.
    This property allows you to rotate, scale, move, skew, etc., elements.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_transform.asp
    """
    return self.css("transform")

  @transform.setter
  def transform(self, val):
    val = val if val is not None else 'None'
    self.css({"transform": val})

  def rotate(self, val):
    """	Defines a 2D rotation, the angle is specified in the parameter

    Related Pages:

      https://css-tricks.com/snippets/css/text-rotation/
      https://www.w3schools.com/cssref/css3_pr_transform.asp

    :param val: Integer | String. The rotation angle.
    """
    if isinstance(val, int):
      val = "%sdeg" % val
    self.transform = "rotate(%s)" % val

  @property
  def transform_origin(self): return self.css("transform-origin")

  @transform_origin.setter
  def transform_origin(self, val):
    val = val if val is not None else 'None'
    self.css({"transform-origin": val})

  @property
  def transform_style(self): return self.css("transform-style")

  @transform_style.setter
  def transform_style(self, val):
    val = val if val is not None else 'None'
    self.css({"transform-style": val})

  @property
  def transition(self): return self.css("transition")

  @transition.setter
  def transition(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, (float, int)):
      val = "%ss" % val
    self.css({"transition": val})

  @property
  def transition_delay(self): return self.css("transition-delay")

  @transition_delay.setter
  def transition_delay(self, val):
    val = val if val is not None else 'None'
    self.css({"transition-delay": val})

  @property
  def transition_duration(self): return self.css("transition-duration")

  @transition_duration.setter
  def transition_duration(self, val):
    val = val if val is not None else 'None'
    self.css({"transition-duration": val})

  @property
  def transition_property(self): return self.css("transition-property")

  @transition_property.setter
  def transition_property(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("transition-property"):
      self.css({m_val: val})
    self.css({"transition-property": val})

  @property
  def transition_timing_function(self):
    return self.css("transition-timing-function")

  @transition_timing_function.setter
  def transition_timing_function(self, val):
    val = val if val is not None else 'None'
    self.css({"transition-timing-function": val})

  @property
  def unicode_bidi(self): return self.css("unicode-bidi")

  @unicode_bidi.setter
  def unicode_bidi(self, val):
    val = val if val is not None else 'None'
    self.css({"unicode-bidi": val})

  @property
  def user_select(self):
    """	The user-select property specifies whether the text of an element can be selected.

    In web browsers, if you double-click on some text it will be selected/highlighted.
    This property can be used to prevent this.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_user-select.asp
    """
    return self.css("user-select")

  @user_select.setter
  def user_select(self, val):
    val = val if val is not None else 'None'
    for m_val in autoPrefixer("user-select"):
      self.css({m_val: val})
    self.css({"user-select": val})

  @property
  def vertical_align(self):
    """	The vertical-align property sets the vertical alignment of an element

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_vertical-align.asp
    """
    return self.css("vertical-align")

  @vertical_align.setter
  def vertical_align(self, val):
    val = val if val is not None else 'None'
    vals = ["baseline", "length", "sub", "super", "top", "text-top", "middle", "bottom", "text-bottom", "initial",
            "inherit", 'None']
    if Defaults_css.CSS_EXCEPTIONS and val not in vals:
      raise ValueError(Defaults_css.CSS_EXCEPTIONS_FORMAT % ("vertical_align", val))

    self.css({"vertical-align": val})

  @property
  def visibility(self): return self.css("visibility")

  @visibility.setter
  def visibility(self, val):
    val = val if val is not None else 'None'
    self.css({"visibility": val})

  @property
  def white_space(self): return self.css("white-space")

  @white_space.setter
  def white_space(self, val):
    val = val if val is not None else 'None'
    self.css({"white-space": val})

  def nowrap(self):
    """

    """
    self.css({"white-space": "nowrap"})

  @property
  def width(self):
    """	The width property sets the width of an element.

    The width of an element does not include padding, borders, or margins!

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_width.asp
    """
    return self.css("width")

  @width.setter
  def width(self, val):
    if val is False:
      if "width" in self.component.attrs:
        del self.component.attrs['width']
      if "width" in self.component.attr["css"]:
        del self.component.attr["css"]["width"]
    else:
      val = val if val is not None else 'None'
      if isinstance(val, int):
        val = "%spx" % val
      self.css({"width": val})

  def width_calc(self, width_in_px: int, container_width: Optional[int] = 100):
    """	Use calc() to calculate the width of a component.

    Related Pages:

      https://www.w3schools.com/cssref/func_calc.asp

    :param int width_in_px: The width used by other components in the line.
    :param int container_width: The percentage width to be used by the component in total. Default 100%.
    """
    self.display = "inline-block"
    if container_width is None:
      container_width = self.width
    else:
      container_width = "%s%%" % container_width
    self.width = "calc(%s - %spx)" % (container_width, width_in_px)
    return self

  @property
  def word_break(self): return self.css("word-break")

  @word_break.setter
  def word_break(self, val):
    val = val if val is not None else 'None'
    self.css({"word-break": val})

  @property
  def word_spacing(self): return self.css("word-spacing")

  @word_spacing.setter
  def word_spacing(self, val):
    val = val if val is not None else 'None'
    self.css({"word-spacing": val})

  @property
  def word_wrap(self): return self.css("word-wrap")

  @word_wrap.setter
  def word_wrap(self, val):
    val = val if val is not None else 'None'
    self.css({"word-wrap": val})

  @property
  def writing_mode(self): return self.css("writing-mode")

  @writing_mode.setter
  def writing_mode(self, val):
    val = val if val is not None else 'None'
    self.css({"writing-mode": val})

  @property
  def z_index(self):
    """	The z-index property specifies the stack order of an element.

    An element with greater stack order is always in front of an element with a lower stack order.

    Note: z-index only works on positioned elements (position: absolute, position: relative, position:
    fixed, or position: sticky).

    Related Pages:

      https://www.w3schools.com/cssref/pr_pos_z-index.asp
    """
    return self.css("z-index")

  @z_index.setter
  def z_index(self, val):
    val = val if val is not None else 'None'
    self.css({"z-index": val})

  def middle(self, line_height: Optional[int] = None):
    """	Set the vertical align to middle and also the line height is a value is supplied.

    Usage::

      component.style.css.middle(25)

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_line-height.asp
      https://www.w3schools.com/cssref/pr_pos_vertical-align.asp

    :param line_height: Optional. Set the line height CSS property.
    """
    self.vertical_align = "middle"
    self.text_align = "center"
    if line_height is not None:
      self.line_height = line_height
    return self

  def sticky(self, top: int = 0, bottom: Optional[int] = None, left: Optional[int] = None, right: Optional[int] = None,
             z_index: int = 400):
    """	An element with position: sticky; is positioned based on the user's scroll position

    Usage::

      component.style.css.sticky()

    Related Pages:

      https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_sticky_element

    :param top: The number of pixel from the top
    :param bottom:
    :param left:
    :param right:
    :param z_index: Optional. The CSS level of the component.

    :return: The CSS object to allow the chaining
    """
    if top is not None:
      self.top = top
    elif bottom is not None:
      self.bottom = bottom
    if left is not None:
      self.left = left
    elif right is not None:
      self.right = right
    self.position = "sticky"
    self.z_index = z_index
    return self

  def shadow(self, color: Optional[str] = None, size: int = 5):
    """	Add a default dark shadow to the container

    Usage::

      component.style.css.shadow()

    Related Pages:

      https://www.w3schools.com/css/css3_shadows.asp

    :param color: The color.
    :param size: The size for the shadow.
    """
    if color is None:
      color = self.component.page.theme.colors[2]
    self.css({"box-shadow": "%(size)spx %(size)spx %(size)spx %(color)s" % {'color': color, 'size': size}})
    return self

  def shadow_text(self):
    """

    Related Pages:

      https://www.w3schools.com/css/css3_shadows.asp
    """
    self.text_shadow = "0 0 3px #FF0000, 0 0 5px #0000FF"
    return self

  def fixed_top(self, top: int = 5):
    """	Fix the component on the top of the page

    Usage::

      p.style.css.fixed_top()

    :param top: The margin with the page top border.
    """
    self.position = "fixed"
    self.display = "block"
    self.top = top
    return self

  def fixed_bottom(self, bottom: int = 10):
    """	Fix the component at the bottom of the page.

    Usage::

      p.style.css.fixed_bottom()

    :param bottom: The margin with the bottom of the page.
    """
    self.position = "fixed"
    self.display = "block"
    self.bottom = bottom
    return self

  def borders(self, color: Optional[str] = None, size: int = 1, style: str = "solid"):
    """	Shortcut function to set the border color for a defined HTML component

    Usage::

      a.style.css.borders()

    :param color: Optional. The border color. Default the grey from selected theme
    :param size: Optional. The border size. Default 1pz
    :param style: Optional. The border style. Default solid - a plain line
    """
    if color is None:
      color = self.component.page.theme.greys[-1]
    self.border = "%spx %s %s" % (size, style, color)
    return self

  def borders_light(self, color: Optional[str] = None, size: int = 1, style: str = "solid"):
    """	Shortcut function to set the light border color for a defined HTML component.

    Usage::

      a.style.css.borders_light()

    :param color: Optional. The border color. Default the grey from selected theme
    :param size: Optional. The border size. Default 1pz
    :param style: Optional. The border style. Default solid - a plain line
    """
    if color is None:
      color = self.component.page.theme.greys[3]
    return self.borders(color, size, style)

  def bold(self):
    """	Shortcut to put the text in bold
    """
    self.font_weight = "bold"
    return self

  def italic(self):
    """	Shortcut to put the text in italic
    """
    self.font_style = "italic"
    return self

  def underline(self):
    """	Shortcut to put the underline the text

    Related Pages:

      https://www.w3schools.com/cssref/pr_text_text-decoration.asp
    """
    self.text_decoration = "underline"
    return self

  def absolute(self, top: Optional[tuple] = None, left: Optional[tuple] = None, bottom: Optional[tuple] = None,
               right: Optional[tuple] = None, transform: bool = True, center: bool = False):
    """
	
    :param top:
    :param left:
    :param bottom:
    :param right:
    :param transform:
    :param center:
    """
    if top is not None:
      top = Arguments.size(top, unit="px")
      self.top = "%s%s" % (top[0], top[1])
    if bottom is not None:
      bottom = Arguments.size(bottom, unit="px")
      self.bottom = "%s%s" % (bottom[0], bottom[1])
    if left is not None:
      left = Arguments.size(left, unit="px")
      self.left = "%s%s" % (left[0], left[1])
    if right is not None:
      right = Arguments.size(right, unit="px")
      self.right = "%s%s" % (right[0], right[1])
    if center:
      self.margin = "0 auto"
      self.left = 0
      self.right = 0
      self.text_align = "center"
    elif transform:
      self.transform = "translate(-%s, -%s)" % (self.left, self.top)
    self.position = "absolute"
    return self

  def fixed(self, top: Optional[tuple] = None, left: Optional[tuple] = None, bottom: Optional[tuple] = None,
            right: Optional[tuple] = None, transform: bool = True):
    """
	
    :param top:
    :param left:
    :param bottom:
    :param right:
    :param transform:
    """
    if top is not None:
      top = Arguments.size(top, unit="px")
      self.top = "%s%s" % (top[0], top[1])
    if bottom is not None:
      bottom = Arguments.size(bottom, unit="px")
      self.bottom = "%s%s" % (bottom[0], bottom[1])
    if left is not None:
      left = Arguments.size(left, unit="px")
      self.left = "%s%s" % (left[0], left[1])
    if right is not None:
      right = Arguments.size(right, unit="px")
      self.right = "%s%s" % (right[0], right[1])
    if transform:
      if top is None and left is None:
        self.transform = "translate(-%s, -%s)" % (self.left, self.top)
    self.position = "fixed"
    return self

  def font_factor(self, factor: float):
    """
	
    :param factor:
    """
    self.font_size = self.component.page.body.style.globals.font.normal(factor)
    return self.component

  def margins(self, top: Any = None, right: Any = None, bottom: Any = None, left: Any = None):
    """	Set the margins of the component

    :param top: Optional. The size from the top of the component with its unit
    :param right: Optional. The size from the right of the component with its unit
    :param bottom: Optional. The size from the bottom of the component with its unit
    :param left: Optional. The size from the left of the component with its unit
    """
    width = self.width or '100%'
    overall_margin, overal_margin_unit = 0, None
    if right is not None:
      right = Arguments.size(right, 'px')
      self.margin_right = "%s%s" % (right[0], right[1])
      overall_margin += right[0]
      overal_margin_unit = right[1]
    if left is not None:
      left = Arguments.size(left, 'px')
      self.margin_left = "%s%s" % (left[0], left[1])
      overall_margin += left[0]
      overal_margin_unit = left[1]
    if top is not None:
      top = Arguments.size(top, 'px')
      self.margin_top = "%s%s" % (top[0], top[1])
    if bottom is not None:
      bottom = Arguments.size(bottom, 'px')
      self.margin_bottom = "%s%s" % (bottom[0], bottom[1])
    if overall_margin > 0:
      self.width = "calc(%s - %s%s)" % (width, overall_margin, overal_margin_unit)
    return self

  def inline_block(self, width: types.SIZE_TYPE = None):
    """ Shortcut for the display CSS attribute and the value inline-block.
    This will also remove the with property set to the component if in percentage.

    Related Pages:

      https://www.w3schools.com/css/css_inline-block.asp

    Usage:

      mode_switch = page.ui.fields.toggle({"off": 'No', "on": "Yes"}, is_on=True, label="Switch", htmlCode="switch")
      mode_switch.style.css.inline_block()

    :param width: Optional.
    """
    if self.width is not None and self.width.endswith("%"):
      self.width = None
    if width is not None:
      if isinstance(width, tuple) and width[0] is not None:
        width = "%s%s" % (width[0], width[1])
      self.width = width
    self.display = "inline-block"
    return self

  def hide(self):
    """ Shortcut for the display None CSS property.

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_display.asp

    Usage:

      warning = page.ui.icons.warning()
      warning.style.css.hide()

    """
    self.display = None
    return self

  def invisible(self):
    """ The visibility property specifies whether or not an element is visible.

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_visibility.asp
    """
    self.visibility = "hidden"

  def gradient_text(self, from_color: str, to_color: str, direction: str = "bottom"):
    """ you'll need two colors for the gradient to transition between.

    Related Pages:

      https://cssgradient.io/blog/css-gradient-text/

    :param from_color: The first color code
    :param to_color: The last color code
    :param direction: Optional. The gradient side
    """
    self.css({"background": "-webkit-linear-gradient(%s, %s, %s)" % (direction, from_color, to_color),
              "-webkit-text-fill-color": "transparent", "-webkit-background-clip": "text"})

  def inline(self):
    """ Shortcut to the inline-block CSS style.

    Usage::

        editor.style.css.inline()
    """
    self.display = "inline-block"
    return self

  def calc_width(self, width: Any = "100%", by: Any = None):
      """ Set the with of a component and it can take into account complex ones.

      .. Tips::

        Since this object will take the margins of the components it is important to
        set them all before.

      Usage::

        autocomplete = page.ui.fields.autocomplete(label="Auto complete")
        autocomplete.input.style.css.margin_h = 5
        autocomplete.input.style.css.calc_width(by=autocomplete.label)

      :param width: The width object
      :param by: A size object or a component on the same line in the page.
      """
      width = Arguments.size(width, unit="px", toStr=True)
      f = []
      if by is not None:
        if hasattr(by, "style"):
          by.style.css.inline()
          f.append(by.style.css.width)
          if by.style.css.margin_left is not None:
            f.append(by.style.css.margin_left)
          if by.style.css.margin_right is not None:
            f.append(by.style.css.margin_right)
          if by.style.css.margin is not None:
            margins = by.style.css.margin.split(" ")
            if len(margins) < 3:
              f.append(margins[-1])
              f.append(margins[-1])
            elif len(margins) == 4:
              f.append(margins[1])
              f.append(margins[3])
        else:
          f.append(Arguments.size(by, unit="px", toStr=True))
      if self.margin_left is not None:
        f.append(self.margin_left)
      if self.margin_right is not None:
        f.append(self.margin_right)
      if self.margin is not None:
        margins = self.margin.split(" ")
        if len(margins) < 3:
          f.append(margins[-1])
          f.append(margins[-1])
        elif len(margins) == 4:
          f.append(margins[1])
          f.append(margins[3])
      self.css({"width": "calc(%s - (%s))" % (width, " + ".join(f))})
      return self
