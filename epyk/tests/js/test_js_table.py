


aggFnss = getAggFnc()
print( aggFnss['sum Over Sum Agg'].toJs({'digits': 0}))


cols = TableCols()
cols.add([1, 2], 'div', attr={'dsc': "dfgfd"})
cols.add([1, 2], 'container_class', attr={'class': "dfgfd"})
cols.add(1, 'age', attr={'steps': 100, 'start': 'white', 'end': 'pink', 'columnOrders': []})
#cols.add(2, TableRowStyle, attr={'class': "gdfgdf"})
#cols.add(2, TableRowStyle, attr={'class': "youpi"})
#cols.add(1, TableRowStyleCss, attr={'css': {'color': 'yellow'}})