#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Inputs(JsHtml.JsHtml):

    def autocomplete(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns the value of the autocomplete attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_autocomplete.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.autocomplete" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.autocomplete = %s" % (self.component.dom.varName, data))

    def autofocus(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns whether a text field should automatically get focus when the page loads.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_autofocus.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.autofocus" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.autofocus = %s" % (self.component.dom.varName, data))

    def defaultValue(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns the default value of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_defaultvalue.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.defaultValue" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.defaultValue = %s" % (self.component.dom.varName, data))

    def disabled(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns whether the text field is disabled, or not.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_disabled.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.disabled" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.disabled = %s" % (self.component.dom.varName, data))

    def maxLength(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns the value of the maxlength attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_maxlength.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.maxLength" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.maxLength = %s" % (self.component.dom.varName, data))

    def pattern(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns the value of the pattern attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_pattern.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.pattern" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.pattern = %s" % (self.component.dom.varName, data))

    def placeholder(self, data: types.JS_DATA_TYPES = None):
        """
        Set or get the placeholder for an HTML component.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_placeholder.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.placeholder" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.placeholder = %s" % (self.component.dom.varName, data))

    def readOnly(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns whether a text field is read-only, or not.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_readonly.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.readOnly" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.readOnly = %s" % (self.component.dom.varName, data))

    def required(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns whether the text field must be filled out before submitting a form.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_required.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.required" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.required = %s" % (self.component.dom.varName, data))

    def size(self, data: types.JS_DATA_TYPES = None):
        """
        Sets or returns the value of the size attribute of a text field.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_size.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.size" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.size = %s" % (self.component.dom.varName, data))

    def name(self, data: types.JS_DATA_TYPES = None):
        """
        Set or get the placeholder for an HTML component.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_name.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.name" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.name = %s" % (self.component.dom.varName, data))


class InputFileDom:

    def __init__(self, selector, page, component):
        self.varId = selector
        self.component = component
        self.page = page

    @property
    def name(self):
        """
        Returns the name of the file referenced by the File object.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.name" % self.varId)

    @property
    def lastModified(self):
        """
        Returns the last modified time of the file, in millisecond since the UNIX epoch (January 1st, 1970 at Midnight).

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.lastModified" % self.varId)

    @property
    def lastModifiedDate(self):
        """
        Returns the last modified Date of the file referenced by the File object.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsDate.JsDate.get("%s.lastModifiedDate" % self.varId)

    @property
    def size(self):
        """
        Returns the size of the file in bytes.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsNumber.JsNumber.get("%s.size" % self.varId)

    @property
    def type(self):
        """
        Returns the MIME type of the file.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.type" % self.varId)

    @property
    def webkitRelativePath(self):
        """
        Returns the path the URL of the File is relative to.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.webkitRelativePath" % self.varId)

    def toStr(self):
        return JsObjects.JsArray.JsArray.get(self.varId)


class InputFilesList:

    def __init__(self, selector, page, component):
        self.varId = selector
        self.component = component
        self.page = page

    def __getitem__(self, x) -> InputFileDom:
        return InputFileDom("%s.files[%s]" % (self.varId, x), page=self.page, component=self.component)

    def toStr(self):
        return JsObjects.JsArray.JsArray.get("%s.files" % self.varId)


class InputFiles(Inputs):

    @property
    def files(self):
        """
        The files property returns a FileList object, representing the file or files selected with the file
        upload button.

        Related Pages:

            https://www.w3schools.com/jsref/prop_fileupload_files.asp
        """
        return InputFilesList(self.varId, page=self.page, component=self.component)
