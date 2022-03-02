#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core import html
from epyk.core.data import tree as data_tree
from epyk.interfaces import Arguments


class Trees:

  def __init__(self, ui):
    self.page = ui.page

  def tree(self, data=None, width: Union[tuple, int] = (100, "%"), height: Union[tuple, int] = (None, 'px'),
           html_code: str = None, helper: str = None, options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    Usage::

      data = [{"value": 'test', 'items': [{"value": 'child 1', 'color': 'red'}]}]
      page.ui.lists.tree(data)

      data = [{"value": 'test', 'icon': "fas fa-check", "css": {'color': 'green'}, 'items': [{
        "value": 'child 1', "css": {'color': 'red'}, 'icon': "fas fa-times"}]},
              {"value": 'test 2', 'icon': "fas fa-exclamation-triangle", "css": {'color': 'orange'}, 'items': [{
                "value": 'child 1', "css": {'color': 'red'}, 'icon': "fas fa-times"}],
               }]

      hyr = page.ui.tree(data)
      hyr.options.icon_close = "fas fa-caret-right"
      hyr.options.icon_open = "fas fa-caret-down"
      hyr.options.with_badge = True
      hyr.options.with_icon = "icon"
      hyr.click_node([page.js.alert(pk.events.value)])
      hyr.click([page.js.alert(pk.events.value)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.Tree`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/tree.py

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlTrees.Tree(self.page, data or [], width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(html_tree)
    return html_tree

  def inputs(self, data=None, width: Union[tuple, int] = (100, "%"), height: Union[tuple, int] = (None, 'px'),
             html_code: str = None, helper: str = None, options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.TreeInput`

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlTrees.TreeInput(
      self.page, data or [], width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(html_tree)
    return html_tree

  def menu(self, data=None, width: Union[tuple, int] = (100, "%"), height: Union[tuple, int] = (None, 'px'),
           html_code: str = None, helper: str = None, options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:

    #TODO Ask if this module is still maintained.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlEvent.Menu(self.page, data or [], width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(html_tree)
    return html_tree

  def dropdown(self, record=None, text: str = "", width: Union[tuple, int] = (100, "%"),
               height: Union[tuple, int] = (None, 'px'), html_code: str = None, helper: str = None,
               options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.DropDown`

    Related Pages:

      http://getbootstrap.com/docs/4.0/components/dropdowns/
      https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_ref_js_dropdown_multilevel_css&stacked=h
      https://codepen.io/svnt/pen/beEgre

      https://codepen.io/raneio/pen/NbbZEM
      https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover
      https://codepen.io/antoniputra/pen/BzyWmb

    Attributes:
    ----------
    :param record:
    :param text:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"width": 70}
    dfl_options.update(options or {})
    html_d = html.HtmlTrees.DropDown(
      self.page, record, text, width, height, html_code, helper, dfl_options, profile)
    html.Html.set_component_skin(html_d)
    return html_d

  def folder(self, folder: str = None, width: Union[tuple, int] = (100, "%"), height: Union[tuple, int] = (None, 'px'),
             html_code: str = None, helper: str = None, options: dict = None, profile: Union[dict, bool] = None):
    options = options or {}
    if folder is not None:
      data = data_tree.folders(
        folder, excluded_folders=options.get("excluded_folders", ["outs", "static"]), make_url=options.get("make_url"))
    else:
      data = []
    tree = self.tree(
      data, width=width, height=height, html_code=html_code, helper=helper, options=options, profile=profile)
    if height[0] is not None:
      tree.style.css.overflow = "auto"
    html.Html.set_component_skin(tree)
    return tree
