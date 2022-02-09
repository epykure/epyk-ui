#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options
from epyk.core.html.options import OptChart


class D3GgeographyConfig(Options):

  @property
  def popupOnHover(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @popupOnHover.setter
  def popupOnHover(self, flag):
    self._config(flag)

  @property
  def hideAntarctica(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @hideAntarctica.setter
  def hideAntarctica(self, flag):
    self._config(flag)

  @property
  def hideHawaiiAndAlaska(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @hideHawaiiAndAlaska.setter
  def hideHawaiiAndAlaska(self, flag):
    self._config(flag)

  @property
  def highlightOnHover(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @highlightOnHover.setter
  def highlightOnHover(self, flag):
    self._config(flag)

  @property
  def highlightBorderColor(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @highlightBorderColor.setter
  def highlightBorderColor(self, color):
    self._config(color)

  def highlightFillColor(self, js_funcs, profile=None):
    raise NotImplementedError()

  @property
  def borderColor(self):
    """
    Description:
    ------------

    """
    return self._config_get('#444')

  @borderColor.setter
  def borderColor(self, color):
    self._config(color)

  @property
  def borderOpacity(self):
    """
    Description:
    ------------

    """
    return self._config_get(1)

  @borderOpacity.setter
  def borderOpacity(self, num):
    self._config(num)

  @property
  def borderWidth(self):
    """
    Description:
    ------------

    """
    return self._config_get(0.5)

  @borderWidth.setter
  def borderWidth(self, num):
    self._config(num)

  @property
  def dataUrl(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @dataUrl.setter
  def dataUrl(self, url):
    self._config(url)

  def popupTemplate(self, js_funcs, profile=None):
    raise NotImplementedError()


class D3GgeographyBubbleConfig(D3GgeographyConfig):

  @property
  def animate(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @animate.setter
  def animate(self, flag):
    self._config(flag)

  @property
  def radius(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @radius.setter
  def radius(self, num):
    self._config(num)

  @property
  def fillOpacity(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @fillOpacity.setter
  def fillOpacity(self, num):
    self._config(num)

  @property
  def exitDelay(self):
    """
    Description:
    ------------

    """
    return self._config_get(100)

  @exitDelay.setter
  def exitDelay(self, num):
    self._config(num)

  @property
  def key(self):
    """
    Description:
    ------------

    """
    return self._config_get("JSON.stringify")

  @key.setter
  def key(self, value):
    self._config(value, js_type=True)


class D3ArcConfig(Options):

  @property
  def strokeColor(self):
    """
    Description:
    ------------

    """
    return self._config_get('#DD1C77')

  @strokeColor.setter
  def strokeColor(self, color):
    self._config(color)

  @property
  def strokeWidth(self):
    """
    Description:
    ------------

    """
    return self._config_get(1)

  @strokeWidth.setter
  def strokeWidth(self, num):
    self._config(num)

  @property
  def arcSharpness(self):
    """
    Description:
    ------------

    """
    return self._config_get(1)

  @arcSharpness.setter
  def arcSharpness(self, num):
    self._config(num)

  @property
  def animationSpeed(self):
    """
    Description:
    ------------

    """
    return self._config_get(600)

  @animationSpeed.setter
  def animationSpeed(self, num):
    self._config(num)

  @property
  def popupOnHover(self):
    """
    Description:
    ------------

    """
    return self._config_get(False)

  @popupOnHover.setter
  def popupOnHover(self, flag):
    self._config(flag)

  def popupTemplate(self, js_funcs, profile=None):
    raise NotImplementedError()


class ChartGeo(OptChart.OptionsChart):

  @property
  def element(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @element.setter
  def element(self, component):
    self._config(component, js_type=True)

  @property
  def dataType(self):
    """
    Description:
    ------------

    """
    return self._config_get("json")

  @dataType.setter
  def dataType(self, value):
    self._config(value)

  @property
  def dataUrl(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @dataUrl.setter
  def dataUrl(self, url):
    self._config(url)

  @property
  def reponsive(self):
    """
    Description:
    ------------

    """
    return self._config_get(True)

  @reponsive.setter
  def reponsive(self, flag):
    self._config(flag)

  @property
  def scope(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @scope.setter
  def scope(self, value):
    self._config(value)

  @property
  def geographyConfig(self) -> D3GgeographyConfig:
    return self._config_sub_data("geographyConfig", D3GgeographyConfig)

  @property
  def bubblesConfig(self) -> D3GgeographyBubbleConfig:
    return self._config_sub_data("bubblesConfig", D3GgeographyBubbleConfig)

  @property
  def projection(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @projection.setter
  def projection(self, value):
    self._config(value)

  def setProjection(self, js_funcs, profile=None):
    raise NotImplementedError()

  def done(self, js_funcs, profile=None):
    raise NotImplementedError()
