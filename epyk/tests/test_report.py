"""

"""

from epyk.core.Page import Report


rptObj = Report()
# rptObj.theme = 'grey'
# f = rptObj.ui.forms.inputs([
#   {"label": "name", "htmlCode": "input"},
#   {"label": "name 2", "htmlCode": "input2"},
# ], "http://127.0.0.1:5000", "POST")
# f + rptObj.ui.fields.today('test')
# print(rptObj.tags.bdi("test"))
# print(rptObj.entities.POUND)
# print(rptObj.symbols.ALMOST_EQUAL_TO)
# rptObj.ui.d
d = rptObj.ui.fields.today('test')
i = rptObj.ui.fields.input(placeholder='test2', label='test1')
i.input.set_attrs(name='required')
i.input.set_attrs({'name': 'input1'})
i2 = rptObj.ui.fields.input('test3', label='test2')
# f + rptObj.ui.fields.today('test')
rptObj.ui.modal.forms([d, i, i2], "http://127.0.0.1:5000", "POST")
rptObj.outs.html_file(name='test')
