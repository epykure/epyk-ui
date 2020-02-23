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

  def tree(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
    rptObj.ui.lists.tree(data)

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_tree = html.HtmlTrees.Tree(self.context.rptObj, data or [], color, width, height, htmlCode, helper, options or {}, profile)
    self.context.register(html_tree)
    return html_tree

  def inputs(self, data=None, color=None, width=(100, "%"), height=(None, 'px'),
           htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    html_tree = html.HtmlTrees.TreeInput(self.context.rptObj, data or [], color, width, height, htmlCode, helper, options or {}, profile)
    self.context.register(html_tree)
    return html_tree
