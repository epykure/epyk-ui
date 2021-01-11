#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class Modal(JsHtml.JsHtmlRich):
  name = "Bootstrap Modal"

  def toggle(self):
    """
    Description:
    ------------
    Manually toggles a modal. Returns to the caller before the modal has actually been shown or hidden (i.e. before the shown.bs.modal or hidden.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('toggle')" % self._src.dom.jquery.varId)

  def show(self):
    """
    Description:
    ------------
    Manually opens a modal. Returns to the caller before the modal has actually been shown (i.e. before the shown.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('show')" % self._src.dom.jquery.varId)

  def hide(self):
    """
    Description:
    ------------
    Manually hides a modal. Returns to the caller before the modal has actually been hidden (i.e. before the hidden.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('hide')" % self._src.dom.jquery.varId)

  def handleUpdate(self):
    """
    Description:
    ------------
    Manually readjust the modal’s position if the height of a modal changes while it is open (i.e. in case a scrollbar appears).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('handleUpdate')" % self._src.dom.jquery.varId)

  def dispose(self):
    """
    Description:
    ------------
    Destroys an element’s modal.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('handleUpdate')" % self._src.dom.jquery.varId)
