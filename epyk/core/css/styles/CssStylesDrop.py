"""
CSS Style module for the Files Drop components
"""


from epyk.core.css.styles import CssStyle


class CssDropFile(CssStyle.CssCls):
  attrs = {'text-align': 'center', 'padding': '5px', 'margin': '5px 0 10px 0'}

  def customize(self, style, eventsStyles):
    style.update({'border': '1px dashed %s' % self.getColor('colors', 1), 'color': self.getColor('colors', 1)})
