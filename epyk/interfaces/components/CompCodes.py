#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Code:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def css(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
          profile=None):
    """
    Description:
    ------------
    CSS Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

      page.ui.codes.css('''
      .cssdivnoborder {margin: 0 ;clear: both ;padding: 0 ;border: 0 ;}
      .cssdivnoborder:focus {outline: 1px solid #B4BABF ;}
      ''')

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def xml(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
          profile=None):
    """
    Description:
    ------------
    XML Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'xml', 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def sql(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
          profile=None):
    """
    Description:
    ------------
    SQL Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'sql', 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dflt_options,
                                         helper, profile)
    return html_code

  @html.Html.css_skin()
  def r(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
        profile=None):
    """
    Description:
    ------------
    R Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {
      "lineNumbers": True, 'mode': 'r', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def python(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
             profile=None):
    """
    Description:
    ------------
    Python Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'python', 'styleActiveLine': True, 'autoRefresh': False}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text.strip(), color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def javascript(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None,
                 helper=None, profile=None):
    """
    Description:
    ------------
    Javascript Text editor.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'javascript', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dflt_options,
                                         helper, profile)
    return html_code

  @html.Html.css_skin()
  def markdown(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None,
               helper=None, profile=None):
    """
    Description:
    ------------
    Markdown Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'markdown', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code

  @html.Html.css_skin()
  def rst(self, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None, helper=None,
          profile=None):
    """
    Description:
    ------------
    RestructuredText editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'rst', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dflt_options,
                                         helper, profile)
    return html_code

  @html.Html.css_skin()
  def code(self, language, text="", color=None, width=(90, '%'), height=(200, 'px'), html_code=None, options=None,
           helper=None, profile=None):
    """
    Description:
    ------------
    Generic code editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage::

    Templates:

    Attributes:
    ----------
    :param language: String. The language.
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param html_code: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': language, 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dflt_options, helper, profile)
    return html_code
