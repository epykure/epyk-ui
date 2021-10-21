
import json
from epyk.fwk.mdc.html import HtmlMdcForms
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

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
    html_but = HtmlMdcForms.Check(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.tooltip(tooltip)
    html_but.style.css.min_height = 0
    return html_but

  def toggle(self, flag=False, label=None, width=(None, '%'), height=(None, 'px'), html_code=None, options=None,
             profile=None):
    """
    Description:
    -----------
    Add a toggle component.

    Usage::


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
    html_but = HtmlMdcForms.Toggle(
      self.page, {"checked": flag, "label": label or ""}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.attr["type"] = "button"
    html_but.attr["role"] = "switch"
    if flag:
      html_but.attr["class"].add("mdc-switch--selected")
    else:
      html_but.attr["class"].add("mdc-switch--unselected")
    html_but.aria.checked = json.dumps(flag)
    return html_but
