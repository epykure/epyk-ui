

from epyk.core.html.options import Options


class OptionsSelect(Options):

  @property
  def all(self):
    """
    Description:
    ------------
    Specify if the all item should be added to the items.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("all", False)

  @all.setter
  def all(self, flag):
    self._report.attr["all"] = flag

  @property
  def empty(self):
    """
    Description:
    ------------
    Specify if the Empty item should be added to the items.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("empty", False)

  @empty.setter
  def empty(self, flag):
    self._report.attr["empty"] = flag

  @property
  def disabled(self):
    """
    Description:
    ------------

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("disabled", False)

  @disabled.setter
  def disabled(self, flag):
    self._report.attr["disabled"] = flag

  @property
  def drop_up(self):
    """
    Description:
    ------------
    dropupAuto is set to true by default, which automatically determines whether
    or not the menu should display above or below the select box.
    If dropupAuto is set to false, manually make the select a dropup menu by adding the .dropup class to the select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-dropup-auto", False)

  @drop_up.setter
  def drop_up(self, flag):
    self._report.attr["data-dropup-auto"] = flag

  @property
  def header(self):
    """
    Description:
    ------------
    Add a header to the dropdown menu, e.g. header: 'Select a condiment' or data-header="Select a condiment"

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-header")

  @header.setter
  def header(self, num):
    self._report.attr["data-header"] = num

  @property
  def live_search(self):
    """
    Description:
    ------------
    You can add a search input by passing data-live-search="true" attribute.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-live-search", False)

  @live_search.setter
  def live_search(self, flag):
    self._report.attr["data-live-search"] = flag

  @property
  def max_options(self):
    """
    Description:
    ------------
    Limit the number of options that can be selected via the data-max-options attribute.
    It also works for option groups. Customize the message displayed when the limit is reached with maxOptionsText.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-max-options", 1)

  @max_options.setter
  def max_options(self, num):
    self._report.attr["data-max-options"] = num

  @property
  def placeholder(self):
    """
    Description:
    ------------
    Using the title attribute will set the default placeholder text when nothing is selected.
    This works for both multiple and standard select boxes:

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("title", "")

  @placeholder.setter
  def placeholder(self, value):
    self._report.attr["title"] = value

  @property
  def selected(self):
    """
    Description:
    ------------
    The selected items
    """
    return self.get(None)

  @selected.setter
  def selected(self, value):
    self.set(value)

  @property
  def select_all(self):
    """
    Description:
    ------------
    Adds two buttons to the top of the menu - Select All & Deselect All with data-actions-box="true".

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-actions-box", False)

  @select_all.setter
  def select_all(self, flag):
    self._report.attr["data-actions-box"] = flag

  @property
  def selected_text_format(self):
    """
    Description:
    ------------
    Specify how the selection is displayed with the data-selected-text-format attribute on a multiple select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("ata-selected-text-format", "")

  @selected_text_format.setter
  def selected_text_format(self, value):
    self._report.attr["ata-selected-text-format"] = value

  @property
  def show_tick(self):
    """
    Description:
    ------------
    You can also show the checkmark icon on standard select boxes with the show-tick class:

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("show-tick", True)

  @show_tick.setter
  def show_tick(self, flag):
    self._report.attr["show-tick"] = flag

  @property
  def size(self):
    """
    Description:
    ------------
    Specify a number for data-size to choose the maximum number of items to show in the menu.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-size")

  @size.setter
  def size(self, num):
    self._report.attr["data-size"] = num

  @property
  def style(self):
    """
    Description:
    ------------

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("style", "")

  @style.setter
  def style(self, value):
    self._report.attr["style"] = value

  @property
  def title(self):
    """
    Description:
    ------------
    Using the title attribute will set the default placeholder text when nothing is selected.
    This works for both multiple and standard select boxes:

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("title", "")

  @title.setter
  def title(self, value):
    self._report.attr["title"] = value

  @property
  def width(self):
    """
    Description:
    ------------

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/examples/
    """
    return self._report.attr.get("data-width")

  @width.setter
  def width(self, value):
    self._report.attr["data-width"] = value


