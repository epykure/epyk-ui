#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Sliders(object):
  """
  Description:
  ------------
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

    - https://jqueryui.com/progressbar/
    - https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, context):
    self.context = context

  def slider(self, number=0, minimum=0, maximum=100, width=(100, '%'), height=(None, 'px'), htmlCode=None, attrs=None,
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
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if isinstance(number, list):
      minimum, maximum = min(number), max(number)
      number = minimum
    html_slider = html.HtmlEvent.Slider(self.context.rptObj, number, minimum, maximum, width, height,  attrs or {}, helper,
                                        options or {}, htmlCode, profile)
    return html_slider

  def date(self, value=None, min=None, max=None, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
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
    :param min:
    :param max:
    :param width:
    :param height:
    :param htmlCode:
    :param attrs:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    if value is None:
      value = min
    html_slider = html.HtmlEvent.SliderDate(self.context.rptObj, value, min, max, width, height, attrs or {}, helper,
                                            options or {}, htmlCode, profile)
    return html_slider

  def date_range(self, value1=None, value2=None, min=None, max=None, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                 helper=None, options=None, profile=None):
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
    :param htmlCode:
    :param attrs:
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
    html_slider = html.HtmlEvent.SliderDates(self.context.rptObj, [value1, value2], min, max, width, height, attrs or {}, helper,
                                             options or {}, htmlCode, profile)
    return html_slider

  def range(self, values, min=0, max=100, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
             helper=None, options=None, profile=None):
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
    :param htmlCode:
    :param attrs:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    options['range'] = True
    html_slider = html.HtmlEvent.Range(self.context.rptObj, values, min, max, width, height, attrs or {}, helper,
                                         options or {}, htmlCode, profile)
    return html_slider

  def progressbar(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
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
    :param htmlCode:
    :param attrs:
    :param helper:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.ProgressBar(self.context.rptObj, number, total, width, height,  attrs or {}, helper,
                                         options or {}, htmlCode, profile)
    return html_pr

  def progress(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
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
    :param htmlCode:
    :param attrs:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    progress = self.progressbar(number, total, width, height, htmlCode, attrs, helper, options, profile)
    progress.style.css.border_radius = '50px'
    progress.style.css.background = self.context.rptObj.theme.greys[4]
    progress.options.css({"border-radius": "50px", "border-color": self.context.rptObj.theme.greys[5]})
    return progress
