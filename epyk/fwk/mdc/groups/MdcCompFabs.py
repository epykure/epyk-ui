
from epyk.core.py import types
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def floating(self, text: str = None, icon: str = None, category: str = "primary", width: types.SIZE_TYPE = (None, "%"),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None, tooltip: str = None,
               profile: types.PROFILE_TYPE = None, options: dict = None):
    """

    Related Pages:

      https://material.io/components/buttons-floating-action-button
      https://github.com/material-components/material-components-web/tree/master/packages/mdc-fab

    :param text:
    :param icon:
    :param category:
    :param width:
    :param height:
    :param html_code:
    :param tooltip:
    :param profile:
    :param options:
    """
    elements = [self.page.web.mdc.ripple()]
    if icon is not None:
      elements.append(self.page.web.mdc.icon(icon.lower()))
    if text is not None:
      elements.append(self.page.web.mdc.label(text))
    button = self.page.web.std.button(
      elements, html_code=html_code, tooltip=tooltip, align=None, options=options, profile=profile)
    button.add_style(["mdc-fab"], {"width": width, "height": height}, clear_first=True)
    if len(elements) > 2:
      button.attr["class"].add("mdc-fab--extended")
      if icon is not None:
        button.icon = elements[1]
      if text is not None:
        button.text = elements[-1]
    return button
