"""

"""

from epyk.core import html


class Layouts(object):
  def __init__(self, context):
    self.context = context

  def _size(self, size):
    """

    :param size:
    :return:
    """
    if size[0] is None and size[1] == "px" and hasattr(self.context.rptObj, "style"):
      size = (self.context.rptObj.style.defaults.font.size, self.context.rptObj.style.defaults.font.unit)
    return size

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
    size = self._size(size)
    return self.context.register(html.HtmlOthers.Hr(self.context.rptObj, color, count, size, background_color, height, align, profile))

  def panel(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), helper=None, profile=None):
    """
    Add Html Component by using + to this object and you will be able to switch between them.

    :param htmlObjs:
    :param width:
    :param height:
    :param helper:
    :param profile:
    :return:
    """
    return self.context.register(html.HtmlContainer.Panel(self.context.rptObj, htmlObjs, width, height, helper, profile))

  def paneldisplay(self, htmlObjs=None, title='', width=(100, '%'), height=(None, 'px'), panelOptions=None, helper=None, profile=None):
    """

    :param htmlObjs:
    :param title:
    :param width:
    :param height:
    :param panelOptions:
    :param helper:
    :param profile:
    :return:
    """
    return self.context.register(html.HtmlContainer.PanelDisplay(self.context.rptObj, htmlObjs, title, width, height, panelOptions, helper, profile))

  def panelsplit(self, width=(100, '%'), height=(None, 'px'), leftWidth=50, left=None, right=None, resizable=True, helper=None, profile=None):
    """

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
    :return:
    """
    return self.context.register(html.HtmlContainer.PanelSplit(self.context.rptObj, width, height, leftWidth, left, right, resizable, helper, profile))

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
    :return:
    """
    return self.context.register(html.HtmlContainer.Col(self.context.rptObj, htmlObjs, position, width, height, align, helper, profile))

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
    :return:
    """
    return self.context.register(html.HtmlContainer.Row(self.context.rptObj, htmlObjs, width, height, aresData, align,
                                                        valign, colsWith, closable, resizable, titles, helper, profile))

  def grid(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), colsDim=None, colsAlign=None,
           noGlutters=False, align=None, helper=None, profile=None):
    return self.context.register(html.HtmlContainer.Grid(self.context.rptObj, htmlObjs, width, height, colsDim,
                                                         colsAlign, noGlutters, align, helper, profile))

  def tabs(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), tabNames=None, rowsCss=None, colsCss=None,
           closable=False, selectedTab=None, htmlCode=None, alwaysReload=False, encoding="UTF-8", helper=None, profile=None):
    """
    Python wrapper for a multi Tabs component

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    :param htmlObjs:
    :param width:
    :param height:
    :param tabNames:
    :param rowsCss:
    :param colsCss:
    :param closable:
    :param selectedTab:
    :param htmlCode:
    :param alwaysReload:
    :param encoding:
    :param helper:
    :param profile:
    :return:
    """
    return self.context.register(html.HtmlContainer.Tabs(self.context.rptObj, htmlObjs, width, height, tabNames, rowsCss,
                                                         colsCss, closable, selectedTab, htmlCode, alwaysReload, encoding, helper, profile))

  def pills(self, htmlObjs=None, width=(100, '%'), height=(None, 'px'), colsDim=None, rowsCss=None, colsCss=None,
            closable=False, selectedTab=None, htmlCode=None, alwaysReload=False, encoding="UTF-8", helper=None, profile=None):
    """
    Python wrapper to the Bootstrap Pills interface

    Documentation
    https://getbootstrap.com/docs/4.0/components/navs/

    :param htmlObjs:
    :param width:
    :param height:
    :param colsDim:
    :param rowsCss:
    :param colsCss:
    :param closable:
    :param selectedTab:
    :param htmlCode:
    :param alwaysReload:
    :param encoding:
    :param helper:
    :param profile:
    :return:
    """
    return self.context.register(html.HtmlContainer.Pills(self.context.rptObj, htmlObjs, width, height, colsDim, rowsCss,
                                                          colsCss, closable, selectedTab, htmlCode, alwaysReload, encoding, helper, profile))

  def div(self, htmlObjs=None, label=None, color=None, size=(None, "px"), width=(100, "%"), icon=None, height=(None, "px"), editable=False,
          align='left', padding=None, htmlCode=None, tag='div', helper=None, profile=None):
    """

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

    :rtype: html.HtmlContainer.Div

    :return:
    """
    size = self._size(size)
    return self.context.register(html.HtmlContainer.Div(self.context.rptObj, htmlObjs, label, color, size, width, icon,
                                                        height, editable, align, padding, htmlCode, tag, helper, profile))

  def fixeddiv(self, text=None, top=100, left=None, right=None, color=None, size=(None, "px"), width=(None, "px"), icon=None,
               height=(None, "px"), editable=False, align='left', backgroundColor='white', zindex=None, padding=None,
               htmlCode=None, tag='div', helper=None, profile=None):
    size = self._size(size)
    return self.context.register(html.HtmlContainer.DivFixed(self.context.rptObj, text, top, left, right, color, size,
                                                             width, icon, height, editable, align, backgroundColor, zindex,
                                                             padding, htmlCode, tag, helper, profile))

  def dragdiv(self, text=None, top=100, left=None, right=None, color=None, size=(None, "px"), width=(None, "px"), icon=None,
              height=(None, "px"), editable=False, align='left', backgroundColor='white', padding=None, htmlCode=None,
              tag='div', helper=None, profile=None):
    size = self._size(size)
    return self.context.register(html.HtmlContainer.DragDiv(self.context.rptObj, text, top, left, right, color, size,
                                                            width, icon, height, editable, align, backgroundColor, padding, htmlCode, tag, helper, profile))

  def loading(self, value=None, profile=None):
    return self.context.register(html.HtmlOthers.Loading(self.context.rptObj, value))

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
    size = self._size(size)
    return self.context.register(html.HtmlPopup.Popup(self.context.rptObj, htmlObj, title, color, size, width, height,
                                                      withBackground, draggable, margin, profile))

  def iframe(self, url, width=(100, "%"), height=(100, "%"), helper=None, profile=None):
    return self.context.register(html.HtmlContainer.IFrame(self.context.rptObj, url, width, height, helper, profile))

  def dialogs(self, recordSet=None, width=(100, "%"), height=(500, "px"), helper=None, profile=None):
    return self.context.register(html.HtmlContainer.Dialog(self.context.rptObj, recordSet, width, height, helper, profile))

  def menu(self, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    return self.context.register(html.HtmlContainer.IconsMenu(self.context.rptObj, width, height, htmlCode, helper, profile))

  def multiFilter(self, items=None, title=None, width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """

    :param items:
    :param title:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param profile:

    :rtype: html.HtmlEvent.Filters
    :return:
    """
    items = items or []
    return self.context.register(html.HtmlEvent.Filters(self.context.rptObj, items, title, width, height, htmlCode, helper, profile))


