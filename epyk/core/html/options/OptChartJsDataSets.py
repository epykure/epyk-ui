
import sys
from typing import Any, Union
from epyk.core.html.options import Options


class CommConfigs(Options):

  def _get_commons(self, name: str = None):
    """ Get common attributes for all data series.

    :param name: The attribute's name
    """
    return self.component.options['commons'].get(name or sys._getframe().f_back.f_code.co_name)

  def _set_commons(self, value: Any, name: str = None):
    """ Set common attributes for all data series.

    :param value: The attribute's value
    :param name: The attribute's name
    """
    name = name or sys._getframe().f_back.f_code.co_name
    for ds in self.component._datasets:
      ds._attrs[name] = value
    self.component.options['commons'][name] = value

  def update(self, vals: dict):
    """ Update multiple series attributes.

    :param vals: All the common attributes to be set for the series
    """
    for k, v in vals.items():
      self._set_commons(v, k)

  def attr(self, name: str, value: Any = None):
    """ Method to add bespoke attributes for datasets series.

    :param name: The attribute's name
    :param value: The attribute's value
    """
    if value is None:
      return self._get_commons(name)

    self._set_commons(value, name)

  @property
  def borderWidth(self):
    """ The bar border width (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @borderWidth.setter
  def borderWidth(self, num: int):
    self._set_commons(num)

  @property
  def borderRadius(self):
    """ The bar border radius (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @borderRadius.setter
  def borderRadius(self, num: int):
    self._set_commons(num)

  @property
  def borderSkipped(self):
    """ The edge to skip when drawing bar..

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @borderSkipped.setter
  def borderSkipped(self, value: Union[bool, str]):
    self._set_commons(value)

  @property
  def clip(self):
    """ How to clip relative to chartArea.
    Positive value allows overflow, negative value clips that many pixels inside chartArea. 0 = clip at chartArea..

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @clip.setter
  def clip(self, value: Any):
    self._set_commons(value)

  @property
  def hoverBackgroundColor(self):
    """ The bar background color when hovered.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @hoverBackgroundColor.setter
  def hoverBackgroundColor(self, value: str):
    self._set_commons(value)

  @property
  def hoverBorderColor(self):
    """ The bar border color when hovered.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @hoverBorderColor.setter
  def hoverBorderColor(self, value: str):
    self._set_commons(value)

  @property
  def hoverBorderWidth(self):
    """ The bar border width when hovered (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @hoverBorderWidth.setter
  def hoverBorderWidth(self, num: int):
    self._set_commons(num)

  @property
  def hoverBorderRadius(self):
    """ The bar border radius when hovered (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @hoverBorderRadius.setter
  def hoverBorderRadius(self, num: int):
    self._set_commons(num)

  @property
  def hoverOffset(self):
    """ Arc offset when hovered (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @hoverOffset.setter
  def hoverOffset(self, num: int):
    self._set_commons(num)

  @property
  def order(self):
    """ The drawing order of dataset. Also affects order for stacking, tooltip and legend..

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @order.setter
  def order(self, value: str):
    self._set_commons(value)

  @property
  def offset(self):
    """ arc offset (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @offset.setter
  def offset(self, values: Any):
    self._set_commons(values)

  @property
  def pointStyle(self):
    """ Shape style.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @pointStyle.setter
  def pointStyle(self, value: str):
    self._set_commons(value)

  @property
  def stack(self):
    """ The ID of the group to which this dataset belongs to (when stacked, each group will be a separate stack).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @stack.setter
  def stack(self, value: str):
    self._set_commons(value)


class Pie(CommConfigs):

  @property
  def circumference(self):
    """ Per-dataset override for the sweep that the arcs cover.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @circumference.setter
  def circumference(self, num: float):
    self._set_commons(num)

  @property
  def spacing(self):
    """ Fixed arc offset (in pixels). Similar to offset but applies to all arcs.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @spacing.setter
  def spacing(self, num: float):
    self._set_commons(num)

  @property
  def weight(self):
    """ The relative thickness of the dataset. Providing a value for weight will cause the pie or doughnut dataset to
    be drawn with a thickness relative to the sum of all the dataset weight values.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @weight.setter
  def weight(self, num: float):
    self._set_commons(num)

  @property
  def rotation(self):
    """ bubble rotation (in degrees).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @rotation.setter
  def rotation(self, value: float):
    self._set_commons(value)


class Radar(Pie):

  @property
  def spanGaps(self):
    """ If true, lines will be drawn between points with no or null data.
    If false, points with null data will create a break in the line.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @spanGaps.setter
  def spanGaps(self, flag: bool):
    self._set_commons(flag)


class Line(CommConfigs):

  @property
  def fill(self):
    """ How to fill the area under the line.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @fill.setter
  def fill(self, value: Union[bool, str]):
    self._set_commons(value)

  @property
  def stepped(self):
    """ If the stepped value is set to anything other than false, tension will be ignored.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @stepped.setter
  def stepped(self, value: Union[bool, str]):
    self._set_commons(value)

  @property
  def showLine(self):
    """ If the stepped value is set to anything other than false, tension will be ignored.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @showLine.setter
  def showLine(self, flag: bool):
    self._set_commons(flag)

  @property
  def tension(self):
    """ Bezier curve tension of the line. Set to 0 to draw straightlines.
    This option is ignored if monotone cubic interpolation is used.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/line.html
    """
    return self._get_commons()

  @tension.setter
  def tension(self, value: float):
    self._set_commons(value)


class Bar(CommConfigs):

  @property
  def maxBarThickness(self):
    """ Set this to ensure that bars have a maximum length in pixels.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @maxBarThickness.setter
  def maxBarThickness(self, num: int):
    self._set_commons(num)

  @property
  def barThickness(self):
    """

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @barThickness.setter
  def barThickness(self, num: int):
    self._set_commons(num)

  @property
  def minBarLength(self):
    """ Set this to ensure that bars have a minimum length in pixels.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @minBarLength.setter
  def minBarLength(self, num: int):
    self._set_commons(num)

  @property
  def barPercentage(self):
    """ Percent (0-1) of the available width each bar should be within the category width. 1.0 will take
    the whole category width and put the bars right next to each other.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @barPercentage.setter
  def barPercentage(self, num: int):
    self._set_commons(num)

  @property
  def skipNull(self):
    """ If true, null or undefined values will not be used for spacing calculations when determining bar size.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @skipNull.setter
  def skipNull(self, flag: bool):
    self._set_commons(flag)


class Bubble(CommConfigs):

  @property
  def rotation(self):
    """ bubble rotation (in degrees).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @rotation.setter
  def rotation(self, value: float):
    self._set_commons(value)

  @property
  def radius(self):
    """ bubble radius (in pixels).

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @radius.setter
  def radius(self, value: int):
    self._set_commons(value)


class Polar(CommConfigs):

  @property
  def borderAlign(self):
    """ Border Alignment.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
      https://www.chartjs.org/docs/latest/charts/polar.html#border-alignment
    """
    return self._get_commons()

  @borderAlign.setter
  def borderAlign(self, value: str):
    self._set_commons(value)

  @property
  def borderJoinStyle(self):
    """ arc border join style.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
      https://www.chartjs.org/docs/latest/charts/polar.html#border-alignment
    """
    return self._get_commons()

  @borderJoinStyle.setter
  def borderJoinStyle(self, value: str):
    self._set_commons(value)

  @property
  def circular(self):
    """ By default the Arc is curved. If circular: false the Arc will be flat.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
    """
    return self._get_commons()

  @circular.setter
  def circular(self, flag: bool):
    self._set_commons(flag)

  @property
  def hoverBorderJoinStyle(self):
    """ arc border join style when hovered.

    Related Pages:

      https://www.chartjs.org/docs/latest/charts/bar.html
      https://www.chartjs.org/docs/latest/charts/polar.html#border-alignment
    """
    return self._get_commons()

  @hoverBorderJoinStyle.setter
  def hoverBorderJoinStyle(self, value: str):
    self._set_commons(value)
