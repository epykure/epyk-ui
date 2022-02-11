#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.py import OrderedSet


class CatalogGroup:

  def __init__(self, page: primitives.PageModel, class_list_type: OrderedSet,
               html_id: str = None, component: primitives.HtmlModel = None):
    self.page, self.__class_list_type, self._html_id = page, class_list_type, html_id
    self.component = component

  def _add_class(self, css_obj: primitives.CssClsModel) -> primitives.CssClsModel:
    self.__class_list_type.add(css_obj)
    return css_obj

  def _set_class(self, css_cls):
    css_obj = css_cls(self.page, html_id=self._html_id)
    return self._add_class(css_obj)
