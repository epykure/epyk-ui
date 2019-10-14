from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()
rptObj.ui.side_bar()

cls_name = rptObj.style.anonymous_cls({"color": "red"})
rptObj.ui.text("test").style.addCls(cls_name)

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)