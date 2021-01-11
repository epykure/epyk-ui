#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Slider(object):
  """
  Description:
  ------------
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

  Related Pages:

    https://jqueryui.com/progressbar/
    https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """

  def __init__(self, context):
    self.context = context

  def progressbar(self, number=0, total=100, label="", htmlCode=None):
    """
    The MDC Linear Progress component is a spec-aligned linear progress indicator component adhering to the Material Design progress & activity requirements.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param number:
    :param total:
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': None,
      'arias': {'role': 'progressbar', 'valuemin': 0, 'valuemax': 1, 'valuenow': number/total, 'label': label},
      'children': [
        {"type": 'div', 'class': 'mdc-linear-progress__buffering-dots', 'css': None},
        {"type": 'div', 'class': 'mdc-linear-progress__buffer', 'css': None},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__primary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__secondary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
    ]}
    html_pr = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})

    dom_obj = JsMdcComponents.LinearProgress(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    html_pr.onReady([html_pr.dom.setProgress(number)])
    return html_pr

  def slider(self, value=0, total=100, label="", htmlCode=None):
    """
    Description:
    ------------
    MDC Slider provides an implementation of the Material Design slider component.
    It is modeled after the browser’s <input type="range"> element. Sliders are fully RTL-aware, and conform to the WAI-ARIA slider authoring practices.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': None, 'attrs': {"tabindex": 0},
              'arias': {"role": 'slider', 'label': label, 'valuenow': value, 'valuemax': total, 'valuemin': 0}, 'children': [
        {"type": 'div', 'class': 'mdc-slider__track-container', 'css': None, 'children': [
          {"type": 'div', 'class': 'mdc-slider__track', 'css': None}
        ]},
        {"type": 'div', 'class': 'mdc-slider__thumb-container', 'css': None, 'children': [
          {"type": 'circle', 'class': 'mdc-slider__thumb', 'css': None,
           'args': {"x": 10.5, "y": 10.5, 'r': 7.875, "width": (21, "px"), "height": (21, "px")}}
        ]},
        #{"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
      ]

    }
    html_pr = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr

  def discrete(self, value=0, total=100, label="", htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': 'mdc-slider mdc-slider--discrete', 'css': None, 'attrs': {"tabindex": 0},
              'arias': {"role": 'slider', 'label': label, 'valuenow': value, 'valuemax': total, 'valuemin': 0},
              'children': [
                {"type": 'div', 'class': 'mdc-slider__track-container', 'css': None, 'children': [
                  {"type": 'div', 'class': 'mdc-slider__track', 'css': None}
                ]},
                {"type": 'div', 'class': 'mdc-slider__thumb-container', 'css': None, 'children': [
                  {"type": 'div', 'class': 'mdc-slider__pin', 'css': None, 'children': [
                    {"type": 'span', 'class': 'mdc-slider__pin-value-marker', 'css': None}
                  ]},
                  {"type": 'circle', 'class': 'mdc-slider__thumb', 'css': None,
                   'args': {"x": 10.5, "y": 10.5, 'r': 7.875, "width": (21, "px"), "height": (21, "px")}},
                  {"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
                ]},
                # {"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
              ]

              }
    html_pr = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr

  def tracker(self, value=0, total=100, label="", htmlCode=None):
    """
    Description:
    ------------
    Discrete sliders support display markers on their tracks by adding the mdc-slider--display-markers modifier class to mdc-slider, and <div class="mdc-slider__track-marker-container"></div> to the track container.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param htmlCode: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': 'mdc-slider mdc-slider--discrete mdc-slider--display-markers', 'css': None, 'attrs': {"tabindex": 0},
              'arias': {"role": 'slider', 'label': label, 'valuenow': value, 'valuemax': total, 'valuemin': 0},
              'children': [
                {"type": 'div', 'class': 'mdc-slider__track-container', 'css': None, 'children': [
                  {"type": 'div', 'class': 'mdc-slider__track', 'css': None},
                  {"type": 'div', 'class': 'mdc-slider__track-marker-container', 'css': None},
                ]},
                {"type": 'div', 'class': 'mdc-slider__thumb-container', 'css': None, 'children': [
                  {"type": 'div', 'class': 'mdc-slider__pin', 'css': None, 'children': [
                    {"type": 'span', 'class': 'mdc-slider__pin-value-marker', 'css': None}
                  ]},
                  {"type": 'circle', 'class': 'mdc-slider__thumb', 'css': None,
                   'args': {"x": 10.5, "y": 10.5, 'r': 7.875, "width": (21, "px"), "height": (21, "px")}},
                  {"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
                ]},
                # {"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
              ]

              }
    html_pr = self.context.rptObj.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr
