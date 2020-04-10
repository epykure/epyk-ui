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

  def d_text(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    html_input = html.HtmlInput.Input(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                      options or {}, attrs or {}, profile)
    self.context.register(html_input)
    return html_input

  def d_search(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------
    One of the new types of inputs in HTML5 is search

    Usage:
    ------
    rptObj.ui.inputs.d_search("")

    Related Pages:
    --------------
    https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input/search
    https://css-tricks.com/webkit-html5-search-inputs/

    Attributes:
    ----------
    :param text:
    :param placeholder:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    """
    attrs = attrs or {}
    html_search = html.HtmlInput.Input(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                       options, attrs, profile)
    attrs.update({"type": 'search'})
    self.context.register(html_search)
    return html_search

  def password(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    attrs = attrs or {}
    attrs.update({"type": 'password'})
    return self.context.register(html.HtmlInput.Input(self.context.rptObj, text, placeholder, width, height,
                                                      htmlCode, filter, options, attrs, profile))

  def d_time(self, text="", placeholder='', width=(139, "px"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    date = rptObj.ui.dates.now(label="date")
    date.label.css({"width": "auto"})

    Attributes:
    ----------
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
    dflt_options = {'timeFormat': 'HH:mm:ss'}
    dflt_options.update(options or {})
    html_input_t = html.HtmlInput.InputTime(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                            dflt_options, attrs or {}, profile)
    self.context.register(html_input_t)
    return html_input_t

  def d_date(self, text, placeholder='', width=(140, "px"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    date = rptObj.ui.dates.now(label="date")
    date.label.css({"width": "auto"})

    Attributes:
    ----------
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
    html_date = html.HtmlInput.InputDate(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                         options, attrs or {}, profile)
    self.context.register(html_date)
    return html_date

  def d_int(self, value="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    attrs = attrs or {}
    attrs.update({"type": 'number'})
    html_integer = html.HtmlInput.InputInteger(self.context.rptObj, value, placeholder, width, height, htmlCode, filter,
                                               options, attrs, profile)
    self.context.register(html_integer)
    return html_integer

  def d_range(self, value, min=0, max=100, step=1, placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
              options=None, attrs=None, profile=None):
    attrs = attrs or {}
    attrs.update({"type": 'range'})
    html_range = html.HtmlInput.InputRange(self.context.rptObj, value, min, max, step, placeholder, width, height,
                                           htmlCode, filter, options or {}, attrs, profile)
    self.context.register(html_range)
    return html_range

  def _output(self, value="", options=None, profile=False):
    """
    Description:
    ------------
    Create a HTML output object

    Usage:
    ------
    rptObj.ui.inputs._output("test output")

    Attributes:
    ----------
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
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.inputs.textarea("Test")

    Related Pages:
    --------------
    https://www.w3schools.com/tags/tag_textarea.asp

    Attributes:
    ----------
    :param text:
    :param width:
    :param rows:
    :param background_color:
    :param htmlCode:
    :param options:
    :param profile:
    """
    dfltOptions = {"spellcheck": True, 'selectable': False}
    dfltOptions.update(options or {})
    html_t_area = html.HtmlInput.TextArea(self.context.rptObj, text, width, rows, placeholder, background_color,
                                          htmlCode, dfltOptions, profile)
    self.context.register(html_t_area)
    return html_t_area

  def autocomplete(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
                    options=None, attrs=None, profile=None):
    """
    Description:
    ------------
    Enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching and filtering.

    https://jqueryui.com/autocomplete/

    Attributes:
    ----------
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
    """
    html_input = html.HtmlInput.AutoComplete(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                             options or {}, attrs or {}, profile)
    self.context.register(html_input)
    return html_input

  def input(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    return self.d_text(text, placeholder, width, height, htmlCode, filter, options, attrs, profile)

  def hidden(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    """
    input = self.d_text(text, placeholder, width, height, htmlCode, filter, options, attrs, profile)
    input.style.css.display = None
    return input

  def checkbox(self, flag, group_name=None, width=(None, "%"), height=(None, "px"),
               htmlCode=None, filter=None, options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.inputs.checkbox(False)

    Attributes:
    ----------
    :param flag:
    :param width:
    :param height:
    :param htmlCode:
    :param filter:
    :param options:
    :param attrs:
    :param profile:
    """
    html_coech = html.HtmlInput.Checkbox(self.context.rptObj, flag, group_name, width, height, htmlCode,
                                         filter, options or {}, attrs or {}, profile)
    self.context.register(html_coech)
    return html_coech

  def radio(self, flag, label=None, group_name=None, icon=None, width=(None, "%"), height=(None, "px"),
            htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Related Pages:
    --------------
    https://www.w3schools.com/tags/att_input_type_radio.asp

    Usage:
    ------
    rptObj.ui.inputs.radio(False, label="radio")

    Attributes:
    ----------
    :param flag:
    :param label:
    :param group_name:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_radio = html.HtmlInput.Radio(self.context.rptObj, flag, label, group_name, icon, width, height, htmlCode,
                                      helper, profile)
    self.context.register(html_radio)
    return html_radio

  def editor(self, text="", title="", language='python', width=(100, "%"), height=(None, "px"), isEditable=True,
             htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param title:
    :param language:
    :param width:
    :param height:
    :param isEditable:
    :param htmlCode:
    :param options:
    :param profile:

    :rtype: html.HtmlTextEditor.Editor
    """
    return self.context.register(html.HtmlTextEditor.Editor(self.context.rptObj, text, title, language, width,
              height, isEditable, htmlCode, options, profile))

  def cell(self, text=None, width=(100, "%"), height=(None, "px"), isEditable=False,
           htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param isEditable:
    :param htmlCode:
    :param profile:
    """
    html_cell = html.HtmlTextEditor.Cell(self.context.rptObj, text, width, height, isEditable, htmlCode, options, profile)
    self.context.register(html_cell)
    return html_cell

  def search(self, text='', placeholder='Search..', color=None, height=(None, "px"), htmlCode=None,
             tooltip='', extensible=False, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.inputs.search()

    Related Pages:
    --------------
    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

    Attributes:
    ----------
    :param text:
    :param placeholder:
    :param color:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param extensible:
    :param profile:
    """
    html_s = html.HtmlInput.Search(self.context.rptObj, text, placeholder, color, height, htmlCode, tooltip,
                                   extensible, profile)
    self.context.register(html_s)
    return html_s

  def label(self, label, text="", placeholder='', width=(100, "%"), height=(None, "px"), htmlCode=None, filter=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :return:
    """
    label = self.context.rptObj.ui.texts.label(label).css({"display": 'block', 'text-align': 'left', 'margin-top': '10px',
                                                           "position": "absolute", "z-index": '20px', "font-size": '14px'})
    html_input = html.HtmlInput.Input(self.context.rptObj, text, placeholder, width, height, htmlCode, filter,
                                      options or {}, attrs or {}, profile).css({"margin-top": '10px'})
    div = self.context.rptObj.ui.div([label, html_input])
    div.input = html_input
    div.label = label
    self.context.register(html_input)
    html_input.on('focus', [
      "document.getElementById('%s').animate({'marginTop': ['10px', '-8px']}, {duration: 50, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlId,
    ])
    html_input.on('blur', [
      "document.getElementById('%s').animate({'marginTop': ['-8px', '10px']}, {duration: 1000, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlId,
    ])
    return div
