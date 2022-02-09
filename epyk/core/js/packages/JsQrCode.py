#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class QrCode(JsPackage):
  lib_alias = {"js": "qrcodejs", 'css': "qrcodejs"}

  def clear(self):
    """
    Description:
    ------------
    Clear the code.

    Usage:
    -----

      qrcode = page.ui.qrcode()
      button = page.ui.button("Clear")
      button.click([qrcode.js.clear()])

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/
    """
    return JsObjects.JsObjects.get('%s.clear()' % self.varName)

  def makeCode(self, data: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    Make another code.

    Usage:
    -----

      qrcode = page.ui.qrcode()
      button = page.ui.button("Write Test")
      button.click([qrcode.js.makeCode("Test")])

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :param Union[str, primitives.JsDataModel] data: The text to be used to build to code.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get('%s.makeCode(%s)' % (self.varName, data))
