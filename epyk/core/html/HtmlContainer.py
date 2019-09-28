"""
Wrapper to the Bootstrap Layout library
"""


import json

from epyk.core.html import Html
from epyk.core.html import HtmlSelect


class Panel(Html.Html):
  __pyStyle = ['CssDivNoBorder']
  name, category, callFnc = 'Multi Panel', 'Layouts', 'panel'

  def __init__(self, report, htmlObjs, width, height, helper, profile):
    super(Panel, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.__htmlOrder, self.__htmlRef, self.htmlMaps = [], {}, {}
    for htmlObj in htmlObjs:
      self.__add__(htmlObj)
    self.css({"padding": "5px"})

  def __add__(self, htmlObj):
    """ Add an Html Object to this object"""
    htmlObj.inReport = False
    self.__htmlRef[htmlObj.htmlId] = htmlObj
    self.__htmlOrder.append(htmlObj.htmlId)
    self._addToContainerMap(htmlObj)

  @property
  def jqId(self):
    """ Refer to the internal select item """
    return "$('#%s_select')" % self.htmlId

  def onDocumentLoadVar(self):
    """ Return the variable to store in the global section of the javacript part """
    self.jsVal = "%s_data" % self.htmlId
    self.addGlobalVar(self.jsVal, json.dumps(self.__htmlOrder))

  def onDocumentLoadFnc(self):
    """ Pure Javascript onDocumentLoad Function """
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, ''' htmlObj.empty() ;
     data.forEach(function(item){
        htmlObj.append('<option value="' + item + '">' + item + '</option>') ; }) ; ''', 'Javascript Object builder')

  def __str__(self):
    """ Return the onload, the HTML object and the javascript events """
    # No string method for a container, it will add its data in the html directly
    # The below part is the string representation
    items = ['<div %s>' % self.strAttr(pyClassNames=self.pyStyle)]
    items.append('<div class="form-group py_csssdivboxmargin"><select class="form-control" id="%s_select"></select></div>' % (self.htmlId))
    for name in self.__htmlOrder:
      obj = self.__htmlRef[name].html()
      items.append('<div style="display:none" id="%s" >%s</div>' % (name, obj))
    items.append('</div>')

    # The function to change the display according to the item name selected
    self._report.jsOnLoadFnc.add('''
        $('#%(htmlId)s_select').on('change', function (event){ 
          DisplayItem( $('#%(htmlId)s_select option:checked').val(), %(htmlItems)s ) }); 
      ''' % {'htmlId': self.htmlId, 'htmlItems': json.dumps(self.__htmlOrder)})

    # The global function to hide and show components based on a list
    # This is global as some other components might want to use it and there is no need to rewrite it every time
    self.addGlobalFnc('DisplayItem(htmlIdToDisplay, idListToHidde)', '''
        idListToHidde.forEach(function(htmlId) { $('#' + htmlId).hide() ; }); $('#' + htmlIdToDisplay).show() ; ''',
                      'The global function to hide and show components based on a list. This is global as some other components might want to use it and there is no need to rewrite it every time')
    return "".join(items)


class PanelSplit(Html.Html):
  __reqJs, __reqCss = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Panel Split', 'Layouts', 'panelsplit'
  mocks = []

  def __init__(self, report, width, height, leftWidth, leftObj, rightObj, resizable, helper, profile):
    super(PanelSplit, self).__init__(report, None, width=width[0], widthUnit=width[1], height=height[0],
                                     heightUnit=height[1], profile=profile)
    self.leftWidth, self.htmlMaps, self.resizable = leftWidth, {}, resizable
    if leftObj is not None:
      self.left(leftObj)
    if rightObj is not None:
      self.right(rightObj)
    self.cssLeft = {'flex':'0 0 auto', 'padding': '5px', 'min-width': '100px', 'width': self.leftWidth, 'white-space': 'nowrap'}
    self.cssRight = {'flex': '0 1 auto', 'padding': '5px', 'width': '100%', 'background': self.getColor('greys', 0),
                     'border-left': '3px solid %s' % self.getColor("success", 1)}
    self.css({'display': 'flex', 'flex-direction': 'row', 'overflow': 'hidden', 'xtouch-action': 'none'})

  def left(self, htmlObj):
    """ Add the left component to the panel """
    htmlObj.inReport = False
    self.htmlLeft = htmlObj
    self._addToContainerMap(htmlObj)

  def right(self, htmlObj):
    """ Add the right component to the panel """
    htmlObj.inReport = False
    self.htmlRight = htmlObj
    self._addToContainerMap(htmlObj)

  def html(self):
    """ Return the onload, the HTML object and the javascript events """
    # Update the HTML element with the values defined in the function call in the report
    if hasattr(self, 'jsUpdateFnc'):
      self.__addUpdtMethod(self.pyToJsData(self.vals))
    items = ['<div %s>' % self.strAttr(pyClassNames=self.pyStyle)]
    items.append('<div style="%s" id="%s_left" class="panel-left">%s</div>' % ( ";".join(["%s:%s" % (k, v) for k, v in self.cssLeft.items()]), self.htmlId, self.htmlLeft.html()))
    items.append('<div style="%(style)s" id="%(htmlId)s_right" class="panel-right">%(right)s</div>' % {'style': ";".join(["%s:%s" % (k, v) for k, v in self.cssRight.items()]), 'htmlId': self.htmlId, 'right': self.htmlRight.html()})
    items.append('</div>')
    if self.resizable:
      self._report.jsOnLoadFnc.add('''
         $("#%(htmlId)s_left").resizable({handleSelector: ".splitter", resizeHeight: false});
         $("#%(htmlId)s_right").resizable({handleSelector: ".splitter-horizontal", resizeWidth: true});
        ''' % {'htmlId': self.htmlId})
    return "".join(items)


