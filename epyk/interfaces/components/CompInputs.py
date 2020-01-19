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
    size = self.context._size(size)
    attrs = attrs or {}
    html_search = html.HtmlInput.Input(self.context.rptObj, text, placeholder, size, width, height, htmlCode, filter,
                                       options, attrs, profile)
    attrs.update({"type": 'search'})
    self.context.register(html_search)
    return html_search

  def password(self, text="", placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    attrs = attrs or {}
    attrs.update({"type": 'password'})
    return self.context.register(html.HtmlInput.Input(self.context.rptObj, text, placeholder, size, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_time(self, text="", placeholder='', size=(None, 'px'), width=(139, "px"), height=(None, "px"), htmlCode=None, filter=None,
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
    """
    size = self.context._size(size)
    html_input_t = html.HtmlInput.InputTime(self.context.rptObj, text, placeholder, size, width, height, htmlCode, filter,
                                            options, attrs or {}, profile)
    self.context.register(html_input_t)
    return html_input_t

  def d_date(self, text, placeholder='', size=(None, 'px'), width=(140, "px"), height=(None, "px"), htmlCode=None, filter=None,
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
    """
    size = self.context._size(size)
    html_date = html.HtmlInput.InputDate(self.context.rptObj, text, placeholder, size, width, height, htmlCode, filter,
                                         options, attrs or {}, profile)
    self.context.register(html_date)
    return html_date

  def d_int(self, value="", placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    size = self.context._size(size)
    attrs = attrs or {}
    attrs.update({"type": 'number'})
    html_integer = html.HtmlInput.InputInteger(self.context.rptObj, value, placeholder, size, width, height, htmlCode, filter,
                                               options, attrs, profile)
    self.context.register(html_integer)
    return html_integer

  def d_range(self, value, min=0, max=100, step=1, placeholder='', size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    size = self.context._size(size)
    attrs = attrs or {}
    attrs.update({"type": 'range'})
    html_range = html.HtmlInput.InputRange(self.context.rptObj, value, min, max, step, placeholder, size, width, height,
                                           htmlCode, filter, options, attrs, profile)
    self.context.register(html_range)
    return html_range

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

  def textarea(self, text="", width=(100, '%'), rows=5, placeholder=None, size=(None, 'px'), background_color=None, htmlCode=None,
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
    """
    size = self.context._size(size)
    dfltOptions = {"spellcheck": True, 'selectable': True}
    dfltOptions.update(options or {})
    html_t_area = html.HtmlInput.TextArea(self.context.rptObj, text, width, rows, placeholder, size, background_color,
                                          htmlCode, dfltOptions, profile)
    self.context.register(html_t_area)
    return html_t_area

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

  def checkbox(self, flag, label=None, group_name=None, size=(None, 'px'), width=(None, "%"), height=(None, "px"),
               htmlCode=None, filter=None, options=None, attrs=None, profile=None):
    """

    Example
    rptObj.ui.inputs.checkbox(False)

    :param flag:
    :param size:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    """
    size = self.context._size(size)
    html_coech = html.HtmlInput.Checkbox(self.context.rptObj, flag, label, group_name, size, width, height, htmlCode,
                                         filter, options or {}, attrs or {}, profile)
    self.context.register(html_coech)
    return html_coech

  def radio(self, flag, label=None, group_name=None, icon=None, size=(None, 'px'), width=(None, "%"), height=(None, "px"),
            htmlCode=None, helper=None, profile=None):
    """

    Documentation
    https://www.w3schools.com/tags/att_input_type_radio.asp

    Example
    rptObj.ui.inputs.radio(False, label="radio")

    :param flag:
    :param label:
    :param group_name:
    :param size:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    size = self.context._size(size)
    html_coech = html.HtmlInput.Radio(self.context.rptObj, flag, label, group_name, icon, size, width, height, htmlCode,
                                      helper, profile)
    self.context.register(html_coech)
    return html_coech

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

  def cell(self, text=None, size=(None, 'px'), width=(100, "%"), height=(None, "px"), isEditable=False,
           htmlCode=None, profile=None):
    """

    :param text:
    :param size:
    :param width:
    :param height:
    :param isEditable:
    :param htmlCode:
    :param profile:
    """
    size = self.context._size(size)
    html_cell = html.HtmlTextEditor.Cell(self.context.rptObj, text, size, width, height,
                                         isEditable, htmlCode, profile)
    self.context.register(html_cell)
    return html_cell

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
    """
    size = self.context._size(size)
    html_s = html.HtmlInput.Search(self.context.rptObj, text, placeholder, color, size, height, htmlCode, tooltip,
                                   extensible, profile)
    self.context.register(html_s)
    return html_s
