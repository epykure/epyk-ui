
from epyk.core.html.Html import Component
from epyk.core.js.packages import JsQuery
from epyk.fwk.bs.options import OptBsDT
from epyk.fwk.bs.dom import DomBsDatePicker


class BsDatePicker(Component):
  #requirements = ('tempusdominus-bootstrap-4', )
  requirements = ('tempus-dominus', )
  css_classes = ["input-group", "date"]
  name = "Bootstrap DatePicker"
  _option_cls = OptBsDT.DT

  str_repr = '''
<div class="form-group">
    <div {attrs} data-target-input="nearest">
        <input type="text" class="form-control datetimepicker-input" data-target="#{htmlCode}"/>
        <div class="input-group-append" data-target="#{htmlCode}" data-toggle="datetimepicker">
            <div class="input-group-text" style="height:100%"><i class="fa fa-calendar"></i></div>
        </div>
    </div>
</div>'''

  #_js__builder__ = '''%(jqId)s.datetimepicker(options)''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}
  _js__builder__ = '''console.log(htmlObj); new tempusDominus.TempusDominus(htmlObj, {dateRange: true})'''

  @property
  def options(self) -> OptBsDT.DT:
    """ The component options. """
    return super().options

  @property
  def dom(self) -> DomBsDatePicker.DomDate:
    """ The common DOM properties. """
    if self._dom is None:
      self._dom = DomBsDatePicker.DomDate(component=self, page=self.page)
    return self._dom
