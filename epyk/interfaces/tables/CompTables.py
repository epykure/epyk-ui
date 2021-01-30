
from epyk.core.html import tables as html_tables

from epyk.interfaces.tables import CompTabulator
from epyk.interfaces.tables import CompDatatable
from epyk.interfaces.tables import CompTablesPlotly
from epyk.interfaces.tables import CompTableD3
from epyk.interfaces.tables import CompAgGrid
from epyk.interfaces.tables import CompPivot
from epyk.interfaces.tables import CompTableGoogle


class Tables(object):
  def __init__(self, context):
    self.context = context
    # Default table configuration per available framework
    self.datatable = self.datatables.table
    self.tabulator = self.tabulators.table
    self.plotly = self.plotlys.table
    self.aggrid = self.aggrids.table
    self.pivot = self.pivots.pivot

  @property
  def aggrids(self):
    """
    Description:
    -----------
    ag-Grid is the industry standard for JavaScript Enterprise Applications.
    Developers using ag-Grid are building applications that would not be possible if ag-Grid did not exist.

    Usage:
    -----

    Related Pages:

      https://www.ag-grid.com/javascript-grid/
    """
    return CompAgGrid.AgGrid(self)

  @property
  def tabulators(self):
    """
    Description:
    -----------
    Interface to the different Tabulator configurations.

    Usage:
    -----

    Related Pages:

      http://tabulator.info/
    """
    return CompTabulator.Tabulators(self)

  @property
  def google(self):
    """
    Description:
    -----------
    """
    if not getattr(self.context.rptObj, '_with_google_imports', False):
      raise Exception("Google produce must be added using for example rptObj.imports().google_products(['charts'])")

    return CompTableGoogle.Google(self)

  @property
  def pivots(self):
    """
    Description:
    -----------
    Interface to the different Pivot Table configurations.

    Related Pages:

      https://pivottable.js.org/examples/
    """
    return CompPivot.Pivottable(self)

  @property
  def d3(self):
    """
    Description:
    -----------
    Interface to the different Tabulator configurations.

    Related Pages:

      https://github.com/d3/d3/wiki/Gallery

    :rtype: CompTableD3.D3
    """
    return CompTableD3.D3(self)

  @property
  def plotlys(self):
    """
    Interface to the different Tabulator configurations.

    Related Pages:

      http://tabulator.info/

    :rtype: CompTabulator.Tabulators
    """
    return CompTablesPlotly.Plotly(self)

  @property
  def datatables(self):
    """
    Description:
    -----------
    Interface to the different Datatable configurations.

    Related Pages:

      https://datatables.net/

    :rtype: CompDatatable.Datatables
    """
    return CompDatatable.Datatables(self)

  def config(self, htmlCode, visible=False, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param htmlCode:
    :param visible:
    :param profile:
    """
    return html_tables.HtmlTableConfig.ConfigTable(self.context.rptObj, htmlCode, visible, profile)

  def basic(self, records, cols, rows, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Usage::

      simple_table = page.ui.tables.basic(df.to_dict("records"), cols=["COL1"], rows=["COL2"])
      simple_table.add({"COL1": "Value"})

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    table = html_tables.HtmlTable.Bespoke(self.context.rptObj, records, cols, rows, width, height, htmlCode, options, profile)
    return table

  def grid(self, records, cols, rows, width=(None, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    Usage::

      """
    width_cells, width_rows_header = 50, 100
    for rec in records:
      for c in cols:
        if c not in rec:
          rec[c] = 0
    table = html_tables.HtmlTable.Bespoke(self.context.rptObj, records, cols, rows, width, height, htmlCode, options, profile)
    table.css({"width": "%spx" % (width_rows_header + len(cols) * width_cells)})
    # table[0][0]._vals = ""
    for i in table[1:]:
      for j in range(len(rows)):
        i[j].attr["name"] = "row_header"
        i[j].css({"width": "%spx" % width_rows_header})
      for cell in i[j:]:
        cell.attr["contenteditable"] = 'true'
        cell.css({"width": '%spx' % width_cells})
    table.style.clear()
    # Set the style for the table grid
    # table.style.add_classes.table.grid_row_header()
    table.style.add_classes.table.grid_vals()
    # table.style.add_classes.table.grid_no_header()
    return table
