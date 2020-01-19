"""
Module with the different pre defined flavours of tree
"""


# Check if pandas is available in the current environment
# if it is the case this module can handle Dataframe directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core import html


class Trees(object):
  def __init__(self, context):
    self.context = context

  def tree(self, data=None, size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, profile=None):
    """

    Example
    data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
    rptObj.ui.lists.tree(data)

    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_tree = html.HtmlTrees.Tree(self.context.rptObj, data or [], size, color, width, height, htmlCode, helper, profile)
    self.context.register(html_tree)
    return html_tree

  def inputs(self, data=None, size=(None, "px"), color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, profile=None):
    """

    Example
    data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
    rptObj.ui.lists.tree(data)

    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_tree = html.HtmlTrees.TreeInput(self.context.rptObj, data or [], size, color, width, height, htmlCode, helper, profile)
    self.context.register(html_tree)
    return html_tree
