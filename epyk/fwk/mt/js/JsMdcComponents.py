#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsNodeDom


class JsMdcHtml(JsNodeDom.JsDoms):
  css_class = None

  def __init__(self, htmlObj, varName=None):
    self.htmlObj, self.varName = htmlObj, varName or htmlObj.style.varName # because driven from the CSS
    if self.css_class is not None:
      self.htmlObj.attr["class"].add(self.css_class)

  def instantiate(self, html_id=None):
    raise Exception("This should be defined in the sub classes")


class FAB(JsMdcHtml):
  css_class = "mdc-fab"

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id


class Button(JsMdcHtml):
  css_class = "mdc-button"

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id


class ButtonFloating(JsMdcHtml):
  css_class = "mdc-icon-button"

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id

  def unbounded(self, bool):
    """

    https://material.io/develop/web/components/buttons/icon-buttons/

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.unbounded = %s" % (self.varName, bool)


class ButtonToggle(JsMdcHtml):
  css_class = "mdc-icon-button"

  def instantiate(self, html_id=None):
    return "new mdc.iconButton.MDCIconButtonToggle(document.querySelector('%s'))" % html_id

  def setAttr(self):
    return "console.log(%s.foundation_)" % self.varName #.setContent('RRRRR')" % self._selector


class ButtonSwitch(JsMdcHtml):
  css_class = "mdc-switch"

  def instantiate(self, html_id=None):
    return "new mdc.switchControl.MDCSwitch(document.querySelector('%s'))" % html_id

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.checked" % self.varName)

  @property
  def checked(self):
    """
    Description:
    ------------
    Setter/getter for the switch’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checked" % self.varName, isPyData=False)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Setter/getter for the switch’s disabled state

    Related Pages:

      https://material.io/develop/web/components/input-controls/switches/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.disabled" % self.varName, isPyData=False)

  def check(self, bool=True):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param bool: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.checked = %s" % (self.varName, bool)


class MenuSurface(JsMdcHtml):
  css_class = "mdc-menu-surface"

  def instantiate(self, html_id=None):
    return "new mdc.menuSurface.MDCMenuSurface(document.querySelector('%s'))" % html_id


class TabBar(JsMdcHtml):
  css_class = "mdc-tab-bar"

  def instantiate(self, html_id=None):
    return "new mdc.tabBar.MDCTabBar(document.querySelector('%s'))" % html_id

  def getScrollPosition(self):
    """
    Description:
    ------------
    Returns the scroll position of the Tab Scroller

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.getScrollPosition()" % self.varName)

  def getFocusedTabIndex(self):
    """
    Description:
    ------------
    Returns the index of the focused Tab.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.getFocusedTabIndex()" % self.varName)

  def getTabListLength(self):
    """
    Description:
    ------------
    Returns the number of child Tab components.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.getTabListLength()" % self.varName)

  def setActiveTab(self, num):
    """
    Description:
    ------------
    Sets the tab at the given index to be activated.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/

    Attributes:
    ----------
    :param num: index.
    """
    num = JsUtils.jsConvertData(num, None)
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.setActiveTab(%s)" % (self.varName, num))

  def activateTabAtIndex(self, num):
    """
    Description:
    ------------
    Activates the Tab at the given index with the given clientRect.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/

    Attributes:
    ----------
    :param num: index.
    """
    num = JsUtils.jsConvertData(num, None)
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.activateTabAtIndex(%s)" % (self.varName, num))

  def deactivateTabAtIndex(self, num):
    """
    Description:
    ------------
    Deactivates the Tab at the given index.

    Related Pages:

      https://material.io/develop/web/components/tabs/tab-bar/

    Attributes:
    ----------
    :param num: index.
    """
    num = JsUtils.jsConvertData(num, None)
    return JsObjects.JsNumber.JsNumber("%s.foundation_.adapter_.deactivateTabAtIndex(%s)" % (self.varName, num))


class TopBar(JsMdcHtml):
  css_class = "mdc-top-app-bar"

  def instantiate(self, html_id=None):
    return "new mdc.topAppBar.MDCTopAppBar(document.querySelector('%s'))" % html_id


class LinearProgress(JsMdcHtml):

  def instantiate(self, html_id=None):
    return "new mdc.linearProgress.MDCLinearProgress(document.querySelector('%s'))" % html_id

  def setProgress(self, num):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param num: Number.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.progress = %s" % (self.varName, num)

  def setDeterminate(self, bool):
    """
    Description:
    ------------
    Toggles the component between the determinate and indeterminate state.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.determinate = %s" % (self.varName, bool)

  def setBuffer(self, num):
    """
    Description:
    ------------
    Sets the buffer bar to this value. Value should be between [0, 1].

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param num: Number.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.buffer = %s" % (self.varName, num)

  def setReverse(self, bool):
    """
    Description:
    ------------
    Reverses the direction of the linear progress indicator.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.reverse = %s" % (self.varName, bool)


