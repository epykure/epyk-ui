
from epyk.core.js import JsUtils

from epyk.core.js.packages import JsCrossFilter
from epyk.core.js.packages import JsDatatable
from epyk.core.js.packages import JsDc
from epyk.core.js.packages import JsRequire
from epyk.core.js.packages import JsTabulator


data = [
    {"name": "banana", "category": "fruit", "country": "Martinique", "outOfDateQuantity": 3, "quantity": 12},
    {"name": "apple", "category": "fruit", "country": "Spain", "outOfDateQuantity": 7, "quantity": 9},
    {"name": "tomato", "category": "vegetable", "country": "Spain", "outOfDateQuantity": 2, "quantity": 25}
  ]


# ------------------------------------------------------------------------------------------------------------------
#
f = JsUtils.JsFile("CrossFilter", path=r"../outs")
f.writeJs([
    JsCrossFilter.CrossFilter(data, 'cross1').dimension("quantity").filter([9, 13]),
    JsCrossFilter.CrossFilter(data, 'cross1').dimension("quantity").top(10),
    # JsCrossFilter.CrossFilter(data, 'cross1').dimension("category").group().reduceCount()
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
f = JsUtils.JsFile("Datatable", path=r"../outs")
f.writeJs([
    JsDatatable.DatatableAPI().draw('page').clear().cell().data(),
    JsDatatable.DatatableAPI().draw('page').state(),
    JsDatatable.DatatableAPI().columns([1, 2]).search("%test").draw().jquery_nodes(),
    JsDatatable.DatatableAPI().columns([1, 2]).search("%test").draw()
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
dcChart = JsDc.DC()
f = JsUtils.JsFile("DC", path=r"../outs")
f.writeJs([
    dcChart.width(23).height(23).toStr()
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
#repObj = JsRequire.JsRequire(False)
#print(repObj.getImports(['socket.io', 'd3', 'bootstrap', 'tabulator', 'c3', 'datatables']))


# ------------------------------------------------------------------------------------------------------------------
#
tabulator = JsTabulator.Tabulator()
f = JsUtils.JsFile("Tabulator", path=r"../outs")
f.writeJs([
    tabulator.getRow(2).select()
])
f.close()
