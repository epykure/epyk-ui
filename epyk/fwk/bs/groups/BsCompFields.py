
from epyk.interfaces import Arguments
from epyk.core.py import types


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def text(self, value: str = "", label: str = None, placeholder: str = "",
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           tooltip=None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """   Create beautifully simple form labels that float over your input fields.

    TODO: Fix but on label animation.

    Usage::

      lbl1 = page.web.bs.fields.text("This is a label", label="Ok")

    Related Pages:

        https://getbootstrap.com/docs/5.1/forms/floating-labels/
 
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param label: Optional. The text of label to be added to the component.
    :param placeholder: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    cinput = self.page.web.std.input(value, html_code=html_code, options=options, profile=profile)
    cinput.attr["type"] = "text"
    cinput.attr["class"].initialise(["form-control"])
    cinput.style.clear_style()
    if placeholder:
      cinput.attr["placeholder"] = placeholder

    clabel = self.page.web.std.tags.label(label, options=options, profile=profile)
    clabel.attr["for"] = cinput.htmlCode
    clabel.attr["class"].clear()
    clabel.style.clear_style()

    content = self.page.web.std.div(
      [cinput, clabel], width=width, height=height, html_code=html_code, options=options, profile=profile)
    content.attr["class"].initialise(["form-floating"])
    content.style.clear_style()
    content.label = clabel
    content.input = cinput
    if tooltip is not None:
      content.tooltip(tooltip)
    return content

  def password(self, value: str = "", label: str = None, placeholder: str = "",
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
               html_code: str = None, tooltip: str = None, options: dict = None,
               profile: types.PROFILE_TYPE = None):
    """   Add password component.

    Usage::

      lbl2 = page.web.bs.fields.password("This is a label", label="Ok")

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/floating-labels/
 
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param label: Optional. The text of label to be added to the component.
    :param placeholder: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    component = self.text(value=value, label=label, placeholder=placeholder, width=width, height=height,
                          html_code=html_code, tooltip=tooltip,  options=options, profile=profile)
    component.input.attr["type"] = "password"
    return component

  def email(self, value: str = "", label: str = None, placeholder: str = "",
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
            html_code: str = None, tooltip: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None):
    """   

    Usage::

      lbl3 = page.web.bs.fields.email(label="Ok")

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/floating-labels/
 
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param label: Optional. The text of label to be added to the component.
    :param placeholder: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    component = self.text(value=value, label=label, placeholder=placeholder, width=width, height=height,
                          html_code=html_code, tooltip=tooltip,  options=options, profile=profile)
    component.input.attr["type"] = "email"
    return component

  def textarea(self, value: str = "", label: str = None, placeholder: str = "",
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
               html_code: str = None, tooltip: str = None, options: dict = None,
               profile: types.PROFILE_TYPE = None):
    """   By default, <textarea>s with .form-control will be the same height as <input>s.

    Usage::

      page.web.bs.fields.textarea(label="Ok")

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/floating-labels/
 
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param label: Optional. The text of label to be added to the component.
    :param placeholder: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    cinput = self.page.web.std.textarea(value, html_code=html_code, rows=None, options=options, profile=profile)
    cinput.attr["class"].initialise(["form-control"])
    cinput.style.clear_style()
    cinput.style.css.height = "%s%s" % (height[0], height[1])
    if placeholder:
      cinput.attr["placeholder"] = placeholder

    clabel = self.page.web.std.tags.label(label, options=options, profile=profile)
    clabel.attr["for"] = cinput.htmlCode
    clabel.attr["class"].clear()
    clabel.style.clear_style()

    content = self.page.web.std.div(
      [cinput, clabel], width=width, html_code=html_code, options=options, profile=profile)
    content.attr["class"].initialise(["form-floating"])
    content.style.clear_style()
    content.label = clabel
    content.input = cinput
    if tooltip is not None:
      content.tooltip(tooltip)
    return content


class TextComponents:

  def __init__(self, ui):
    self.page = ui.page

  def small(self, text: str, width: types.SIZE_TYPE = (100, "px"), height: types.SIZE_TYPE = (None, "px"),
            html_code: str = None, tooltip: str = '',
            options: dict = None, profile: types.PROFILE_TYPE = None):
    """   
 
    :param text: Optional. The value to be displayed to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    component = self.page.web.std.tags.small(text, width, height, html_code, tooltip, options, profile)
    component.style.clear_all(no_default=True)
    return component

  def strong(self, text: str, width: types.SIZE_TYPE = (100, "px"), height: types.SIZE_TYPE = (None, "px"),
             html_code: str = None, tooltip: str = '', options: dict = None, profile: types.PROFILE_TYPE = None):
    """   
 
    :param text: Optional. The value to be displayed to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    component = self.page.web.std.tags.strong(text, width, height, html_code, tooltip, options, profile)
    component.add_style(["me-auto"], clear_first=True)
    return component
