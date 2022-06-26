from epyk.fwk.mdc import PkgImports
from epyk.interfaces import Arguments
from epyk.fwk.mdc.html import HtmlMdcForms
from epyk.fwk.mdc import groups
from epyk.core.css import Defaults as Defaults_css


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.MATERIAL_DESIGN_COMPONENTS)
    self.page.imports.reload()
    Defaults_css.ICON_FAMILY = 'material-design-icons'   # Set the default family for icons to rely on Material design
    Defaults_css.ICON_MAPPINGS[Defaults_css.ICON_FAMILY] = PkgImports.ICON_MAPPINGS
    self.page.jsImports.add("material-components-web")
    self.page.cssImport.add("material-components-web")
    self.page.css.customText('''
    :root {--mdc-theme-primary: %(color)s; --mdc-theme--on-primary: %(color)s; --mdc-theme--primary-bg: %(color)s;}
    .mdc-text-field--focused:not(.mdc-text-field--disabled) .mdc-floating-label {color: var(--mdc-theme-primary);}
    .mdc-select:not(.mdc-select--disabled).mdc-select--focused .mdc-floating-label {color: %(color)s}
    .mdc-snackbar__action:not(:disabled) {color: %(color)s}
              ''' % {"color": self.page.theme.success.base})

    self.page.cssImport.add('@cds/core')
    self.page.cssImport.add('@cds/city')
    self.page.body.attr['cds-text'] = "body"
    # Shortcut for the main components
    #self.icon = self.icons.icon
    self.check = self.buttons.check
    self.toggle = self.buttons.toggle

  def text(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Text(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    if options is not None and options.get("large"):
      html_but.attr["class"].add("ms-Spinner--large")
    return html_but

  def progress(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """
    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-linear-progress

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.ProgressBar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def select(self, text="Loading...", label: str = "", width=(None, "%"),
             height=(None, "%"), options=None, profile=None):
    """
    https://github.com/material-components/material-components-web/tree/master/packages/mdc-linear-progress

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Select(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def navbar(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """
    https://github.com/material-components/material-components-web/tree/master/packages/mdc-top-app-bar#regular-top-app-bar

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    self.page.cssImport.add("material-icons")
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.TopAppBar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def slider(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """
    https://github.com/material-components/material-components-web/tree/master/packages/mdc-top-app-bar#regular-top-app-bar

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Slider(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def snackbar(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """
    https://github.com/material-components/material-components-web/tree/master/packages/mdc-snackbar

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Snackbar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def chip(self, text="Loading...", width=(None, "%"), height=(None, "%"), options=None, profile=None):
    """
    https://github.com/material-components/material-components-web/tree/master/packages/mdc-chips

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Chip(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  # @property
  # def icons(self):
  #   """
  #   Description:
  #   ------------
  #   MDC Form Field aligns an MDC Web form field (for example, a checkbox) with its label and makes it RTL-aware.
  #   It also activates a ripple effect upon interacting with the label.
  #
  #   Related Pages:
  #
  #     https://material.io/develop/web/components/input-controls/form-fields/
  #     http://google.github.io/material-design-icons/
  #   """
  #   return GrpMtIcons.Icon(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    Buttons allow users to take actions, and make choices, with a single tap.

    Related Pages:

      https://material.io/components/buttons
    """
    return groups.MdcCompBtns.Components(self)

  @property
  def fabs(self):
    """
    Description:
    ------------
    A floating action button (FAB) represents the primary action of a screen.

    Related Pages:

      https://material.io/components/buttons-floating-action-button
    """
    return groups.MdcCompFabs.Components(self)

