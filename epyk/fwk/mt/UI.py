from epyk.interfaces import Arguments
from epyk.fwk.mt import PkgImports


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.MATERIAL_DESIGN_COMPONENTS)
    self.page.jsImports.add("material-components-web")
    self.page.cssImport.add("material-components-web")
    self.page.css.customText('''
    :root {--mdc-theme-primary: %(color)s; --mdc-theme--on-primary: %(color)s; --mdc-theme--primary-bg: %(color)s;}
    .mdc-text-field--focused:not(.mdc-text-field--disabled) .mdc-floating-label {color: var(--mdc-theme-primary);}
              ''' % {"color": self.page.theme.success[1]})

    self.page.cssImport.add('@cds/core')
    self.page.cssImport.add('@cds/city')
    self.page.body.attr['cds-text'] = "body"
