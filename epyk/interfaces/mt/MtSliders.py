#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Slider:
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

  def __init__(self, ui):
    self.page = ui.page

  def progressbar(self, number=0, total=100, label="", html_code=None):
    """
    The MDC Linear Progress component is a spec-aligned linear progress indicator component adhering to the Material
    Design progress & activity requirements.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param number:
    :param total:
    :param label:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': {},
      'arias': {'role': 'progressbar', 'valuemin': 0, 'valuemax': 1, 'valuenow': number/total, 'label': label},
      'children': [
        {"type": 'div', 'class': 'mdc-linear-progress__buffering-dots', 'css': None},
        {"type": 'div', 'class': 'mdc-linear-progress__buffer', 'css': None},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__primary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__secondary-bar',
         'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
    ]}
    html_pr = self.page.web.mt.composite(schema, options={"reset_class": True})

    dom_obj = JsMdcComponents.LinearProgress(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    html_pr.onReady([html_pr.dom.setProgress(number)])
    return html_pr

  def slider(self, value=0, total=100, label="", html_code=None):
    """
    Description:
    ------------
    MDC Slider provides an implementation of the Material Design slider component.
    It is modeled after the browser’s <input type="range"> element. Sliders are fully RTL-aware, and conform to the WAI-
    ARIA slider authoring practices.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': None, 'attrs': {"tabindex": 0}, 'class': "mdc-slider",
              'arias': {"role": 'slider', 'label': label, 'valuenow': value, 'valuemax': total, 'valuemin': 0},
              'children': [
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
    html_pr = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr

  def continuous(self, value=0, total=100, label="", html_code=None):
    """
    Description:
    ------------
    Continuous sliders allow users to make meaningful selections that don’t require a specific value.

    Note: The step size for value quantization is, by default, 1.
    To specify a custom step size, provide a value for the step attribute on the input element.

    Related Pages:

      https://material.io/components/sliders/web#sliders

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'css': None, 'class': "mdc-slider", 'children': [
        {"type": 'input', "class": "mdc-slider__input",
         'attrs': {"type": "range", "min": 0, "max": 100}, 'css': False, 'args': {'text': value}},
        {"type": 'div', 'class': 'mdc-slider__track', 'css': None, 'children': [
          {"type": 'div', 'class': 'mdc-slider__track--inactive', 'css': None},
          {"type": 'div', 'class': 'mdc-slider__track--active', 'css': None, 'children': [
            {"type": 'div', 'class': 'mdc-slider__track--active_fill', 'css': None},
          ]},
        ]},

        {"type": 'div', 'class': 'mdc-slider__thumb', 'css': None, 'children': [
          {"type": 'div', 'class': 'mdc-slider__thumb-knob', 'css': None},
        ]}]}
    html_pr = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr

  def discrete(self, value=0, total=100, label="", html_code=None):
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
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
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
    html_pr = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr

  def tracker(self, value=0, total=100, label="", html_code=None):
    """
    Description:
    ------------
    Discrete sliders support display markers on their tracks by adding the mdc-slider--display-markers modifier class
    to mdc-slider, and <div class="mdc-slider__track-marker-container"></div> to the track container.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param value:
    :param total:
    :param label:
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    """
    schema = {"type": 'div', 'class': 'mdc-slider mdc-slider--discrete mdc-slider--display-markers', 'css': None,
              'attrs': {"tabindex": 0},
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
    html_pr = self.page.web.mt.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.Slider(html_pr)
    html_pr.style.builder(html_pr.style.varName, dom_obj.instantiate("#%s" % html_pr.htmlCode))
    # Add the specific dom features
    html_pr.dom = dom_obj
    return html_pr
