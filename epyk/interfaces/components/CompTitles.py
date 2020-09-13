#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.interfaces import Arguments


class Titles(object):

  def __init__(self, context):
    self.context = context

  def head(self, text=None, options=None, tooltip="", align="left", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    # html_title.style.css.border_left = '5px solid %s' % self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_size = Defaults_css.font(15)
    html_title.style.css.text_transform = 'uppercase'
    html_title.style.css.text_align = align
    html_title.style.css.margin_left = 2
    html_title.style.css.padding_left = 2
    html_title.style.css.bold()
    return html_title

  def headline(self, text=None, options=None, tooltip="", align="left", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(8)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 5
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_style = 'italic'
    return html_title

  def title(self, text=None, options=None, tooltip="", align="left", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param align:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(12)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 10
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    return html_title

  def section(self, text=None, options=None, tooltip="", align="left", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param tooltip: String. Optional. A string with the value of the tooltip
    :param align: String. Optional. A string with the horizontal position of the component
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(8)
    html_title.style.css.text_align = align
    html_title.style.css.margin_top = 20
    html_title.style.css.margin_bottom = 10
    return html_title

  def rubric(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.border_left = '3px solid %s' % self.context.rptObj.theme.colors[-1]
    html_title.style.css.font_size = Defaults_css.font(6)
    return html_title

  def caption(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(4)
    html_title.style.css.color = self.context.rptObj.theme.colors[-1]
    return html_title

  def underline(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.context.rptObj, "div", text, width, height, htmlCode, tooltip,
                                           dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(6)
    html_title.style.css.border_bottom = '2px solid %s' % self.context.rptObj.theme.colors[-1]
    return html_title

  def subtitle(self, text=None, name=None, contents=None, color=None, picture=None, icon=None, marginTop=5, htmlCode=None,
               width=("auto", ""), height=(None, "px"), align=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param name:
    :param contents:
    :param color:
    :param picture:
    :param icon:
    :param marginTop:
    :param htmlCode:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    title = self.context.rptObj.ui.title(text=text, name=name, contents=contents, color=color, picture=picture, icon=icon,
            marginTop=marginTop, htmlCode=htmlCode, width=width, height=height, align=align, options=options, profile=profile)
    title.style.css.font_size = Defaults_css.font(3)
    title.style.css.bold()
    return title

