from typing import Union
from epyk.core.py import primitives
from epyk.core.py import types
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects

class QuillClipboard:
    def __init__(self, page, varId):
        self.page = page
        self.varId = varId

    def addMatcher(self, selector: Union[str, int], js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
        """Adds a custom matcher to the Clipboard. Matchers using nodeType are called first, in the order they were
        added, followed by matchers using a CSS selector, also in the order they were added. nodeType may be
        Node.ELEMENT_NODE or Node.TEXT_NODE.

        :param selector:
        :param js_funcs:
        :param profile:
        """
        return JsUtils.jsWrap("%s.clipboard.addMatcher(%s, (node, delta) => {%s})" % (
            self.varId, JsUtils.jsConvertData(selector, None),
            JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

    def dangerouslyPasteHTML(self, i, source: str):
        """Inserts content represented by HTML snippet into editor at a given index.

        :param i:
        :param source:
        """
        i = JsUtils.jsConvertData(i, None)
        source = JsUtils.jsConvertData(source, None)
        return JsUtils.jsWrap("%s.clipboard.dangerouslyPasteHTML(%s, %s)" % (i, source))


class QuillKeyboard:

    def __init__(self, page, varId):
        self.page = page
        self.varId = varId

    def addBinding(self, keys: dict, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
        """Adds a custom matcher to the Clipboard.

        :param keys:
        :param js_funcs:
        :param profile:
        """
        return JsUtils.jsWrap("%s.keyboard.addBinding(%s, function(range, context) {%s})" % (
            self.varId, JsUtils.jsConvertData(keys, None),
            JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))


class QuillHistory:

    def __init__(self, page, varId):
        self.page = page
        self.varId = varId

    def clear(self):
        """Clears the history stack. """
        return JsUtils.jsWrap("%s.history.clear()" % self.varId)

    def cutoff(self):
        """Normally changes made in short succession (configured by delay) are merged as a single change, so that
        triggering an undo will undo multiple changes. Using cutoff() will reset the merger window so that a changes before
        and after cutoff() is called will not be merged."""
        return JsUtils.jsWrap("%s.history.cutoff()" % self.varId)

    def undo(self):
        """Undo last change."""
        return JsUtils.jsWrap("%s.history.undo()" % self.varId)

    def redo(self):
        """If last change was an undo, redo this undo. Otherwise does nothing."""
        return JsUtils.jsWrap("%s.history.redo()" % self.varId)


class Quill(JsPackage):
    lib_alias = {"js": "quill", 'css': "quill"}

    def deleteText(self):
        """Binds event-handling function.
        `Quill <https://quilljs.com/docs/api#deletetext>`_

        """
        return JsUtils.jsWrap("%s.deleteText()" % self.varId)

    def getContents(self, index: int = 0, length: int = None):
        """Retrieves contents of the editor, with formatting data, represented by a Delta object.
        `Quill <https://quilljs.com/docs/api#getcontents>`_

        :param index:
        :param length:
        """
        if not length:
            return JsUtils.jsWrap("%s.getContents(%s)" % (self.varId, index))

        return JsUtils.jsWrap("%s.getContents(%s, %s)" % (self.varId, index, length))

    def getLength(self) -> JsObjects.JsNumber.JsNumber:
        """Retrieves the length of the editor contents. Note even when Quill is empty, there is still a blank line
        represented by '\n', so getLength will return 1.
        `Quill <https://quilljs.com/docs/api#getLength>`_
        """
        return JsObjects.JsNumber.JsNumber.get("%s.getLength()" % self.varId)

    def getText(self, index: int = 0, length: int = None):
        """Retrieves the string contents of the editor. Non-string content are omitted, so the returned string's length
        may be shorter than the editor's as returned by getLength.
        `Quill <https://quilljs.com/docs/api#gettext>`_

        :param index:
        :param length:
        """
        if not length:
            return JsUtils.jsWrap("%s.getText(%s)" % (self.varId, index))

        return JsUtils.jsWrap("%s.getText(%s, %s)" % (self.varId, index, length))

    def getSemanticHTML(self, index: int = 0, length: int = None):
        """Get the HTML representation of the editor contents. This method is useful for exporting the contents of the
        editor in a format that can be used in other applications.
        `Quill <https://quilljs.com/docs/api#getsemantichtml>`_

        :param index:
        :param length:
        """
        if not length:
            return JsUtils.jsWrap("%s.getSemanticHTML(%s)" % (self.varId, index))

        return JsUtils.jsWrap("%s.getSemanticHTML(%s, %s)" % (self.varId, index, length))

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
        return JsUtils.jsWrap("%s.insertEmbed(%s, %s, %s, %s)" % (self.varId, index, type, value, source))

    def setText(self, text, source: str = "api"):
        """Sets contents of editor with given text, returning a Delta representing the change.
        `Quill <https://quilljs.com/docs/api#settext>`_

        :param text:
        :param source:
        """
        text = JsUtils.jsConvertData(text, None)
        source = JsUtils.jsConvertData(source, None)
        return JsUtils.jsWrap("%s.setText(%s, %s)" % (self.varId, text, source))

    @property
    def history(self) -> QuillHistory:
        """The History module is responsible for handling undo and redo for Quill. It can be configured with the
        following options:"""
        return QuillHistory(self.page, self.varId)

    @property
    def keyboard(self) -> QuillKeyboard:
        """The Keyboard module enables custom behavior for keyboard events in particular contexts. Quill uses this to
        bind formatting hotkeys and prevent undesirable browser side effects."""
        return QuillKeyboard(self.page, self.varId)

    @property
    def clipboard(self) -> QuillKeyboard:
        """"""
        return QuillClipboard(self.page, self.varId)
