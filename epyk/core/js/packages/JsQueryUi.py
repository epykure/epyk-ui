"""
Wrapper to the Jquery UI package

https://api.jqueryui.com/
"""

import json

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class JQueryUI(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_selector = 'jQuery("body")'
  lib_set_var = False

  def labels(self):
    """
    Finds all label elements associated with the first selected element.

    :return:
    """
    self._js.append("labels()")
    return self

  def cssClip(self, css=None):
    """
    Getter/setter for an object version of the CSS clip property.

    Documentation
    https://api.jqueryui.com/cssClip/

    :param css:

    :return:
    """
    if css is not None:
      self._js.append("cssClip(%s)" % JsUtils.jsConvertData(css, None))
    else:
      self._js.append("cssClip()")
    return self

  def position(self, options=None):
    """
    The jQuery UI .position() method allows you to position an element relative to the window, document, another element, or the cursor/mouse, without worrying about offset parents.

    Documentation
    https://api.jqueryui.com/position/

    :param options:

    :return:
    """
    if options is not None:
      self._js.append("position(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("position()")
    return self

  def draggable(self, options=None):
    """
    Enable draggable functionality on any DOM element.
    Move the draggable object by clicking on it with the mouse and dragging it anywhere within the viewport.

    Example

    Documentation
    https://jqueryui.com/draggable/

    :param options:
    """
    if options is not None:
      return self.fnc("draggable(%s)" % JsUtils.jsConvertData(options, None))

    return self.fnc("draggable()")

  def droppable(self, options=None):
    """
    Enable any DOM element to be droppable, a target for draggable elements.

    Example

    Documentation
    https://jqueryui.com/droppable/

    :param options:

    :return:
    """
    if options is not None:
      self._js.append("droppable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("droppable()")
    return self

  def sortable(self, options=None):
    """
    Enable a group of DOM elements to be sortable.
    Click on and drag an element to a new spot within the list, and the other items will adjust to fit.
    By default, sortable items share draggable properties.

    Documentation
    https://jqueryui.com/sortable/

    :param options:

    :return:
    """
    if options is not None:
      self._js.append("sortable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("sortable()")
    return self

  def resizable(self, options=None):
    """
    Enable any DOM element to be resizable.
    With the cursor grab the right or bottom border and drag to the desired width or height.

    Example

    Documentation
    https://jqueryui.com/resizable/#constrain-area

    :param options:

    :return:
    """
    if options is not None:
      self._js.append("resizable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("resizable()")
    return self

  def selectable(self, options=None):
    """
    Enable a DOM element (or group of elements) to be selectable.
    Draw a box with your cursor to select items. Hold down the Ctrl key to make multiple non-adjacent selections.

    Documentation
    https://jqueryui.com/selectable/

    :param options:

    :return:
    """
    if options is not None:
      self._js.append("selectable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("selectable()")
    return self

  def addClass(self, cls_name, delay, callback):
    """
    Adds class(es) to elements while animating all style changes.

    Documentation
    https://jqueryui.com/addClass/

    :param cls_name:
    :param delay:
    :param callback:

    :return:
    """
    self._js.append("addClass('%s', %s, %s)" % (cls_name, delay, ";".join(JsUtils.jsConvertFncs(callback))))
    return self

  def removeClass(self, cls_name, delay, callback):
    """
    Removes class(es) from elements while animating all style changes.

    Documentation
    https://jqueryui.com/removeClass/

    :param cls_name:
    :param delay:
    :param callback:

    :return:
    """
    self._js.append("removeClass('%s', %s, %s)" % (cls_name, delay, ";".join(JsUtils.jsConvertFncs(callback))))
    return self

  def switchClass(self, cls_name, new_cls_name, delay):
    """
    Add and remove class(es) to elements while animating all style changes.

    :param cls_name:
    :param new_cls_name:
    :param delay:

    :return:
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    new_cls_name = JsUtils.jsConvertData(new_cls_name, None)
    self._js.append("removeClass(%s, %s, %s)" % (cls_name, new_cls_name, delay))
    return self

  def toggleClass(self, cls_name, delay):
    """
    Toggle class(es) on elements while animating all style changes.

    Documentation
    https://jqueryui.com/toggleClass/

    :param cls_name:
    :param delay:

    :return:
    """
    cls_name = JsUtils.jsConvertData(cls_name, None)
    self._js.append("toggleClass(%s, %s)" % (cls_name, delay))
    return self

  def show(self, selected_effect=None, options=None, delay=None, callback=None):
    """
    Display elements using custom effects.

    Documentation
    https://jqueryui.com/show/

    :param selected_effect:
    :param options:
    :param delay:
    :param callback:

    :return:
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
    Display elements using custom effects.

    Documentation
    https://jqueryui.com/show/

    :param selected_effect:
    :param options:
    :param delay:
    :param callback:

    :return:
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

    Documentation
    https://jqueryui.com/toggle/

    :param selected_effect:
    :param options:
    :param delay:

    :return:
    """
    selected_effect = JsUtils.jsConvertData(selected_effect, None)
    options = JsUtils.jsConvertData(options, None)
    self._js.append("toggle(%s, %s, %s)" % (selected_effect, options, delay))
    return self

  def animate(self, css=None, delay=None):
    """
    Animate the properties of elements between colors.

    Documentation
    https://jqueryui.com/animate/

    :param css:
    :param delay:

    :return:
    """
    self._js.append("animate(%s, %s)" % (JsUtils.jsConvertData(css, None), delay))
    return self


class JQueryUiDatePicker(JQueryUI):

  def setDefaults(self):
    """

    :return:
    """

  def formatDate(self):
    """

    :return:
    """

  def option(self, name, value):
    """

    :return:
    """
    return "$('#%s input').datepicker( 'option', '%s', %s)" % (self.src.htmlId, name, json.dumps(value))

  def refresh(self):
    """

    :return:
    """


class JQueryUiSlider(JQueryUI):
  """

  Documentation
  https://api.jqueryui.com/slider/

  """

  def destroy(self):
    """

    :return:
    """

  def disable(self):
    """

    :return:
    """

  def option(self, name, value):
    """

    :return:
    """

  def enable(self):
    pass

  def value(self):
    pass

  def values(self):
    pass

  def widget(self):
    pass

  def instance(self):
    pass


class JQueryUiProgressBar(JQueryUI):
  """

  """
