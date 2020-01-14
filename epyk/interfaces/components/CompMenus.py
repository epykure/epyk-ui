"""
Module dedicated to produce Menus components
"""

from epyk.core import html


class Menus(object):
  def __init__(self, context):
    self.context = context

  def menu(self):
    pass

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
