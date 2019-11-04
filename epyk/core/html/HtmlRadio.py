"""
Module for the HTML radio components
"""

import json

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsList


class Radio(Html.Html):
  __reqJs = ['jquery']
  name, category, callFnc = 'Radio Buttons', 'Buttons', 'radio'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, vals, checked, htmlCode, label, width, height, radioVisible, event,
               withRemoveButton, align, filters, tooltip, radioType, helper, profile):
    # add font awesome only if there is an icon
    hasJsEvents = False
    for rec in vals:
      rec['__radio'] = radioVisible
      if not 'checked' in rec and checked is not None and rec['value'] == checked:
        rec['checked'] = True
      if 'event' in rec:
        hasJsEvents = True
    if withRemoveButton:
      vals.append({'value': '_remove'})
    super(Radio, self).__init__(report, vals, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], globalFilter=filters, profile=profile)
    #
    self.add_label(label, css={"height": "20px", "line-height": "20px", "width": "auto"})
    self.add_helper(helper)

    self._jsStyles = {'tooltip': tooltip}
    cssMod = self._report.style.get("CssRadioButton")
    self._report.style.cssCls("CssRadioButton")
    self._jsStyles['normal'] = cssMod.classname
    self._jsStyles['cssLabel'] = {'display': 'inline-block'} if radioType == 'row' else {'display': 'block'}
    self._jsStyles['cssRadio'] = {'display': 'inline-block', 'margin-top': -1, 'vertical-align': 'middle'}
    cssMod = self._report.style.get("CssRadioButtonSelected")
    self._report.style.cssCls("CssRadioButtonSelected")
    self._jsStyles['selected'] = cssMod.classname
    if htmlCode is not None:
      self._report.htmlCodes[self.htmlCode] = self
    self.css({'display': 'inline-block', 'padding': 0, 'text-align': align})
    for evts in ['click', 'change']:
      # Add the source to the different events
      self.jsFrg(evts, '''
        var data = %(jsQueryData)s;
        $(this).parent().children().attr('class', '%(cssNormalStyle)s');
        $(this).attr('class', '%(cssSelectedStyle)s'); $(this).find('input').prop('checked', true)
        ''' % {'jsVal': self.val, "htmlId": self.htmlId, 'htmlCode': self.htmlCode, 'jsQueryData': self.jsQueryData,
               'cssSelectedStyle': self._jsStyles['selected'], 'cssNormalStyle': self._jsStyles['normal']})

    if event is not None:
      self.change(self._report.jsPost(event['script'], event.get('htmlCodes'), event.get('success', '')))
    elif hasJsEvents:
      for rec in self.vals:
        if 'event' in rec:
          if 'script' in rec['event']:
            self.click(rec['value'], self._report.jsPost(rec['event']['script'], None, isPyData=rec['event'].get('isPyData', True)))
          elif 'url' in rec['event']:
            if rec['event'].get('method', 'POST') == 'POST':
              self.click(self._report.jsPost(rec['event']['url'], None, isPyData=rec['event'].get('isPyData', True), isDynUrl=rec['event'].get('isDynUrl', False)), rec['value'])
            elif rec['event'].get('method', 'POST') == 'GET':
              self.click(self._report.jsGet(rec['event']['url'], None, isPyData=rec['event'].get('isPyData', True), isDynUrl=rec['event'].get('isDynUrl', False)), rec['value'])
            elif rec['event'].get('method', 'POST') == 'LINK':
              self.click(self._report.jsGoTo(rec['event']['url'], isPyData=rec['event'].get('isPyData', False), urlName=rec['event'].get('urlName', '_self')), rec['value'] )

  def tooltip(self, value, location='top'):
    self._jsStyles['tooltip'] = value
    return self

  def initVal(self, val):
    for rec in self.vals:
      rec['checked'] = True if rec['value'] == val else False

  @property
  def id_container(self):
    return self.htmlId

  @property
  def jqId(self):
    return "$('#%s div')" % self.htmlId

  @property
  def jsQueryData(self):
    return "{event_val: $(this).find('input').val(), event_code: '%s'}" % self.htmlId

  @property
  def jqIdChecked(self): return  "$('input[name=input_%s]:checked') " % self.htmlId

  @property
  def val(self): return "$('input[name=input_%s]:checked').val()" % self.htmlId

  def click(self, jsFnc, radioVal=None):
    if isinstance(jsFnc, list):
      jsFnc = ";".join(jsFnc)
    if radioVal is None:
      return super(Radio, self).click(jsFnc)

    return super(Radio, self).click("if (data['event_val'] == %(radioVal)s) {%(jsFnc)s}" % {"radioVal": json.dumps(radioVal), 'jsFnc': jsFnc})

  @property
  def disableFnc(self): return 'event.preventDefault();if($(this).find("input").attr("disabled")) {return {}}'

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty() ; 
      var htmlId = htmlObj.attr('id'); var withRemoveButton = false;
      data.forEach(function(rec){
        if (rec.value.indexOf('_remove') >= 0 ) {withRemoveButton = true}
        else {
          var style = jsStyles.normal; var content = rec.value; var tooltip = "";
          if (rec.tooltip != undefined) {tooltip = rec.tooltip};
          if (rec.label != undefined) {content = rec.label};
          if (!rec.__radio) {var radioDisplay = jsStyles.cssRadio['display'] = 'none'};
          
          var label = $("<label>");
          label.css(jsStyles.cssLabel).attr("title", tooltip).attr("name", htmlId).data("toggle", "tooltip");
          
          var inputRadio = $("<input style='margin-right:5px' type='radio' "+ radioDisplay +" name='input_"+ htmlId +"' value='" + rec.value + "' />");
          inputRadio.css(jsStyles.cssRadio);
          if (rec.checked){inputRadio.prop('checked', true); label.addClass(jsStyles.selected)}
          else {label.addClass(jsStyles.normal)};
          label.append(inputRadio).append($('<p style="display:inline-block;margin:0;padding:0">'+ content +'</p>'));
          htmlObj.append(label);
        }});
      
      htmlObj.find('label').tooltip();
      if (jsStyles.tooltip != ""){ 
        var tip = $('<i class="fas fa-info-circle" title="'+ jsStyles.tooltip +'"></i>');
        tip.tooltip(); htmlObj.append($("<div style='width:100%;text-align:right'></div>").append(tip))}
      if (withRemoveButton) {
        htmlObj.append( "<label name='"+ htmlId +"'><i class='fa fa-times' style='color:red'></i><input type='radio' style='display:none' name='input_"+ htmlId +"' value=''></label>");}''', 'Javascript Object builder')

  def jsDisable(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None, reset=True):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
        var labels = {};
        $('#%(htmlId)s').find('label').each(function(){
          labels[$(this).find('p').text()] = $(this); $(this).find('input').attr('disabled', false)});
        %(jsData)s.forEach(function(rec){
          if (typeof rec !== "object"){rec = {value: rec}};
          if (rec.value in labels){labels[rec.value].find('input').attr('disabled', true)};
        })''' % {'jsData': jsData, 'jsStyles': self._jsStyles, 'htmlId': self.htmlId}

  def jsRemove(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    """
    :example: r.jsSelect("['E']")
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
        %(jsData)s.forEach(function(rec){
          if (typeof rec !== "object"){rec = {value: rec}};
          $('#%(htmlId)s').find('label').each(function(){
            var p = $(this).find('p').text(); if(p == rec.value){ $(this).remove()}})
        })''' % {'jsData': jsData, 'jsStyles': self._jsStyles, 'htmlId': self.htmlId}

  def jsSelect(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    """
    :example: r.jsSelect("['E']")
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      %(jsData)s.forEach(function(rec){
        if (typeof rec !== "object"){rec = {'value': rec}}
        $('#%(htmlId)s').find('label').each(function(){var p = $(this).find('p').text(); if(p == rec.value){$(this).trigger("click")}})
      })''' % {'jsData': jsData, 'jsStyles': self._jsStyles, 'htmlId': self.htmlId}

  def jsAdd(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    """

    :example: c.jsAdd([{"value": 'A', "name": 'Test'}], isPyData=True, isUnique=True)
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      var existingVals = [];
      $('#%(htmlId)s').find('label').each(function(){existingVals.push($(this).find('p').text())});
      var jsStyles = %(jsStyles)s;
      %(jsData)s.forEach(function(rec){
        if (typeof rec !== "object"){rec = {'value': rec}}
        if (existingVals.indexOf(rec.value) == -1){
          if (rec.tooltip === undefined) {rec.tooltip = ''};
          if (rec.label === undefined) {rec.label = rec.value};
            
          var label = $("<label></label>");
          label.css(jsStyles.cssLabel).attr("title", rec.tooltip).attr("name", '%(htmlId)s').data("toggle", "tooltip");
          var inputRadio = $("<input style='margin-right:5px' type='radio' name='input_%(htmlId)s' value='" + rec.value + "' />");
          inputRadio.css(jsStyles.cssRadio);
          if (rec.checked){inputRadio.prop('checked', true); label.addClass(jsStyles.selected)}
          else {label.addClass(jsStyles.normal)};
          label.append(inputRadio).append($('<p style="display:inline-block;margin:0;padding:0">'+ rec.label +'</p>'));
          $('#%(htmlId)s').append(label)
        }
      })''' % {'jsData': jsData, 'jsStyles': self._jsStyles, 'htmlId': self.htmlId}

  def __str__(self):
    return '''<div %(strAttr)s><div></div>%(helper)s</div>''' % {"htmlId": self.htmlId, 'strAttr': self.get_attrs(pyClassNames=['CssDivNoBorder']), "helper": self.helper}


  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    p = document.add_paragraph()
    p.add_run("Selected: ")
    runner = p.add_run(self._report.http.get(self.htmlCode, self.vals))
    runner.bold = True

  def to_xls(self, workbook, worksheet, cursor):
    """
    :link xlxWritter Documentation: https://xlsxwriter.readthedocs.io/format.html
    """
    worksheet.write(cursor['row'], 0, "Selected:")
    worksheet.write(cursor['row'], 1, self._report.http.get(self.htmlCode, self.vals))
    cursor['row'] += 2


class Switch(Html.Html):
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap', 'jquery']
  name, category, callFnc = 'Switch Buttons', 'Buttons', 'switch'
  _grpCls = CssGrpClsList.CssClassSwitch

  def __init__(self, report, recordSet, label, color, size, width, height, htmlCode, profile):
    self.width, self.jsChange, self.size = width[0], '', size
    super(Switch, self).__init__(report, recordSet, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], profile=profile)
    self.add_label(label) # add for
    self.clicks = {'on': [], 'off': []}
    self.labelAttrs = {'margin': '0 10px 0 5px', "display": "inline-block", "vertical-align": "middle", "text-align": "left"}
    self.inputAttrs = {'width': '100px', 'display': 'inline-block', 'height': '20px'}
    self.color = 'inherit' if color is None else color
    self.css({"display": 'inline-block'})
    if htmlCode is not None:
      self._report.htmlCodes[self.htmlCode] = self

  @property
  def val(self): return "$('#%(htmlId)s p').html()" % {'htmlId': self.htmlId}

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, '''var htmlId = htmlObj.attr('id'); 
      if (data.off == data.checked) {$('#'+ htmlId +' input').prop('checked', false); $('#'+ htmlId +' p').html(data.off)}
      else {$('#'+ htmlId +' input').prop('checked', true); $('#'+ htmlId +' p').html(data.on)}; 
      window[htmlId + '_data'] = $('#'+ htmlId +' p').html()''', 'Javascript Object builder')

  def click(self, onFncs=None, offFncs=None):
    if onFncs is not None:
      self.clicks['on'].extend(onFncs)
    if offFncs is not None:
      self.clicks['off'].extend(offFncs)

  def initVal(self, val): self.vals['checked'] = val

  def __str__(self):
    self._report.jsOnLoadFnc.add('''
      $('#%(htmlId)s label').click(function() { 
          if(!$('#%(htmlId)s input').is(':checked')) {$('#%(htmlId)s input').prop('checked', true); %(jsVal)s = '%(val2)s'; %(offFncs)s}
          else {$('#%(htmlId)s input').prop('checked', false); %(jsVal)s = '%(val1)s'; %(onFncs)s};
          %(jsChange)s; $('#%(htmlId)s p').html(%(jsVal)s);
      ''' % {'jsVal': self.jsVal, "htmlId": self.htmlId, 'htmlCode': self.htmlCode,
             'onFncs': ";".join(self.clicks['on']), 'offFncs': ";".join(self.clicks['off']),
             'val1': self.vals['off'], 'val2': self.vals['on'], 'jsChange': self.jsChange})
    if 'text' in self.vals:
      return '''
        <div %s>
          <input type="checkbox"/>
          <label style="width:50px;display:inline-block" for="switch">&nbdp;</label>
          <p style="display:inline-block;margin-left:3px;font-weight:bold" title="%s">%s</p>
        </div>''' % (self.get_attrs(pyClassNames=self.pyStyle), self.vals['text'], self.vals['off'])

    return '''
      <div %s>
        <input type="checkbox" />
        <label style="%s" for="switch">&nbdp;</label>
      </div>''' % (self.get_attrs(pyClassNames=self.pyStyle), ";".join(["%s: %s" % (k, v) for k, v in self.inputAttrs.items()]))

