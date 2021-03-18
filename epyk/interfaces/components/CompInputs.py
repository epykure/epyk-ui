#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.html import Defaults
from epyk.interfaces import Arguments


class Inputs:
  
  def __init__(self, ui):
    self.page = ui.page

  def d_text(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None,
             options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.d_text()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    options = options or {}
    attrs = attrs or {}
    html_input = html.HtmlInput.Input(
      self.page, text, placeholder, width, height, html_code, options, attrs, profile)
    html_input.style.css.margin_bottom = '2px'
    return html_input

  def d_radio(self, flag=False, group_name=None, placeholder='', width=(100, "%"), height=(None, "px"), html_code=None,
              options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.d_radio()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.InputRadio`

    Attributes:
    ----------
    :param flag:
    :param group_name:
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    attrs = attrs or {}
    html_input = html.HtmlInput.InputRadio(self.page, flag, group_name, placeholder, width, height, html_code,
                                           options, attrs, profile)
    return html_input

  def d_search(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
               attrs=None, profile=None):
    """
    Description:
    ------------
    One of the new types of inputs in HTML5 is search

    Usage:
    -----

      page.ui.inputs.d_search("")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input/search
      https://css-tricks.com/webkit-html5-search-inputs/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    attrs = attrs or {}
    html_search = html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code,
                                       options, attrs, profile)
    attrs.update({"type": 'search'})
    return html_search

  @html.Html.css_skin()
  def password(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
               attrs=None, profile=None):
    """
    Description:
    ------------
    Input field that will hide characters typed in.

    Usage:
    -----

      page.ui.inputs.password(placeholder="Password")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    attrs = attrs or {}
    attrs.update({"type": 'password'})
    return html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code, options, attrs,
                                profile)

  def file(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
           attrs=None, profile=None):
    """
    Input file object.

    Description:
    ------------
    Input field that will hide characters typed in

    Usage:
    -----

      page.ui.inputs.file()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.File`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    attrs = attrs or {}
    attrs.update({"type": 'file'})
    return html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code, options, attrs,
                                profile)

  def d_time(self, text="", placeholder='', width=(139, "px"), height=(None, "px"), html_code=None, options=None,
             attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      date = page.ui.inputs.d_time()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.InputTime`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {'timeFormat': 'HH:mm:ss'}
    dflt_options.update(options or {})
    html_input_t = html.HtmlInput.InputTime(self.page, text, placeholder, width, height, html_code,
                                            dflt_options, attrs or {}, profile)
    return html_input_t

  def d_date(self, text, placeholder='', width=(140, "px"), height=(None, "px"), html_code=None, options=None,
             attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      date = page.ui.inputs.d_date()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.InputDate`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_date = html.HtmlInput.InputDate(self.page, text, placeholder, width, height, html_code, options,
                                         attrs or {}, profile)
    return html_date

  def d_int(self, value="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
            attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      date = page.ui.inputs.d_int()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.InputInteger`

    Attributes:
    ----------
    :param value: Integer. Optional. The value of this input number field.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    attrs = attrs or {}
    attrs.update({"type": 'number'})
    html_integer = html.HtmlInput.InputInteger(self.page, value, placeholder, width, height, html_code,
                                               options, attrs, profile)
    return html_integer

  def d_range(self, value, min_val=0, max_val=100, step=1, placeholder='', width=(100, "%"), height=(None, "px"),
              html_code=None, options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param value: Number. Optional. The value of the component.
    :param min_val: Number. Optional. The minimum value.
    :param max_val: Number. Optional. The maximum value.
    :param step: Integer. Optional. The step when the handle is moved.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    attrs = attrs or {}
    attrs.update({"type": 'range'})
    html_range = html.HtmlInput.InputRange(self.page, value, min_val, max_val, step, placeholder, width, height,
                                           html_code, options or {}, attrs, profile)
    return html_range

  def _output(self, value="", options=None, profile=False):
    """
    Description:
    ------------
    Create a HTML output object.

    Usage:
    -----

      page.ui.inputs._output("test output")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Output`

    Attributes:
    ----------
    :param value:
    :param options:
    :param profile:
    """
    html_output = html.HtmlInput.Output(self.page, value, options=options, profile=profile)
    return html_output

  @html.Html.css_skin()
  def textarea(self, text="", width=(100, '%'), rows=5, placeholder=None, background_color=None, html_code=None,
               options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.textarea("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.TextArea`

    Related Pages:

      https://www.w3schools.com/tags/tag_textarea.asp

    Attributes:
    ----------
    :param text:
    :param width:
    :param rows:
    :param placeholder:
    :param background_color:
    :param html_code:
    :param options:
    :param profile:
    """
    dflt_options = {"spellcheck": False, 'selectable': False}
    dflt_options.update(options or {})
    html_t_area = html.HtmlInput.TextArea(self.page, text, width, rows, placeholder, background_color,
                                          html_code, dflt_options, profile)
    return html_t_area

  @html.Html.css_skin()
  def autocomplete(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
                   attrs=None, profile=None):
    """
    Description:
    ------------
    Enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching
    and filtering.

    Usage:
    -----

      page.ui.inputs.autocomplete("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.AutoComplete`


    Related Pages:

      https://jqueryui.com/autocomplete/


    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    attrs = attrs or {}
    html_input = html.HtmlInput.AutoComplete(self.page, text, placeholder, width, height, html_code, options,
                                             attrs, profile)
    html_input.style.css.text_align = "left"
    html_input.style.css.padding_left = 5
    # Take into account the padding left in the width size.
    # TODO: Think about a more flexible way to do this.
    #html_input.style.css.width = Defaults.INPUTS_MIN_WIDTH - 5
    return html_input

  @html.Html.css_skin()
  def input(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
            attrs=None, profile=None):
    """
    Description:
    ------------
    Add a standard input component.

    Usage:
    -----

      page.ui.inputs.input("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.d_text(text, placeholder, width, height, html_code, options, attrs, profile)

  @html.Html.css_skin()
  def left(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
           attrs=None, profile=None):
    """
    Description:
    ------------
    Add a standard input component.

    Usage:
    -----

      page.ui.inputs.input("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.d_text(text, placeholder, width, height, html_code, options, attrs, profile)
    component.style.css.text_align = "left"
    component.style.css.padding_left = 5
    return component

  @html.Html.css_skin()
  def hidden(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
             attrs=None, profile=None):
    """
    Description:
    ------------
    Add a hidden input component to the page.
    This could be used to store data to then be passed to underlying services,

    Usage::

      rptObj.ui.inputs.hidden("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param placeholder: String. Optional. Text visible when the input component is empty.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the componet.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :rtype: html.HtmlInput.Input
    """
    input = self.d_text(text, placeholder, width, height, html_code, options, attrs, profile)
    input.style.css.display = None
    return input

  @html.Html.css_skin()
  def checkbox(self, flag, label="", group_name=None, width=(None, "%"), height=(None, "px"), html_code=None,
               options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.checkbox(False)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Checkbox`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    Attributes:
    ----------
    :param flag:
    :param label:
    :param group_name:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param attrs:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    attrs = attrs or {}
    html_coech = html.HtmlInput.Checkbox(self.page, flag, label, group_name, width, height, html_code,
                                         options, attrs, profile)
    return html_coech

  @html.Html.css_skin()
  def radio(self, flag, label=None, group_name=None, icon=None, width=(None, "%"), height=(None, "px"), html_code=None,
            helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.radio(['Single', 'Multiple'], html_code="type", checked="Multiple")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Radio`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_radio.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/radio.py

    Attributes:
    ----------
    :param flag:
    :param label:
    :param group_name:
    :param icon:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    html_radio = html.HtmlInput.Radio(self.page, flag, label, group_name, icon, width, height, html_code,
                                      helper, options or {}, profile)
    return html_radio

  @html.Html.css_skin()
  def editor(self, text="", language='python', width=(100, "%"), height=(300, "px"), html_code=None, options=None,
             profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.editor()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Editor`

    Attributes:
    ----------
    :param text:
    :param language:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param profile:
    """
    dflt_options = {
      "lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    editor = html.HtmlTextEditor.Editor(self.page, text, language, width, height, html_code, dflt_options,
                                        profile)
    return editor

  @html.Html.css_skin()
  def cell(self, text="", language='python', width=(100, "%"), height=(60, "px"), html_code=None, options=None,
           profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.cell()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Cell`

    Attributes:
    ----------
    :param text:
    :param language:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param profile:
    """
    dflt_options = {"lineNumbers": True, 'mode': language, 'matchBrackets': True, 'styleActiveLine': True,
                    'autoRefresh': True}
    if options is not None:
      dflt_options.update(options)
    html_cell = html.HtmlTextEditor.Cell(
      self.page, text, language, width, height, html_code, dflt_options, profile)
    return html_cell

  @html.Html.css_skin()
  def search(self, text='', placeholder='Search..', align="left", color=None, width=(100, "%"), height=(None, "px"),
             html_code=None, tooltip='', extensible=False, options=None, profile=None):
    """
    Description:
    ------------
    Add an input search component.

    Usage:
    -----

      page.ui.inputs.search()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Cell`

    Related Pages:

      https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list_filter.py

    Attributes:
    ----------
    :param text:
    :param placeholder:
    :param align:
    :param color:
    :param width:
    :param height:
    :param html_code:
    :param tooltip:
    :param extensible:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"icon": "fas fa-search", 'position': 'left', 'select': True, "border": 1}
    if options is not None:
      dflt_options.update(options)
    html_s = html.HtmlInput.Search(self.page, text, placeholder, color, width, height, html_code, tooltip,
                                   extensible, dflt_options, profile)
    html_s.style.css.height = Defaults.LINE_HEIGHT + 5
    if align == "center":
      html_s.style.css.margin = "auto"
      html_s.style.css.display = "block"
    return html_s

  @html.Html.css_skin()
  def label(self, label, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None,
            options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.label()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Input`
      - :class:`epyk.core.html.HtmlText.Label`
      - :class:`epyk.core.html.HtmlContainer.Div`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------

    """
    label = self.page.ui.texts.label(label).css({
      "display": 'block', 'text-align': 'left', 'margin-top': '10px', "position": "absolute", "z-index": '20px',
      "font-size": '14px'})
    html_input = html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code,
                                      options or {}, attrs or {}, profile).css({"margin-top": '10px'})
    div = self.page.ui.div([label, html_input])
    div.input = html_input
    div.label = label
    html_input.on('focus', [
      "document.getElementById('%s').animate({'marginTop': ['10px', '-8px']}, {duration: 50, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlCode,
    ])
    html_input.on('blur', [
      "document.getElementById('%s').animate({'marginTop': ['-8px', '10px']}, {duration: 1000, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlCode,
    ])
    return div
