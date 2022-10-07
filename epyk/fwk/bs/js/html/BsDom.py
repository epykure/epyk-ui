#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class Modal(JsHtml.JsHtmlRich):
  name = "Bootstrap Modal"

  def toggle(self):
    """  
    Manually toggles a modal. Returns to the caller before the modal has actually been shown or hidden
    (i.e. before the shown.bs.modal or hidden.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('toggle')" % self.component.dom.jquery.varId)

  def show(self):
    """  
    Manually opens a modal. Returns to the caller before the modal has actually been shown
    (i.e. before the shown.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('show')" % self.component.dom.jquery.varId)

  def hide(self):
    """  
    Manually hides a modal. Returns to the caller before the modal has actually been hidden
    (i.e. before the hidden.bs.modal event occurs).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('hide')" % self.component.dom.jquery.varId)

  def handleUpdate(self):
    """  
    Manually readjust the modal’s position if the height of a modal changes while it is open
    (i.e. in case a scrollbar appears).

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('handleUpdate')" % self.component.dom.jquery.varId)

  def dispose(self):
    """  
    Destroys an element’s modal.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return JsObjects.JsObjects.get("%s.modal('handleUpdate')" % self.component.dom.jquery.varId)
