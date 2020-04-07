
from epyk.core import html

from epyk.core.html import Defaults as defaults_html
from epyk.core.css import Defaults as defaults_css


class Code(object):

  def __init__(self, context):
    self.context = context

  def python(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    if not isinstance(text, list):
      text = [text]
    dflt_options = {"lineNumbers": True, 'mode': 'python', 'matchBrackets': True, 'styleActiveLine': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def javascript(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    if not isinstance(text, list):
      text = [text]
    dflt_options = {"lineNumbers": True, 'true': 'javascript'}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code
