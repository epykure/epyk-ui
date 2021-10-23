#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Titles:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def head(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"), height=('auto', ""),
           html_code=None, profile=False):
    """
    Description:
    ------------


    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
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
    return html_title

  @html.Html.css_skin()
  def headline(self, text="", options=None, tooltip="", align="left", color=True, width=(None, "px"),
               height=('auto', ""), html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def title(self, text=None, options=None, tooltip="", align="left", color=None, width=(None, "px"),
            height=('auto', ""), html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. he text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def section(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"),
              height=('auto', ""), html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def rubric(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"), height=('auto', ""),
             html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def category(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"),
               height=('auto', ""), html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def caption(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"),
              height=('auto', ""), html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def underline(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"),
                height=('auto', ""),  html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title

  @html.Html.css_skin()
  def bold(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"), height=('auto', ""),
           html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        http://192.168.0.34:8081/script/home

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    return html_title

  @html.Html.css_skin()
  def subtitle(self, text="", name=None, contents=None, color=None, picture=None, icon=None, top=5,
               html_code=None, width=("auto", ""), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param name:
    :param contents:
    :param color: String. Optional. The font color in the component. Default inherit.
    :param picture:
    :param icon:
    :param top:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    title = self.page.ui.title(text=text, name=name, contents=contents, color=color, picture=picture, icon=icon,
                               top=top, html_code=html_code, width=width, height=height, align=align, options=options,
                               profile=profile)
    title.style.css.font_size = self.page.body.style.globals.font.normal(2)
    title.style.css.bold()
    return title

  @html.Html.css_skin()
  def upper(self, text="", options=None, tooltip="", align="left", color=None, width=(None, "px"), height=('auto', ""),
            html_code=None, profile=False):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.titles.upper("Test")
      page.ui.titles.upper("Test", color=True)

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
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
    return html_title
