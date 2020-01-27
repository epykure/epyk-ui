"""

"""


class CssMixin(object):
  """

  """
  @property
  def css_align_content(self): return self.htmlObj.css("align-content")

  @css_align_content.setter
  def css_align_content(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-content": val})

  @property
  def css_align_items(self): return self.htmlObj.css("align-items")

  @css_align_items.setter
  def css_align_items(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-items": val})

  @property
  def css_align_self(self): return self.htmlObj.css("align-self")

  @css_align_self.setter
  def css_align_self(self, val):
    val = val or 'None'
    self.htmlObj.css({"align-self": val})

  @property
  def css_all(self): return self.htmlObj.css("all")

  @css_all.setter
  def css_all(self, val):
    val = val or 'None'
    self.htmlObj.css({"all": val})

  @property
  def css_animation(self): return self.htmlObj.css("animation")

  @css_animation.setter
  def css_animation(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation": val})

  @property
  def css_animation_delay(self): return self.htmlObj.css("animation-delay")

  @css_animation_delay.setter
  def css_animation_delay(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-delay": val})

  @property
  def css_animation_direction(self): return self.htmlObj.css("animation-direction")

  @css_animation_direction.setter
  def css_animation_direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-direction": val})

  @property
  def css_animation_duration(self): return self.htmlObj.css("animation-duration")

  @css_animation_duration.setter
  def css_animation_duration(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-duration": val})

  @property
  def css_animation_fill_mode(self): return self.htmlObj.css("animation-fill-mode")

  @css_animation_fill_mode.setter
  def css_animation_fill_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-fill-mode": val})

  @property
  def css_animation_iteration_count(self): return self.htmlObj.css("animation-iteration-count")

  @css_animation_iteration_count.setter
  def css_animation_iteration_count(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-iteration-count": val})

  @property
  def css_animation_name(self): return self.htmlObj.css("animation-name")

  @css_animation_name.setter
  def css_animation_name(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-name": val})

  @property
  def css_animation_play_state(self): return self.htmlObj.css("animation-play-state")

  @css_animation_play_state.setter
  def css_animation_play_state(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-play-state": val})

  @property
  def css_animation_timing_function(self): return self.htmlObj.css("animation-timing-function")

  @css_animation_timing_function.setter
  def css_animation_timing_function(self, val):
    val = val or 'None'
    self.htmlObj.css({"animation-timing-function": val})

  @property
  def css_backface_visibility(self): return self.htmlObj.css("backface-visibility")

  @css_backface_visibility.setter
  def css_backface_visibility(self, val):
    val = val or 'None'
    self.htmlObj.css({"backface-visibility": val})

  @property
  def css_background(self): return self.htmlObj.css("background")

  @css_background.setter
  def css_background(self, val):
    val = val or 'None'
    self.htmlObj.css({"background": val})

  @property
  def css_background_attachment(self): return self.htmlObj.css("background-attachment")

  @css_background_attachment.setter
  def css_background_attachment(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-attachment": val})

  @property
  def css_background_blend_mode(self): return self.htmlObj.css("background-blend-mode")

  @css_background_blend_mode.setter
  def css_background_blend_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-blend-mode": val})

  @property
  def css_background_clip(self): return self.htmlObj.css("background-clip")

  @css_background_clip.setter
  def css_background_clip(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-clip": val})

  @property
  def css_background_color(self): return self.htmlObj.css("background-color")

  @css_background_color.setter
  def css_background_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-color": val})

  @property
  def css_background_image(self): return self.htmlObj.css("background-image")

  @css_background_image.setter
  def css_background_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-image": val})

  @property
  def css_background_origin(self): return self.htmlObj.css("background-origin")

  @css_background_origin.setter
  def css_background_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-origin": val})

  @property
  def css_background_position(self): return self.htmlObj.css("background-position")

  @css_background_position.setter
  def css_background_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-position": val})

  @property
  def css_background_repeat(self): return self.htmlObj.css("background-repeat")

  @css_background_repeat.setter
  def css_background_repeat(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-repeat": val})

  @property
  def css_background_size(self): return self.htmlObj.css("background-size")

  @css_background_size.setter
  def css_background_size(self, val):
    val = val or 'None'
    self.htmlObj.css({"background-size": val})

  @property
  def css_border(self): return self.htmlObj.css("border")

  @css_border.setter
  def css_border(self, val):
    val = val or 'None'
    self.htmlObj.css({"border": val})

  @property
  def css_border_bottom(self): return self.htmlObj.css("border-bottom")

  @css_border_bottom.setter
  def css_border_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom": val})

  @property
  def css_border_bottom_color(self): return self.htmlObj.css("border-bottom-color")

  @css_border_bottom_color.setter
  def css_border_bottom_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-color": val})

  @property
  def css_border_bottom_left_radius(self): return self.htmlObj.css("border-bottom-left-radius")

  @css_border_bottom_left_radius.setter
  def css_border_bottom_left_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-left-radius": val})

  @property
  def css_border_bottom_right_radius(self): return self.htmlObj.css("border-bottom-right-radius")

  @css_border_bottom_right_radius.setter
  def css_border_bottom_right_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-right-radius": val})

  @property
  def css_border_bottom_style(self): return self.htmlObj.css("border-bottom-style")

  @css_border_bottom_style.setter
  def css_border_bottom_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-style": val})

  @property
  def css_border_bottom_width(self): return self.htmlObj.css("border-bottom-width")

  @css_border_bottom_width.setter
  def css_border_bottom_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-bottom-width": val})

  @property
  def css_border_collapse(self): return self.htmlObj.css("border-collapse")

  @css_border_collapse.setter
  def css_border_collapse(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-collapse": val})

  @property
  def css_border_color(self): return self.htmlObj.css("border-color")

  @css_border_color.setter
  def css_border_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-color": val})

  @property
  def css_border_image(self): return self.htmlObj.css("border-image")

  @css_border_image.setter
  def css_border_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image": val})

  @property
  def css_border_image_outset(self): return self.htmlObj.css("border-image-outset")

  @css_border_image_outset.setter
  def css_border_image_outset(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-outset": val})

  @property
  def css_border_image_repeat(self): return self.htmlObj.css("border-image-repeat")

  @css_border_image_repeat.setter
  def css_border_image_repeat(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-repeat": val})

  @property
  def css_border_image_slice(self): return self.htmlObj.css("border-image-slice")

  @css_border_image_slice.setter
  def css_border_image_slice(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-slice": val})

  @property
  def css_border_image_source(self): return self.htmlObj.css("border-image-source")

  @css_border_image_source.setter
  def css_border_image_source(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-source": val})

  @property
  def css_border_image_width(self): return self.htmlObj.css("border-image-width")

  @css_border_image_width.setter
  def css_border_image_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-image-width": val})

  @property
  def css_border_left(self): return self.htmlObj.css("border-left")

  @css_border_left.setter
  def css_border_left(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left": val})

  @property
  def css_border_left_color(self): return self.htmlObj.css("border-left-color")

  @css_border_left_color.setter
  def css_border_left_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-color": val})

  @property
  def css_border_left_style(self): return self.htmlObj.css("border-left-style")

  @css_border_left_style.setter
  def css_border_left_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-style": val})

  @property
  def css_border_left_width(self): return self.htmlObj.css("border-left-width")

  @css_border_left_width.setter
  def css_border_left_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-left-width": val})

  @property
  def css_border_radius(self): return self.htmlObj.css("border-radius")

  @css_border_radius.setter
  def css_border_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-radius": val})

  @property
  def css_border_right(self): return self.htmlObj.css("border-right")

  @css_border_right.setter
  def css_border_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right": val})

  @property
  def css_border_right_color(self): return self.htmlObj.css("border-right-color")

  @css_border_right_color.setter
  def css_border_right_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-color": val})

  @property
  def css_border_right_style(self): return self.htmlObj.css("border-right-style")

  @css_border_right_style.setter
  def css_border_right_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-style": val})

  @property
  def css_border_right_width(self): return self.htmlObj.css("border-right-width")

  @css_border_right_width.setter
  def css_border_right_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-right-width": val})

  @property
  def css_border_spacing(self): return self.htmlObj.css("border-spacing")

  @css_border_spacing.setter
  def css_border_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-spacing": val})

  @property
  def css_border_style(self): return self.htmlObj.css("border-style")

  @css_border_style.setter
  def css_border_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-style": val})

  @property
  def css_border_top(self): return self.htmlObj.css("border-top")

  @css_border_top.setter
  def css_border_top(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top": val})

  @property
  def css_border_top_color(self): return self.htmlObj.css("border-top-color")

  @css_border_top_color.setter
  def css_border_top_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-color": val})

  @property
  def css_border_top_left_radius(self): return self.htmlObj.css("border-top-left-radius")

  @css_border_top_left_radius.setter
  def css_border_top_left_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-left-radius": val})

  @property
  def css_border_top_right_radius(self): return self.htmlObj.css("border-top-right-radius")

  @css_border_top_right_radius.setter
  def css_border_top_right_radius(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-right-radius": val})

  @property
  def css_border_top_style(self): return self.htmlObj.css("border-top-style")

  @css_border_top_style.setter
  def css_border_top_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-style": val})

  @property
  def css_border_top_width(self): return self.htmlObj.css("border-top-width")

  @css_border_top_width.setter
  def css_border_top_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-top-width": val})

  @property
  def css_border_width(self): return self.htmlObj.css("border-width")

  @css_border_width.setter
  def css_border_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"border-width": val})

  @property
  def css_bottom(self): return self.htmlObj.css("bottom")

  @css_bottom.setter
  def css_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"bottom": val})

  @property
  def css_box_decoration_break(self): return self.htmlObj.css("box-decoration-break")

  @css_box_decoration_break.setter
  def css_box_decoration_break(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-decoration-break": val})

  @property
  def css_box_shadow(self): return self.htmlObj.css("box-shadow")

  @css_box_shadow.setter
  def css_box_shadow(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-shadow": val})

  @property
  def css_box_sizing(self): return self.htmlObj.css("box-sizing")

  @css_box_sizing.setter
  def css_box_sizing(self, val):
    val = val or 'None'
    self.htmlObj.css({"box-sizing": val})

  @property
  def css_caption_side(self): return self.htmlObj.css("caption-side")

  @css_caption_side.setter
  def css_caption_side(self, val):
    val = val or 'None'
    self.htmlObj.css({"caption-side": val})

  @property
  def css_caret_color(self): return self.htmlObj.css("caret-color")

  @css_caret_color.setter
  def css_caret_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"caret-color": val})

  @property
  def css_clear(self): return self.htmlObj.css("clear")

  @css_clear.setter
  def css_clear(self, val):
    val = val or 'None'
    self.htmlObj.css({"clear": val})

  @property
  def css_clip(self): return self.htmlObj.css("clip")

  @css_clip.setter
  def css_clip(self, val):
    val = val or 'None'
    self.htmlObj.css({"clip": val})

  @property
  def css_clip_path(self): return self.htmlObj.css("clip-path")

  @css_clip_path.setter
  def css_clip_path(self, val):
    val = val or 'None'
    self.htmlObj.css({"clip-path": val})

  @property
  def css_color(self): return self.htmlObj.css("color")

  @css_color.setter
  def css_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"color": val})

  @property
  def css_column_count(self): return self.htmlObj.css("column-count")

  @css_column_count.setter
  def css_column_count(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-count": val})

  @property
  def css_column_fill(self): return self.htmlObj.css("column-fill")

  @css_column_fill.setter
  def css_column_fill(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-fill": val})

  @property
  def css_column_gap(self): return self.htmlObj.css("column-gap")

  @css_column_gap.setter
  def css_column_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-gap": val})

  @property
  def css_column_rule(self): return self.htmlObj.css("column-rule")

  @css_column_rule.setter
  def css_column_rule(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule": val})

  @property
  def css_column_rule_color(self): return self.htmlObj.css("column-rule-color")

  @css_column_rule_color.setter
  def css_column_rule_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-color": val})

  @property
  def css_column_rule_style(self): return self.htmlObj.css("column-rule-style")

  @css_column_rule_style.setter
  def css_column_rule_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-style": val})

  @property
  def css_column_rule_width(self): return self.htmlObj.css("column-rule-width")

  @css_column_rule_width.setter
  def css_column_rule_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-rule-width": val})

  @property
  def css_column_span(self): return self.htmlObj.css("column-span")

  @css_column_span.setter
  def css_column_span(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-span": val})

  @property
  def css_column_width(self): return self.htmlObj.css("column-width")

  @css_column_width.setter
  def css_column_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"column-width": val})

  @property
  def css_columns(self): return self.htmlObj.css("columns")

  @css_columns.setter
  def css_columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"columns": val})

  @property
  def css_content(self): return self.htmlObj.css("content")

  @css_content.setter
  def css_content(self, val):
    val = val or 'None'
    self.htmlObj.css({"content": val})

  @property
  def css_counter_increment(self): return self.htmlObj.css("counter-increment")

  @css_counter_increment.setter
  def css_counter_increment(self, val):
    val = val or 'None'
    self.htmlObj.css({"counter-increment": val})

  @property
  def css_counter_reset(self): return self.htmlObj.css("counter-reset")

  @css_counter_reset.setter
  def css_counter_reset(self, val):
    val = val or 'None'
    self.htmlObj.css({"counter-reset": val})

  @property
  def css_cursor(self): return self.htmlObj.css("cursor")

  @css_cursor.setter
  def css_cursor(self, val):
    val = val or 'None'
    self.htmlObj.css({"cursor": val})

  @property
  def css_direction(self): return self.htmlObj.css("direction")

  @css_direction.setter
  def css_direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"direction": val})

  @property
  def css_display(self): return self.htmlObj.css("display")

  @css_display.setter
  def css_display(self, val):
    val = val or 'None'
    self.htmlObj.css({"display": val})

  @property
  def css_empty_cells(self): return self.htmlObj.css("empty-cells")

  @css_empty_cells.setter
  def css_empty_cells(self, val):
    val = val or 'None'
    self.htmlObj.css({"empty-cells": val})

  @property
  def css_filter(self): return self.htmlObj.css("filter")

  @css_filter.setter
  def css_filter(self, val):
    val = val or 'None'
    self.htmlObj.css({"filter": val})

  @property
  def css_flex(self): return self.htmlObj.css("flex")

  @css_flex.setter
  def css_flex(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex": val})

  @property
  def css_flex_basis(self): return self.htmlObj.css("flex-basis")

  @css_flex_basis.setter
  def css_flex_basis(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-basis": val})

  @property
  def css_flex_direction(self): return self.htmlObj.css("flex-direction")

  @css_flex_direction.setter
  def css_flex_direction(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-direction": val})

  @property
  def css_flex_flow(self): return self.htmlObj.css("flex-flow")

  @css_flex_flow.setter
  def css_flex_flow(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-flow": val})

  @property
  def css_flex_grow(self): return self.htmlObj.css("flex-grow")

  @css_flex_grow.setter
  def css_flex_grow(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-grow": val})

  @property
  def css_flex_shrink(self): return self.htmlObj.css("flex-shrink")

  @css_flex_shrink.setter
  def css_flex_shrink(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-shrink": val})

  @property
  def css_flex_wrap(self): return self.htmlObj.css("flex-wrap")

  @css_flex_wrap.setter
  def css_flex_wrap(self, val):
    val = val or 'None'
    self.htmlObj.css({"flex-wrap": val})

  @property
  def css_float(self): return self.htmlObj.css("float")

  @css_float.setter
  def css_float(self, val):
    val = val or 'None'
    self.htmlObj.css({"float": val})

  @property
  def css_font(self): return self.htmlObj.css("font")

  @css_font.setter
  def css_font(self, val):
    val = val or 'None'
    self.htmlObj.css({"font": val})

  @property
  def css_font_family(self): return self.htmlObj.css("font-family")

  @css_font_family.setter
  def css_font_family(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-family": val})

  @property
  def css_font_kerning(self): return self.htmlObj.css("font-kerning")

  @css_font_kerning.setter
  def css_font_kerning(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-kerning": val})

  @property
  def css_font_size(self): return self.htmlObj.css("font-size")

  @css_font_size.setter
  def css_font_size(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-size": val})

  @property
  def css_font_size_adjust(self): return self.htmlObj.css("font-size-adjust")

  @css_font_size_adjust.setter
  def css_font_size_adjust(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-size-adjust": val})

  @property
  def css_font_stretch(self): return self.htmlObj.css("font-stretch")

  @css_font_stretch.setter
  def css_font_stretch(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-stretch": val})

  @property
  def css_font_style(self): return self.htmlObj.css("font-style")

  @css_font_style.setter
  def css_font_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-style": val})

  @property
  def css_font_variant(self): return self.htmlObj.css("font-variant")

  @css_font_variant.setter
  def css_font_variant(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-variant": val})

  @property
  def css_font_weight(self): return self.htmlObj.css("font-weight")

  @css_font_weight.setter
  def css_font_weight(self, val):
    val = val or 'None'
    self.htmlObj.css({"font-weight": val})

  @property
  def css_grid(self): return self.htmlObj.css("grid")

  @css_grid.setter
  def css_grid(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid": val})

  @property
  def css_grid_area(self): return self.htmlObj.css("grid-area")

  @css_grid_area.setter
  def css_grid_area(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-area": val})

  @property
  def css_grid_auto_columns(self): return self.htmlObj.css("grid-auto-columns")

  @css_grid_auto_columns.setter
  def css_grid_auto_columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-columns": val})

  @property
  def css_grid_auto_flow(self): return self.htmlObj.css("grid-auto-flow")

  @css_grid_auto_flow.setter
  def css_grid_auto_flow(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-flow": val})

  @property
  def css_grid_auto_rows(self): return self.htmlObj.css("grid-auto-rows")

  @css_grid_auto_rows.setter
  def css_grid_auto_rows(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-auto-rows": val})

  @property
  def css_grid_column(self): return self.htmlObj.css("grid-column")

  @css_grid_column.setter
  def css_grid_column(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column": val})

  @property
  def css_grid_column_end(self): return self.htmlObj.css("grid-column-end")

  @css_grid_column_end.setter
  def css_grid_column_end(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-end": val})

  @property
  def css_grid_column_gap(self): return self.htmlObj.css("grid-column-gap")

  @css_grid_column_gap.setter
  def css_grid_column_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-gap": val})

  @property
  def css_grid_column_start(self): return self.htmlObj.css("grid-column-start")

  @css_grid_column_start.setter
  def css_grid_column_start(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-column-start": val})

  @property
  def css_grid_gap(self): return self.htmlObj.css("grid-gap")

  @css_grid_gap.setter
  def css_grid_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-gap": val})

  @property
  def css_grid_row(self): return self.htmlObj.css("grid-row")

  @css_grid_row.setter
  def css_grid_row(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row": val})

  @property
  def css_grid_row_end(self): return self.htmlObj.css("grid-row-end")

  @css_grid_row_end.setter
  def css_grid_row_end(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-end": val})

  @property
  def css_grid_row_gap(self): return self.htmlObj.css("grid-row-gap")

  @css_grid_row_gap.setter
  def css_grid_row_gap(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-gap": val})

  @property
  def css_grid_row_start(self): return self.htmlObj.css("grid-row-start")

  @css_grid_row_start.setter
  def css_grid_row_start(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-row-start": val})

  @property
  def css_grid_template(self): return self.htmlObj.css("grid-template")

  @css_grid_template.setter
  def css_grid_template(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template": val})

  @property
  def css_grid_template_areas(self): return self.htmlObj.css("grid-template-areas")

  @css_grid_template_areas.setter
  def css_grid_template_areas(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-areas": val})

  @property
  def css_grid_template_columns(self): return self.htmlObj.css("grid-template-columns")

  @css_grid_template_columns.setter
  def css_grid_template_columns(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-columns": val})

  @property
  def css_grid_template_rows(self): return self.htmlObj.css("grid-template-rows")

  @css_grid_template_rows.setter
  def css_grid_template_rows(self, val):
    val = val or 'None'
    self.htmlObj.css({"grid-template-rows": val})

  @property
  def css_hanging_punctuation(self): return self.htmlObj.css("hanging-punctuation")

  @css_hanging_punctuation.setter
  def css_hanging_punctuation(self, val):
    val = val or 'None'
    self.htmlObj.css({"hanging-punctuation": val})

  @property
  def css_height(self): return self.htmlObj.css("height")

  @css_height.setter
  def css_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"height": val})

  @property
  def css_hyphens(self): return self.htmlObj.css("hyphens")

  @css_hyphens.setter
  def css_hyphens(self, val):
    val = val or 'None'
    self.htmlObj.css({"hyphens": val})

  @property
  def css_isolation(self): return self.htmlObj.css("isolation")

  @css_isolation.setter
  def css_isolation(self, val):
    val = val or 'None'
    self.htmlObj.css({"isolation": val})

  @property
  def css_justify_content(self): return self.htmlObj.css("justify-content")

  @css_justify_content.setter
  def css_justify_content(self, val):
    val = val or 'None'
    self.htmlObj.css({"justify-content": val})

  @property
  def css_left(self): return self.htmlObj.css("left")

  @css_left.setter
  def css_left(self, val):
    val = val or 'None'
    self.htmlObj.css({"left": val})

  @property
  def css_letter_spacing(self): return self.htmlObj.css("letter-spacing")

  @css_letter_spacing.setter
  def css_letter_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"letter-spacing": val})

  @property
  def css_line_height(self): return self.htmlObj.css("line-height")

  @css_line_height.setter
  def css_line_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"line-height": val})

  @property
  def css_list_style(self): return self.htmlObj.css("list-style")

  @css_list_style.setter
  def css_list_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style": val})

  @property
  def css_list_style_image(self): return self.htmlObj.css("list-style-image")

  @css_list_style_image.setter
  def css_list_style_image(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-image": val})

  @property
  def css_list_style_position(self): return self.htmlObj.css("list-style-position")

  @css_list_style_position.setter
  def css_list_style_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-position": val})

  @property
  def css_list_style_type(self): return self.htmlObj.css("list-style-type")

  @css_list_style_type.setter
  def css_list_style_type(self, val):
    val = val or 'None'
    self.htmlObj.css({"list-style-type": val})

  @property
  def css_margin(self): return self.htmlObj.css("margin")

  @css_margin.setter
  def css_margin(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin": val})

  @property
  def css_margin_bottom(self): return self.htmlObj.css("margin-bottom")

  @css_margin_bottom.setter
  def css_margin_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin-bottom": val})

  @property
  def css_margin_left(self): return self.htmlObj.css("margin-left")

  @css_margin_left.setter
  def css_margin_left(self, val):
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
  def css_margin_right(self): return self.htmlObj.css("margin-right")

  @css_margin_right.setter
  def css_margin_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"margin-right": val})

  @property
  def css_margin_top(self): return self.htmlObj.css("margin-top")

  @css_margin_top.setter
  def css_margin_top(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    val = val or 'None'
    self.htmlObj.css({"margin-top": val})

  @property
  def css_max_height(self): return self.htmlObj.css("max-height")

  @css_max_height.setter
  def css_max_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"max-height": val})

  @property
  def css_max_width(self): return self.htmlObj.css("max-width")

  @css_max_width.setter
  def css_max_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"max-width": val})

  @property
  def css_min_height(self): return self.htmlObj.css("min-height")

  @css_min_height.setter
  def css_min_height(self, val):
    val = val or 'None'
    self.htmlObj.css({"min-height": val})

  @property
  def css_min_width(self): return self.htmlObj.css("min-width")

  @css_min_width.setter
  def css_min_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"min-width": val})

  @property
  def css_mix_blend_mode(self): return self.htmlObj.css("mix-blend-mode")

  @css_mix_blend_mode.setter
  def css_mix_blend_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"mix-blend-mode": val})

  @property
  def css_object_fit(self): return self.htmlObj.css("object-fit")

  @css_object_fit.setter
  def css_object_fit(self, val):
    val = val or 'None'
    self.htmlObj.css({"object-fit": val})

  @property
  def css_object_position(self): return self.htmlObj.css("object-position")

  @css_object_position.setter
  def css_object_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"object-position": val})

  @property
  def css_opacity(self): return self.htmlObj.css("opacity")

  @css_opacity.setter
  def css_opacity(self, val):
    val = val or 'None'
    self.htmlObj.css({"opacity": val})

  @property
  def css_order(self): return self.htmlObj.css("order")

  @css_order.setter
  def css_order(self, val):
    val = val or 'None'
    self.htmlObj.css({"order": val})

  @property
  def css_outline(self): return self.htmlObj.css("outline")

  @css_outline.setter
  def css_outline(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline": val})

  @property
  def css_outline_color(self): return self.htmlObj.css("outline-color")

  @css_outline_color.setter
  def css_outline_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-color": val})

  @property
  def css_outline_offset(self): return self.htmlObj.css("outline-offset")

  @css_outline_offset.setter
  def css_outline_offset(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-offset": val})

  @property
  def css_outline_style(self): return self.htmlObj.css("outline-style")

  @css_outline_style.setter
  def css_outline_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-style": val})

  @property
  def css_outline_width(self): return self.htmlObj.css("outline-width")

  @css_outline_width.setter
  def css_outline_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"outline-width": val})

  @property
  def css_overflow(self): return self.htmlObj.css("overflow")

  @css_overflow.setter
  def css_overflow(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow": val})

  @property
  def css_overflow_x(self): return self.htmlObj.css("overflow-x")

  @css_overflow_x.setter
  def css_overflow_x(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow-x": val})

  @property
  def css_overflow_y(self): return self.htmlObj.css("overflow-y")

  @css_overflow_y.setter
  def css_overflow_y(self, val):
    val = val or 'None'
    self.htmlObj.css({"overflow-y": val})

  @property
  def css_padding(self): return self.htmlObj.css("padding")

  @css_padding.setter
  def css_padding(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding": val})

  @property
  def css_padding_bottom(self): return self.htmlObj.css("padding-bottom")

  @css_padding_bottom.setter
  def css_padding_bottom(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-bottom": val})

  @property
  def css_padding_left(self): return self.htmlObj.css("padding-left")

  @css_padding_left.setter
  def css_padding_left(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-left": val})

  @property
  def css_padding_right(self): return self.htmlObj.css("padding-right")

  @css_padding_right.setter
  def css_padding_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-right": val})

  @property
  def css_padding_top(self): return self.htmlObj.css("padding-top")

  @css_padding_top.setter
  def css_padding_top(self, val):
    val = val or 'None'
    self.htmlObj.css({"padding-top": val})

  @property
  def css_page_break_after(self): return self.htmlObj.css("page-break-after")

  @css_page_break_after.setter
  def css_page_break_after(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-after": val})

  @property
  def css_page_break_before(self): return self.htmlObj.css("page-break-before")

  @css_page_break_before.setter
  def css_page_break_before(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-before": val})

  @property
  def css_page_break_inside(self): return self.htmlObj.css("page-break-inside")

  @css_page_break_inside.setter
  def css_page_break_inside(self, val):
    val = val or 'None'
    self.htmlObj.css({"page-break-inside": val})

  @property
  def css_perspective(self): return self.htmlObj.css("perspective")

  @css_perspective.setter
  def css_perspective(self, val):
    val = val or 'None'
    self.htmlObj.css({"perspective": val})

  @property
  def css_perspective_origin(self): return self.htmlObj.css("perspective-origin")

  @css_perspective_origin.setter
  def css_perspective_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"perspective-origin": val})

  @property
  def css_pointer_events(self): return self.htmlObj.css("pointer-events")

  @css_pointer_events.setter
  def css_pointer_events(self, val):
    val = val or 'None'
    self.htmlObj.css({"pointer-events": val})

  @property
  def css_position(self): return self.htmlObj.css("position")

  @css_position.setter
  def css_position(self, val):
    val = val or 'None'
    self.htmlObj.css({"position": val})

  @property
  def css_quotes(self): return self.htmlObj.css("quotes")

  @css_quotes.setter
  def css_quotes(self, val):
    val = val or 'None'
    self.htmlObj.css({"quotes": val})

  @property
  def css_resize(self): return self.htmlObj.css("resize")

  @css_resize.setter
  def css_resize(self, val):
    val = val or 'None'
    self.htmlObj.css({"resize": val})

  @property
  def css_right(self): return self.htmlObj.css("right")

  @css_right.setter
  def css_right(self, val):
    val = val or 'None'
    self.htmlObj.css({"right": val})

  @property
  def css_scroll_behavior(self): return self.htmlObj.css("scroll-behavior")

  @css_scroll_behavior.setter
  def css_scroll_behavior(self, val):
    val = val or 'None'
    self.htmlObj.css({"scroll-behavior": val})

  @property
  def css_tab_size(self): return self.htmlObj.css("tab-size")

  @css_tab_size.setter
  def css_tab_size(self, val):
    val = val or 'None'
    self.htmlObj.css({"tab-size": val})

  @property
  def css_table_layout(self): return self.htmlObj.css("table-layout")

  @css_table_layout.setter
  def css_table_layout(self, val):
    val = val or 'None'
    self.htmlObj.css({"table-layout": val})

  @property
  def css_text_align(self): return self.htmlObj.css("text-align")

  @css_text_align.setter
  def css_text_align(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-align": val})

  @property
  def css_text_align_last(self): return self.htmlObj.css("text-align-last")

  @css_text_align_last.setter
  def css_text_align_last(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-align-last": val})

  @property
  def css_text_decoration(self): return self.htmlObj.css("text-decoration")

  @css_text_decoration.setter
  def css_text_decoration(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration": val})

  @property
  def css_text_decoration_color(self): return self.htmlObj.css("text-decoration-color")

  @css_text_decoration_color.setter
  def css_text_decoration_color(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-color": val})

  @property
  def css_text_decoration_line(self): return self.htmlObj.css("text-decoration-line")

  @css_text_decoration_line.setter
  def css_text_decoration_line(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-line": val})

  @property
  def css_text_decoration_style(self): return self.htmlObj.css("text-decoration-style")

  @css_text_decoration_style.setter
  def css_text_decoration_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-decoration-style": val})

  @property
  def css_text_indent(self): return self.htmlObj.css("text-indent")

  @css_text_indent.setter
  def css_text_indent(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-indent": val})

  @property
  def css_text_justify(self): return self.htmlObj.css("text-justify")

  @css_text_justify.setter
  def css_text_justify(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-justify": val})

  @property
  def css_text_overflow(self): return self.htmlObj.css("text-overflow")

  @css_text_overflow.setter
  def css_text_overflow(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-overflow": val})

  @property
  def css_text_shadow(self): return self.htmlObj.css("text-shadow")

  @css_text_shadow.setter
  def css_text_shadow(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-shadow": val})

  @property
  def css_text_transform(self): return self.htmlObj.css("text-transform")

  @css_text_transform.setter
  def css_text_transform(self, val):
    val = val or 'None'
    self.htmlObj.css({"text-transform": val})

  @property
  def css_top(self): return self.htmlObj.css("top")

  @css_top.setter
  def css_top(self, val):
    val = val or 'None'
    self.htmlObj.css({"top": val})

  @property
  def css_transform(self): return self.htmlObj.css("transform")

  @css_transform.setter
  def css_transform(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform": val})

  @property
  def css_transform_origin(self): return self.htmlObj.css("transform-origin")

  @css_transform_origin.setter
  def css_transform_origin(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform-origin": val})

  @property
  def css_transform_style(self): return self.htmlObj.css("transform-style")

  @css_transform_style.setter
  def css_transform_style(self, val):
    val = val or 'None'
    self.htmlObj.css({"transform-style": val})

  @property
  def css_transition(self): return self.htmlObj.css("transition")

  @css_transition.setter
  def css_transition(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition": val})

  @property
  def css_transition_delay(self): return self.htmlObj.css("transition-delay")

  @css_transition_delay.setter
  def css_transition_delay(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-delay": val})

  @property
  def css_transition_duration(self): return self.htmlObj.css("transition-duration")

  @css_transition_duration.setter
  def css_transition_duration(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-duration": val})

  @property
  def css_transition_property(self): return self.htmlObj.css("transition-property")

  @css_transition_property.setter
  def css_transition_property(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-property": val})

  @property
  def css_transition_timing_function(self): return self.htmlObj.css("transition-timing-function")

  @css_transition_timing_function.setter
  def css_transition_timing_function(self, val):
    val = val or 'None'
    self.htmlObj.css({"transition-timing-function": val})

  @property
  def css_unicode_bidi(self): return self.htmlObj.css("unicode-bidi")

  @css_unicode_bidi.setter
  def css_unicode_bidi(self, val):
    val = val or 'None'
    self.htmlObj.css({"unicode-bidi": val})

  @property
  def css_user_select(self): return self.htmlObj.css("user-select")

  @css_user_select.setter
  def css_user_select(self, val):
    val = val or 'None'
    self.htmlObj.css({"user-select": val})

  @property
  def css_vertical_align(self): return self.htmlObj.css("vertical-align")

  @css_vertical_align.setter
  def css_vertical_align(self, val):
    val = val or 'None'
    self.htmlObj.css({"vertical-align": val})

  @property
  def css_visibility(self): return self.htmlObj.css("visibility")

  @css_visibility.setter
  def css_visibility(self, val):
    val = val or 'None'
    self.htmlObj.css({"visibility": val})

  @property
  def css_white_space(self): return self.htmlObj.css("white-space")

  @css_white_space.setter
  def css_white_space(self, val):
    val = val or 'None'
    self.htmlObj.css({"white-space": val})

  @property
  def css_width(self): return self.htmlObj.css("width")

  @css_width.setter
  def css_width(self, val):
    val = val or 'None'
    self.htmlObj.css({"width": val})

  @property
  def css_word_break(self): return self.htmlObj.css("word-break")

  @css_word_break.setter
  def css_word_break(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-break": val})

  @property
  def css_word_spacing(self): return self.htmlObj.css("word-spacing")

  @css_word_spacing.setter
  def css_word_spacing(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-spacing": val})

  @property
  def css_word_wrap(self): return self.htmlObj.css("word-wrap")

  @css_word_wrap.setter
  def css_word_wrap(self, val):
    val = val or 'None'
    self.htmlObj.css({"word-wrap": val})

  @property
  def css_writing_mode(self): return self.htmlObj.css("writing-mode")

  @css_writing_mode.setter
  def css_writing_mode(self, val):
    val = val or 'None'
    self.htmlObj.css({"writing-mode": val})

  @property
  def css_z_index(self): return self.htmlObj.css("z-index")

  @css_z_index.setter
  def css_z_index(self, val):
    val = val or 'None'
    self.htmlObj.css({"z-index": val})
