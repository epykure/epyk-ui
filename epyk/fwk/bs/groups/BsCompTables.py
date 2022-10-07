
class Components:
  def __init__(self, ui):
    self.page = ui.page

  def basic(self, records, cols=None, rows=None, category=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """  
    Documentation and examples for opt-in styling of tables (given their prevalent use in JavaScript plugins)
    with Bootstrap.

    Usage::

      from epyk.tests import mocks

      t = page.web.bs.table(mocks.popularity_2020)

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/

    :param records: List<dict>. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param category: String. Optional. The Bootstrap predefined category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.std.tables.basic(records, cols, rows, width, height, html_code, options, profile)
    component.style.clear_style()
    component.attr["class"].initialise(["table"])
    component.options.responsive = True
    component.options.hover = True
    if category is not None:
      component.attr["class"].add("table-%s" % category)
    return component

  def striped(self, records, cols=None, rows=None, category=None, width=(100, '%'), height=(None, 'px'), html_code=None,
              options=None, profile=None):
    """  
    Documentation and examples for opt-in styling of tables (given their prevalent use in JavaScript plugins)
    with Bootstrap.

    Usage::

      from epyk.tests import mocks

      t = page.web.bs.tables.striped(mocks.popularity_2020)
      t.options.size("sm")
      t.set_editable_cols([1, 2])

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/

    :param records: List<dict>. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param category: String. Optional. The Bootstrap predefined category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    table = self.basic(records, cols, rows, category, width, height, html_code, options, profile)
    table.options.striped = True
    return table