class Select(JsMdcHtml):
  css_class = "mdc-select"

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.value" % self.varName)

  def instantiate(self, html_id=None):
    return "new mdc.select.MDCSelect(document.querySelector('%s'))" % html_id

  def setDisabled(self, bool):
    """
    Updates the disabled state.

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.disabled = %s" % (self.varName, bool)

  def setValue(self, value):
    """

    https://material.io/develop/web/components/input-controls/select-menus/

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.value = %s" % (self.varName, value)

  def getValue(self):
    """

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    return self.content

  def getSelectedIndex(self):
    """
    Returns the index of the currently selected menu item.

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    return JsObjects.JsNumber.JsNumber("%s.selectedIndex" % self.varName)


class List(JsMdcHtml):
  css_class = "mdc-list"

  def instantiate(self, html_id=None):
    return "new mdc.list.MDCList(document.querySelector('%s'))" % html_id

  def singleSelection(self, bool):
    """

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.singleSelection = %s" % (self.varName, bool)


class Line(JsMdcHtml):
  css_class = "mdc-line-ripple"

  def instantiate(self, html_id=None):
    return "new mdc.lineRipple.MDCLineRipple(document.querySelector('%s'))" % html_id


class Chip(JsMdcHtml):
  css_class = "mdc-chip-set"

  def instantiate(self, html_id=None):
    return "new mdc.chips.MDCChipSet(document.querySelector('%s'))" % html_id

  def getSelectChip(self):
    """
    Description:
    ------------
    Proxies to the foundation’s

    Related Pages:

      https://material.io/develop/web/components/chips/
    """
    return JsObjects.JsArray.JsArray("%s.selectedChipIds" % self.varName) # % (self.varName, num)

  def selectChipAtIndex(self, index):
    """
    Description:
    ------------
    Calls MDCChip#setSelectedFromChipSet(selected) on the chip at the given index.
    Will emit a selection event if called with shouldNotifyClients set to true.
    The emitted selection event will be ignored by the MDCChipSetFoundation.

    Related Pages:

      https://material.io/develop/web/components/chips/

    Attributes:
    ----------
    :param num: index.
    """
    index = JsUtils.jsConvertData(index, None)
    return JsObjects.JsObjects.get("%s.foundation_.adapter_.selectChipAtIndex(%s)" % (self.varName, index))

  def getChipListCount(self):
    """
    Description:
    ------------
    Proxies to the foundation’s

    Related Pages:

      https://material.io/develop/web/components/chips/

    """
    return JsObjects.JsArray.JsArray("%s.foundation_.adapter_.getChipListCount()" % self.varName)


class Field(JsMdcHtml):
  css_class = "mdc-form-field"

  def instantiate(self, html_id=None):
    return "new mdc.formField.MDCFormField(document.querySelector('%s'))" % html_id

  def input(self, value):
    """

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.input = %s" % (self.varName, value)


