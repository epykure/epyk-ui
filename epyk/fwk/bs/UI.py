import logging

from epyk.core.py import primitives
from epyk.fwk.bs.html import HtmlBsDate
from epyk.fwk.bs.html import HtmlBsWidgets
from epyk.core.py import types
from typing import List

from epyk.fwk.bs import PkgImports
from epyk.fwk.bs import groups
from epyk.interfaces import Arguments


class Components:

  def __init__(self, page: primitives.PageModel):
    self.page = page
    self.icon_family = 'bootstrap-icons'
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.BOOTSTRAP)
    self.page.imports.reload()
    # Component shortcuts
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

  def set_bootstrap(self, version: str = "5.1.0"):
    """Set bootstrap version.

    :param version:
    """
    self.page.imports.pkgs.bootstrap.version = version

  def set_icons(self, icons_def: dict = None, name: str = None):
    """Set icon framework. By default this will load bootstrap-icons.

    :param icons_def: Icon framework dictionary definition
    :param name: Icon framework name
    """
    self.page.icons.add_icons(icons_def or PkgImports.ICON_MAPPINGS, name or self.icon_family, default_family=True)

  def date(self, value: str = None, width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"),
           html_code: str = None, profile: types.PROFILE_TYPE = None, options: dict = None,
           version: str = None) -> HtmlBsDate.BsDatePicker:
    """Toast default date component.

    Usage::
      page.web.bs.date("2021-08-05")
      page.web.bs.date()

    `Get Bootstrap <https://nhn.github.io/tui.date-picker/latest/>`_

    :param value: Optional. The initial time value format YYYY-MM-DD
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param version: Optional. define a particular version for Dominus Tempus
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if version:
      if HtmlBsDate.BsDatePicker.version:
        logging.error("Cannot override version if defined at HTML component level")

      self.page.imports.pkgs.get('tempus-dominus').version = version
    datepicker = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if hasattr(datepicker.options, "formats"):
      datepicker.options.formats.date_only()
    if value is not None:
      datepicker.options.date = self.page.js.moment.new(value)
    else:
      datepicker.options.date = self.page.js.moment.now()
    if hasattr(datepicker.options, "display"):
      datepicker.options.display.buttons.today = True
      datepicker.options.display.buttons.close = True
    else:
      datepicker.options.buttons.showToday = True
      datepicker.options.buttons.showClose = True
    return datepicker

  def time(self, hour: int = None, minute: int = 0, second: int = 0,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           profile: types.PROFILE_TYPE = None, options=None, version: str = None) -> HtmlBsDate.BsDatePicker:
    """Toast default date component.

    Usage::
      page.web.bs.time(23, 30)
      page.web.bs.time()

    `Get Bootstrap <https://nhn.github.io/tui.date-picker/latest/>`_

    :param hour: Optional. The hours' value
    :param minute: Optional. The minutes' value
    :param second: Optional. The seconds' value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if version:
      if HtmlBsDate.BsDatePicker.version:
        raise Exception("Cannot set")

    timepicker = HtmlBsDate.BsDatePicker(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    if hour is not None:
      timepicker.options.date = self.page.js.moment.time(hour, minute, second)
    else:
      timepicker.options.date = self.page.js.moment.now()
    if hasattr(timepicker.options, "formats"):
      timepicker.options.formats.time_only()
    return timepicker

  def loading(self, text: str = "Loading...", width: types.SIZE_TYPE = (None, "%"),
              height: types.SIZE_TYPE = (None, "%"), category=None, options: dict = None,
              profile: types.PROFILE_TYPE = None):
    """Indicate the loading state of a component or page with Bootstrap spinners, built entirely with HTML, CSS,
    and no JavaScript.

    Usage::
      l1 = page.web.bs.loading()
      l1.style.bs.sizing("sm")
      page.web.bs.loading(category="primary", options={"kind": "grow", "visible": True})

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/spinners/>`_

    :param text: Optional. The value to be displayed to the component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param category: Optional. The Bootstrap predefined category
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    self.page.imports.add('bootstrap')
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
    """Free, high quality, open source icon library with over 1,300 icons. Include them anyway you like—SVGs,
    SVG sprite, or web fonts. Use them with or without Bootstrap in any project.

    Usage::
      e = page.web.bs.icons.edit()
      e.style.css.color = "red"

    `Get Bootstrap <https://icons.getbootstrap.com/#icons>`_
    """
    self.page.cssImport.add("bootstrap-icons")
    return groups.BsCompIcons.Components(self)

  @property
  def images(self) -> groups.BsCompImages.Components:
    """Add images and badges to your web page.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/images/
      https://getbootstrap.com/docs/5.1/components/badge/
    """
    return groups.BsCompImages.Components(self)

  @property
  def fields(self) -> groups.BsCompFields.Components:
    """Create beautifully simple form labels that float over your input fields.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/forms/floating-labels/>`_
    """
    return groups.BsCompFields.Components(self)

  @property
  def texts(self) -> groups.BsCompFields.TextComponents:
    """  

    """
    return groups.BsCompFields.TextComponents(self)

  @property
  def tables(self) -> groups.BsCompTables.Components:
    """Documentation and examples for opt-in styling of tables (given their prevalent use in JavaScript plugins)
    with Bootstrap.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/content/tables/>`_
    """
    return groups.BsCompTables.Components(self)

  @property
  def lists(self) -> groups.BsCompLists.Components:
    """Customize the native <select>s with custom CSS that changes the element’s initial appearance.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/select/
      https://getbootstrap.com/docs/5.1/components/list-group/
    """
    return groups.BsCompLists.Components(self)

  @property
  def buttons(self) -> groups.BsCompBtns.Components:
    """Use Bootstrap’s custom button styles for actions in forms, dialogs, and more with support for multiple sizes,
    states, and more.

    Usage::
      btn = page.web.bs.button("Test")
      btn.click([page.js.console.log(select.dom.content)])

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/forms/checks-radios/>`_
    """
    return groups.BsCompBtns.Components(self)

  @property
  def toasts(self):
    """Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/toasts/>`_
    """
    return groups.BsCompToasts.Components(self)

  @property
  def sliders(self):
    """Use our custom range inputs for consistent cross-browser styling and built-in customization.

    Documentation and examples for using Bootstrap custom progress bars featuring support for stacked bars,
    animated backgrounds, and text labels

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/range/
      https://getbootstrap.com/docs/5.1/components/progress/
    """
    return groups.BsCompSliders.Components(self)

  @property
  def inputs(self) -> groups.BsCompInputs.Components:
    """Pre-defined inputs components.

    """
    return groups.BsCompInputs.Components(self)

  @property
  def alerts(self) -> groups.BsCompAlerts.Components:
    """Alerts are available for any length of text, as well as an optional close button.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/alerts/>`_
    """
    return groups.BsCompAlerts.Components(self)

  @property
  def modals(self) -> groups.BsCompModals.Components:
    """Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/modal/>`_

    Usage::
      oc = page.web.bs.modals.success("Content", "Title")
      oc.options.scroll = True
      page.web.bs.modals.button(oc, "Open")
    """
    return groups.BsCompModals.Components(self)

  @property
  def offcanvas(self) -> groups.BsCompModals.OffComponents:
    """Use Bootstrap’s JavaScript modal plugin to add dialogs to your site for lightboxes, user notifications,
    or completely custom content.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/modal/>`_
    """
    return groups.BsCompModals.OffComponents(self)

  @property
  def navbars(self) -> groups.BsCompNavs.Components:
    """Documentation and examples for Bootstrap’s powerful, responsive navigation header, the navbar.
    Includes support for branding, navigation, and more, including support for our collapse plugin.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/navbar/>`_
    """
    return groups.BsCompNavs.Components(self)

  @property
  def panels(self) -> groups.BsCompPanels.Components:
    """Documentation and examples for how to use Bootstrap’s included navigation components.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/navs-tabs/>`_
    """
    return groups.BsCompPanels.Components(self)

  @property
  def layouts(self) -> groups.BsCompLayouts.Components:
    """
    """
    return groups.BsCompLayouts.Components(self)

  def accordion(self, values=None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
                height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None,
                options: dict = None) -> HtmlBsWidgets.BsAccordion:
    """Add an Accordion panel.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/accordion/>`_

    Usage::
      acc = page.web.bs.accordion()
      acc.add_section("Test", "content")
      acc.header(0).click([acc.panel(0).build("New content")])

    :param values: Optional. Title: content
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
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
    """Add a breadcrumb.

    `Get Bootstrap <https://getbootstrap.com/docs/5.1/components/breadcrumb/>`_

    Usage::
      page.web.bs.breadcrumb(["AAA", "BBBB"], active="AAA")

    :param values: Optional. Title: content
    :param active: Optional. The active section in the breadcrumb
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
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
    """Add an off canvas panel.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/offcanvas/>`_

    Usage::
      oc = page.web.bs.offcanvas(["AAA", "BBB"])

    :param values: Optional. Title: content
    :param position: Optional. The offcanvas position in the page
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
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
    """Add an off canvas panel.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/offcanvas/>`_

    Usage::
      oc = page.web.bs.offcanvas(["AAA", "BBB"])

    :param values: Optional. Title: content
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
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
    """Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

    `Get Bootstrap <https://getbootstrap.com/docs/5.0/components/toasts/>`_

    :param values: Optional. Components added to the body
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
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
