
from epyk.core.html.Html import Component
from epyk.core.html import HtmlList
from epyk.fwk.bs.options import OptBsWidget


class BsBreadcrumb(Component):
  name = "Bootstrap Breadcrumb"
  str_repr = '''<nav aria-label="breadcrumb" {attrs}><ol class="breadcrumb">{sub_items}</ol></nav>'''
  dyn_repr = '''{sub_item}'''

  def add_item(self, component, active=False):
    """
    Description:
    -----------
    Add the sub item to the list of items.
    This will also add the component to the page component dictionary.

    Attributes:
    ----------
    :param component: Component | String. The breadcrumb item.
    :param active: Boolean. Optional. The selected status for the item.
    """
    if not hasattr(component, "options"):
      component = HtmlList.Li(self.page, component)
    component.attr["class"].add("breadcrumb-item")
    if active:
      component.attr["class"].add("active")
    component.options.managed = False
    self.components.add(component)
    self.items.append(component)
    return component

  def add_section(self, text, url="#", active=False):
    """
    Description:
    -----------
    Add a section to the breadcrumb.

    Attributes:
    ----------
    :param text: String. The link to be added.
    :param url: String. Optional. The link when clicked.
    :param active: Boolean. Optional. The current page.
    """
    if active:
      component = HtmlList.Li(self.page, text)
      component.attr["class"].add("breadcrumb-item")
      component.attr["class"].add("active")
      component.aria.current = "page"
    else:
      link = self.page.web.std.link(text, url)
      link.attr["class"].clear()
      component = HtmlList.Li(self.page, link)
      component.attr["class"].add("breadcrumb-item")
    component.options.managed = False
    self.components.add(component)
    self.items.append(component)
    return component


class BsAccordion(Component):
  css_classes = ["accordion"]
  name = "Bootstrap Accordion"
  str_repr = '''<div {attrs}>{sub_items}</div>'''
  dyn_repr = '''{sub_item}'''

  def header(self, n):
    """
    Description:
    -----------
    Get a dedicated header component.

    Attributes:
    ----------
    :param n: Integer. The header index.
    """
    return self.items[n]["header"]

  def panel(self, n):
    """
    Description:
    -----------
    Get a dedicated panel component.

    Attributes:
    ----------
    :param n: Integer. The panel index.
    """
    return self.items[n]["content"]

  def add_section(self, header, content, prepend=False):
    """
    Description:
    -----------
    Add a new section to the accordion component.

    Attributes:
    ----------
    :param header: String | Component. The tab title.
    :param content: String | Component. The tab panel.
    :param prepend: Boolean. Optional. The position of the tab.
    """
    button = self.page.web.std.button(header)
    button.attr["class"].initialise(["accordion-button"])
    button.attr["data-bs-toggle"] = "collapse"
    button.attr["aria-expanded"] = "true"
    button.options.managed = False
    header = self.page.web.std.div(button)
    header.attr["class"].initialise(["accordion-header"])
    header.options.managed = False
    content_body = self.page.web.std.div(content)
    content_body.attr["class"].initialise(["accordion-body"])
    content = self.page.web.std.div(content_body)
    content.attr["class"].initialise(["accordion-collapse", "collapse", "show"])
    content.attr["aria-labelledb"] = header.htmlCode
    button.attr["aria-controls"] = content.htmlCode
    button.attr["data-bs-target"] = "#%s" % content.htmlCode
    content.options.managed = False
    if prepend:
      self.items.insert(0, {"header": header, "content": content})
    else:
      self.items.append({"header": header, "content": content})

  def write_item(self, item):
    """
    Description:
    -----------
    Write an item to the component definition.

    Attributes:
    ----------
    :param item: Dictionary. A sub item to the accrdion object.
    """
    content = self.page.web.std.div([item["header"], item["content"]])
    content.attr["class"].add("accordion-item")
    content.options.managed = False
    return {"sub_item": content.html()}


