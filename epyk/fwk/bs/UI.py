
from epyk.fwk.bs.html import HtmlBsForms
from epyk.fwk.bs.html import HtmlBsDate

from epyk.fwk.bs import PkgImports
from epyk.interfaces import Arguments


class BsCompLists:
  def __init__(self, ui):
    self.page = ui.page

  def select(self, values=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
             profile=None, multiple=False, options=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSelect(
      self.page, values, html_code, options or {}, profile,
      {"width": width, "height": height})
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

  def radio(self, record=None, html_code=None, group_name=None, width=(100, '%'), height=(None, "px"),
            align='left', options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "radio"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(20, "px"), label=None, icon=None,
            html_code=None, profile=None, options=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
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


class BsCompAlerts:

  def __init__(self, ui):
    self.page = ui.page

  def primary(self):
    pass

  def secondary(self):
    pass

  def success(self):
    pass

  def danger(self):
    pass

  def warning(self):
    pass

  def info(self):
    pass

  def light(self):
    pass

  def dark(self):
    pass


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.BOOTSTRAP)
    self.page.imports.pkgs.bootstrap.version = "5.1.0"
    self.page.jsImports.add("bootstrap")
    self.page.cssImport.add("bootstrap")
    self.select = self.lists.select
    self.check = self.buttons.check
    self.toggle = self.buttons.toggle

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

  def breadcrumb(self, values=None, selected=None, width=(100, '%'), height=(30, 'px'), html_code=None, options=None,
                 profile=None):
    pass

  def loading(self, text="Loading...", color=None, options=None, profile=None):
    options = options or {}
    component = self.web.std.div()
    component.attr["class"].add("spinner-%s" % options.get("kind", "border"))
    component.attr["role"] = "status"
    component.span = self.web.std.texts.span(text)
    component.span.attr["class"].add("visually-hidden")
    return component

  @property
  def fields(self):
    return BootstrapFields(self)

  @property
  def lists(self):
    return BsCompLists(self)

  @property
  def buttons(self):
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
    Alerts are available for any length of text, as well as an optional close button.

    https://getbootstrap.com/docs/5.0/components/alerts/

    """
    return BsCompAlerts(self)
