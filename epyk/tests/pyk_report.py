from epyk.core.Page import Report
from epyk.core.py import Pyk
rptObj = Report()


button = rptObj.ui.buttons.button('Contact Sales')
imp = rptObj.ui.buttons.important('Get Started for Free')

Pyk.exports({'button': button, 'imp': imp})