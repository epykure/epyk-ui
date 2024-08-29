from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsObject


class JsDOMRect:

    def __init__(self, js_code: str, unit: bool = False):
        self.varId = js_code
        self.unit = unit

    def setVar(self, js_code: str, var_type: str = "var"):
        return JsObject.JsObject("%s %s = %s" % (var_type, js_code, self.varId))

    @property
    def x(self):
        """The x read-only property of the DOMRectReadOnly interface represents the x coordinate of the DOMRect's origin.
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/x>`_
        """
        if self.unit:
            return JsString.JsString("%s.x + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.x" % self.varId)

    @property
    def y(self):
        """The y read-only property of the DOMRectReadOnly interface represents the y coordinate of the DOMRect's origin.
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/y>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.y + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.y" % self.varId)

    @property
    def width(self):
        """The width read-only property of the DOMRectReadOnly interface represents the width of the DOMRect.
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/width>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.width + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.width" % self.varId)

    @property
    def height(self):
        """The height read-only property of the DOMRectReadOnly interface represents the height of the DOMRect.
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/height>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.height + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.height" % self.varId)

    @property
    def top(self):
        """The top read-only property of the DOMRectReadOnly interface returns the top coordinate value of the DOMRect.
        (Has the same value as y, or y + height if height is negative.)
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/top>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.top + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.top" % self.varId)

    @property
    def right(self):
        """The right read-only property of the DOMRectReadOnly interface returns the right coordinate value of the DOMRect.
        (Has the same value as x + width, or x if width is negative.)
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/right>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.right + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.right" % self.varId)

    @property
    def bottom(self):
        """The bottom read-only property of the DOMRectReadOnly interface returns the bottom coordinate value of the DOMRect.
        (Has the same value as y + height, or y if height is negative.)
        `mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/bottom>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.bottom + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.bottom" % self.varId)

    @property
    def left(self):
        """The left read-only property of the DOMRectReadOnly interface returns the left coordinate value of the DOMRect.
        (Has the same value as x, or x + width if width is negative.)
        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/DOMRectReadOnly/left>`_
        """
        if self.unit:
            return JsString.JsString.get("%s.left + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.left" % self.varId)

    @property
    def window_left(self):
        """

        """
        if self.unit:
            return JsString.JsString.get("%s.left + window.scrollX + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.left + window.scrollX" % self.varId)

    @property
    def window_top(self):
        """

        """
        if self.unit:
            return JsString.JsString.get("%s.top + window.scrollY + 'px'" % self.varId)

        return JsNumber.JsNumber("%s.top + window.scrollY" % self.varId)
