
from epyk.core.html.options import Options, OptionsWithTemplates


class OptionsTableRow(Options):
  @property
  def cssClasses(self):
    """
    """
    return self._config_get([])

  @cssClasses.setter
  def cssClasses(self, values):
    self._config(values)


class OptionsTableCell(OptionsWithTemplates):

  @property
  def cssClasses(self):
    """
    """
    return self._config_get([])

  @cssClasses.setter
  def cssClasses(self, values):
    self._config(values)

  @property
  def center(self):
    """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return self._config_get()

  @center.setter
  def center(self, flag):
    if flag:
      self.component.attr["class"].add("text-center")

  def position(self, alias):
    """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
    self.component.attr["class"].add("text-%s" % alias)

  def align(self, alias):
    """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
    self.component.attr["class"].add("align-%s" % alias)

  def padding(self, value, position="s"):
    """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/utilities/spacing/
    """
    self.component.attr["class"].add("p%s-%s" % (position, value))

  def margin(self, value, position="s"):
    """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/utilities/spacing/
    """
    self.component.attr["class"].add("m%s-%s" % (position, value))


class OptionsBasic(Options):
  @property
  def bordered(self):
    """
    Add .table-bordered for borders on all sides of the table and cells.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return self._config_get()

  @bordered.setter
  def bordered(self, flag):
    if flag:
      self.component.attr["class"].add("table-bordered")
    else:
      self.component.attr["class"].add("table-borderless")

  @property
  def hover(self):
    """
    Add .table-hover to enable a hover state on table rows within a <tbody>.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return self._config_get()

  @hover.setter
  def hover(self, flag):
    if flag:
      self.component.attr["class"].add("table-hover")

  def size(self, alias):
    """
    Add .table-sm to make any .table more compact by cutting all cell padding in half.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
    self.component.attr["class"].add("table-%s" % alias)

  @property
  def striped(self):
    """
    Add the striped CSS class from Bootstrap.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return self._config_get()

  @striped.setter
  def striped(self, flag):
    if flag:
      self.component.attr["class"].add("table-striped")

  @property
  def responsive(self):
    """
    Make the table responsive using Bootstrap class.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return self._config_get()

  @responsive.setter
  def responsive(self, flag):
    if flag:
      self.component.attr["class"].add("table-responsive")

  @property
  def rowCssClasses(self):
    """
    """
    return self._config_get([])

  @rowCssClasses.setter
  def rowCssClasses(self, values):
    self._config(values)

  @property
  def colCssClasses(self):
    """
    """
    return self._config_get([])

  @colCssClasses.setter
  def colCssClasses(self, values):
    self._config(values)

  @property
  def with_header(self):
    """
    """
    return self._config_get(True)

  @with_header.setter
  def with_header(self, flag):
    self._config(flag)

  @property
  def with_hover(self):
    """
    """
    return self._config_get(True)

  @with_hover.setter
  def with_hover(self, flag):
    self._config(flag)


class OptionsPivot(OptionsWithTemplates):
  component_properties = ('aggregator', 'aggregatorName', 'showUI', 'dataClass')

  @property
  def aggregator(self):
    """
    Constructor for an object which will aggregate results per cell (see documentation)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.aggregators['Count']()")

  @aggregator.setter
  def aggregator(self, attrs):
    self._config(attrs, js_type=True)

  @property
  def aggregatorName(self):
    """
    Name of the aggregator, used for display purposes in some renderers.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("Count")

  @aggregatorName.setter
  def aggregatorName(self, attrs):
    self._config(attrs)

  @property
  def cols(self):
    """
    Array of attribute names for use as columns.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get([])

  @cols.setter
  def cols(self, values):
    self._config(values)

  @property
  def showUI(self):
    """
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
    The order in which row data is provided to the renderer, must be one of "key_a_to_z", "value_a_to_z",
    "value_z_to_a", ordering by value orders by row total

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("")

  @rowOrder.setter
  def rowOrder(self, attrs):
    self._config(attrs)

  @property
  def rows(self):
    """
    Array of attribute names to use as rows.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get([])

  @rows.setter
  def rows(self, values):
    self._config(values)

  @property
  def colOrder(self):
    """
    the order in which column data is provided to the renderer, must be one of "key_a_to_z", "value_a_to_z",
    "value_z_to_a", ordering by value orders by column total

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
    Constructor for the data class to be built and passed to the Renderer (should be a subclass of the default)

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.PivotData")

  @dataClass.setter
  def dataClass(self, attrs):
    self._config(attrs, js_type=True)

  @property
  def filter(self):
    """
    Called on each record, returns false if the record is to be excluded from the input before rendering or
    true otherwise

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get('false')

  @filter.setter
  def filter(self, attrs):
    self._config(attrs, js_type=True)

  @property
  def sorters(self):
    """
    accessed or called with an attribute name and can return a function which can be used as an argument to array.sort
    for output purposes.
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
    Object passed through to renderer as options. See Renderers and Optional Extra Renderers for details.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get()

  @rendererOptions.setter
  def rendererOptions(self, attrs):
    self._config(attrs)


class OptionsPivotUI(OptionsPivot):
  component_properties = (
    'aggregator', 'aggregatorName', 'showUI',
    #'derivedAttributes',
    #'dataClass', 'sorters', 'rendererOptions',
    #'inclusions', 'exclusions', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop',
    #'menuLimit', 'autoSortUnusedAttrs', 'unusedAttrsVertical', 'rendererOptions'
  )

  @property
  def inclusions(self):
    """
    Object whose keys are attribute names and values are arrays of attribute values which denote records to include in
    rendering; used to prepopulate the filter menus that appear on double-click (overrides exclusions below).

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
    Object whose keys are attribute names and values are arrays of attribute values which denote records to exclude
    from rendering; used to prepopulate the filter menus that appear on double-click.

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
    Object whose keys are attribute names and values are arrays of attribute values which denote records to exclude
    from rendering; used to prepopulate the filter menus that appear on double-click.

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
    Contains attribute names to omit from the aggregator arguments dropdowns.

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
    Contains attribute names to omit from the drag'n'drop portion of the UI.

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
    Called upon renderer refresh with an object representing the current UI settings (see example).

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @onRefresh.setter
  def onRefresh(self, attrs):
    self._config(attrs, js_type=True)

  @property
  def menuLimit(self):
    """
    maximum number of values to list in the double-click menu.

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
    controls whether or not unused attributes are kept sorted in the UI.

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
    Controls whether or not unused attributes are shown vertically instead of the default which is horizontally.
    true means always vertical, false means always horizontal. If set to a number (as is the default) then
    if the attributes' names' combined length in characters exceeds the number then the attributes will be shown
    vertically.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get(85)

  @unusedAttrsVertical.setter
  def unusedAttrsVertical(self, flag):
    self._config(flag)

  @property
  def rendererOptions(self):
    """
    passed through to renderer as options. See Renderers and Optional Extra Renderers for details.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})

  @rendererOptions.setter
  def rendererOptions(self, flag):
    self._config(flag)

  @property
  def renderer(self):
    """

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.renderers")

  @renderer.setter
  def renderer(self, value):
    self._config(value, js_type=True)

  @property
  def renderers(self):
    """

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get("$.pivotUtilities.renderers")

  @renderers.setter
  def renderers(self, value):
    self._config(value, js_type=True)

  @property
  def rendererName(self):
    """

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get()

  @rendererName.setter
  def rendererName(self, value):
    self._config(value)
