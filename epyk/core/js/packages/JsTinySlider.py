#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class TinySlider(JsPackage):
  lib_alias = {"js": "tiny-slider", 'css': "tiny-slider"}

  def goTo(self, n: int):
    """
    Go to specific slide by number or keywords.
 
    :param int n: the depth of the tree at start.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.goTo(%s)' % (self.varName, n))

  def getInfo(self):
    """
    Get slider information.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.getInfo()' % self.varName)

  def next(self):
    """
    Go to specific slide by number or keywords.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.goTo("next")' % self.varName)

  def previous(self):
    """
    Go to specific slide by number or keywords.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.goTo("previous")' % self.varName)

  def last(self):
    """
    Go to specific slide by number or keywords.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.goTo("last")' % self.varName)

  def first(self):
    """
    Go to specific slide by number or keywords.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.goTo("first")' % self.varName)

  def pause(self):
    """
    Programmatically stop slider autoplay when autoplay: true.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.pause()' % self.varName)

  def play(self):
    """
    Programmatically start slider autoplay when autoplay: true.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.play()' % self.varName)

  def updateSliderHeight(self):
    """
    Manually adjust slider height when autoHeight is true.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.updateSliderHeight()' % self.varName)

  def destroy(self):
    """
    Destroy the slider.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.destroy()' % self.varName)

  def rebuild(self):
    """
    Rebuild the slider after destroy.

    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
    """
    return JsObjects.JsObjects.get('%s.rebuild()' % self.varName)
