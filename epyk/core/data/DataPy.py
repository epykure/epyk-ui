#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


from epyk.core.py import OrderedSet


class Plotly(object):

  @staticmethod
  def surface(data, y_columns, x_axis, z_axis):
      """
      Description:
      -----------

      Attributes:
      ----------
      :param data:
      :param y_columns:
      :param x_axis:
      :param z_axis:
      """
      z_a, x_a, agg_y = set(), set(), {}
      for rec in data:
        if z_axis in rec:
          z_a.add(rec[z_axis])
        if x_axis in rec:
          x_a.add(rec[x_axis])
        if z_axis in rec and x_axis in rec:
          agg_key = (rec[x_axis], rec[z_axis])
          for y in y_columns:
            agg_y.setdefault(agg_key, {})[y] = agg_y.get(agg_key, {}).get(y, 0) + float(rec[y] if rec[y] else 0)
      z_array = sorted(list(z_a))
      x_array = sorted(list(x_a))
      naps = {'datasets': [], 'series': [], 'python': True}
      for y in y_columns:
        nap = []
        for z in z_array:
          row = [agg_y.get((x, z), {}).get(y, 0) for x in x_array]
          nap.append(row)
        naps['datasets'].append(nap)
        naps['series'].append(y)
      return naps

  @staticmethod
  def map(data):
    return {'datasets': data, 'series': [], 'python': True}

  @staticmethod
  def countries(data, country_col, size_col, scale=False):
    aggregated = {}
    for rec in data:
      if country_col in rec:
        try:
          aggregated[rec[country_col]] = aggregated.get(rec[country_col], 0) + float(rec.get(size_col, 0))
        except: pass

    records = []
    if aggregated:
      max_value = max(aggregated.values())
      factor = scale if scale else 50 / max_value
      record = {'locations': [], 'marker': {'size': []}, 'python': True}
      for k, v in aggregated.items():
        record['locations'].append(k)
        record['marker']['size'].append(v * factor)
      records.append(record)
    return records

  @staticmethod
  def choropleth(data, country_col, size_col, scale=False):
    aggregated = {}
    for rec in data:
      if country_col in rec:
        try:
          aggregated[rec[country_col]] = aggregated.get(rec[country_col], 0) + float(rec.get(size_col, 0))
        except Exception as err:
          pass

    records = []
    if aggregated:
      max_value = max(aggregated.values())
      factor = scale if scale else 50 / max_value
      record = {'locations': [], 'z': []}
      for k, v in aggregated.items():
        record['locations'].append(k)
        record['z'].append(v * factor)
      records.append(record)
    return records

  @staticmethod
  def locations(data, long_col, lat_col, size_col, scale=False):
    aggregated = {}
    for rec in data:
      if long_col in rec and lat_col in rec:
        point = (rec[long_col], rec[lat_col])
        try:
          aggregated[point] = aggregated.get(point, 0) + float(rec.get(size_col, 0))
        except:
          pass

    records = []
    if aggregated:
      max_value = max(aggregated.values())
      factor = 1 / scale if scale else 50 / max_value
      record = {'lon': [], 'lat': [], 'marker': {'size': []}}
      for k, v in aggregated.items():
        record['lon'].append(float(k[0]))
        record['lat'].append(float(k[1]))
        record['marker']['size'].append(v * factor)
      records.append(record)
    return records

  @staticmethod
  def xy(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    if data is None:
      return {'datasets': [], 'python': True, 'series': y_columns}

    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    data = []
    for c in y_columns:
      series = {'x': [], 'y': []}
      for x, y in agg_data.get(c, {}).items():
        series['x'].append(x)
        series['y'].append(y)
      data.append(series)
    return {'datasets': data, 'python': True, 'series': y_columns}

  @staticmethod
  def xy_text(data, y_columns, x_axis, text=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param text: String. The column corresponding to the key in the dictionaries in the record
    """
    if text is None:
      return Plotly.xy(data, y_columns, x_axis)

    agg_data, texts = {}, {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
          texts.setdefault(y, {})[rec[x_axis]] = rec[text]
    data = []
    for c in y_columns:
      series = {'x': [], 'y': [], 'text': []}
      for x, y in agg_data.get(c, {}).items():
        series['x'].append(x)
        series['y'].append(y)
        series['text'].append(texts.get(c, {}).get(x, ''))
      data.append(series)
    return {'datasets': data, 'python': True, 'series': y_columns}

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param z_axis:
    """
    agg_data, agg_z = {}, {}
    for rec in data:
      for i, y in enumerate(y_columns):
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(
            rec[y] if rec[y] else 0)
        if z_axis is not None and i < len(z_axis):
          z_col = sum([float(rec[z]) for z in z_axis]) if isinstance(z_axis, list) else float(
            rec[z_axis] if rec[z_axis] else 0)
          agg_z.setdefault(y, {})[rec[x_axis]] = agg_z.get(y, {}).get(rec[x_axis], 0) + z_col
    labels, data = OrderedSet(), []
    for c in y_columns:
      series = {"x": [], "y": [], "z": []}
      for x, y in agg_data[c].items():
        labels.add(x)
        series['x'].append(x)
        series['y'].append(y)
        series['z'].append(agg_z.get(c, {}).get(x, 0))
      data.append(series)
    is_data = {"labels": labels, 'datasets': [], 'series': [], 'python': True}
    for i, l in enumerate(y_columns):
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

  @staticmethod
  def x_yz(data, y_columns, x_axis, z_axis, dy=0, dx=0, dz=0):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param z_axis:
    :param dy:
    :param dx:
    :param dz:
    """
    agg_data, agg_z = {}, {}
    for rec in data:
      for i, y in enumerate(y_columns):
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(
            rec[y] if rec[y] else 0)
        if z_axis is not None and i < len(z_axis):
          z_col = sum([float(rec.get(z, 0)) for z in z_axis]) if isinstance(z_axis, list) else float(
            rec[z_axis] if rec.get(z_axis, 0) else 0)
          agg_z.setdefault(y, {})[rec.get(x_axis, 0)] = agg_z.get(y, {}).get(rec.get(x_axis, 0), 0) + z_col
    labels, data = OrderedSet(), []
    for c in y_columns:
      series = {"x": [], "y": [], "z": []}
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
        z = agg_z.get(c, {}).get(x, 0)
        series['x'].append([x, float(x) + dx if x else 1])
        series['y'].append([y, y + dy])
        series['z'].append([z, z + dz])
      data.append(series)
    is_data = {"labels": labels, 'datasets': [], 'series': [], 'python': True}
    for i, l in enumerate(y_columns):
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

  @staticmethod
  def table(data, columns, dflt=''):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param columns: List. The key in the recordset to be used to build the row
    :param dflt: Optional. The default value if key is missing
    """
    result = {'values': [], 'python': True, 'header': [[c] for c in columns]}
    if data is None:
      return result

    for rec in data:
      result['values'].append([rec.get(c, dflt) for c in columns])
    return result


class Vis(object):

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis):
    """
    Description:
    ------------

    :param data:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    """
    agg_data = {}
    for rec in data:
      key_point = (rec[x_axis], rec[z_axis])
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[key_point] = agg_data.get(y, {}).get(key_point, 0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for point, y in agg_data[c].items():
        series.append({"x": float(point[0]), "y": y, 'z': float(point[1]), 'group': i})
      data.append(series)
    return data

  @staticmethod
  def xy(data, y_columns, x_axis):
    """
    Description:
    ------------

    :param data:
    :param y_columns:
    :param x_axis:
    """
    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = set(), []
    for i, c in enumerate(y_columns):
      series = []
      for x, y in agg_data[c].items():
        labels.add(x)
        series.append({"x": float(x), "y": y, 'group': i})
      data.append(series)
    return data

  @staticmethod
  def timeline(data, start, content, end=None, type=None, group=None, options=None):
    """
    Description:
    -----------
    Data transformation for the Vis Timeline chart

    Attributes:
    ----------
    :param data:
    :param start: String: The column in the record for the start date
    :param content: String:
    :param end: String: Optional. The column in the record for the end date
    :param type: String. Optional.
    :param group:
    :param options:
    """
    is_data = {'datasets': [], 'python': True}
    if data is None:
      return is_data

    options = options or {}
    for rec in data:
      row = {"start": rec[start], 'content': rec.get(content, '')}
      if 'className' in rec:
        row['className'] = rec['className']
      if end is not None and end in rec:
        row['end'] = rec[end]
      if type is not None and type in rec:
        row['type'] = rec[type]
      elif 'type' in options:
        row['type'] = options['type']
      if group is not None and group in rec:
        row['group'] = rec[group]
      is_data['datasets'].append(row)
    return is_data


class ChartJs(object):

  @staticmethod
  def y(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    if data is None or y_columns is None:
      return is_data

    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          if rec[y] is None:
            agg_data.setdefault(y, {})[rec[x_axis]] = rec[y]
          else:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = OrderedSet(), []
    for c in y_columns:
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
    is_data["labels"] = labels
    for i, y in enumerate(y_columns):
      is_data["datasets"].append([agg_data.get(y, {}).get(x) for x in labels])
      is_data["series"].append(y)
    return is_data

  @staticmethod
  def xy(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    agg_data = {}
    for rec in data:
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
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    for i, l in enumerate(y_columns):
      is_data["labels"].append(l)
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param z_axis:
    """
    is_data = {"labels": OrderedSet(), 'datasets': [], 'series': [], 'python': True}
    if y_columns is None:
      return is_data

    agg_data, agg_r = {}, {}
    for rec in data:
      for i, y in enumerate(y_columns):
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
        if z_axis is not None and i < len(z_axis):
          agg_r.setdefault(y, {})[rec[x_axis]] = agg_r.get(y, {}).get(rec[x_axis], 0) + float(rec[z_axis[i]])
    data = []
    for c in y_columns:
      series = []
      for x, y in agg_data.get(c, {}).items():
        is_data["labels"].add(x)
        series.append({"x": x, "y": y, 'r': agg_r.get(c, {}).get(x, 1)})
      data.append(series)
    for i, l in enumerate(y_columns):
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data


class C3(object):

  @staticmethod
  def y(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = OrderedSet(), []
    for c in y_columns:
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
    is_data = {"labels": labels, 'datasets': [], 'series': [], 'python': True}
    for i, y in enumerate(y_columns):
      is_data["datasets"].append([agg_data.get(y, {}).get(x) for x in labels])
      is_data["series"].append(y)
    return is_data


class NVD3(object):

  @staticmethod
  def xy(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
        series.append({"x": x, "y": y})
      data.append(series)
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    for i, l in enumerate(y_columns):
      is_data["labels"].append(l)
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data

  @staticmethod
  def labely(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = set(), []
    for c in y_columns:
      series = []
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
        series.append({"label": x, "y": y})
      data.append(series)
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    for i, l in enumerate(y_columns):
      is_data["labels"].append(l)
      is_data["datasets"].append(data[i])
      is_data["series"].append(l)
    return is_data


class Datatable(object):

  @staticmethod
  def table(data, columns, dflt=''):
    """
    Description:
    ------------
    Tranform the data in a list of list for Datatable

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param columns: List. The key in the recordset to be used to build the row
    :param dflt: Optional. The default value if key is missing
    """
    records = []
    for rec in data:
      records.append([rec.get(c, dflt) for c in columns])
    return records


class Google(object):

  @staticmethod
  def y(data, y_columns, x_axis):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    if data is None:
      return is_data

    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    labels, data = OrderedSet(), []
    for c in y_columns:
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
    is_data["labels"] = labels
    for x in labels:
      is_data["datasets"].append([x] + [agg_data.get(y, {}).get(x) for y in y_columns])
    is_data["series"] = y_columns
    is_data["x"] = x_axis
    return is_data

  @staticmethod
  def table(data, rows, cols):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param rows:
    :param cols:
    """
    is_data = {"rows": rows, 'datasets': [], 'cols': cols, 'python': True}
    for rec in data:
      is_data['datasets'].append([rec.get(c, '') for c in rows + cols])
    return is_data


class HtmlComponents(object):

  def markdown(self, content, tooltips=None, case_sensitive=False):
    """
    Description:
    ------------
    Format the markdown text with tooltips

    Attributes:
    ----------
    :param content: String. The markdown content
    :param tooltips: Dictionary. The words to be replaced
    """
    if tooltips is None:
      return content

    code_block, new_content = False, []
    for line in content.split("\n"):
      if line.startswith("```") and not code_block:
        code_block = True
      elif line.startswith("```"):
        code_block = False

      if code_block or line.startswith("["):
        new_content.append(line)
      else:
        for k, v in tooltips.items():
          tooltip = '<a style="color:grey" href="" onmouseout="hideTooltip()" onmouseover="showTooltip(this, \'%s\')">%s</a>' % (v, k)
          if case_sensitive:
            line = line.replace(k, tooltip)
          else:
            insensitive_replace = re.compile(re.escape(k), re.IGNORECASE)
            line = insensitive_replace.sub(tooltip, line)
        new_content.append(line)
    return "\n".join(new_content)
