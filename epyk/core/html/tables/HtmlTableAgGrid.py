
from epyk.core.html import Html

from epyk.core.data import DataClass
from epyk.core.data import DataEnum
from epyk.core.data import DataGroup
from epyk.core.data import DataEnumMulti

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  name, category, callFnc = 'Table', 'Tables', 'table'
  __reqJs = ['ag-grid']

  def __init__(self, report, records, width, height, htmlCode, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    if records is not None:
      self.config.data = records

  @property
  def config(self):
    if self.__config is None:
      self.__config = TableConfig(self._report)
    return self.__config

  def add_column(self, field, title=None):
    """

    :param field:
    :param title:
    """
    col_def = self.config.columns
    col_def.field = field
    col_def.headerName = field if title is None else title
    col_def.filter = True
    return col_def

  @property
  def tableId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  def build(self, data=None, options=None, profile=False):
    return 'var %s =  new agGrid.Grid(%s, %s)' % (self.tableId, self.dom.varName, self.config)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class Column(DataClass):

  @property
  def headerName(self):
    """
    """
    return self._attrs["headerName"]

  @headerName.setter
  def headerName(self, val):
    self._attrs["headerName"] = val

  @property
  def field(self):
    """
    """
    return self._attrs["field"]

  @field.setter
  def field(self, val):
    self._attrs["field"] = val

  @property
  def sortable(self):
    """
    """
    return self._attrs["sortable"]

  @sortable.setter
  def sortable(self, val):
    self._attrs["sortable"] = val

  @property
  def filter(self):
    """
    """
    return self._attrs["filter"]

  @filter.setter
  def filter(self, val):
    self._attrs["filter"] = val

  @property
  def checkboxSelection(self):
    """
    """
    return self._attrs["checkboxSelection"]

  @checkboxSelection.setter
  def checkboxSelection(self, val):
    self._attrs["checkboxSelection"] = val

  @property
  def suppressMovable(self):
    """
    The column property suppressMovable changes whether the column can be dragged.

    https://www.ag-grid.com/javascript-grid-column-moving/
    """
    return self._attrs["suppressMovable"]

  @suppressMovable.setter
  def suppressMovable(self, val):
    self._attrs["suppressMovable"] = val

  @property
  def pinned(self):
    """
    """
    return self._attrs["pinned"]

  @pinned.setter
  def pinned(self, val):
    self._attrs["pinned"] = val

  @property
  def lockPosition(self):
    """
    The column property lockPosition locks columns to the first position in the grid.

    https://www.ag-grid.com/javascript-grid-column-moving/

    """
    return self._attrs["lockPosition"]

  @lockPosition.setter
  def lockPosition(self, val):
    self._attrs["cellClass"] = 'locked-col'
    self._attrs["lockPosition"] = val

  @property
  def rowGroup(self):
    """
    """
    return self._attrs["rowGroup"]

  @rowGroup.setter
  def rowGroup(self, val):
    self._attrs["rowGroup"] = val


class TableConfig(DataClass):

  @property
  def columns(self):
    """
    """
    return self.sub_data_enum("columnDefs ", Column)

  @property
  def data(self):
    """
    """
    return self._attrs["rowData "]

  @data.setter
  def data(self, val):
    self._attrs["rowData "] = val
