from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class DomSnackbar(JsHtml.JsHtmlRich):

  def isOpen(self) -> JsObjects.JsBoolean.JsBoolean:
    """
    Description:
    -----------
    Returns whether the snackbar is open.

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-snackbar
    """
    return JsObjects.JsBoolean.JsBoolean.get("window['%s'].isOpen()" % self.component.htmlCode)

  def open(self):
    """
    Description:
    -----------
    Opens the snackbar.

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-snackbar
    """
    return JsUtils.jsWrap("window['%s'].open()" % self.component.htmlCode)

  def close(self, reason: str = None):
    """
    Description:
    -----------
    Closes the snackbar, optionally with the specified action indicating why it was closed.

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-snackbar

    Attributes:
    ----------
    :param reason:
    """
    if reason is None:
      return JsUtils.jsWrap("window['%s'].close()" % self.component.htmlCode)

    reason = JsUtils.jsConvertData(reason, None)
    return JsUtils.jsWrap("window['%s'].close(%s)" % (self.component.htmlCode, reason))
