#!/usr/bin/python
# -*- coding: utf-8 -*-


class Theme(object):

  def __init__(self, ovrs_attrs=None):
    self.__colors = {
      "charts": list(self._charts),
      "colors": list(self._colors),
      "greys": list(self._greys),
      "warning": list(self._warning),
      "danger": list(self._danger),
      "success": list(self._success),
    }
    if ovrs_attrs is not None:
      self.__colors.update(ovrs_attrs)

  @property
  def charts(self):
    return self.__colors["charts"]

  @charts.setter
  def charts(self, colors):
    self.__colors["charts"] = colors

  @property
  def colors(self):
    return self.__colors["colors"]

  @colors.setter
  def colors(self, colors):
    self.__colors["colors"] = colors

  @property
  def greys(self):
    return self.__colors["greys"]

  @greys.setter
  def greys(self, colors):
    self.__colors["greys"] = colors

  @property
  def warning(self):
    return self.__colors["warning"]

  @warning.setter
  def warning(self, colors):
    self.__colors["warning"] = colors

  @property
  def danger(self):
    return self.__colors["danger"]

  @danger.setter
  def danger(self, colors):
    self.__colors["danger"] = colors

  @property
  def success(self):
    return self.__colors["success"]

  @success.setter
  def success(self, colors):
    self.__colors["success"] = colors


class ThemeCustome(Theme):
  _charts, _colors, _greys = [], [], []
  _warning, _danger, _success = set(), set(), set()


class ThemeDefault(Theme):

  _charts = [
    '#009999', '#336699', '#ffdcb9',
    '#cc99ff', '#b3d9ff', '#ffff99',
    '#000066', '#b2dfdb', '#80cbc4',
    '#e0f2f1', '#b2dfdb', '#80cbc4',  # teal
    '#ffebee', '#ffcdd2', '#ef9a9a',  # red
    '#f3e5f5', '#e1bee7', '#ce93d8',  # purple
    '#ede7f6', '#d1c4e9', '#b39ddb',  # deep purple
    '#e8eaf6', '#c5cae9', '#9fa8da',  # indigo
    '#fffde7', '#fff9c4', '#fff59d',  # yellow
    '#fff3e0', '#ffe0b2', '#ffcc80',  # orange
    '#efebe9', '#d7ccc8', '#bcaaa4',  # brown
  ]
  _colors = ["#e8f5e9", '#c8e6c9', '#a5d6a7', '#81c784', '#66bb6a', '#4caf50', '#43a047', '#388e3c', '#2e7d32',
             '#1b5e20']
  _greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242',
            '#212121', '#000000']
  _warning, _danger, _success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#3bb194')
