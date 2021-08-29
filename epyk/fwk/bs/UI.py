
from epyk.fwk.bs.html import HtmlBsForms
from epyk.fwk.bs.html import HtmlBsDate

from epyk.fwk.bs import PkgImports
from epyk.interfaces import Arguments


class BootstrapFields:

  def __init__(self, ui):
    self.page = ui.page

  def text(self, value="", label=None, color=None, align='left', width=(None, "px"), height=(None, "px"),
           html_code=None, tooltip=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "text"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def password(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "input"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def email(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSFloatingLabel(
      self.page, {"value": value, "label": label or "", "type": "email"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def textarea(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSFloatingTextArea(
      self.page, {"value": value, "label": label or "", "type": "email"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def slider(self, value=0, min=0, max=10, step=1, orientation='horizontal', label=None, width=(100, '%'),
             height=(None, 'px'), html_code=None, options=None, range=False, profile=None):
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

  def check(self, flag=False, width=(None, "px"), height=(None, "px"), label=None, html_code=None, profile=None,
            options=None):

    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def radio(self, flag=False, width=(None, "px"), height=(None, "px"), label=None, html_code=None, profile=None,
            options=None):

    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "radio"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

  def select(self, values, width=(None, "px"), height=(None, "px"), label=None, html_code=None, profile=None,
             options=None):

    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSelect(
      self.page, values, html_code, options or {}, profile,
      {"width": width, "height": height})
    return html_but

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
    date.options.formats.time_only()
    return date

  @property
  def fields(self):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/floating-labels/
    """
    return BootstrapFields(self)
