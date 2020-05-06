
from epyk.core.py import OrderedSet


class DataGlobal(object):

  def __init__(self, data, report=None, component=None):
    self._data = data
    self._report, self._component = report, component

  @property
  def chartjs(self):
    """
    Description:
    ------------

    """
    return DataCharrtJs(self._data, self._report, self._component)

  @property
  def c3(self):
    """
    Description:
    ------------

    """
    return DataCharrtJs(self._data, self._report, self._component)

  @property
  def billboard(self):
    """
    Description:
    ------------

    """
    return DataCharrtJs(self._data, self._report, self._component)


class DataCharrtJs(object):

  def __init__(self, data, report=None, component=None):
    self._data = data
    self._report, self._component = report, component

  def xy(self, y_columns, x_axis, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param y_column:
    :param x_axis:
    :param profile:
    """
    agg_data = {}
    for rec in self._data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y})
      data.append(series)
    is_data = {"labels": [], 'datasets': [], 'series': []}
    for i, l in enumerate(y_columns):
      is_data["labels"].append(l)
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

  def y(self, y_columns, x_axis, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param y_column:
    :param x_axis:
    :param profile:
    """
    agg_data = {}
    for rec in self._data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = OrderedSet(), []
    for c in y_columns:
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
    is_data = {"labels": labels, 'datasets': [], 'series': []}
    for i, y in enumerate(y_columns):
      is_data["datasets"].append([agg_data.get(y, {}).get(x) for x in labels])
      is_data["series"].append(y)
    return is_data

  def xyz(self, y_columns, x_axis, z_axis, profile=None):
    """

    :param y_column:
    :param x_axis:
    :param z_axis:
    :param profile:
    """
    agg_data, agg_r = {}, {}
    for rec in self._data:
      for i, y in enumerate(y_columns):
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
        if z_axis is not None and i < len(z_axis):
          agg_r.setdefault(y, {})[rec[x_axis]] = agg_r.get(y, {}).get(rec[x_axis], 0) + float(rec[z_axis[i]])
    labels, data = OrderedSet(), []
    for c in y_columns:
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": x, "y": y, 'r': agg_r.get(c, {}).get(x, 1)})
      data.append(series)
    is_data = {"labels": labels, 'datasets': [], 'series': []}
    for i, l in enumerate(y_columns):
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

