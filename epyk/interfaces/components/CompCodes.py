#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core import html
from epyk.interfaces import Arguments


class Code:

  def __init__(self, ui):
    self.page = ui.page

  def css(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
          height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
          options: Optional[dict] = None, helper: Optional[str] = None,
          profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {
      "lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def xml(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
          height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
          options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
          profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {
      "lineNumbers": True, 'mode': 'xml', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(
      self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def sql(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
          height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
          options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
          profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {
      "lineNumbers": True, 'mode': 'sql', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def r(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
        height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
        options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
        profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {
      "lineNumbers": True, 'mode': 'r', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def python(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
             height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
             options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
             profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"lineNumbers": True, 'mode': 'python', 'styleActiveLine': True, 'autoRefresh': False}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(
      self.page, text.strip(), color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def javascript(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
                 height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
                 options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
                 profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"lineNumbers": True, 'mode': 'javascript', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def markdown(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
               height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
               options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
               profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"lineNumbers": True, 'mode': 'markdown', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def rst(self, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
          height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
          options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
          profile: Optional[Union[dict, bool]] = None):
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
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"lineNumbers": True, 'mode': 'rst', 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component

  def code(self, language: str, text: str = "", color: Union[str, bool] = None, width: Union[tuple, int] = (90, '%'),
           height: Union[tuple, int] = (200, 'px'), html_code: Optional[str] = None,
           options: Optional[Union[dict, bool]] = None, helper: Optional[str] = None,
           profile: Optional[Union[dict, bool]] = None):
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
    :param str language: The language.
    :param str text: Optional. The text.
    :param Union[str, bool] color: Optional. The color code.
    :param Union[tuple, int] width: Optional. The with details in the format(value, unit).
    :param Union[tuple, int] height: Optional. The height details in the format(value, unit).
    :param Optional[str] html_code: Optional. The unique component ID.
    :param Optional[Union[dict, bool]] options: Optional. The object properties.
    :param Optional[str] helper: Optional. The helper.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"lineNumbers": True, 'mode': language, 'autoRefresh': True, 'styleActiveLine': True}
    if options is not None:
      dfl_options.update(options)
    component = html.HtmlTextEditor.Code(self.page, text, color, width, height, html_code, dfl_options, helper, profile)
    html.Html.set_component_skin(component)
    return component
