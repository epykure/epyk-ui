"""
Module dedicated to produce Menus components
"""

from epyk.core import html


class Menus(object):
  def __init__(self, context):
    self.context = context

  def top(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Usage:
    ------
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
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
    self.context.register(col)
    return col

  def bottom(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Usage:
    ------
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.inReport = False
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

    Usage:
    ------
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
    menu_li, menu_title, menu_items, menu_divs = [], [], [], []
    for k in data:
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.inReport = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.context.rptObj.ui.list(menu_li, color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    for i, m in enumerate(menu_title):
      if isinstance(menu_items[i][0], list):
        grid = self.context.rptObj.ui.div([])
        for item in menu_items[i]:
          grid + self.context.rptObj.ui.col([m, *item], width=(None, "px")).css({"color": "white", "padding": "0 5px",
                        "display": 'inline-block', "vertical-align": 'top', "margin": '2px 0'})
        html_div = self.context.rptObj.ui.div(grid).css({"vertical-align": 'None'})
        html_div.attr["name"] = "divs_%s" % (html_list.htmlId)
        html_div.style.display = None
      else:
        html_div = self.context.rptObj.ui.div(
          self.context.rptObj.ui.grid([
            self.context.rptObj.ui.col([m, *menu_items[i]]).css({"color": "white", "padding": "0 5px"})]))
        html_div.attr["name"] = "divs_%s" % (html_list.htmlId)
        html_div.style.display = None
      menu_divs.append(html_div)
    html_list.click_items(
      [self.context.rptObj.js.getElementById(l.htmlId).setAttribute("data-select", "false") for l in html_list]
      + [self.context.rptObj.js.objects.dom("this").setAttribute("data-select", "true")])
    col = self.context.rptObj.ui.col([html_list, *menu_divs])
    col.css({"background-color": "#333", "margin": 0, "color": 'white'})
    return col

  def icons(self):
    pass

  def buttons(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
              htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    bs = rptObj.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
    bs[2].click([
      rptObj.js.alert(bs[2].dom.content)
    ])

    Attributes:
    ----------
    :param data:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    dfl_button_css = {"button_css": {"border-radius": 0, "border": "0px solid black"}}
    options = options or {}
    dfl_button_css.update(options)
    html_obj = html.HtmlButton.Buttons(self.context.rptObj, data or [], color, width, height, htmlCode, helper,
                                       dfl_button_css, profile)
    html_obj.css({"border": "1px solid %s" % html_obj._report.theme.greys[4], "padding": "2px"})
    self.context.register(html_obj)
    return html_obj

  def right(self):
    pass

  def left(self):
    pass
