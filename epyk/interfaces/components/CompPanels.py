"""
Module dedicated to produce Menus components
"""

from epyk.core import html


class Panels(object):
  def __init__(self, context):
    self.context = context

  def pills(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
            css_tab=None, options=None, profile=False):
    """
    Python wrapper to the Bootstrap Pills interface

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '5px', "font-size": '%s%s' % (size[0] + 2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["background"] = html_tabs.getColor("greys", 0)
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs.getColor("greys", 0), 'background': html_tabs.getColor("success", 1)}
    self.context.register(html_tabs)
    return html_tabs

  def tabs(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
           css_tab=None, options=None, profile=False):
    """
    Python wrapper for a multi Tabs component

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                 "border-bottom": "1px solid white", "font-size": '%s%s' % (size[0]+2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    self.context.register(html_tabs)
    return html_tabs

  def arrows_up(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                css_tab=None, options=None, profile=False):
    """
    Python wrapper for a multi Tabs component

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "1px solid white", "font-size": '%s%s' % (size[0]+2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab,
                                        options or {"tab_class": 'CssPanelArrowUp'}, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["height"] = "60px"
    html_tabs.css_tab_clicked_dflt = {"background": html_tabs.getColor("success", 1), "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def arrows_down(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                css_tab=None, options=None, profile=False):
    """
    Python wrapper for a multi Tabs component

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "1px solid white", "font-size": '%s%s' % (size[0]+2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab,
                                        options or {"tab_class": 'CssPanelArrowDown'}, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["height"] = "60px"
    html_tabs.css_tab_clicked_dflt = {"background": html_tabs.getColor("success", 1), "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def menu(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
            css_tab=None, options=None, profile=False):
    """
    Python wrapper to the Bootstrap Pills interface

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '10px 10px 0 0', "font-size": '%s%s' % (size[0] + 2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab,
                                        options or {}, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["background"] = html_tabs.getColor("greys", 0)
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs.getColor("greys", 0), 'background': html_tabs.getColor("success", 1)}
    html_tabs.tabs_container.css({"border-bottom": "2px solid %s" % html_tabs.getColor("success", 1)})

    self.context.register(html_tabs)
    return html_tabs