class Icon(JsMdcHtml):
  css_class = "mdc-text-field-icon"

  def instantiate(self, html_id=None):
    return "new mdc.textField.MDCTextFieldIcon(document.querySelector('%s'))" % html_id

  def setDisabled(self, bool):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation.setDisabled(%s)" % (self.varName, bool)

  def setAriaLabel(self, label):
    """
    Description:
    ------------
    Updates the icon’s aria-label.

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    label = JsUtils.jsConvertData(label, None)
    return "%s.foundation.setAriaLabel(%s)" % (self.varName, label)

  def setContent(self, content):
    """
    Description:
    ------------
    Updates the icon’s text content

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param content: String.
    """
    content = JsUtils.jsConvertData(content, None)
    return "%s.foundation.setContent(%s)" % (self.varName, content)


class TextNothedOutline(JsMdcHtml):
  css_class = "mdc-text-field--outlined"

  def instantiate(self, html_id=None):
    return "new mdc.notchedOutline.MDCNotchedOutline(document.querySelector('%s'))" % html_id


class TextRipple(JsMdcHtml):
  css_class = "mdc-text-field"

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.value" % self.varName)

  def instantiate(self, html_id=None):
    return "new mdc.textField.MDCTextField(document.querySelector('%s'))" % html_id

  def setDisabled(self, bool=True):
    """
    Description:
    ------------
    Updates the input’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.input_.disabled = %s" % (self.varName, bool)

  def isValid(self):
    """
    Description:
    ------------
    Returns the component’s current validity state (either native or custom, depending on how setUseNativeValidation() was configured).

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.foundation_.adapter_.isValid_" % self.varName, isPyData=False)

  def getValue(self):
    """
    Returns the input’s value.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.value" % self.varName, isPyData=False)

  def setValue(self, value):
    """
    Sets the input’s value.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsBoolean.JsBoolean("%s.value = %s" % (self.varName, value), isPyData=False)


class TextFloating(JsMdcHtml):
  css_class = "mdc-floating-label"

  def instantiate(self, html_id=None):
    return "new mdc.floatingLabel.MDCFloatingLabel(document.querySelector('%s'))" % html_id

  def float(self, bool):
    """
    Description:
    ------------
    Floats or docks the label, depending on the value of shouldFloat.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation_.float(%s)" % (self.varName, bool)

  def shake(self, bool):
    """
    Description:
    ------------
    Shakes or stops shaking the label, depending on the value of shouldShake.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation_.shake(%s)" % (self.varName, bool)

  def getWidth(self):
    """
    Description:
    ------------
    Returns the width of the label element.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getWidth()" % self.varName)


class Radio(JsMdcHtml):
  css_class = "mdc-radio"

  def instantiate(self, html_id=None):
    return "new mdc.radio.MDCRadio(document.querySelector('%s'))" % html_id

  @property
  def val(self):
    """
    Description:
    -----------

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, name: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr(), self.value))

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.checked" % self.varName)

  @property
  def checked(self):
    """
    Description:
    ------------
    Setter/getter for the radio’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checked" % self.varName, isPyData=False)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Setter/getter for the radio’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.disabled" % self.varName, isPyData=False)

  @property
  def value(self):
    """
    Description:
    ------------
    Setter/getter for the radio’s value

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  def check(self, bool=True):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param bool: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.checked = %s" % (self.varName, bool)

  def setDisabled(self, bool=True):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.disabled = %s" % (self.varName, bool)

  def addClass(self, className):
    """
    Description:
    ------------
    Adds a class to the root element

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    className = JsUtils.jsConvertData(className, None)
    return "%s.foundation_.adapter_.addClass(%s)" % (self.varName, className)

  def removeClass(self, className):
    """
    Description:
    ------------
    Removes a class from the root element

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    className = JsUtils.jsConvertData(className, None)
    return "%s.foundation_.adapter_.removeClass(%s)" % (self.varName, className)


class Slider(JsMdcHtml):
  css_class = "mdc-slider"

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.foundation_.getValue()" % self.varName)

  def instantiate(self, html_id=None):
    return "new mdc.slider.MDCSlider(document.querySelector('%s'))" % html_id

  def getValue(self):
    """
    Returns the current value of the slider

    https://material.io/develop/web/components/input-controls/sliders/

    :return:
    """
    return self.content

  def setValue(self, num):
    """
    Description:
    ------------
    Sets the current value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setValue(%s)" % (self.varName, num)

  def getMax(self):
    """
    Description:
    ------------
    Returns the max value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getMax()" % self.varName)

  def setMax(self, num):
    """
    Description:
    ------------
    Returns the max value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setMax(%s)" % (self.varName, num)

  def getMin(self):
    """
    Description:
    ------------
    Returns the min value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getMin()" % self.varName)

  def setMin(self, num):
    """
    Description:
    ------------
    Sets the min value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setMin(%s)" % (self.varName, num)

  def getStep(self):
    """
    Description:
    ------------
    Returns the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getStep()" % self.varName)

  def setStep(self, num):
    """
    Description:
    ------------
    Sets the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setStep(%s)" % (self.varName, num)

  def isDisabled(self):
    """
    Description:
    ------------
    Returns whether or not the slider is disabled

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.foundation_.isDisabled()" % self.varName, isPyData=False)

  def setDisabled(self, bool):
    """
    Description:
    ------------
    Sets the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    bool = JsUtils.setDisabled(bool, None)
    return "%s.foundation_.setDisabled(%s)" % (self.varName, bool)


