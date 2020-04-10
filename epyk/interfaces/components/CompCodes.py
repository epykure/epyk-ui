
from epyk.core import html


class Code(object):

  def __init__(self, context):
    self.context = context

  def css(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def xml(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'mode': 'xml', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def sql(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'mode': 'sql', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def r(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'mode': 'r', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def python(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'mode': 'python', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code

  def javascript(self, text="", color=None, width=(90, '%'), height=(None, 'px'), htmlCode=None, options=None, helper=None, profile=None):
    """
    """
    dflt_options = {"lineNumbers": True, 'true': 'javascript', 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_code = html.HtmlTextEditor.Code(self.context.rptObj, text, color, width, height, htmlCode, dflt_options, helper, profile)
    self.context.register(html_code)
    return html_code
