#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.interfaces import Arguments


class Steppers(object):

  def __init__(self, context):
    self.context = context

  def stepper(self, records, width=(100, '%'), height=(70, 'px'), color=None, options=None):
    """
    Description:
    ------------
    Entry point for the stepper object

    Usage::

      rptObj.ui.stepper([
        {"value": 'test 1', "status": 'success', 'label': 'test'},
        {"value": 'test 2', "status": 'error'},
        {"value": 'test 3', "status": 'pending'}])

    Attributes:
    ----------
    :param records: A list with the different steps defined in the workflow
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional.
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"line": True}
    if options is not None:
      dft_options.update(options)
    st = html.HtmlStepper.Stepper(self.context.rptObj, records, width, height, color, dft_options)
    st.style.add_classes.div.stepper()
    st.style.css_class.media({'.cssdivstepper li': {"float": None, 'width': '100%'},
                               '.cssdivstepper li line': {'stroke-width': 0},
                               '.cssdivstepper li [name=label]': {'width': '100%!IMPORTANT'}}, 'only', 'screen',
                              {"and": [{'max-width': '600px'}]})
    return st

  def arrow(self, records, width=(100, '%'), height=(70, 'px'), color=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param color:
    :param options:
    """
    dft_options = {"shape": 'arrow'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options)

  def rectangle(self, records, width=(100, '%'), height=(70, 'px'), color=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param color:
    :param options:
    """
    dft_options = {"shape": 'rectangle'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options)

  def triangle(self, records, width=(100, '%'), height=(70, 'px'), color=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param color:
    :param options:
    """
    dft_options = {"shape": 'rectangle'}
    if options is not None:
      dft_options.update(options)
    return self.stepper(records, width, height, color, dft_options)

  def vertical(self, records, shape='circle',  width=(100, '%'), height=(70, 'px'), color=None, options=None):
    """
    Description:
    ------------
    Entry point for the stepper object

    Usage::

      rptObj.ui.stepper([
        {"value": 'test 1', "status": 'success', 'label': 'test'},
        {"value": 'test 2', "status": 'error'},
        {"value": 'test 3', "status": 'pending'}])

    Attributes:
    ----------
    :param records: A list with the different steps defined in the workflow
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional.
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"line": False, "shape": shape}
    if options is not None:
      dft_options.update(options)
    st = html.HtmlStepper.Stepper(self.context.rptObj, records, width, height, color, dft_options)
    return st
