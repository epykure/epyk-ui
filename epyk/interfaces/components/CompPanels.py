
from epyk.core import html


class Panels(object):
  def __init__(self, context):
    self.context = context

  def pills(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Usage::

      tab = rptObj.ui.panels.pills()
    for i in range(5):
      tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Related Pages:

			https://getbootstrap.com/docs/4.0/components/navs/
    """
    dflt_options = {"css_tab": {'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0', 'border-radius': '5px',
                                'color': self.context.rptObj.theme.greys[-1], "background": self.context.rptObj.theme.greys[0]}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    html_tabs.options.css_tab_clicked = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.success[1]}
    self.context.register(html_tabs)
    return html_tabs

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Usage::

      tab = rptObj.ui.panels.tabs()
    for i in range(5):
      tab.add_panel("Panel %s" % i, rptObj.ui.text("test %s" % i))

    Related Pages:

			https://getbootstrap.com/docs/4.0/components/navs/

    """
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                                "border-bottom": "1px solid white"}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper,
                                        dflt_options, profile)
    self.context.register(html_tabs)
    return html_tabs

  def arrows_up(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Related Pages:

			https://getbootstrap.com/docs/4.0/components/navs/

    """
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                                "border-bottom": "1px solid white"}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsUp(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_up()
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {"background": html_tabs._report.theme.success[1], "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def arrows_down(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
                  options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper for a multi Tabs component

    Related Pages:

			https://getbootstrap.com/docs/4.0/components/navs/
    """
    dflt_options = {
      "css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 "border-bottom": "1px solid white"}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.TabsArrowsDown(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    for t in html_tabs.tabs():
      t.style.add_classes.layout.panel_arrow_down()
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["height"] = "30px"
    html_tabs.options.css_tab_clicked = {"background": html_tabs._report.theme.success[1], "color": "white"}
    self.context.register(html_tabs)
    return html_tabs

  def menu(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    """
    Description:
    ------------
    Python wrapper to the Bootstrap Pills interface

    Related Pages:

			https://getbootstrap.com/docs/4.0/components/navs/
    """
    dflt_options = {"css_tab": {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '10px 10px 0 0'}}
    if options is not None:
      dflt_options.update(options)
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, width, height, htmlCode, helper, dflt_options, profile)
    html_tabs.options.css_tab["color"] = html_tabs._report.theme.greys[-1]
    html_tabs.options.css_tab["background"] = html_tabs._report.theme.greys[0]
    html_tabs.options.css_tab_clicked = {'color': html_tabs._report.theme.greys[0], 'background': html_tabs._report.theme.success[1]}
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
    """
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_slide = html.HtmlContainer.PanelSlide(self.context.rptObj, htmlObjs, title, color, width, height,
                                               htmlCode, helper, options or {}, profile)
    self.context.register(html_slide)
    return html_slide

  def split(self, left=None, right=None, width=(100, '%'), height=(200, 'px'), left_width=(160, 'px'), resizable=True,
            helper=None, profile=None):
    """
    Description:
    ------------

    Usage::

      number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
    number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
    div = rptObj.ui.layouts.panelsplit(left=number, right=number_2)

    Related Pages:

			https://codepen.io/rstrahl/pen/eJZQej

    Attributes:
    ----------
    :param width:
    :param height:
    :param left_width:
    :param left:
    :param right:
    :param resizable:
    :param helper:
    :param profile:
    """
    html_split = html.HtmlContainer.PanelSplit(self.context.rptObj, width, height, left_width, left, right, resizable, helper, profile)
    self.context.register(html_split)
    return html_split
