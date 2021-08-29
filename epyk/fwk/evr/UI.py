from epyk.interfaces import Arguments
from epyk.fwk.evr import PkgImports
from epyk.fwk.evr.html import HtmlEvrForms


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.EVERGREEN)
    self.page.jsImports.add('evergreen-ui')

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlEvrForms.Btn(
      self.page, text, html_code, options or {}, profile, {"width": width, "height": height})
    return html_but

