#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.html import graph

from epyk.core.html import Defaults as defaults_html
from epyk.interfaces import Arguments


class Numbers:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def digits(self, text=None, color=None, align='center', width=None, height=None, html_code=None, tooltip=None,
             options=None, profile=None):
    """
    Description:
    ------------
    The <span> tag is used to group inline-elements in a document.

    The <span> tag provides no visual change by itself.

    The <span> tag provides a way to add a hook to a part of a text or a part of a document.

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.span("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Position`

    Related Pages:

      https://www.w3schools.com/tags/tag_span.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/numbers.py

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    if width is None:
      width = (defaults_html.TEXTS_SPAN_WIDTH, 'px')
    if height is None:
      height = (defaults_html.LINE_HEIGHT, 'px')
    html_label = html.HtmlText.Position(self.page, text, color, align, width, height, html_code, tooltip,
                                        options, profile)
    html_label.position(3, {"font-size": self.page.body.style.globals.font.normal(5), "font-weight": "bold"})
    html_label.position(4, {"font-size": self.page.body.style.globals.font.normal(5), "font-weight": "bold"})
    html_label.digits(True)
    return html_label

  @html.Html.css_skin()
  def number(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None,
             options=None, helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.number(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The color of the value.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"digits": 0, "thousand_sep": ',', "decimal_sep": '.'}
    if options is not None:
      dflt_options.update(options)
    html_number = html.HtmlText.Numeric(
      self.page, number, title, label, icon, color, tooltip, html_code, dflt_options, helper, width, profile)
    html_number.style.css.text_align = align
    html_number.style.css.font_factor(5)
    return html_number

  @html.Html.css_skin()
  def percent(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None, options=None,
              helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.percent(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The color of the value.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                              profile)
    html_number.money("%", fmt="%v%s")
    return html_number

  @html.Html.css_skin()
  def pound(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None,
            options=None, helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.pound(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                              profile)
    html_number.money("£")
    return html_number

  @html.Html.css_skin()
  def euro(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None, options=None,
           helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.euro(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                              profile)
    html_number.money("€", fmt="%v %s")
    return html_number

  @html.Html.css_skin()
  def dollar(self, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None,
             options=None, helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.dollar(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                              profile)
    html_number.money("$", fmt="%v %s")
    return html_number

  @html.Html.css_skin()
  def money(self, symbol, number=0, title=None, label=None, icon=None, color=None, tooltip='', html_code=None,
            options=None, helper=None, width=(100, '%'), align="center", profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.texts.money(289839898, label="test", helper="Ok", icon="fas fa-align-center")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Numeric`

    Attributes:
    ----------
    :param symbol: String. The currency symbol.
    :param number: Number. Optional. The value to be displayed to the component. Default now.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param align: String. The text-align property within this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_number = self.number(number, title, label, icon, color, tooltip, html_code, options, helper, width, align,
                              profile)
    html_number.money(symbol, fmt="%v %s")
    return html_number

  @html.Html.css_skin()
  def plotly(self, value, profile=None, options=None, width=(100, "%"), height=(330, "px"),
             html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.graph.GraphPlotly.Indicator`

    Attributes:
    ----------
    :param value: Number. a value.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    ind = graph.GraphPlotly.Indicator(self.page, width, height, options or {}, html_code, profile)
    ind.add_trace({'value': value}, mode="number")
    return ind

  @html.Html.css_skin()
  def plotly_with_delta(self, value, profile=None, options=None, width=(100, "%"),
                        height=(330, "px"), html_code=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----


    Underlying HTML Objects:

      - :class:`epyk.core.graph.GraphPlotly.Indicator`

    Attributes:
    ----------
    :param value: Number. a value.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    ind = graph.GraphPlotly.Indicator(self.page, width, height, options or {}, html_code, profile)
    ind.add_trace({'value': value}, mode="number+delta")
    return ind

  @html.Html.css_skin()
  def move(self, current, previous=None, components=None, title=None, align="center", width=(100, '%'),
           height=(None, "px"), color=None, label=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.numbers.move(100, 60, helper="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Delta`

    Attributes:
    ----------
    :param current: Number. The current value.
    :param previous: Number. Optional. Default the current value and not move.
    :param components: HTML Component. Optional. List of HTML component to be added.
    :param title: String | Component. Optional. The title definition.
    :param align: String. Optional. The text-align property within this component.
    :param color: String. Optional. The text color.
    :param label: String. Optional. The label for the up and down component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'red': self.page.theme.danger[1], 'green': self.page.theme.success[1],
                    'orange': self.page.theme.warning[1]}
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
    return html_up_down
