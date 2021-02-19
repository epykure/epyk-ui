#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.interfaces import Arguments


class Menus(object):

  def __init__(self, context):
    self.context = context

  def top(self, data=None, color=None, width=(100, "%"), height=(30, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a menu item at the top of the page.
    The menu will be fixed on the page, always visible

    Usage:
    -----

      l = page.ui.lists.list(["A", "B"])
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

    Attributes:
    ----------
    :param data:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
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
      titles.append(self.context.rptObj.ui.text(k["value"], width=(dflt_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.context.rptObj.ui.col(width=(dflt_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.padding = "0 2px"
      col.style.css.background = self.context.rptObj.theme.greys[0]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"text": c}
            link = self.context.rptObj.ui.link(**c)
            link.style.css.display = 'block'
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(self.context.rptObj, [], color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})

    html_div = self.context.rptObj.ui.div()
    html_div.style.css.background = self.context.rptObj.theme.greys[1]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.margin_top = int(self.context.rptObj.body.style.css.padding_top[:-2])
    html_div.style.css.top = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.context.rptObj.ui.div([t, panels[i]], width=("auto", ''))
      cont.mouse([panels[i].dom.show(display_value="block").r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.context.rptObj.body.style.css.padding_top is not None:
      self.context.rptObj.body.style.css.padding_top = int(self.context.rptObj.body.style.css.padding_top[:-2]) + height[0] + 5
    else:
      self.context.rptObj.body.style.css.padding_top = height[0] + 5
    return html_div

  def bottom(self, data=None, color=None, width=(100, "%"), height=(30, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a menu item at the bottom of the page.
    The menu will be fixed on the page, always visible.

    Usage:
    -----

      l = page.ui.lists.list(["A", "B"])
      page.ui.menus.top([{"value": "Menu 1", 'children': ["Item 1", "Item 2"]},"Menu 1 2"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    Attributes:
    ----------
    :param data:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
      titles.append(self.context.rptObj.ui.text(k["value"], width=(dflt_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.context.rptObj.ui.col(width=(dflt_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.bottom = height[0]
      col.style.css.padding = "0 2px"
      col.style.css.background = self.context.rptObj.theme.greys[0]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"text": c}
            link = self.context.rptObj.ui.link(**c)
            link.style.css.display = 'block'
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(self.context.rptObj, [], color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})

    html_div = self.context.rptObj.ui.div()
    html_div.style.css.background = self.context.rptObj.theme.greys[1]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.bottom = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.context.rptObj.ui.div([panels[i], t], width=("auto", ''))
      cont.mouse([panels[i].dom.show().r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.context.rptObj.body.style.css.padding_bottom is not None:
      self.context.rptObj.body.style.css.padding_bottom = int(self.context.rptObj.body.style.css.padding_bottom[:-2]) + \
                                                       height[0] + 5
    else:
      self.context.rptObj.body.style.css.padding_bottom = height[0] + 5
    return html_div

  def menu(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      l = page.ui.lists.list(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Grid`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    Attributes:
    ----------
    :param data:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.options.managed = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.context.rptObj.ui.list(menu_li, color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    for i, m in enumerate(menu_title):
      if menu_items[i] and isinstance(menu_items[i][0], list):
        grid = self.context.rptObj.ui.div([])
        for item in menu_items[i]:
          grid.add(self.context.rptObj.ui.col([m, *item], width=(None, "px")).css({"padding": "0 5px",
                        "display": 'inline-block', "vertical-align": 'top', "margin": '2px 0'}))
        html_div = self.context.rptObj.ui.div(grid).css({"vertical-align": 'None'})
        html_div.attr["name"] = "divs_%s" % (html_list.htmlCode)
        html_div.style.display = None
      else:
        grid = self.context.rptObj.ui.grid([self.context.rptObj.ui.col([m, *menu_items[i]]).css({"padding": "0 5px"})])
        html_div = self.context.rptObj.ui.div(grid)
        html_div.attr["name"] = "divs_%s" % (html_list.htmlCode)
        html_div.style.display = None
      menu_divs.append(html_div)
    if records is None:
      html_list.click_items(
        [self.context.rptObj.js.getElementById(l.htmlCode).setAttribute("data-select", "false") for l in html_list]
        + [self.context.rptObj.js.objects.dom("this").setAttribute("data-select", "true")])
    col = self.context.rptObj.ui.col([html_list, *menu_divs])
    col.css({"background-color": self.context.rptObj.theme.greys[0], "margin": 0})
    return col

  def bar(self, data=None, align="left", position="top", color=None, width=(350, "px"), height=(None, 'px'),
          options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      l = page.ui.lists.list(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlContainer.Grid`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    Attributes:
    ----------
    :param data:
    :param align: String. Optional. A string with the horizontal position of the component
    :param position: String. Optional. A string with the vertical position of the component
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    records = []
    dflt_options = {"target": '_self'}
    if options is not None:
      dflt_options.update(options)
    for k in data:
      if not isinstance(k, dict):
        records.append({'value': k})
      else:
        records.append(k)

    row = self.context.rptObj.ui.row(color, width=width, height=height, options=dflt_options, profile=profile, position=position)
    for _ in range(len(records)):
      col = self.context.rptObj.ui.col(align=align, position=position)
      col.options.responsive = False
      row.add(col)
    for i, k in enumerate(records):
      title_text = k.get("value")
      if title_text is not None:
        title_text = self.context.rptObj.ui.titles.section(title_text, align=align)
        title_text.style.css.margin_top = 0
        row[i].add(title_text)
      if k.get("children", []):
        items = self.context.rptObj.ui.list()
        for child in k.get("children", []):
          if isinstance(child, dict):
            if 'target' not in child:
              child['options'] = {'target': dflt_options['target']}
            else:
              child['options'] = {'target': child['target']}
              del child['target']
            link = self.context.rptObj.ui.link(**child)
            link.style.css.white_space = "nowrap"
            li = self.context.rptObj.ui.lists.item(link)
            items.add(li)
          else:
            li = self.context.rptObj.ui.lists.item(child)
            items.add(li)
        row[i].add(items)
    return row

  def icons(self, data, width=(100, '%'), height=(None, 'px'), align="center", options=None, profile=False):
    """
    Description:
    ------------
    Add a menu bar with font awesome icons.

    Usage:
    -----


    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align: String. Optional. A string with the horizontal position of the component
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    dflt_options = {"margin-right": 5}
    if options is not None:
      dflt_options.update(options)
    div = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    for d in data:
      div.add(self.context.rptObj.ui.icons.fluent(icon=d, text="", width=(15, 'px'), options={"icon_family": 'fluent'}))
      div[-1].style.css.margin_right = dflt_options["margin-right"]
    return div

  def buttons(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      bs = page.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
      bs[2].click([
        page.js.alert(bs[2].dom.content)
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Buttons`

    Attributes:
    ----------
    :param data:
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_button_css = {"button_css": {"border-radius": 0, "border": "0px solid black"}}
    options = options or {}
    dfl_button_css.update(options)
    html_obj = html.HtmlButton.Buttons(self.context.rptObj, data or [], color, width, height, htmlCode, helper,
                                       dfl_button_css, profile)
    html_obj.css({"border": "1px solid %s" % html_obj._report.theme.greys[4], "padding": "2px"})
    return html_obj

  def images(self, data, path=None, width=(100, '%'), height=(None, 'px'), align="center", options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.menus.images(["https://jupyter.org/favicon.ico", "https://codepen.io//favicon.ico"])

    Attributes:
    ----------
    :param path:
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param align:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    dflt_options = {"margin-left": 20, "margin-right": 20, 'image-width': 50}
    if options is not None:
      dflt_options.update(options)
    div = self.context.rptObj.ui.div(width=width, height=height, align=align, options=options, profile=profile)
    for d in data:
      img_attrs = {'width': (dflt_options['image-width'], 'px')}
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
      img = self.context.rptObj.ui.img(**img_attrs)
      if url is not None:
        img.goto(url)
      img.style.css.display = 'inline-block'
      div.add(img)
      div[-1].style.css.margin_right = dflt_options["margin-right"]
    return div

  def right(self, data=None, color=None, width=(100, "%"), height=(30, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param color:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
      titles.append(self.context.rptObj.ui.text(k["value"], width=(dflt_options['tab_width'], 'px'), align="center"))
      children = k.get("children", [])
      col = self.context.rptObj.ui.div(width=(dflt_options['tab_width'], 'px'))
      col.style.css.display = None
      col.style.css.bottom = height[0]
      col.style.css.padding = "0 2px"
      col.style.css.background = self.context.rptObj.theme.greys[1]
      col.style.css.position = "absolute"
      if children:
        items = []
        for c in children:
          if hasattr(c, 'options'):
            items.append(c)
          else:
            if not isinstance(c, dict):
              c = {"value": c}
            link = self.context.rptObj.ui.link(*c)
            items.append(link)
        col.add(items)
      panels.append(col)
    html_list = html.HtmlList.List(self.context.rptObj, [], color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})

    html_div = self.context.rptObj.ui.div()
    html_div.style.css.background = self.context.rptObj.theme.greys[0]
    html_div.css({"position": "fixed", "margin": 0, "left": 0})
    html_div.style.css.bottom = 0
    html_div.panels = panels
    html_div.titles = titles
    for i, t in enumerate(titles):
      cont = self.context.rptObj.ui.table([panels[i], t], width=("auto", ''))
      cont.mouse([panels[i].dom.show().r], [panels[i].dom.hide().r])
      html_div.add(cont)
    html_div.style.css.line_height = height[0]
    if self.context.rptObj.body.style.css.padding_bottom is not None:
      self.context.rptObj.body.style.css.padding_bottom = int(self.context.rptObj.body.style.css.padding_bottom[:-2]) + \
                                                       height[0] + 5
    else:
      self.context.rptObj.body.style.css.padding_bottom = height[0] + 5
    return html_div

  def left(self):
    pass

  def divisor(self, data, divider=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------
    Add list of items separated by a symbol (default BLACK_RIGHT_POINTING_TRIANGLE).
    The components will be based on Links.

    Usage:
    -----

      record = []
      page.ui.menus.divisor(record)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlText.link`

    Attributes:
    ----------
    :param divider: symbols.shape | String. The symbol between the links.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    if divider is None:
      divider = self.context.rptObj.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.texts = []
    for rec in data[:-1]:
      if not isinstance(rec, dict):
        rec = {"text": rec}
      div.texts.append(self.context.rptObj.ui.link(*rec).css({"display": 'inline-block'}))
      div += div.texts[-1]
      div += self.context.rptObj.ui.text(divider).css({"display": 'inline-block', 'margin': '0 5px', 'font-size': Defaults_css.font(-2)})

    rec = {"text": data[-1]} if not isinstance(data[-1], dict) else data[-1]
    div += self.context.rptObj.ui.link(*rec).css({"display": 'inline-block'})
    return div

  def button(self, value, components, symbol=None, width=("auto", ''), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

      mb = page.ui.menus.button("Value", page.ui.button("sub button"))
      mb.items[0].click([page.js.alert(mb.items[0].dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlButton.Button`

    Attributes:
    ----------
    :param value:
    :param components:
    :param symbol:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.items = components if isinstance(components, list) else [components]
    content = self.context.rptObj.ui.div(div.items, width=("auto", ''))
    content.style.css.display = None
    content.style.css.padding = 5
    content.style.css.background = self.context.rptObj.theme.greys[0]
    content.style.css.z_index = 5
    content.style.css.position = 'absolute'
    if symbol is None:
      symbol = self.context.rptObj.symbols.shapes.BLACK_DOWN_POINTING_SMALL_TRIANGLE
    but = self.context.rptObj.ui.button("%s %s" % (value, symbol),width=width, profile=profile)
    div += but
    div += content
    div.on("mouseover", [content.dom.css({"display": 'block'}).r])
    div.on("mouseout", [content.dom.css({"display": 'none'}).r])
    return div

  def toolbar(self, data, width=("auto", ''), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----

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

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    options = options or {}
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.context.rptObj.theme.greys[1]
    div.style.css.margin = "2px 0 0 0"
    for d in data:
      div += self.context.rptObj.ui.images.badge(icon=d, text="", width=(15, 'px'), options={"badge_position": 'right', "icon_family": options.get("icon_family")})
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
    return div

  def selections(self, data, width=(150, 'px'), height=('auto', ''), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Menu using Jquery UI external module.

    Usage:
    -----

        page.ui.menus.selections(["Item 1", "Item 2"])

        page.ui.menus.selections([
          {'value': "fas fa-exclamation-triangle", 'items': [
            {"value": 'value 1'},
            {"value": 'value 2'},
            {"value": 'value 3'},
          ]},
            "fas fa-exclamation-triangle"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

    Related Pages:

      https://jqueryui.com/menu/

    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    new_data = []
    for d in data:
      if not isinstance(d, dict):
        new_data.append({"value": d})
      else:
        new_data.append(d)
    html_pr = html.HtmlEvent.Menu(self.context.rptObj, new_data, width, height, helper, options or {}, htmlCode, profile)
    return html_pr

  def contextual(self, record=None, width=(None, '%'), height=(None, 'px'), visible=False, options=None, profile=None):
    """
    Description:
    ------------
    Set a bespoke Context Menu on an Item. This will create a popup on the page with action.
    This component is generic is need to be added to a component to work.

    Usage:
    -----

      menu = page.ui.contextual([{"text": 'text', 'event': 'alert("ok")'}])
      page.ui.title("Test").attach_menu(menu)

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py

    Attributes:
    ----------
    :param record: Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param visible: Boolean. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_menu = html.HtmlMenu.ContextMenu(self.context.rptObj, record or [], width, height, visible, options or {}, profile)
    return html_menu

  def pills(self, data, width=(100, '%'), height=(50, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param data:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    container = self.context.rptObj.ui.div(width=width, height=height, htmlCode=htmlCode, options=options, helper=helper, profile=profile)
    for d in data:
      pill = self.context.rptObj.ui.div(d, width=("auto", ""))
      pill.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[4]
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
    return container
