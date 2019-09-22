"""
CSS Style module for the Icons components
"""


from epyk.core.css.styles import CssStyle


class CssIcon(CssStyle.CssCls):
  attrs = {'margin': '4px 10px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"color": self.getColor('colors', 5)})


class CssStdIcon(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'font-size': '20px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('colors', 5)})
    eventsStyles['hover'].update({"color": self.getColor('colors', 5)})


class CssSmallIcon(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 15px 0 0', 'font-size': '10px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"color": self.getColor('colors', 5)})


class CssSmallIconRigth(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 0 0 15px', 'font-size': '10px', 'cursor': 'pointer', 'float': 'right'}

  def customize(self, style, eventsStyles):
    eventsStyles['hover'].update({"color": self.getColor('colors', 5)})


class CssSmallIconRed(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 15px 0 0', 'font-size': '10px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('danger', 1)})
    eventsStyles['hover'].update({"color": self.getColor('danger', 1)})


class CssOutIcon(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 0 0 20px', 'font-size': '15px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update( {"color": self.getColor('danger', 1)})
    eventsStyles['hover'].update({"color": self.getColor('danger', 1)})


class CssBigIcon(CssStyle.CssCls):
  attrs = {'display': 'inline-block', 'margin': '0 10px 0 10px', 'cursor': 'pointer'}

  def customize(self, style, eventsStyles):
    style.update({"color": self.getColor('danger', 1), 'font-size': self.fontSize})
    eventsStyles['hover'].update({"color": self.getColor('danger', 1)})
