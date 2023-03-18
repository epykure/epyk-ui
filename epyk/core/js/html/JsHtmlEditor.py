#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from typing import Union
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class Console(JsHtml.JsHtmlRich):

  def write(self, data, timestamp=None, stringify: bool = False, skip_data_convert: bool = False, format: str = None,
            profile: Union[bool, dict] = False):
    """

    :param data:
    :param timestamp:
    :param profile:
    :param stringify:
    :param skip_data_convert:
    :param format: A string output format using %s to define the data in the string
    """
    js_data = data if skip_data_convert else JsUtils.jsConvertData(data, None)
    if stringify:
      js_data = "JSON.stringify(%s)" % js_data
    if self.component.options.showdown is not False:
      js_data = '''
        (function(d){ var conv = new showdown.Converter(%s);
            let frag = document.createRange().createContextualFragment(conv.makeHtml(d)); 
            if((frag.firstChild === null) || (typeof frag.firstChild.style == "undefined")){return d}
            else{frag.firstChild.style.display = 'inline-block';frag.firstChild.style.margin = 0 ;  
                 return frag.firstChild.outerHTML}})(%s) ''' % (json.dumps(self.component.options.showdown), js_data)
    if format is not None:
      js_data = JsUtils.jsConvertData(format, None).toStr().replace("%s", '"+ %s +"') % js_data
    if timestamp or (self.component.options.timestamp and timestamp != False):
      return JsObjects.JsObjects.get(
        "%s.innerHTML += ' > '+ new Date().toISOString().replace('T', ' ').slice(0, 19) +', '+ %s +'<br/>'" % (
          self.varName, js_data))

    return JsObjects.JsObjects.get("%s.innerHTML += ' > '+ %s +'<br/>'" % (self.component.dom.varId, js_data))

  def clear(self):
    """ Clear the editor. """
    return JsObjects.JsObjects.get('%s.innerHTML = ""' % self.varName)


class Editor(JsHtml.JsHtmlRich):

  def timestamp(self):
    """ Update the editor timestamp. """
    return self.querySelector("span").innerHTML(JsObjects.JsDate.JsDate().getStrTimeStamp())


class CodeMirror(JsHtml.JsHtmlRich):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "%s.getWrapperElement()" % component.editorId, "", None
    self.component, self.page = component, page
    self._js = []
    self._jquery, self._jquery_ui, self._d3 = None, None, None

  @property
  def content(self):
    """ Get the editor content. """
    return JsHtml.ContentFormatters(self.page, "%s.getValue()" % self.component.editorId)

  def select(self) -> JsObjects.JsObject:
    """ Select the whole content of the editor.

    Related Pages:

      https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('selectAll')" % self.component.editorId)

  def singleSelection(self) -> JsObjects.JsObject:
    """ When multiple selections are present, this deselects all but the primary selection.

    Related Pages:

      https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('singleSelection')" % self.component.editorId)

  def killLine(self) -> JsObjects.JsObject:
    """ Emacs-style line killing. Deletes the part of the line after the cursor.

    If that consists only of whitespace, the newline at the end of the line is also deleted.

    Related Pages:

      https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('killLine')" % self.component.editorId)

  def deleteLine(self) -> JsObjects.JsObject:
    """ Deletes the whole line under the cursor, including newline at the end.

    Related Pages:

      https://codemirror.net/3/doc/manual.html#keymaps
    """
    return JsObjects.JsObjects.get("%s.execCommand('deleteLine')" % self.component.editorId)

  def copy(self) -> JsObjects.JsObject:
    """ Copy the editor content. """
    return JsObjects.JsObjects.get("%s.execCommand('copy')" % self.component.editorId)

  def setValue(self, data: Union[str, primitives.JsDataModel, float, dict, list]) -> JsObjects.JsObject:
    """ Set the editor content.

    :param data: The value to put in the editor
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get("%s.setValue(%s)" % (self.component.editorId, data))

  def setOption(self, name: Union[str, primitives.JsDataModel, float, dict, list],
                value: Union[str, primitives.JsDataModel, float, dict, list]) -> JsObjects.JsObject:
    """ Set specific options to the editor.

    :param name: The option's name
    :param value: The option's value
    """
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.setOption(%s, %s)" % (self.component.editorId, name, value))

  def refresh(self) -> JsUtils.jsWrap:
    """ Refresh the Editor's content """
    return JsUtils.jsWrap("%s.refresh()" % self.component.editorId)

  def clear(self) -> JsUtils.jsWrap:
    """ Clear the editor's content. """
    return JsUtils.jsWrap('%s.setValue("")' % self.component.editorId)

  def empty(self) -> JsUtils.jsWrap:
    """ Empty the editor. """
    return JsUtils.jsWrap('%s.setValue("")' % self.component.editorId)

  def appendText(self, text: Union[str, primitives.JsDataModel], from_selection: bool = True) -> JsObjects.JsVoid:
    """ Append test to the editor's content.

    :param text: The text to append
    :param from_selection: Optional
    """
    text = JsUtils.jsConvertData(text, None)
    from_selection = JsUtils.jsConvertData(from_selection, None)
    return JsObjects.JsVoid(r'''
      var editContent = %(editor)s.getDoc();
      var editCursor = editContent.getCursor();
      if (%(toEnd)s){editContent.replaceRange("\n" + %(text)s, {line: editContent.size})}
      else {editContent.replaceRange("\n" + %(text)s, {line: editCursor.line})}
      ''' % {"editor": self.component.editorId, "text": text, "toEnd": from_selection})
