#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Json(JsPackage):
  lib_alias = {"js": "json-formatter-js", 'css': "json-formatter-js"}

  def openAtDepth(self, n: int):
    """Default: 1 This number indicates up to how many levels the rendered tree should open.
    It allows use cases such as collapse all levels (with value 0) or expand all levels (with value Infinity).

    `json-formatter <https://github.com/mohsen1/json-formatter-js>`_

    :param n: Integer. the depth of the tree at start.
    """
    return JsObjects.JsObjects.get('%s.openAtDepth(%s)' % (self.varName, n))

  @property
  def json(self):
    """ """
    return JsObjects.JsObjects.get("%s.json" % self.varName)

  @property
  def data(self):
    """ """
    return JsObjects.JsObjects.get("JSON.stringify(%s.json)" % self.varName)
