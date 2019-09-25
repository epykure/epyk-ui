"""
HTML tags
"""

import sys


class Tags(object):

  def __tag(self, tab_name, data, css_styles, cls_names, attrs):
    """
    Build the HTML tag

    :param tab_name: The function tag name
    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return:
    """
    html_tags = []
    if css_styles is not None:
      html_tags.append('style="%s"' % ";".join(['%s:%s' % (k, v) for k, v in css_styles.items()]))
    if cls_names is not None:
      html_tags.append('class="%s"' % " ".join(cls_names))
    if attrs is not None:
      html_tags.append(" ".join(['%s="%s"' % (k, v) for k, v in attrs.items() if k not in ["class", "style"]]))
    return "<%(tag)s %(html_tags)s>%(data)s</%(tag)s>" % {"tag": tab_name, "html_tags": " ".join(html_tags), "data": data}

  def bdi(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    BDI stands for Bi-Directional Isolation.
    The <bdi> tag is new in HTML5.

    Documentation
    https://www.w3schools.com/tags/tag_bdi.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def bdo(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    bdo stands for Bi-Directional Override.
    The <bdo> tag is used to override the current text direction.

    Documentation
    https://www.w3schools.com/tags/tag_bdo.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def em(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <em> tag is a phrase tag. It renders as emphasized text.

    Documentation
    https://www.w3schools.com/tags/tag_em.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def strong(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <strong> tag is a phrase tag. It defines important text.

    Documentation
    https://www.w3schools.com/tags/tag_strong.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def samp(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <samp> tag is a phrase tag. It defines sample output from a computer program.

    Documentation
    https://www.w3schools.com/tags/tag_samp.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def kbd(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <kbd> tag is a phrase tag. It defines keyboard input.

    Documentation
    https://www.w3schools.com/tags/tag_kbd.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def var(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <var> tag also supports the Global Attributes in HTML.

    Documentation
    https://www.w3schools.com/tags/tag_var.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def sup(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <sup> tag defines superscript text. Superscript text appears half a character above the normal line, and is sometimes rendered in a smaller font. Superscript text can be used for footnotes, like WWW

    Documentation
    https://www.w3schools.com/tags/tag_sup.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def wbr(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <wbr> (Word Break Opportunity) tag specifies where in a text it would be ok to add a line-break.

    Documentation
    https://www.w3schools.com/tags/tag_wbr.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def time(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <time> tag defines a human-readable date/time.

    Documentation
    https://www.w3schools.com/tags/tag_time.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def sub(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <sub> tag defines subscript text. Subscript text appears half a character below the normal line, and is sometimes rendered in a smaller font.
    Subscript text can be used for chemical formulas, like H2O.

    Documentation
    https://www.w3schools.com/tags/tag_sub.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def small(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <small> tag defines smaller text (and other side comments).

    Documentation
    https://www.w3schools.com/tags/tag_small.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def s(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <s> tag specifies text that is no longer correct, accurate or relevant.

    Documentation
    https://www.w3schools.com/tags/tag_s.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def i(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <i> tag defines a part of text in an alternate voice or mood. The content of the <i> tag is usually displayed in italic.

    Documentation
    https://www.w3schools.com/tags/tag_i.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def q(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <q> tag defines a short quotation.

    Browsers normally insert quotation marks around the quotation.

    Documentation
    https://www.w3schools.com/tags/tag_q.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def mark(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <mark> tag defines marked text.

    Use the <mark> tag if you want to highlight parts of your text.

    Documentation
    https://www.w3schools.com/tags/tag_mark.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def ins(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <ins> tag defines a text that has been inserted into a document.

    Documentation
    https://www.w3schools.com/tags/tag_ins.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def dfn(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <dfn> tag represents the defining instance of a term in HTML.

    Documentation
    https://www.w3schools.com/tags/tag_dfn.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def cite(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <cite> tag defines the title of a work (e.g. a book, a song, a movie, a TV show, a painting, a sculpture, etc.).

    Documentation
    https://www.w3schools.com/tags/tag_cite.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def abbr(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Documentation
    https://www.w3schools.com/tags/tag_abbr.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def meter(self, data, css_styles=None, cls_names=None, attrs=None):
    """
    The <meter> tag defines a scalar measurement within a known range, or a fractional value.
    This is also known as a gauge.

    Documentation
    https://www.w3schools.com/tags/tag_meter.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return self.__tag(sys._getframe().f_code.co_name, data, css_styles, cls_names, attrs)

  def comment(self, data):
    """
    The <abbr> tag defines an abbreviation or an acronym, like "HTML", "Mr.", "Dec.", "ASAP", "ATM".

    Documentation
    https://www.w3schools.com/tags/tag_abbr.asp

    :param css_styles: A dictionary with the CSS Styles
    :param cls_names: A list with the class Names
    :param attrs: A dictionary with the tag attributes

    :return: A string of the tag
    """
    return "<!--%s-->" % data
