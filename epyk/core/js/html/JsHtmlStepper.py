
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects


class Step(JsHtml.JsHtmlRich):
  pass


class Stepper(JsHtml.JsHtmlRich):

  def complete(self, i):
    """

    :param i:
    """
    return ""

  def status(self):
    """

    """
    return ""

  def delete(self, i):
    """

    :param i:
    """
    return ""

  def disable(self, i):
    """

    :param i:
    """
    return ""

  def addItem(self, key, value):
    """

    """
    return ""

  def put(self, i):
    """

    :param i:
    """
    return ""


class Drawer(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsHtml.ContentFormatters(self._report, ''' 
      (function(doms, contents){var index =-1; doms.childNodes.forEach(function(dom, k){if(dom.style.display !== 'none'){index = k}}); 
        if (index >= 0){return contents.childNodes[index].innerHTML} else{return index}  })(%s, %s)
        ''' % (self.querySelector("div[name=drawer_panels]"), self.querySelector("div[name=drawer_content]")))

  def hide(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get(''' 
      (function(doms){doms.childNodes.forEach(function(dom){dom.style.display = 'none'; })})(%s)
      ''' % self.querySelector("div[name=drawer_panels]"))

  def add(self, link, panel=""):
    """
    Description:
    ------------

    :param link:
    :param panel:
    """
    return JsObjects.JsObjects.get('''
      ''' % self.querySelectorAll("[name=drawer_panels]"))

  def delete(self, i):
    """
    Description:
    ------------

    :param link:
    """
    return JsObjects.JsObjects.get(''' 
          %(panel)s.childNodes[%(i)s].remove(); %(drawer)s.childNodes[%(i)s].remove(); 
          ''' % {'panel': self.querySelector("div[name=drawer_panels]"), 'drawer': self.querySelector("div[name=drawer_content]"), 'i': i})
