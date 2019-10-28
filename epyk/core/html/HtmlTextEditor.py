"""
Wrapper to the Codemirror components
"""

import json

from epyk.core.js import JsUtils
from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsText


class Editor(Html.Html):
  name, category, callFnc = 'Code Editor', 'Text', 'editor'
  _grpCls = CssGrpClsText.CssClassEditor
  __reqCss, __reqJs = ['codemirror', 'font-awesome'], ['codemirror', 'font-awesome']
  cssTitle = "CssTitle4"

  def __init__(self, report, vals, title, size, language, width, height, isEditable, htmlCode, options, profile):
    super(Editor, self).__init__(report, vals, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode, profile=profile)
    self.size, self.isEditable, self.strTime, self.title = "%s%s" % (size[0], size[1]), isEditable, None, title
    dflOptions, dftActions = {'lineNumbers': True, 'mode': language}, []
    if not options is None:
      if 'visible' in options:
        dftActions.append("hide")
        del options['visible']

      dflOptions.update(options)
    if not isEditable:
      dflOptions['readOnly'] = 'true'
    self._jsStyles, self._jsActions, self._definedActions = {'language': language, 'options': dflOptions, 'actions': dftActions}, {}, ['run', 'load', 'auto', 'clone', 'save', 'delete']
    self.css({'font-size': self.size})
    self.addGlobalVar('%s_editor' % self.htmlId)

  @property
  def val(self):
    return '%(htmlId)s_editor.getValue()' % {"htmlId": self.htmlId}

  @property
  def jsQueryData(self):
    return "{event_val: %(htmlId)s_editor.getValue(), event_code: '%(htmlId)s'}" % {"htmlId": self.htmlId}

  @property
  def jsClear(self):
    return "%(htmlId)s_editor.setValue('')" % {"htmlId": self.htmlId}

  def trigger(self, event):
    if event in ['load', 'run']:
      self._triggerEvents.add("$('#%(htmlId)s_%(action)s').trigger('click')" % {"htmlId": self.htmlId, "action": event})
    else:
      return super(Editor, self).trigger(event)

  def onDocumentReady(self):
    self.jsUpdateDataFnc = '''
      %(pyCls)s(%(jqId)s, %(htmlId)s_data, %(jsStyles)s); 
      if(%(htmlCode)s != null) {%(breadCrumVar)s['params'][%(htmlCode)s] = %(jsVal)s };
      ''' % {'pyCls': self.__class__.__name__, 'jqId': self.jqId, 'htmlId': self.htmlId, 'htmlCode': json.dumps(self.htmlCode),
             'jsVal': self.val, 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'jsStyles': json.dumps(self._jsStyles)}
    if self.dataSrc is None or self.dataSrc.get('type') != 'url':
      self._report.jsOnLoadFnc.add(self.jsUpdateDataFnc)
    if self.strTime is None:
      self._report.jsOnLoadFnc.add("$('#%s_updated p').text(Today())" % self.htmlId)

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' 
      if (window[htmlObj.attr('id') + '_editor'] == undefined) {
        window[htmlObj.attr('id') + '_editor'] = CodeMirror.fromTextArea(htmlObj.get(0), jsStyles.options)} 
      window[htmlObj.attr('id') + '_editor'].setValue(data); 
      if ($('#'+ htmlObj.attr('id') +'_save').length != 0) {
        window[htmlObj.attr('id') + '_editor'].on('keydown', function(i, e) { 
            if (e.ctrlKey && e.keyCode == 83) { 
              e.preventDefault(); $('#'+ htmlObj.attr('id') +'_save').trigger('click')} 
        })
      };
      jsStyles.actions.forEach(function(rec){
        if (rec == 'hide'){$(window[htmlObj.attr('id') + '_editor'].getWrapperElement()).hide()}
      });
      window[htmlObj.attr('id') + '_editor'].getGutterElement().style["background"] = "inherit"; 
      window[htmlObj.attr('id') + '_editor'].getWrapperElement().style["background"] = "inherit";
      window[htmlObj.attr('id') + '_editor'].getWrapperElement().style["color"] = "inherit"; 
      window[htmlObj.attr('id') + '_editor'].getWrapperElement().style["overflow"] = "hidden"; 
      window[htmlObj.attr('id') + '_editor'].getWrapperElement().style["height"] = "100%"''')

  def jsAction(self, jsFncs, icon, pyCssCls, tooltip, action):
    """
    Define the event on the editor when the save is clicked.
    This will call a Ajax service
    .
    :return: The object itself
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if action not in self._definedActions:
      self._definedActions.append(action)
    self._report.style.cssCls(pyCssCls)
    self._jsActions[action] = "<span id='%(htmlId)s_%(action)s' title='%(tooltip)s' class='%(cssStyle)s %(icon)s'></span>" % {
      "icon": icon, "cssStyle": self._report.style.cssName(pyCssCls), "htmlId": self.htmlId, 'tooltip': tooltip, 'action': action}
    self._report.jsOnLoadFnc.add("$('#%(htmlId)s_%(action)s').on('click', function(event) {%(jsFncs)s})" % {"htmlId": self.htmlId, "jsFncs": ";".join(jsFncs), 'action': action})
    return self

  # --------------------------------------------------------------------------------------------------------------
  #                                   EDITOR STANDARD EVENTS
  #
  # None of those functions are based on an Ajax call as I do not thing they are supposed to do something special in case of
  # success or failure of an internal event. Problems are tackled in the standard way using the epyk popup message (and the status for the color)
  def save(self, jsFncs, icon='fas fa-save', pyCssCls="CssSmallIcon", tooltip='click to save changes'):
    """
    :example: >>> editor.save( report.jsPost( "/reports/create/script", [editor]) )
    :wrap jsAction:
    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs = ["var data = %(data)s;" % {"data": self.jsQueryData}] + jsFncs
    return self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'save')

  def delete(self, jsFncs, icon='fas fa-times-circle', pyCssCls="CssSmallIconRed", tooltip='click to delete the function'):
    return self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'delete')

  def run(self, jsFncs, icon='fas fa-play', pyCssCls="CssSmallIcon", tooltip='Run button on the Editor Component'):
    return self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'run')

  def clone(self, jsFncs, icon='fas fa-copy', pyCssCls="CssSmallIcon", tooltip='Create a copy of the script'):
    return self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'clone')

  def show(self, jsFncs=None, icon='fas fa-eye', pyCssCls="CssSmallIcon", tooltip='Show / Hide the code'):
    if jsFncs is None:
      jsFncs = []
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return self.jsAction(["$(window['%s_editor'].getWrapperElement()).toggle()" % self.htmlId] + jsFncs, icon, pyCssCls, tooltip, 'show')

  def load(self, jsFncs, icon='fas fa-sync', pyCssCls="CssSmallIcon", tooltip='Load button on the Editor Component', interval=5000):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if self.strTime is None:
      jsFncs.append("$('#%s_updated p').text(Today())" % self.htmlId)
    self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'load')
    jsFncsAuto = ['''
          $(this).toggleClass('fa-pulse');
          if (window['%(htmlId)s_interval'] == undefined) { window['%(htmlId)s_interval']  = setInterval(  function() { $("#%(htmlId)s_load").trigger('click'); }, %(interval)s ); }
          else {
            if( $(this).hasClass('fa-pulse') ) {window['%(htmlId)s_interval']  = setInterval( function() { $("#%(htmlId)s_load").trigger('click'); }, %(interval)s ); }
            else { clearInterval( window['%(htmlId)s_interval'] )}} ; ''' % {'interval': interval, "htmlId": self.htmlId}]
    return self.jsAction(jsFncsAuto, "fas fa-clock", pyCssCls, "Auto Update button on the Editor Component", 'auto')

  def setTime(self, strTime):
    self.strTime = strTime
    return self

  def download(self, jsFncs='', icon='fas fa-file-download', pyCssCls="CssSmallIcon", tooltip='Download temporary version of the script'):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append("event.stopPropagation(); %s; return false;" % self._report.jsDownload(fileName="tempScript.py", jsData="window['%s_editor'].getValue()" % self.htmlId))
    return self.jsAction(jsFncs, icon, pyCssCls, tooltip, 'clone')

  def __str__(self):
    events = []
    for action in self._definedActions:
      if action in self._jsActions:
        events.append(self._jsActions[action])

    cssMod, title4 = self._report.style.get(self.cssTitle), ""
    if cssMod is not None:
      self._report.style.cssCls(self.cssTitle)
      title4 = cssMod.classname
    self._report.style.cssCls("CssSmallIcon")
    return '''
      <div style="display:inline-block;width:100%%;padding:5px">
        %(events)s
        <span class="%(title4)s" style="display:inline-block;width:200px;padding-left:10px">%(title)s</span>
        <span id='%(htmlId)s_updated' style='float:right;font-style:italic;margin:7px 10px 0 0;display:inline-block:width:100%%'>
            <i style="margin:0 5px 0 0" class="fas fa-clock %(cssStyle)s"></i>
            Last update: <p style="display:inline-block">%(strTime)s</p>
        </span>
      </div>
      <textarea %(attr)s>%(vals)s</textarea>
    ''' % {'attr': self.strAttr(pyClassNames=self.defined), "vals": self.vals, 'htmlId': self.htmlId,
           "cssStyle": self._report.style.cssName("CssSmallIcon"),
           'strTime': self.strTime, 'events': "".join(events), "title": self.title, "title4": title4}


class Console(Html.Html):
  name, category, callFnc = 'Python Cell Runner', 'Text', 'pytestcell'
  __reqCss, __reqJs = ['codemirror'], ['codemirror']

  def __init__(self, report, vals, size, width, height, isEditable, htmlCode, profile):
    super(Console, self).__init__(report, vals, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode, profile=profile)
    self.size, self.isEditable = "%s%s" % (size[0], size[1]), isEditable
    self._jsRun, self._jsSave = '', ''
    self.addGlobalVar("%s_count" % self.htmlId, "0")
    self.css({'font-size': self.size, 'padding': '10px', "min-height": "30px", "font-family": "Arial, monospace"})

  @property
  def val(self):
    return '%(htmlId)s_editor.getValue()' % {"htmlId": self.htmlId}

  @property
  def jsQueryData(self):
    return "{ event_out: $('#%(htmlId)s_result_data').text(), event_val: %(htmlId)s_editor.getValue(), event_code: '%(htmlId)s' }" % {'htmlId': self.htmlId}


  # --------------------------------------------------------------------------------------------------------------
  #                                   EDITOR STANDARD EVENTS
  #
  # Those are already embedding an ajax call as b default the return of those call will change the display
  # Make sure you are not calling a Ajax call within an AJax call, event engine should remain simple
  # Remember PEP20: Simple is better than complex.
  def run(self, url=None, jsData=None, jsFncs=None, httpCodes=None, tooltip="Run the line"):
    """
    Add an event action to the console object.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs] if jsFncs is not None else []
    jsFncs = [
      "if (!data.status){$('#%(htmlId)s_result_data').css('color', '%(redColor)s')} else {$('#%(htmlId)s_result_data').css('color', '%(blackColor)s')}" % {"htmlId": self.htmlId, 'redColor': self.getColor('redColor', 4), 'blackColor': self.getColor('greyColor', 8) },
      "%(htmlId)s_count ++; $('#%(htmlId)s_counter').text( 'In [ '+ %(htmlId)s_count +']')" % {"htmlId": self.htmlId},
      "$('#%(htmlId)s_result_data').text(data.output); $('#%(htmlId)s_print_data').text(data.print);" % {"htmlId": self.htmlId}] + jsFncs + ["$('#%(htmlId)s_result').show();$('#%(htmlId)s_print').show();" % {"htmlId": self.htmlId} ]
    self._jsRun = (self._report.jsPost(url=url, jsData=jsData, jsFnc=jsFncs, httpCodes=httpCodes) if url is not None else ";".join(jsFncs), tooltip)
    return self

  def save(self, url=None, js_data=None, js_fncs=None, httpCodes=None, tooltip="Save the run"):
    """
    Add an event action to the console object to save the result of the In and out.
    """
    if not isinstance(js_fncs, list):
      js_fncs = [js_fncs] if js_fncs is not None else []
    self._jsSave = (self._report.jsPost(url=url, jsData=js_data, jsFnc=js_fncs, httpCodes=httpCodes) if url is not None else ";".join(js_fncs), tooltip)
    return self

  def __str__(self):
    runButton, saveButton = '', ''
    if self._jsRun != '':
      self._report.jsOnLoadFnc.add('''
        var %(htmlId)s_editor = CodeMirror.fromTextArea( $('#%(htmlId)s').get(0), {placeholder: "report.myFncs()", lineNumbers: true, mode: 'python'} ) ;
        %(htmlId)s_editor.setSize(null, 30); %(htmlId)s_editor.getWrapperElement().style["line-height"] = "1.5"; %(htmlId)s_editor.refresh() ;
        %(htmlId)s_editor.on('keydown', function(i, e) { 
            if (e.keyCode  == 13) { var data = %(data)s ; e.preventDefault(); %(run)s ;} 
            else {
              $('#%(htmlId)s_result_data').text(''); $('#%(htmlId)s_print_data').text('');
              $('#%(htmlId)s_result').hide(); $('#%(htmlId)s_print').hide();}
        }) ;
        $('#%(htmlId)s_run').on('click', function(event) {  var data = %(data)s ; %(run)s ; })''' % {"htmlId": self.htmlId, "run": self._jsRun[0], 'data': self.jsQueryData})
      self._report.style.cssCls('CssStdIcon')
      runButton = '<i title="%(tooltip)s" id="%(htmlId)s_run" class="%(iconCss)s fas fa-caret-right"></i>' % {'tooltip': self._jsRun[1], "htmlId": self.htmlId, "iconCss": self._report.style.cssName('CssStdIcon')}
    if self._jsSave != '':
      self._report.jsOnLoadFnc.add('''
        $('#%(htmlId)s_save').on('click', function(event) {  var data = %(data)s ; %(save)s ; })''' % {
        "htmlId": self.htmlId, "save": self._jsSave[0], 'data': self.jsQueryData})
      self._report.style.cssCls('CssOutIcon')
      saveButton = '<i title="%(tooltip)s" id="%(htmlId)s_run" class="%(iconCss)s far fa-save"></i>' % {'tooltip': self._jsSave[1], "htmlId": self.htmlId, "iconCss": self._report.style.cssName('CssOutIcon')}
    self._report.style.cssCls('CssTdEditor')
    return '''
      <table style="width:100%%;margin-top:10px;padding:5px 0 5px 10px">
        <tr>
          <td style="height:100%%;width:100px;border-left:5px solid %(blueColor)s;vertical-align:middle;color:%(blueColor)s"> 
            <span title="count number of runs" id="%(htmlId)s_counter" >In [ 0 ]</span> 
            %(runButton)s
          </td>
          <td class="%(tdRunCss)s"><textarea %(attr)s></textarea></td>
        </tr>
        <tr style="height:3px;display:inline-block"></tr>
        <tr style="display:none" id="%(htmlId)s_result">
          <td style="padding-top:10px;padding-bottom:10px;height:100%%;width:100px;border-left:5px solid blue;vertical-align:middle;color:red"> 
            <span title="Number of store results">Out [ 0 ]</span>  
            %(saveButton)s
          </td>
          <td class="%(tdRunCss)s" id="%(htmlId)s_result_data"></td>
        </tr>
        <tr style="display:none;" id="%(htmlId)s_print">
          <td colspan=2 style="height:100px;">
            <div style="width:100%%;height:100%%;background-color:%(blackColor)s;color:%(whiteColor)s;text-align:left;padding:5px;margin-top:10px" id="%(htmlId)s_print_data" >
              Server logs generated from the print command
            </div>
          </td>
        </tr>
      </table>
      ''' % {'attr': self.strAttr(), 'htmlId': self.htmlId, 'runButton': runButton, 'tdRunCss': self._report.style.cssName('CssTdEditor'), 'saveButton': saveButton,
             'blackColor': self.getColor('greys', 9), 'whiteColor': self.getColor('greys', 0),
             'redColor': self.getColor('danger', 1), 'blueColor': self.getColor('colors', 6)}


class Tags(Html.Html):
  name, category, callFnc = 'Tags', None, 'tags'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, vals, title, icon, size, width, height, htmlCode, profile):
    super(Tags, self).__init__(report, vals, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                               code=htmlCode, profile=profile)
    self.title, self.icon = title, icon
    self.css({"margin-top": "5px", "font-size": "%s%s" % (size[0], size[1]), "font-family": report.style.defaults.font.family})

  @property
  def val(self):
    return "%(breadCrumVar)s['params']['%(htmlId)s']" % {"htmlId": self.htmlId, "breadCrumVar": self._report.jsGlobal.breadCrumVar}

  def jsEmpty(self):
    return "%(breadCrumVar)s['params']['%(htmlId)s'] = []; $('#%(htmlId)s_tags').text('')" % {"htmlId": self.htmlId, "breadCrumVar": self._report.jsGlobal.breadCrumVar}

  def jsAdd(self, jsData):
    jsData = JsUtils.jsConvertData(jsData, None)
    self.addGlobalFnc('RemoveSelection(srcObj, htmlId)', 'srcObj.parent().remove()',
       fncDsc="Remove the item from the Tags Html component but also from the underlying javascript variable")
    return '''
      $('#%(htmlId)s_tags').append("<span style='margin:2px;background:%(baseColor)s;color:%(whiteColor)s;border-radius:8px;1em;vertical-align:middle;display:inline-block;padding:0 2px 1px 10px;cursor:pointer'>"+ %(jsData)s +"<i onclick='RemoveSelection($(this), \\\"%(htmlId)s\\\")' style='margin-left:10px' class='far fa-times-circle'></i></span>")
      ''' % {"htmlId": self.htmlId, "jsData": jsData, 'whiteColor': self.getColor('greys', 0), "baseColor": self.getColor("colors", 9)}

  def __str__(self):
    return '''
      <div %(attr)s>
        <div style='margin:0;display:inline-block;vertical-align:middle;width:90px;float:left;padding:2px 5px 0 5px;height:30px;border:1px solid %(greyColor)s'>
          <i class="%(icon)s" style="margin-right:10px"></i>%(title)s</div>
        <div id='%(htmlId)s_tags' style='padding:2px 5px 0 5px;border:1px solid %(greyColor)s;height:30px'></div>
      </div>''' % {"attr": self.strAttr(pyClassNames=self.defined), "title": self.title, 'icon': self.icon,
                   'htmlId': self.htmlId, 'greyColor': self.getColor("greys", 2)}
