#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.py import types
from epyk.core.html import graph
from epyk.customs.data.html import HtmlProgress

from epyk.core.html import Defaults as defaults_html
from epyk.interfaces import Arguments


class Numbers:

    def __init__(self, ui):
        self.page = ui.page

    def digits(self, text: str = None, color: str = None, align: str = 'center', width: types.SIZE_TYPE = None,
               height: types.SIZE_TYPE = None, html_code: str = None, tooltip: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Position:
        """The <span> tag is used to group inline-elements in a document.

        The <span> tag provides no visual change by itself.

        The <span> tag provides a way to add a hook to a part of a text or a part of a document.

        :tags:
        :categories:

        Usage::

          page.ui.texts.span("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Position`

        `w3schools <https://www.w3schools.com/tags/tag_span.asp>`_
        `Templates numbers <https://github.com/epykure/epyk-templates/blob/master/locals/components/numbers.py>`_

        :param text: Optional. The string value to be displayed in the component
        :param color: Optional. The color of the text
        :param align: Optional. The position of the icon in the line (left, right, center)
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param tooltip: Optional. A string with the value of the tooltip
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        if width is None:
            width = (defaults_html.TEXTS_SPAN_WIDTH, 'px')
        if height is None:
            height = (defaults_html.LINE_HEIGHT, 'px')
        html_label = html.HtmlText.Position(
            self.page, text, color, align, width, height, html_code, tooltip, options, profile)
        html_label.position(3, {"font-size": self.page.body.style.globals.font.normal(5), "font-weight": "bold"})
        html_label.position(4, {"font-size": self.page.body.style.globals.font.normal(5), "font-weight": "bold"})
        html_label.digits(True)
        html.Html.set_component_skin(html_label)
        return html_label

    def number(self, number: float = 0, title: str = None, label: str = None, icon: int = None, color: str = None,
               tooltip: str = None, html_code: str = None, options: dict = None, helper: str = None,
               width: types.SIZE_TYPE = (100, '%'), align: str = "center",
               profile: types.PROFILE_TYPE = None) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The color of the value
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {"digits": 0, "thousand_sep": ',', "decimal_sep": '.'}
        if options is not None:
            dflt_options.update(options)
        html_number = html.HtmlText.Numeric(
            self.page, number, title, label, icon, color, tooltip, html_code, dflt_options, helper, width, profile)
        html_number.style.css.text_align = align
        html_number.style.css.font_factor(5)
        html.Html.set_component_skin(html_number)
        return html_number

    def percent(self, number: float = 0, title: str = None, label: str = None, icon: str = None, color: str = None,
                tooltip: str = None, html_code: str = None, options: str = None,
                helper: str = None, width: types.SIZE_TYPE = (100, '%'), align: str = "center",
                profile: types.PROFILE_TYPE = None) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.percent(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The color of the value
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: Optional. The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                                  profile)
        html_number.money("%", fmt="%v%s")
        html.Html.set_component_skin(html_number)
        return html_number

    def pound(self, number: float = 0, title: str = None, label: str = None, icon: str = None, color: str = None,
              tooltip: str = None, html_code: str = None, options: dict = None, helper: str = None,
              width: types.SIZE_TYPE = (100, '%'), align: str = "center", profile: types.PROFILE_TYPE = None
              ) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.pound(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The font color in the component. Default inherit
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: Optional. The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                                  profile)
        html_number.money("£")
        html.Html.set_component_skin(html_number)
        return html_number

    def euro(self, number: float = 0, title: str = None, label: str = None, icon: str = None, color: str = None,
             tooltip: str = None, html_code: str = None, options: dict = None, helper: str = None,
             width: types.SIZE_TYPE = (100, '%'), align: str = "center", profile: types.PROFILE_TYPE = None
             ) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.euro(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The font color in the component. Default inherit
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: Optional. The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                                  profile)
        html_number.money("€", fmt="%v %s")
        html.Html.set_component_skin(html_number)
        return html_number

    def dollar(self, number: float = 0, title: str = None, label: str = None, icon: str = None, color: str = None,
               tooltip: str = None, html_code: str = None, options: dict = None, helper: str = None,
               width: types.SIZE_TYPE = (100, '%'), align: str = "center",
               profile: types.PROFILE_TYPE = None
               ) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.dollar(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The font color in the component. Default inherit
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: Optional. The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                                  profile)
        html_number.money("$", fmt="%v %s")
        html.Html.set_component_skin(html_number)
        return html_number

    def money(self, symbol: str, number: float = 0, title: str = None, label: str = None, icon: str = None,
              color: str = None, tooltip: str = None, html_code: str = None,
              options: dict = None, helper: str = None, width: types.SIZE_TYPE = (100, '%'),
              align: str = "center", profile: types.PROFILE_TYPE = None
              ) -> html.HtmlText.Numeric:
        """

        :tags:
        :categories:

        Usage::

          page.ui.texts.money(289839898, label="test", helper="Ok", icon="fas fa-align-center")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlText.Numeric`

        :param symbol: The currency symbol
        :param number: Optional. The value to be displayed to the component. Default now
        :param title: Optional. A panel title. This will be attached to the title property
        :param label: Optional. The text of label to be added to the component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param color: Optional. The font color in the component. Default inherit
        :param tooltip: Optional. A string with the value of the tooltip
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param align: Optional. The text-align property within this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_number = self.number(
            number, title, label, icon, color, tooltip, html_code, options, helper, width, align, profile)
        html_number.money(symbol, fmt="%v %s")
        html.Html.set_component_skin(html_number)
        return html_number

    def plotly(self, value: float = 0, profile: types.PROFILE_TYPE = None, options: dict = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
               html_code: str = None) -> graph.GraphPlotly.Indicator:
        """

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.graph.GraphPlotly.Indicator`

        :param value: Optional. Number. a value
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        ind = graph.GraphPlotly.Indicator(self.page, width, height, options or {}, html_code, profile)
        ind.add_trace({'value': value}, mode="number")
        html.Html.set_component_skin(ind)
        return ind

    def plotly_with_delta(self, value, profile: types.PROFILE_TYPE = None, options: dict = None,
                          width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (330, "px"),
                          html_code: str = None) -> graph.GraphPlotly.Indicator:
        """

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.graph.GraphPlotly.Indicator`

        :param value: Number. a value
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        ind = graph.GraphPlotly.Indicator(self.page, width, height, options or {}, html_code, profile)
        ind.add_trace({'value': value}, mode="number+delta")
        html.Html.set_component_skin(ind)
        return ind

    def move(self, current, previous=None, components=None, title: str = None, align: str = "center",
             width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, "px"), color: str = None,
             label: str = None, options: dict = None, helper: str = None, profile: types.PROFILE_TYPE = None
             ) -> html.HtmlTextComp.UpDown:
        """

        :tags:
        :categories:

        Usage::

          page.ui.numbers.move(100, 60, helper="test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextComp.Delta`

        :param current: The current value
        :param previous: Optional. Default the current value and not move
        :param components: Optional. List of HTML component to be added
        :param title: Optional. The title definition
        :param align: Optional. The text-align property within this component
        :param color: Optional. The text color
        :param label: Optional. The label for the up and down component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. The value to be displayed to the helper icon
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                        'red': self.page.theme.danger.base, 'green': self.page.theme.success.base,
                        'orange': self.page.theme.warning.base}
        previous = previous or current
        if options is not None:
            dflt_options.update(options)
        components = components or []
        if title is not None:
            if not hasattr(title, 'options'):
                title = self.page.ui.titles.title(title)
                title.style.css.display = "block"
                title.style.css.text_align = align
            components.insert(0, title)
        html_up_down = html.HtmlTextComp.UpDown(
            self.page, {"value": current, 'previous': previous}, components, color, label, width, height, dflt_options,
            helper, profile)
        if title is not None:
            html_up_down.title = title
        html.Html.set_component_skin(html_up_down)
        return html_up_down

    def progress(self, value: float = 0, width: types.SIZE_TYPE = (90, 'px'), height: types.SIZE_TYPE = (None, "px"),
                 html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        options = options or {}
        if options.get("half", False):
            if height[0] is None:
                height = (width[0] / 2, width[1])
            return HtmlProgress.Gauge(
                value, page=self.page, width=width, height=height, html_code=html_code, options=options,
                profile=profile)

        if height[0] is None:
            height = width
        return HtmlProgress.Circle(
            value, page=self.page, width=width, height=height, html_code=html_code, options=options, profile=profile)
