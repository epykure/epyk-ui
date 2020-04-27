
from epyk.core import html


class Drawers(object):

  def __init__(self, context):
    self.context = context

  def drawer(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    html_col = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    self.context.register(html_col)
    return html_col

  def left(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    options = options or {}
    options["side"] = 'right'
    html_col = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    self.context.register(html_col)
    return html_col

  def right(self, width=(100, '%'), height=(200, 'px'), options=None, profile=None, helper=None):
    options = options or {}
    options["side"] = 'right'
    html_col = html.HtmlDrawer.Drawer(self.context.rptObj, width, height, options, helper, profile)
    self.context.register(html_col)
    return html_col


