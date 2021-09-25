
from epyk.interfaces import Arguments
from epyk.fwk.bs.html import HtmlBsForms


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def select(self, records=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
             profile=None, multiple=False, options=None):
    """
    Description:
    -----------
    HTML Select component.

    Usage::

      select = page.web.bs.lists.select([
        {"value": "value 1"},
        {"value": "value 2"},
        {"value": "value 3", "selected": True},
      ], multiple=True)

      select = page.web.bs.lists.select(selected="value 2")
      data = ["value 1", "value 2", "value 3"]
      select.data = select.parsers.from_list(data)

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/select/

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param selected: String. Optional. The selected value or values.
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param multiple: Boolean. Optional. To set if the component can handle multiple selections.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    html_but = HtmlBsForms.BsSelect(
      self.page, [], html_code, options or {}, profile,
      {"width": width, "height": height})
    html_but.init_selected = selected
    if records is not None:
      for rec in records:
        if selected is not None:
          if rec["value"] == selected:
            rec["selected"] = True
        html_but.add_option(rec["value"], rec.get("name", rec["value"]), selected=rec.get("selected", False))
    if multiple:
      html_but.attr["multiple"] = True
    return html_but

  def dropdown(self, records=None, text="", width=('auto', ""), height=(None, 'px'), html_code=None,
               options=None, profile=None):
    """
    Description:
    -----------


    https://getbootstrap.com/docs/5.0/components/dropdowns/

    Attributes:
    ----------
    :param records:
    :param text:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """

  def list(self, data=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
           profile=None):
    """
    Description:
    -----------
    List groups are a flexible and powerful component for displaying a series of content.
    Modify and extend them to support just about any content within.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/list-group

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["list-group-item"]
    component = self.page.web.std.lists.list(data, None, width, height, html_code, None, options, profile)
    component.attr["class"].initialise(["list-group"])
    return component

  def numbers(self, data=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
              profile=None):
    """
    Description:
    -----------
    Add the .list-group-numbered modifier class (and optionally use an <ol> element) to opt into numbered list group
    items. Numbers are generated via CSS (as opposed to a <ol>s default browser styling) for better placement inside l
    ist group items and to allow for better customization.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/list-group/#numbered

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["list-group-item"]
    component = self.page.web.std.lists.list(data, None, width, height, html_code, None, options, profile)
    component.attr["class"].initialise(["list-group", "list-group-numbered"])
    return component

  def buttons(self, data=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
              profile=None):
    """
    Description:
    -----------
    With <button>s, you can also make use of the disabled attribute instead of the .disabled class. Sadly,
    <a>s don’t support the disabled attribute.

    Usage::

      list = select = page.web.bs.lists.buttons(["value 1", "value 2", "value 3"])
      list.item(0).add_style("active")
      list.item(2).add_style("disabled")

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/list-group/#links-and-buttons

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["list-group-item", "list-group-item-action"]
    options["item_type"] = "button"
    component = self.page.web.std.lists.list(data, None, width, height, html_code, None, options, profile)
    component.attr["class"].initialise(["list-group", "list-group-numbered"])
    return component

  def flush(self, data=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
            profile=None):
    """
    Description:
    -----------
    Add .list-group-flush to remove some borders and rounded corners to render list group items edge-to-edge in a
    parent container (e.g., cards).

    Usage::

      list = select = page.web.bs.lists.flush(["value 1", "value 2", "value 3"])
      list.item(1).add_style("list-group-item-success")
      list.item(0).add_style("active")
      list.item(2).add_style("disabled")

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/list-group/#flush

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["list-group-item"]
    component = self.page.web.std.lists.list(data, None, width, height, html_code, None, options, profile)
    component.attr["class"].initialise(["list-group", "list-group-flush"])
    return component

  def badges(self, values, width=('auto', ""), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a list of badges.

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/list-group/#with-badges

    Usage::

      list = select = page.web.bs.lists.badges({
        "value 1": 23, "value 2": 14, "value 3": 59})
      list.item(0).add_style("active")
      list.item(2).add_style("disabled")

    Attributes:
    ----------
    :param values:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    options = options or {}
    options["li_class"] = ["list-group-item", "d-flex", "justify-content-between", "align-items-center"]
    component = self.page.web.std.lists.list([], None, width, height, html_code, None, options, profile)
    for k, v in values.items():
      b = self.page.web.bs.images.pill(v)
      li = self.page.web.std.lists.item()
      li.innerPyHTML = [k]
      li.set_html_content(b)
      li.add_style(options["li_class"], clear_first=True)
      component.add(li)
    component.attr["class"].initialise(["list-group"])
    return component

  def checks(self, data=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------
    Add a list checkboxes.

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. Integer for the component width.
    :param height: Tuple. Optional. Integer for the component height.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    options = options or {}
    options["li_class"] = ["list-group-item"]
    options["item_type"] = "button"
    component = self.page.web.std.lists.list([], None, width, height, html_code, None, options, profile)
    for value in data:
      check = self.page.web.bs.check(label=value)
      check.add_style(["form-check-input", "me-1"], clear_first=True)
      li = self.page.web.std.lists.item("", tag="label")
      li.set_html_content(check)
      component.add(li)
    component.attr["class"].initialise(["list-group"])
    return component

  def datalist(self, records=None, html_code=None, selected=None, width=(100, "%"), height=(None, "%"),
               profile=None, options=None):
    """
    Description:
    -----------
    Datalists allow you to create a group of <option>s that can be accessed (and autocompleted) from within an <input>.
    These are similar to <select> elements, but come with more menu styling limitations and differences.
    While most browsers and operating systems include some support for <datalist> elements, their styling is
    nconsistent at best.

    Usage::

      select = page.web.bs.lists.datalist(selected="value 2")
      data = ["value 1", "value 2", "value 3"]
      select.data = select.parsers.from_list(data)

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/form-control/

    Attributes:
    ----------
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
    component = HtmlBsForms.BsDataList(
      self.page, [], html_code, options or {}, profile,
      {"width": width, "height": height})
    component.init_selected = selected
    if records is not None:
      for rec in records:
        if selected is not None:
          if rec["value"] == selected:
            rec["selected"] = True
        component.add_option(rec["value"], rec.get("name", rec["value"]), selected=rec.get("selected", False))
    component.attr["list"] = "%sOptions" % component.htmlCode
    return component
