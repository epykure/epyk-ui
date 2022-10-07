
from epyk.interfaces import Arguments
from epyk.fwk.bs.html import HtmlBsWidgets


class Components:

  def __init__(self, ui):
    self.page = ui.page

  def panel(self, components=None, width=(100, "%"), height=(None, "px"), html_code=None,
            options=None, profile=False):
    """

    Related Pages:

      https://getbootstrap.com/docs/5.1/components/buttons/#block-buttons

    # gap-2 d-md-flex justify-content-md-en

    :param components: List<Component>. Optional. The sub components.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    content = self.page.web.std.div(
      components, width=width, height=height, html_code=html_code, options=options, profile=profile)
    content.attr["class"].initialise(["d-grid"])
    return content

  def pills(self, data=None, active=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
            profile=None):
    """   

    Usage::

      page.web.bs.panels.pills(["tab 1", "tab 2"], active="tab 2")

    :param data:
    :param active: Boolean. Optional.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["nav-item"]
    component = self.page.web.std.lists.list([], None, width, height, html_code, None, options, profile)
    component.add_style(["nav", "nav-pills", "nav-fill"], clear_first=True)
    for value in data:
      if isinstance(value, dict):
        link = self.page.web.std.link(value["value"], value.get("url", "#"))
        if value["value"] == active:
          link.add_style(["active"])
          link.aria.current = "page"
      else:
        link = self.page.web.std.link(value)
        if value == active:
          link.add_style(["active"])
          link.aria.current = "page"
      link.add_style(["nav-link"], clear_first=True)
      li = self.page.web.std.lists.item()
      li.set_html_content(link)
      component.add(li)
    return component

  def tabs(self, data=None, active=None, width=('auto', ""), height=(None, 'px'), html_code=None, options=None,
           profile=None):
    """   

    :param data:
    :param active: Boolean. Optional.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    options["li_class"] = ["nav-item"]
    component = self.page.web.std.lists.list([], None, width, height, html_code, None, options, profile)
    component.add_style(["nav", "nav-tabs"], clear_first=True)
    for value in data:
      if isinstance(value, dict):
        link = self.page.web.std.link(value["value"], value.get("url", "#"))
        if value["value"] == active:
          link.add_style(["active"])
          link.aria.current = "page"
      else:
        link = self.page.web.std.link(value)
        if value == active:
          link.add_style(["active"])
          link.aria.current = "page"
      link.add_style(["nav-link"], clear_first=True)
      li = self.page.web.std.lists.item()
      li.set_html_content(link)
      component.add(li)
    return component

  def nav(self, items=None, active=None, vertical=False, width=(100, '%'), height=(100, '%'), options=None, profile=None):
    """   Add a simple navigation bar.

    Usage::

      n1 = page.web.bs.panels.nav(["tab 1", "tab 2"], active="tab 2")
      n1.style.bs.justify_content("end")

      page.web.bs.panels.nav(["tab 1", "tab 2"], active="tab 2", vertical=True)

    :param items:
    :param active: Boolean. Optional.
    :param vertical: Boolean. Optional. The direction for the navigation bar.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    component = HtmlBsWidgets.BsNav(
      self.page, None, None, options or {}, profile, {"width": width, "height": height})
    component.attr["data-bs-ride"] = "carousel"
    if vertical:
      component.attr["class"].add("flex-column")
    if items is not None:
      for item in items:
        component.add_item(item, active=active == item)
    return component
