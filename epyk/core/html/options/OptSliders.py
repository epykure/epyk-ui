
from epyk.core.html.options import Options


class OptionsSlider(Options):

  @property
  def animate(self):
    """
    Description:
    ------------
    Whether to slide the handle smoothly when the user clicks on the slider track. Also accepts any valid animation

    Related Pages:

      https://api.jqueryui.com/slider/#option-animate

		:param animate:
    """
    return self._config_get(False)

  @animate.setter
  def animate(self, value):
    self._config(value)

  @property
  def classes(self):
    """
    Description:
    ------------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the classes option.

    Related Pages:

      https://api.jqueryui.com/slider/#option-classes

		:param classes:
    """
    return self._config_get('classes')

  @classes.setter
  def classes(self, value):
    self._config(value)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the slider if set to true.

    Related Pages:

      https://api.jqueryui.com/slider/#option-disabled

		:param disabled:
    """
    return self._config_get(False)

  @disabled.setter
  def disabled(self, value):
    self._config(value)

  @property
  def max(self):
    """
    Description:
    ------------
    The maximum value of the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#option-max

		:param max:
    """
    return self._config_get(100)

  @max.setter
  def max(self, value):
    self._config(value)

  @property
  def min(self):
    """
    Description:
    ------------
    The minimum value of the slider.

    Related Pages:

      https://api.jqueryui.com/slider/#option-min

		:param min:
    """
    return self._config_get(0)

  @min.setter
  def min(self, value):
    self._config(value)

  @property
  def orientation(self):
    """
    Description:
    ------------
    Determines whether the slider handles move horizontally (min on left, max on right) or vertically (min on bottom, max on top).
    Possible values: "horizontal", "vertical".

    Related Pages:

      https://api.jqueryui.com/slider/#option-orientation
    """
    return self._config_get("horizontal")

  @orientation.setter
  def orientation(self, value):
    self._config(value)

  @property
  def range(self):
    """
    Description:
    ------------
    Whether the slider represents a range.

    Related Pages:

      https://api.jqueryui.com/slider/#option-range
    """
    return self._config_get(False)

  @range.setter
  def range(self, value):
    self._config(value)

  @property
  def step(self):
    """
    Description:
    ------------
    Determines the size or amount of each interval or step the slider takes between the min and max.
    The full specified value range of the slider (max - min) should be evenly divisible by the step.

    Related Pages:

      https://api.jqueryui.com/slider/#option-step
    """
    return self._config_get(1)

  @step.setter
  def step(self, value):
    self._config(value)

  @property
  def value(self):
    """
    Description:
    ------------
    Determines the value of the slider, if there's only one handle.
    If there is more than one handle, determines the value of the first handle.

    Related Pages:

      https://api.jqueryui.com/slider/#option-value
    """
    return self._config_get(0)

  @value.setter
  def value(self, value):
    self._config(value)

  @property
  def values(self):
    """
    Description:
    ------------
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

  @property
  def classes(self):
    """
    Description:
    ------------
    Initialize the progressbar with the classes option specified, changing the theming for the ui-progressbar

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-classes
    """
    return self._config_get(None)

  @classes.setter
  def classes(self, value):
    self._config(value)

  @property
  def background(self):
    """
    Description:
    ------------

    """
    return self._config_group_get('css', None)

  @background.setter
  def background(self, value):
    self._config_group('css', value)

  def css(self, attrs):
    """
    Description:
    ------------

    :param attrs:
    """
    css_attrs = self._config_get('css', {})
    css_attrs.update(attrs)
    self._config(css_attrs)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the progressbar if set to true.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-disabled
    """
    return self._config_get(None)

  @disabled.setter
  def disabled(self, bool):
    self._config(bool)

  @property
  def max(self):
    """
    Description:
    ------------
    The maximum value of the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-max
    """
    return self._config_get(100)

  @max.setter
  def max(self, num):
    self._config(num)

  @property
  def value(self):
    """
    Description:
    ------------
    The value of the progressbar.

    Related Pages:

      https://api.jqueryui.com/progressbar/#option-value
    """
    return self._config_get(None)

  @value.setter
  def value(self, val):
    self._config(val)


class OptionsMenu(Options):

  @property
  def classes(self):
    """
    Description:
    ------------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the

    Related Pages:

      https://api.jqueryui.com/menu/#option-classes
    """
    return self._config_get({})

  @classes.setter
  def classes(self, value):
    self._config(value)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the menu if set to true

    Related Pages:

      https://api.jqueryui.com/menu/#option-disabled
    """
    return self._config_get(False)

  @disabled.setter
  def disabled(self, bool):
    self._config(bool)

  @property
  def icons(self):
    """
    Description:
    ------------
    Icons to use for submenus, matching an icon provided by the jQuery UI CSS Framework.

    Related Pages:

      https://api.jqueryui.com/menu/#option-icons
    """
    return self._config_get(None)

  @icons.setter
  def icons(self, bool):
    self._config(bool)

  @property
  def position(self):
    """
    Description:
    ------------
    Identifies the position of submenus in relation to the associated parent menu item.
    The of option defaults to the parent menu item, but you can specify another element to position against.
    You can refer to the jQuery UI Position utility for more details about the various options.

    Related Pages:

      https://api.jqueryui.com/menu/#option-position
    """
    return self._config_get(None)

  @position.setter
  def position(self, bool):
    self._config(bool)


