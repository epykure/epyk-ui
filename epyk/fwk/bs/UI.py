
from epyk.core.py import primitives
from epyk.fwk.bs.html import HtmlBsDate
from epyk.fwk.bs.html import HtmlBsWidgets
from epyk.core.py import types
from typing import Any, List

from epyk.fwk.bs import PkgImports
from epyk.fwk.bs import groups
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Components:

  def __init__(self, page: primitives.PageModel):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.BOOTSTRAP)
    self.page.imports.reload()
    Defaults_css.ICON_FAMILY = 'bootstrap-icons'   # Set the default family for icons to rely on Bootstrap
    Defaults_css.ICON_MAPPINGS[Defaults_css.ICON_FAMILY] = PkgImports.ICON_MAPPINGS

    self.page.imports.pkgs.bootstrap.version = "5.1.0"
    self.page.jsImports.add("bootstrap")
    self.page.cssImport.add("bootstrap")
    #
    self.select = self.lists.select
    self.slider = self.sliders.slider
    self.button = self.buttons.button
    self.check = self.buttons.check
    self.toggle = self.buttons.toggle
    self.icon = self.icons.icon
    self.table = self.tables.basic
    # original containers
    self.grid = self.layouts.grid
    self.row = self.layouts.row
    self.col = self.layouts.col
    self.div = self.layouts.container

  def date(self, value: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"),
           html_code: str = None, profile: types.PROFILE_TYPE = None, options: dict = None) -> HtmlBsDate.BsDatePicker:
    """
    Description:
    ------------
    Toast default date component.

    Usage::

      page.web.bs.date("2021-08-05")
      page.web.bs.date()

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param value: Optional. The initial time value format YYYY-MM-DD
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    datepicker = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile,
      {"width": width, "height": height})
    datepicker.options.formats.date_only()
    if value is not None:
      datepicker.options.date = self.page.js.moment.new(value)
    else:
      datepicker.options.date = self.page.js.moment.now()
    datepicker.options.buttons.showToday = True
    datepicker.options.buttons.showClose = True
    return datepicker

  def time(self, hour: int = None, minute: int = 0, second: int = 0,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           profile: types.PROFILE_TYPE = None, options=None) -> HtmlBsDate.BsDatePicker:
    """
    Description:
    ------------
    Toast default date component.

    Usage::

      page.web.bs.time(23, 30)
      page.web.bs.time()

    Related Pages:

      https://nhn.github.io/tui.date-picker/latest/

    Attributes:
    ----------
    :param hour: Optional. The hours' value
    :param minute: Optional. The minutes' value.
    :param second: Optional. The seconds' value.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    timepicker = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile,
      {"width": width, "height": height})
    if hour is not None:
      timepicker.options.date = self.page.js.moment.time(hour, minute, second)
    else:
      timepicker.options.date = self.page.js.moment.now()
    timepicker.options.formats.time_only()
    return timepicker

  def loading(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
              height: types.SIZE_TYPE = (None, "%"), category=None, options: dict = None,
              profile: types.PROFILE_TYPE = None):
    """
    Description:
    ------------
    Indicate the loading state of a component or page with Bootstrap spinners, built entirely with HTML, CSS,
    and no JavaScript.

    Usage::

      l1 = page.web.bs.loading()
      l1.style.bs.sizing("sm")

      page.web.bs.loading(category="primary", options={"kind": "grow", "visible": True})

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/spinners/

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param category: Optional. The Bootstrap predefined category.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    options = options or {}
    component = self.page.web.std.div(width=width, height=height, profile=profile)
    component.attr["class"].initialise(["spinner-%s" % options.get("kind", "border")])
    if category is not None:
      component.attr["class"].add("text-%s" % category)
    component.attr["role"] = "status"
    component.span = self.page.web.std.texts.span(text)
    if options.get("visible", False):
      component.span.attr["class"].clear()
    else:
      component.span.attr["class"].initialise(["visually-hidden"])
    return component

  @property
  def icons(self) -> groups.BsCompIcons.Components:
    """
    Description:
    ------------
    Free, high quality, open source icon library with over 1,300 icons. Include them anyway you like—SVGs,
    SVG sprite, or web fonts. Use them with or without Bootstrap in any project.

    Usage::

      e = page.web.bs.icons.edit()
      e.style.css.color = "red"

    Related Pages:

      https://icons.getbootstrap.com/#icons
    """
    self.page.cssImport.add("bootstrap-icons")
    return groups.BsCompIcons.Components(self)

  @property
  def images(self) -> groups.BsCompImages.Components:
    """
    Description:
    ------------
    Add images and badges to your web page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/images/
      https://getbootstrap.com/docs/5.1/components/badge/
    """
    return groups.BsCompImages.Components(self)

  @property
  def fields(self) -> groups.BsCompFields.Components:
    """
    Description:
    ------------
    Create beautifully simple form labels that float over your input fields.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/floating-labels/
    """
    return groups.BsCompFields.Components(self)

  @property
  def texts(self) -> groups.BsCompFields.TextComponents:
    """
    Description:
    ------------

    """
    return groups.BsCompFields.TextComponents(self)

  @property
  def tables(self) -> groups.BsCompTables.Components:
    """
    Description:
    ------------
    Documentation and examples for opt-in styling of tables (given their prevalent use in JavaScript plugins)
    with Bootstrap.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
    return groups.BsCompTables.Components(self)

  @property
  def lists(self) -> groups.BsCompLists.Components:
    """
    Description:
    ------------
    Customize the native <select>s with custom CSS that changes the element’s initial appearance.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/select/
      https://getbootstrap.com/docs/5.1/components/list-group/
    """
    return groups.BsCompLists.Components(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    Use Bootstrap’s custom button styles for actions in forms, dialogs, and more with support for multiple sizes,
    states, and more.

    Usage::

      btn = page.web.bs.button("Test")
      btn.click([
        page.js.console.log(select.dom.content)
      ])

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/
    """
    return groups.BsCompBtns.Components(self)

  @property
  def toasts(self):
    """
    Description:
    ------------
    Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/
    """
    return groups.BsCompToasts.Components(self)

  @property
  def sliders(self):
    """
    Description:
    ------------
    Use our custom range inputs for consistent cross-browser styling and built-in customization.

    Documentation and examples for using Bootstrap custom progress bars featuring support for stacked bars,
    animated backgrounds, and text labels

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/range/
      https://getbootstrap.com/docs/5.1/components/progress/
    """
    return groups.BsCompSliders.Components(self)

  @property
  def inputs(self) -> groups.BsCompInputs.Components:
    """
    Description:
    ------------
    Pre-defined inputs components.

    """
    return groups.BsCompInputs.Components(self)

  @property
  def alerts(self) -> groups.BsCompAlerts.Components:
    """
    Description:
    ------------
    Alerts are available for any length of text, as well as an optional close button.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/alerts/
    """
    return groups.BsCompAlerts.Components(self)

  @property
  def modals(self) -> groups.BsCompModals.Components:
    """
    Description:
    ------------
    Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/modal/

    Usage::

      oc = page.web.bs.modals.success("Content", "Title")
      oc.options.scroll = True
      page.web.bs.modals.button(oc, "Open")
    """
    return groups.BsCompModals.Components(self)

  @property
  def offcanvas(self) -> groups.BsCompModals.OffComponents:
    """
    Description:
    ------------
    Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/modal/

    Usage::

    """
    return groups.BsCompModals.OffComponents(self)

  @property
  def navbars(self) -> groups.BsCompNavs.Components:
    """
    Description:
    ------------
    Documentation and examples for Bootstrap’s powerful, responsive navigation header, the navbar.
    Includes support for branding, navigation, and more, including support for our collapse plugin.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/navbar/

    Usage::

    """
    return groups.BsCompNavs.Components(self)

  @property
  def panels(self) -> groups.BsCompPanels.Components:
    """
    Description:
    ------------
    Documentation and examples for how to use Bootstrap’s included navigation components.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/navs-tabs/
    """
    return groups.BsCompPanels.Components(self)

  @property
  def layouts(self) -> groups.BsCompLayouts.Components:
    """
    Description:
    ------------

    Related Pages:


    """
    return groups.BsCompLayouts.Components(self)

  def accordion(self, values=None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
                height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None,
                options: dict = None) -> HtmlBsWidgets.BsAccordion:
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
    :param values: Optional. Title: content.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsAccordion(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for k, v in reversed(list(values.items())):
        component.add_section(k, v)
    return component

  def breadcrumb(self, values: list = None, active: str = None, html_code: str = None,
                 width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "%"),
                 profile: types.PROFILE_TYPE = None, options: dict = None) -> HtmlBsWidgets.BsBreadcrumb:
    """
    Description:
    ------------
    Add a breadcrumb.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/breadcrumb/

    Usage::

      page.web.bs.breadcrumb(["AAA", "BBBB"], active="AAA")

    Attributes:
    ----------
    :param values: Optional. Title: content.
    :param active: Optional. The active section in the breadcrumb.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsBreadcrumb(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for v in values:
        component.add_section(v, active=v == active)
    return component

  def offcanva(self, values: list = None, position: str = "start", html_code: str = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "%"),
               profile: types.PROFILE_TYPE = None, options: dict = None) -> HtmlBsWidgets.BsOffCanvas:
    """
    Description:
    ------------
    Add an off canvas panel.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/

    Usage::

      oc = page.web.bs.offcanvas(["AAA", "BBB"])

    Attributes:
    ----------
    :param values: Optional. Title: content.
    :param position: Optional. The offcanvas position in the page.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsOffCanvas(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    component.add_style(["offcanvas-%s" % position])
    component.attr["aria-labelledby"] = "offcanvasLabel"
    component.attr["tabindex"] = "-1"
    component.add_to_header(self.page.web.bs.offcanvas.dismiss(component))
    if values is not None:
      for v in values:
        component.add_to_body(v)
    return component

  def modal(self, values: dict = None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None,
            options: dict = None) -> HtmlBsWidgets.BsModal:
    """
    Description:
    ------------
    Add an off canvas panel.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/offcanvas/

    Usage::

      oc = page.web.bs.offcanvas(["AAA", "BBB"])

    Attributes:
    ----------
    :param values: Optional. Title: content.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsModal(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if values is not None:
      for v in values:
        component.add_to_body(v)
    component.attr["tabindex"] = "-1"
    component.options.fade = True
    return component

  def navbar(self, values=None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None,
             options: dict = None) -> HtmlBsWidgets.BsNavBar:
    """
    Description:
    -----------

    Attributes:
    ----------
    :param values:
    :param html_code:
    :param width:
    :param height:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsNavBar(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    component.attr["aria-labelledby"] = "offcanvasLabel"
    component.attr["tabindex"] = "-1"
    component.add_to_header(self.page.web.bs.offcanvas.dismiss(component))
    if values is not None:
      for v in values:
        component.add_to_body(v)
    return component

  def scrollspy(self, values=None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
                height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None, options: dict = None):
    pass

  def toast(self, values: List[primitives.HtmlModel] = None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None,
            options: dict = None) -> HtmlBsWidgets.BsToast:
    """
    Description:
    -----------
    Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

    Usage::


    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/

    Attributes:
    ----------
    :param values: Optional. Components added to the body.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsToast(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    component.attr["role"] = "alert"
    component.aria.live = "assertive"
    component.aria.atomic = "true"
    if values is not None:
      for v in values:
        component.add_to_body(v)
    return component

