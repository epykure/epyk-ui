from epyk.interfaces import Arguments
from epyk.fwk.ftw.html import HtmlFtwForms


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def select(self, records=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
             profile=None, options=None):
    """   HTML Select component.

    Usage::

      select = page.web.ftw.lists.select([
        {"value": "value 1"},
        {"value": "value 2"},
        {"value": "value 3", "selected": True},
      ], multiple=True)

      select = page.web.ftw.lists.select(selected="value 2")
      data = ["value 1", "value 2", "value 3"]
      select.data = select.parsers.from_list(data)

    Related Pages:

      https://developer.microsoft.com/en-us/fabric-js/components/dropdown/dropdown
 
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param selected: String. Optional. The selected value or values.
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlFtwForms.Select(
      self.page, [], html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.init_selected = selected
    if records is not None:
      for rec in records:
        if selected is not None:
          if rec["value"] == selected:
            rec["selected"] = True
        html_but.add_option(rec["value"], rec.get("name", rec["value"]), selected=rec.get("selected", False))
    html_but.attr["tabindex"] = "0"
    return html_but
