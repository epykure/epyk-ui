
from typing import Union, Optional
from epyk.core.py import types
from epyk.core.html.options import Options
from epyk.core.js import JsUtils


class OptionsSlider(Options):
  component_properties = ("css", 'show_min_max', "force_show_current")

  @property
  def animate(self):
    """
    Whether to slide the handle smoothly when the user clicks on the slider track. Also accepts any valid animation.

    Related Pages:

      https://api.jqueryui.com/slider/#option-animate
    """
    return self._config_get(False)

  @animate.setter
  def animate(self, flag: bool):
    self._config(flag)

  @property
  def css(self):
    """
    Whether to slide the handle smoothly when the user clicks on the slider track. Also accepts any valid animation.

    Related Pages:

      https://api.jqueryui.com/slider/#option-animate
    """
    return self._config_get({"background": self.page.theme.success[0]})

  @css.setter
  def css(self, values: dict):
    self._config(values)

  @property
  def handler_css(self):
    """
    Whether to slide the handle smoothly when the user clicks on the slider track. Also accepts any valid animation.

    Related Pages:

      https://api.jqueryui.com/slider/#option-animate
    """
    return self._config_get()

  @handler_css.setter
  def handler_css(self, value):
    self._config(value)

  def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """

    :param js_funcs:
    :param profile:
    """
    self._config("function (event, ui){%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile), js_type=True)

  @property
  def classes(self):
    """
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the classes option.

    Related Pages:

      https://api.jqueryui.com/slider/#option-classes
    """
    return self._config_get('classes')

  @classes.setter
  def classes(self, value: str):
    self._config(value)

  @property
  def disabled(self):
    """
    Disables the slider if set to true.

    Related Pages:

      https://api.jqueryui.com/slider/#option-disabled
    """
    return self._config_get(False)

  @disabled.setter
  def disabled(self, flag: bool):
    self._config(flag)

  @property
  def max(self):
    """
    The maximum value of the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#option-max
    """
    return self._config_get(100)

  @max.setter
  def max(self, value: float):
    self._config(value)

  @property
  def min(self):
    """
    The minimum value of the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#option-min

    :prop value: The min value
    """
    return self._config_get(0)

  @min.setter
  def min(self, value: float):
    self._config(value)

  @property
  def show_min_max(self):
    """

    """
    return self._config_get(True)

  @show_min_max.setter
  def show_min_max(self, flag: bool):
    if not flag:
      self.component.style.css.padding = 0
    self._config(flag)

  @property
  def force_show_current(self):
    """

    """
    return self._config_get(False)

  @force_show_current.setter
  def force_show_current(self, flag: bool):
    if not flag:
      self.component.style.css.padding = 0
    self._config(flag)

  @property
  def orientation(self):
    """
    Determines whether the slider handles move horizontally (min on left, max on right) or vertically (min on bottom,
    max on top).
    Possible values: "horizontal", "vertical".

    Related Pages:

      https://api.jqueryui.com/slider/#option-orientation
    """
    return self._config_get("horizontal")

  @orientation.setter
  def orientation(self, value: str):
    self._config(value)

  @property
  def range(self):
    """
    Whether the slider represents a range.

    Related Pages:

      https://api.jqueryui.com/slider/#option-range
    """
    return self._config_get(False)

  @range.setter
  def range(self, flag: bool):
    self._config(flag)

  def slide(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
            readout: bool = True, readout_level: str = "handle", readout_format: Optional[bool] = True,
            options: types.OPTION_TYPE = None, css: dict = None, precision: int = 0, delay_ms: int = 0):
    """   Triggered on every mouse move during slide.
    The value provided in the event as ui.value represents the value that the handle will have as a result of
    the current movement.

    Related Pages:

      https://api.jqueryui.com/slider/
      https://jqueryui.com/position/

    Usage::

      slider = page.ui.slider(5)
      slider.options.step = 0.01
      slider.options.slide(precision=2)

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param readout: Optional. Show the value in a popup
    :param readout_level: Optional
    :param readout_format: Optional
    :param options: Optional. The slide effect options
    :param delay_ms: Optional. The delay before the change in milliseconds
    :param css: Optional. The label CSS attributes
    :param precision: Optional. Number of digits in the slider increments
    """
    dfl_css = {"color": self.page.theme.black}
    if css is not None:
      dfl_css.update(css)
    if readout:
      if readout_level == "slider":
        if readout_format is True:
          readout_format = {"type": "number", "precision": precision, "thousand": ",", "decimal": "."}
        elif isinstance(readout_format, int):
          readout_format = {"type": "number", "precision": readout_format, "thousand": ",", "decimal": "."}
        if readout_format and readout_format["type"] in ("number", "money"):
          self.component.page.jsImports.add("accounting")
          fmt_html = "accounting.formatNumber(ui.value, %s)" % readout_format
        else:
          if self.component.is_range:
            fmt_html = "ui.values[0] +' - '+ ui.values[1]"
          else:
            fmt_html = "ui.value"
        if self.component.is_range:
          options = options or {"position": "absolute", "right": "-45px", "top": "-8px", "font-size": "10px"}
        else:
          options = options or {"position": "absolute", "right": "-35px", "top": "-8px", "font-size": "10px"}
        options.update(dfl_css)
        value = '''
if ($("#%(htmlCode)s").find('output').length){var label = $("#%(htmlCode)s").find('output')[0]}
else {var label = $('<output></output>'); label.css(%(options)s); $("#%(htmlCode)s").append(label)}
$(label).html(%(fmt_html)s)''' % {"htmlCode": self.component.html_code, "options": options, "fmt_html": fmt_html}
      else:
        if readout_format is True:
          readout_format = {"type": "number", "precision": precision, "thousand": ",", "decimal": "."}
        elif isinstance(readout_format, int):
          readout_format = {"type": "number", "precision": readout_format, "thousand": ",", "decimal": "."}
        options = options or {"my": "center top", "at": "center bottom", "offset": "0, 10"}
        if readout_format and readout_format["type"] in ("number", "money"):
          self.component.page.jsImports.add("accounting")
          fmt_html = "accounting.formatNumber(ui.value, %s)" % readout_format
        else:
          fmt_html = "ui.values[0] +' - '+ ui.values[1]" if self.component.is_range else "ui.value"
        self.force_show_current = True
        output_component = self.component.output
        value = '''%(builder)s(document.getElementsByName('%(htmlCode)s')[0], %(fmt_html)s, %(builderOptions)s)''' % {
          "builder": self.js_tree['out_builder_fnc'], "builderOptions": output_component.options.config_js(),
          "fmt_html": fmt_html, "htmlCode": self.component.output.html_code}
      if js_funcs is None:
        js_funcs = []
      if delay_ms:
        js_funcs.append("setTimeout(function(){%(value)s}, %(delay_ms)s)" % {"value": value, "delay_ms": delay_ms})
      else:
        js_funcs.append(value)
    self._config(
      "function (event, ui){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  def create(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
    """   Triggered when the slider is created.

    Related Pages:

      https://api.jqueryui.com/slider/

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
    self._config("function (){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  @property
  def step(self):
    """
    Determines the size or amount of each interval or step the slider takes between the min and max.
    The full specified value range of the slider (max - min) should be evenly divisible by the step.

    Usage::

      slider = page.ui.slider(5)
      slider.options.step = 0.01

    Related Pages:

      https://api.jqueryui.com/slider/#option-step
    """
    return self._config_get(1)

  @step.setter
  def step(self, value: int):
    self._config(value)

  @property
  def value(self):
    """
    Determines the value of the slider, if there's only one handle.
    If there is more than one handle, determines the value of the first handle.

    Related Pages:

      https://api.jqueryui.com/slider/#option-value
    """
    return self._config_get(0)

  @value.setter
  def value(self, value: int):
    self._config(value)

  @property
  def values(self):
    """
    This option can be used to specify multiple handles.
    If the range option is set to true, the length of values should be 2.

    Related Pages:

      https://api.jqueryui.com/slider/#option-values
    """
    return self._config_get(0)

  @values.setter
  def values(self, value):
    self._config(value)


class OptionsProgBar(Options):
  component_properties = ("show_percentage", "digits")

  @property
  def classes(self):
    """
    Initialize the progressbar with the classes option specified, changing the theming for the ui-progressbar

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-classes
    """
    return self._config_get(None)

  @classes.setter
  def classes(self, value: str):
    self._config(value)

  @property
  def digits(self):
    """
    Get the number of digit for the value.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-classes
    """
    return self._config_get(2)

  @digits.setter
  def digits(self, value: int):
    self._config(value)

  @property
  def background(self):
    """

    """
    return self._config_group_get('css', None)

  @background.setter
  def background(self, value: str):
    self._config_group('css', value)

  @property
  def border_color(self):
    """

    """
    return self._config_group_get('css', None, name="borderColor")

  @border_color.setter
  def border_color(self, value: str):
    self._config_group('css', value, name="borderColor")

  def css(self, attrs: dict):
    """

    :param attrs: The CSS attributes
    """
    css_attrs = self._config_get({}, 'css')
    css_attrs.update(attrs)
    self._config(css_attrs)

  @property
  def disabled(self):
    """
    Disables the progressbar if set to true.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-disabled
    """
    return self._config_get(None)

  @disabled.setter
  def disabled(self, flag: bool):
    self._config(flag)

  @property
  def max(self):
    """
    The maximum value of the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-max
    """
    return self._config_get(100)

  @max.setter
  def max(self, num: int):
    self._config(num)

  @property
  def min(self):
    """
    The min value of the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-max
    """
    return self._config_get(0)

  @min.setter
  def min(self, num: int):
    self._config(num)

  @property
  def value(self):
    """
    The value of the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-value
    """
    return self._config_get(None)

  @value.setter
  def value(self, val):
    self._config(val)

  @property
  def rounded(self):
    """
    Change the border radius style of the component.
    """
    return self.component.style.css.border_radius

  @rounded.setter
  def rounded(self, val: int):
    self.component.style.css.border_radius = val
    self.css({"border-radius": self.component.style.css.border_radius})

  @property
  def show_percentage(self):
    return self._config_get(False)

  @show_percentage.setter
  def show_percentage(self, flag: bool):
    self._config(flag)


class OptionsMenu(Options):

  @property
  def classes(self):
    """
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the

    Related Pages:

      https://api.jqueryui.com/menu/#option-classes
    """
    return self._config_get({})

  @classes.setter
  def classes(self, value: dict):
    self._config(value)

  @property
  def disabled(self):
    """
    Disables the menu if set to true

    Related Pages:

      https://api.jqueryui.com/menu/#option-disabled
    """
    return self._config_get(False)

  @disabled.setter
  def disabled(self, flag: bool):
    self._config(flag)

  @property
  def icons(self):
    """
    Icons to use for submenus, matching an icon provided by the jQuery UI CSS Framework.

    Related Pages:

      https://api.jqueryui.com/menu/#option-icons
    """
    return self._config_get(None)

  @icons.setter
  def icons(self, flag: bool):
    self._config(flag)

  @property
  def position(self):
    """
    Identifies the position of submenus in relation to the associated parent menu item.
    The of option defaults to the parent menu item, but you can specify another element to position against.
    You can refer to the jQuery UI Position utility for more details about the various options.

    Related Pages:

      https://api.jqueryui.com/menu/#option-position
    """
    return self._config_get(None)

  @position.setter
  def position(self, flag: bool):
    self._config(flag)


class OptionDialog(Options):
  component_properties = ("empty", )

  @property
  def appendTo(self):
    """
    Which element the dialog (and overlay, if modal) should be appended to

    Related Pages:

      https://api.jqueryui.com/dialog/#option-appendTo
    """
    return self._config_get('body')

  @appendTo.setter
  def appendTo(self, value: Union[bool, str]):
    self._config(value)

  @property
  def autoOpen(self):
    """
    If set to true, the dialog will automatically open upon initialization.
    If false, the dialog will stay hidden until the open() method is called.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-autoOpen
    """
    return self._config_get(True)

  @autoOpen.setter
  def autoOpen(self, flag: bool):
    self._config(flag)

  @property
  def classes(self):
    """
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the

    Related Pages:

      https://api.jqueryui.com/dialog/#option-classes
    """
    return self._config_get({})

  @classes.setter
  def classes(self, value: dict):
    self._config(value)

  @property
  def closeOnEscape(self):
    """
    Specifies whether the dialog should close when it has focus and the user presses the escape (ESC) key.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-closeOnEscape
    """
    return self._config_get(True)

  @closeOnEscape.setter
  def closeOnEscape(self, flag: bool):
    self._config(flag)

  @property
  def closeText(self):
    """
    Specifies the text for the close button. Note that the close text is visibly hidden when using a standard theme.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-closeText
    """
    return self._config_get(True)

  @closeText.setter
  def closeText(self, flag: bool):
    self._config(flag)

  @property
  def draggable(self):
    """
    If set to true, the dialog will be draggable by the title bar. Requires the jQuery UI Draggable widget to
    be included.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-draggable
    """
    return self._config_get(True)

  @draggable.setter
  def draggable(self, flag: bool):
    self._config(flag)

  @property
  def height(self):
    """
    The height of the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-height
    """
    return self._config_get('auto')

  @height.setter
  def height(self, value: Union[str, int]):
    self._config(value)

  @property
  def hide(self):
    """
    If and how to animate the hiding of the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-hide
    """
    return self._config_get(None)

  @hide.setter
  def hide(self, value):
    self._config(value)

  @property
  def maxHeight(self):
    """
    The maximum height to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-maxHeight
    """
    return self._config_group_get("option", None)

  @maxHeight.setter
  def maxHeight(self, value: int):
    self._config_group("option", value)

  @property
  def maxWidth(self):
    """
    The maximum width to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-maxWidth
    """
    return self._config_group_get("option", None)

  @maxWidth.setter
  def maxWidth(self, value: int):
    self._config_group("option", value)

  @property
  def minHeight(self):
    """
    The minimum height to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-minHeight
    """
    return self._config_group_get("option", None)

  @minHeight.setter
  def minHeight(self, value: int):
    self._config_group("option", value)

  @property
  def minWidth(self):
    """
    The minimum width to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-minWidth
    """
    return self._config_group_get("option", None)

  @minWidth.setter
  def minWidth(self, value: int):
    self._config_group("option", value)

  def position(self, my: str = "center", at: str = "center", of: str = "window"):
    """
    Specifies where the dialog should be displayed when opened. The dialog will handle collisions such that as much
    of the dialog is visible as possible.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-position

    :param my:
    :param at:
    :param of:
    """
    self._config({"my": my, "at": at, "of": of})
    return self

  @property
  def modal(self):
    """
    If set to true, the dialog will have modal behavior; other items on the page will be disabled, i.e.,
    cannot be interacted with.
    Modal dialogs create an overlay below the dialog but above other page elements.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-modal
    """
    return self._config_group_get("option", None)

  @modal.setter
  def modal(self, value: bool):
    self._config_group("option", value)

  @property
  def resizable(self):
    """
    If set to true, the dialog will be resizable. Requires the jQuery UI Resizable widget to be included.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-resizable
    """
    return self._config_group_get("option", None)

  @resizable.setter
  def resizable(self, value: bool):
    self._config_group("option", value)

  @property
  def title(self):
    """
    Specifies the title of the dialog. If the value is null, the title attribute on the dialog source element will
    be used.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-title
    """
    return self._config_get(None)

  @title.setter
  def title(self, value: str):
    self._config(value)

  @property
  def width(self):
    """
    The width of the dialog, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-title
    """
    return self._config_get(300)

  @width.setter
  def width(self, value: int):
    self._config(value)

  @property
  def empty(self):
    """
    Empty the dialog content first.

    This is the default behaviour in case of content as text.
    """
    return self._config_get(True)

  @empty.setter
  def empty(self, flag: bool):
    self._config(flag)


class OptionBar(Options):

  @property
  def draggable(self):
    """
    Set the bar draggable using Jquery UI
    """
    return self._config_get(False)

  @draggable.setter
  def draggable(self, flag: bool):
    self._config(flag)


class OptionsSkillbars(Options):
  component_properties = ("success", "warning", "danger", "percentage", "digits")

  def set_thresholds(self, inf: float = 20, sup: float = 50):
    self._config([inf, sup], name="thresholds")

  @property
  def thresholds(self):
    return self._config_get([20, 50])

  @property
  def digits(self):
    """ Number of digit for the percentage value.. """
    return self._config_get(2)

  @digits.setter
  def digits(self, num: int):
    self._config(num)

  @property
  def percentage(self):
    """
    Flag to display the percentage value on the bars.
    """
    return self._config_get(False)

  @percentage.setter
  def percentage(self, flag: bool):
    self._config(flag)

  @property
  def success(self):
    """
    """
    return self._config_get(self.page.theme.success[0])

  @success.setter
  def success(self, color: str):
    self._config(color)

  @property
  def warning(self):
    """
    """
    return self._config_get(self.page.theme.warning.light)

  @warning.setter
  def warning(self, color: str):
    self._config(color)

  @property
  def danger(self):
    """
    """
    return self._config_get(self.page.theme.danger.light)

  @danger.setter
  def danger(self, color: str):
    self._config(color)

  @property
  def width(self):
    """
    """
    return self._config_get(100)

  @width.setter
  def width(self, num: float):
    self._config(num)

  @property
  def height(self):
    """ Set height for the bars default 20px """
    return self._config_get(None)

  @height.setter
  def height(self, num: float):
    for row in self.component.innerPyHTML:
        row[1][0].style.css.line_height = num
        row[1][0].style.css.height = num
    self._config(num)

  @property
  def value(self):
    """ Key used in the record to get the value """
    return self._config_get("value")

  @value.setter
  def value(self, name: str):
    self._config(name)

  @property
  def label(self):
    """ Key used in the record to get the label """
    return self._config_get("label")

  @label.setter
  def label(self, name: str):
    self._config(name)

  def css(self, values: dict):
    """ Set CSS for bars """
    for row in self.component.innerPyHTML:
        row[1][0].css(values)
    self._config(values)