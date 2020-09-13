#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.interfaces import Arguments


class Menus(object):
  def __init__(self, context):
    self.context = context

  def top(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      l = rptObj.ui.lists.list(["A", "B"])

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
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      menu_li.append(k["value"])
      menu_title.append(k.get("title"))
      menu_items.append(k.get("children", []))
    html_list = html.HtmlList.List(self.context.rptObj, menu_li, color, width, height, htmlCode,
                                   helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.context.rptObj.ui.div(
      self.context.rptObj.ui.grid([
        self.context.rptObj.ui.col([
          self.context.rptObj.ui.title("test", level=1),
          *menu_items[0]
        ]).css({"color": "white", "padding": "0 5px"})
      ])
    )

    col = self.context.rptObj.ui.col([html_list, html_div])
    col.css({"background-color": "#333", "position": "fixed", "margin": 0, "top": 0, "left": 0, "color": 'white'})
    return col

  def bottom(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      l = rptObj.ui.lists.list(["A", "B"])

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
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      if not isinstance(k, dict):
        k = {"value": k}
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.options.managed = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.context.rptObj.ui.list(menu_li, color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.context.rptObj.ui.div(
      self.context.rptObj.ui.grid([
        self.context.rptObj.ui.col([
          menu_title[0], *menu_items[0]]).css({"color": "white", "padding": "0 5px"})
      ])
    )
    html_div.style.display = None

    html_list.click_items([
      #self.context.rptObj.js.console.log(html_list),
      html_div.dom.toggle()
    ])

    col = self.context.rptObj.ui.col([html_div, html_list])
    col.css({"background-color": "#333",
             "position": "fixed", "bottom": 0, "left": 0,
             "margin": 0, "color": 'white'})
    return col

  def menu(self, data=None, position="bottom", color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      l = rptObj.ui.lists.list(["A", "B"])

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
    :param position: String. Optional.
    :param color: String. Optional. The font color in the component. Default inherit
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
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

    Usage::

      l = rptObj.ui.lists.list(["A", "B"])

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
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    records = []
    for k in data:
      if not isinstance(k, dict):
        records.append({'value': k})
      else:
        records.append(k)

    row = self.context.rptObj.ui.row(color, width=width, height=height, options=options or {}, profile=profile, position=position)
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
            link = self.context.rptObj.ui.link(**child)
            link.options.target = '_blank'
            li = self.context.rptObj.ui.lists.item(link)
            items.add(li)
          else:
            li = self.context.rptObj.ui.lists.item(child)
            items.add(li)
        row[i].add(items)
    return row

  def icons(self, data, width=("auto", ''), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.context.rptObj.theme.greys[1]
    div.style.css.margin = "2px 0 0 0"
    for d in data:
      div += self.context.rptObj.ui.icons.fluent(icon=d, text="", width=(15, 'px'), options={"icon_family": 'fluent'})
    return div

  def buttons(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      bs = rptObj.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
      bs[2].click([
      rptObj.js.alert(bs[2].dom.content)
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlButton.Buttons`

    Attributes:
    ----------
    :param data:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
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

  def right(self):
    pass

  def left(self):
    pass

  def divisor(self, data, divider=None, width=(100, '%'), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage::

      record = []
      rptObj.ui.menus.divisor(record)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlText.Text`

    Attributes:
    ----------
    :param divider:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    if divider is None:
      divider = self.context.rptObj.symbols.shapes.BLACK_RIGHT_POINTING_TRIANGLE
    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.texts = []
    for rec in data[:-1]:
      div.texts.append(self.context.rptObj.ui.text(rec).css({"display": 'inline-block'}))
      div += div.texts[-1]
      div += self.context.rptObj.ui.text(divider).css({"display": 'inline-block', 'margin': '0 5px', 'font-size': Defaults_css.font(-2)})
    div +=self.context.rptObj.ui.text(data[-1]).css({"display": 'inline-block'})
    return div

  def button(self, value, object, symbol=None, width=("auto", ''), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Usage::

      mb = rptObj.ui.menus.button("Value", rptObj.ui.button("sub button"))
      mb.item.click([rptObj.js.alert(mb.item.dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlButton.Button`

    Attributes:
    ----------
    :param value:
    :param object:
    :param symbol:
    :param width:
    :param height:
    :param options:
    :param profile:
    """

    div = self.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    div.item = object
    content = self.context.rptObj.ui.div(object, width=("auto", ''))
    content.style.css.display = None
    content.style.css.bottom = 0
    content.style.css.padding = 5
    content.style.css.background = self.context.rptObj.theme.greys[0]
    content.style.css.z_index = 5
    content.style.css.position = 'absolute'
    if symbol is None:
      symbol = self.context.rptObj.symbols.shapes.BLACK_DOWN_POINTING_SMALL_TRIANGLE
    but = self.context.rptObj.ui.button("%s %s" % (value, symbol),
                                        width=width, profile=profile)
    div += but
    div += content
    div.on("mouseover", [content.dom.css({"display": 'block'})])
    div.on("mouseout", [content.dom.css({"display": 'none'})])
    return div

  def toolbar(self, data, width=("auto", ''), height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param options:
    :param profile:
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

  def selections(self, data, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param attrs:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.Menu(self.context.rptObj, data, width, height,  attrs or {}, helper, options or {}, htmlCode, profile)
    return html_pr

  def contextual(self, records=None, width=(None, '%'), height=(None, 'px'), visible=False, options=None,
                 profile=None):
    """
    Description:
    ------------
    Set a bespoke Context Menu on an Item. This will create a popup on the page with action.
    This component is generic is need to be added to a component to work

    Usage::

      menu = rptObj.ui.contextual([{"text": 'text', 'event': 'alert("ok")'}])
      rptObj.ui.title("Test").attach_menu(menu)

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py

    Attributes:
    ----------
    :param records: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param visible: Optional.
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_menu = html.HtmlMenu.ContextMenu(self.context.rptObj, records or [], width, height, visible, options or {}, profile)
    return html_menu
