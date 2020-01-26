"""
CSS Style module for the Pivot components
"""


from epyk.core.css.styles import CssStyle


class CssPivotHead(CssStyle.CssCls):
  attrs = {'font-size': '8pt', 'padding': '5px'}
  cssId = {'reference': '.pvtTable tr th'}

  def customize(self, style, eventsStyles):
    style.update({
      'color': self.rptObj.theme.greys[-1],
      'background-color': self.rptObj.theme.colors[0],
      'border': '1px solid %s' % self.rptObj.theme.colors[3]})


class CssPivotCells(CssStyle.CssCls):
  attrs = {'font-size': '8pt', 'padding': '5px'}
  cssId = {'reference': '.pvtTable tr td'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.greys[0],
                  'border': '1px solid %s' % self.rptObj.theme.colors[3]})
    eventsStyles['hover'].update({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[2]})


class CssPivotAxis(CssStyle.CssCls):
  attrs = {'background': 'red'}
  cssId = {'reference': '.pvtAxisContainer li span.pvtAttr'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.greys[-1], 'background-color': self.rptObj.theme.colors[1],
                  'border': '1px solid %s' % self.rptObj.theme.colors[1]})


class CssPivotFilterBox(CssStyle.CssCls):
  cssId = {'reference': '.pvtAxisContainer'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.greys[1], 'background-color': self.rptObj.theme.colors[3],
                  'border': '1px solid %s' % self.rptObj.theme.colors[1]})


class CssPivotFilterVals(CssStyle.CssCls):
  cssId = {'reference': '.pvtVals'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.greys[1], 'background-color': self.rptObj.theme.colors[3],
                  'border': '1px solid %s' % self.rptObj.theme.colors[1]})


class CssPivotFilterBoxPopUp(CssStyle.CssCls):
  cssId = {'reference': '.pvtFilterBox'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.greys[1], 'background-color': self.rptObj.theme.colors[2],
                  'border': '1px solid %s' % self.rptObj.theme.colors[1]})
