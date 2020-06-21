

from epyk.core.html.options import Options


class OptionsSelect(Options):

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
  def actionsBox(self, bool):
    self._config(bool)

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
    Align the menu to the right instead of the left. If set to 'auto', the menu will automatically align right if there isn't room for the menu's full width when aligned to the left.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @dropdownAlignRight.setter
  def dropdownAlignRight(self, bool):
    self._config(bool)

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
  def dropupAuto(self, bool):
    self._config(bool)

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
  def header(self, bool):
    self._config(bool)

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
  def hideDisabled(self, bool):
    self._config(bool)

  @property
  def iconBase(self):
    """
    Description:
    ------------
    Set the base to use a different icon font instead of Glyphicons.
    If changing iconBase, you might also want to change tickIcon, in case the new icon font uses a different naming scheme.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._config_get(False)

  @iconBase.setter
  def iconBase(self, bool):
    self._config(bool)

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
  def liveSearch(self, bool):
    self._config(bool)

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
    The text that is displayed when maxOptions is enabled and the maximum number of options for the given scenario have been selected.

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
  def selectOnTab(self, bool):
    self._config(bool)

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
  def showContent(self, bool):
    self._config(bool)

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
  def showIcon(self, bool):
    self._config(bool)

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
  def showSubtext(self, bool):
    self._config(bool)

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
  def showTick(self, bool):
    self._config(bool)

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
    If enabled, the items in the dropdown will be rendered using virtualization (i.e. only the items that are within the viewport will be rendered).
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
    This is useful in cases where the window has areas that the dropdown menu should not cover - for instance a fixed header.
    When set to an integer, the same padding will be added to all sides.
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
  def sanitize(self, bool):
    self._config(bool)
