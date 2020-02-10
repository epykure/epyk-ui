"""

"""


def autoPrefixer(prop):
  pass


class CssMixin(object):
  """

  """
  @property
  def align_content(self): return self.htmlObj.css("align-content")

  @align_content.setter
  def align_content(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-content": val})

  @property
  def align_items(self): return self.htmlObj.css("align-items")

  @align_items.setter
  def align_items(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-items": val})

  @property
  def align_self(self): return self.htmlObj.css("align-self")

  @align_self.setter
  def align_self(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-self": val})

  @property
  def all(self): return self.htmlObj.css("all")

  @all.setter
  def all(self, val):
    val = val or 'None'
    self.htmlObj.css({"all": val})

  @property
  def animation(self): return self.htmlObj.css("animation")

  @animation.setter
  def animation(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation": val})

  @property
  def animation_delay(self): return self.htmlObj.css("animation-delay")

  @animation_delay.setter
  def animation_delay(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-delay": val})

  @property
  def animation_direction(self): return self.htmlObj.css("animation-direction")

  @animation_direction.setter
  def animation_direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-direction": val})

  @property
  def animation_duration(self): return self.htmlObj.css("animation-duration")

  @animation_duration.setter
  def animation_duration(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-duration": val})

  @property
  def animation_fill_mode(self): return self.htmlObj.css("animation-fill-mode")

  @animation_fill_mode.setter
  def animation_fill_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-fill-mode": val})

  @property
  def animation_iteration_count(self): return self.htmlObj.css("animation-iteration-count")

  @animation_iteration_count.setter
  def animation_iteration_count(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-iteration-count": val})

  @property
  def animation_name(self): return self.htmlObj.css("animation-name")

  @animation_name.setter
  def animation_name(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-name": val})

  @property
  def animation_play_state(self): return self.htmlObj.css("animation-play-state")

  @animation_play_state.setter
  def animation_play_state(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-play-state": val})

  @property
  def animation_timing_function(self): return self.htmlObj.css("animation-timing-function")

  @animation_timing_function.setter
  def animation_timing_function(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-timing-function": val})

  @property
  def backface_visibility(self): return self.htmlObj.css("backface-visibility")

  @backface_visibility.setter
  def backface_visibility(self, val):
    val = val or 'None'
    self.htmlObj.css({"backface-visibility": val})

  @property
  def background(self): return self.htmlObj.css("background")

  @background.setter
  def background(self, val):
    val = val or 'None'
    self.htmlObj.css({"background": val})

  @property
  def background_attachment(self): return self.htmlObj.css("background-attachment")

  @background_attachment.setter
  def background_attachment(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-attachment": val})

  @property
  def background_blend_mode(self): return self.htmlObj.css("background-blend-mode")

  @background_blend_mode.setter
  def background_blend_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-blend-mode": val})

  @property
  def background_clip(self): return self.htmlObj.css("background-clip")

  @background_clip.setter
  def background_clip(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-clip": val})

  @property
  def background_color(self): return self.htmlObj.css("background-color")

  @background_color.setter
  def background_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-color": val})

  @property
  def background_image(self): return self.htmlObj.css("background-image")

  @background_image.setter
  def background_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-image": val})

  @property
  def background_origin(self): return self.htmlObj.css("background-origin")

  @background_origin.setter
  def background_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-origin": val})

  @property
  def background_position(self): return self.htmlObj.css("background-position")

  @background_position.setter
  def background_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-position": val})

  @property
  def background_repeat(self): return self.htmlObj.css("background-repeat")

  @background_repeat.setter
  def background_repeat(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-repeat": val})

  @property
  def background_size(self): return self.htmlObj.css("background-size")

  @background_size.setter
  def background_size(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-size": val})

  @property
  def border(self): return self.htmlObj.css("border")

  @border.setter
  def border(self, val):
    val = val or 'None'
    self.htmlObj.css({"border": val})

  @property
  def border_bottom(self): return self.htmlObj.css("border-bottom")

  @border_bottom.setter
  def border_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom": val})

  @property
  def border_bottom_color(self): return self.htmlObj.css("border-bottom-color")

  @border_bottom_color.setter
  def border_bottom_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-color": val})

  @property
  def border_bottom_left_radius(self): return self.htmlObj.css("border-bottom-left-radius")

  @border_bottom_left_radius.setter
  def border_bottom_left_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-left-radius": val})

  @property
  def border_bottom_right_radius(self): return self.htmlObj.css("border-bottom-right-radius")

  @border_bottom_right_radius.setter
  def border_bottom_right_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-right-radius": val})

  @property
  def border_bottom_style(self): return self.htmlObj.css("border-bottom-style")

  @border_bottom_style.setter
  def border_bottom_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-style": val})

  @property
  def border_bottom_width(self): return self.htmlObj.css("border-bottom-width")

  @border_bottom_width.setter
  def border_bottom_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-width": val})

  @property
  def border_collapse(self): return self.htmlObj.css("border-collapse")

  @border_collapse.setter
  def border_collapse(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-collapse": val})

  @property
  def border_color(self): return self.htmlObj.css("border-color")

  @border_color.setter
  def border_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-color": val})

  @property
  def border_image(self): return self.htmlObj.css("border-image")

  @border_image.setter
  def border_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image": val})

  @property
  def border_image_outset(self): return self.htmlObj.css("border-image-outset")

  @border_image_outset.setter
  def border_image_outset(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-outset": val})

  @property
  def border_image_repeat(self): return self.htmlObj.css("border-image-repeat")

  @border_image_repeat.setter
  def border_image_repeat(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-repeat": val})

  @property
  def border_image_slice(self): return self.htmlObj.css("border-image-slice")

  @border_image_slice.setter
  def border_image_slice(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-slice": val})

  @property
  def border_image_source(self): return self.htmlObj.css("border-image-source")

  @border_image_source.setter
  def border_image_source(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-source": val})

  @property
  def border_image_width(self): return self.htmlObj.css("border-image-width")

  @border_image_width.setter
  def border_image_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-width": val})

  @property
  def border_left(self): return self.htmlObj.css("border-left")

  @border_left.setter
  def border_left(self, val):
    val = val or 'None'
    if isinstance(val, int):
      self.htmlObj.css({"border-left": "%spx" % val})
    else:
      self.htmlObj.css({"border-left": val})

  @property
  def border_left_color(self): return self.htmlObj.css("border-left-color")

  @border_left_color.setter
  def border_left_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-color": val})

  @property
  def border_left_style(self): return self.htmlObj.css("border-left-style")

  @border_left_style.setter
  def border_left_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-style": val})

  @property
  def border_left_width(self): return self.htmlObj.css("border-left-width")

  @border_left_width.setter
  def border_left_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-width": val})

  @property
  def border_radius(self): return self.htmlObj.css("border-radius")

  @border_radius.setter
  def border_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-radius": val})

  @property
  def border_right(self): return self.htmlObj.css("border-right")

  @border_right.setter
  def border_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right": val})

  @property
  def border_right_color(self): return self.htmlObj.css("border-right-color")

  @border_right_color.setter
  def border_right_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-color": val})

  @property
  def border_right_style(self): return self.htmlObj.css("border-right-style")

  @border_right_style.setter
  def border_right_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-style": val})

  @property
  def border_right_width(self): return self.htmlObj.css("border-right-width")

  @border_right_width.setter
  def border_right_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-width": val})

  @property
  def border_spacing(self): return self.htmlObj.css("border-spacing")

  @border_spacing.setter
  def border_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-spacing": val})

  @property
  def border_style(self): return self.htmlObj.css("border-style")

  @border_style.setter
  def border_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-style": val})

  @property
  def border_top(self): return self.htmlObj.css("border-top")

  @border_top.setter
  def border_top(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top": val})

  @property
  def border_top_color(self): return self.htmlObj.css("border-top-color")

  @border_top_color.setter
  def border_top_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-color": val})

  @property
  def border_top_left_radius(self): return self.htmlObj.css("border-top-left-radius")

  @border_top_left_radius.setter
  def border_top_left_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-left-radius": val})

  @property
  def border_top_right_radius(self): return self.htmlObj.css("border-top-right-radius")

  @border_top_right_radius.setter
  def border_top_right_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-right-radius": val})

  @property
  def border_top_style(self): return self.htmlObj.css("border-top-style")

  @border_top_style.setter
  def border_top_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-style": val})

  @property
  def border_top_width(self): return self.htmlObj.css("border-top-width")

  @border_top_width.setter
  def border_top_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-width": val})

  @property
  def border_width(self): return self.htmlObj.css("border-width")

  @border_width.setter
  def border_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-width": val})

  @property
  def bottom(self): return self.htmlObj.css("bottom")

  @bottom.setter
  def bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"bottom": val})

  @property
  def box_decoration_break(self): return self.htmlObj.css("box-decoration-break")

  @box_decoration_break.setter
  def box_decoration_break(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-decoration-break": val})

  @property
  def box_shadow(self): return self.htmlObj.css("box-shadow")

  @box_shadow.setter
  def box_shadow(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-shadow": val})

  @property
  def box_sizing(self): return self.htmlObj.css("box-sizing")

  @box_sizing.setter
  def box_sizing(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-sizing": val})

  @property
  def caption_side(self): return self.htmlObj.css("caption-side")

  @caption_side.setter
  def caption_side(self, val):
    val = val or 'None'
    self.htmlObj.css({"caption-side": val})

  @property
  def caret_color(self): return self.htmlObj.css("caret-color")

  @caret_color.setter
  def caret_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"caret-color": val})

  @property
  def clear(self): return self.htmlObj.css("clear")

  @clear.setter
  def clear(self, val):
    val = val or 'None'
    self.htmlObj.css({"clear": val})

  @property
  def clip(self): return self.htmlObj.css("clip")

  @clip.setter
  def clip(self, val):
    val = val or 'None'
    self.htmlObj.css({"clip": val})

  @property
  def clip_path(self): return self.htmlObj.css("clip-path")

  @clip_path.setter
  def clip_path(self, val):
    val = val or 'None'
    self.htmlObj.css({"clip-path": val})

  @property
  def color(self): return self.htmlObj.css("color")

  @color.setter
  def color(self, val):
    val = val or 'None'
    self.htmlObj.css({"color": val})

  @property
  def column_count(self): return self.htmlObj.css("column-count")

  @column_count.setter
  def column_count(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-count": val})

  @property
  def column_fill(self): return self.htmlObj.css("column-fill")

  @column_fill.setter
  def column_fill(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-fill": val})

  @property
  def column_gap(self): return self.htmlObj.css("column-gap")

  @column_gap.setter
  def column_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-gap": val})

  @property
  def column_rule(self): return self.htmlObj.css("column-rule")

  @column_rule.setter
  def column_rule(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule": val})

  @property
  def column_rule_color(self): return self.htmlObj.css("column-rule-color")

  @column_rule_color.setter
  def column_rule_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-color": val})

  @property
  def column_rule_style(self): return self.htmlObj.css("column-rule-style")

  @column_rule_style.setter
  def column_rule_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-style": val})

  @property
  def column_rule_width(self): return self.htmlObj.css("column-rule-width")

  @column_rule_width.setter
  def column_rule_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-width": val})

  @property
  def column_span(self): return self.htmlObj.css("column-span")

  @column_span.setter
  def column_span(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-span": val})

  @property
  def column_width(self): return self.htmlObj.css("column-width")

  @column_width.setter
  def column_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-width": val})

  @property
  def columns(self): return self.htmlObj.css("columns")

  @columns.setter
  def columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"columns": val})

  @property
  def content(self): return self.htmlObj.css("content")

  @content.setter
  def content(self, val):
    val = val or 'None'
    self.htmlObj.css({"content": val})

  @property
  def counter_increment(self): return self.htmlObj.css("counter-increment")

  @counter_increment.setter
  def counter_increment(self, val):
    val = val or 'None'
    self.htmlObj.css({"counter-increment": val})

  @property
  def counter_reset(self): return self.htmlObj.css("counter-reset")

  @counter_reset.setter
  def counter_reset(self, val):
    val = val or 'None'
    self.htmlObj.css({"counter-reset": val})

  @property
  def cursor(self): return self.htmlObj.css("cursor")

  @cursor.setter
  def cursor(self, val):
    val = val or 'None'
    self.htmlObj.css({"cursor": val})

  @property
  def direction(self): return self.htmlObj.css("direction")

  @direction.setter
  def direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"direction": val})

  @property
  def display(self): return self.htmlObj.css("display")

  @display.setter
  def display(self, val):
    val = val or 'None'
    self.htmlObj.css({"display": val})

  @property
  def empty_cells(self): return self.htmlObj.css("empty-cells")

  @empty_cells.setter
  def empty_cells(self, val):
    val = val or 'None'
    self.htmlObj.css({"empty-cells": val})

  @property
  def filter(self): return self.htmlObj.css("filter")

  @filter.setter
  def filter(self, val):
    val = val or 'None'
    self.htmlObj.css({"filter": val})

  @property
  def flex(self): return self.htmlObj.css("flex")

  @flex.setter
  def flex(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex": val})

  @property
  def flex_basis(self): return self.htmlObj.css("flex-basis")

  @flex_basis.setter
  def flex_basis(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-basis": val})

  @property
  def flex_direction(self): return self.htmlObj.css("flex-direction")

  @flex_direction.setter
  def flex_direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-direction": val})

  @property
  def flex_flow(self): return self.htmlObj.css("flex-flow")

  @flex_flow.setter
  def flex_flow(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-flow": val})

  @property
  def flex_grow(self): return self.htmlObj.css("flex-grow")

  @flex_grow.setter
  def flex_grow(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-grow": val})

  @property
  def flex_shrink(self): return self.htmlObj.css("flex-shrink")

  @flex_shrink.setter
  def flex_shrink(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-shrink": val})

  @property
  def flex_wrap(self): return self.htmlObj.css("flex-wrap")

  @flex_wrap.setter
  def flex_wrap(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-wrap": val})

  @property
  def float(self):
    """
    The float property specifies how an element should float

    Documentation
    https://www.w3schools.com/cssref/pr_class_float.asp
    """
    return self.htmlObj.css("float")

  @float.setter
  def float(self, val):
    val = val or 'none'
    defined_vals = set(['none', 'left', 'right', 'initial', 'inherit'])
    if val not in defined_vals:
      raise Exception("float value %s not recognized" % val)

    self.htmlObj.css({"float": val})

  @property
  def font(self): return self.htmlObj.css("font")

  @font.setter
  def font(self, val):
    val = val or 'None'
    self.htmlObj.css({"font": val})

  @property
  def font_family(self): return self.htmlObj.css("font-family")

  @font_family.setter
  def font_family(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-family": val})

  @property
  def font_kerning(self): return self.htmlObj.css("font-kerning")

  @font_kerning.setter
  def font_kerning(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-kerning": val})

  @property
  def font_size(self): return self.htmlObj.css("font-size")

  @font_size.setter
  def font_size(self, val):
    val = val or 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.htmlObj.css({"font-size": val})

  @property
  def font_size_adjust(self): return self.htmlObj.css("font-size-adjust")

  @font_size_adjust.setter
  def font_size_adjust(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-size-adjust": val})

  @property
  def font_stretch(self): return self.htmlObj.css("font-stretch")

  @font_stretch.setter
  def font_stretch(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-stretch": val})

  @property
  def font_style(self): return self.htmlObj.css("font-style")

  @font_style.setter
  def font_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-style": val})

  @property
  def font_variant(self): return self.htmlObj.css("font-variant")

  @font_variant.setter
  def font_variant(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-variant": val})

  @property
  def font_weight(self): return self.htmlObj.css("font-weight")

  @font_weight.setter
  def font_weight(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-weight": val})

  @property
  def grid(self): return self.htmlObj.css("grid")

  @grid.setter
  def grid(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid": val})

  @property
  def grid_area(self): return self.htmlObj.css("grid-area")

  @grid_area.setter
  def grid_area(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-area": val})

  @property
  def grid_auto_columns(self): return self.htmlObj.css("grid-auto-columns")

  @grid_auto_columns.setter
  def grid_auto_columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-columns": val})

  @property
  def grid_auto_flow(self): return self.htmlObj.css("grid-auto-flow")

  @grid_auto_flow.setter
  def grid_auto_flow(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-flow": val})

  @property
  def grid_auto_rows(self): return self.htmlObj.css("grid-auto-rows")

  @grid_auto_rows.setter
  def grid_auto_rows(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-rows": val})

  @property
  def grid_column(self): return self.htmlObj.css("grid-column")

  @grid_column.setter
  def grid_column(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column": val})

  @property
  def grid_column_end(self): return self.htmlObj.css("grid-column-end")

  @grid_column_end.setter
  def grid_column_end(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-end": val})

  @property
  def grid_column_gap(self): return self.htmlObj.css("grid-column-gap")

  @grid_column_gap.setter
  def grid_column_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-gap": val})

  @property
  def grid_column_start(self): return self.htmlObj.css("grid-column-start")

  @grid_column_start.setter
  def grid_column_start(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-start": val})

  @property
  def grid_gap(self): return self.htmlObj.css("grid-gap")

  @grid_gap.setter
  def grid_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-gap": val})

  @property
  def grid_row(self): return self.htmlObj.css("grid-row")

  @grid_row.setter
  def grid_row(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row": val})

  @property
  def grid_row_end(self): return self.htmlObj.css("grid-row-end")

  @grid_row_end.setter
  def grid_row_end(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-end": val})

  @property
  def grid_row_gap(self): return self.htmlObj.css("grid-row-gap")

  @grid_row_gap.setter
  def grid_row_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-gap": val})

  @property
  def grid_row_start(self): return self.htmlObj.css("grid-row-start")

  @grid_row_start.setter
  def grid_row_start(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-start": val})

  @property
  def grid_template(self): return self.htmlObj.css("grid-template")

  @grid_template.setter
  def grid_template(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template": val})

  @property
  def grid_template_areas(self): return self.htmlObj.css("grid-template-areas")

  @grid_template_areas.setter
  def grid_template_areas(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-areas": val})

  @property
  def grid_template_columns(self): return self.htmlObj.css("grid-template-columns")

  @grid_template_columns.setter
  def grid_template_columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-columns": val})

  @property
  def grid_template_rows(self): return self.htmlObj.css("grid-template-rows")

  @grid_template_rows.setter
  def grid_template_rows(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-rows": val})

  @property
  def hanging_punctuation(self): return self.htmlObj.css("hanging-punctuation")

  @hanging_punctuation.setter
  def hanging_punctuation(self, val):
    val = val or 'None'
    self.htmlObj.css({"hanging-punctuation": val})

  @property
  def height(self): return self.htmlObj.css("height")

  @height.setter
  def height(self, val):
    val = val or 'None'
    self.htmlObj.css({"height": val})

  @property
  def hyphens(self): return self.htmlObj.css("hyphens")

  @hyphens.setter
  def hyphens(self, val):
    val = val or 'None'
    self.htmlObj.css({"hyphens": val})

  @property
  def isolation(self): return self.htmlObj.css("isolation")

  @isolation.setter
  def isolation(self, val):
    val = val or 'None'
    self.htmlObj.css({"isolation": val})

  @property
  def justify_content(self): return self.htmlObj.css("justify-content")

  @justify_content.setter
  def justify_content(self, val):
    val = val or 'None'
    self.htmlObj.css({"justify-content": val})

  @property
  def left(self): return self.htmlObj.css("left")

  @left.setter
  def left(self, val):
    val = val or 'None'
    self.htmlObj.css({"left": val})

  @property
  def letter_spacing(self): return self.htmlObj.css("letter-spacing")

  @letter_spacing.setter
  def letter_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"letter-spacing": val})

  @property
  def line_height(self): return self.htmlObj.css("line-height")

  @line_height.setter
  def line_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"line-height": val})

  @property
  def list_style(self): return self.htmlObj.css("list-style")

  @list_style.setter
  def list_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style": val})

  @property
  def list_style_image(self): return self.htmlObj.css("list-style-image")

  @list_style_image.setter
  def list_style_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-image": val})

  @property
  def list_style_position(self): return self.htmlObj.css("list-style-position")

  @list_style_position.setter
  def list_style_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-position": val})

  @property
  def list_style_type(self): return self.htmlObj.css("list-style-type")

  @list_style_type.setter
  def list_style_type(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-type": val})

  @property
  def margin(self): return self.htmlObj.css("margin")

  @margin.setter
  def margin(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin": val})

  @property
  def margin_bottom(self): return self.htmlObj.css("margin-bottom")

  @margin_bottom.setter
  def margin_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin-bottom": val})

  @property
  def margin_left(self): return self.htmlObj.css("margin-left")

  @margin_left.setter
  def margin_left(self, val):
    """

    Documentation
    https://www.w3schools.com/cssref/pr_margin-left.asp

    :param val:
    :return:
    """
    if isinstance(val, int):
      val = "%spx" % val
    val = val or 'None'
    self.htmlObj.css({"margin-left": val})

  @property
  def margin_right(self): return self.htmlObj.css("margin-right")

  @margin_right.setter
  def margin_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin-right": val})

  @property
  def margin_top(self): return self.htmlObj.css("margin-top")

  @margin_top.setter
  def margin_top(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val or 'None'
    self.htmlObj.css({"margin-top": val})

  @property
  def max_height(self): return self.htmlObj.css("max-height")

  @max_height.setter
  def max_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"max-height": val})

  @property
  def max_width(self): return self.htmlObj.css("max-width")

  @max_width.setter
  def max_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"max-width": val})

  @property
  def min_height(self): return self.htmlObj.css("min-height")

  @min_height.setter
  def min_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"min-height": val})

  @property
  def min_width(self): return self.htmlObj.css("min-width")

  @min_width.setter
  def min_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"min-width": val})

  @property
  def mix_blend_mode(self): return self.htmlObj.css("mix-blend-mode")

  @mix_blend_mode.setter
  def mix_blend_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"mix-blend-mode": val})

  @property
  def object_fit(self): return self.htmlObj.css("object-fit")

  @object_fit.setter
  def object_fit(self, val):
    val = val or 'None'
    self.htmlObj.css({"object-fit": val})

  @property
  def object_position(self): return self.htmlObj.css("object-position")

  @object_position.setter
  def object_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"object-position": val})

  @property
  def opacity(self): return self.htmlObj.css("opacity")

  @opacity.setter
  def opacity(self, val):
    val = val or 'None'
    self.htmlObj.css({"opacity": val})

  @property
  def order(self): return self.htmlObj.css("order")

  @order.setter
  def order(self, val):
    val = val or 'None'
    self.htmlObj.css({"order": val})

  @property
  def outline(self): return self.htmlObj.css("outline")

  @outline.setter
  def outline(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline": val})

  @property
  def outline_color(self): return self.htmlObj.css("outline-color")

  @outline_color.setter
  def outline_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-color": val})

  @property
  def outline_offset(self): return self.htmlObj.css("outline-offset")

  @outline_offset.setter
  def outline_offset(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-offset": val})

  @property
  def outline_style(self): return self.htmlObj.css("outline-style")

  @outline_style.setter
  def outline_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-style": val})

  @property
  def outline_width(self): return self.htmlObj.css("outline-width")

  @outline_width.setter
  def outline_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-width": val})

  @property
  def overflow(self): return self.htmlObj.css("overflow")

  @overflow.setter
  def overflow(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow": val})

  @property
  def overflow_x(self): return self.htmlObj.css("overflow-x")

  @overflow_x.setter
  def overflow_x(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow-x": val})

  @property
  def overflow_y(self): return self.htmlObj.css("overflow-y")

  @overflow_y.setter
  def overflow_y(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow-y": val})

  @property
  def padding(self): return self.htmlObj.css("padding")

  @padding.setter
  def padding(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding": val})

  @property
  def padding_bottom(self): return self.htmlObj.css("padding-bottom")

  @padding_bottom.setter
  def padding_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-bottom": val})

  @property
  def padding_left(self): return self.htmlObj.css("padding-left")

  @padding_left.setter
  def padding_left(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-left": val})

  @property
  def padding_right(self): return self.htmlObj.css("padding-right")

  @padding_right.setter
  def padding_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-right": val})

  @property
  def padding_top(self): return self.htmlObj.css("padding-top")

  @padding_top.setter
  def padding_top(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-top": val})

  @property
  def page_break_after(self): return self.htmlObj.css("page-break-after")

  @page_break_after.setter
  def page_break_after(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-after": val})

  @property
  def page_break_before(self): return self.htmlObj.css("page-break-before")

  @page_break_before.setter
  def page_break_before(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-before": val})

  @property
  def page_break_inside(self): return self.htmlObj.css("page-break-inside")

  @page_break_inside.setter
  def page_break_inside(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-inside": val})

  @property
  def perspective(self): return self.htmlObj.css("perspective")

  @perspective.setter
  def perspective(self, val):
    val = val or 'None'
    self.htmlObj.css({"perspective": val})

  @property
  def perspective_origin(self): return self.htmlObj.css("perspective-origin")

  @perspective_origin.setter
  def perspective_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"perspective-origin": val})

  @property
  def pointer_events(self): return self.htmlObj.css("pointer-events")

  @pointer_events.setter
  def pointer_events(self, val):
    val = val or 'None'
    self.htmlObj.css({"pointer-events": val})

  @property
  def position(self): return self.htmlObj.css("position")

  @position.setter
  def position(self, val):
    val = val or 'None'
    self.htmlObj.css({"position": val})

  @property
  def quotes(self): return self.htmlObj.css("quotes")

  @quotes.setter
  def quotes(self, val):
    val = val or 'None'
    self.htmlObj.css({"quotes": val})

  @property
  def resize(self): return self.htmlObj.css("resize")

  @resize.setter
  def resize(self, val):
    val = val or 'None'
    self.htmlObj.css({"resize": val})

  @property
  def right(self): return self.htmlObj.css("right")

  @right.setter
  def right(self, val):
    val = val or 'None'
    self.htmlObj.css({"right": val})

  @property
  def scroll_behavior(self): return self.htmlObj.css("scroll-behavior")

  @scroll_behavior.setter
  def scroll_behavior(self, val):
    val = val or 'None'
    self.htmlObj.css({"scroll-behavior": val})

  @property
  def tab_size(self): return self.htmlObj.css("tab-size")

  @tab_size.setter
  def tab_size(self, val):
    val = val or 'None'
    self.htmlObj.css({"tab-size": val})

  @property
  def table_layout(self): return self.htmlObj.css("table-layout")

  @table_layout.setter
  def table_layout(self, val):
    val = val or 'None'
    self.htmlObj.css({"table-layout": val})

  @property
  def text_align(self): return self.htmlObj.css("text-align")

  @text_align.setter
  def text_align(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-align": val})

  @property
  def text_align_last(self): return self.htmlObj.css("text-align-last")

  @text_align_last.setter
  def text_align_last(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-align-last": val})

  @property
  def text_decoration(self): return self.htmlObj.css("text-decoration")

  @text_decoration.setter
  def text_decoration(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration": val})

  @property
  def text_decoration_color(self): return self.htmlObj.css("text-decoration-color")

  @text_decoration_color.setter
  def text_decoration_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-color": val})

  @property
  def text_decoration_line(self): return self.htmlObj.css("text-decoration-line")

  @text_decoration_line.setter
  def text_decoration_line(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-line": val})

  @property
  def text_decoration_style(self): return self.htmlObj.css("text-decoration-style")

  @text_decoration_style.setter
  def text_decoration_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-style": val})

  @property
  def text_indent(self): return self.htmlObj.css("text-indent")

  @text_indent.setter
  def text_indent(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-indent": val})

  @property
  def text_justify(self): return self.htmlObj.css("text-justify")

  @text_justify.setter
  def text_justify(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-justify": val})

  @property
  def text_overflow(self): return self.htmlObj.css("text-overflow")

  @text_overflow.setter
  def text_overflow(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-overflow": val})

  @property
  def text_shadow(self): return self.htmlObj.css("text-shadow")

  @text_shadow.setter
  def text_shadow(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-shadow": val})

  @property
  def text_transform(self): return self.htmlObj.css("text-transform")

  @text_transform.setter
  def text_transform(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-transform": val})

  @property
  def top(self): return self.htmlObj.css("top")

  @top.setter
  def top(self, val):
    val = val or 'None'
    self.htmlObj.css({"top": val})

  @property
  def transform(self): return self.htmlObj.css("transform")

  @transform.setter
  def transform(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform": val})

  @property
  def transform_origin(self): return self.htmlObj.css("transform-origin")

  @transform_origin.setter
  def transform_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform-origin": val})

  @property
  def transform_style(self): return self.htmlObj.css("transform-style")

  @transform_style.setter
  def transform_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform-style": val})

  @property
  def transition(self): return self.htmlObj.css("transition")

  @transition.setter
  def transition(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition": val})

  @property
  def transition_delay(self): return self.htmlObj.css("transition-delay")

  @transition_delay.setter
  def transition_delay(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-delay": val})

  @property
  def transition_duration(self): return self.htmlObj.css("transition-duration")

  @transition_duration.setter
  def transition_duration(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-duration": val})

  @property
  def transition_property(self): return self.htmlObj.css("transition-property")

  @transition_property.setter
  def transition_property(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-property": val})

  @property
  def transition_timing_function(self): return self.htmlObj.css("transition-timing-function")

  @transition_timing_function.setter
  def transition_timing_function(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-timing-function": val})

  @property
  def unicode_bidi(self): return self.htmlObj.css("unicode-bidi")

  @unicode_bidi.setter
  def unicode_bidi(self, val):
    val = val or 'None'
    self.htmlObj.css({"unicode-bidi": val})

  @property
  def user_select(self): return self.htmlObj.css("user-select")

  @user_select.setter
  def user_select(self, val):
    val = val or 'None'
    self.htmlObj.css({"user-select": val})

  @property
  def vertical_align(self): return self.htmlObj.css("vertical-align")

  @vertical_align.setter
  def vertical_align(self, val):
    val = val or 'None'
    self.htmlObj.css({"vertical-align": val})

  @property
  def visibility(self): return self.htmlObj.css("visibility")

  @visibility.setter
  def visibility(self, val):
    val = val or 'None'
    self.htmlObj.css({"visibility": val})

  @property
  def white_space(self): return self.htmlObj.css("white-space")

  @white_space.setter
  def white_space(self, val):
    val = val or 'None'
    self.htmlObj.css({"white-space": val})

  @property
  def width(self): return self.htmlObj.css("width")

  @width.setter
  def width(self, val):
    val = val or 'None'
    self.htmlObj.css({"width": val})

  @property
  def word_break(self): return self.htmlObj.css("word-break")

  @word_break.setter
  def word_break(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-break": val})

  @property
  def word_spacing(self): return self.htmlObj.css("word-spacing")

  @word_spacing.setter
  def word_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-spacing": val})

  @property
  def word_wrap(self): return self.htmlObj.css("word-wrap")

  @word_wrap.setter
  def word_wrap(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-wrap": val})

  @property
  def writing_mode(self): return self.htmlObj.css("writing-mode")

  @writing_mode.setter
  def writing_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"writing-mode": val})

  @property
  def z_index(self): return self.htmlObj.css("z-index")

  @z_index.setter
  def z_index(self, val):
    val = val or 'None'
    self.htmlObj.css({"z-index": val})
