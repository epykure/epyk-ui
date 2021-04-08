#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import logging

from epyk.core.py import OrderedSet
from epyk.core.data.recs import RecItems


class Plotly:

  @staticmethod
  def surface(data, y_columns, x_axis, z_axis):
      """
      Description:
      -----------
      Transform a record to a valid data structure for Plotly surfaces.

      Usage:
      -----


      Attributes:
      ----------
      :param data: List of dictionaries. The data to be converted.
      :param y_columns: List. The keys in the dictionaries used as y axes.
      :param x_axis: String. The key in the dictionaries used as x axis.
      :param z_axis: String. The key in the dictionaries used as z axis.
      """
      naps = {'datasets': [], 'series': [], 'python': True}

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
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of Dictionaries.
    """
    return {'datasets': data, 'series': [], 'python': True}

  @staticmethod
  def countries(data, country_col, size_col, scale=False):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param country_col:
    :param size_col:
    :param scale:
    """
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
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param country_col:
    :param size_col:
    :param scale:
    """
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
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param long_col:
    :param lat_col:
    :param size_col:
    :param scale:
    """
    aggregated = {}
    for rec in data:
      if long_col in rec and lat_col in rec:
        point = (rec[long_col], rec[lat_col])
        try:
          aggregated[point] = aggregated.get(point, 0) + float(rec.get(size_col, 0))
        except Exception as err:
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
  def xy(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    if data is None:
      return {'datasets': [], 'python': True, 'series': y_columns}

    results = []
    if options is not None and options.get("agg") == 'distinct':
      for y in y_columns:
        series = {'x': [], 'y': [], 'text': []}
        for rec in data:
          series["x"].append(rec[x_axis])
          series["y"].append(rec[y])
        results.append(series)
    else:
      agg_data = {}
      for rec in data:
        for y in y_columns:
          if y in rec:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
      results = []
      for c in y_columns:
        series = {'x': [], 'y': []}
        for x, y in agg_data.get(c, {}).items():
          series['x'].append(x)
          series['y'].append(y)
        results.append(series)
    return {'datasets': results, 'python': True, 'series': y_columns}

  @staticmethod
  def xy_text(data, y_columns, x_axis, text=None, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    :param text: String. The column corresponding to the key in the dictionaries in the record
    """
    if text is None:
      return Plotly.xy(data, y_columns, x_axis, options=options)

    results = []
    if options is not None and options.get("agg") == 'distinct':
      for y in y_columns:
        series = {'x': [], 'y': [], 'text': []}
        for rec in data:
          series["x"].append(rec[x_axis])
          series["y"].append(rec[y])
          if text is not None:
            series["text"].append(rec.get(text, ""))
        results.append(series)
    else:
      agg_data, texts = {}, {}
      for rec in data:
        for y in y_columns:
          if y in rec:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
            texts.setdefault(y, {})[rec[x_axis]] = rec[text]
      for c in y_columns:
        series = {'x': [], 'y': [], 'text': []}
        for x, y in agg_data.get(c, {}).items():
          series['x'].append(x)
          series['y'].append(y)
          series['text'].append(texts.get(c, {}).get(x, ''))
        results.append(series)
    return {'datasets': results, 'python': True, 'series': y_columns}

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis):
    """
    Description:
    ------------

    Usage:
    -----

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

    Usage:
    -----

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

    Usage:
    -----

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


class Vis:

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis):
    """
    Description:
    ------------


    Usage:
    -----

    Attributes:
    ----------
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

    Usage:
    -----

    Attributes:
    ----------
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
    Data transformation for the Vis Timeline chart.

    Usage:
    -----

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


class ChartJs:

  @staticmethod
  def copy(records, empty=False):
    """
    Description:
    ------------
    Create a copy of the ChartJs dataset.

    Attributes:
    ----------
    :param records: Dictionary. A ChartJs data structure object.
    :param empty: Boolean. Optional. Specify of the data need to be removed.
    """
    result = {"labels": list(records["labels"]), 'datasets': [], 'series': list(records["series"]), 'python': records["python"]}
    for d in records['datasets']:
      result['datasets'].append({"data": list(d["data"]), 'label': d["label"]})
    if empty:
      result["labels"] = []
      for d in result['datasets']:
        d["data"] = []
      return result

    return result

  @staticmethod
  def y(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python record.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
            if hasattr(rec[y], "toStr"):
              agg_data.setdefault(y, {})[rec[x_axis]] = rec[y]
            elif rec[y]:
              try:
                agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
              except Exception as err:
                if options is not None and options.get("verbose", False):
                  logging.warning(err)
                  logging.warning("Error summing rec: %s" % rec)
    labels, data = OrderedSet(), []
    for c in y_columns:
      for x, y in agg_data.get(c, {}).items():
        labels.add(x)
    is_data["labels"] = sorted(labels)
    for i, y in enumerate(y_columns):
      series = []
      for x in is_data["labels"]:
        value = agg_data.get(y, {}).get(x)
        series.append(value)
      is_data["datasets"].append({"data": series, 'label': y})
      is_data["series"].append(y)
    return is_data

  @staticmethod
  def xy(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python record.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    agg_data = {}
    for rec in data:
      for y in y_columns:
        if y in rec:
          if rec[y]:
            try:
              agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
            except Exception as err:
              if options is not None and options.get("verbose", False):
                logging.warning(err)
                logging.warning("Error summing rec: %s" % rec)
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
      is_data["datasets"].append({"data": data[i], 'label': l})
      is_data["series"].append(l)
    return is_data

  @staticmethod
  def xyz(data, y_columns, x_axis, z_axis=None, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python record.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param z_axis:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    is_data = {"labels": OrderedSet(), 'datasets': [], 'series': [], 'python': True}
    if y_columns is None:
      return is_data

    agg_data, agg_r = {}, {}
    for rec in data:
      for i, y in enumerate(y_columns):
        if y in rec:
          # agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
          agg_data.setdefault(y, {}).setdefault(rec[x_axis], []).append(float(rec[y]))
        if z_axis is not None and i < len(z_axis):
          agg_r.setdefault(y, {})[rec[x_axis]] = agg_r.get(y, {}).get(rec[x_axis], 0) + float(rec[z_axis[i]])
    data = []
    for c in y_columns:
      series = []
      for x, ys in agg_data.get(c, {}).items():
        is_data["labels"].add(x)
        for y in ys:
          series.append({"x": x, "y": y, 'r': agg_r.get(c, {}).get(x, 2)})
      data.append(series)
    for i, l in enumerate(y_columns):
      is_data["datasets"].append({"data": data[i], 'label': l})
      is_data["series"].append(l)
    return is_data


class C3:

  @staticmethod
  def y(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: List of dict. The Python records.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    is_data = {"labels": OrderedSet(), 'datasets': [], 'series': [], 'python': True}
    if data is None or y_columns is None:
      return is_data

    if options is not None and options.get("agg") == 'distinct':
      for y in y_columns:
        is_data["datasets"].append([])
        is_data["series"].append(y)
      is_data["labels"] = []
      for rec in data:
        is_data["labels"].append(rec[x_axis])
        for i, y in enumerate(y_columns):
          is_data["datasets"][i].append(rec.get(y))
    else:
      agg_data = {}
      for rec in data:
        for y in y_columns:
          if y in rec:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])

      for c in y_columns:
        for x, y in agg_data.get(c, {}).items():
          is_data["labels"].add(x)
      for i, y in enumerate(y_columns):
        is_data["datasets"].append([agg_data.get(y, {}).get(x) for x in is_data["labels"]])
        is_data["series"].append(y)
    return is_data


class NVD3:

  @staticmethod
  def xy(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python record.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    is_data = {"labels": OrderedSet(), 'datasets': [], 'series': [], 'python': True}
    if data is None or y_columns is None:
      return is_data

    if options is not None and options.get("agg") == 'distinct':
      for y in y_columns:
        is_data["series"].append(y)
        is_data["labels"].append(y)
        result = []
        for rec in data:
          result.append({"x": rec[x_axis], "y": rec[y]})
        is_data["datasets"].append(result)
    else:
      agg_data, result = {}, []
      for rec in data:
        for y in y_columns:
          if y in rec:
            agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
      for c in y_columns:
        series = []
        for x, y in agg_data.get(c, {}).items():
          series.append({"x": x, "y": y})
        result.append(series)
      for i, l in enumerate(y_columns):
        is_data["labels"].append(l)
        is_data["datasets"].append(result[i])
        is_data["series"].append(l)
    return is_data

  @staticmethod
  def labely(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python record.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    is_data = {"labels": OrderedSet(), 'datasets': [], 'series': [], 'python': True}
    if data is None or y_columns is None:
      return is_data

    agg_data, result = {}, []
    for rec in data:
      for y in y_columns:
        if y in rec:
          agg_data.setdefault(y, {})[rec[x_axis]] = agg_data.get(y, {}).get(rec[x_axis], 0) + float(rec[y])
    for c in y_columns:
      series = []
      for x, y in agg_data.get(c, {}).items():
        is_data["labels"].add(x)
        series.append({"label": x, "y": y})
      result.append(series)
    for i, l in enumerate(y_columns):
      is_data["labels"].append(l)
      is_data["datasets"].append(result[i])
      is_data["series"].append(l)
    return is_data


class Datatable:

  @staticmethod
  def table(data, columns, dflt=''):
    """
    Description:
    ------------
    Transform the data in a list of list for Datatable

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python recordset
    :param columns: List. The key in the recordset to be used to build the row
    :param dflt: String. Optional. The default value if key is missing.
    """
    records = []
    for rec in data:
      records.append([rec.get(c, dflt) for c in columns])
    return records


class Google:

  @staticmethod
  def y(data, y_columns, x_axis, options=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data: List of dict. The Python records.
    :param y_columns: List. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: String. The column corresponding to a key in the dictionaries in the record
    """
    is_data = {"labels": [], 'datasets': [], 'series': [], 'python': True}
    if data is None:
      return is_data

    if options is not None and options.get("agg") == 'distinct':
      labels = OrderedSet()
      for rec in data:
        labels.add(rec[x_axis])
        for y in y_columns:
          if y in rec:
            is_data['datasets'].append([str(rec[x_axis]), rec[y]])
      is_data["labels"] = sorted(list(labels))
    else:
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
        is_data["datasets"].append([str(x)] + [agg_data.get(y, {}).get(x) for y in y_columns])
    is_data["series"] = y_columns
    is_data["x"] = x_axis
    return is_data

  @staticmethod
  def table(data, rows, cols):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param rows:
    :param cols:
    """
    is_data = {"rows": rows, 'datasets': [], 'cols': cols, 'python': True}
    if data is None:
      return is_data

    for rec in data:
      is_data['datasets'].append([rec.get(c, '') for c in rows + cols])
    return is_data


class Checkbox:

  @staticmethod
  def from_records(data, column, all_checked=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param column:
    :param all_checked:
    """
    result = [{"value": rec[column], "checked": all_checked} for rec in data]
    return result

  @staticmethod
  def from_df(df, column, all_checked=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param df:
    :param column:
    :param all_checked:
    """
    result = [{"value": rec[column], "checked": all_checked} for rec in df[column].unique().tolist()]
    return result

  @staticmethod
  def from_list(data, checked=None, all_checked=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param all_checked:
    """
    result = []
    for value in data:
      result.append({"value": value})
      if checked is not None and value == checked:
        result[-1]["checked"] = True
    return result


class SelectionBox:

  @staticmethod
  def from_records(records, column):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param column:
    """
    result = {}
    for rec in records:
      result[rec[column]] = {'name': rec[column], 'value': rec[column].strip()}
    return [result[k] for k in sorted(result.keys())]

  @staticmethod
  def from_df(df, column, all_checked=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param df:
    :param column:
    :param all_checked:
    """
    return [{'name': r, 'value': r} for r in df[column].unique().tolist()]

  @staticmethod
  def from_list(values, all_checked=False):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param values:
    :param all_checked:
    """
    return [{'name': r, 'value': r} for r in values]

  @staticmethod
  def from_dict(values, all_checked=False):
    return [{'name': values[k], 'value': k} for k in sorted(values.keys())]


class ListData:

  @staticmethod
  def from_records(records, column):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param column:
    """
    result = set()
    for rec in records:
      result.add(rec[column].strip())
    return sorted(list(result))


class HtmlComponents:

  def markdown(self, content, tooltips=None, case_sensitive=False):
    """
    Description:
    ------------
    Format the markdown text with tooltips.

    Usage:
    -----

    Attributes:
    ----------
    :param content: String. The markdown content.
    :param tooltips: Dictionary. Optional. The words to be replaced.
    :param case_sensitive: Boolean. Optional. Case sensitive flag.
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

  @property
  def checkboxes(self):
    """
    Description:
    ------------
    Property to provide standard ways to build the data for the Checkboxes.
    Those transformation will be done on the Python side and they will not have any impact on the JavaScript side.

    The purpose here is the prepare the data before passing it to the HTML container.

    Those functions can be used in the interface but also in the build method to ensure the format for the
    JavaScript processing.
    """
    return Checkbox

  @property
  def radio(self):
    """
    Description:
    ------------

    """
    return Checkbox

  @property
  def check(self):
    """
    Description:
    ------------

    """
    return Checkbox

  @property
  def select(self):
    """
    Description:
    ------------

    """
    return SelectionBox

  @property
  def list(self):
    """
    Description:
    ------------

    """
    return ListData


class Tree:

  def __add_level(self, path, tree, root, excluded_folders, make_url=None, options=None):
    """
    Description:
    ------------
    Internal function to do the nesting for the folders definition.
    This is used in the folder method.

    Attributes:
    ----------
    :param path: String. The path.
    :param tree: List. The current tree pointer.
    :param root: String. The root path.
    :param excluded_folders: Tuple. The excluded folders.
    :param make_url: Function. Optional. A make url function to build this in the leaves.
    :param options: Dictionary. Optional. All the options added to this function (styles...).
    """
    for fp in os.listdir(path):
      if fp.startswith(".") or fp.startswith("__") or (excluded_folders is not None and fp in excluded_folders):
        continue

      fp_path = os.path.join(path, fp)
      if os.path.isdir(fp_path):
        tree.append({"value": fp, "_path": fp_path, "items": []})
        if options.get("styles", {}).get("node") is not None:
          tree[-1]["css"] = options["styles"]["node"]
        self.__add_level(fp_path, tree[-1]["items"], root, excluded_folders, make_url=make_url, options=options)
      elif fp.endswith(".py"):
        tree.append({"value": fp, "_path": fp_path}) # "url": "/code_frame?classpath=%s&script=%s" % (root, fp_path)
        if options.get("styles", {}).get("leaf") is not None:
          tree[-1]["css"] = options["styles"]["leaf"]
        if make_url is not None:
          tree[-1]["url"] = make_url({"path": fp_path, "root": root, "file": fp})

  def folders(self, path, excluded_folders=None, make_url=None, style_leaf=None, style_node=None):
    """
    Description:
    ------------
    Get a tree structure from a path.
    This will get all the files and sub folders.

    Usage:
    -----

    Attributes:
    ----------
    :param path: String. The path.
    :param excluded_folders: List | Tuple. Optional.
    :param make_url: Function. Optional.
    :param style_leaf: Dictionary. Optional. The style to be used for the nodes.
    :param style_node: Dictionary. Optional. The style to be used for the children.
    """
    _, root_folder = os.path.split(path)
    result = [{"value": root_folder, "items": [], "_path": path}]
    if path is not None:
      self.__add_level(path, result[0]["items"], path, excluded_folders, make_url, options={"styles": {"leaf": style_leaf, "node": style_node}})
    return result


class ListItems:

  @property
  def text(self):
    """
    Description:
    ------------
    """
    return ListData

  @property
  def link(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsLinkRec

  @property
  def box(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsBoxRec

  @property
  def tweet(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsTweetRec

  @property
  def icon(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsIconRec

  @property
  def check(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsCheckRec

  @property
  def radio(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsBoxRec

  @property
  def badge(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsBoxRec

  @property
  def button(self):
    """
    Description:
    ------------
    """
    return RecItems.ItemsBoxRec
