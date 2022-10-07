
from epyk.interfaces import Arguments
from epyk.fwk.bs.html import HtmlBsWidgets


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def dismiss(self, text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"),
              html_code=None, tooltip=None, profile=None, options=None):
    """   Add a dismiss button to close all toasts.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/
 
    :param text: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param category:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    btn = self.page.web.bs.button(text, icon, category, width, height, html_code, tooltip, profile, options)
    btn.add_style(["btn-close"], clear_first=True)
    btn.attr["data-bs-dismiss"] = "toast"
    btn.aria.label = "Close"
    return btn

  def container(self, components=None, label=None, color=None, width=(100, "%"), icon=None,
                height=(None, "px"), editable=False, align='left', padding=None, html_code=None, helper=None,
                options=None, profile=None, position=None):
    """
    Containers are a fundamental building block of Bootstrap that contain, pad, and align your content within a
    given device or viewport.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/#stacking
 
    :param components:
    :param label:
    :param color:
    :param width:
    :param icon:
    :param height:
    :param editable:
    :param align:
    :param padding:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    :param position:
    """
    component = self.page.web.std.div(components, label, color, width, icon, height, editable, align, padding,
                                      html_code, 'div', helper, options, profile, position)
    component.add_style(["toast-container"], clear_first=True)
    return component

  def fixed(self, components=None, label=None, color=None, width=(100, "%"), icon=None,
            height=(None, "px"), editable=False, align='left', padding=None, html_code=None, helper=None,
            options=None, profile=None, position=None):
    """   
 
    :param components:
    :param label:
    :param color:
    :param width:
    :param icon:
    :param height:
    :param editable:
    :param align:
    :param padding:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    :param position:
    """
    component = self.page.web.std.div(components, label, color, width, icon, height, editable, align, padding,
                                      html_code, 'div', helper, options, profile, position)
    component.add_style(["position-fixed", "bottom-0", "end-0", "p-3"], clear_first=True)
    return component

  def custom(self, values=None, html_code=None, width=(100, "%"), height=(None, "%"), profile=None, options=None):
    """   Push notifications to your visitors with a toast, a lightweight and easily customizable alert message.

    Usage::

      t = page.web.bs.toasts.custom(["This is content"])
      b = page.web.bs.button("Hide")
      b.click([t.js.hide()])

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/toasts/
      https://getbootstrap.com/docs/5.0/components/toasts/#custom-content
 
    :param values: List<Components>. The different HTML objects to be added to the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsToast(
      self.page, None, html_code, options or {}, profile, {"width": width, "height": height})
    component.flex_container = True
    component.attr["role"] = "alert"
    component.aria.live = "assertive"
    component.aria.atomic = "true"
    if values is not None:
      for v in values:
        component.add_to_body(v)
    return component

  def button(self, toast,  text="", icon=None, category="primary", width=(None, "%"), height=(None, "px"),
             html_code=None, tooltip=None, profile=None, options=None):
    """   Add a button attached to the modal.

    Related Pages:

      https://getbootstrap.com/docs/5.0/components/modal/
 
    :param toast:
    :param text: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param category:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    btn = self.page.web.bs.button(text, icon, category, width, height, html_code, tooltip, profile, options)
    btn.attr["data-bs-toggle"] = "toast"
    btn.attr["data-bs-target"] = "#%s" % toast.htmlCode
    return btn