class OptionDialog(Options):

  @property
  def appendTo(self):
    """
    Description:
    ------------
    Which element the dialog (and overlay, if modal) should be appended to

    Related Pages:

      https://api.jqueryui.com/dialog/#option-appendTo
    """
    return self._config_get('body')

  @appendTo.setter
  def appendTo(self, bool):
    self._config(bool)

  @property
  def autoOpen(self):
    """
    Description:
    ------------
    If set to true, the dialog will automatically open upon initialization.
    If false, the dialog will stay hidden until the open() method is called.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-autoOpen
    """
    return self._config_get(True)

  @autoOpen.setter
  def autoOpen(self, bool):
    self._config(bool)

  @property
  def classes(self):
    """
    Description:
    ------------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the

    Related Pages:

      https://api.jqueryui.com/dialog/#option-classes
    """
    return self._config_get({})

  @classes.setter
  def classes(self, value):
    self._config(value)

  @property
  def closeOnEscape(self):
    """
    Description:
    ------------
    Specifies whether the dialog should close when it has focus and the user presses the escape (ESC) key.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-closeOnEscape
    """
    return self._config_get(True)

  @closeOnEscape.setter
  def closeOnEscape(self, value):
    self._config(value)

  @property
  def closeText(self):
    """
    Description:
    ------------
    Specifies the text for the close button. Note that the close text is visibly hidden when using a standard theme.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-closeText
    """
    return self._config_get(True)

  @closeText.setter
  def closeText(self, value):
    self._config(value)

  @property
  def draggable(self):
    """
    Description:
    ------------
    If set to true, the dialog will be draggable by the title bar. Requires the jQuery UI Draggable widget to be included.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-draggable
    """
    return self._config_get(True)

  @draggable.setter
  def draggable(self, value):
    self._config(value)

  @property
  def height(self):
    """
    Description:
    ------------
    The height of the dialog.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-height
    """
    return self._config_get('auto')

  @height.setter
  def height(self, value):
    self._config(value)

  @property
  def hide(self):
    """
    Description:
    ------------
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
    Description:
    ------------
    The maximum height to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-maxHeight
    """
    return self._config_group_get("option", None)

  @maxHeight.setter
  def maxHeight(self, value):
    self._config_group("option", value)

  @property
  def maxWidth(self):
    """
    Description:
    ------------
    The maximum width to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-maxWidth
    """
    return self._config_group_get("option", None)

  @maxWidth.setter
  def maxWidth(self, value):
    self._config_group("option", value)

  @property
  def minHeight(self):
    """
    Description:
    ------------
    The minimum height to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-minHeight
    """
    return self._config_group_get("option", None)

  @minHeight.setter
  def minHeight(self, value):
    self._config_group("option", value)

  @property
  def minWidth(self):
    """
    Description:
    ------------
    The minimum width to which the dialog can be resized, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-minWidth
    """
    return self._config_group_get("option", None)

  @minWidth.setter
  def minWidth(self, value):
    self._config_group("option", value)

  def position(self, my="center", at="center", of="window"):
    """
    Description:
    ------------
    Specifies where the dialog should be displayed when opened. The dialog will handle collisions such that as much of the dialog is visible as possible.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-position

    :param my: String.
    :param at: String.
    :param of: String.
    """
    self._config({"my": my, "at": at, "of": of})
    return self

  @property
  def modal(self):
    """
    Description:
    ------------
    If set to true, the dialog will have modal behavior; other items on the page will be disabled, i.e., cannot be interacted with.
    Modal dialogs create an overlay below the dialog but above other page elements.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-modal
    """
    return self._config_group_get("option", None)

  @modal.setter
  def modal(self, value):
    self._config_group("option", value)

  @property
  def resizable(self):
    """
    Description:
    ------------
    If set to true, the dialog will be resizable. Requires the jQuery UI Resizable widget to be included.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-resizable
    """
    return self._config_group_get("option", None)

  @resizable.setter
  def resizable(self, value):
    self._config_group("option", value)

  @property
  def title(self):
    """
    Description:
    ------------
    Specifies the title of the dialog. If the value is null, the title attribute on the dialog source element will be used.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-title
    """
    return self._config_get(None)

  @title.setter
  def title(self, value):
    self._config(value)

  @property
  def width(self):
    """
    Description:
    ------------
    The width of the dialog, in pixels.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-title

		:param width:
    """
    return self._config_get(300)

  @width.setter
  def width(self, value):
    self._config(value)


class OptionBar(Options):

  @property
  def draggable(self):
    """
    Description:
    ------------
    Set the bar draggable using Jquery UI
    """
    return self._config_get(False)

  @draggable.setter
  def draggable(self, bool):
    self._config(bool)
