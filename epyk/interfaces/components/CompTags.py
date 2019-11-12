"""

"""

import sys

from epyk.core import html


class Tags(object):

  def __init__(self, context):
    self.context = context

  def bdi(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    BDI stands for Bi-Directional Isolation.
    The <bdi> tag is new in HTML5.

    Example
    bdi = rptObj.ui.tags.bdi("bdi tag")
    bdi.click(rptObj.js.alert("test"))
    bdi.css({'cursor': 'pointer'})

    Documentation
    https://www.w3schools.com/tags/tag_bdi.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_bdi = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_bdi)
    return html_bdi

  def bdo(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    bdo stands for Bi-Directional Override.
    The <bdo> tag is used to override the current text direction.

    Documentation
    https://www.w3schools.com/tags/tag_bdo.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_bdo = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_bdo)
    return html_bdo

  def em(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <em> tag is a phrase tag. It renders as emphasized text.

    Documentation
    https://www.w3schools.com/tags/tag_em.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_em = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_em)
    return html_em

  def strong(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <strong> tag is a phrase tag. It defines important text.

    Documentation
    https://www.w3schools.com/tags/tag_strong.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_strong = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_strong)
    return html_strong

  def samp(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <samp> tag is a phrase tag. It defines sample output from a computer program.

    Documentation
    https://www.w3schools.com/tags/tag_samp.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_samp = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_samp)
    return html_samp

  def kbd(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <kbd> tag is a phrase tag. It defines keyboard input.

    Documentation
    https://www.w3schools.com/tags/tag_kbd.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_kbd = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_kbd)
    return html_kbd

  def var(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <var> tag also supports the Global Attributes in HTML.

    Documentation
    https://www.w3schools.com/tags/tag_var.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_var = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_var)
    return html_var

  def sup(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <sup> tag defines superscript text. Superscript text appears half a character above the normal line, and is sometimes rendered in a smaller font. Superscript text can be used for footnotes, like WWW

    Documentation
    https://www.w3schools.com/tags/tag_sup.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_sup = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_sup)
    return html_sup

  def wbr(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <wbr> (Word Break Opportunity) tag specifies where in a text it would be ok to add a line-break.

    Documentation
    https://www.w3schools.com/tags/tag_wbr.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_wbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_wbr)
    return html_wbr

  def time(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <time> tag defines a human-readable date/time.

    Documentation
    https://www.w3schools.com/tags/tag_time.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_time = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_time)
    return html_time

  def sub(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <sub> tag defines subscript text. Subscript text appears half a character below the normal line, and is sometimes rendered in a smaller font.
    Subscript text can be used for chemical formulas, like H2O.

    Documentation
    https://www.w3schools.com/tags/tag_sub.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_sub = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_sub)
    return html_sub

  def small(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <small> tag defines smaller text (and other side comments).

    Documentation
    https://www.w3schools.com/tags/tag_small.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_small = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_small)
    return html_small

  def s(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <s> tag specifies text that is no longer correct, accurate or relevant.

    Documentation
    https://www.w3schools.com/tags/tag_s.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_s = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_s)
    return html_s

  def i(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <i> tag defines a part of text in an alternate voice or mood. The content of the <i> tag is usually displayed in italic.

    Documentation
    https://www.w3schools.com/tags/tag_i.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_i = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_i)
    return html_i

  def q(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <q> tag defines a short quotation.

    Browsers normally insert quotation marks around the quotation.

    Documentation
    https://www.w3schools.com/tags/tag_q.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_q = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_q)
    return html_q

  def mark(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <mark> tag defines marked text.

    Use the <mark> tag if you want to highlight parts of your text.

    Documentation
    https://www.w3schools.com/tags/tag_mark.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_mark = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                        height, htmlCode, tooltip, profile)
    self.context.register(html_mark)
    return html_mark

  def ins(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <ins> tag defines a text that has been inserted into a document.

    Documentation
    https://www.w3schools.com/tags/tag_ins.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_ins = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_ins)
    return html_ins

  def dfn(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <dfn> tag represents the defining instance of a term in HTML.

    Documentation
    https://www.w3schools.com/tags/tag_dfn.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_dfn = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_dfn)
    return html_dfn

  def cite(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <cite> tag defines the title of a work (e.g. a book, a song, a movie, a TV show, a painting, a sculpture, etc.).

    Documentation
    https://www.w3schools.com/tags/tag_cite.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_cite = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_cite)
    return html_cite

  def abbr(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Documentation
    https://www.w3schools.com/tags/tag_abbr.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_abbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_abbr)
    return html_abbr

  def meter(self, text, size=(None, "px"), width=(100, "px"), height=(None, "px"), htmlCode=None, tooltip='', profile=None):
    """
    The <meter> tag defines a scalar measurement within a known range, or a fractional value.
    This is also known as a gauge.

    Documentation
    https://www.w3schools.com/tags/tag_meter.asp

    :param text: String with the content to be added to the component
    :param size: Tuple with the size value and its unit
    :param width: Tuple with the width value and its unit
    :param height: Tuple with the height value and its unit
    :param htmlCode: String. The code reference of the component
    :param tooltip: String. The tooltip to be display on the component
    :param profile: Boolean flag to set the profiling mode for the component
    """
    size = self.context._size(size)
    html_abbr = html.HtmlTags.HtmlGeneric(self.context.rptObj, sys._getframe().f_code.co_name, text, size, width,
                                         height, htmlCode, tooltip, profile)
    self.context.register(html_abbr)
    return html_abbr

  def comment(self, text):
    """
    Add an HTML comment to the code

    :param text: String with the content to be added to the component
    """
    html_comm = html.HtmlTags.HtmlComment(self.context.rptObj, text)
    self.context.register(html_comm)
    return html_comm
