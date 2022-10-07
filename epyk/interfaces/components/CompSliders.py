#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.py import types


class Sliders:
  """  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

    - https://jqueryui.com/progressbar/
    - https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, ui):
    self.page = ui.page

  def slider(self, number: float = 0, minimum: float = 0, maximum: float = 100, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Add a Jquery UI slider object to the page

    Usage::

      page.ui.slider(40)
      page.ui.slider([1, 2, 3, 4, 5, 6, 7])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Slider`

    Related Pages:

      https://jqueryui.com/slider/

    :param number: Optional. The initial value
    :param minimum: Optional. The min value. Default 0
    :param maximum: Optional. The max value. Default 100
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if isinstance(number, list):
      minimum, maximum = min(number), max(number)
      number = minimum
    html_slider = html.HtmlEvent.Slider(
      self.page, number, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def date(self, value=None, minimum: float = None, maximum: float = None, width: types.SIZE_TYPE = (100, '%'),
           height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
           options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SliderDate`

    :param value: Optional. The initial value
    :param minimum: Optional. The min value
    :param maximum: Optional. The max value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    if value is None:
      value = minimum
    html_slider = html.HtmlEvent.SliderDate(
      self.page, value, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def date_range(self, value1: str = None, value2: str = None, minimum: float = None, maximum: float = None,
                 width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (20, 'px'),
                 html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None):
    """

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SliderDate`

    :param value1: Optional. The initial min value
    :param value2: Optional. The initial max value
    :param minimum: Optional. The min value
    :param maximum: Optional. The max value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = True
    if value1 is None:
      value1 = minimum
    if value2 is None:
      value2 = maximum
    html_slider = html.HtmlEvent.SliderDates(
      self.page, [value1, value2], minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def range(self, values=None, minimum: float = 0, maximum: float = 100, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Range`

    :param values: Optional. The initial values
    :param minimum: Optional. The min value. Default 0
    :param maximum: Optional. The max value. Default 100
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    values = values or [minimum, maximum]
    options['range'] = True
    html_slider = html.HtmlEvent.Range(
      self.page, values, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def upper(self, value=None, minimum: float = 0, maximum: float = 100, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Range`

    :param value: Optional. The initial value
    :param minimum: Optional. The min value. Default 0
    :param maximum: Optional. The max value. Default 100
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = 'max'
    html_slider = html.HtmlEvent.Slider(
      self.page, value or 0, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def lower(self, value=None, minimum: float = 0, maximum: float = 100, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Range`

    :param value: Optional. The initial value
    :param minimum: Optional. The min value. Default 0
    :param maximum: Optional. The max value. Default 100
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = 'min'
    html_slider = html.HtmlEvent.Slider(
      self.page, value or 0, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_slider)
    return html_slider

  def progressbar(self, number: float = 0, total: float = 100, width: types.SIZE_TYPE = (100, '%'),
                  height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
                  options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Add a progress bar component to the page

    Usage::

      page.ui.sliders.progressbar(300)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.ProgressBar`

    Related Pages:

      https://jqueryui.com/progressbar/

    :param number: Optional. The initial value
    :param total: Optional. The total value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.ProgressBar(
      self.page, number, total, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_pr)
    return html_pr

  def progress(self, number: float = 0, total: float = 100, width: types.SIZE_TYPE = (100, '%'),
               height: types.SIZE_TYPE = (20, 'px'), html_code: str = None, helper: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """

    Usage::

    :param number: Optional. The initial value
    :param total: Optional. The total value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    progress = self.progressbar(number, total, width, height, html_code, helper, options, profile)
    progress.style.css.border_radius = '50px'
    progress.style.css.background = self.page.theme.greys[4]
    progress.options.css({"border-radius": "50px", "border-color": self.page.theme.greys[5]})
    html.Html.set_component_skin(progress)
    return progress
