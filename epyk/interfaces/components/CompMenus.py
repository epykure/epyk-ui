#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List

from epyk.core import html
from epyk.interfaces import Arguments


class Menus:

  def __init__(self, ui):
    self.page = ui.page

  def top(self, data: List[dict] = None, color: str = None, width: Union[tuple, int] = (100, "%"),
          height: Union[tuple, int] = (30, 'px'), html_code: str = None,
          helper: str = None, options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlContainer.Div:
    """Add a menu item at the top of the page. The menu will be fixed on the page, always visible

    Usage::
      page.ui.menus.top([{"value": "Menu 1", 'children': ["Item 1", "Item 2"]},"Menu 1 2"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Grid`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    :param data: Optional. The top menu values
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"tab_width": 100}
    if options is not None:
      dflt_options.update(options)
    titles, panels = [], []
    for k in data:
      if not isinstance(k, dict):
        k = {"value": k}
      titles.append(self.page.ui.text(k["value"], width=(dflt_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.page.ui.col(width=(dflt_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.padding = "0 2px"
      col.style.css.background = self.page.theme.greys[0]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"text": c}
            link = self.page.ui.link(**c)
            link.style.css.display = 'block'
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(
      self.page, [], color, width, height, html_code, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.page.ui.div()
    html_div.style.css.background = self.page.theme.greys[1]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.margin_top = int(self.page.body.style.css.padding_top[:-2])
    html_div.style.css.top = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.page.ui.div([t, panels[i]], width=("auto", ''))
      cont.mouse([panels[i].dom.show(display_value="block").r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.page.body.style.css.padding_top is not None:
      self.page.body.style.css.padding_top = int(self.page.body.style.css.padding_top[:-2]) + height[0] + 5
    else:
      self.page.body.style.css.padding_top = height[0] + 5
    html.Html.set_component_skin(html_div)
    return html_div

  def bottom(self, data: List[dict] = None, color: str = None, width: Union[tuple, int] = (100, "%"),
             height: Union[tuple, int] = (30, 'px'), html_code: str = None,
             helper: str = None, options: dict = None, profile: Union[bool, dict] = None
             ) -> html.HtmlContainer.Div:
    """Add a menu item at the bottom of the page. The menu will be fixed on the page, always visible.

    Usage::
      page.ui.menus.bottom([{"value": "Menu 1", 'children': ["Item 1", "Item 2"]},"Menu 1 2"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    :param data: Optional. The top menu values
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"tab_width": 100}
    if options is not None:
      dflt_options.update(options)
    titles, panels = [], []
    for k in data:
      if not isinstance(k, dict):
        k = {"value": k}
      titles.append(self.page.ui.text(k["value"], width=(dflt_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.page.ui.col(width=(dflt_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.bottom = height[0]
      col.style.css.padding = "0 2px"
      col.style.css.background = self.page.theme.greys[0]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"text": c}
            link = self.page.ui.link(**c)
            link.style.css.display = 'block'
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(
      self.page, [], color, width, height, html_code, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.page.ui.div()
    html_div.style.css.background = self.page.theme.greys[1]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.bottom = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.page.ui.div([panels[i], t], width=("auto", ''))
      cont.mouse([panels[i].dom.show().r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.page.body.style.css.padding_bottom is not None:
      self.page.body.style.css.padding_bottom = int(self.page.body.style.css.padding_bottom[:-2]) + height[0] + 5
    else:
      self.page.body.style.css.padding_bottom = height[0] + 5
    html.Html.set_component_skin(html_div)
    return html_div

  def menu(self, data: list = None, color: str = None, width: Union[tuple, int] = (100, "%"),
           height: Union[tuple, int] = (None, 'px'), html_code: str = None,
           helper: str = None, options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlContainer.Col:
    """  

    Usage::
      page.ui.menus.menu([{"value": "File", "children": [{"url": "Test", "text": "Test"}]}])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Grid`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    :param data:
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    menu_li, menu_title, menu_items, menu_divs = [], [], [], []
    records = []
    for k in data:
      if not isinstance(k, dict):
        records.append({'value': k})
      else:
        records.append(k)
    for k in records:
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.page.ui.title(title_text, level=4)
        title_text.options.managed = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.page.ui.list(menu_li, color, width, height, html_code, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    for i, m in enumerate(menu_title):
      if menu_items[i] and isinstance(menu_items[i][0], list):
        grid = self.page.ui.div([])
        for item in menu_items[i]:
          grid.add(self.page.ui.col([m, *item], width=(None, "px")).css(
            {"padding": "0 5px", "display": 'inline-block', "vertical-align": 'top', "margin": '2px 0'}))
        html_div = self.page.ui.div(grid).css({"vertical-align": 'None'})
        html_div.attr["name"] = "divs_%s" % html_list.htmlCode
        html_div.style.display = None
      else:
        grid = self.page.ui.grid([self.page.ui.col([m, *menu_items[i]]).css({"padding": "0 5px"})])
        html_div = self.page.ui.div(grid)
        html_div.attr["name"] = "divs_%s" % html_list.htmlCode
        html_div.style.display = None
      menu_divs.append(html_div)
    if records:
      html_list.click_items(
        [self.page.js.getElementById(l.htmlCode).setAttribute("data-select", "false") for l in html_list]
        + [self.page.js.objects.dom("this").setAttribute("data-select", "true")])
    col = self.page.ui.col([html_list, *menu_divs])
    col.css({"background-color": self.page.theme.greys[0], "margin": 0})
    html.Html.set_component_skin(col)
    return col

  def bar(self, data=None, align: str = "left", position: str = "top", color: str = None,
          width: Union[tuple, int] = (350, "px"), height: Union[tuple, int] = (None, 'px'), options: dict = None,
          profile: Union[bool, dict] = None):
    """  

    Usage::
      page.ui.menus.bar([{"value": "File", "children": [{"url": "Test", "text": "Test"}]}])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Grid`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    :param data:
    :param align: Optional. A string with the horizontal position of the component
    :param position: Optional. A string with the vertical position of the component
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    records = []
    dfl_options = {"target": '_self'}
    if options is not None:
      dfl_options.update(options)
    for k in data:
      if not isinstance(k, dict):
        records.append({'value': k})
      else:
        records.append(k)
    row = self.page.ui.row(
      color, width=width, height=height, options=dfl_options, profile=profile, position=position)
    for _ in range(len(records)):
      col = self.page.ui.col(align=align, position=position)
      col.options.responsive = False
      row.add(col)
    for i, k in enumerate(records):
      title_text = k.get("value")
      if title_text is not None:
        title_text = self.page.ui.titles.section(title_text, align=align)
        title_text.style.css.margin_top = 0
        row[i].add(title_text)
      if k.get("children", []):
        items = self.page.ui.list()
        for child in k.get("children", []):
          if isinstance(child, dict):
            if 'target' not in child:
              child['options'] = {'target': dfl_options['target']}
            else:
              child['options'] = {'target': child['target']}
              del child['target']
            link = self.page.ui.link(**child)
            link.style.css.white_space = "nowrap"
            li = self.page.ui.lists.item(link)
            items.add(li)
          else:
            li = self.page.ui.lists.item(child)
            items.add(li)
        row[i].add(items)
    html.Html.set_component_skin(row)
    return row

  def icons(self, data: List[Union[str, dict]] = None, width=(100, '%'), height: Union[tuple, int] = (None, 'px'), align: str = "center",
            html_code: str = None, options: dict = None, profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """Add a menu bar with font awesome icons.

    Usage::
      icons = page.ui.menus.icons(
        ["bi-1-circle-fill", "bi-search-heart-fill", "bi-x-circle-fill"], options={"icon_family": "bootstrap-icons"})

    :param data: Optional. Parameter bar icons
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    dfl_options = {"margin-right": 5}
    if options is not None:
      dfl_options.update(options)
    div = self.page.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    div.style.css.text_align = "right"
    icons = []
    if data:
      for i, d in enumerate(data):
        if isinstance(d, dict):
          if "width" not in d:
            d["width"] = (15, 'px')
          if "options" not in d:
            d["options"] = {}
          if "html_code" not in d:
            d["html_code"] = "%s_%s" % (html_code, i)
          if "icon_family" not in d["options"]:
            d["options"]["icon_family"] = dfl_options.get("icon_family", self.page.icons.family)
          icons.append(self.page.ui.icons.fluent(**d))
        else:
          icon_code = None if not html_code else "%s_%s" % (html_code, i)
          icons.append(self.page.ui.icons.fluent(
            icon=d, text="", width=(15, 'px'), html_code=icon_code, options={
              "icon_family": dfl_options.get("icon_family", self.page.icons.family)}))
        icons[-1].style.css.margin = "0 %spx 0 0" % dfl_options["margin-right"]
        div.add(icons[-1])
    html.Html.set_component_skin(div)
    div.icons = icons
    return div

  def buttons(self, data: list = None, color: str = None, width: Union[tuple, int] = ("auto", ""),
              height: Union[tuple, int] = (None, 'px'), html_code: str = None,
              helper: str = None, options: dict = None, profile: Union[bool, dict] = None
              ) -> html.HtmlButton.Buttons:
    """  

    Usage::
      bs = page.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
      bs[2].click([page.js.alert(bs[2].dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Buttons`

    :param data:
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlButton.Buttons(
      self.page, data or [], color, width, height, html_code, helper, options or {}, profile)
    component.css({"border": "1px solid %s" % component.page.theme.greys[4], "padding": "2px", "min-height": "40px"})
    html.Html.set_component_skin(component)
    return component

  def images(self, data: list = None, path: str = None, width: Union[tuple, int] = (100, '%'),
             height: Union[tuple, int] = (None, 'px'), align: str = "center",
             options: dict = None, profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """  

    Usage::
      page.ui.menus.images(["https://jupyter.org/favicon.ico", "https://codepen.io//favicon.ico"])

    :param path:
    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The text-align property within this component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    dfl_options = {"margin-left": 20, "margin-right": 20, 'image-width': 50}
    if options is not None:
      dfl_options.update(options)
    div = self.page.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    if data is not None:
      for d in data:
        img_attrs = {'width': (dfl_options['image-width'], 'px')}
        if not isinstance(d, dict):
          img_attrs['image'] = d
        else:
          img_attrs.update(d)
        if path is not None:
          img_attrs['path'] = path
        url = None
        if 'url' in img_attrs:
          url = img_attrs['url']
          del img_attrs['url']

        img = self.page.ui.img(**img_attrs)
        if url is not None:
          img.goto(url)
        img.style.css.display = 'inline-block'
        div.add(img)
        div[-1].style.css.margin_right = dfl_options["margin-right"]
    html.Html.set_component_skin(div)
    return div

  def right(self, data=None, color: str = None, width: Union[tuple, int] = (100, "%"),
            height: Union[tuple, int] = (30, 'px'), html_code: str = None,
            helper: str = None, options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlContainer.Div:
    """  

    Usage::
      page.ui.lists.

    :param data:
    :param color:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    :param helper:
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"tab_width": 100}
    if options is not None:
      dfl_options.update(options)
    titles, panels = [], []
    for k in data:
      if not isinstance(k, dict):
        k = {"value": k}
      titles.append(self.page.ui.text(k["value"], width=(dfl_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.page.ui.div(width=(dfl_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.bottom = height[0]
      col.style.css.padding = "0 2px"
      col.style.css.background = self.page.theme.greys[1]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"value": c}
            link = self.page.ui.link(*c)
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(
      self.page, [], color, width, height, html_code, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.page.ui.div()
    html_div.style.css.background = self.page.theme.greys[0]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.bottom = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.page.ui.table([panels[i], t], width=("auto", ''))
      cont.mouse([panels[i].dom.show().r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.page.body.style.css.padding_bottom is not None:
      self.page.body.style.css.padding_bottom = int(self.page.body.style.css.padding_bottom[:-2]) + height[0] + 5
    else:
      self.page.body.style.css.padding_bottom = height[0] + 5
    html.Html.set_component_skin(html_div)
    return html_div

  def divisor(self, data, divider: bool = None, width: Union[tuple, int] = (100, '%'),
              height: Union[tuple, int] = (None, 'px'), options: dict = None,
              profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """Add list of items separated by a symbol (default BLACK_RIGHT_POINTING_TRIANGLE).
    The components will be based on Links.

    Usage::
      page.ui.menus.divisor([])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlText.link`

    :param data:
    :param divider: symbols.shape | String. The symbol between the links.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if divider is None:
      divider = self.page.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    div.texts = []
    for rec in data[:-1]:
      if not isinstance(rec, dict):
        rec = {"text": rec}
      div.texts.append(self.page.ui.link(*rec).css({"display": 'inline-block'}))
      div += div.texts[-1]
      div += self.page.ui.text(divider).css({
        "display": 'inline-block', 'margin': '0 5px', 'font-size': self.page.body.style.globals.font.normal(-2)})
    rec = {"text": data[-1]} if not isinstance(data[-1], dict) else data[-1]
    div += self.page.ui.link(*rec).css({"display": 'inline-block'})
    html.Html.set_component_skin(div)
    return div

  def button(self, value, components: Union[html.Html.Html, List[html.Html.Html]], symbol: str = None,
             width: Union[tuple, int] = ("auto", ''), height: Union[tuple, int] = (None, 'px'), options: dict = None,
             profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """  

    Usage::
      mb = page.ui.menus.button("Value", page.ui.button("sub button"))
      mb.items[0].click([page.js.alert(mb.items[0].dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlButton.Button`

    :param value:
    :param components:
    :param symbol:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    div.items = components if isinstance(components, list) else [components]
    content = self.page.ui.div(div.items, width=("auto", ''))
    content.style.css.display = None
    content.style.css.padding = 5
    content.style.css.background = self.page.theme.greys[0]
    content.style.css.z_index = 5
    content.style.css.position = 'absolute'
    if symbol is None:
      symbol = self.page.symbols.shapes.BLACK_DOWN_POINTING_SMALL_TRIANGLE
    but = self.page.ui.button("%s %s" % (value, symbol), width=width, profile=profile)
    div += but
    div += content
    div.on("mouseover", [content.dom.css({"display": 'block'}).r])
    div.on("mouseout", [content.dom.css({"display": 'none'}).r])
    html.Html.set_component_skin(div)
    return div

  def toolbar(self, data: list = None, width: Union[tuple, int] = ("auto", ''),
              height: Union[tuple, int] = (None, 'px'), options: dict = None,
              profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """  

    Usage::
      tb = page.ui.menus.toolbar(["fas fa-paint-brush", "fas fa-code"])
      tb[1].link.val = 4589
      tb[1].tooltip("This is a tooltip")
      tb[0].style.css.color = 'red'

      # with other icon families
      page.ui.menus.toolbar(["face"], options={"icon_family": 'material-design-icons'})
      page.ui.menus.toolbar(["Mail", "AdminALogo32"], options={"icon_family": 'office-ui-fabric-core'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Badge`

    :param data: Optional. The list of icons
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    options = options or {}
    div = self.page.ui.div(width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.page.theme.greys[1]
    div.style.css.margin = "2px 0 0 0"
    if data is not None:
      for d in data:
        div += self.page.ui.images.badge(
          icon=d, text="", width=(15, 'px'), options={
            "badge_position": 'right', "icon_family": options.get("icon_family")})
        div.style.css.padding = "0 2px 2px 2px"
        div[-1].style.clear(no_default=True)
        div[-1].attr["class"].add("badge")
        div[-1].style.css.width = 25
        div[-1].style.css.padding = 0
        div[-1].style.css.height = False
        div[-1].style.css.text_align = 'center'
        div[-1].style.css.cursor = 'pointer'
        div[-1].style.css.margin = 0
        div[-1].icon.style.css.float = None
    html.Html.set_component_skin(div)
    return div

  def selections(self, data, width=(150, 'px'), height=('auto', ''), html_code: str = None,
                 helper: str = None, options: dict = None, profile: Union[bool, dict] = None) -> html.HtmlEvent.Menu:
    """Menu using Jquery UI external module.

    Usage::
        page.ui.menus.selections(["Item 1", "Item 2"])
        page.ui.menus.selections([
          {'value': "fas fa-exclamation-triangle", 'items': [
            {"value": 'value 1'}, {"value": 'value 2'}, {"value": 'value 3'}]},
            "fas fa-exclamation-triangle"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

    `jqueryui <https://jqueryui.com/menu/>`_

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    new_data = []
    for d in data:
      if not isinstance(d, dict):
        new_data.append({"value": d})
      else:
        new_data.append(d)
    html_pr = html.HtmlEvent.Menu(
      self.page, new_data, width, height, helper, options or {}, html_code, profile)
    html.Html.set_component_skin(html_pr)
    return html_pr

  def contextual(self, record: list = None, width: Union[tuple, int] = (None, '%'),
                 height: Union[tuple, int] = (None, 'px'),
                 html_code: str = None, visible: bool = False, options: dict = None,
                 profile: Union[bool, dict] = None) -> html.HtmlMenu.ContextMenu:
    """Set a bespoke Context Menu on an Item. This will create a popup on the page with action.
    This component is generic is need to be added to a component to work.

    Usage::
      menu = page.ui.contextual([{"text": 'text', 'event': 'alert("ok")'}])
      page.ui.title("Test").attach_menu(menu)

    `Templates <https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py>`_

    :param record: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param visible: Optional.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_menu = html.HtmlMenu.ContextMenu(
      self.page, record or [], width, height, visible, html_code, options or {}, profile)
    html.Html.set_component_skin(html_menu)
    return html_menu

  def pills(self, data: List = None, width: Union[tuple, int] = (100, '%'), height: Union[tuple, int] = (50, 'px'),
            html_code: str = None, helper: str = None,
            options: dict = None, profile: Union[bool, dict] = False) -> html.HtmlContainer.Div:
    """  

    Usage::
      page.ui.pills.

    :param data: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    container = self.page.ui.div(
      width=width, height=height, html_code=html_code, options=options, helper=helper, profile=profile)
    if data is not None:
      for d in data:
        pill = self.page.ui.div(d, width=("auto", ""))
        pill.style.css.border = "1px solid %s" % self.page.theme.greys[4]
        pill.style.css.border_radius = 10
        pill.style.css.cursor = "pointer"
        pill.style.css.padding = "2px 10px"
        pill.style.css.margin_right = 5
        pill.style.add_classes.div.color_hover()
        container.add(pill)
    container.style.css.overflow_x = "auto"
    container.style.css.white_space = "nowrap"
    container.style.css.display = "inline-block"
    container.style.css.margin_top = 10
    container.style.css.margin_bottom = 10
    html.Html.set_component_skin(container)
    return container
