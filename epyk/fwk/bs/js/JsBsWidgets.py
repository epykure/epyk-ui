
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class Modal(JsPackage):

  def hide(self):
    return JsUtils.jsWrap("%s.checked = true" % self.component.dom.varName)


class OffCanvas(JsPackage):

  def hide(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/#methods
    """
    return JsUtils.jsWrap("%s.hide()" % self.varName)

  def toggle(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/#methods
    """
    return JsUtils.jsWrap("%s.toggle()" % self.varName)

  def show(self):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/#methods
    """
    return JsUtils.jsWrap("%s.show()" % self.varName)
