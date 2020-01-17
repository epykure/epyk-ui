"""
Module dedicated to produce Menus components
"""

from epyk.core import html


class Menus(object):
  def __init__(self, context):
    self.context = context

  def top(self, data=None, size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Example
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
    size = self.context._size(size)
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      menu_li.append(k["value"])
      menu_title.append(k.get("title"))
      menu_items.append(k.get("children", []))
    html_list = html.HtmlList.List(self.context.rptObj, menu_li, size, color, width, height, htmlCode,
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

  def bottom(self, data=None, size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Example
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
    size = self.context._size(size)
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.inReport = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.context.rptObj.ui.list(menu_li, size, color, width, height, htmlCode, helper, options or {}, profile)
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

  def menu(self, data=None, position="bottom", size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Example
    l = rptObj.ui.lists.list(["A", "B"])

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
    http://astronautweb.co/snippet/font-awesome/
    """
    size = self.context._size(size)
    menu_li, menu_title, menu_items = [], [], []
    for k in data:
      menu_li.append(k["value"])
      title_text = k.get("title")
      if title_text is not None:
        title_text = self.context.rptObj.ui.title(title_text, level=4)
        title_text.inReport = False
      menu_title.append(title_text)
      menu_items.append(k.get("children", []))
    html_list = self.context.rptObj.ui.list(menu_li, size, color, width, height, htmlCode, helper, options or {}, profile)
    html_list.css({"list-style": 'none'})
    html_div = self.context.rptObj.ui.div(
      self.context.rptObj.ui.grid([
        self.context.rptObj.ui.col([
          menu_title[0], *menu_items[0]]).css({"color": "white", "padding": "0 5px"})
      ])
    )
    html_div.style.display = None

    html_list.click_items(
      [self.context.rptObj.js.getElementById(l.htmlId).setAttribute("data-select", "toto") for l in html_list]
      + [
      self.context.rptObj.js.objects.dom("this").setAttribute("data-select", "true"),
      self.context.rptObj.js.console.log(html_list.dom.val),
      html_div.dom.toggle()
    ])

    col = self.context.rptObj.ui.col([html_list, html_div])
    col.css({"background-color": "#333", "margin": 0, "color": 'white'})
    return col

  def icons(self):
    pass

  def buttons(self, data=None, size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
              htmlCode=None, helper=None, options=None, profile=None):
    """

    Example
    bs = rptObj.ui.buttons.buttons(["Button", "Button 2", "Button 3"])
    bs[2].click([
      rptObj.js.alert(bs[2].dom.content)
    ])

    :param data:
    :param size:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    :return:
    """
    dfl_button_css = {"button_css": {"border-radius": 0, "border": "0px solid black"}}
    options = options or {}
    dfl_button_css.update(options)
    size = self.context._size(size)
    html_obj = html.HtmlButton.Buttons(self.context.rptObj, data or [], size, color, width, height, htmlCode, helper,
                                       dfl_button_css, profile)
    html_obj.css({"border": "1px solid %s" % html_obj.getColor("greys", 4), "padding": "2px"})
    self.context.register(html_obj)
    return html_obj

  def right(self):
    pass

  def left(self):
    pass