class Drawers(JsMdcHtml):
  css_class = "mdc-drawer"

  def instantiate(self, html_id=None):
    return "new mdc.drawer.MDCDrawer.attachTo(document.querySelector('%s'))" % html_id


class CheckBox(JsMdcHtml):
  css_class = 'mdc-form-field'

  def instantiate(self, html_id=None):
    return "new mdc.checkbox.MDCCheckbox(document.querySelector('%s'));" % html_id

  @property
  def checked(self):
    """
    Description:
    ------------
    Setter/getter for the checkbox’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/checkboxes/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checked" % self.varName, isPyData=False)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Setter/getter for the checkbox’s disabled state

    Related Pages:

      https://material.io/develop/web/components/input-controls/checkboxes/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.disabled" % self.varName, isPyData=False)

  @property
  def indeterminate(self):
    """
    Description:
    ------------
    Setter/getter for the checkbox’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/checkboxes/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.indeterminate" % self.varName, isPyData=False)

  @property
  def value(self):
    """
    Description:
    ------------
    getter for the checkbox’s value

    Related Pages:

      https://material.io/develop/web/components/input-controls/checkboxes/
    """
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  def setValue(self, value):
    """
    Sets the checkbox’s value.

    :param value:
    :return:
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsBoolean.JsBoolean("%s.value = %s" % (self.varName, value), isPyData=False)

  def setStatus(self, status, bool=True):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/input-controls/checkboxes/

    Attributes:
    ----------
    :param label: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.%s = %s" % (self.varName, status, bool)

class SnackBar(JsMdcHtml):
  css_class = "mdc-snackbar"

  def instantiate(self, html_id=None):
    return "new mdc.snackbar.MDCSnackbar(document.querySelector('%s'));" % html_id


  @property
  def isOpen(self):
    """
    Gets whether the snackbar is currently open.

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.isOpen" % self.varName, isPyData=False)

  @property
  def timeoutMs(self):
    """
    Gets/sets the automatic dismiss timeout in milliseconds.
    Value must be between 4000 and 10000 (or -1 to disable the timeout completely) or an error will be thrown.
    Defaults to 5000 (5 seconds).

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return JsObjects.JsNumber.JsNumber("%s.timeoutMs" % self.varName, isPyData=False)


  @property
  def closeOnEscape(self):
    """
    Gets/sets whether the snackbar closes when it is focused and the user presses the ESC key. Defaults to true.

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.closeOnEscape" % self.varName, isPyData=False)

  @property
  def labelText(self):
    """
    Gets the textContent of the label element

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return JsObjects.JsObjects.get("%s.labelText" % self.varName)

  def setLabelText(self, value):
    """
    Sets the textContent of the label element

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return '%s.labelText = "%s"' % (self.varName, value)

  @property
  def actionButtonText(self):
    """
    Gets the textContent of the action button element.

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return JsObjects.JsObjects.get("%s.actionButtonText" % self.varName)

  def setActionButtonText(self, value):
    """
    Sets the textContent of the action button element.

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """
    return '%s.actionButtonText = "%s"' % (self.varName, value)

  def open(self):
    """
    Opens the snackbar.

    Related Pages:

      https://material.io/develop/web/components/snackbars/

    :return:
    """

    return "%s.open();" % self.varName

  def close(self, reason=''):
    """
    Closes the snackbar, optionally with the specified reason indicating why it was closed.

    Related Pages:

      https://material.io/develop/web/components/snackbars/
    """

    return "%s.close(%s);" % (self.varName, reason)