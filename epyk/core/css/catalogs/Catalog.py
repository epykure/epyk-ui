#!/usr/bin/python
# -*- coding: utf-8 -*-


class CatalogGroup:

  def __init__(self, report, class_list_type, html_id=None):
    self.page, self.__class_list_type, self._html_id = report, class_list_type, html_id

  def _add_class(self, cssObj):
    self.__class_list_type.add(cssObj)
    return cssObj

  def _set_class(self, classObj):
    cssObj = classObj(self.page, html_id=self._html_id)
    return self._add_class(cssObj)
