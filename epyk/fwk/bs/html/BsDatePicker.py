#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.js.packages import JsQuery

from epyk.fwk.bs.html.options import BsOptions


class BsDate(html.Html.Html):

  requirements = ('bootstrap-datetimepicker', 'jquery')
  name = 'Bootstrap Name'

  def __init__(self, report, value, label, icon, html_code, profile, options, helper):
    super(BsDate, self).__init__(report, value, html_code=html_code, profile=profile)
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
    Dedicated options for the Datetimepicker object.

    Usage:
    -----

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/

    :rtype: BsOptions.OptionsDt
    """
    return self.__options

  _js__builder__ = 'options.date = data; delete options.builder; $(htmlObj).datetimepicker(options)' % {
    "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s>%s%s</div>' % (
      self.get_attrs(pyClassNames=self.style.get_classes()), self.input.html(), self.span.html())
