"""
CSS Style module for the Chart components
"""


from epyk.core.css.styles import CssStyle


class CssDivChart(CssStyle.CssCls):
  """
  CSS class for the Chart container
  """
  attrs = {'margin': '0 0 5px 0', 'outline': 'none'}

  def customize(self, style, eventsStyles):
    style.update({'border': "1px solid %s" % self.rptObj.theme.greys[3]})
    eventsStyles['hover'].update({'border': "1px solid %s" % self.rptObj.theme.colors[1]})


# --------------------------------------------------------------------------------------------------------------
#
#                                   BILLBOARD SECTION
# --------------------------------------------------------------------------------------------------------------
class CssBillboardTitle(CssStyle.CssCls):
  cssId = {'child': ".bb-title"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssBillboardLegend(CssStyle.CssCls):
  cssId = {'child': ".bb text"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssBillboardAxis(CssStyle.CssCls):
  cssId = {'child': ".bb-axis line, .bb-axis-x line, .bb-axis .domain, .bb-axis-x .domain"}

  def customize(self, style, eventsStyles):
    style.update({'stroke': self.rptObj.theme.greys[-1]})


class CssBillboardXAxis(CssStyle.CssCls):
  cssId = {'child': ".bb-axis-x text"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssBillboardYAxis(CssStyle.CssCls):
  cssId = {'child': ".bb-axis-y text"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})



# --------------------------------------------------------------------------------------------------------------
#
#                                   C3 SECTION
# --------------------------------------------------------------------------------------------------------------
class CssC3Title(CssStyle.CssCls):
  cssId = {'child': ".c3-title"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssC3Legend(CssStyle.CssCls):
  cssId = {'child': '.c3 text'}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssC3Axis(CssStyle.CssCls):
  cssId = {'child': '.c3-axis line, .c3-axis .domain'}

  def customize(self, style, eventsStyles):
    style.update({'stroke': self.rptObj.theme.greys[-1]})


class CssC3XAxis(CssStyle.CssCls):
  cssId = {'child': ".c3-axis-x text"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


class CssC3YAxis(CssStyle.CssCls):
  cssId = {'child': ".c3-axis-y text"}

  def customize(self, style, eventsStyles):
    style.update({'fill': "%s !IMPORTANT" % self.rptObj.theme.greys[-1]})


# --------------------------------------------------------------------------------------------------------------
#
#                                   NVD3 SECTION
# --------------------------------------------------------------------------------------------------------------
class CssNVD3Axis(CssStyle.CssCls):
  cssId = {'child': '.nvd3 .nv-axis g path.domain'}

  def customize(self, style, eventsStyles):
    style.update({'stroke': self.rptObj.theme.greys[-1], 'stroke-opacity': 1})


class CssNVD3AxisLabel(CssStyle.CssCls):
  cssId = {'child': '.nvd3 .nv-axis'}

  def customize(self, style, eventsStyles):
    style.update({'fill': self.rptObj.theme.greys[-1]})


class CssNVD3AxisLegend(CssStyle.CssCls):
  cssId = {'child': 'svg text'}

  def customize(self, style, eventsStyles):
    style.update({'fill': self.rptObj.theme.greys[-1]})


class CssNVD3HideGrid(CssStyle.CssCls):
  cssId = {'child': '.nvd3 .tick line'}

  def customize(self, style, eventsStyles):
    style.update({'display': 'none'})


# Bootstrap issue
# https://stackoverflow.com/questions/18894820/jquery-sparklines-and-twitter-bootstrap-3-tooltip-style-overrides
class CssSparklines(CssStyle.CssCls):
  cssId = {'reference': '.jqstooltip'}
  attrs = {"ebkit-box-sizing": "content-box", "-moz-box-sizing": "content-box", "box-sizing": "content-box"}

