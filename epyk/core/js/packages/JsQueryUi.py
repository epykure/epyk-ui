"""
Wrapper to the Jquery UI package

Related Pages:

		https://api.jqueryui.com/
"""

import json

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js.statements import JsIf


class JQueryUI(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_set_var = False

  def __init__(self, component, varName=None, selector=None, setVar=True, report=None):
    super(JQueryUI, self).__init__(src=component, varName=varName, selector=selector, data=None, setVar=setVar, parent=report)
    self._src = component

  def labels(self):
    """
    Description:
    -----------
    Finds all label elements associated with the first selected element.
    """
    self.fnc("labels()")
    return self

  def cssClip(self, css=None):
    """
    Description:
    -----------
    Getter/setter for an object version of the CSS clip property.

    Related Pages:

      https://api.jqueryui.com/cssClip/

    Attributes:
    ----------
    :param css:
    """
    if css is not None:
      self.fnc("cssClip(%s)" % JsUtils.jsConvertData(css, None))
    else:
      self.fnc("cssClip()")
    return self

  def position(self, options=None):
    """
    Description:
    ------------
    The jQuery UI .position() method allows you to position an element relative to the window, document, another element, or the cursor/mouse, without worrying about offset parents.

    Related Pages:

      https://api.jqueryui.com/position/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The position definition.
    """
    if options is not None:
      self.fnc("position(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self.fnc("position()")
    return self

  def draggable(self, options=None):
    """
    Description:
    ------------
    Enable draggable functionality on any DOM element.
    Move the draggable object by clicking on it with the mouse and dragging it anywhere within the viewport.

    Related Pages:

      https://jqueryui.com/draggable/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The draggable definition.
    """
    if options is not None:
      return self.fnc("draggable(%s)" % JsUtils.jsConvertData(options, None))

    return self.fnc("draggable()")

  def droppable(self, options=None):
    """
    Description:
    ------------
    Enable any DOM element to be droppable, a target for draggable elements.

    Related Pages:

      https://jqueryui.com/droppable/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The droppable definition.
    """
    if options is not None:
      self._js.append("droppable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("droppable()")
    return self

  def sortable(self, options=None):
    """
    Description:
    ------------
    Enable a group of DOM elements to be sortable.
    Click on and drag an element to a new spot within the list, and the other items will adjust to fit.
    By default, sortable items share draggable properties.

    Related Pages:

      https://jqueryui.com/sortable/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The sortable definition.
    """
    if options is not None:
      self._js.append("sortable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("sortable()")
    return self

  def resizable(self, options=None):
    """
    Description:
    ------------
    Enable any DOM element to be resizable.
    With the cursor grab the right or bottom border and drag to the desired width or height.

    Related Pages:

      https://jqueryui.com/resizable/#constrain-area

    Attributes:
    ----------
    :param options: Dictionary. Optional. The resizable definition.
    """
    if options is not None:
      self._js.append("resizable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("resizable()")
    return self

  def selectable(self, options=None):
    """
    Description:
    ------------
    Enable a DOM element (or group of elements) to be selectable.
    Draw a box with your cursor to select items. Hold down the Ctrl key to make multiple non-adjacent selections.

    Related Pages:

      https://jqueryui.com/selectable/

    Attributes:
    ----------
    :param options: Dictionary. Optional. The selectable definition.
    """
    if options is not None:
      self._js.append("selectable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("selectable()")
    return self

  def addClass(self, cls_name, delay, callback):
    """
    Description:
    ------------
    Adds class(es) to elements while animating all style changes.

    Related Pages:

      https://jqueryui.com/addClass/

    Attributes:
    ----------
    :param cls_name:
    :param delay:
    :param callback:
    """
    self._js.append("addClass('%s', %s, %s)" % (cls_name, delay, ";".join(JsUtils.jsConvertFncs(callback))))
    return self

  def removeClass(self, cls_name, delay, callback):
    """
    Description:
    ------------
    Removes class(es) from elements while animating all style changes.

    Related Pages:

      https://jqueryui.com/removeClass/

    Attributes:
    ----------
    :param cls_name:
    :param delay:
    :param callback:
    """
    self._js.append("removeClass('%s', %s, %s)" % (cls_name, delay, ";".join(JsUtils.jsConvertFncs(callback))))
    return self

  def switchClass(self, cls_name, new_cls_name, delay):
    """
    Description:
    ------------
    Add and remove class(es) to elements while animating all style changes.

    Attributes:
    ----------
    :param cls_name:
    :param new_cls_name:
    :param delay:
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    new_cls_name = JsUtils.jsConvertData(new_cls_name, None)
    self._js.append("removeClass(%s, %s, %s)" % (cls_name, new_cls_name, delay))
    return self

  def toggleClass(self, cls_name, delay):
    """
    Description:
    ------------
    Toggle class(es) on elements while animating all style changes.

    Related Pages:

      https://jqueryui.com/toggleClass/

    Attributes:
    ----------
    :param cls_name:
    :param delay:
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    self._js.append("toggleClass(%s, %s)" % (cls_name, delay))
    return self

  def show(self, selected_effect=None, options=None, delay=None, callback=None):
    """
    Description:
    ------------
    Display elements using custom effects.

    Related Pages:

      https://jqueryui.com/show/

    Attributes:
    ----------
    :param selected_effect:
    :param options:
    :param delay:
    :param callback:
    """
    if selected_effect is None:
      self._js.append("show()")
    else:
      selected_effect = JsUtils.jsConvertData(selected_effect, None)
      options = JsUtils.jsConvertData(options, None)
      callback = ";".join(JsUtils.jsConvertFncs(callback))
      self._js.append("show(%s, %s, %s, %s)" % (selected_effect, options, delay, callback))
    return self

  def hide(self, selected_effect=None, options=None, delay=None, callback=None):
    """
    Description:
    ------------
    Display elements using custom effects.

    Related Pages:

      https://jqueryui.com/show/

    Attributes:
    ----------
    :param selected_effect:
    :param options:
    :param delay:
    :param callback:
    """
    if selected_effect is None:
      self._js.append("hide()")
    else:
      selected_effect = JsUtils.jsConvertData(selected_effect, None)
      options = JsUtils.jsConvertData(options, None)
      callback = ";".join(JsUtils.jsConvertFncs(callback))
      self._js.append("hide(%s, %s, %s, %s)" % (selected_effect, options, delay, callback))
    return self

  def toggle(self, selected_effect, options, delay):
    """
    Description:
    ------------

    Related Pages:

      https://jqueryui.com/toggle/

    Attributes:
    ----------
    :param selected_effect:
    :param options:
    :param delay:
    """
    selected_effect = JsUtils.jsConvertData(selected_effect, None)
    options = JsUtils.jsConvertData(options, None)
    self._js.append("toggle(%s, %s, %s)" % (selected_effect, options, delay))
    return self

  def animate(self, css=None, delay=None):
    """
    Description:
    ------------
    Animate the properties of elements between colors.

    Related Pages:

      https://jqueryui.com/animate/

    Attributes:
    ----------
    :param css:
    :param delay:
    """
    self._js.append("animate(%s, %s)" % (JsUtils.jsConvertData(css, None), delay))
    return self


class JQueryUiDatePicker(JQueryUI):

  def setDefaults(self):
    """
    Description:
    ------------

    """

  def formatDate(self):
    """
    Description:
    ------------

    """

  def option(self, name, value):
    """
    Description:
    ------------

    """
    return "$('#%s input').datepicker( 'option', '%s', %s)" % (self.src.htmlCode, name, json.dumps(value))

  def refresh(self):
    """
    Description:
    ------------

    """


class Slider(JQueryUI):

  def destroy(self):
    """
    Description:
    ------------
    Removes the slider functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/slider/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.slider("destroy")' % self._src.dom.jquery.varId)

  def disable(self):
    """
    Description:
    ------------
    Disables the slider

    Related Pages:

      https://api.jqueryui.com/slider/#method-disable
    """
    return JsObjects.JsObjects.get('%s.slider("disable")' % self._src.dom.jquery.varId)

  def enable(self):
    """
    Description:
    ------------
    Enables the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#method-enable
    """
    return JsObjects.JsObjects.get('%s.slider("enable")' % self._src.dom.jquery.varId)

  def instance(self):
    """
    Description:
    ------------
    Retrieves the slider's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/slider/#method-instance
    """
    return JsObjects.JsObjects.get('%s.slider("instance")' % self._src.dom.jquery.varId)

  def option(self, jsData=None):
    """
    Description:
    ------------
    Retrieves the slider's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/slider/#method-instance

    Attributes:
    ----------
    :param jsData:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.slider("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.slider("option", %s)' % (self._src.dom.jquery.varId, jsData))

  def value(self, jsData=None):
    """
    Description:
    ------------
    Get the value of the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#method-value

    Attributes:
    ----------
    :param jsData:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.slider("value")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.slider("value", %s)' % (self._src.dom.jquery.varId, jsData))

  def values(self, index=0, jsData=None):
    """
    Description:
    ------------
    Get the value for the specified handle.

    Related Pages:

      https://api.jqueryui.com/slider/#method-value

    Attributes:
    ----------
    :param index:
    :param jsData:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.slider("values", %s)' % (self._src.dom.jquery.varId, index))

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.slider("value", %s, %s)' % (self._src.dom.jquery.varId, index, jsData))

  def slide(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    if self._src.is_range:
      return JsObjects.JsObjects.get('%(id)s.slider("values", %(value)s); %(id)s.slider("option", "slide").call(%(id)s, null, {values: %(value)s})' % {
                                     "id": self._src.dom.jquery.varId, "value": value})

    return JsObjects.JsObjects.get('%(id)s.slider("value", %(value)s); %(id)s.slider("option", "slide").call(%(id)s, null, {value: %(value)s})' % {
      "id": self._src.dom.jquery.varId, "value": value})

  def inRange(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value: Number. The value to compare to the selected range.
    """
    if self._src.options.range:
      if self._src.options.range == "max":
        return JsObjects.JsObjects.get(
          '''%(compId)s.slider("value") < %(val)s && %(val)s < %(compId)s.slider("option", "max")''' % {
            "compId": self._src.dom.jquery.varId, "val": value})
      if self._src.options.range == "min":
        return JsObjects.JsObjects.get(
          '''%(compId)s.slider("option", "min") < %(val)s && %(val)s < %(compId)s.slider("value")''' % {
            "compId": self._src.dom.jquery.varId, "val": value})
      return JsObjects.JsObjects.get(
        '''%(compId)s.slider("values")[0] < %(val)s && %(val)s < %(compId)s.slider("values")[1]''' % {
          "compId": self._src.dom.jquery.varId, "val": value})

    return JsObjects.JsObjects.get(
      '''%(compId)s.slider("value") == %(val)s''' % {
        "compId": self._src.dom.jquery.varId, "val": value})


class ProgressBar(JQueryUI):

  def destroy(self):
    """
    Description:
    ------------
    Removes the progressbar functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.progressbar("destroy")' % self._src.dom.jquery.varId)

  def disable(self):
    """
    Description:
    ------------
    Disables the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-disable
    """
    return JsObjects.JsObjects.get('%s.progressbar("disable")' % self._src.dom.jquery.varId)

  def enable(self):
    """
    Description:
    ------------
    Enables the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-enable
    """
    return JsObjects.JsObjects.get('%s.progressbar("enable")' % self._src.dom.jquery.varId)

  def instance(self):
    """
    Description:
    ------------
    Retrieves the progressbar's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-instance
    """
    return JsObjects.JsObjects.get('%s.progressbar("instance")' % self._src.dom.jquery.varId)

  def option(self, jsData=None, jsValue=None):
    """
    Description:
    ------------
    Gets the value currently associated with the specified optionName.
    Gets an object containing key/value pairs representing the current progressbar options hash.
    Sets the value of the progressbar option associated with the specified optionName.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-instance

    Attributes:
    ----------
    :param jsData:
    :param jsValue:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.progressbar("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.progressbar("option", %s)' % (self._src.dom.jquery.varId, jsData))

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.progressbar("option", %s, %s)' % (self._src.dom.jquery.varId, jsData, jsValue))

  def value(self, jsValue=None):
    """
    Description:
    ------------
    Retrieves the progressbar's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-instance

    Attributes:
    ----------
    :param jsValue:
    """
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.progressbar("value")' % self._src.dom.jquery.varId)

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.progressbar("value", %s)' % (self._src.dom.jquery.varId, jsValue))

  def add(self, jsValue=None):
    """
    Description:
    ------------
    Add value to the progress bar.

    Attributes:
    ----------
    :param jsValue: Float | JsObject. The value to be added to the current state.
    """
    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%(varId)s.progressbar("value", %(varId)s.progressbar("value") + %(jsValue)s)' % {
      "varId": self._src.dom.jquery.varId, "jsValue": jsValue})

  def tooltip(self, jsValue=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsValue:
    :param options:
    """
    return JsObjects.JsVoid(''' let options = %(options)s;
%(varId)s.find('div').attr("title", ""+ (%(varId)s.progressbar("value") / options.max * 100).toFixed(2) +"%% ("+ %(varId)s.progressbar("value") +" / "+ options.max +")")
 ''' % {"varId": self._src.dom.jquery.varId, 'options': self._src.options.config_js(options)})


class Menu(JQueryUI):

  def blur(self):
    """
    Description:
    ------------
    Removes focus from a menu, resets any active element styles and triggers the menu's blur event.

    Related Pages:

      https://api.jqueryui.com/menu/#method-blur
    """
    return JsObjects.JsObjects.get('%s.menu("blur")' % self._src.dom.jquery.varId)

  def collapse(self):
    """
    Description:
    ------------
    Closes the currently active sub-menu.

    Related Pages:

      https://api.jqueryui.com/menu/#method-collapse
    """
    return JsObjects.JsObjects.get('%s.menu("collapse")' % self._src.dom.jquery.varId)

  def collapseAll(self):
    """
    Description:
    ------------
    Closes all open sub-menus.

    Related Pages:

      https://api.jqueryui.com/menu/#method-collapseAll
    """
    return JsObjects.JsObjects.get('%s.menu("collapseAll", null, true)' % self._src.dom.jquery.varId)

  def destroy(self):
    """
    Description:
    ------------
    Removes the menu functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/menu/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.menu("destroy")' % self._src.dom.jquery.varId)

  def disable(self):
    """
    Description:
    ------------
    Disables the menu.

    Related Pages:

      https://api.jqueryui.com/menu/#method-disable
    """
    return JsObjects.JsObjects.get('%s.menu("disable")' % self._src.dom.jquery.varId)

  def enable(self):
    """
    Description:
    ------------
    Enables the menu.

    Related Pages:

      https://api.jqueryui.com/menu/#method-disable
    """
    return JsObjects.JsObjects.get('%s.menu("enable")' % self._src.dom.jquery.varId)

  def expand(self):
    """
    Description:
    ------------
    Opens the sub-menu below the currently active item, if one exists.

    Related Pages:

      https://api.jqueryui.com/menu/#method-expand
    """
    return JsObjects.JsObjects.get('%s.menu("expand")' % self._src.dom.jquery.varId)

  def instance(self):
    """
    Description:
    ------------
    Retrieves the menu's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/menu/#method-instance
    """
    return JsObjects.JsObjects.get('%s.menu("instance")' % self._src.dom.jquery.varId)

  def isFirstItem(self):
    """
    Description:
    ------------
    Returns a boolean value stating whether or not the currently active item is the first item in the menu.

    Related Pages:

      https://api.jqueryui.com/menu/#method-isFirstItem
    """
    return JsObjects.JsBoolean.JsBoolean('%s.menu("isFirstItem")' % self._src.dom.jquery.varId)

  def isLastItem(self):
    """
    Description:
    ------------
    Returns a boolean value stating whether or not the currently active item is the last item in the menu

    Related Pages:

      https://api.jqueryui.com/menu/#method-isLastItem
    """
    return JsObjects.JsBoolean.JsBoolean('%s.menu("isLastItem")' % self._src.dom.jquery.varId)

  def next(self):
    """
    Description:
    ------------
    Moves active state to next menu item.

    Related Pages:

      https://api.jqueryui.com/menu/#method-next
    """
    return JsObjects.JsObjects.get('%s.menu("next")' % self._src.dom.jquery.varId)

  def nextPage(self):
    """
    Description:
    ------------
    Moves active state to first menu item below the bottom of a scrollable menu or the last item if not scrollable.

    Related Pages:

      https://api.jqueryui.com/menu/#method-nextPage
    """
    return JsObjects.JsObjects.get('%s.menu("nextPage")' % self._src.dom.jquery.varId)

  def option(self, jsData=None, jsValue=None):
    """
    Description:
    ------------
    Gets an object containing key/value pairs representing the current menu options hash.
    Sets the value of the menu option associated with the specified optionName.
    Sets one or more options for the menu.

    Related Pages:

      https://api.jqueryui.com/progressbar/#method-option

    Attributes:
    ----------
    :param jsData:
    :param jsValue:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.menu("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.menu("option", %s)' % (self._src.dom.jquery.varId, jsData))

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.menu("option", %s, %s)' % (self._src.dom.jquery.varId, jsData, jsValue))

  def previous(self):
    """
    Description:
    ------------
    Moves active state to previous menu item.

    Related Pages:

      https://api.jqueryui.com/menu/#method-previous
    """
    return JsObjects.JsObjects.get('%s.menu("previous")' % self._src.dom.jquery.varId)

  def previousPage(self):
    """
    Description:
    ------------
    Moves active state to first menu item above the top of a scrollable menu or the first item if not scrollable.

    Related Pages:

      https://api.jqueryui.com/menu/#method-previousPage
    """
    return JsObjects.JsObjects.get('%s.menu("previousPage")' % self._src.dom.jquery.varId)

  def refresh(self):
    """
    Description:
    ------------
    nitializes sub-menus and menu items that have not already been initialized.
    New menu items, including sub-menus can be added to the menu or all of the contents of the menu can be replaced and then initialized with the refresh() method.

    Related Pages:

      https://api.jqueryui.com/menu/#method-refresh
    """
    return JsObjects.JsObjects.get('%s.menu("refresh")' % self._src.dom.jquery.varId)

  def select(self):
    """
    Description:
    ------------
    Selects the currently active menu item, collapses all sub-menus and triggers the menu's select event.

    Related Pages:

      https://api.jqueryui.com/menu/#method-select
    """
    return JsObjects.JsObjects.get('%s.menu("select")' % self._src.dom.jquery.varId)


class Dialog(JQueryUI):

  def close(self):
    """
    Description:
    ------------
    Closes the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-close
    """
    return JsObjects.JsObjects.get('%s.dialog("close")' % self._src.dom.jquery.varId)

  def destroy(self):
    """
    Description:
    ------------
    Removes the dialog functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.dialog("destroy")' % self._src.dom.jquery.varId)

  def instance(self):
    """
    Description:
    ------------
    Retrieves the dialog's instance object. If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-instance
    """
    return JsObjects.JsObjects.get('%s.dialog("instance")' % self._src.dom.jquery.varId)

  def isOpen(self):
    """
    Description:
    ------------
    Whether the dialog is currently open.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-isOpen
    """
    return JsObjects.JsObjects.get('%s.dialog("isOpen")' % self._src.dom.jquery.varId)

  def moveToTop(self):
    """
    Description:
    ------------
    Moves the dialog to the top of the dialog stack.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-moveToTop
    """
    return JsObjects.JsObjects.get('%s.dialog("moveToTop")' % self._src.dom.jquery.varId)

  def open(self):
    """
    Description:
    ------------
    Opens the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-open
    """
    return JsObjects.JsObjects.get('%s.dialog("open")' % self._src.dom.jquery.varId)

  def add(self):
    """
    Description:
    ------------
    Opens the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-open
    """
    return JsObjects.JsVoid('''
var div = $(document.createElement("div")); div.innerHTML = "wegegre";
div.dialog({modal: false, title: "rrrr", autoOpen: false}); div.dialog("open")
%s.append(div)''' % self._src.dom.jquery.varId)

  def dialog(self, event):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param event:
    """
    event = JsUtils.jsConvertData(event, None)
    return JsObjects.JsVoid("%s.dialog(%s)" % (self._src.dom.jquery.varId, event))

  def option(self, jsData=None, jsValue=None):
    """
    Description:
    ------------
    Gets the value currently associated with the specified optionName.
    Gets an object containing key/value pairs representing the current dialog options hash.
    Sets the value of the dialog option associated with the specified optionName.
    Sets one or more options for the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#method-option

    Attributes:
    ----------
    :param jsData:
    :param jsValue:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.dialog("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.dialog("option", %s)' % (self._src.dom.jquery.varId, jsData))

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.dialog("option", %s, %s)' % (self._src.dom.jquery.varId, jsData, jsValue))


class AutocompleteFormats:

  def __init__(self, component):
    self.component = component

  def groups(self):
    """
    Description:
    ------------

    """
    return JsUtils.jsWrap('''
%s.autocomplete("instance")._renderItem = function( ul, item ) {
  return $( "<li>" )
    .append( "<div>" + item.label + "<br>" + item.category + "</div>" )
    .appendTo( ul );
}''' % self.component.dom.jquery.varId)


class Autocomplete(JQueryUI):

  def empty(self):
    """
    Description:
    ------------
    Empty the content of the HTML component using the innerHTML JavaScript property.
    """
    return '%s.val("")' % self._src.dom.jquery.varId

  def close(self):
    """
    Description:
    ------------
    Closes the dialog.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-close
    """
    return JsObjects.JsObjects.get('%s.autocomplete("close")' % self._src.dom.jquery.varId)

  def destroy(self):
    """
    Description:
    ------------
    Removes the autocomplete functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.autocomplete("destroy")' % self._src.dom.jquery.varId)

  def disable(self):
    """
    Description:
    ------------
    Disables the autocomplete.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-disable
    """
    return JsObjects.JsObjects.get('%s.autocomplete("disable")' % self._src.dom.jquery.varId)

  def enable(self):
    """
    Description:
    ------------
    Enables the autocomplete.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-enable
    """
    return JsObjects.JsObjects.get('%s.autocomplete("enable")' % self._src.dom.jquery.varId)

  def instance(self):
    """
    Description:
    ------------
    Retrieves the autocomplete's instance object.
    If the element does not have an associated instance, undefined is returned.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-enable
    """
    return JsObjects.JsObjects.get('%s.autocomplete("instance")' % self._src.dom.jquery.varId)

  def option(self, jsData=None, jsValue=None):
    """
    Description:
    ------------
    Gets the value currently associated with the specified optionName.
    Gets an object containing key/value pairs representing the current dialog options hash.
    Sets the value of the dialog option associated with the specified optionName.
    Sets one or more options for the dialog.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-option

    Attributes:
    ----------
    :param jsData:
    :param jsValue:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.autocomplete("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.autocomplete("option", %s)' % (self._src.dom.jquery.varId, jsData))

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.autocomplete("option", %s, %s)' % (self._src.dom.jquery.varId, jsData, jsValue))

  def search(self, jsData=None):
    """
    Description:
    ------------
    Triggers a search event and invokes the data source if the event is not canceled.
    Can be used by a selectbox-like button to open the suggestions when clicked.
    When invoked with no parameters, the current input's value is used. Can be called with an empty string
    and minLength: 0 to display all items.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#method-close

    Attributes:
    ----------
    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.autocomplete("search", %s)' % (self._src.dom.jquery.varId, jsData))

  def source(self, jsData):
    """
    Description:
    ------------

    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.autocomplete("option", "source", %s)' % (self._src.dom.jquery.varId, jsData))

  def ui_item(self, field):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param field:
    """
    field = JsUtils.jsConvertData(field, None)
    return JsObjects.JsObjects.get("ui.item[%s]" % field)

  @property
  def renderItems(self):
    """
    Description:
    ------------

    """
    return AutocompleteFormats(self._src)

  def renderItem(self, callback):
    """
    Description:
    ------------

    https://jqueryui.com/autocomplete/#custom-data

    Attributes:
    ----------
    :param callback:

    """
    return JsUtils.jsWrap('%s.autocomplete("instance")._renderItem = %s' % (self._src.dom.jquery.varId, callback))

  def if_(self, jsRule, jsFncs):
    """
    Description:
    ------------
    Generic if statement for an input component.

    Attributes:
    ----------
    :param jsRule: String.
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsIf.JsIf(jsRule, jsFncs)


class Datepicker(JQueryUI):
  # TODO add dialog

  def destroy(self):
    """
    Description:
    ------------
    Removes the datepicker functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-destroy
    """
    return JsObjects.JsObjects.get('%s.datepicker("destroy")' % self._src.dom.jquery.varId)

  def getDate(self):
    """
    Description:
    ------------
    Returns the current date for the datepicker or null if no date has been selected.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-getDate
    """
    return JsObjects.JsObjects.get('%s.datepicker("getDate")' % self._src.dom.jquery.varId)

  def hide(self):
    """
    Description:
    ------------
    Close a previously opened date picker.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-hide
    """
    return JsObjects.JsObjects.get('%s.datepicker("hide")' % self._src.dom.jquery.varId)

  def isDisabled(self):
    """
    Description:
    ------------
    Determine whether a date picker has been disabled.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-isDisabled
    """
    return JsObjects.JsObjects.get('%s.datepicker("isDisabled")' % self._src.dom.jquery.varId)

  def disable(self):
    """
    Description:
    ------------
    Disable the datepicker component

    """
    return JsObjects.JsObjects.get('%s.datepicker("option", "disabled", true )' % self._src.dom.jquery.varId)

  def enable(self):
    """
    Description:
    ------------
    Enable the datepciker component
    """
    return JsObjects.JsObjects.get('%s.datepicker("option", "disabled", false )' % self._src.dom.jquery.varId)

  def option(self, jsData=None, jsValue=None):
    """
    Description:
    ------------
    Gets the value currently associated with the specified optionName.
    Gets an object containing key/value pairs representing the current dialog options hash.
    Sets the value of the dialog option associated with the specified optionName.
    Sets one or more options for the dialog.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-option

    Attributes:
    ----------
    :param jsData:
    :param jsValue:
    """
    if jsData is None:
      return JsObjects.JsObjects.get('%s.datepicker("option")' % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    if jsValue is None:
      return JsObjects.JsObjects.get('%s.datepicker("option", %s)' % (self._src.dom.jquery.varId, jsData))

    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.datepicker("option", %s, %s)' % (self._src.dom.jquery.varId, jsData, jsValue))

  def format_dates(self, class_name, dts=None, css=None, tooltip=""):
    """
    Description:
    ------------
    Change the CSS style for some selected dates in the datepicker.
    This function can be also used on the Javascript side from the js property.

    Attributes:
    ----------
    :param class_name: String. The name of the CSS added to the page with the CSS attributes.
    :param dts: List. A list of dates format YYYY-MM-DD.
    :param css: Dictionary. The CSS Attributes for the CSS class.
    :param tooltip: String. The tooltip when the mouse is hover
    """
    dts = dts or []
    if css is not None:
      self._src._report.body.style.custom_class(css, classname="%s a" % class_name)
    return JsObjects.JsObjects.get('''%(varId)s.datepicker("option", "beforeShowDay", function (date) {
        var utc = date.getTime() - date.getTimezoneOffset()*60000; var newDate = new Date(utc); const dts = %(dts)s;
        if(dts.includes(newDate.toISOString().split('T')[0])){return [true, '%(class_name)s', '%(tooltip)s']} else {return [true, '', '']}
      })''' % {"dts": JsUtils.jsConvertData(dts, None), 'tooltip': tooltip, "class_name": class_name, "varId": self._src.dom.jquery.varId})

  def refresh(self):
    """
    Description:
    ------------
    Redraw the date picker, after having made some external modifications.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-refresh
    """
    return JsObjects.JsObjects.get('%s.datepicker("refresh")' % self._src.dom.jquery.varId)

  def setDate(self, jsData=None,):
    """
    Description:
    ------------
    Sets the date for the datepicker. The new date may be a Date object or a string in the current date format (e.g.,
    "01/26/2009"), a number of days from today (e.g., +7) or a string of values and periods
    ("y" for years, "m" for months, "w" for weeks, "d" for days, e.g., "+1m +7d"), or null to clear the selected date.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-setDate

    Attributes:
    ----------
    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.datepicker("setDate", %s)' % (self._src.dom.jquery.varId, jsData))

  def show(self):
    """
    Description:
    ------------
    Open the date picker. If the datepicker is attached to an input, the input must be visible for the datepicker to be shown.

    Related Pages:

      https://api.jqueryui.com/datepicker/#method-show
    """
    return JsObjects.JsObjects.get('%s.datepicker("show")' % self._src.dom.jquery.varId)
