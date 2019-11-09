"""

"""

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core import html


class Inputs(object):
  def __init__(self, context):
    self.context = context

  def d_text(self, text="", placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """

    :param text:
    :param placeholder:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    """
    size = self.context._size(size)
    html_input = html.HtmlInput.Input(self.context.rptObj, text, placeholder, size, width, height, htmlCode, filter,
                                      options or {}, attrs or {}, profile)
    self.context.register(html_input)
    return html_input

  def d_search(self, text="", placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    One of the new types of inputs in HTML5 is search

    Example
    rptObj.ui.inputs.d_search("")

    Documentation
    https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input/search
    https://css-tricks.com/webkit-html5-search-inputs/

    :param text:
    :param placeholder:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:

    :rtype: html.HtmlInput.Input

    :return:
    """
    if attrs is None:
      attrs = {}
    html_search = html.HtmlInput.Input(self.context.rptObj, text, placeholder, size, width, height, htmlCode, filter,
                                       options, attrs, profile)
    attrs.update({"type": 'search'})
    self.context.register(html_search)
    return html_search

  def password(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    if attrs is None:
      attrs = {}
    attrs.update({"type": 'password'})
    return self.context.register(html.HtmlInput.Input(self.context.rptObj, text, placeholder, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_time(self, text="", placeholder='', width=(139, "px"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """

    Examples
    date = rptObj.ui.dates.now(label="date")
    date.label.css({"width": "auto"})

    :param text:
    :param placeholder:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    :return:
    """
    if attrs is None:
      attrs = {}
    return self.context.register(html.HtmlInput.InputTime(self.context.rptObj, text, placeholder, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_date(self, text, placeholder='', width=(140, "px"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """

    Examples
    date = rptObj.ui.dates.now(label="date")
    date.label.css({"width": "auto"})

    :param text:
    :param placeholder:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    :return:
    """
    if attrs is None:
      attrs = {}
    return self.context.register(html.HtmlInput.InputDate(self.context.rptObj, text, placeholder, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_int(self, value="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    if attrs is None:
      attrs = {}
    attrs.update({"type": 'number'})
    return self.context.register(html.HtmlInput.InputInteger(self.context.rptObj, value, placeholder, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_range(self, value, min=0, max=100, step=1, placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    if attrs is None:
      attrs = {}
    attrs.update({"type": 'range'})
    return self.context.register(html.HtmlInput.InputRange(self.context.rptObj, value, min, max, step, placeholder, width,
                                                           height, htmlCode, filter, options, attrs, profile))

  def _output(self, value="", options=None, profile=False):
    """
    Create a HTML output object

    Example
    rptObj.ui.inputs._output("test output")

    :param value:
    :param options:
    :param profile:
    """
    html_output = html.HtmlInput.Output(self.context.rptObj, value)
    self.context.register(html_output)
    return html_output

  def textarea(self, text="", width=(100, '%'), rows=5, placeholder=None, background_color=None, htmlCode=None,
               options=None, profile=None):
    """

    Example
    rptObj.ui.inputs.textarea("Test")

    Documentation
    https://www.w3schools.com/tags/tag_textarea.asp

    :param text:
    :param width:
    :param rows:
    :param background_color:
    :param htmlCode:
    :param options:
    :param profile:

    :rtype: html.HtmlInput.TextArea
    :return:
    """
    if options is None:
      options = {}
    dfltOptions = {"spellcheck": True, 'selectable': True}
    dfltOptions.update(options)
    return self.context.register(html.HtmlInput.TextArea(self.context.rptObj, text, width, rows, placeholder, background_color,
                                                         htmlCode, dfltOptions, profile))

  def input(self, text="", placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """

    :param text:
    :param placeholder:
    :param size:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:

    :rtype: html.HtmlInput.Input
    :return:
    """
    return self.d_text(text, placeholder, size, width, height, htmlCode, filter, options, attrs, profile)

  def editor(self, text="", title="", size=(None, 'px'), language='python', width=(100, "%"), height=(None, "px"), isEditable=True,
             htmlCode=None, options=None, profile=None):
    """

    :param text:
    :param title:
    :param size:
    :param language:
    :param width:
    :param height:
    :param isEditable:
    :param htmlCode:
    :param options:
    :param profile:
    :rtype: html.HtmlTextEditor.Editor
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextEditor.Editor(self.context.rptObj, text, title, size, language, width,
              height, isEditable, htmlCode, options, profile))

  def console(self, text=None, size=(None, 'px'), width=(100, "%"), height=(None, "px"), isEditable=False,
              htmlCode=None, profile=None):
    """

    :param text:
    :param size:
    :param width:
    :param height:
    :param isEditable:
    :param htmlCode:
    :param profile:
    :rtype: html.HtmlTextEditor.Console
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextEditor.Console(self.context.rptObj, text, size, width, height,
               isEditable, htmlCode, profile))

  def search(self, text='', placeholder='Search..', color=None, size=(None, 'px'), height=(None, "px"), htmlCode=None,
             tooltip='', extensible=False, profile=None):
    """

    Example
    rptObj.ui.inputs.search()

    Documentation
    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

    :param text:
    :param placeholder:
    :param color:
    :param size:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param extensible:
    :param profile:
    :rtype: html.HtmlInput.Search
    :return:
    """
    size = self.context._size(size)
    return self.context.register(
      html.HtmlInput.Search(self.context.rptObj, text, placeholder, color, size, height, htmlCode, tooltip, extensible,
                            profile))
