"""

"""


from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsInput


class Popup(Html.Html):
  __reqCss, __reqJs = ['bootstrap', 'jquery-scrollbar'], ['jquery', 'jquery-scrollbar']
  name, category, callFnc = 'Popup Container', 'Container', 'popup'
  # _grpCls = CssGrpClsInput.CssClassPopup

  def __init__(self, report, htmlObj, title, color, width, height, withBackground, draggable, margin, profile):
    super(Popup, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                profile=profile)
    self.inputs, self.height, self.width = [], "%s%s" % (height[0], height[1]) if height is not None else "100%", width
    if htmlObj is not None:
      if isinstance(htmlObj, list):
        for obj in htmlObj:
          self.__add__(obj)
      else:
        self.__add__(htmlObj)
    self._title, self.withBackground, self.draggable, self.margin = title, withBackground, draggable, margin
    if color is not None:
      self.css({"color": color})
    if self.withBackground:
      self.frameWidth = "%s%s" % (width[0], width[1])
      self.css({'width': '100%', 'position': 'fixed', 'height': '100%', 'background-color': 'rgba(0,0,0,0.4)',
                'left': 0, 'top': 0, 'margin': 'auto'})
      self.css({'display': 'none', 'z-index': '10000', 'text-align': 'center', 'padding-top': '100px',
                'padding-left': '%s%%' % self.margin, 'padding-right': '%s%%' % self.margin})
      if draggable:
        self._report.jsImports.add('jqueryui')
        self._report.cssImport.add('jqueryui')
        self._report.jsOnLoadFnc.add("$('#%s > table').draggable();" % self.htmlId)
    else:
      self.frameWidth = "100%"
      self.margin = None
      self.css({'position': 'absolute', 'margin': 0, 'padding': 0, 'display': 'none', 'z-index': '10000'})
      if draggable:
        self._report.jsImports.add('jqueryui')
        self._report.cssImport.add('jqueryui')
        self._report.jsOnLoadFnc.add("%s.draggable()" % self.jqId)
    self.set_attrs(name="name", value="report_popup")
    self._report.keyboard(27, "$('div[name=report_popup]').hide()")

  @property
  def title(self):
    if self._title is None:
      raise Exception("No title defined for this popup window")

    return "$('#title_%s span').text()" % self.htmlId

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set too late
    htmlObj.container = "#%s_content" % self.htmlId
    if htmlObj.category in ['Input']:
      self.inputs.append((htmlObj.jqId, htmlObj.placeholder, htmlObj.val, htmlObj.__class__.__name__) )
    self.val.append(htmlObj)
    return self

  def jsSetInputVals(self, jsData):
    jsFncs = []
    for input in self.inputs:
      jsFncs.append("%s(%s, %s['%s'])" % (input[3], input[0], jsData, input[1]))
    return jsFncs

  def jsInputData(self, typeRow='dict'):
    if typeRow == 'dict':
      vals = []
      for input in self.inputs:
        if input[1] is not None:
          vals.append("'%s': %s" % (input[1], input[2]))
      return " [{%s}]" % ",".join(vals)

    return " [%s]" % ",".join([input[2] for input in self.inputs])

  def jsTitle(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''$('#title_%(htmlId)s span').text(%(jsData)s)''' % {'htmlId': self.htmlId, 'jsData': jsData}

  def submit(self, jsFncs, label='Submit'):
    button = self._report.button(label)
    self.__add__(button)
    button.jsFrg('click', "%s;%s" % (";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs, self.jsHide() ) )

  def show(self):
    fncs = []
    for htmlObj in self.vals:
      if getattr(htmlObj, 'dataSrc') is not None and htmlObj.dataSrc['type'] == 'script':
        fncs.append(htmlObj.jsLoadFromSrc(htmlObj.dataSrc.get('jsDataKey')))
      elif getattr(htmlObj, 'dataSrc') is not None and htmlObj.dataSrc['type'] == 'url':
        fncs.append(self._report.jsPost(htmlObj.dataSrc['url']))
    fncs.append("$('#%s').show()" % self.htmlId)
    fncs.append(self.jsResize())
    return ";".join(fncs)

  def jsResize(self):
    return '''
      var resizeEvent = window.document.createEvent('UIEvents');
      resizeEvent.initUIEvent('resize', true, false, window, 0);
      window.dispatchEvent(resizeEvent)''' % {'htmlId': self.htmlId}

  def jsShow(self, x=None, y=20, absolute=False):
    if self.margin is None:
      if x is None:
        x = - self.width / 2
      if absolute:
        return ";".join(["$('#%(htmlId)s').css({'left': %(x)s, 'top': %(y)s})" % {'htmlId': self.htmlId, 'x': x, 'y': y}, super(Popup, self).jsShow(), self.jsResize()])

      return ";".join(["$('#%(htmlId)s').css({'left': event.clientX + %(x)s, 'top': event.clientY + %(y)s})" % {
        'htmlId': self.htmlId, 'x': x, 'y': y}, super(Popup, self).jsShow(), self.jsResize()])

    #TODO: Fix Problem resizing content
    return ";".join(["$('#%(htmlId)s').css({'padding': '10%% %(margin)s%%'})" % {'htmlId': self.htmlId, 'margin': self.margin},
                    super(Popup, self).jsShow(), self.jsResize(), '''
                    if ($('#%(htmlId)s_content').height() > $(window).height()-150){
                      $('#%(htmlId)s_content').css({'height': $(window).height()-150 + 'px'})};
                    ''' % {'htmlId': self.htmlId}])

  def hide(self): return "$('#%s').hide()" % self.htmlId

  def html(self):
    """ Return the HTML display of a split container"""
    self.loadStyle()
    self.jsEvents()

    trTitle, closePopup = '', ''
    if self._title is not None:
      self._report.style.cssCls('CssPopupTableTitle')
      self._report.style.cssCls('CssPopupTableTitleContent')
      trTitle = '''
        <tr>
          <th name="title" id="title_%(htmlId)s" style="height:30px">
            <span style="margin-right:10px">%(title)s</span>
            <i onclick="$('#%(htmlId)s').hide()" style="margin:0 2px 0 2px;cursor:pointer" class="fas fa-window-close"></i>
          </th>
        </tr>''' % {'htmlId': self.htmlId, 'title': self._title}
    else:
      closePopup = '''<i onclick="$('#%(htmlId)s').hide()" style="margin:0 2px 0 2px;cursor:pointer" class="fas fa-window-close"></i>''' % {'htmlId': self.htmlId}

    content = '''
      <table id="%(htmlId)s_table" style="width:%(frameWidth)s;margin:auto">
        %(title)s
        <tr>
          <td style="padding:10px">
            <div style="width:100%%;text-align:right">%(closePopup)s</div>
            <div  class='scroll_content' id="%(htmlId)s_content" style="height:%(height)s;overflow:auto;width:100%%">%(objects)s</div>
          </td>
        </tr>
      </table>''' % {'title': trTitle, 'htmlId': self.htmlId, 'objects': "\n".join([val.html() for val in self.vals]),
                     'height': self.height, "frameWidth": self.frameWidth, 'closePopup': closePopup}

    self._report.jsOnLoadFnc.add(''' 
      $('#%(htmlId)s').on('click', function(e) {if(e.target == this) {$('#%(htmlId)s').hide()}});
      $('.scroll_content').mCustomScrollbar()''' % {"htmlId": self.htmlId})
    return '''<div %s>%s</div>''' % (self.get_attrs(pyClassNames=self.pyStyle), content)

  @property
  def val(self):
    return '$("#%s").html()' % self.htmlId

  def jsUpdate(self, data=''): return '$("#%s").html(%s)' % (self.htmlId, data)

  def to_word(self, document):
    pass
