"""

"""

import sys

from epyk.core import html


class Tags(object):

  def __init__(self, context):
    self.context = context

  def b(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <b> tag specifies bold text without any extra importance.

    Related Pages:
    --------------
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
                                       height, htmlCode, tooltip, profile)
    html_b.style.clear()
    self.context.register(html_b)
    return html_b

  def delete(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    html_d = html.HtmlTags.HtmlGeneric(self.context.rptObj, 'del', text, width,  height, htmlCode, tooltip, profile)
    html_d.style.clear()
    self.context.register(html_d)
    return html_d

  def u(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    Underline a misspelled word with the <u> tag:
    <p>This is a <u>paragraph</u>.</p>

    Related Pages:
    --------------
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
                                       height, htmlCode, tooltip, profile)
    html_u.style.clear()
    self.context.register(html_u)
    return html_u

  def p(self, text, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    A paragraph is marked up as follows with the <p> tag:
    <p>This is some text in a paragraph.</p>

    Related Pages:
    --------------
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
                                       height, htmlCode, tooltip, profile)
    html_p.style.clear()
    self.context.register(html_p)
    return html_p

  def bdi(self, text, width=(100, "%"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    BDI stands for Bi-Directional Isolation.
    The <bdi> tag is new in HTML5.

    Usage:
    ------
    bdi = rptObj.ui.tags.bdi("bdi tag")
    bdi.click(rptObj.js.alert("test"))
    bdi.css({'cursor': 'pointer'})

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_bdi)
    return html_bdi

  def bdo(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    bdo stands for Bi-Directional Override.
    The <bdo> tag is used to override the current text direction.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_bdo)
    return html_bdo

  def em(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <em> tag is a phrase tag. It renders as emphasized text.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_em)
    return html_em

  def strong(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <strong> tag is a phrase tag. It defines important text.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_strong)
    return html_strong

  def samp(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <samp> tag is a phrase tag. It defines sample output from a computer program.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_samp)
    return html_samp

  def kbd(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <kbd> tag is a phrase tag. It defines keyboard input.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_kbd)
    return html_kbd

  def var(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <var> tag also supports the Global Attributes in HTML.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_var)
    return html_var

  def sup(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <sup> tag defines superscript text. Superscript text appears half a character above the normal line, and is sometimes rendered in a smaller font. Superscript text can be used for footnotes, like WWW

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_sup)
    return html_sup

  def wbr(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <wbr> (Word Break Opportunity) tag specifies where in a text it would be ok to add a line-break.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_wbr)
    return html_wbr

  def time(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <time> tag defines a human-readable date/time.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_time)
    return html_time

  def sub(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <sub> tag defines subscript text. Subscript text appears half a character below the normal line, and is sometimes rendered in a smaller font.
    Subscript text can be used for chemical formulas, like H2O.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_sub)
    return html_sub

  def small(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <small> tag defines smaller text (and other side comments).

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_small)
    return html_small

  def s(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <s> tag specifies text that is no longer correct, accurate or relevant.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_s)
    return html_s

  def i(self, text, width=(None, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <i> tag defines a part of text in an alternate voice or mood. The content of the <i> tag is usually displayed in italic.

    Related Pages:
    --------------
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
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_i)
    return html_i

  def q(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <q> tag defines a short quotation.

    Browsers normally insert quotation marks around the quotation.

    Related Pages:
    --------------
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
                                       height, htmlCode, tooltip, profile)
    self.context.register(html_q)
    return html_q

  def mark(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <mark> tag defines marked text.

    Use the <mark> tag if you want to highlight parts of your text.

    Related Pages:
    --------------
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
                                          height, htmlCode, tooltip, profile)
    self.context.register(html_mark)
    return html_mark

  def ins(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <ins> tag defines a text that has been inserted into a document.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_ins)
    return html_ins

  def dfn(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <dfn> tag represents the defining instance of a term in HTML.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_dfn)
    return html_dfn

  def cite(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <cite> tag defines the title of a work (e.g. a book, a song, a movie, a TV show, a painting, a sculpture, etc.).

    Related Pages:
    --------------
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
                                          height, htmlCode, tooltip, profile)
    self.context.register(html_cite)
    return html_cite

  def abbr(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_abbr)
    return html_abbr

  def meter(self, text, width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    Description:
    ------------
    The <meter> tag defines a scalar measurement within a known range, or a fractional value.
    This is also known as a gauge.

    Related Pages:
    --------------
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
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_abbr)
    return html_abbr

  def comment(self, text):
    """
    Description:
    ------------
    Add an HTML comment to the code

    Attributes:
    ----------
    :param text: String with the content to be added to the component
    """
    html_comm = html.HtmlTags.HtmlComment(self.context.rptObj, text)
    self.context.register(html_comm)
    return html_comm
