#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChart


class FrappeLine(Options):
  component_properties = ("data",)

  @property
  def height(self):
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def data(self):
    return self._config_get([])

  @data.setter
  def data(self, flag):
    self._config(flag)

  @property
  def colors(self):
    return self._config_get()

  @colors.setter
  def colors(self, colors):
    self._config(colors)
