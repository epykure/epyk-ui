
import json
from typing import Optional, Union

from epyk.core import html
from epyk.core.py import types
from epyk.fwk.mdc.html import HtmlMdcForms
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def button(self, text: str = "", icon: Optional[Union[str, bool]] = None, width: types.SIZE_TYPE = (None, "%"),
             height: types.SIZE_TYPE = (None, "px"), align: str = "left", html_code: str = None,
             tooltip: str = None, profile: types.PROFILE_TYPE = None,
             options: types.OPTION_TYPE = None) -> html.HtmlButton.Button:
    """
    Description:
    -----------

    Related Pages:

      https://github.com/material-components/material-components-web/tree/master/packages/mdc-button

    Attributes:
    ----------
    :param text: Optional.
    :param icon: Optional. A string with the value of the icon to display from font-awesome.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: Optional. A string with the value of the tooltip.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """

  def check(self, flag: bool = False, tooltip: str = None, width: types.SIZE_TYPE = (None, "px"),
            height: types.SIZE_TYPE =(None, "px"), label: str = None, html_code: str = None,
            profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None):
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
    :param flag: Optional. The component initial status.
    :param label: Optional. The text of label to be added to the component.
    :param tooltip: Optional. The tooltip text.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlMdcForms.Check(
      self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.tooltip(tooltip)
    html_but.style.css.min_height = 0
    return html_but

  def toggle(self, flag: bool = False, label: str = None, width: types.SIZE_TYPE = (None, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Add a toggle component.

    Usage::


    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/

    Attributes:
    ----------
    :param flag: Optional. The component initial status.
    :param label: Optional. The text of label to be added to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
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
