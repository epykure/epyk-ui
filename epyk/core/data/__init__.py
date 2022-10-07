#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys

from epyk.core.data import Data
from epyk.core.data import DataPy
from epyk.core.data import DataEvent

from epyk.core.js.objects.JsData import Datamap
from epyk.core.js.JsLocation import URLSearchParams


# Shortcut data in the framework.
# All those features are available in the report object but this allow a shortcut when the context is not necessary
chartJs = DataPy.ChartJs()

apexCharts = DataPy.ChartJs()

plotly = DataPy.Plotly()

vis = DataPy.Vis()

nvd3 = DataPy.NVD3()

c3 = DataPy.C3()

bb = DataPy.C3()

google = DataPy.Google()

datatable = DataPy.Datatable()

tree = DataPy.Tree()

events = DataEvent.DataEvents()

configs = DataEvent.DataConfig()

loops = DataEvent.DataLoops()

primitives = DataEvent.DataPrimitives()

datamap = Datamap

http = URLSearchParams("location.search")

components = DataPy.HtmlComponents()

list_items = DataPy.ListItems()


class Sent:

  def __init__(self, data):
    self.__data = data

  def get(self, name: str = None):
    """
    Set the option attribute to be added on the Javascript side during the component build

    :param str name: The attribute name.
    """
    return self.__data[name or sys._getframe().f_back.f_code.co_name]


class Received:

  data_sent = None

  def __init__(self, data=None, tags=None):
    self.__data = data
    self.__tags = tags
    self.__response_tags = set()

  def set(self, value, name=None):
    """
    Set the option attribute to be added on the Javascript side during the component build

    :param value: Object. The value for the name
    :param name: String. The attribute name
    """
    self.__response_tags.add(name or sys._getframe().f_back.f_code.co_name)
    self.__data[name or sys._getframe().f_back.f_code.co_name] = value

  def get(self, name=None):
    """
    Set the option attribute to be added on the Javascript side during the component build

    :param name: String. The attribute name
    """
    if self.__data is not None:
      return self.__data[name or sys._getframe().f_back.f_code.co_name]

    return events.data[name or sys._getframe().f_back.f_code.co_name]

  @property
  def s(self):
    """

    TODO: Find a way to keep autocompletion without overidding this property
    :return:
    """
    if self.data_sent is None:
      raise ValueError("data_sent must be defined")

    return self.data_sent(self.__data)

  @classmethod
  def flask_request(cls, req):
    if req.method == 'POST':
      return cls(req.get_json())

    return cls(req)

  def response(self):
    data = {}
    for t in list(self.__response_tags):
      data[t] = self.__data[t]
    return json.dumps(data)


class DataSchemaProperties:

  def __init__(self, context: dict):
    self._context = context

  @property
  def keys(self):
    return self._context['keys']

  @property
  def values(self):
    return self._context['values']

  @property
  def columns(self):
    return list(self.keys | self.values)

  @property
  def funcs(self):
    return self._context['fncs']

  @property
  def containers(self):
    return self._context['containers']


class DataProperties:

  def __init__(self, context: dict):
    self._context = context

  def add(self, records, js_funcs: list = None, profile=None):
    data_id = len(self._context["sources"])
    self._context["sources"][data_id] = records
    self._context["schema"][data_id] = {"containers": {}, 'fncs': js_funcs or [], "profile": profile}
    return data_id

  def get_schema(self, data_id: int):
    return self._context["schema"][data_id]

  def get_records(self, data_id: int):
    return self._context["sources"][data_id]
