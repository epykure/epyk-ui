

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class _Export:

  @property
  def region(self):
    """

    """
    return JsObjects.JsString.JsString.get("region")

  @property
  def code(self):
    """

    """
    return JsObjects.JsString.JsString.get("code")

  @property
  def element(self):
    """

    """
    return JsObjects.JsString.JsString.get("element")
