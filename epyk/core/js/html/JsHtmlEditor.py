
import json

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class Console(JsHtml.JsHtmlRich):

  def write(self, data, timestamp=None, stringify=False, skip_data_convert=False, format=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param timestamp:
    :param profile:
    :param stringify:
    :param skip_data_convert:
    :param format: String. A string output format using %s to define the data in the string
    """
    js_data = data if skip_data_convert else JsUtils.jsConvertData(data, None)
    if stringify:
      js_data = "JSON.stringify(%s)" % js_data
    if self._src.options.showdown is not False:
      js_data = '''
        (function(d){ var conv = new showdown.Converter(%s);
            let frag = document.createRange().createContextualFragment(conv.makeHtml(d)); 
            if((frag.firstChild === null) || (typeof frag.firstChild.style == "undefined")){return d}
            else{frag.firstChild.style.display = 'inline-block';frag.firstChild.style.margin = 0 ;  
                 return frag.firstChild.outerHTML}})(%s) ''' % (json.dumps(self._src.options.showdown), js_data)
    if format is not None:
      js_data = JsUtils.jsConvertData(format, None).toStr().replace("%s", '"+ %s +"') % js_data
    if timestamp or (self._src.options.timestamp and timestamp != False):
      return JsObjects.JsObjects.get("%s.innerHTML += ' > '+ new Date().toISOString().replace('T', ' ').slice(0, 19) +', '+ %s +'<br/>'" % (self.varName, js_data))

    return JsObjects.JsObjects.get("%s.innerHTML += ' > '+ %s +'<br/>'" % (self._src.dom.varId, js_data))

  def clear(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get('%s.innerHTML = ""' % self.varName)


class Editor(JsHtml.JsHtmlRich):

  def timestamp(self):
    """
    Description:
    ------------
    Update the editor timestamp
    """
    return self.querySelector("span").innerHTML(JsObjects.JsDate.JsDate().getStrTimeStamp())


class CodeMirror(JsHtml.JsHtmlRich):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "%s.getWrapperElement()" % htmlObj.editorId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui, self._d3 = None, None, None

  @property
  def content(self):
    """
    Description:
    -----------

    :return:
    """
    return JsHtml.ContentFormatters(self._report, "%s.getValue()" % self._src.editorId)

  def select(self):
    """
    Description:
    -----------
    Select the whole content of the editor.

    Related Pages:
    --------------
    https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('selectAll')" % self._src.editorId)

  def singleSelection(self):
    """
    Description:
    -----------
    When multiple selections are present, this deselects all but the primary selection.

    Related Pages:
    --------------
    https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('singleSelection')" % self._src.editorId)

  def killLine(self):
    """
    Description:
    -----------
    Emacs-style line killing. Deletes the part of the line after the cursor.
    If that consists only of whitespace, the newline at the end of the line is also deleted.

    Related Pages:
    --------------
    https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('killLine')" % self._src.editorId)

  def deleteLine(self):
    """
    Description:
    -----------
    Deletes the whole line under the cursor, including newline at the end.

    Related Pages:
    --------------
    https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('deleteLine')" % self._src.editorId)

  def copy(self):
    """
    Description:
    -----------
    """
    return JsObjects.JsObjects.get("%s.execCommand('copy')" % self._src.editorId)

  def setValue(self, data):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:

    :return:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get("%s.setValue(%s)" % (self._src.editorId, data))

  def setOption(self, name, value):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param value:

    :return:
    """
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.setOption(%s, %s)" % (self._src.editorId, name, value))

  def refresh(self):
    """
    Description:
    -----------

    :return:
    """
    return JsObjects.JsObjects.get("%s.refresh()" % self._src.editorId)

  def clear(self):
    """
    Description:
    -----------

    :return:
    """
    return JsObjects.JsObjects.get('%s.setValue("")' % self._src.editorId)

  def empty(self):
    """
    Description:
    -----------

    :return:
    """
    return JsObjects.JsObjects.get('%s.setValue("")' % self._src.editorId)
