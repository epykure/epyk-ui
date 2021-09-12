
from epyk.fwk.bs.html import HtmlBsDate
from epyk.fwk.bs.html import HtmlBsWidgets

from epyk.fwk.bs import PkgImports
from epyk.fwk.bs import groups
from epyk.interfaces import Arguments


class Components:

  def __init__(self, page):
    self.page = page
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(PkgImports.BOOTSTRAP)
    self.page.imports.reload()

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

  def date(self, value=None, width=(None, "px"), height=(None, "px"), html_code=None, profile=None, options=None):
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
    :param value: String. Optional. The initial time value format YYYY-MM-DD
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def time(self, hour=None, minute=0, second=0, width=(None, "px"), height=(None, "px"), html_code=None, profile=None,
           options=None):
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
    :param hour: Integer. Optional. The hours' value
    :param minute: Integer. Optional. The minutes' value.
    :param second: Integer. Optional. The seconds' value.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def loading(self, text="Loading...", width=(None, "%"), height=(None, "%"), category=None, options=None, profile=None):
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
    :param text: String. Optional. The value to be displayed to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param category: String. Optional. The Bootstrap predefined category.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
  def icons(self):
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
  def images(self):
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
  def fields(self):
    """
    Description:
    ------------
    Create beautifully simple form labels that float over your input fields.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/floating-labels/
    """
    return groups.BsCompFields.Components(self)

  @property
  def tables(self):
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
  def lists(self):
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

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/
    """
    return groups.BsCompBtns.Components(self)

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
  def inputs(self):
    """
    """
    return groups.BsCompInputs.Components(self)

  @property
  def alerts(self):
    """
    Description:
    ------------
    Alerts are available for any length of text, as well as an optional close button.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/alerts/
    """
    return groups.BsCompAlerts.Components(self)

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
    return groups.BsCompModals.Components(self)

  @property
  def vignets(self):
    """
    Description:
    ------------

    Usage::


    """
    return groups.BsCompVignets.Components(self)

  @property
  def panels(self):
    """
    Description:
    ------------
    Documentation and examples for how to use Bootstrap’s included navigation components.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/navs-tabs/
    """
    return groups.BsCompPanels.Components(self)

  @property
  def layouts(self):
    """
    Description:
    ------------

    Related Pages:


    """
    return groups.BsCompLayouts.Components(self)

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

  def breadcrumb(self, values=None, active=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None,
                 options=None):
    """
    Description:
    ------------
    Add an breadcrumb.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/breadcrumb/

    Usage::

      page.web.bs.breadcrumb(["AAA", "BBBB"], active="AAA")

    Attributes:
    ----------
    :param values: List. Optional. Title: content.
    :param active: String. Optional. The active section in the breadcrumb.
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
        component.add_section(v, active=v==active)
    return component
