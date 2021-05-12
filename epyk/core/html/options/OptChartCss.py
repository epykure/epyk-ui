#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options


class ChartCssOptions(Options):

  @property
  def title(self):
    """
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    self._config(text)
    self.show_heading()

  def show_labels(self):
    self._report.attr["class"].add("show-labels")

  def show_data_axes(self):
    self._report.attr["class"].add("show-data-axes")

  def reverse_data(self):
    self._report.attr["class"].add("reverse-data")

  def reverse_datasets(self):
    self._report.attr["class"].add("reverse-datasets")

  def show_secondary_axes(self, n):
    self._report.attr["class"].add("show-%s-secondary-axes" % n)

  def show_primary_axis(self):
    self._report.attr["class"].add("show-primary-axis")

  def multiple(self):
    self._report.attr["class"].add("multiple")

  def show_heading(self):
    self._report.attr["class"].add("show-heading")

  def datasets_spacing(self, n):
    self._report.attr["class"].add("datasets-spacing-%s" % n)

  def data_spacing(self, n):
    self._report.attr["class"].add("data-spacing-%s" % n)

  def row_style(self, attrs):
    self._report.row_style.attrs.update(attrs)
