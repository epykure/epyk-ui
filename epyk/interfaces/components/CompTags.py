#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from typing import Union
from epyk.core import html
from epyk.interfaces import Arguments


class Tags:

  def __init__(self, ui):
    self.page = ui.page

  def a(self, text: str, url: str, width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
        html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <a> tag defines a hyperlink, which is used to link from one page to another.

    The most important attribute of the <a> element is the href attribute, which indicates the link's destination.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGenericLink`

    Related Pages:

      https://www.w3schools.com/tags/tag_a.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Usage::
 
    :param text: String with the content to be added to the component.
    :param url: String. Specifies the URL of the page the link goes to.
    :param width: Tuple with the width value and its unit.
    :param height: Tuple with the height value and its unit.
    :param html_code: String. The code reference of the component.
    :param tooltip: String. The tooltip to be display on the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_a = html.HtmlTags.HtmlGenericLink(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html_a.set_attrs(name="href", value=url)
    html_a.style.clear()
    html.Html.set_component_skin(html_a)
    return html_a

  def aside(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
            html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <aside> tag defines some content aside from the content it is placed in.

    The aside content should be related to the surrounding content.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGenericLink`

    Related Pages:

      https://www.w3schools.com/tags/tag_aside.asp
 
    :param text: String with the content to be added to the component.
    :param width: Tuple with the width value and its unit.
    :param height: Tuple with the height value and its unit.
    :param html_code: String. The code reference of the component.
    :param tooltip: String. The tooltip to be display on the component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_a = html.HtmlTags.HtmlGenericLink(self.page, sys._getframe().f_code.co_name, text, width,
                                           height, html_code, tooltip, options, profile)
    html_a.style.clear()
    html.Html.set_component_skin(html_a)
    return html_a

  def b(self, text: str, width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <b> tag specifies bold text without any extra importance.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_b.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_b = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                       height, html_code, tooltip, options, profile)
    html_b.style.clear()
    html.Html.set_component_skin(html_b)
    return html_b

  def h1(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`s

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_h1 = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                        height, html_code, tooltip, options, profile)
    html_h1.style.clear_all()
    html.Html.set_component_skin(html_h1)
    return html_h1

  def h2(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_h2 = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                        height, html_code, tooltip, options, profile)
    html_h2.style.clear_all()
    html.Html.set_component_skin(html_h2)
    return html_h2

  def h3(self, text: str = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_h3 = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                        height, html_code, tooltip, options, profile)
    html_h3.style.clear_all()
    html.Html.set_component_skin(html_h3)
    return html_h3

  def hn(self, level: int, text: str, width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp
 
    :param level: Integer.
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_hn = html.HtmlTags.HtmlGeneric(self.page, "h%s" % level, text, width,
                                        height, html_code, tooltip, options, profile)
    html_hn.style.clear_all()
    html.Html.set_component_skin(html_hn)
    return html_hn

  def delete(self, text: str, width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
             html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_d = html.HtmlTags.HtmlGeneric(self.page, 'del', text, width,  height, html_code, tooltip, options, profile)
    html_d.style.clear()
    html.Html.set_component_skin(html_d)
    return html_d

  def figcaption(self, text: str = "", width=(None, "%"), height=(None, "px"), html_code=None, tooltip='',
                 options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <figcaption> tag defines a caption for a <figure> element.

    The <figcaption> element can be placed as the first or last child of the <figure> element.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGenericLink`

    Related Pages:

      https://www.w3schools.com/tags/tag_figcaption.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_f = html.HtmlTags.HtmlGenericLink(self.page, sys._getframe().f_code.co_name, text, width,
                                           height, html_code, tooltip, options, profile)
    html_f.style.clear()
    html.Html.set_component_skin(html_f)
    return html_f

  def u(self, text, width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
        html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    Underline a misspelled word with the <u> tag:
    <p>This is a <u>paragraph</u>.</p>

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_u.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_u = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                       height, html_code, tooltip, options, profile)
    html_u.style.clear()
    html.Html.set_component_skin(html_u)
    return html_u

  def p(self, text = "", width: Union[tuple, int] = (None, "%"), height: Union[tuple, int] = (None, "px"),
        html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    A paragraph is marked up as follows with the <p> tag:
    <p>This is some text in a paragraph.</p>

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_p.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_p = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                       height, html_code, tooltip, options, profile)
    html_p.style.clear()
    html.Html.set_component_skin(html_p)
    return html_p

  def bdi(self, text, width: Union[tuple, int] = (100, "%"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    BDI stands for Bi-Directional Isolation.
    The <bdi> tag is new in HTML5.

    Usage::

      bdi = rptObj.ui.tags.bdi("bdi tag")
      bdi.click(rptObj.js.alert("test"))
      bdi.css({'cursor': 'pointer'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_bdi.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_bdi = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_bdi)
    return html_bdi

  def bdo(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    bdo stands for Bi-Directional Override.
    The <bdo> tag is used to override the current text direction.

    Usage::

      bdo = rptObj.ui.tags.bdo("bdo tag")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_bdo.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_bdo = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_bdo)
    return html_bdo

  def ol(self, text="", width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <ol> tag defines an ordered list. An ordered list can be numerical or alphabetical.

    Use the <li> tag to define list items.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_ol.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_sup = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width, height, html_code,
                                         tooltip, options, profile)
    html.Html.set_component_skin(html_sup)
    return html_sup

  def em(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
         html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <em> tag is a phrase tag. It renders as emphasized text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_em.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_em = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_em)
    return html_em

  def strong(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
             html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <strong> tag is a phrase tag. It defines important text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_strong.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_strong = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_strong)
    return html_strong

  def samp(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <samp> tag is a phrase tag. It defines sample output from a computer program.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_samp.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_samp = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_samp)
    return html_samp

  def kbd(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <kbd> tag is a phrase tag. It defines keyboard input.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_kbd.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_kbd = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_kbd)
    return html_kbd

  def var(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <var> tag also supports the Global Attributes in HTML.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_var.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_var = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_var)
    return html_var

  def sup(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <sup> tag defines superscript text. Superscript text appears half a character above the normal line,
    and is sometimes rendered in a smaller font. Superscript text can be used for footnotes, like WWW

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_sup.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_sup = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_sup)
    return html_sup

  def wbr(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <wbr> (Word Break Opportunity) tag specifies where in a text it would be ok to add a line-break.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_wbr.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_wbr = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_wbr)
    return html_wbr

  def time(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <time> tag defines a human-readable date/time.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_time.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_time = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_time)
    return html_time

  def sub(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <sub> tag defines subscript text. Subscript text appears half a character below the normal line,
    and is sometimes rendered in a smaller font.
    Subscript text can be used for chemical formulas, like H2O.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_sub.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_sub = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_sub)
    return html_sub

  def small(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
            html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <small> tag defines smaller text (and other side comments).

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_small.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_small = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_small)
    return html_small

  def s(self, text, width=(100, "px"), height: Union[tuple, int] = (None, "px"), html_code: str = None,
        tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <s> tag specifies text that is no longer correct, accurate or relevant.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_s.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_s = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_s)
    return html_s

  def i(self, text, width: Union[tuple, int] = (None, "px"), height: Union[tuple, int] = (None, "px"),
        html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <i> tag defines a part of text in an alternate voice or mood. The content of the <i>
    tag is usually displayed in italic.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Usage::


    Related Pages:

      https://www.w3schools.com/tags/tag_i.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_i = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_i)
    return html_i

  def q(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
        html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <q> tag defines a short quotation.

    Browsers normally insert quotation marks around the quotation.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_q.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_q = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                       height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_q)
    return html_q

  def mark(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <mark> tag defines marked text.

    Use the <mark> tag if you want to highlight parts of your text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_mark.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_mark = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                          height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_mark)
    return html_mark

  def nav(self, text: str = None, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The HTML <nav> element represents a section of a page whose purpose is to provide navigation links, either within
    the current document or to other documents.
    Common examples of navigation sections are menus, tables of contents, and indexes.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://fr.w3docs.com/apprendre-html/html-tag-nav.html
      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_mark = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                          height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_mark)
    return html_mark

  def ins(self, text, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <ins> tag defines a text that has been inserted into a document.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_ins.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_ins = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_ins)
    return html_ins

  def dfn(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
          html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <dfn> tag represents the defining instance of a term in HTML.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_dfn.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_dfn = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                         height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_dfn)
    return html_dfn

  def cite(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <cite> tag defines the title of a work (e.g. a book, a song, a movie, a TV show, a painting, a sculpture, etc.).

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_cite.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_cite = html.HtmlTags.HtmlGeneric(self.page, sys._getframe().f_code.co_name, text, width,
                                          height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_cite)
    return html_cite

  def abbr(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_abbr.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_abbr = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_abbr)
    return html_abbr

  def meter(self, text: str, width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
            html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <meter> tag defines a scalar measurement within a known range, or a fractional value.
    This is also known as a gauge.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_meter.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_abbr = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_abbr)
    return html_abbr

  def comment(self, text: str):
    """  
    Add an HTML comment to the code

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlComment`
 
    :param text: String with the content to be added to the component
    """
    html_comm = html.HtmlTags.HtmlComment(self.page, text)
    html.Html.set_component_skin(html_comm)
    return html_comm

  def span(self, text: str = "", width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
           html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <span> tag is an inline container used to mark up a part of a text, or a part of a document.

    The <span> tag is easily styled by CSS or manipulated with JavaScript using the class or id attribute.

    The <span> tag is much like the <div> element, but <div> is a block-level element and <span> is an inline element.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_span.asp

    Usage::

      s2 = page.ui.tags.span('''
        Value Formatter €
        A Value Formatter is
        ''', options={"multiline": True})
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_span = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_span)
    return html_span

  def label(self, text: str = "", width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
            html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    The <label> tag defines a label for several elements.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_span = html.HtmlTags.HtmlGeneric(
      self.page, sys._getframe().f_code.co_name, text, width, height, html_code, tooltip, options, profile)
    html.Html.set_component_skin(html_span)
    return html_span

  def no_tag(self, text: str = "", width: Union[tuple, int] = (100, "px"), height: Union[tuple, int] = (None, "px"),
             html_code: str = None, tooltip: str = '', options: dict = None, profile: Union[dict, bool] = None):
    """  
    Dummy HTML without any tag to add this to the list of a container objects.
 
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param html_code: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean flag to set the profiling mode for the component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    return html.HtmlTags.HtmlGeneric(
      self.page, None, text, width, height, html_code, tooltip, options, profile)
