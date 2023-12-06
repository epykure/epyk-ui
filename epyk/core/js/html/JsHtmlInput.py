#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Inputs(JsHtml.JsHtml):

    def autocomplete(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns the value of the autocomplete attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_autocomplete.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.autocomplete" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.autocomplete = %s" % (self.component.dom.varName, data))

    def autofocus(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns whether a text field should automatically get focus when the page loads.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_autofocus.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.autofocus" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.autofocus = %s" % (self.component.dom.varName, data))

    def defaultValue(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns the default value of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_defaultvalue.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.defaultValue" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.defaultValue = %s" % (self.component.dom.varName, data))

    def disabled(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns whether the text field is disabled, or not.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_disabled.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.disabled" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.disabled = %s" % (self.component.dom.varName, data))

    def maxLength(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns the value of the maxlength attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_maxlength.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.maxLength" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.maxLength = %s" % (self.component.dom.varName, data))

    def pattern(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns the value of the pattern attribute of a text field.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_pattern.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.pattern" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.pattern = %s" % (self.component.dom.varName, data))

    def placeholder(self, data: types.JS_DATA_TYPES = None):
        """Set or get the placeholder for an HTML component.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_placeholder.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.placeholder" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.placeholder = %s" % (self.component.dom.varName, data))

    def readOnly(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns whether a text field is read-only, or not.

        Related Pages:

            https://www.w3schools.com/jsref/prop_text_readonly.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.readOnly" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.readOnly = %s" % (self.component.dom.varName, data))

    def required(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns whether the text field must be filled out before submitting a form.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_required.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.required" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.required = %s" % (self.component.dom.varName, data))

    def size(self, data: types.JS_DATA_TYPES = None):
        """Sets or returns the value of the size attribute of a text field.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_size.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.size" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.size = %s" % (self.component.dom.varName, data))

    def name(self, data: types.JS_DATA_TYPES = None):
        """Set or get the placeholder for an HTML component.

        Related Pages:

          https://www.w3schools.com/jsref/prop_text_name.asp

        :param data: A String corresponding to a JavaScript object.
        """
        if data is None:
            return JsObjects.JsString.JsString.get("%s.name" % self.component.dom.varName)

        data = JsUtils.jsConvertData(data, None)
        return JsUtils.jsWrap("%s.name = %s" % (self.component.dom.varName, data))

    @property
    def valid(self):
        """ Return the overall input validity flag """
        return JsObjects.JsBoolean.JsBoolean.get("%s.validity.valid" % self.component.dom.varName)

    @property
    def validationMessage(self):
        """ Contains the message a browser will display when the validity is false. """
        return JsObjects.JsObject.JsObject.get("%s.validationMessage" % self.component.dom.varName)

    @property
    def validity(self):
        """ Get the input validity object """
        return JsObjects.JsObject.JsObject.get("%s.validity" % self.component.dom.varName)

    def checkValidity(self):
        """The HTMLSelectElement.checkValidity() method checks whether the element has any constraints and whether
        it satisfies them. If the element fails its constraints, the browser fires a cancelable invalid event at the
        element, and then returns false.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/checkValidity
        """
        return JsObjects.JsObject.JsObject.get("%s.checkValidity()" % self.component.dom.varName)

    def reportValidity(self):
        """The HTMLFormElement.reportValidity() method returns true if the element's child controls satisfy their
        validation constraints. When false is returned, cancelable invalid events are fired for each invalid child and
        validation problems are reported to the user.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/reportValidity
        """
        return JsObjects.JsObject.JsObject.get("%s.reportValidity()" % self.component.dom.varName)

    def validity_state(self):
        """Get the input validity state """
        return JsObjects.JsString.JsString.get("(function(inpForm){for (var key in inpForm.validity){if(inpForm.validity[key]){return key}}})(%s)" % self.component.dom.varName)

    def setCustomValidity(self, label: types.JS_DATA_TYPES = None, invalid_cls: str = None):
        """Sets the validationMessage property of an input element

        Related Pages:

          https://www.w3schools.com/js/js_validation_api.asp
        """
        if invalid_cls is None:
            invalid = "invalid"
            self.page.properties.css.add_text(".invalid {border-color: red !important}", "inval_input")
        return JsUtils.jsWrap("if(%(text)s){%(id)s.classList.add(%(cls)s); %(id)s.setCustomValidity(%(text)s)} else {%(id)s.classList.remove(%(cls)s); %(id)s.setCustomValidity('')}" % {
            "id": self.component.dom.varName, "text": JsUtils.jsConvertData(label, None),
            "cls": JsUtils.jsConvertData(invalid, None)})


class InputFileDom:

    def __init__(self, selector, page, component):
        self.varId = selector
        self.component = component
        self.page = page

    @property
    def name(self):
        """Returns the name of the file referenced by the File object.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.name" % self.varId)

    @property
    def lastModified(self):
        """Returns the last modified time of the file, in millisecond since the UNIX epoch (January 1st, 1970 at Midnight).

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.lastModified" % self.varId)

    @property
    def lastModifiedDate(self):
        """Returns the last modified Date of the file referenced by the File object.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsDate.JsDate.get("%s.lastModifiedDate" % self.varId)

    @property
    def size(self):
        """Returns the size of the file in bytes.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsNumber.JsNumber.get("%s.size" % self.varId)

    @property
    def type(self):
        """Returns the MIME type of the file.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/File
        """
        return JsObjects.JsString.JsString.get("%s.type" % self.varId)

    @property
    def webkitRelativePath(self):
        """Returns the path the URL of the File is relative to.

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
        """The files property returns a FileList object, representing the file or files selected with the file
        upload button.

        Related Pages:

            https://www.w3schools.com/jsref/prop_fileupload_files.asp
        """
        return InputFilesList(self.varId, page=self.page, component=self.component)
