#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.js.packages import JsQuery

from epyk.fwk.bs.html.options import BsOptions


class BsDate(html.Html.Html):
  __reqCss, __reqJs = ['bootstrap-datetimepicker'], ['bootstrap-datetimepicker']
  name = 'Bootstrap Name'

  def __init__(self, report, value, label, icon, htmlCode, profile, options, helper):
    super(BsDate, self).__init__(report, value, htmlCode=htmlCode, profile=profile)
    self.style.clear_all()
    self.__options = BsOptions.OptionsDt(self, options)
    self.attr['class'].add("input-group date")

    self.input = self._report.web.std.inputs.d_text(self.val)
    self.input.style.clear_all()
    self.input.attr['class'].add("form-control")
    self.input.options.managed = False

    self.span = self._report.web.std.div()
    self.span.style.clear_all()
    self.span.attr['class'].add("input-group-addon")
    self.span.options.managed = False

    icon = self._report.web.std.texts.span('Text')
    icon.style.clear_all()
    icon.options.managed = False

    self.span += icon

  @property
  def options(self):
    """
    Description:
    -----------
    Dedicated options for the Datetimepicker object

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/

    :rtype: BsOptions.OptionsDt
    """
    return self.__options

  @property
  def _js__builder__(self):
    return 'options.date = data; $(htmlObj).datetimepicker(options)' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.input.html(), self.span.html())