class BsDropdown(Component):
  css_classes = ["dropdown"]
  name = "Bootstrap Dropdown"
  str_repr = '''<div {attrs}>{buttons}<ul class="dropdown-menu">{sub_items}<ul></div>'''

  def __init__(self, report, vals, html_code=None, options=None, profile=None, css_attrs=None):
    super(BsDropdown, self).__init__(report, vals, html_code, options, profile, css_attrs)
    self.items = {"buttons": [], "options": []}

  def button(self, n=0):
    """
    Description:
    -----------
    Get a dedicated button from the Dropdown component.
    By default there is a button but it is not always the case for split button.

    Attributes:
    ----------
    :param n: Integer. Optional. The button index. Default 0.
    """
    return self.items[n]

  def item(self, n):
    """
    Description:
    -----------
    Get a dedicated item in the dropdown component..

    Attributes:
    ----------
    :param n: Integer. The item index.
    """
    return self.items["options"][n]

  def add_button(self, value, category="primary", split=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param category:
    :param split:
    """

  def add_delimiter(self):
    """
    Description:
    ------------
    Add a delimiter item the dropdown
    """
    hr = self.page.web.std.layouts.hr()
    hr.attr["class"].initialise(["dropdown-divider"])
    hr.options.managed = False
    self.components.add(hr)
    self.items["options"].append(hr)
    return hr

  def add_item(self, component, url="#", active=False):
    """
    Description:
    ------------
    Add an item to the Dropdown list.

    Attributes:
    ----------
    :param component: HTML | String. The item to be added to the dropdown.
    :param url: String. Optional. The url path for the link.
    :param active: Boolean. Optional. The status of the option item.
    """
    link = self.page.web.std.link(component, url=url)
    link.attr["class"].initialise(["dropdown-item"])
    link.options.managed = False
    if active:
      link.attr["class"].add("active")
    item = HtmlList.Li(self.page, link)
    item.options.managed = False
    self.components.add(item)
    self.items["options"].append(item)
    return item


class BsModal(Component):
  css_classes = ["modal-dialog"]
  name = "Bootstrap Modal"
  str_repr = '''<div {attrs}>{sub_items}</div>'''
  dyn_repr = '''{sub_item}'''

  def add_title(self, header, content, prepend=False):
    pass

  def add_item(self, header, content, prepend=False):
    pass


class BsCarousel(Component):
  css_classes = ["carousel", "slide"]
  name = "Bootstrap Carousel"
  _option_cls = OptBsWidget.Carousel
  str_repr = '''
<div {attrs}>
  <div class="carousel-inner">
    {sub_items}
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#{htmlCode}" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#{htmlCode}" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
'''
  dyn_repr = '''
<div class="carousel-item {active}">
  <img src="{image}" class="d-block w-100" alt="...">
</div>'''

  _js__builder__ = '''var carousel = new bootstrap.Carousel(htmlObj, options)'''

  @property
  def options(self):
    """
    Description:
    -----------
    The component options.

    :rtype: OptBsWidget.Carousel
    """
    return super().options

  def add_item(self, image, active=False):
    self.items.append({"image": image, "active": ""})

  def write_item(self, item):
    return item


class BsNav(Component):
  css_classes = ["nav"]
  name = "Bootstrap Nav"
  str_repr = '''<nav {attrs}>{sub_items}</nav>'''
  dyn_repr = '''{sub_item}'''

  def add_item(self, component, url="#", active=False, disabled=False):
    """
    Description:
    ------------
    Add an item to the Nav list.

    https://getbootstrap.com/docs/5.1/components/navs-tabs/

    Attributes:
    ----------
    :param component: HTML | String. The item to be added to the Nav.
    :param url: String. Optional. The url path for the link.
    :param active: Boolean. Optional. The status of the option item.
    :param disabled: Boolean. Optional.
    """
    link = self.page.web.std.link(component, url=url)
    link.add_style(["nav-link"], clear_first=True)
    link.options.managed = False
    if active:
      link.attr["class"].add("active")
      link.aria.current = "page"
    self.components.add(link)
    self.items.append(link)
    return link

  def add_dropdown(self, component, url="#", active=False, disabled=False):
    pass


class BsTabs(BsNav):
  css_classes = ["nav", "nav-tabs"]
  name = "Bootstrap Tabs"


class BsPills(BsNav):
  css_classes = ["nav", "nav-pills"]
  name = "Bootstrap Pills"


class BsCard(Component):
  css_classes = ["card"]
  name = "Bootstrap Card"
  str_repr = '''<div {attrs}><div class="card-body">{sub_items}</div></div>'''
  dyn_repr = '''{sub_item}'''

  def add_header(self, value):
    title = self.page.web.std.div(value)
    title.attr["class"].initialise(["card-header"])
    title.options.managed = False
    self.items.insert(0, title)
    return title

  def add_footer(self, value):
    title = self.page.web.std.div(value)
    title.attr["class"].initialise(["card-footer"])
    title.options.managed = False
    self.items.insert(0, title)
    return title

  def add_title(self, value):
    title = self.page.web.std.tags.hn(5, value)
    title.attr["class"].initialise(["card-title"])
    title.options.managed = False
    self.items.append(title)
    return title

  def add_subtitle(self, value):
    title = self.page.web.std.tags.hn(6, value)
    title.attr["class"].initialise(["card-subtitle"])
    title.options.managed = False
    self.items.append(title)
    return title

  def add_text(self, value):
    pass

  def add_link(self, value, url="#"):
    link = self.page.web.std.link(value, url)
    link.attr["class"].initialise(["card-link"])
    link.options.managed = False
    self.items.append(link)
    return link

