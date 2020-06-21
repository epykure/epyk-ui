from epyk.core.Page import Report
from epyk.core.py import Pyk
rptObj = Report()


button = rptObj.ui.buttons.button('This is button')
imp = rptObj.ui.buttons.important('This is an important button')

Pyk.exports({'button': button, 'imp': imp})