"""
Module dedicated to produce Menus components
"""

from epyk.core import html


class Panels(object):
  def __init__(self, context):
    self.context = context

  def pills(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
            css_tab=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Usage:
    ------
    tab = rptObj.ui.panels.pills()
    for i in range(5):
      tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Related Pages:
    --------------
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    if css_tab is None:
      css_tab = {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '5px'}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    html_tabs.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.css_tab["background"] = html_tabs._report.theme.greys[0]
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.success[1]}
    self.context.register(html_tabs)
    return html_tabs

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, css_tab=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Usage:
    ------
    tab = rptObj.ui.panels.tabs()
    for i in range(5):
      tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Related Pages:
    --------------
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                 "border-bottom": "1px solid white"}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    self.context.register(html_tabs)
    return html_tabs

  def arrows_up(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                css_tab=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Related Pages:
    --------------
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "1px solid white"}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, css_tab,
                                        options or {"tab_class": 'CssPanelArrowUp'}, profile)
    html_tabs.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.css_tab["height"] = "60px"
    html_tabs.css_tab_clicked_dflt = {"background": html_tabs._report.theme.success[1], "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def arrows_down(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                  css_tab=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Related Pages:
    --------------
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "1px solid white"}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, css_tab,
                                        options or {"tab_class": 'CssPanelArrowDown'}, profile)
    html_tabs.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.css_tab["height"] = "60px"
    html_tabs.css_tab_clicked_dflt = {"background": html_tabs._report.theme.success[1], "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def menu(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
           css_tab=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Related Pages:
    --------------
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '10px 10px 0 0'}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    html_tabs.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.css_tab["background"] = html_tabs._report.theme.greys[0]
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.success[1]}
    html_tabs.tabs_container.css({"border-bottom": "2px solid %s" % html_tabs._report.theme.success[1]})
    self.context.register(html_tabs)
    return html_tabs

  def sliding(self, htmlObjs, title, color=None, width=(100, "%"), height=(None, "px"),
            htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param htmlObjs:
    :param title:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    :return:
    """
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_slide = html.HtmlContainer.PanelSlide(self.context.rptObj, htmlObjs, title, color, width, height,
                                               htmlCode, helper, options or {}, profile)
    self.context.register(html_slide)
    return html_slide

  def split(self, width=(100, '%'), height=(None, 'px'), leftWidth=50, left=None, right=None, resizable=True,
            helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
    number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
    div = rptObj.ui.layouts.panelsplit(left=number, right=number_2)

    Related Pages:
    --------------
    https://codepen.io/rstrahl/pen/eJZQej

    Attributes:
    ----------
    :param width:
    :param height:
    :param leftWidth:
    :param left:
    :param right:
    :param resizable:
    :param helper:
    :param profile:
    """
    html_split = html.HtmlContainer.PanelSplit(self.context.rptObj, width, height, leftWidth, left, right, resizable, helper, profile)
    self.context.register(html_split)
    return html_split
