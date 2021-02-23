#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.data import tree as data_tree
from epyk.interfaces import Arguments


class Trees(object):

  def __init__(self, context):
    self.context = context

  def tree(self, data=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      data = [{"value": 'test', 'items': [{"value": 'child 1', 'color': 'red'}]}]
      page.ui.lists.tree(data)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.Tree`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/tree.py

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlTrees.Tree(self.context.rptObj, data or [], width, height, htmlCode, helper, options or {}, profile)
    return html_tree

  def inputs(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
             htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.TreeInput`

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
    html_tree = html.HtmlTrees.TreeInput(self.context.rptObj, data or [], width, height, htmlCode, helper, options or {}, profile)
    return html_tree

  def menu(self, data=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Menu`

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

    #TODO Ask if this module is still maintained.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlEvent.Menu(self.context.rptObj, data or [], width, height, htmlCode, helper, options or {}, profile)
    return html_tree

  def dropdown(self, record=None, text="", width=(100, "%"), height=(32, 'px'), htmlCode=None,
               helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

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
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dftl_options = {"width": 70}
    dftl_options.update(options or {})
    html_d = html.HtmlTrees.DropDown(self.context.rptObj, record, text, width, height, htmlCode, helper,
                                     dftl_options, profile)
    return html_d

  def folder(self, folder=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None,
             profile=None):
    options = options or {}
    if folder is not None:
      data = data_tree.folders(folder, excluded_folders=options.get("excluded_folders", ["outs", "static"]), make_url=options.get("make_url"))
    else:
      data = []
    tree = self.tree(data, width=width, height=height, htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    if height[0] is not None:
      tree.style.css.overflow = "auto"
    return tree
