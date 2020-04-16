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

  def tree(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Related Pages:
Usage::

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

    Usage::

      Related Pages:
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

  def menu(self, data=None, color=None, width=(100, "%"), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      Related Pages:
Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:

    #TODO Ask if this module is still maintained
    """
    html_tree = html.HtmlEvent.Menu(self.context.rptObj, data or [], color, width, height, htmlCode, helper, options or {}, profile)
    self.context.register(html_tree)
    return html_tree

  def dropdown(self, recordSet=None, text="", width=(100, "%"), height=(32, 'px'), htmlCode=None,
               helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Related Pages:
http://getbootstrap.com/docs/4.0/components/dropdowns/
    https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_ref_js_dropdown_multilevel_css&stacked=h
    https://codepen.io/svnt/pen/beEgre

    https://codepen.io/raneio/pen/NbbZEM
    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover
    https://codepen.io/antoniputra/pen/BzyWmb

    Attributes:
    ----------
    :param recordSet:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dftl_options = {"width": 70}
    dftl_options.update(options or {})
    html_d = html.HtmlTrees.DropDown(self.context.rptObj, recordSet, text, width, height, htmlCode, helper,
                                     dftl_options, profile)
    self.context.register(html_d)
    return html_d
