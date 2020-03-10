
from epyk.core.html.graph import GraphPlotly

from epyk.core.js.packages import JsPlotly


class LayoutCenter(GraphPlotly.Layout):

  @property
  def lat(self):
    return self._attrs["lat"]

  @lat.setter
  def lat(self, val):
    self._attrs["lat"] = val

  @property
  def lon(self):
    return self._attrs["lon"]

  @lon.setter
  def lon(self, val):
    self._attrs["lon"] = val


class LayoutMapBox(GraphPlotly.Layout):

  @property
  def style(self):
    return self._attrs["style"]

  @style.setter
  def style(self, val):
    self._attrs["style"] = val

  @property
  def zoom(self):
    return self._attrs["zoom"]

  @zoom.setter
  def zoom(self, val):
    self._attrs["zoom"] = val

  @property
  def center(self):
    """

    :rtype: LayoutCenter
    """
    return self.sub_data("center", LayoutCenter)


class LayoutGeo(GraphPlotly.Layout):

  @property
  def dragmode(self):
    return self._attrs["dragmode"]

  @dragmode.setter
  def dragmode(self, val):
    self._attrs["dragmode"] = val

  @property
  def mapboxAccessToken(self):
    return self._attrs["mapboxAccessToken"]

  @mapboxAccessToken.setter
  def mapboxAccessToken(self, val):
    self._attrs["mapboxAccessToken"] = val

  @property
  def mapbox(self):
    """

    :rtype: LayoutMapBox
    """
    return self.sub_data("mapbox", LayoutMapBox)


class DataScatterMapBox(GraphPlotly.DataChart):

  @property
  def lon(self):
    return self._attrs["lon"]

  @lon.setter
  def lon(self, val):
    self._attrs["lon"] = val

  @property
  def lat(self):
    return self._attrs["lat"]

  @lat.setter
  def lat(self, val):
    self._attrs["lat"] = val


class Scatter(GraphPlotly.Chart):

  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def layout(self):
    """

    :rtype: LayoutGeo
    """
    if self._layout is None:
      self._layout = LayoutGeo(self._report)
    return self._layout

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='scattermapbox', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataScatterMapBox(self._report, attrs=c_data))
    return self


class Chorolet(GraphPlotly.Chart):

  __reqJs = ['plotly.js']

  @property
  def chart(self):
    """
    :rtype: JsPlotly.Bar
    """
    if self._chart is None:
      self._chart = JsPlotly.Pie(self._report, varName=self.chartId)
    return self._chart

  @property
  def layout(self):
    """

    :rtype: LayoutGeo
    """
    if self._layout is None:
      self._layout = LayoutGeo(self._report)
    return self._layout

  @property
  def data(self):
    return self._traces[-1]

  def add_trace(self, data, type='choroplethmapbox', mode=None):
    c_data = dict(data)
    if type is not None:
      c_data['type'] = type
    if mode is not None:
      c_data['mode'] = mode
    self._traces.append(DataScatterMapBox(self._report, attrs=c_data))
    return self
