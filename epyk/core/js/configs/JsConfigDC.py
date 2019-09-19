"""

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the DC Charts
  """
  listAttributes = []
  jsCls = None


# ---------------------------------------------------------------------------------------------------------
#                                          C3 Configurations
# ---------------------------------------------------------------------------------------------------------
class JsBar(JsBase):
  """
  Configuration for a Bars Chart in DC
  """
  alias = 'bar'
  name = 'Bars'
  jsCls = 'barChart'
  _attrs = {}


class JsPie(JsBase):
  """
  Configuration for a Bars Chart in DC
  """
  alias = 'pie'
  name = 'Pie Chart'
  jsCls = 'pieChart'
  _attrs = {}
