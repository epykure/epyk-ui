#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.py import types


class Titles:
  """

  """

  def __init__(self, ui):
    self.page = ui.page

  def __format_text(self, text: Union[str, dict], size: str = None, italic: bool = True) -> str:
    if isinstance(text, dict):
      sub_title = self.page.ui.div(list(text.values())[0])
      sub_title.options.managed = False
      if italic:
        sub_title.style.css.italic()
      sub_title.style.css.color = self.page.theme.greys[4]
      sub_title.style.css.text_transform = "lowercase"
      sub_title.style.css.display = "inline"
      sub_title.style.css.font_size = size or self.page.body.style.globals.font.normal(-3)
      return "<b>%s</b> %s" % (list(text.keys())[0], sub_title.html())

    return text

  def head(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
           color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
           html_code: str = None, profile: types.PROFILE_TYPE = False):
    """


    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    text = self.__format_text(text, self.page.body.style.globals.font.normal(5), italic=False)
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip,  dflt_options, profile)
    if color:
      html_title.style.css.color = self.page.theme.colors[-1] if color is True else color
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(10)
    html_title.style.css.text_transform = 'uppercase'
    html_title.style.css.text_align = align
    html_title.style.css.margin_left = 2
    html_title.style.css.padding_left = 2
    html_title.style.css.bold()
    html.Html.set_component_skin(html_title)
    return html_title

  def headline(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
               color: bool = True, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
               html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

      page.ui.titles.headline("Daily")

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal(2))
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.page, "div", text, width, height, html_code, tooltip,
                                           dflt_options, profile)
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(6)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 5
    html_title.style.css.font_style = 'italic'
    html.Html.set_component_skin(html_title)
    return html_title

  def title(self, text: Union[str, dict] = None, options: dict = None, tooltip: str = "", align: str = "left",
            color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
            html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. he text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal(-3))
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(8)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 10
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    if hasattr(self.page, '_content_table'):   # and self.options.content_table:
      self.page._content_table.add_title(html_title, level=1)
    html.Html.set_component_skin(html_title)
    return html_title

  def section(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
              color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
              html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

      t0 = page.ui.titles.section("Available Items")

    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal())
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.page, "div", text, width, height, html_code, tooltip,
                                           dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(4)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 20
    html_title.style.css.margin_bottom = 10
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    if hasattr(self.page, '_content_table'):   # and self.options.content_table:
      self.page._content_table.add_title(html_title, level=4)
    html.Html.set_component_skin(html_title)
    return html_title

  def rubric(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
             color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
             html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal(), italic=False)
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.border_left = '3px solid %s' % self.page.theme.colors[2]
    html_title.style.css.padding_left = 5
    html_title.style.css.text_align = align
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(2)
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    html.Html.set_component_skin(html_title)
    return html_title

  def category(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
               color: str = None, width: types.SIZE_TYPE = (None, "px"),
               height: types.SIZE_TYPE = ('auto', ""), html_code: str = None,
               profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
 -
    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal())
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    if color:
      u_color = self.page.theme.notch(-2) if color is True else color
    else:
      u_color = self.page.theme.greys[2]
    html_title.style.css.border_bottom = '3px solid %s' % u_color
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(5)
    html_title.style.css.margin_bottom = 5
    html_title.style.css.text_align = align
    html_title.style.css.text_transform = "uppercase"
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    html.Html.set_component_skin(html_title)
    return html_title

  def caption(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
              color: str = None,
              width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""), html_code: str = None,
              profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
 -
    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal())
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(2)
    html_title.style.css.color = self.page.theme.colors[-1]
    html_title.style.css.text_align = align
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    html.Html.set_component_skin(html_title)
    return html_title

  def underline(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
                color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
                html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
 -
    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param color: Optional. The font color in the component. Default inherit
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal(), italic=False)
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(4)
    if color:
      color = self.page.theme.notch(-2) if color is True else color
    else:
      color = self.page.theme.greys[2]
    html_title.style.css.border_bottom = '2px solid %s' % color
    html_title.style.css.margin_bottom = 10
    html_title.style.css.text_align = align
    html.Html.set_component_skin(html_title)
    return html_title

  def bold(self, text: str = "", options: dict = None, tooltip: str = "", align: str = "left", color: str = None,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
           html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
 -
    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(2)
    html_title.style.css.font_weight = "bold"
    if color:
      html_title.style.css.color = self.page.theme.notch() if color is True else color
    html_title.style.css.text_align = align
    html.Html.set_component_skin(html_title)
    return html_title

  def subtitle(self, text: str = "", name: str = None, contents=None, color: str = None, picture: str = None,
               icon: str = None, top: int = 5, html_code: str = None, width: types.SIZE_TYPE = ("auto", ""),
               height: types.SIZE_TYPE = (None, "px"), align: str = None, options: dict = None,
               profile: types.PROFILE_TYPE = None):
    """

    :tags:
    :categories:

    Usage::
 -
    :param text: Optional. The value to be displayed to the component
    :param name:
    :param contents:
    :param color: Optional. The font color in the component. Default inherit
    :param picture:
    :param icon:
    :param top:
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    title = self.page.ui.title(text=text, name=name, contents=contents, color=color, picture=picture, icon=icon,
                               top=top, html_code=html_code, width=width, height=height, align=align, options=options,
                               profile=profile)
    title.style.css.font_size = self.page.body.style.globals.font.normal(2)
    title.style.css.bold()
    html.Html.set_component_skin(title)
    return title

  def upper(self, text: Union[str, dict] = "", options: dict = None, tooltip: str = "", align: str = "left",
            color: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = ('auto', ""),
            html_code: str = None, profile: types.PROFILE_TYPE = False):
    """

    :tags:
    :categories:

    Usage::

      page.ui.titles.upper("Test")
      page.ui.titles.upper("Test", color=True)

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py
 -
    :param text: Optional. The value to be displayed to the component
    :param options: Optional. Specific Python options available for this component
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    text = self.__format_text(text, self.page.body.style.globals.font.normal(3), italic=False)
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(
      self.page, "div", text, width, height, html_code, tooltip, dflt_options, profile)
    html_title.style.css.font_size = self.page.body.style.globals.font.normal(8)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 10
    html_title.style.css.padding_bottom = 5
    html_title.style.css.margin_bottom = 20
    html_title.style.css.bold()
    html_title.style.css.text_transform = "uppercase"
    if color:
      u_color = self.page.theme.notch(-2) if color is True else color
    else:
      u_color = self.page.theme.greys[2]
    html_title.style.css.border_bottom = "3px solid %s" % u_color
    if color:
      html_title.style.css.color = self.page.theme.notch(2) if color is True else color
    html.Html.set_component_skin(html_title)
    return html_title