class PanelDisplay(Html.Html):
  __pyStyle = ['CssDivNoBorder', 'CssPanelTitle']
  name, category, callFnc = 'Display Panel', 'Layouts', 'paneldisplay'

  def __init__(self, report, htmlObjs, title, width, height, panelOptions, helper, profile):
    if not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]
    self.__panelOptions = panelOptions if panelOptions is not None else {}
    super(PanelDisplay, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.__htmlOrder, self.__htmlRef, self.htmlMaps, self.title, self.showPanel = [], {}, {}, title, self.__panelOptions.get("visible", True)
    for htmlObj in htmlObjs:
      self.__add__(htmlObj)
    self.addGlobalVar("panel_show_%s" % self.htmlId, len(self.vals))
    self.css({"margin-bottom": "5px"})

  @property
  def jqId(self): return "$('#%s_icon')" % self.htmlId

  @property
  def jsQueryData(self): return "{}"

  def __add__(self, htmlObj):
    """ Add an Html Object to this object"""
    htmlObj.inReport = False
    self.__htmlRef[htmlObj.htmlId] = htmlObj
    self.__htmlOrder.append(htmlObj.htmlId)
    self._addToContainerMap(htmlObj)

  def getObj(self, i):
    return self.__htmlRef[self.__htmlOrder[i]]

  # -----------------------------------------------------------------------------------------
  #                                STANDARD DATATABLE JAVASCRIPT
  # -----------------------------------------------------------------------------------------
  def jsClose(self): return "$('#%s_toggle').hide()" % self.htmlId

  def jsExpand(self): return "$('#%s_toggle').show()" % self.htmlId

  def jsState(self): return "$('#%s_toggle').is(':visible')" % self.htmlId

  def __str__(self):
    items = ['<div %s>' % self.strAttr(pyClassNames=[self.pyStyle[0]])]
    visible, arrow = ("show", 'down') if self.showPanel else ('none', 'up')
    if self.__panelOptions.get("arrow", True):
      items.append('''
        <div onselectstart="return false" class="%(cssCls)s">
          %(title)s<i id="%(htmlId)s_icon" onclick="PanelDisplay(this, \'%(htmlId)s\')" style="cursor:pointer;margin:5px 0 5px 5px;float:right" class="fas fa-chevron-circle-%(arrow)s"></i>
        </div>''' % {'cssCls': self._report.style.cssName("CssPanelTitle"), 'title': self.title, 'htmlId': self.htmlId, 'arrow': arrow})
      self.addGlobalFnc("PanelDisplay(srcObj, htmlId)", '''
            $('#'+ htmlId + '_toggle').toggle();
            if ($('#'+ htmlId +'_toggle').css('display') == 'block') {$(srcObj).attr('class', 'fa fa-chevron-circle-down fa-w-16')}
            else {$(srcObj).attr('class', 'fa fa-chevron-circle-up fa-w-16')}
            var resizeEvent = window.document.createEvent('UIEvents');
            resizeEvent.initUIEvent('resize', true, false, window, 0);
            window.dispatchEvent(resizeEvent);
            ''', 'Javascript function to monitor the display of the sliding panel.')
    else:
      items.append('''<div onselectstart="return false" class="%(cssCls)s" style="cursor:pointer" onclick="PanelDisplayNoArrow(this, \'%(htmlId)s\')">%(title)s
        </div>''' % {'cssCls': self._report.style.cssName("CssPanelTitle"), 'title': self.title, 'htmlId': self.htmlId, 'arrow': arrow})
      self.addGlobalFnc("PanelDisplayNoArrow(srcObj, htmlId)", '''
        $('#'+ htmlId + '_toggle').toggle();
        var resizeEvent = window.document.createEvent('UIEvents');
        resizeEvent.initUIEvent('resize', true, false, window, 0);
        window.dispatchEvent(resizeEvent)''', '')
    items.append("<div id='%s_toggle' style='display:%s'>" % (self.htmlId, visible))
    for name in self.__htmlOrder:
      items.append('<div id="%s_container">%s</div>' % (name, self.__htmlRef[name].html()))
    items.append("</div></div>")
    return "".join(items)


class Div(Html.Html):
  __pyStyle = ['CssDivNoBorder']
  __reqCss, __reqJs = ['bootstrap'], ['jquery']
  name, category, callFnc = 'Simple Container', 'Layouts', 'div'

  def __init__(self, report, htmlObj, label, color, size, width, icon, height, editable, align, padding, htmlCode, tag,
               helper, profile):
    if isinstance(htmlObj, list) and htmlObj:
      for obj in htmlObj:
        if hasattr(obj, 'inReport'):
          obj.inReport = False
    elif htmlObj is not None and hasattr(htmlObj, 'inReport'):
      htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    super(Div, self).__init__(report, htmlObj, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                              profile=profile)
    self.htmlMaps, self.tag = {}, tag
    # Add the component predefined elements
    self.add_icon(icon)
    self.add_label(label)
    self.add_helper(helper)

    self.css({"color": color or self.getColor("greys", -1), "font-size": "%s%s" % (size[0], size[1]) if size[0] is not None else 'inherit',
              'text-align': align, "vertical-align": 'middle'})
    if padding is not None:
      self.css('padding', '%s' % padding)
    if editable:
      self.addAttr('contenteditable', "true")
      self.css('overflow', 'auto')

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    if not isinstance(self.vals, list):
      self.vals = [self.vals]
    self.vals.append(htmlObj)
    self._addToContainerMap(htmlObj)
    return self

  @property
  def val(self):
    """ Return the Javascript Value """
    return '$("#%s").html()' % self.htmlId

  @property
  def jsQueryData(self): return "{event_val: '', event_code: '%s'}" % self.htmlId

  def __str__(self):
    return "<div %s></div>%s" % (self.strAttr(pyClassNames=self.pyStyle), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    if isinstance(self.vals, list):
      for val in self.vals:
        if hasattr(val, 'inReport'):
          val.to_word(document)
    else:
      if hasattr(self.vals, 'inReport'):
        self.vals.to_word(document)


class DivFixed(Div):
  name, category, callFnc = 'Fixed Div', 'Layouts', 'fixeddiv'

  def __init__(self, report, text, top, left, right, color, size, width, icon, height, editable,
               align, backgroundColor, zindex, padding, htmlCode, tag, helper, profile):
    super(DivFixed, self).__init__(report, [], color, size, width[0], width[1], icon, height[0], height[1], editable, align,
                                   padding, htmlCode, tag, profile)
    self.css({'position': 'fixed', 'top': "%spx" % top, ' white-space': 'nowrap'})
    if zindex is not None:
      self.css('z-index', zindex)
    if isinstance(text, list):
      for subTxt in text:
        self + self._report.text(subTxt, size=size)
    else:
      self + self._report.text(text, size=size)
    if left is not None:
      self.css('left', "%spx" % left)
    elif right is not None:
      self.css('right', "%spx" % right)
    if backgroundColor is not None:
      self.css('background-color', backgroundColor)


class DragDiv(Div):
  __reqJs = ['jqueryui']
  name, category, callFnc = 'Drag Div', 'Layouts', 'dragdiv'

  def __init__(self, report, text, top, left, right, color, size, width, icon, height, editable,
               align, backgroundColor, padding, htmlCode, tag, helper, profile):
    super(DragDiv, self).__init__(report, [], color, size, width[0], width[1], icon, height[0], height[1], editable, align, padding,
                                  htmlCode, tag, profile)
    self.css({'position': 'absolute', 'top': "%spx" % top, 'border-radius': '10px'})
    self.size = 10 if size is None else size
    self + self._report.text(text, size=self.size)
    if left is not None:
      self.css('left', "%spx" % left)
    elif right is not None:
      self.css('right', "%spx" % right)
    if backgroundColor is not None:
      self.css('background-color', backgroundColor)

  def jsFocus(self):
    return '$("#%s_content").focus()' % self.htmlId

  def html(self):
    """ Return the HTML display of a split container"""
    self.loadStyle()
    self.jsEvents()
    icon = ''
    self._report.jsOnLoadFnc.add("%s.draggable()" % self.jqId)
    self._report.jsOnLoadFnc.add("%s.bind('dragstop', function(){  } )" % self.jqId)
    if self.icon is not None:
      icon = '<i class="%s"></i>&nbsp;' % self.icon
    val = "".join([v.html() if hasattr(v, 'inReport') else v for v in self.vals])
    edit = self._report.edit()
    edit.click([self.jsFocus()])
    save = self._report.lock()
    save.click(["%s.draggable( 'disable' );" % self.jqId], ["%s.draggable('enable');" % self.jqId])
    delete = self._report.delete()
    delete.click([self.jsRemove()])
    return '''
      <div %(attr)s>%(icon)s
        <div id="%(htmlId)s_content" autocorrect="off" spellcheck="false" contenteditable=true style="float:left;margin-left:5px;margin-right:10px;">%(content)s</div>
        %(options)s  
      </div>
      ''' % {'attr': self.strAttr(pyClassNames=self.pyStyle), 'icon': icon,
             'content': val, 'htmlId': self.htmlId, 'options': "".join([str(delete), str(save),str(edit)])}


class Row(Html.Html):
  __cssCls = []
  name, category, callFnc = 'Row', 'Layouts', 'row'

  def __init__(self, report, htmlObjs, width, height, data, align, valign, colsWith, closable, resizable, titles, helper, profile):
    if data is not None:
      # Load the different HTML components from a static list
      # This mode will automatically add the inReport to the new components
      htmlObjs = []
      for component in data:
        fnc = getattr(report, component['htmlComponent'])
        parameters = dict(component)
        del parameters['htmlComponent']

        htmlObjs.append(fnc(**parameters))
    self.colsWith = [] if colsWith is None else colsWith
    self.htmlMaps = {}
    super(Row, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    for htmlObj in htmlObjs:
      self.__add__(htmlObj)
    self.align, self.valign, self.closable, self.resizable, self.titles = align, valign, closable, resizable, titles
    self.css({"padding": "5px 0 5px 0", "border-collapse": "collapse", 'table-layout': 'fixed' })

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.vals.append(htmlObj)
    self._addToContainerMap(htmlObj)
    return self

  def get(self, htmlCode):
    """ Return the Html component in the parameter bar """
    return self.__components[htmlCode]

  def html(self):
    """ Return the HTML display of a split container"""
    self.loadStyle()
    self.jsEvents()
    items = ['<div style="width:100%%;display:block;"><table %s><tr>' % self.strAttr(pyClassNames=self.pyStyle)]
    widths = {}
    if self.colsWith:
      for i, _ in enumerate(self.vals):
        widths[i] = 'width:%s' % self.colsWith[i]

    if self.closable:
      if self.titles:
        for i, htmlObj in enumerate(self.vals):
          onclickEvent = "ResizableRow(this, 'col_%s_%s')" % (self.htmlId, i)  # if self.colsWith else "$(\'#col_%s_%s\').children().toggle()" % ( self.htmlId, i)
          items.append('<th style="text-align:left;padding:5px 0 5px 0;%s"><i onclick="%s" style="cursor:pointer;" class="far fa-minus-square"></i>&nbsp;<p style="color:%s;display:inline">%s</p></th>' % (widths.get(i, ''), onclickEvent, self.getColor('danger', 1), self.titles[i].upper()))
      else:
        for i, htmlObj in enumerate(self.vals):
          onclickEvent = "ResizableRow(this, 'col_%s_%s'))" % (self.htmlId, i)  # if self.colsWith else "$(\'#col_%s_%s\').children().toggle()" % ( self.htmlId, i)
          items.append( '<th style="text-align:left;%s"><i onclick="%s" style="cursor:pointer;" class="far fa-minus-square"></i></th>' % (
            widths.get(i, ''), onclickEvent))
      items.append('</tr><tr>')  # $(htmlId).parent().width()
      self.addGlobalFnc("ResizableRow(htmlId, targetId)", '''
         if ( $(htmlId).parent().data('size') == undefined) { $(htmlId).parent().data('size', $(this).parent().width() ) } ; 
         $('#' + targetId).children().toggle(); var styleDisplay = $('#' + targetId).children().css('display') ;
         if ( styleDisplay == 'block') { $(htmlId).parent().width($(htmlId).parent().data('size')) ; }
         else { $(htmlId).parent().width(10) ; } ''')

    for i, htmlObj in enumerate(self.vals):
      extraStyle = 'padding:0 0 0 5px' if i != 0 else 'padding:0'
      items.append( '<td id="col_%s_%s" style="font-size:inherit;line-height:inherit;vertical-align:%s;text-align:%s;%s;%s">%s</td>' % (self.htmlId, i, self.valign, self.align, widths.get(i, ''), extraStyle, htmlObj.html()))
    items.append('</tr></table></div>')
    if self.resizable:
      self._report.jsImports.add('datatables-col-resizable')
      self._report.jsOnLoadFnc.add("%s.colResizable({ liveDrag:true });" % self.jqId)
    return "".join(items)


class Col(Html.Html):
  name, category, callFnc = 'Column', 'Layouts', 'col'

  def __init__(self, report, htmlObjs, position, width, height, align, helper, profile):
    self.position, self.htmlMaps = position, {}
    super(Col, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    if htmlObjs is not None:
      for htmlObj in htmlObjs:
        self.__add__(htmlObj)
    if align == "center":
      self.css({'margin': 'auto', 'display': 'inline-block', 'text-align': 'center'})
    else:
      self.css({'display': 'inline-block'})

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.vals.append(htmlObj)
    self._addToContainerMap(htmlObj)
    return self

  def content(self):
    return self.html()

  def html(self):
    """ Return the HTML display of a split container"""
    self.loadStyle()
    self.jsEvents()
    divStyle = ''
    if self.position == 'bottom':
      self.position = 'center'
      divStyle = ' style="margin:auto"'
    elif self.position == 'middle':
      divStyle = ' style="margin:auto"'
    self.css({"justify-content": self.position})
    return '<div %s><div%s>%s</div></div>' % (self.strAttr(), divStyle, "".join([htmlObj.html() for htmlObj in self.vals]))

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    for i, htmlObj in enumerate(self.vals):
      htmlObj.to_word(document)

  def to_xls(self, workbook, worksheet, cursor):
    for i, htmlObj in enumerate(self.vals):
      try:
        htmlObj.to_xls(workbook, worksheet, cursor)
      except Exception as err:
        cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
        worksheet.write(cursor['row'], 0, str(err), cell_format)
        cursor['row'] += 2


class Grid(Html.Html):
  references, cssCls = {}, ['container-fluid']
  name, category, callFnc = 'Grid', 'Layouts', 'grid'

  def __init__(self, report, htmlObjs, width, height, colsDim, colsAlign, noGlutters, align, helper, profile):
    super(Grid, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.css({'overflow-x': 'hidden', 'padding': 0})
    self.rowsStyle, self.colsStyle, self.noGlutters = {}, {}, noGlutters
    if align == 'center':
      self.css({'margin': 'auto'})
    self.colsDim, self.htmlMaps, self.colsAlign  = [], {}, []
    if colsDim is None:
      colsDim, currDim = [], 0
      for h in range(0, len(htmlObjs)-1):
        currDim += int(12 / len(htmlObjs))
        colsDim.append(int(12 /len(htmlObjs)))
      colsDim.append(12 - currDim)
    for i, htmlObj in enumerate(htmlObjs):
      self.__add__( (htmlObj, colsDim[i]))
    if colsAlign is not None:
      self.colsAlign = colsAlign

  def __add__(self, htmlObjWithDim):
    """ Add items to a container """
    if isinstance(htmlObjWithDim, tuple):
      htmlObj, dim = htmlObjWithDim
    else:
      htmlObj, dim = htmlObjWithDim, 1
    self._addToContainerMap(htmlObj)
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.vals.append(htmlObj)
    self.colsDim.append(dim)
    self.colsAlign.append("left")
    return self

  def jsTogglePanel(self, i):
    if i == 1:
      return '''
       var nextColDim = panel_dims_%(htmlId)s[1];
       var nextColDimTotal = panel_dims_%(htmlId)s[1] + panel_dims_%(htmlId)s[0];
       $(%(jqId)s.find('div')[1]).toggle();
       const panelDisplay = $(%(jqId)s.find('div')[1]).css('display');
       if (panelDisplay == 'block') {var cls = $(%(jqId)s.find('div')[1]).next().attr('class').replace("col-md-" + nextColDimTotal, "col-md-" + panel_dims_%(htmlId)s[1])}
       else {var cls = $(%(jqId)s.find('div')[1]).next().attr('class').replace("col-md-" + panel_dims_%(htmlId)s[1], "col-md-" + nextColDimTotal)}
       $(%(jqId)s.find('div')[1]).next().attr('class', cls)
       ''' % {'jqId': self.jqId, 'htmlId': self.htmlId}

    # TODO: Fix this part
    return "$(%(jqId)s.find('div:nth-child(%(index)s)')).toggle()" % {'jqId': self.jqId, 'index': i}

  def get(self, id):
    """ Return the Html component in the parameter bar """
    return self.vals[id]

  def resize(self):
    """
    Automatically rezise the space for the containers.

    This will rescale based on the number of items and the fact that the max per row is 12
    It will update the colsDim list
    """
    max_size = int(12 / len(self.colsDim))
    self.colsDim = [max_size] * len(self.colsDim)

  def html(self):
    self.loadStyle()
    self.jsEvents()
    items = ['<div %s>' % self.strAttr(pyClassNames=self.pyStyle)]
    items.append('<div class="row%s">' % (' no-gutters' if self.noGlutters else ''))
    dimRow, rowIndex, colPerObj = 0, 1, {}
    for i, htmlObj in enumerate(self.vals):
      if dimRow == 12:
        items.append('</div><div class="row%s">' % (' no-gutters' if self.noGlutters else ''))
        dimRow = 0

      if isinstance(htmlObj, HtmlSelect.Select):
        htmlObj.container = "#%s" % self.htmlId # The container should be defined in this case to be visible
      htmlContent = htmlObj.content() if isinstance(htmlObj, Col) else htmlObj.html()
      items.append('<div class="col col-md-%s text-%s">%s</div>' % (self.colsDim[i], self.colsAlign[i], htmlContent))
      dimRow += 1 if self.colsDim[i] == 'auto' else self.colsDim[i]
      colPerObj[i] = self.colsDim[i]
      rowIndex += 1
      if dimRow > 12:
        raise Exception("BootStrap allow a max of 12 columns per Row")
    self._report.js.getVar("panel_dims_%s" % self.htmlId, colPerObj)
    items.append('</div></div>')
    return "".join(items)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    for i, htmlObj in enumerate(self.vals):
      try:
        htmlObj.to_word(document)
      except Exception as err:
        from docx.shared import RGBColor

        errotTitle = document.add_heading().add_run("Error")
        errotTitle.font.color.rgb = RGBColor(255, 0, 0)
        errotTitle.font.italic = True
        errorParagraph = document.add_paragraph().add_run((str(err)))
        errorParagraph.font.color.rgb = RGBColor(255, 0, 0)
        errorParagraph.font.italic = True

  def to_xls(self, workbook, worksheet, cursor):
    for i, htmlObj in enumerate(self.vals):
      try:
        htmlObj.to_xls(workbook, worksheet, cursor)
      except Exception as err:
        cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
        worksheet.write(cursor['row'], 0, str(err), cell_format)
        cursor['row'] += 2

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val): return True if val == "[" else None

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report=None):
    pass

  @classmethod
  def jsMarkDown(self, vals):
    return '''
      '''


class Tabs(Html.Html):
  name, category, callFnc = 'Tabs', 'Layouts', 'tabs'
  __reqCss = ['bootstrap']
  cssCls = ['nav', 'nav-pills']
  __pyStyle = ['CssDivNoBorder', 'CssBorderTab', 'CssBorderTabSelected']
  htmlObj = None

  def __init__(self, report, htmlObjs, width, height, tabNames, rowsCss, colsCss, closable,
               selectedTab, htmlCode, alwaysReload, encoding, helper, profile):
    super(Tabs, self).__init__(report, [], htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                               heightUnit=height[1], profile=profile)
    self.rowsStyle, self.colsStyle, self.selectedTab = {}, {}, selectedTab
    self.tabNames, self.htmlMaps, self.bespokeTabEvents = [], {}, set()
    if tabNames is None:
      tabNames = list(range(1, len(htmlObjs)+1))
    for i, htmlObj in enumerate(htmlObjs):
      if isinstance(htmlObj, dict):
        if hasattr(htmlObj['value'], 'inReport'):
          self.__add__((htmlObj['value'], htmlObj['name']))
          continue

        tanValue = htmlObj.get('name', htmlObj['value'])
        if hasattr(tanValue, 'decode'):
          tanValue = tanValue.decode(encoding)
        self.__add__((self._report.paragraph(htmlObj['value']), tanValue))
        if htmlObj.get('isActive', False):
          self.selectedTab = tanValue
      else:
        self.__add__((htmlObj, tabNames[i]))
    self.css({'overflow-y': 'hidden', 'overflow-x': 'hidden', 'margin-top': '5px'})
    self.addGlobalVar("tabs_counts_%s" % self.htmlId, len(self.vals))
    for evts in ['click', 'change']:
      # Add the source to the different events
      self.jsFrg(evts, ''' 
        $('#%(htmlId)s li div').removeClass('%(selectedTab)s');
        $(this).find('div').addClass('%(selectedTab)s');
        $('div[name="panel_%(htmlId)s"]').hide(); var tabIndex = $(this).data('index'); var data = %(jsQueryData)s;
        if ('%(htmlCode)s' != 'None') {
          %(windowState)s; %(breadCrumVar)s['params']['%(htmlCode)s'] = data.event_val}
        ''' % {'jsQueryData': self.jsQueryData, 'htmlId': self.htmlId, 'htmlCode': self.htmlCode,
               'selectedTab': self._report.style.cssName(self.pyStyle[2]), 'breadCrumVar': self._report.jsGlobal.breadCrumVar,
               'windowState': self._report.jsChangeUrl("{'%s': data.event_val}" % self.htmlCode)})
    if self.htmlCode is not None:
      if self.htmlCode in self._report.http:
        self.selectedTab = self._report.http[self.htmlCode]
      if self.selectedTab is not None:
        self._report.jsOnLoadFnc.add("%(breadCrumVar)s['params']['%(htmlCode)s'] = '%(selectedTab)s'" % {'selectedTab': self.selectedTab, 'breadCrumVar': self._report.jsGlobal.breadCrumVar,
                                                                                                         'htmlCode': self.htmlCode})
    # Check the tab reloading
    self.alwaysReload = alwaysReload
    self.addGlobalVar("reload_%s" % self.htmlId)

  def jsRefreshTab(self, jsTabName=None, isPyData=True):
    if jsTabName is not None:
      if isPyData:
        jsTabName = json.dumps(jsTabName)
      return 'delete %(htmlId)s_TAB_LOAD[%(jsTabName)s]' % {'htmlId': self.htmlId, 'jsTabName': jsTabName}

    return '%(htmlId)s_TAB_LOAD = {}' % {'htmlId': self.htmlId}

  def jsEvents(self):
    if hasattr(self, 'jsFncFrag'):
      for eventKey, fnc in self.jsFncFrag.items():
        if self.htmlCode is not None:
          fnc.insert(0, self.jsAddUrlParam(self.htmlCode, self.val, isPyData=False))
        jsFnc = self.jsLoading(fnc)
        if getattr(self._report, 'PROFILE', False):
          self._report.jsOnLoadEvtsFnc.add(
            "$('#%(htmlId)s').delegate('li.tab_comp', '%(eventKey)s', function(event){var t0 = performance.now(); %(jsFnc)s; console.log('|Tabs|%(eventKey)s(%(htmlId)s)|'+ (performance.now()-t0))})" % {
              'htmlId': self.htmlId, 'eventKey': eventKey, 'jsFnc': jsFnc})
        else:
          self._report.jsOnLoadEvtsFnc.add("$('#%(htmlId)s').delegate('li.tab_comp', '%(eventKey)s', function(event){%(jsFnc)s})" % {'htmlId': self.htmlId, 'eventKey': eventKey, 'jsFnc': jsFnc})

  def jsShowPanel(self, panelIndex='tabIndex', jsData='data'):
    return "$('#%(htmlId)s_panel_'+ %(panelIndex)s).show() ; " % {'panelIndex': panelIndex, 'htmlId': self.htmlId}

  def jsUpdatePanel(self, panelIndex='tabIndex', jsData='data', unLockOthers=False):
    return '''
          if (typeof %(panelIndex)s === 'undefined') {
              var dummy = $('<div/>'); $(dummy).css('color', "%(whiteColor)s");
              $('#%(htmlId)s').children('li').each(function () {
                  if ($(this).find("div").css("background-color") != dummy.css("color")) { 
                      %(panelIndex)s = $(this).data('index') ; }}) } ;
                      
          for (var key in %(jsData)s) {
            if( %(htmlId)s_MAP_COMPONENTS[key] != undefined) {
              var htmlObj;
              if (%(htmlId)s_MAP_COMPONENTS[key][1].startsWith('$') ) { htmlObj = eval(%(htmlId)s_MAP_COMPONENTS[key][1]) ; }
              else {htmlObj = window[%(htmlId)s_MAP_COMPONENTS[key][1]] ; }
              window[%(htmlId)s_MAP_COMPONENTS[key][0]]( htmlObj, data[key] ) ; } }
          
          if ( %(unLockOthers)s ) {%(htmlId)s_TAB_LOAD = {}}
          $('#%(htmlId)s_panel_' + %(panelIndex)s ).show() ; %(panelIndex)s = undefined ;    
      ''' % {'panelIndex': panelIndex, 'htmlId': self.htmlId, 'jsData': jsData, 'whiteColor': self.getColor('greys', 0),
             'unLockOthers': json.dumps(unLockOthers)}

  @property
  def jqId(self): return "$('#%s li.tab_comp')" % self.htmlId

  @property
  def jsQueryData(self):
    # return the tab name and not the content of the tab
    return "{event_val: $(this).find('div').text(), event_code: '%s'}" % self.htmlId

  @property
  def val(self):
    # return the tab name and not the content of the tab
    return "%(breadCrumVar)s['params']['%(htmlCode)s']" % {'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'htmlCode': self.htmlCode}

  def jsAddTab(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      if (%(tabName)s != ''){
        tabs_counts_%(htmlId)s ++;
        $('#%(htmlId)s').append('<li class="nav-item tab_comp" style="padding:0" data-index=tabs_counts_%(htmlId)s><div class="nav-link" style="cursor:pointer;font-variant:small-caps;font-weight:bold;padding:2px 15px">'+ %(tabName)s +'</div></li>') ;
      }''' % {'tabName': jsData, 'htmlId': self.htmlId}

  def jsDelTab(self, tabName):
    return '''
      var pos = -1;
      $('#%(htmlId)s li').each(function( index ) {
         if( $( this ).text() == '%(tabName)s') { pos = index ;} });
      if (pos != -1) { $('#%(htmlId)s li')[pos].remove(); }
      '''  % {'tabName': tabName, 'htmlId': self.htmlId, 'tabName': tabName}

  def jsSelectNextTab(self, forward=True):
    if self.htmlCode is None:
      raise Exception("The HtmlCode should be defined to use this feature")

    return '''
      var tabNames = %(tabNames)s; var selectedTab = %(breadCrumVar)s['params']['%(htmlId)s'];
      var indexTab = tabNames.indexOf(selectedTab);
      if(%(forward)s){indexTab++} else if(indexTab > 0){indexTab--};
      $('#%(htmlId)s li:eq('+ indexTab +')').trigger('click');
      ''' % {"htmlId": self.htmlId, 'tabNames': self.tabNames, 'breadCrumVar': self._report.jsGlobal.breadCrumVar,
             'forward': json.dumps(forward)}

  def keyboardShortcut(self):
    self._report.keyboard('33', self.jsSelectNextTab()) # pageUp
    self._report.keyboard('34', self.jsSelectNextTab(False))  # pageDown
    return self

  def __add__(self, htmlObjWithDim):
    """ Add items to a container """
    if isinstance(htmlObjWithDim, tuple):
      htmlObj, name = htmlObjWithDim
    else:
      htmlObj, name = htmlObjWithDim, 1
    self._addToContainerMap(htmlObj)
    if hasattr(htmlObj, 'inReport'):
      htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.vals.append(htmlObj)
    self.tabNames.append(name)
    return self

  def jsLoading(self, jsFnc):
    return " var loading = $('#%(htmlId)s_panel_loading'); loading.show() ; %(jsFnc)s " % {'jsFnc': ";".join(jsFnc), 'htmlId': self.htmlId}

  def click(self, jsFncs, tabName=None, refresh=False, excTabs=None):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if not refresh:
      refresh = self.alwaysReload
    if tabName is not None:
      self.bespokeTabEvents.add(tabName)
      self.jsFrg('click', '''
        if (data['event_val'] == %(tabName)s) {
          if((%(htmlId)s_TAB_LOAD[data['event_val']] == undefined) || %(refresh)s) { 
            %(htmlId)s_TAB_LOAD[data['event_val']] = 1; %(jsFnc)s; $('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()} 
          else {$('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()} 
          var resizeEvent = window.document.createEvent('UIEvents');
          resizeEvent.initUIEvent('resize', true, false, window, 0);
          window.dispatchEvent(resizeEvent);
        }''' % {'refresh': json.dumps(refresh), "tabName": json.dumps(tabName), 'jsFnc': ";".join(jsFncs), 'htmlId': self.htmlId})
    elif excTabs is not None:
      self.bespokeTabEvents.add(tabName)
      self.jsFrg('click', '''
        if (!%(excTabs)s.includes(data['event_val'])) {
          if((%(htmlId)s_TAB_LOAD[data['event_val']] == undefined) || %(refresh)s) { 
            %(htmlId)s_TAB_LOAD[data['event_val']] = 1; %(jsFnc)s; $('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()} 
          else {$('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()} 
          var resizeEvent = window.document.createEvent('UIEvents');
          resizeEvent.initUIEvent('resize', true, false, window, 0);
          window.dispatchEvent(resizeEvent);
        }''' % {'refresh': json.dumps(refresh), "excTabs": json.dumps(excTabs), 'jsFnc': ";".join(jsFncs), 'htmlId': self.htmlId})
    else:
      self.jsFrg('click', ''' 
       if((%(htmlId)s_TAB_LOAD[data['event_val']] == undefined) || %(alwaysReload)s) {
          %(htmlId)s_TAB_LOAD[data['event_val']] = 1; %(jsFnc)s; $('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()} 
       else {$('#%(htmlId)s_panel_'+ tabIndex).show(); loading.hide()}  
       var resizeEvent = window.document.createEvent('UIEvents');
       resizeEvent.initUIEvent('resize', true, false, window, 0);
       window.dispatchEvent(resizeEvent);
       ''' % {'alwaysReload': json.dumps(refresh), 'htmlId': self.htmlId, 'jsFnc': ";".join(jsFncs)})
    return self

  def html(self):
    """ Return the HTML representation of a Tabular object """
    self.loadStyle()
    if len(self.bespokeTabEvents) == 0:
      self.click(' ') # Because otherwise the display will not work
    else:
      self.click(' ', excTabs=list(self.bespokeTabEvents))
    self.jsEvents()
    self.addGlobalVar("%s_MAP_COMPONENTS" % self.htmlId, json.dumps(self.htmlMaps))
    self.addGlobalVar("%s_TAB_LOAD" % self.htmlId, json.dumps({}))
    items, tabs = ['<ul %s>' % self.strAttr(pyClassNames=[self.pyStyle[0]])], []
    selectCss, tabCss = self._report.style.cssName(self.pyStyle[2]), self._report.style.cssName(self.pyStyle[1])
    for i, htmlObj in enumerate(self.vals):
      if self.tabNames[i] == self.selectedTab:
        items.append(''' 
            <li id="tab_%(htmlId)s_selected" class="nav-item tab_comp" data-index=%(i)s>
              <div class="%(tabCssCls)s" style="font-size:%(size)s;cursor:pointer;font-variant:small-caps;font-weight:bold;padding:2px 15px">%(tabNames)s</div>
            </li>''' % {'htmlId': self.htmlId, "i": i, 'tabNames': self.tabNames[i], 'tabCssCls': "%s %s" % (tabCss, selectCss), 'size': self._report.pyStyleDfl['headerFontSize']})
        self._report.jsOnLoadEvtsFnc.add("$('#tab_%s_selected').trigger('click')" % self.htmlId)
      else:
        items.append('''
            <li class="nav-item tab_comp" style="padding:0" data-index=%(index)s>
              <div class="%(tabCssCls)s" style="font-size:%(size)s;cursor:pointer;font-variant:small-caps;font-weight:bold;padding:2px 15px">%(name)s</div>
            </li>''' % {'tabCssCls': tabCss, 'index': i, 'name': self.tabNames[i], 'size': self._report.pyStyleDfl['headerFontSize']})
      tabs.append(htmlObj)
    items.append('</ul>')
    self._report.jsOnLoadFnc.add("$('#%(htmlId)s').delegate('span', 'click', function(event) {event.stopPropagation()})" % {'htmlId': self.htmlId})
    for i, tab in enumerate(tabs):
      if self.tabNames[i] == self.selectedTab:
        items.append('<div id="%(htmlId)s_panel_%(index)s" name="panel_%(htmlId)s" style="text-align:center;padding:10px">%(obj)s</div>' % {'htmlId': self.htmlId, 'index': i, 'obj': tab.html() if hasattr(tab, 'html') else tab})
      else:
        items.append('<div id="%(htmlId)s_panel_%(index)s" name="panel_%(htmlId)s" style="text-align:center;display:none;padding:10px">%(obj)s</div>' % {'htmlId': self.htmlId, 'index': i, 'obj': tab.html() if hasattr(tab, 'html') else tab})
    items.append('<div id="%(htmlId)s_panel_loading" style="text-align:center;display:none;border:1px solid %(lightColor)s;padding:10px"><i class="fas fa-spinner fa-spin"></i><br />Loading...</div>' % {'lightColor': self.getColor('greys', 3), 'htmlId': self.htmlId})
    return "".join(items)


class Pills(Tabs):
  cssCls = ['nav', 'nav-pills']
  name, category, callFnc = 'Pills', 'Layouts', 'pills'
  __reqCss = ['bootstrap']
  __pyStyle = ['CssDivNoBorder']


class IFrame(Html.Html):
  name, category, callFnc = 'IFrame', 'Container', 'iframe'
  __reqCss = ['bootstrap']
  __pyStyle = ['CssDivNoBorder']

  def __init__(self, report, url, width, height, helper, profile):
    super(IFrame, self).__init__(report, url, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                 profile=profile)
    self.css({"overflow-x": 'hidden'})

  def __str__(self):
    return "<iframe src='%s' %s frameborder='0' scrolling='no'></iframe>" % (self.vals, self.strAttr(pyClassNames=self.pyStyle))


class Dialog(Html.Html):
  name, category, callFnc = 'DialogMenu', 'Layouts', 'dialogs'
  __reqCss, __reqJs = ['jqueryui', 'datatables', 'datatables-export'], ['jquery', 'datatables', 'datatables-export']

  def __init__(self, report, recordSet, width, widthUnit, height, heightUnit, helper, profile):
    super(Dialog, self).__init__(report, recordSet, width=width, widthUnit=widthUnit, height=height, heightUnit=heightUnit,
                                 profile=profile)
    self.css({"border": '2px solid #F4F4F4'})

  def jsAdd(self, title='data.event_val', isPyData=False):
    if isPyData:
      title = json.loads(title)

    return ''' 
    var dialogWindow = $("<div>");
    var table = $("table");
    dialogWindow.append(table);
    dialogWindow.append('<input type="text">');
    var d = dialogWindow.dialog( { modal: false, title: %(title)s, show: 'puff', fluid: true,
        close: function () {$(this).remove()}, appendTo: "#%(htmlId)s", resizable: false,
        buttons: [{text: "Close", click: function() { $( this ).dialog("close")} } ]
    });
    d.parent().draggable({containment: '#%(htmlId)s'}); 
    event.preventDefault();
    ''' % {'title': title, 'htmlId': self.htmlId}

  def __str__(self):
    return "<div %s></div>" % self.strAttr()


class IconsMenu(Html.Html):
  name, category, callFnc = 'Icons Menu', 'Layouts', 'menu'
  __reqCss, __reqJs = ['jqueryui', 'datatables', 'datatables-export', 'jquery-scrollbar'], ['jquery', 'datatables', 'datatables-export', 'jquery-scrollbar']

  def __init__(self, report, width, height, htmlCode, helper, profile):
    super(IconsMenu, self).__init__(report, None, width=width, widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode,
                                    profile=profile)
    self._jsActions, self._definedActions = {}, []
    self.css( {"margin": "5px 0"})
    self.addGlobalVar("%s_items" % self.htmlId, "{}")

  @property
  def val(self):
    return "%s_items" % self.htmlId

  def jsAction(self, action, icon, tooltip, pyCssCls="CssBigIcon", url=None, jsData=None, jsFncs=None, httpCodes=None):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []

    # Add this to an ajax POST call if an URL is defined
    fnc = self._report.jsPost(url=url, jsData=jsData, jsFnc=jsFncs, httpCodes=httpCodes) if url is not None else ";".join(jsFncs)
    self._jsActions[action] = "<span id='%(htmlId)s_%(action)s' title='%(tooltip)s' class='%(cssStyle)s %(icon)s'></span>" % {
      "icon": icon, "cssStyle": self._report.style.cssCls(pyCssCls), "htmlId": self.htmlId, 'tooltip': tooltip, 'action': action}
    self._report.jsOnLoadFnc.add("$('#%(htmlId)s_%(action)s').on('click', function(event) { %(jsFncs)s; %(htmlId)s_items['%(action)s'] = true; })" % {"htmlId": self.htmlId, "jsFncs": fnc, 'action': action})
    if action not in self._definedActions:
      self._definedActions.append(action)
    return self

  def addSelect(self, action, data, width=150):
    options = []
    for d in data:
      options.append("<option>%s</option>" % d)
    self._jsActions[action] = '<select id="inputState" class="form-control" style="width:%spx;display:inline-block">%s</select>' % (width, "".join(options))
    self._definedActions.append(action)
    return self

  def __str__(self):
    htmlIcons = []
    for action, htmlDef in self._jsActions.items():
      htmlIcons.append(htmlDef)
    return "<div %s>%s</div>" % (self.strAttr(), "".join(htmlIcons))
