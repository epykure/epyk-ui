
from typing import Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Quill(JsPackage):
  lib_alias = {"js": "quill", 'css': "quill"}

  def deleteText(self):
    """Binds event-handling function.
    `Quill <https://quilljs.com/docs/api#deletetext>`_

    """
    return JsUtils.jsWrap("%s.deleteText()" % self.varName)

  def getContents(self, index: int = 0, length: int = None):
    """Retrieves contents of the editor, with formatting data, represented by a Delta object.
    `Quill <https://quilljs.com/docs/api#getcontents>`_

    :param index:
    :param length:
    """
    if not length:
      return JsUtils.jsWrap("%s.getContents(%s)" % (self.varName, index))

    return JsUtils.jsWrap("%s.getContents(%s, %s)" % (self.varName, index, length))

  def getLength(self) -> JsObjects.JsNumber.JsNumber:
    """Retrieves the length of the editor contents. Note even when Quill is empty, there is still a blank line
    represented by '\n', so getLength will return 1.
    `Quill <https://quilljs.com/docs/api#getLength>`_
    """
    return JsObjects.JsNumber.JsNumber.get("%s.getLength()" % self.varName)

  def getText(self, index: int = 0, length: int = None):
    """Retrieves the string contents of the editor. Non-string content are omitted, so the returned string's length
    may be shorter than the editor's as returned by getLength.
    `Quill <https://quilljs.com/docs/api#gettext>`_

    :param index:
    :param length:
    """
    if not length:
      return JsUtils.jsWrap("%s.getText(%s)" % (self.varName, index))

    return JsUtils.jsWrap("%s.getText(%s, %s)" % (self.varName, index, length))

  def getSemanticHTML(self, index: int = 0, length: int = None):
    """Get the HTML representation of the editor contents. This method is useful for exporting the contents of the
    editor in a format that can be used in other applications.
    `Quill <https://quilljs.com/docs/api#getsemantichtml>`_

    :param index:
    :param length:
    """
    if not length:
      return JsUtils.jsWrap("%s.getSemanticHTML(%s)" % (self.varName, index))

    return JsUtils.jsWrap("%s.getSemanticHTML(%s, %s)" % (self.varName, index, length))

  def insertEmbed(self, index: int, type: str, value, source: str = "api"):
    """Insert embedded content into the editor, returning a Delta representing the change. Source may be "user", "api",
    or "silent". Calls where the source is "user" when the editor is disabled are ignored.
    `Quill <https://quilljs.com/docs/api#insertembed>`_

    :param index:
    :param type:
    :param value:
    :param source:
    """
    type = JsUtils.jsConvertData(type, None)
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.insertEmbed(%s, %s, %s, %s)" % (self.varName, index, type, value, source))

  def setText(self, text, source: str = "api"):
    """Sets contents of editor with given text, returning a Delta representing the change.
    `Quill <https://quilljs.com/docs/api#settext>`_

    :param text:
    :param source:
    """
    text = JsUtils.jsConvertData(text, None)
    source = JsUtils.jsConvertData(source, None)
    return JsUtils.jsWrap("%s.setText(%s, %s)" % (self.varName, text, source))
