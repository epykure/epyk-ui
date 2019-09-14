

# Crossfilter

data = [
    {"name": "banana", "category": "fruit", "country": "Martinique", "outOfDateQuantity": 3, "quantity": 12},
    {"name": "apple", "category": "fruit", "country": "Spain", "outOfDateQuantity": 7, "quantity": 9},
    {"name": "tomato", "category": "vegetable", "country": "Spain", "outOfDateQuantity": 2, "quantity": 25}
  ]

js = [
CrossFilter(data, 'cross1').dimension("quantity").filter([9, 13]),
CrossFilter(data, 'cross1').dimension("quantity").top(10)
]

for j in js:
print(j.toStr())


#cross = CrossFilter(data, 'cross1').dimension("category").group()
#rData = cross.reduceCount()
#rDataAll = cross.all()

#print(rData.toStr())
#print(rDataAll.toStr())

#

datatable = DatatableAPI().draw('page').clear().cell().data()
  print(datatable.toStr())

  datatable = DatatableAPI().draw('page').state()
  print(datatable.toStr())

  print(DatatableAPI().columns([1, 2]).search("%test").draw().jquery_nodes().toStr())

  colTable = DatatableAPI().columns([1, 2]).search("%test").draw()
  print(colTable.toStr())


dcChart = DC()
  print(dcChart.width(23).height(23).toStr())



repObj = JsRequire(False)
  print(repObj.getImports(['socket.io', 'd3', 'bootstrap', 'tabulator', 'c3', 'datatables']))

tabulator = Tabulator()
print(tabulator.getRow(2).select().toStr())