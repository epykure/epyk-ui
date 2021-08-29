from epyk.interfaces import Arguments
from epyk.fwk.clr import PkgImports
from epyk.fwk.clr.html import HtmlClrForms


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.CLARITY)
    self.page.cssImport.add('@cds/core')
    self.page.cssImport.add('@cds/city')
    self.page.body.attr['cds-text'] = "body"

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
    self.page.jsImports.add('@cds/button')
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlClrForms.Btn(
      self.page, text, html_code, options or {}, profile, {"width": width, "height": height})
    return html_but
