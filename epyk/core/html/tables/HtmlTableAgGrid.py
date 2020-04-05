
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

  @property
  def tableId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  def build(self, data=None, options=None, profile=False):
    return 'var %s =  agGrid.Grid("#%s", %s)' % (self.tableId, self.htmlId, self.config)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))

