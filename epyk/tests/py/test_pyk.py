from epyk.core.py import Pyk
from epyk.core.Page import Report


rpt_obj = Report()
list_filter_object = Pyk.requires(r'C:\Users\nelso\Downloads\list_filter.py')
Pyk.register(rpt_obj, [list_filter_object.list1, list_filter_object.search])
print(rpt_obj.outs.html_file())
