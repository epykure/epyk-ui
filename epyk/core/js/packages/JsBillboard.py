#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsC3


class Billboard(JsC3.C3):
  lib_alias = {'js': "billboard.js", 'css': 'billboard.js'}

  def export(self):
    """
    Description:
    -----------
    Export chart as an image.

    Related Pages:

      https://naver.github.io/billboard.js/release/latest/doc/Chart.html#export
    """
    return JsObjects.JsVoid("%s.export()" % self._selector)

  def revert(self, target: Union[str, list, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Export chart as an image.

    Related Pages:

      https://naver.github.io/billboard.js/release/latest/doc/Chart.html#export

    Attributes:
    ----------
    :param Union[str, list, primitives.JsDataModel] target: ids to be reverted.
    """
    target = JsUtils.jsConvertData(target, None)
    return JsObjects.JsVoid("%s.revert(%s)" % (self._selector, target))
