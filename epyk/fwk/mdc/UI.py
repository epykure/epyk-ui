from epyk.core.py import types
from epyk.core import html
from epyk.fwk.mdc import PkgImports
from epyk.interfaces import Arguments
from epyk.fwk.mdc.html import HtmlMdcForms
from epyk.fwk.mdc import groups
from typing import Union, List


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}

    self.page.icons.add('material-design-icons', PkgImports.MATERIAL_DESIGN_COMPONENTS)
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
    self.check = self.buttons.check
    self.toggle = self.buttons.toggle
    self.button = self.buttons.button
    self.icon = self.icons.icon

  def label(self, text: str = "", width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
            html_code: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlTags.HtmlGeneric:
    """
    Description:
    ------------

    Related Pages:



    Attributes:
    ----------
    """
    label = self.page.web.std.tags.span(
      text=text, width=width, height=height, html_code=html_code, options=options, profile=profile)
    label.add_style(["mdc-fab__label"], {"width": width, "height": height}, clear_first=True)
    return label

  def ripple(self, components: Union[html.Html.Html, List[html.Html.Html]] = None, color: str = None,
            width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
            editable: bool = False, align: str = 'left', padding: int = None, html_code: str = None,
            options: dict = None, profile: types.PROFILE_TYPE = None,
            position: Union[bool, dict] = None) -> html.HtmlContainer.Div:
    """
    Description:
    ------------

    Related Pages:


    Attributes:
    ----------
    """
    ripple = self.page.web.std.div(
      components=components, color=color, width=width, height=height, editable=editable, align=align, padding=padding,
      html_code=html_code, options=options, profile=profile, position=position)
    ripple.add_style(["mdc-fab__ripple"], {"width": width, "height": height}, clear_first=True)
    return ripple

  def text(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "%"),
           options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:



    Attributes:
    ----------
    :param text: Optional. The initial value.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Text(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    if options is not None and options.get("large"):
      html_but.attr["class"].add("ms-Spinner--large")
    return html_but

  def progress(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
               height: types.SIZE_TYPE = (None, "%"), options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-linear-progress

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.ProgressBar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def select(self, text: str = "Loading...", label: str = "", width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "%"), options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-linear-progress

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param label: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Select(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def navbar(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "%"), options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-top-app-bar#regular-top-app-bar

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    self.page.cssImport.add("material-icons")
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.TopAppBar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def slider(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "%"), options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-top-app-bar#regular-top-app-bar

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Slider(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  def snackbar(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
               height: types.SIZE_TYPE = (None, "%"), options: types.OPTION_TYPE = None,
               category: str = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-snackbar

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param category: Optional. The snackbar predefined category
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Snackbar(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    if category is not None:
      html_but.attr["class"].add("mdc-snackbar--{}".format(category.lower()))
    return html_but

  def chip(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "%"),
           options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-chips

    Attributes:
    ----------
    :param text: Optional. The initial value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Chip(self.page, text, None, options or {}, profile, {"width": width, "height": height})
    return html_but

  @property
  def icons(self):
    """
    Description:
    ------------
    MDC Form Field aligns an MDC Web form field (for example, a checkbox) with its label and makes it RTL-aware.
    It also activates a ripple effect upon interacting with the label.

    Related Pages:

      https://material.io/develop/web/components/input-controls/form-fields/
      http://google.github.io/material-design-icons/
    """
    return groups.MdcCompIcons.Components(self)

  @property
  def buttons(self) -> groups.MdcCompBtns.Components:
    """
    Description:
    ------------
    Buttons allow users to take actions, and make choices, with a single tap.

    Related Pages:

      https://material.io/components/buttons
    """
    return groups.MdcCompBtns.Components(self)

  @property
  def fabs(self) -> groups.MdcCompFabs.Components:
    """
    Description:
    ------------
    A floating action button (FAB) represents the primary action of a screen.

    Related Pages:

      https://material.io/components/buttons-floating-action-button
      https://github.com/material-components/material-components-web/tree/master/packages/mdc-fab
    """
    return groups.MdcCompFabs.Components(self)

  @property
  def sliders(self) -> groups.MdcCompSliders.Components:
    """
    Description:
    ------------
    Sliders allow users to make selections from a range of values.

    The MDC Slider implementation supports both single point sliders (one thumb) and range sliders (two thumbs).
    It is backed by the browser <input type="range"> element, is fully accessible, and is RTL-aware.

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-slider
    """
    return groups.MdcCompSliders.Components(self)
