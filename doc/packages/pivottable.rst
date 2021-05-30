PivotTable.js
=============

- Documentation: https://pivottable.js.org/examples/
- NPM alias: ``pivottable``
- Package Type: JavaScript


---------------------


The package **pivottable** is available in the framework by using the following component::

    languages = [
      {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
      {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
    ]

    tb = page.ui.tables.pivot(languages, ['name'], ['type'])

The above will display a pivot table. More details available on the website: https://github.com/nicolaskruchten/pivottable/wiki

Options
*******

It is possible to use aggregator and renderers directly in the fframework.
The below will use the sum aggregator on the column rating::

    tb = page.ui.tables.pivot(languages, ['name'], ['type'])
    tb.aggregators.sum('rating')

More bespoke ones are also available::

    tb.aggregators.diffAbsolute('change', 'rating')

And it is possible to create custom ones::

    tb.aggregators.quick("change", "Abs Change", "+= Math.abs(col1)")

Different renders are available in the property ``page.ui.tables.pivots.``

And all pivottables options are available ``tb.options``. A detailled documentation is available for each property::

  @property
  def exclusions(self):
    """
    Description:
    ------------
    Object whose keys are attribute names and values are arrays of attribute values which denote records to exclude
    from rendering; used to prepopulate the filter menus that appear on double-click.

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Parameters
    """
    return self._config_get({})


Style
*****

This component will have some predefined CSS class in order to change the nav bar and the button but it is possible
as any other component to change the style by using the ``style.css`` property.

