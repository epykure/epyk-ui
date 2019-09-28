"""
Wrapper to the predefined Forms

Documentation
https://www.w3schools.com/html/html_forms.asp
"""

from epyk.core.html import Html


class Form(Html.Html):
  name, category, callFnc = 'Generic Form', 'Forms', 'form'
  __pyStyle = ['CssDivNoBorder']

  def __init__(self, report, action, method, helper):
    super(Form, self).__init__(report)
    self.attr["action"] = action
    self.attr["method"] = method
    self.add_helper(helper)

  def __str__(self):
    return '<form %s>%s</form>' % (self.strAttr(pyClassNames=self.pyStyle), self.helper)
