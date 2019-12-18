"""
Wrapper to the predefined Forms

Documentation
https://www.w3schools.com/html/html_forms.asp
"""

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class Form(Html.Html):
  name, category, callFnc = 'Generic Form', 'Forms', 'form'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, htmlObjs, action, method, helper):
    super(Form, self).__init__(report, [])
    self.css({"padding": '5px'})
    self.attr.update({"action": action, "method": method})
    self.add_helper(helper)
    for i, htmlObj in enumerate(htmlObjs):
      self.__add__(htmlObj)

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.val.append(htmlObj)
    return self

  def __str__(self):
    s = self._report.ui.button("Submit").set_attrs({"type": 'submit'})
    self.__add__(s)
    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    return '<form %s>%s</form>%s' % (self.get_attrs(pyClassNames=self.defined), str_vals, self.helper)
