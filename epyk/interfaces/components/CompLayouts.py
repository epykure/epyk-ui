"""

"""

from epyk.core import html


class Layouts(object):
  def __init__(self, context):
    self.context = context

  def new_line(self, count=1, profile=None):
    """
    Wrapper around the Br html tag.

    The <br> tag inserts a single line break.

    Example
    rptObj.ui.layouts.new_line(10)

    Documentation
    https://www.w3schools.com/tags/tag_br.asp

    :param count: Optional, The number of empty line to put. Default 1
    :param profile: Optional, Activate the profiler
    :return:
    """
    return self.context.register(html.HtmlOthers.Newline(self.context.rptObj, count, profile=profile))

  def hr(self, count=1, size=(None, 'px'), color=None, background_color=None, height=(None, 'px'), align=None, profile=None):
    """
    Wrapper around the HT html tag.

    The <hr> tag defines a thematic break in an HTML page (e.g. a shift of topic).

    Example
    rptObj.ui.layouts.hr(10)

    Documentation
    https://www.w3schools.com/tags/tag_hr.asp

    :param count: The number of HR tag to be added
    :param size:
    :param color: Optional. The color code for the font
    :param background_color: Optional. The component background color
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. The content position. Values (left, right, center). Default center
    :param profile: Optional. A flag to set the component performance storage
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlOthers.Hr(self.context.rptObj, color, count, size, background_color, height, align, profile))

  def panelsplit(self, width=(100, '%'), height=(None, 'px'), leftWidth=50, left=None, right=None, resizable=True, helper=None, profile=None):
    """

    Example
    number = rptObj.ui.rich.number(500, "Test", height=(150, 'px'))
    number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
    div = rptObj.ui.layouts.panelsplit(left=number, right=number_2)

    Documentation
    https://codepen.io/rstrahl/pen/eJZQej

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

  def col(self, htmlObjs=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None, profile=None):
    """
    Python wrapper for a column of HTML elements from Bootstrap

    This component is a container and it is used to display multiple Ares components in column.
    You can first add a component in the data list then add the + operator to add more.

    Documentation
    https://getbootstrap.com/docs/4.0/layout/grid/
    https://www.alsacreations.com/tuto/lire/1493-css3-flexbox-layout-module.html

    :param htmlObjs:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param profile:
    """
    html_col = html.HtmlContainer.Col(self.context.rptObj, htmlObjs, position, width, height, align, helper, profile)
    self.context.register(html_col)
    return html_col

  def row(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), aresData=None, align='left',
          valign='top', colsWith=None, closable=False, resizable=False, titles=None, helper=None, profile=None):
    """
    Python wrapper for a row of HTML items

    :param htmlObjs:
    :param width:
    :param height:
    :param aresData:
    :param align:
    :param valign:
    :param colsWith:
    :param closable:
    :param resizable:
    :param titles:
    :param helper:
    :param profile:
    """
    html_row = html.HtmlContainer.Row(self.context.rptObj, htmlObjs, width, height, aresData, align, valign, colsWith,
                                      closable, resizable, titles, helper, profile)
    self.context.register(html_row)
    return html_row

  def grid(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), colsDim=None, colsAlign=None,
           noGlutters=False, align=None, helper=None, profile=None):
    """

    Example
    div = rptObj.ui.layouts.grid([number, number_3, number_2, number_4])

    :param htmlObjs:
    :param width:
    :param height:
    :param colsDim:
    :param colsAlign:
    :param noGlutters:
    :param align:
    :param helper:
    :param profile:
    """
    html_grid = html.HtmlContainer.Grid(self.context.rptObj, htmlObjs, width, height, colsDim, colsAlign, noGlutters,
                                        align, helper, profile)
    self.context.register(html_grid)
    return html_grid

  def tabs(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
           css_tab=None, profile=False):
    """
    Python wrapper for a multi Tabs component

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0',
                 "border-bottom": "1px solid white", "font-size": '%s%s' % (size[0]+2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab, profile)
    self.context.register(html_tabs)
    return html_tabs

  def menu(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
            css_tab=None, profile=False):
    """
    Python wrapper to the Bootstrap Pills interface

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '10px 10px 0 0', "font-size": '%s%s' % (size[0] + 2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["background"] = html_tabs.getColor("greys", 0)
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs.getColor("greys", 0), 'background': html_tabs.getColor("success", 1)}
    html_tabs.tabs_container.css({"border-bottom": "2px solid %s" % html_tabs.getColor("success", 1)})

    self.context.register(html_tabs)
    return html_tabs

  def pills(self, color=None, size=(None, "px"), width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None,
            css_tab=None, profile=False):
    """
    Python wrapper to the Bootstrap Pills interface

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    size = self.context._size(size)
    if css_tab is None:
      css_tab = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 0 0',
                 'border-radius': '5px', "font-size": '%s%s' % (size[0] + 2, size[1])}
    html_tabs = html.HtmlContainer.Tabs(self.context.rptObj, color, size, width, height, htmlCode, helper, css_tab, profile)
    html_tabs.css_tab["color"] = html_tabs.getColor("greys", -1)
    html_tabs.css_tab["background"] = html_tabs.getColor("greys", 0)
    html_tabs.css_tab_clicked_dflt = {'color': html_tabs.getColor("greys", 0), 'background': html_tabs.getColor("success", 1)}
    self.context.register(html_tabs)
    return html_tabs

  def panel(self, htmlObjs=None, title=None, color=None, size=(None, "px"), width=(100, "%"), height=(None, "px"),
            htmlCode=None, helper=None, profile=False):
    size = self.context._size(size)
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_panel = html.HtmlContainer.Panel(self.context.rptObj, htmlObjs, title, color, size, width, height, htmlCode, helper, profile)
    self.context.register(html_panel)
    return html_panel

  def slide(self, htmlObjs, title, color=None, size=(None, "px"), width=(100, "%"), height=(None, "px"),
            htmlCode=None, helper=None, profile=False):
    size = self.context._size(size)
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_slide = html.HtmlContainer.PanelSlide(self.context.rptObj, htmlObjs, title, color, size, width, height, htmlCode, helper, profile)
    self.context.register(html_slide)
    return html_slide

  def div(self, htmlObjs=None, label=None, color=None, size=(None, "px"), width=(100, "%"), icon=None, height=(None, "px"), editable=False,
          align='left', padding=None, htmlCode=None, tag='div', helper=None, profile=None):
    """
    Example
    div = rptObj.ui.div([html])
    div += html_2

    Documentation
    https://www.w3schools.com/tags/tag_div.asp

    :param htmlObjs:
    :param label:
    :param color:
    :param size:
    :param width:
    :param icon:
    :param height:
    :param editable:
    :param align:
    :param padding:
    :param htmlCode:
    :param tag:
    :param profile:
    """
    size = self.context._size(size)
    if htmlObjs is not None and not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    html_div = html.HtmlContainer.Div(self.context.rptObj, htmlObjs, label, color, size, width, icon, height, editable,
                                     align, padding, htmlCode, tag, helper, profile)
    self.context.register(html_div)
    return html_div

  def popup(self, htmlObj=None, title=None, color=None, size=(None, 'px'), width=(100, '%'), height=(None, 'px'),
            withBackground=True, draggable=False, margin=10, profile=None):
    """

    Example
    popup = report.popup(report.title('Test'), color="red")
    popup + report.paragraph('Test')


    Documentation
    https://www.w3schools.com/tags/tag_div.asp

    :param htmlObj:
    :param title:
    :param color:
    :param size:
    :param width:
    :param height:
    :param withBackground:
    :param draggable:
    :param margin:
    :param profile:
    :rtype: html.HtmlPopup.Popup
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlPopup.Popup(self.context.rptObj, htmlObj, title, color, size, width, height,
                                                      withBackground, draggable, margin, profile))

  def iframe(self, url, width=(100, "%"), height=(100, "%"), helper=None, profile=None):
    """

    Example
    rptObj.ui.layouts.iframe("http://www.google.com")

    :param url:
    :param width:
    :param height:
    :param helper:
    :param profile:
    """
    html_frame = html.HtmlContainer.IFrame(self.context.rptObj, url, width, height, helper, profile)
    self.context.register(html_frame)
    return html_frame

  def dialogs(self, recordSet=None, width=(100, "%"), height=(200, "px"), helper=None, profile=None):

    html_dialog = html.HtmlContainer.Dialog(self.context.rptObj, recordSet, width, height, helper, profile)
    self.context.register(html_dialog)
    return html_dialog

  def icons(self, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """

    Example
    menu = rptObj.ui.layouts.icons()
    menu.icon.click([menu.icon.dom.css({"color": 'red'})])

    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:
    """
    html_icon = html.HtmlContainer.IconsMenu(self.context.rptObj, width, height, htmlCode, helper, profile)
    self.context.register(html_icon)
    return html_icon

  def multiFilter(self, items=None, title=None, size=(None, 'px'), width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """

    :param items:
    :param title:
    :param size:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlEvent.Filters
    :return:
    """
    size = self.context._size(size)
    items = items or []
    return self.context.register(html.HtmlEvent.Filters(self.context.rptObj, items, title, size, width, height, htmlCode, helper, profile))

  def table(self, records, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """

    Example
    simple_table = rptObj.ui.layouts.table(df.to_dict("records"), cols=["COL1"], rows=["COL2"])
    simple_table.add_row({"COL1": "Value"})

    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    if len(records) > 0:
      if isinstance(records[0], list):
        header = records[0]
        tmp_records = [dict(zip(header, rec)) for rec in records[1:]]
        if rows is None:
          rows = [header[0]]
        if cols is None:
          cols = header[1:]
        records = tmp_records
    if width is None:
      width = (None, "px")
    table = html.tables.HtmlTable.Bespoke(self.context.rptObj, records, cols, rows, width, height, htmlCode, options, profile)
    self.context.register(table)
    return table

  def form(self, action, method, htmlObj=None, helper=None):
    """

    :param action:
    :param method:
    :param htmlObj:
    :param helper:
    :return:
    """
    form = html.HtmlContainer.Form(self.context.rptObj, htmlObj, action, method, helper)
    self.context.register(form)
    return form
