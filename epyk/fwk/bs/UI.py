
from epyk.fwk.bs.html import HtmlBsForms
from epyk.fwk.bs.html import HtmlBsDate
from epyk.fwk.bs.html import HtmlBsWidgets

from epyk.fwk.bs import PkgImports
from epyk.interfaces import Arguments


class BsCompLists:
  def __init__(self, ui):
    self.page = ui.page

  def select(self, values=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
             profile=None, multiple=False, options=None):
    """

    :param values:
    :param html_code:
    :param selected:
    :param width:
    :param height:
    :param profile:
    :param multiple:
    :param options:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSelect(
      self.page, [], html_code, options or {}, profile,
      {"width": width, "height": height})
    for v in values:
      html_but.add_option(v, v)
    return html_but

  def dropdown(self, records=None, text="", width=('auto', ""), height=(None, 'px'), html_code=None, helper=None,
               options=None, profile=None):
    """
    https://getbootstrap.com/docs/5.0/components/dropdowns/

    :param records:
    :param text:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    :return:
    """


class BsCompBtns:
  def __init__(self, ui):
    self.page = ui.page

  def button(self, text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"), align="left",
             html_code=None, tooltip=None, profile=None, options=None):
    button = self.page.web.std.button(text, icon=icon, width=width, height=height, html_code=html_code, tooltip=tooltip,
                                      align=align, options=options, profile=profile)
    button.attr["class"].initialise(["btn"])
    if category is not None:
      button.attr["class"].add("btn-%s" % category)
    return button

  def radio(self, flag=False, html_code=None, group_name=None, width=(None, '%'), height=(None, "px"), label=None,
            options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "radio"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    if group_name is not None:
      html_but.attr["name"] = group_name
    return html_but

  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(None, "px"), label=None, icon=None,
            html_code=None, profile=None, options=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.tooltip(tooltip)
    return html_but

  def switch(self, record=None, label=None, color=None, width=(None, '%'), height=(None, 'px'), align="left",
             html_code=None, options=None, profile=None):
    """
    https://getbootstrap.com/docs/5.0/forms/checks-radios/

    :param record:
    :param label:
    :param color:
    :param width:
    :param height:
    :param align:
    :param html_code:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def toggle(self, flag=False, label=None, color=None, width=(None, '%'), height=(None, 'px'), align="left",
             html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.attr["class"].add("btn-check")
    html_but.attr["autocomplete"].add("off")
    return html_but


class BsCompInputs:
  def __init__(self, ui):
    self.page = ui.page

  def textarea(self, text="", width=(100, '%'), rows=5, placeholder=None, background_color=None, html_code=None,
               options=None, profile=None):
    width = Arguments.size(width, unit="px")
    component = HtmlBsForms.BsSFloatingTextArea(
      self.page, {"value": text, "label": "", "type": "email"}, html_code, options or {}, profile,
      {"width": width})
    component.attr["placeholder"] = placeholder
    component.attr["rows"] = rows
    return component

  def datalist(self, values=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
             profile=None, multiple=False, options=None):
    """
    https://getbootstrap.com/docs/5.0/forms/form-control/

    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsDataList(
      self.page, values, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but


class BootstrapFields:

  def __init__(self, ui):
    self.page = ui.page

  def text(self, value="", label=None, color=None, align='left', width=(None, "px"), height=(None, "px"),
           html_code=None, tooltip=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "text"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return component

  def password(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "input"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    component.attr["placeholder"] = placeholder
    return component

  def email(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
            html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "email"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    component.attr["placeholder"] = placeholder
    return component

  def textarea(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsForms.BsSFloatingTextArea(
      self.page, {"value": value, "label": label or "", "type": "email"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    component.attr["placeholder"] = placeholder
    return component

  def slider(self, value=0, min=0, max=10, step=1, orientation='horizontal', label=None, width=(100, '%'),
             height=(None, 'px'), html_code=None, options=None, range=False, profile=None):
    pass


class BsCompPanelsTexts:

  def __init__(self, ui):
    self.page = ui.page


class BsCompSliders:

  def __init__(self, ui):
    self.page = ui.page

  def progressbar(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None,
                  options=None, profile=None):
    """
    https://getbootstrap.com/docs/5.0/components/progress/

    :param number:
    :param total:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """


class BsCompPanels:

  def __init__(self, ui):
    self.page = ui.page


class BsCompModals:

  def __init__(self, ui):
    self.page = ui.page

  def dialog(self, text, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None, options=None, profile=None):
    pass

  def acknowledge(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def error(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def info(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass

  def success(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass


class BsCompVignets:
  def __init__(self, ui):
    self.page = ui.page

  def card(self, records=None, width=(70, "px"), height=("auto", ''), color=None, background_color=None,
             helper=None, options=None, profile=None):
    """
    https://getbootstrap.com/docs/5.1/components/card/

    :param records:
    :param width:
    :param height:
    :param color:
    :param background_color:
    :param helper:
    :param options:
    :param profile:
    """


class BsCompAlerts:

  def __init__(self, ui):
    self.page = ui.page

  def alert(self, kind=None, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None,
            profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param kind: String. Optional. The Bootstrap predefined category.
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.page.web.std.div(
      components, width=width, height=height, html_code=html_code, options=options, profile=profile)
    content.attr["class"].initialise(["alert"])
    if kind is not None:
      content.attr["class"].add("alert-%s" % kind)
    content.attr["role"] = "alert"
    if options is not None and options.get("close"):
      btn = self.page.web.std.button()
      btn.attr["class"].initialise(["btn-close"])
      btn.attr["data-bs-dismiss"] = "alert"
      btn.attr["aria-label"] = "Close"
      btn.attr["type"] = "button"
      btn.options.managed = False
      content.val.append(btn)
    return content

  def primary(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("primary", components, width, height, html_code, options, profile)
    return content

  def secondary(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("secondary", components, width, height, html_code, options, profile)
    return content

  def success(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("secondary", components, width, height, html_code, options, profile)
    return content

  def danger(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("danger", components, width, height, html_code, options, profile)
    return content

  def warning(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("warning", components, width, height, html_code, options, profile)
    return content

  def info(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("info", components, width, height, html_code, options, profile)
    return content

  def light(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("light", components, width, height, html_code, options, profile)
    return content

  def dark(self, components=None, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add alert to the page.

    Templates:

      https://getbootstrap.com/docs/5.1/components/alerts/

    Attributes:
    ----------
    :param components: Component | String. Optional. The alert sub components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.alert("dark", components, width, height, html_code, options, profile)
    return content


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.BOOTSTRAP)
    self.page.imports.pkgs.bootstrap.version = "5.1.0"
    self.page.jsImports.add("bootstrap")
    self.page.cssImport.add("bootstrap")
    #
    self.select = self.lists.select
    self.button = self.buttons.button
    self.check = self.buttons.check
    self.toggle = self.buttons.toggle
    self.grid = self.page.web.std.grid
    self.row = self.page.web.std.row
    self.col = self.page.web.std.col

  def date(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Toast default date component.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width:
    :param height:
    :param html_code:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    date = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile,
      {"width": width, "height": height})
    date.options.formats.date_only()
    date.options.buttons.showToday = True
    date.options.buttons.showClose = True
    return date

  def time(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
    """
    Description:
    ------------
    Toast default date component.

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value:
    :param width:
    :param height:
    :param html_code:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    date = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile,
      {"width": width, "height": height})
    date.options.formats.time_only()
    return date

  def loading(self, text="Loading...", width=(None, "%"), height=(None, "%"), kind=None, options=None, profile=None):
    """
    Description:
    ------------
    Indicate the loading state of a component or page with Bootstrap spinners, built entirely with HTML, CSS,
    and no JavaScript.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/spinners/

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param kind:
    :param options:
    :param profile:
    """
    options = options or {}
    component = self.page.web.std.div(width=width, height=height, profile=profile)
    component.attr["class"].initialise(["spinner-%s" % options.get("kind", "border")])
    if kind is not None:
      component.attr["class"].add("text-%s" % kind)
    component.attr["role"] = "status"
    component.span = self.page.web.std.texts.span(text)
    component.span.attr["class"].initialise(["visually-hidden"])
    return component

  @property
  def fields(self):
    return BootstrapFields(self)

  @property
  def lists(self):
    return BsCompLists(self)

  @property
  def buttons(self):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/
    """
    return BsCompBtns(self)

  @property
  def inputs(self):
    return BsCompInputs(self)

  @property
  def sliders(self):
    return BsCompSliders(self)

  @property
  def panels(self):
    return BsCompPanels(self)

  @property
  def texts(self):
    return BsCompPanelsTexts(self)

  @property
  def alerts(self):
    """
    Description:
    ------------
    Alerts are available for any length of text, as well as an optional close button.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/alerts/
    """
    return BsCompAlerts(self)

  @property
  def modals(self):
    """
    Description:
    ------------
    Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/modal/

    Usage::

    """
    return BsCompModals(self)

  @property
  def modals(self):
    """
    Description:
    ------------
    Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/modal/

    Usage::

    """
    return BsCompModals(self)

  @property
  def vignets(self):
    """
    Description:
    ------------

    Usage::


    """
    return BsCompVignets(self)

  def accordion(self, values=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None, options=None):
    """
    Description:
    ------------
    Add an Accordion panel.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/accordion/

    Usage::

      acc = page.web.bs.accordion()
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
    component = HtmlBsWidgets.BsAccordion(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for k, v in reversed(list(values.items())):
        component.add_section(k, v)
    return component

  def breadcrumb(self, values=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None, options=None):
    """
    Description:
    ------------
    Add an breadcrumb.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/breadcrumb/

    Usage::

      page.web.bs.breadcrumb(["AAA", "BBBB"])

    Attributes:
    ----------
    :param values: List. Optional. Title: content.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsBreadcrumb(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for v in values:
        component.add_item(v)
    return component
