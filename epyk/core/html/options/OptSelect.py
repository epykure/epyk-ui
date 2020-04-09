
from epyk.core.data import DataClass


class OptionsSelect(DataClass):

  @property
  def actionsBox(self):
    """
    Description:
    ------------
    When set to true, adds two buttons to the top of the dropdown menu (Select All & Deselect All).

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('actionsBox', False)

  @actionsBox.setter
  def actionsBox(self, bool):
    self._report._jsStyles["actionsBox"] = bool
    self.set(bool)

  @property
  def container(self):
    """
    Description:
    ------------
    When set to a string, appends the select to a specific element or selector, e.g., container: 'body' | '.main-body'

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('actionsBox', False)

  @container.setter
  def container(self, bool):
    self._report._jsStyles["container"] = bool
    return self.set(bool)

  @property
  def deselectAllText(self):
    """
    Description:
    ------------
    The text on the button that deselects all options when actionsBox is enabled.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('deselectAllText', False)

  @deselectAllText.setter
  def deselectAllText(self, value):
    self._report._jsStyles["deselectAllText"] = value
    return self.set(value)

  @property
  def dropdownAlignRight(self):
    """
    Description:
    ------------
    Align the menu to the right instead of the left. If set to 'auto', the menu will automatically align right if there isn't room for the menu's full width when aligned to the left.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('dropdownAlignRight', False)

  @dropdownAlignRight.setter
  def dropdownAlignRight(self, bool):
    self._report._jsStyles["dropdownAlignRight"] = bool
    return self.set(bool)

  @property
  def dropupAuto(self):
    """
    Description:
    ------------
    checks to see which has more room, above or below.
    If the dropup has enough room to fully open normally, but there is more room above, the dropup still opens normally.
    Otherwise, it becomes a dropup. If dropupAuto is set to false, dropups must be called manually.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('dropupAuto', False)

  @dropupAuto.setter
  def dropupAuto(self, bool):
    self._report._jsStyles["dropupAuto"] = bool
    return self.set(bool)

  @property
  def header(self):
    """
    Description:
    ------------
    adds a header to the top of the menu; includes a close button by default

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('header', False)

  @header.setter
  def header(self, bool):
    self._report._jsStyles["header"] = bool
    return self.set(bool)

  @property
  def hideDisabled(self):
    """
    Description:
    ------------
    removes disabled options and optgroups from the menu data-hide-disabled: true

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('hideDisabled', False)

  @hideDisabled.setter
  def hideDisabled(self, bool):
    self._report._jsStyles["hideDisabled"] = bool
    return self.set(bool)

  @property
  def iconBase(self):
    """
    Description:
    ------------
    Set the base to use a different icon font instead of Glyphicons.
    If changing iconBase, you might also want to change tickIcon, in case the new icon font uses a different naming scheme.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('iconBase', False)

  @iconBase.setter
  def iconBase(self, bool):
    self._report._jsStyles["iconBase"] = bool
    return self.set(bool)

  @property
  def liveSearch(self):
    """
    Description:
    ------------
    When set to true, adds a search box to the top of the selectpicker dropdown.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('liveSearch', False)

  @liveSearch.setter
  def liveSearch(self, bool):
    self._report._jsStyles["liveSearch"] = bool
    return self.set(bool)

  @property
  def liveSearchPlaceholder(self):
    """
    Description:
    ------------
    When set to a string, a placeholder attribute equal to the string will be added to the liveSearch input.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('liveSearchPlaceholder', False)

  @liveSearchPlaceholder.setter
  def liveSearchPlaceholder(self, value):
    self._report._jsStyles["liveSearchPlaceholder"] = value
    return self.set(value)

  @property
  def liveSearchStyle(self):
    """
    Description:
    ------------
    When set to 'contains', searching will reveal options that contain the searched text.
    For example, searching for pl with return both Apple, Plum, and Plantain.
    When set to 'startsWith', searching for pl will return only Plum and Plantain.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('liveSearchPlaceholder', False)

  @liveSearchStyle.setter
  def liveSearchStyle(self, value):
    self._report._jsStyles["liveSearchStyle"] = value
    return self.set(value)

  @property
  def maxOptions(self):
    """
    Description:
    ------------
    When set to an integer and in a multi-select, the number of selected options cannot exceed the given value.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('maxOptions', False)

  @maxOptions.setter
  def maxOptions(self, value):
    self._report._jsStyles["maxOptions"] = value
    return self.set(value)

  @property
  def maxOptionsText(self):
    """
    Description:
    ------------
    The text that is displayed when maxOptions is enabled and the maximum number of options for the given scenario have been selected.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('maxOptionsText', False)

  @maxOptionsText.setter
  def maxOptionsText(self, value):
    self._report._jsStyles["maxOptionsText"] = value
    return self.set(value)

  @property
  def mobile(self):
    """
    Description:
    ------------
    When set to true, enables the device's native menu for select menus.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('mobile', False)

  @mobile.setter
  def mobile(self, bool):
    self._report._jsStyles["mobile"] = bool
    return self.set(bool)

  @property
  def noneSelectedText(self):
    """
    Description:
    ------------
    The text that is displayed when a multiple select has no selected options.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('noneSelectedText', False)

  @noneSelectedText.setter
  def noneSelectedText(self, value):
    self._report._jsStyles["noneSelectedText"] = value
    return self.set(value)

  @property
  def noneResultsText(self):
    """
    Description:
    ------------
    The text displayed when a search doesn't return any results.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('noneResultsText', False)

  @noneResultsText.setter
  def noneResultsText(self, value):
    self._report._jsStyles["noneResultsText"] = value
    return self.set(value)

  @property
  def selectAllText(self):
    """
    Description:
    ------------
    The text on the button that selects all options when actionsBox is enabled.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('selectAllText', False)

  @selectAllText.setter
  def selectAllText(self, value):
    self._report._jsStyles["selectAllText"] = value
    return self.set(value)

  @property
  def selectOnTab(self):
    """
    Description:
    ------------
    When set to true, treats the tab character like the enter or space characters within the selectpicker dropdown.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('selectOnTab', False)

  @selectOnTab.setter
  def selectOnTab(self, bool):
    self._report._jsStyles["selectOnTab"] = bool
    return self.set(bool)

  @property
  def showContent(self):
    """
    Description:
    ------------
    When set to true, display custom HTML associated with selected option(s) in the button.
    When set to false, the option value will be displayed instead.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('showContent', False)

  @showContent.setter
  def showContent(self, bool):
    self._report._jsStyles["showContent"] = bool
    return self.set(bool)

  @property
  def showIcon(self):
    """
    Description:
    ------------
    When set to true, display icon(s) associated with selected option(s) in the button.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('showIcon', False)

  @showIcon.setter
  def showIcon(self, bool):
    self._report._jsStyles["showIcon"] = bool
    return self.set(bool)

  @property
  def showSubtext(self):
    """
    Description:
    ------------
    When set to true, display subtext associated with a selected option in the button.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('showSubtext', False)

  @showSubtext.setter
  def showSubtext(self, bool):
    self._report._jsStyles["showSubtext"] = bool
    return self.set(bool)

  @property
  def showTick(self):
    """
    Description:
    ------------
    Show checkmark on selected option (for items without multiple attribute).

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('showTick', False)

  @showTick.setter
  def showTick(self, bool):
    self._report._jsStyles["showTick"] = bool
    return self.set(bool)

  @property
  def size(self):
    """
    Description:
    ------------
    When set to 'auto', the menu always opens up to show as many items as the window will allow without being cut off.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('size', False)

  @size.setter
  def size(self, value):
    self._report._jsStyles["size"] = value
    return self.set(value)

  @property
  def style(self):
    """
    Description:
    ------------
    When set to a string, add the value to the button's style.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('style', False)

  @style.setter
  def style(self, value):
    self._report._jsStyles["style"] = value
    return self.set(value)

  @property
  def tickIcon(self):
    """
    Description:
    ------------
    Set which icon to use to display as the "tick" next to selected options.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('tickIcon', False)

  @tickIcon.setter
  def tickIcon(self, value):
    self._report._jsStyles["tickIcon"] = value
    return self.set(value)

  @property
  def title(self):
    """
    Description:
    ------------
    The default title for the selectpicker.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('title', False)

  @title.setter
  def title(self, value):
    self._report._jsStyles["title"] = value
    return self.set(value)

  @property
  def virtualScroll(self):
    """
    Description:
    ------------
    If enabled, the items in the dropdown will be rendered using virtualization (i.e. only the items that are within the viewport will be rendered).
    This drastically improves performance for selects with a large number of options.
    Set to an integer to only use virtualization if the select has at least that number of options.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('virtualScroll', False)

  @virtualScroll.setter
  def virtualScroll(self, value):
    self._report._jsStyles["virtualScroll"] = value
    return self.set(value)

  @property
  def width(self):
    """
    Description:
    ------------
    When set to auto, the width of the selectpicker is automatically adjusted to accommodate the widest option.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('width', False)

  @width.setter
  def width(self, value):
    self._report._jsStyles["width"] = value
    return self.set(value)

  @property
  def windowPadding(self):
    """
    Description:
    ------------
    This is useful in cases where the window has areas that the dropdown menu should not cover - for instance a fixed header.
    When set to an integer, the same padding will be added to all sides.
    Alternatively, an array of integers can be used in the format [top, right, bottom, left].

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('windowPadding', False)

  @windowPadding.setter
  def windowPadding(self, value):
    self._report._jsStyles["windowPadding"] = value
    return self.set(value)

  @property
  def sanitize(self):
    """
    Description:
    ------------
    Enable or disable the sanitization. If activated, 'data-content' on individual options will be sanitized.

    Related Pages:
    --------------
    https://developer.snapappointments.com/bootstrap-select/options/
    """
    return self._attrs.get('sanitize', False)

  @sanitize.setter
  def sanitize(self, bool):
    self._report._jsStyles["sanitize"] = bool
    return self.set(bool)
