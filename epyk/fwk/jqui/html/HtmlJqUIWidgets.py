

from epyk.core.html.Html import Component
from epyk.core.js.packages import JsQuery
from epyk.fwk.jqui.css import JqStyleWidget
from epyk.fwk.jqui.options import OptJqWiidgets
from epyk.fwk.jqui.js import JsJqWidgets


class JqAccordion(Component):
  name = "Jquery Accordion"
  _option_cls = OptJqWiidgets.OptAccordion

  str_repr = '''<div {attrs}>{sub_items}</div>'''
  dyn_repr = '''{header}{content}'''
  _js__builder__ = '''%s.accordion(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  @property
  def var(self):
    """   Return the calendar javaScript object reference after the builder.
    """
    return JsQuery.decorate_var("#%s" % self.htmlCode)

  @property
  def options(self) -> OptJqWiidgets.OptAccordion:
    """   The component options.

    Related Pages:

      https://api.jqueryui.com/accordion/

    :rtype: OptJqWiidgets.OptAccordion
    """
    return super().options

  @property
  def js(self) -> JsJqWidgets.Accordion:
    """   Javascript module of the Accordion component.

    Related Pages:

      https://api.jqueryui.com/accordion/

    :rtype: JsJqWidgets.Accordion
    """
    if self._js is None:
      self._js = JsJqWidgets.Accordion(component=self, js_code=self.var, page=self.page)
    return self._js

  @property
  def style(self) -> JqStyleWidget.Accordion:
    """  
    Property to the CSS Style of the component.

    :rtype: JqStyleWidget.Accordion
    """
    if self._styleObj is None:
      self._styleObj = JqStyleWidget.Accordion(self)
    return self._styleObj

  def header(self, n):
    """   Get a dedicated header component.
 
    :param n: Integer. The header index.
    """
    return self.items[n]["header"]

  def panel(self, n: int):
    """   Get a dedicated panel component.
 
    :param n: Integer. The panel index.
    """
    return self.items[n]["content"]

  def add_section(self, header, content, prepend=False):
    """   Add a new section to the accordion component.
 
    :param header: String | Component. The tab title.
    :param content: String | Component. The tab panel.
    :param prepend: Boolean. Optional. The position of the tab.
    """
    if not hasattr(header, "options"):
      header = self.page.web.std.div(header)
      header.attr["class"].clear()
    header.options.managed = False
    if not hasattr(content, "options"):
      content = self.page.web.std.div(content)
      content.attr["class"].clear()
    content.options.managed = False
    section = {"header": header, "content": content}
    if prepend:
      self.items.insert(0, section)
    else:
      self.items.append(section)
    return section

  def write_item(self, item):
    """   
 
    :param item:
    """
    return {"header": item["header"].html(), "content": item["content"].html()}

  def add_item(self, component):
    raise ValueError("Not available for this class")


class JqTabs(Component):
  name = "Jquery Tabs"
  _option_cls = OptJqWiidgets.OptTabs

  str_repr = '''<div {attrs}><ul>{sub_items_tabs}</ul>{sub_items_panels}</div>'''
  _js__builder__ = '''%s.tabs(options)''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  @property
  def var(self):
    """   Return the calendar javaScript object reference after the builder.
    """
    return JsQuery.decorate_var("#%s" % self.htmlCode)

  @property
  def style(self) -> JqStyleWidget.Accordion:
    """  
    Property to the CSS Style of the component.

    :rtype: JqStyleWidget.Accordion
    """
    if self._styleObj is None:
      self._styleObj = JqStyleWidget.Accordion(self)
    return self._styleObj

  @property
  def options(self) -> OptJqWiidgets.OptTabs:
    """   The component options.

    Related Pages:

      https://api.jqueryui.com/tabs/

    :rtype: OptJqWiidgets.OptTabs
    """
    return super().options

  @property
  def js(self) -> JsJqWidgets.Tabs:
    """   Javascript module of the Tabs component.

    Related Pages:

      https://api.jqueryui.com/tabs/

    :rtype: JsJqWidgets.Tabs
    """
    if self._js is None:
      self._js = JsJqWidgets.Tabs(component=self, js_code=self.var, page=self.page)
    return self._js

  def tab(self, n):
    """   Get a dedicated tab component.
 
    :param n: Integer. The tab index.
    """
    return self.items[n]["header"]

  def panel(self, n: int):
    """   Get a dedicated panel component.
 
    :param n: Integer. The panel index.
    """
    return self.items[n]["content"]

  def add_panel(self, header, content, prepend=False):
    """   Add a new panel to the multi tabs component.
 
    :param header: String | Component. The tab title.
    :param content: String | Component. The tab panel.
    :param prepend: Boolean. Optional. The position of the tab.
    """
    if not hasattr(header, "options"):
      header = self.page.web.std.div(header)
      header.attr["class"].clear()
    header.options.managed = False
    if not hasattr(content, "options"):
      content = self.page.web.std.div(content)
      content.attr["class"].clear()
    content.options.managed = False
    link = self.page.web.std.link(header, url="#%s" % content.htmlCode)
    link.attr["class"].clear()
    link.options.managed = False
    panel = {"header": link, "content": content}
    if prepend:
      self.items.insert(0, panel)
    else:
      self.items.append(panel)
    return panel

  def write_values(self):
    """   

    """
    tabs, panels = [], []
    for item in self.items:
      tabs.append('<li>%s</li>' % item["header"].html())
      panels.append(item["content"].html())
    return {"sub_items_tabs": "".join(tabs), "sub_items_panels": "".join(panels)}

  def add_item(self, component):
    raise ValueError("Not available for this class")
