#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://bl.ocks.org/ctufts/f38ef0187f98c537d791d24fda4a6ef9

from epyk.core.html import Html
from epyk.core.js import JsUtils


class Script(Html.Html):
  name = 'D3 Script'

  def __init__(self, report, data, width, height, html_code, options, profile):
    super(Script, self).__init__(report, data, html_code=html_code, profile=profile,
                                 css_attrs={"width": width, "height": height})
    self._js__builder__ = ""
    self._jsStyles.update(options)
    self._jsStyles.update({"wdith": width[0], "height": height[0]})

  def data(self, data):
    if not isinstance(data, list):
      data = data.split(" ")
    self._vals = data

  def loader(self, str_frg):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str_frg:
    """
    self.builder_name = "D3Builder%s" % self.page.py.hash(str_frg)
    self._js__builder__ = str_frg

  def build(self, data=None, options=None, profile=False, component_id=None):
    return super().build(data, options, profile, component_id=self.dom.d3.varId)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
