#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Sliders:
  """
  Description:
  ------------
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

    - https://jqueryui.com/progressbar/
    - https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def slider(self, number=0, minimum=0, maximum=100, width=(100, '%'), height=(None, 'px'), html_code=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a Jquery UI slider object to the page

    Usage:
    -----

      page.ui.slider(40)
      page.ui.slider([1, 2, 3, 4, 5, 6, 7])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Slider`

    Related Pages:

      https://jqueryui.com/slider/

    Attributes:
    ----------
    :param number:
    :param minimum:
    :param maximum:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if isinstance(number, list):
      minimum, maximum = min(number), max(number)
      number = minimum
    html_slider = html.HtmlEvent.Slider(
      self.page, number, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    return html_slider

  @html.Html.css_skin()
  def date(self, value=None, min_val=None, max_val=None, width=(100, '%'), height=(20, 'px'), html_code=None,
           helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SliderDate`

    Attributes:
    ----------
    :param value:
    :param min_val:
    :param max_val:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    if value is None:
      value = min
    html_slider = html.HtmlEvent.SliderDate(
      self.page, value, min_val, max_val, width, height, helper, options or {}, html_code, profile)
    return html_slider

  @html.Html.css_skin()
  def date_range(self, value1=None, value2=None, min=None, max=None, width=(100, '%'), height=(20, 'px'),
                 html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.SliderDate`

    :param value1:
    :param value2:
    :param min:
    :param max:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = True
    if value1 is None:
      value1 = min
    if value2 is None:
      value2 = max
    html_slider = html.HtmlEvent.SliderDates(
      self.page, [value1, value2], min, max, width, height, helper, options or {}, html_code, profile)
    return html_slider

  @html.Html.css_skin()
  def range(self, values, min=0, max=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
            options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Range`

    :param values:
    :param min:
    :param max:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = True
    html_slider = html.HtmlEvent.Range(
      self.page, values, min, max, width, height, helper, options or {}, html_code, profile)
    return html_slider

  @html.Html.css_skin()
  def progressbar(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
                  options=None, profile=None):
    """
    Description:
    ------------
    Add a progress bar component to the page

    Usage:
    -----

      page.ui.sliders.progressbar(300)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.ProgressBar`

    Related Pages:

      https://jqueryui.com/progressbar/

    Attributes:
    ----------
    :param number: A number (by default between 0 and 100)
    :param total: A number
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.ProgressBar(
      self.page, number, total, width, height, helper, options or {}, html_code, profile)
    return html_pr

  @html.Html.css_skin()
  def progress(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
               options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param number:
    :param total:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    progress = self.progressbar(number, total, width, height, html_code, helper, options, profile)
    progress.style.css.border_radius = '50px'
    progress.style.css.background = self.page.theme.greys[4]
    progress.options.css({"border-radius": "50px", "border-color": self.page.theme.greys[5]})
    return progress
