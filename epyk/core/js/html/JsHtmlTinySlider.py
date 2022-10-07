#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class JsInfo:

  def __init__(self, component: primitives.HtmlModel):
    self.component = component
    self.varName = "info"

  def set(self, js_code: str = "info"):
    """  
    Set the slider info variable on the JavaScript side.
    This is not mandatory in a Slider event as it is already passed in the event function.
 
    :param str js_code: Optional. The slider info variable name. Default info.
    """
    self.varName = js_code
    return JsObjects.JsVoid("var %s = %s.getInfo()" % (js_code, self.component.jsonId))

  @property
  def index(self):
    """  
    Get the slider current index (starts from 1).
    """
    return JsObjects.JsNumber.JsNumber.get("%s.index" % self.varName)

  @property
  def indexCached(self):
    """  
    Get the slider past index.
    """
    return JsObjects.JsNumber.JsNumber.get("%s.indexCached" % self.varName)

  @property
  def displayIndex(self):
    """  
    display index starts from 1.
    """
    return JsObjects.JsNumber.JsNumber.get("%s.displayIndex" % self.varName)

  @property
  def containerId(self):
    """  
    Get the container ID.
    """
    return JsObjects.JsString.JsString.get("%s.container.Id" % self.varName)

  @property
  def slideCount(self):
    """  
    Get the slider views count.
    """
    return JsObjects.JsNumber.JsNumber.get("%s.slideCount" % self.varName)

  @property
  def slideCountNew(self):
    """  

    """
    return JsObjects.JsNumber.JsNumber.get("%s.slideCountNew" % self.varName)

  def slideItems(self, n: int = 0):
    """  
    Get an item in the slider.
 
    :param int n: Optional. The index of the slide to be retrieved in the slider object.
    """
    return JsObjects.JsNodeDom.JsDoms.get("%s.slideItems[%s]" % (self.varName, n))

  @property
  def isOn(self):
    """  

    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.isOn" % self.varName)

  @property
  def hasControls(self):
    """  

    """
    return JsObjects.JsBoolean.JsBoolean.get("%s.hasControls" % self.varName)

  @property
  def navCurrentIndex(self):
    """  

    """
    return JsObjects.JsNumber.JsNumber.get("%s.navCurrentIndex" % self.varName)

  @property
  def navCurrentIndexCached(self):
    """  

    """
    return JsObjects.JsNumber.JsNumber.get("%s.navCurrentIndexCached" % self.varName)

  @property
  def nextButton(self):
    """  
    Get the slider next button DOM object.
    """
    return JsObjects.JsNodeDom.JsDoms.get("%s.nextButton" % self.varName)

  @property
  def prevButton(self):
    """  
    Return the slider previous button DOM object.
    """
    return JsObjects.JsNodeDom.JsDoms.get("%s.prevButton" % self.varName)

  def toStr(self):
    return self.varName


class JsHtmlTinySlider(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """  
    Get the current index in the tiny slider.
    """
    return JsHtml.ContentFormatters(self.page, "%s.getInfo().index" % self.component.jsonId)

  @property
  def info(self):
    """  

    """
    return JsInfo(self.component)
