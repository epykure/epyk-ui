
class Components:

  def __init__(self, ui):
    self.page = ui.page

  def dialog(self, text, title="", width=(100, '%'), height=(20, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a simple dialog modal.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Usage::

      oc = page.web.bs.modals.dialog("content", "Title")

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.bs.modal(
      width=width, height=height, html_code=html_code, options=options, profile=profile)
    component.add_to_header(self.title(title))
    component.add_to_body(text)
    return component

  def acknowledge(self, components=None, title="", width=(100, '%'), height=(None, 'px'), html_code=None,
                  options=None, profile=None):
    """
    Description:
    -----------
    Add an acknowledgement modal.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/borders/

    Attributes:
    ----------
    :param components:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.bs.modal(
      width=width, height=height, html_code=html_code, options=options, profile=profile)
    component.add_to_header(self.title(title))
    component.close = self.button(component, "Close", width=(None, "px"), category="secondary")
    component.confirm = self.button(component, "Confirm", width=(None, "px"))
    component.add_to_footer(component.close)
    component.add_to_footer(component.confirm)
    for c in components:
      component.add_to_body(c)
    component.options.backdrop = "static"
    return component

  def error(self, text, title="", width=(100, '%'), height=(20, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add an error modal.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.bs.modal(
      width=width, height=height, html_code=html_code, options=options, profile=profile)
    icon = self.page.web.bs.icon("bi-exclamation-triangle-fill")
    icon.attr["class"].add("text-danger")
    component.add_to_header(icon)
    component.add_to_header(self.title(title))
    component.add_to_body(text)
    return component

  def success(self, text, title="", width=(100, '%'), height=(20, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add an success modal.

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/borders/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.bs.modal(
      width=width, height=height, html_code=html_code, options=options, profile=profile)
    icon = self.page.web.bs.icon("bi-exclamation-triangle-fill")
    icon.attr["class"].add("text-success")
    component.add_to_header(icon)
    component.add_to_header(self.title(title))
    component.add_to_body(text)
    return component

  def title(self, value="", level=5, width=(100, '%'), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a modal title component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the component.
    :param level: Integer. Optional.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.tags.hn(
      level, value, width=width, height=height, html_code=html_code, options=options, profile=profile)
    component.add_style(["modal-title"], clear_first=True)
    return component

  def button(self, modal,  text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"),
             html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------
    Add a button attached to the modal.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Attributes:
    ----------
    :param modal:
    :param text: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param category:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    btn = self.page.web.bs.button(text, icon, category, width, height, html_code, tooltip, profile, options)
    btn.attr["data-bs-toggle"] = "modal"
    btn.attr["data-bs-target"] = "#%s" % modal.htmlCode
    return btn

  def dismiss(self, text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"),
              html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    -----------
    Add a dismiss button to close all modals.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param category:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    btn = self.page.web.bs.button(text, icon, category, width, height, html_code, tooltip, profile, options)
    btn.add_style(["btn-close"], clear_first=True)
    btn.attr["data-bs-dismiss"] = "modal"
    btn.aria.label = "Close"
    return btn


class OffComponents:

  def __init__(self, ui):
    self.page = ui.page

  def button(self, offcanvas, text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"),
             html_code=None, tooltip=None, profile=None, options=None):
    btn = self.page.web.bs.button(text, icon, category, width, height, html_code, tooltip, profile, options)
    btn.attr["data-bs-toggle"] = "offcanvas"
    btn.attr["aria-controls"] = offcanvas.htmlCode
    btn.attr["data-bs-target"] = "#%s" % offcanvas.htmlCode
    return btn

  def dismiss(self, offcanvas, icon=None, category="primary", width=(None, "%"), height=(None, "px"),
              html_code=None, tooltip=None, profile=None, options=None):
    btn = self.page.web.bs.button("", icon, category, width, height, html_code, tooltip, profile, options)
    btn.add_style(["btn-close", "text-reset"], clear_first=True)
    btn.attr["data-bs-toggle"] = "offcanvas"
    btn.attr["aria-controls"] = offcanvas.htmlCode
    btn.attr["data-bs-target"] = "#%s" % offcanvas.htmlCode
    return btn

  def title(self, value="", level=5, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the component.
    :param level:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.page.ui.tags.hn(level, value, width=width, height=height, options=options, profile=profile)
    component.add_style(["offcanvas-title"], clear_first=True)
    return component
