#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.packages import JsQuery
from epyk.core.html.options import OptJqvM


class JqueryVectorMap(Html.Html):
  name = 'Jquery Vector Map'
  requirements = ('jqvmap', )

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(JqueryVectorMap, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptJqvM.OptionsJqVM(self, options)
    self.chartId = "%s_obj" % self.htmlCode

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptJqvM.OptionsJqVM
    """
    return self.__options

  _js__builder__ = '''%s.vectorMap(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
