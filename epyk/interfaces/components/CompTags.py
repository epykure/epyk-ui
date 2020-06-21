
import sys

from epyk.core import html


class Tags(object):

  def __init__(self, context):
    self.context = context

  def a(self, text, url, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <a> tag defines a hyperlink, which is used to link from one page to another.

    The most important attribute of the <a> element is the href attribute, which indicates the link's destination.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGenericLInk`

    Related Pages:

      https://www.w3schools.com/tags/tag_a.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param url: String. Specifies the URL of the page the link goes to
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_a = html.HtmlTags.HtmlGenericLInk(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                            height, htmlCode, tooltip, options, profile)
    html_a.set_attrs(name="href", value=url)
    html_a.style.clear()
    return html_a

  def aside(self, text="", width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None,
            profile=None):
    """
    Description:
    ------------
    The <aside> tag defines some content aside from the content it is placed in.

    The aside content should be related to the surrounding content.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGenericLInk`

    Related Pages:

      https://www.w3schools.com/tags/tag_aside.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_a = html.HtmlTags.HtmlGenericLInk(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                           height, htmlCode, tooltip, options, profile)
    html_a.style.clear()
    return html_a

  def b(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <b> tag specifies bold text without any extra importance.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_b.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_b = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                       height, htmlCode, tooltip, options, profile)
    html_b.style.clear()
    return html_b

  def h1(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`s

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_h1 = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    html_h1.style.clear_all()
    return html_h1

  def h2(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_h2 = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    html_h2.style.clear_all()
    return html_h2

  def h3(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <h1> to <h6> tags are used to define HTML headings.

    <h1> defines the most important heading. <h6> defines the least important heading.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_hn.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_h3 = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    html_h3.style.clear_all()
    return html_h3

  def delete(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_d = html.HtmlTags.HtmlGeneric(self.context.rptObj, 'del', text, width,  height, htmlCode, tooltip, options, profile)
    html_d.style.clear()
    return html_d

  def u(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    Underline a misspelled word with the <u> tag:
    <p>This is a <u>paragraph</u>.</p>

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_u.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_u = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                       height, htmlCode, tooltip, options, profile)
    html_u.style.clear()
    return html_u

  def p(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    A paragraph is marked up as follows with the <p> tag:
    <p>This is some text in a paragraph.</p>

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_p.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_p = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                       height, htmlCode, tooltip, options, profile)
    html_p.style.clear()
    return html_p

  def bdi(self, text, width=(100, "%"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_bdi = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_bdi

  def bdo(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    bdo stands for Bi-Directional Override.
    The <bdo> tag is used to override the current text direction.

    Usage::

      bdo = rptObj.ui.tags.bdo("bdo tag")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_bdo.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_bdo = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_bdo

  def ol(self, text=None, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <ol> tag defines an ordered list. An ordered list can be numerical or alphabetical.

    Use the <li> tag to define list items.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_ol.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_sup = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width, height, htmlCode, tooltip, options, profile)
    return html_sup

  def em(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <em> tag is a phrase tag. It renders as emphasized text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_em.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_em = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_em

  def strong(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <strong> tag is a phrase tag. It defines important text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_strong.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_strong = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_strong

  def samp(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <samp> tag is a phrase tag. It defines sample output from a computer program.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_samp.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_samp = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_samp

  def kbd(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <kbd> tag is a phrase tag. It defines keyboard input.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_kbd.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_kbd = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_kbd

  def var(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <var> tag also supports the Global Attributes in HTML.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_var.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_var = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_var

  def sup(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <sup> tag defines superscript text. Superscript text appears half a character above the normal line, and is sometimes rendered in a smaller font. Superscript text can be used for footnotes, like WWW

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_sup.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_sup = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_sup

  def wbr(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <wbr> (Word Break Opportunity) tag specifies where in a text it would be ok to add a line-break.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_wbr.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_wbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_wbr

  def time(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <time> tag defines a human-readable date/time.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_time.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_time = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_time

  def sub(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <sub> tag defines subscript text. Subscript text appears half a character below the normal line, and is sometimes rendered in a smaller font.
    Subscript text can be used for chemical formulas, like H2O.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_sub.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_sub = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_sub

  def small(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <small> tag defines smaller text (and other side comments).

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_small.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_small = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_small

  def s(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <s> tag specifies text that is no longer correct, accurate or relevant.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_s.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_s = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_s

  def i(self, text, width=(None, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <i> tag defines a part of text in an alternate voice or mood. The content of the <i> tag is usually displayed in italic.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_i.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_i = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                        height, htmlCode, tooltip, options, profile)
    return html_i

  def q(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <q> tag defines a short quotation.

    Browsers normally insert quotation marks around the quotation.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_q.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_q = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                       height, htmlCode, tooltip, options, profile)
    return html_q

  def mark(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <mark> tag defines marked text.

    Use the <mark> tag if you want to highlight parts of your text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_mark.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_mark = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                          height, htmlCode, tooltip, options, profile)
    return html_mark

  def nav(self, text=None, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The HTML <nav> element represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents.
    Common examples of navigation sections are menus, tables of contents, and indexes.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://fr.w3docs.com/apprendre-html/html-tag-nav.html
      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_mark = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                          height, htmlCode, tooltip, options, profile)
    return html_mark

  def ins(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <ins> tag defines a text that has been inserted into a document.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_ins.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_ins = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_ins

  def dfn(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <dfn> tag represents the defining instance of a term in HTML.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_dfn.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_dfn = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_dfn

  def cite(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <cite> tag defines the title of a work (e.g. a book, a song, a movie, a TV show, a painting, a sculpture, etc.).

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_cite.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_cite = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                          height, htmlCode, tooltip, options, profile)
    return html_cite

  def abbr(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_abbr.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_abbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_abbr

  def meter(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', options=None, profile=None):
    """
    Description:
    ------------
    The <meter> tag defines a scalar measurement within a known range, or a fractional value.
    This is also known as a gauge.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlGeneric`

    Related Pages:

      https://www.w3schools.com/tags/tag_meter.asp

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_abbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, width,
                                         height, htmlCode, tooltip, options, profile)
    return html_abbr

  def comment(self, text):
    """
    Description:
    ------------
    Add an HTML comment to the code

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTags.HtmlComment`

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    """
    html_comm = html.HtmlTags.HtmlComment(self.context.rptObj, text)
    return html_comm
