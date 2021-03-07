#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.fwk.mt.js import JsMdcComponents


class Menu:

  def __init__(self, ui):
    self.page = ui.page

  def surface(self):
    """
    Description:
    ------------

    Related Pages:

      https://material.io/develop/web/components/menu-surface/
    """
    schema = {"type": 'div', 'class': None, 'css': None}
    menu = self.page.web.mt.composite(schema, options={"reset_class": True})

    dom_obj = JsMdcComponents.MenuSurface(menu)
    menu.style.builder(menu.style.varName, dom_obj.instantiate("#%s" % menu.htmlCode))
    # Add the specific dom features
    menu.dom = dom_obj
    return menu

  def anchor(self, text, surface):
    """
    Description:
    ------------

    https://material.io/develop/web/components/menu-surface/

    Attributes:
    ----------
    :param text:
    :param surface:
    """
    button = self.page.ui.button(text)
    button.set_attrs({"class": "menu-surface-button", 'css': None})
    menu = self.page.ui.div([button, surface])
    menu.set_attrs({"class": "mdc-menu-surface--anchor", 'css': None})
    return menu