class OptionsSelectJs(OptionsSelect):
  component_properties = ("auto_select",)

  @property
  def config_default(self):
    """
    Description:
    -----------
    The default value for the configuration in case of template.
    Default value is an empty list.

    Usage::

      component.options.config_default = ["Test 1", "Test 2"]
    """
    return self.get([])

  @config_default.setter
  def config_default(self, flag):
    self.set(flag)

  @property
  def actionsBox(self):
    """
    Description:
    ------------
    When set to true, adds two buttons to the top of the dropdown menu (Select All & Deselect All).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @actionsBox.setter
  def actionsBox(self, flag):
    self._config(flag)

  @property
  def auto_select(self):
    """
    Description:
    ------------
    Auto select the item at the defined index in the list.
    Default will select the first item in the list.
    """
    return self._config_get(0)

  @auto_select.setter
  def auto_select(self, index):
    self._config(index)

  @property
  def container(self):
    """
    Description:
    ------------
    When set to a string, appends the select to a specific element or selector, e.g., container: 'body' | '.main-body'

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @container.setter
  def container(self, value):
    self._config(value)

  @property
  def deselectAllText(self):
    """
    Description:
    ------------
    The text on the button that deselects all options when actionsBox is enabled.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @deselectAllText.setter
  def deselectAllText(self, value):
    self._config(value)

  @property
  def dropdownAlignRight(self):
    """
    Description:
    ------------
    Align the menu to the right instead of the left. If set to 'auto', the menu will automatically align right
    if there isn't room for the menu's full width when aligned to the left.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @dropdownAlignRight.setter
  def dropdownAlignRight(self, flag):
    self._config(flag)

  @property
  def dropupAuto(self):
    """
    Description:
    ------------
    checks to see which has more room, above or below.
    If the dropup has enough room to fully open normally, but there is more room above, the dropup still opens normally.
    Otherwise, it becomes a dropup. If dropupAuto is set to false, dropups must be called manually.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @dropupAuto.setter
  def dropupAuto(self, flag):
    self._config(flag)

  @property
  def header(self):
    """
    Description:
    ------------
    adds a header to the top of the menu; includes a close button by default

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @header.setter
  def header(self, flag):
    self._config(flag)

  @property
  def hideDisabled(self):
    """
    Description:
    ------------
    removes disabled options and optgroups from the menu data-hide-disabled: true

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @hideDisabled.setter
  def hideDisabled(self, flag):
    self._config(flag)

  @property
  def iconBase(self):
    """
    Description:
    ------------
    Set the base to use a different icon font instead of Glyphicons.
    If changing iconBase, you might also want to change tickIcon,
    in case the new icon font uses a different naming scheme.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @iconBase.setter
  def iconBase(self, flag):
    self._config(flag)

  @property
  def liveSearch(self):
    """
    Description:
    ------------
    When set to true, adds a search box to the top of the selectpicker dropdown.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @liveSearch.setter
  def liveSearch(self, flag):
    self._config(flag)

  @property
  def liveSearchPlaceholder(self):
    """
    Description:
    ------------
    When set to a string, a placeholder attribute equal to the string will be added to the liveSearch input.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @liveSearchPlaceholder.setter
  def liveSearchPlaceholder(self, value):
    #self._report.attr["data-actions-box"] = value
    self._config(value)

  @property
  def liveSearchStyle(self):
    """
    Description:
    ------------
    When set to 'contains', searching will reveal options that contain the searched text.
    For example, searching for pl with return both Apple, Plum, and Plantain.
    When set to 'startsWith', searching for pl will return only Plum and Plantain.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @liveSearchStyle.setter
  def liveSearchStyle(self, value):
    self._config(value)

  @property
  def maxOptions(self):
    """
    Description:
    ------------
    When set to an integer and in a multi-select, the number of selected options cannot exceed the given value.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @maxOptions.setter
  def maxOptions(self, value):
    self._config(value)

  @property
  def maxOptionsText(self):
    """
    Description:
    ------------
    The text that is displayed when maxOptions is enabled and the maximum number of options for the given scenario have
    been selected.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @maxOptionsText.setter
  def maxOptionsText(self, value):
    self._config(value)

  @property
  def mobile(self):
    """
    Description:
    ------------
    When set to true, enables the device's native menu for select menus.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @mobile.setter
  def mobile(self, bool):
    self._config(bool)

  @property
  def noneSelectedText(self):
    """
    Description:
    ------------
    The text that is displayed when a multiple select has no selected options.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @noneSelectedText.setter
  def noneSelectedText(self, value):
    self._config(value)

  @property
  def noneResultsText(self):
    """
    Description:
    ------------
    The text displayed when a search doesn't return any results.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @noneResultsText.setter
  def noneResultsText(self, value):
    self._config(value)

  @property
  def selected(self):
    """
    Description:
    ------------
    The selected items
    """
    return self.get(None)

  @selected.setter
  def selected(self, value):
    if hasattr(self.component, "_vals"):
      for rec in self.component._vals:
        if rec.get("selected"):
          rec["selected"] = False
        if rec["value"] == value:
          rec["selected"] = True
    self.set(value)

  @property
  def selectAllText(self):
    """
    Description:
    ------------
    The text on the button that selects all options when actionsBox is enabled.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @selectAllText.setter
  def selectAllText(self, value):
    self._config(value)

  @property
  def selectOnTab(self):
    """
    Description:
    ------------
    When set to true, treats the tab character like the enter or space characters within the selectpicker dropdown.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @selectOnTab.setter
  def selectOnTab(self, flag):
    self._config(flag)

  @property
  def showContent(self):
    """
    Description:
    ------------
    When set to true, display custom HTML associated with selected option(s) in the button.
    When set to false, the option value will be displayed instead.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @showContent.setter
  def showContent(self, flag):
    self._config(flag)

  @property
  def showIcon(self):
    """
    Description:
    ------------
    When set to true, display icon(s) associated with selected option(s) in the button.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @showIcon.setter
  def showIcon(self, flag):
    self._config(flag)

  @property
  def showSubtext(self):
    """
    Description:
    ------------
    When set to true, display subtext associated with a selected option in the button.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @showSubtext.setter
  def showSubtext(self, flag):
    self._config(flag)

  @property
  def showTick(self):
    """
    Description:
    ------------
    Show checkmark on selected option (for items without multiple attribute).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @showTick.setter
  def showTick(self, flag):
    self._config(flag)

  @property
  def size(self):
    """
    Description:
    ------------
    When set to 'auto', the menu always opens up to show as many items as the window will allow without being cut off.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @size.setter
  def size(self, value):
    self._config(value)

  @property
  def style(self):
    """
    Description:
    ------------
    When set to a string, add the value to the button's style.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @style.setter
  def style(self, value):
    self._config(value)

  @property
  def styleBase(self):
    """
    Description:
    ------------
    The default class applied to the button. When using the setStyle method, this class will always remain.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @styleBase.setter
  def styleBase(self, value):
    self._config(value)

  @property
  def tickIcon(self):
    """
    Description:
    ------------
    Set which icon to use to display as the "tick" next to selected options.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @tickIcon.setter
  def tickIcon(self, value):
    self._config(value)

  @property
  def title(self):
    """
    Description:
    ------------
    The default title for the selectpicker.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @title.setter
  def title(self, value):
    self._config(value)

  @property
  def virtualScroll(self):
    """
    Description:
    ------------
    If enabled, the items in the dropdown will be rendered using virtualization
    (i.e. only the items that are within the viewport will be rendered).

    This drastically improves performance for selects with a large number of options.
    Set to an integer to only use virtualization if the select has at least that number of options.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @virtualScroll.setter
  def virtualScroll(self, value):
    self._config(value)

  @property
  def width(self):
    """
    Description:
    ------------
    When set to auto, the width of the selectpicker is automatically adjusted to accommodate the widest option.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @width.setter
  def width(self, value):
    self._config(value)

  @property
  def windowPadding(self):
    """
    Description:
    ------------
    This is useful in cases where the window has areas that the dropdown menu should not cover -
    for instance a fixed header. When set to an integer, the same padding will be added to all sides.
    Alternatively, an array of integers can be used in the format [top, right, bottom, left].

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @windowPadding.setter
  def windowPadding(self, value):
    self._config(value)

  @property
  def sanitize(self):
    """
    Description:
    ------------
    Enable or disable the sanitization. If activated, 'data-content' on individual options will be sanitized.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @sanitize.setter
  def sanitize(self, flag):
    self._config(flag)
