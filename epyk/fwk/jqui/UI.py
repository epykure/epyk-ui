
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.fwk.jqui.html import HtmlJqUIWidgets


class Components:

  def __init__(self, page):
    self.page = page
    self.page.jsImports.add("jqueryui")
    self.page.cssImport.add("jqueryui")

  def progressbar(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
                  options=None, profile=None):
    """
    Description:
    ------------
    Add a progress bar component to the page.

    Usage::

      page.ui.sliders.progressbar(300)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.ProgressBar`

    Related Pages:

      https://jqueryui.com/progressbar/

    Attributes:
    ----------
    :param number: Integer. Optional. The initial value. (by default between 0 and 100)
    :param total: Integer. Optional. The maximum value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.ProgressBar(
      self.page, number, total, width, height, helper, options or {}, html_code, profile)
    return html_pr

  def progress(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
               options=None, profile=None):
    """
    Description:
    ------------
    Add a progress bar component to the page.

    Related Pages:

      https://jqueryui.com/progressbar/

    Attributes:
    ----------
    :param number: Integer. Optional. The initial value.
    :param total: Integer. Optional. The maximum value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    progress = self.progressbar(number, total, width, height, html_code, helper, options, profile)
    progress.style.css.border_radius = '50px'
    progress.style.css.background = self.page.theme.greys[4]
    progress.options.css({"border-radius": "50px", "border-color": self.page.theme.greys[5]})
    return progress

  def selections(self, data, width=(150, 'px'), height=('auto', ''), html_code=None, helper=None, options=None,
                 profile=None):
    """
    Description:
    ------------
    Menu using Jquery UI external module.

    Usage::

        page.ui.menus.selections(["Item 1", "Item 2"])

        page.ui.menus.selections([
          {'value': "fas fa-exclamation-triangle", 'items': [
            {"value": 'value 1'},
            {"value": 'value 2'},
            {"value": 'value 3'},
          ]},
            "fas fa-exclamation-triangle"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

    Related Pages:

      https://jqueryui.com/menu/

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    new_data = []
    for d in data:
      if not isinstance(d, dict):
        new_data.append({"value": d})
      else:
        new_data.append(d)
    html_pr = html.HtmlEvent.Menu(self.page, new_data, width, height, helper, options or {}, html_code, profile)
    return html_pr

  def dialogs(self, text="", width=(100, '%'), height=(20, 'px'), html_code=None, helper=None, options=None,
              profile=None):
    """
    Description:
    ------------
    Simple Jquery UI modal with a text.

    :tags:
    :categories:

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.Dialog(self.page, text, width, height, helper, options or {}, html_code, profile)
    return html_pr

  def slider(self, number=0, minimum=0, maximum=100, width=(100, '%'), height=(None, 'px'), html_code=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a Jquery UI slider object to the page.

    Usage::

      page.ui.slider(40)
      page.ui.slider([1, 2, 3, 4, 5, 6, 7])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Slider`

    Related Pages:

      https://jqueryui.com/slider/

    Attributes:
    ----------
    :param number: Integer. Optional. The initial value.
    :param minimum: Integer. Optional. The minimum value.
    :param maximum: Integer. Optional. The maximum value.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if isinstance(number, list):
      minimum, maximum = min(number), max(number)
      number = minimum
    html_slider = html.HtmlEvent.Slider(
      self.page, number, minimum, maximum, width, height, helper, options or {}, html_code, profile)
    return html_slider

  def date(self, text, placeholder='', width=(140, "px"), height=(None, "px"), html_code=None, options=None,
           attrs=None, profile=None):
    """
    Description:
    ------------
    Add a datepicker.

    Usage::

      date = page.ui.inputs.d_date()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.InputDate`

    Related Pages:

      https://jqueryui.com/datepicker/

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
    html_date = html.HtmlInput.InputDate(self.page, text, placeholder, width, height, html_code, options,
                                         attrs or {}, profile)
    return html_date

  def panel(self, left=None, right=None, width=(100, '%'), height=(200, 'px'), left_width=(160, 'px'), resizable=True,
            helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a split panel to the page.

    :tags:
    :categories:

    Usage::

      number = page.ui.rich.number(500, "Test", height=(150, 'px'))
      number_2 = page.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
      div = page.ui.layouts.panelsplit(left=number, right=number_2)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.PanelSlide`

    Related Pages:

      https://codepen.io/rstrahl/pen/eJZQej
      https://jqueryui.com/resizable/

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param left_width:
    :param left:
    :param right:
    :param resizable:
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_split = html.HtmlContainer.PanelSplit(
      self.page, width, height, left_width, left, right, resizable, helper, options, profile)
    return html_split

  def autocomplete(self, text="", placeholder='', width=(100, "%"), height=(None, "px"), html_code=None, options=None,
                   attrs=None, profile=None):
    """
    Description:
    ------------
    Enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching
    and filtering.

    Usage::

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
    :param attrs: Dictionary. Optional. Specific HTML tags to be added to the component.
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

  def accordion(self, values=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None, options=None):
    """
    Description:
    ------------
    Add an Accordion panel.

    Related Pages:

      https://jqueryui.com/accordion/

    Usage::

      acc = page.web.jqui.accordion()
      acc.add_section("Test", "content")
      acc.header(0).click([
        acc.panel(0).build("New content")
      ])

    Attributes:
    ----------
    :param values: Dictionary. Optional. Title: content.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlJqUIWidgets.JqAccordion(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for k, v in reversed(values.items()):
        component.add_section(k, v)
    return component

  def tabs(self, values=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None, options=None):
    """
    Description:
    -----------
    Add tabs panel.

    Related Pages:

      https://jqueryui.com/tabs/

    Usage::

      acc = page.web.jqui.tabs()
      acc.add_panel("Test", "content")
      acc.tab(0).click([
        acc.panel(0).build("New content")
      ])

    Attributes:
    ----------
    :param values: Dictionary. Optional. Title: content.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlJqUIWidgets.JqTabs(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for k, v in reversed(values.items()):
        component.add_panel(k, v)
    return component
