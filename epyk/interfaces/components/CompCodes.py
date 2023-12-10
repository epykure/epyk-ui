#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core import html
from epyk.core.py import types
from epyk.interfaces import Arguments


class Code:

    def __init__(self, ui):
        self.page = ui.page

    def css(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
            height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
            options: types.OPTION_TYPE = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """CSS Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        Usage::

          page.ui.codes.css('''
          .cssdivnoborder {margin: 0 ;clear: both ;padding: 0 ;border: 0 ;}
          .cssdivnoborder:focus {outline: 1px solid #B4BABF ;}
          ''')

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {
            "lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def xml(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
            height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
            options: types.OPTION_TYPE = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """XML Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {
            "lineNumbers": True, 'mode': 'xml', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def sql(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
            height: types.SIZE_TYPE = (200, 'px'), html_code: Optional[str] = None,
            options: types.OPTION_TYPE = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """SQL Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {
            "lineNumbers": True, 'mode': 'sql', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def r(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
          height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
          options: types.OPTION_TYPE = None, helper: str = None,
          profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """R Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {
            "lineNumbers": True, 'mode': 'r', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def python(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
               height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
               options: types.OPTION_TYPE = None, helper: str = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """Python Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"lineNumbers": True, 'mode': 'python', 'styleActiveLine': True, 'autoRefresh': False}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text.strip(), color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def javascript(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
                   height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
                   options: types.OPTION_TYPE = None, helper: str = None,
                   profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """Javascript Text editor.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"lineNumbers": True, 'mode': 'javascript', 'autoRefresh': True, 'styleActiveLine': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def markdown(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
                 height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
                 options: types.OPTION_TYPE = None, helper: str = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """Markdown Text editor.

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"lineNumbers": True, 'mode': 'markdown', 'autoRefresh': True, 'styleActiveLine': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def rst(self, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
            height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
            options: types.OPTION_TYPE = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """RestructuredText editor.

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"lineNumbers": True, 'mode': 'rst', 'autoRefresh': True, 'styleActiveLine': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component

    def code(self, language: str, text: str = "", color: Union[str, bool] = None, width: types.SIZE_TYPE = (90, '%'),
             height: types.SIZE_TYPE = (200, 'px'), html_code: str = None,
             options: types.OPTION_TYPE = None, helper: str = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.CodeEditor:
        """Generic code editor.

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Code`

        `codemirror <https://codemirror.net/index.html>`_

        :param language: The language
        :param text: Optional. The text
        :param color: Optional. The color code
        :param width: Optional. The with details in the format(value, unit)
        :param height: Optional. The height details in the format(value, unit)
        :param html_code: Optional. The unique component ID
        :param options: Optional. The object properties
        :param helper: Optional. The helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"lineNumbers": True, 'mode': language, 'autoRefresh': True, 'styleActiveLine': True}
        if options is not None:
            dfl_options.update(options)
        component = html.HtmlTextEditor.CodeEditor(
            self.page, text, color, width, height, html_code, dfl_options, helper, profile)
        html.Html.set_component_skin(component)
        return component
