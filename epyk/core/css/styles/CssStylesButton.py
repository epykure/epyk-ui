"""
CSS Style module for the Button components
"""


from epyk.core.css.styles import CssStylesText
from epyk.core.css.styles import CssStyle


class CssButtonBasic(CssStyle.CssCls):
  reqCssCls = [CssStylesText.CssTextBold]
  attrs = {'padding': '1px 10px', 'margin': '2px 0 2px 0', 'text-decoration': 'none', 'border-radius': '5px',
           'white-space': 'nowrap', 'display': 'inline-block'}
  hover = {'text-decoration': 'none', 'cursor': 'pointer'}
  focus = {'outline': 0}
  disabled = {'cursor': 'none'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.rptObj.theme.colors[-1], 'color': self.rptObj.theme.greys[-1],
                  'background-color': self.rptObj.theme.greys[0]})
    eventsStyles['hover'].update({'background-color': self.rptObj.theme.colors[-1], 'color': self.rptObj.theme.colors[0]})
    eventsStyles['disabled'].update({'background-color': self.rptObj.theme.colors[-1], 'color': self.rptObj.theme.colors[6], 'font-style': 'italic'})


class CssButtonReset(CssStyle.CssCls):
  reqCssCls = [CssStylesText.CssTextBold]
  attrs = {'padding': '5px 10px 5px 10px', 'margin-top': '5px', 'text-decoration': 'none', 'border-radius': '5px',
           'display': 'inline-block', 'text-transform': 'uppercase'}
  hover = {'text-decoration': 'none', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px solid %s' % self.rptObj.theme.danger[1], 'color': self.rptObj.theme.danger[1],
                  'background-color': self.rptObj.theme.greys[0]})
    eventsStyles['hover'].update({'background-color': self.rptObj.theme.danger[1], 'color': self.rptObj.theme.greys[0]})


class CssButtonSuccess(CssStyle.CssCls):
  reqCssCls = [CssStylesText.CssTextBold]
  attrs = {'padding': '10px 10px 10px 10px', 'margin': '10px 0px 10px 5px', 'text-decoration': 'none',
           'border-radius': '5px', 'display': 'inline-block', 'text-transform': 'uppercase'}
  hover = {'text-decoration': 'none', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({'color': self.rptObj.theme.colors[9], 'background-color': self.rptObj.theme.greys[0],
                  'border': '1px solid %s' % self.rptObj.theme.colors[9]})
    eventsStyles['hover'].update({'color': self.rptObj.theme.greys[0], 'background-color': self.rptObj.theme.colors[9]})
