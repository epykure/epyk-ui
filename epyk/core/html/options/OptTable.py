"""

https://github.com/nicolaskruchten/pivottable/wiki/Parameters
"""

from epyk.core.html.options import Options


class OptionsPivot(Options):
  component_properties = ('aggregator', 'aggregatorName', 'showUI',
                          'dataClass')

  @property
  def aggregator(self):
    """
    Description:
    ------------
    constructor for an object which will aggregate results per cell (see documentation)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.aggregators['Count']()")

  @aggregator.setter
  def aggregator(self, attrs):
    self.js_type['aggregator'] = True
    self._config(attrs)

  @property
  def aggregatorName(self):
    """
    Description:
    ------------
    Name of the aggregator, used for display purposes in some renderers

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("Count")

  @aggregatorName.setter
  def aggregatorName(self, attrs):
    self._config(attrs)

  @property
  def showUI(self):
    """
    Description:
    ------------
    Show the drag and drop UI panel

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get(True)

  @showUI.setter
  def showUI(self, attrs):
    self._config(attrs)

  @property
  def rowOrder(self):
    """
    Description:
    ------------
    The order in which row data is provided to the renderer, must be one of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value orders by row total

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("")

  @rowOrder.setter
  def rowOrder(self, attrs):
    self._config(attrs)

  @property
  def colOrder(self):
    """
    Description:
    ------------
    the order in which column data is provided to the renderer, must be one of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value orders by column total

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("")

  @colOrder.setter
  def colOrder(self, attrs):
    self._config(attrs)

  @property
  def derivedAttributes(self):
    """
    Description:
    ------------
    object to define derived attributes

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @derivedAttributes.setter
  def derivedAttributes(self, attrs):
    self._config(attrs)

  @property
  def dataClass(self):
    """
    Description:
    ------------
    Constructor for the data class to be built and passed to the Renderer (should be a subclass of the default)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.PivotData")

  @dataClass.setter
  def dataClass(self, attrs):
    self.js_type['dataClass'] = True
    self._config(attrs)

  @property
  def filter(self):
    """
    Description:
    ------------
    Called on each record, returns false if the record is to be excluded from the input before rendering or true otherwise

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get('false')

  @filter.setter
  def filter(self, attrs):
    self.js_type['filter'] = True
    self._config(attrs)

  @property
  def sorters(self):
    """
    Description:
    ------------
    accessed or called with an attribute name and can return a function which can be used as an argument to array.sort for output purposes.
    If no function is returned, the default sorting mechanism is a built-in "natural sort" implementation.
    Useful for sorting attributes like month names, see example 1 and example 2.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get()

  @sorters.setter
  def sorters(self, attrs):
    self._config(attrs)

  @property
  def rendererOptions(self):
    """
    Description:
    ------------
    Object passed through to renderer as options. See Renderers and Optional Extra Renderers for details.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get()

  @rendererOptions.setter
  def rendererOptions(self, attrs):
    self._config(attrs)


class OptionsPivotUI(OptionsPivot):
  component_properties = ('aggregator', 'aggregatorName', 'showUI', 'derivedAttributes',
    'dataClass', 'sorters', 'rendererOptions',
    'inclusions', 'exclusions', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop',
    'menuLimit', 'autoSortUnusedAttrs', 'unusedAttrsVertical', 'rendererOptions')

  @property
  def inclusions(self):
    """
    Description:
    ------------
    object whose keys are attribute names and values are arrays of attribute values which denote records to include in rendering; used to prepopulate the filter menus that appear on double-click (overrides exclusions below)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @inclusions.setter
  def inclusions(self, attrs):
    self._config(attrs)

  @property
  def exclusions(self):
    """
    Description:
    ------------
    object whose keys are attribute names and values are arrays of attribute values which denote records to exclude from rendering; used to prepopulate the filter menus that appear on double-click

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @exclusions.setter
  def exclusions(self, attrs):
    self._config(attrs)

  @property
  def hiddenAttributes(self):
    """
    Description:
    ------------
    object whose keys are attribute names and values are arrays of attribute values which denote records to exclude from rendering; used to prepopulate the filter menus that appear on double-click

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @hiddenAttributes.setter
  def hiddenAttributes(self, attrs):
    self._config(attrs)

  @property
  def hiddenFromAggregators(self):
    """
    Description:
    ------------
    contains attribute names to omit from the aggregator arguments dropdowns

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @hiddenFromAggregators.setter
  def hiddenFromAggregators(self, attrs):
    self._config(attrs)

  @property
  def hiddenFromDragDrop(self):
    """
    Description:
    ------------
    contains attribute names to omit from the drag'n'drop portion of the UI

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @hiddenFromDragDrop.setter
  def hiddenFromDragDrop(self, attrs):
    self._config(attrs)

  @property
  def onRefresh(self):
    """
    Description:
    ------------
    called upon renderer refresh with an object representing the current UI settings (see example)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @onRefresh.setter
  def onRefresh(self, attrs):
    self.js_type['onRefresh'] = True
    self._config(attrs)

  @property
  def menuLimit(self):
    """
    Description:
    ------------
    maximum number of values to list in the double-click menu

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @menuLimit.setter
  def menuLimit(self, attrs):
    self._config(attrs)

  @property
  def autoSortUnusedAttrs(self):
    """
    Description:
    ------------
    controls whether or not unused attributes are kept sorted in the UI

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get(False)

  @autoSortUnusedAttrs.setter
  def autoSortUnusedAttrs(self, attrs):
    self._config(attrs)

  @property
  def unusedAttrsVertical(self):
    """
    Description:
    ------------
    Controls whether or not unused attributes are shown vertically instead of the default which is horizontally. true means always vertical, false means always horizontal. If set to a number (as is the default) then if the attributes' names' combined length in characters exceeds the number then the attributes will be shown vertically

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get(85)

  @unusedAttrsVertical.setter
  def unusedAttrsVertical(self, bool):
    self._config(bool)

  @property
  def rendererOptions(self):
    """
    Description:
    ------------
    passed through to renderer as options. See Renderers and Optional Extra Renderers for details.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @rendererOptions.setter
  def rendererOptions(self, bool):
    self._config(bool)

  @property
  def renderer(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.renderers")

  @renderer.setter
  def renderer(self, value):
    self.js_type['renderers'] = True
    self._config(value)

  @property
  def renderers(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.renderers")

  @renderers.setter
  def renderers(self, value):
    self.js_type['renderers'] = True
    self._config(value)

  @property
  def rendererName(self):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get()

  @rendererName.setter
  def rendererName(self, value):
    self._config(value)
