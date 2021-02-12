#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Code(object):

  def __init__(self, context):
    self.context = context

  def css(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    CSS Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def xml(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    XML Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'xml', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def sql(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    SQL Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'sql', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def r(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    R Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'r', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def python(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Python Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'python', 'styleActiveLine': True, 'autoRefresh': False
                    }
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text.strip(), color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def javascript(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Javascript Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text
    :param color: String. Optional. The color code
    :param width: Tuple. Optional. The with details in the format(value, unit)
    :param height: Tuple. Optional. The height details in the format(value, unit)
    :param htmlCode: String. Optional. The unique component ID
    :param options: Dictionary. Optional. The object properties
    :param helper: String. Optional. The helper message
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'javascript', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def markdown(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Markdown Text editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text
    :param color: String. Optional. The color code
    :param width: Tuple. Optional. The with details in the format(value, unit)
    :param height: Tuple. Optional. The height details in the format(value, unit)
    :param htmlCode: String. Optional. The unique component ID
    :param options: Dictionary. Optional. The object properties
    :param helper: String. Optional. The helper message
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'markdown', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def rst(self, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    RestructuredText editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': 'rst', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code

  def code(self, language, text="", color=None, width=(90, '%'), height=(200, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Generic code editor.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Code`

    Related Pages:

      https://codemirror.net/index.html

    Usage:
    -----

    Templates:

    Attributes:
    ----------
    :param language: String. The language.
    :param text: String. Optional. The text.
    :param color: String. Optional. The color code.
    :param width: Tuple. Optional. The with details in the format(value, unit).
    :param height: Tuple. Optional. The height details in the format(value, unit).
    :param htmlCode: String. Optional. The unique component ID.
    :param options: Dictionary. Optional. The object properties.
    :param helper: String. Optional. The helper message.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"lineNumbers": True, 'mode': language, 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    return html_code
