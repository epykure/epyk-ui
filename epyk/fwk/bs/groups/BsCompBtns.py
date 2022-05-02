
from epyk.core.py import types
from epyk.fwk.bs.html import HtmlBsForms
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def button(self, text: str = "", icon: str = None, category: str = "primary", width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None, tooltip: str = None,
             profile: types.PROFILE_TYPE = None, options: dict = None):
    """
    Description:
    -----------
    Add a button.

    Usage::

      page.web.bs.button("Button", category="primary", tooltip="Comment")

      btn2 = page.web.bs.button(["test", b1])
      btn2.style.bs.sizing("lg")

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/buttons/

    Attributes:
    ----------
    :param text: Optional. The value to be displayed to the button.
    :param icon: Optional. A string with the value of the icon to display from font-awesome.
    :param category: Optional. The Bootstrap predefined category.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. The tooltip text.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    button = self.page.web.std.button(text, icon=icon, width=width, height=height, html_code=html_code, tooltip=tooltip,
                                      align=None, options=options, profile=profile)
    button.add_style(["btn"], {"width": width, "height": height},
                     clear_first=True)
    if category is not None:
      button.attr["class"].add("btn-%s" % category)
    return button

  def radio(self, flag=False, tooltip=None, html_code=None, group_name=None, width=(None, '%'), height=(None, "px"),
            label=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a radio component.

    Usage::

      r1 = page.web.bs.buttons.radio(label="Radio 1", group_name="group_radio")
      r2 = page.web.bs.buttons.radio(label="Radio 2", group_name="group_radio")

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/

    Attributes:
    ----------
    :param flag: Boolean. Optional. The component initial status.
    :param label: String. Optional. The text of label to be added to the component.
    :param tooltip: String. Optional. The tooltip text.
    :param group_name: String. Optional. The group name for group of radio.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "radio"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    if group_name is not None:
      html_but.attr["name"] = group_name
    html_but.tooltip(tooltip)
    return html_but

  def check(self, flag=False, tooltip=None, width=(None, "px"), height=(None, "px"), label=None, html_code=None,
            profile=None, options=None):
    """
    Description:
    -----------
    Add a check component.

    Usage::

      page.web.bs.buttons.check(label="Checkbox")

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/

    Attributes:
    ----------
    :param flag: Boolean. Optional. The component initial status.
    :param label: String. Optional. The text of label to be added to the component.
    :param tooltip: String. Optional. The tooltip text.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.tooltip(tooltip)
    return html_but

  def switch(self, flag=False, label=None, tooltip=None, width=(None, '%'), height=(None, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a switch component.

    Usage::

      page.web.bs.buttons.switch()

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/

    Attributes:
    ----------
    :param flag: Boolean. Optional. The component initial status.
    :param label: String. Optional. The text of label to be added to the component.
    :param tooltip: String. Optional. The tooltip text.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.options.switch = True
    html_but.tooltip(tooltip)
    return html_but

  def toggle(self, flag=False, label=None, width=(None, '%'), height=(None, 'px'), html_code=None, options=None,
             profile=None):
    """
    Description:
    -----------
    Add a toggle component.

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/

    Attributes:
    ----------
    :param flag: Boolean. Optional. The component initial status.
    :param label: String. Optional. The text of label to be added to the component.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsCheck(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.attr["class"].add("btn-check")
    html_but.attr["autocomplete"].add("off")
    return html_but

  def run(self, text="", category="primary", width=(None, "%"), height=(None, "px"), align="left", html_code=None,
          tooltip=None, profile=None, options=None):
    """
    Description:
    -----------
    Add a predefined run button.

    Usage::

      page.web.bs.buttons.run("Start Simulation")

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param category: String. Optional. The Bootstrap predefined category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. The tooltip text.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    btn = self.icon(
      "bi-play", text=text, category=category, width=width, height=height, align=align, html_code=html_code,
      tooltip=tooltip, profile=profile, options=options)
    return btn

  def close(self, text="", width=(None, "%"), height=(None, "px"), html_code=None, tooltip=None, profile=None,
            options=None):
    """
    Description:
    -----------
    Add a close button

    Usage::

      page.web.bs.icons.close()

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the button.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. The tooltip text.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    btn = self.button(text, width=width, height=height, html_code=html_code, tooltip=tooltip,
                      profile=profile, options=options)
    btn.attr["class"].initialise(["btn-close"])
    btn.style.clear_style()
    btn.aria.label = "Close"
    return btn

  def icon(self, icon, text="", category="primary", width=(None, "%"), height=(None, "px"), align="left",
           html_code=None, tooltip=None, profile=None, options=None):
    """
    Description:
    ------------
    Add a button icon.

    Usage::

      page.web.bs.buttons.icon("bi-x-square-fill")

    Attributes:
    ----------
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param text: String. Optional. The value to be displayed to the button.
    :param category: String. Optional. The Bootstrap predefined category.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param tooltip: String. Optional. The tooltip text.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    button = self.page.web.std.button(text, width=width, height=height, html_code=html_code, tooltip=tooltip,
                                      align=align, options=options, profile=profile)
    button.add_icon(icon, family="bootstrap-icons")
    button.icon.style.css.margin_right = 0
    button.attr["class"].initialise(["btn"])
    button.style.css.min_width = 30
    if category is not None:
      button.attr["class"].add("btn-%s" % category)
    return button
