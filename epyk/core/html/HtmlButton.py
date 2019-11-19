"""

"""

import re
import json

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls
from epyk.core.css.groups import CssGrpClsButton


class Button(Html.Html):
  __reqCss, __reqJs = ['font-awesome', 'bootstrap'], ['font-awesome', 'bootstrap', 'jquery']
  name, category, callFnc = 'Button', 'buttons', 'button'

  # CSS Classes
  _grpCls = CssGrpClsButton.CssClassButton

  def __init__(self, report, text, icon, size, width, height, htmlCode, tooltip, profile, options):
    super(Button, self).__init__(report, text, code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], profile=profile)
    # Add the component icon
    self.add_icon(icon, css={"font-size": '10px'})
    self.add_label(text, css={'margin': '1px auto', "float": 'right', 'cursor': 'inherit', 'width': 'auto', 'height': 'auto'})

    #
    self.css({"cursor": 'pointer', 'font-size': "%s%s" % (size[0], size[1])})
    self.__battr, self.groupId = {}, options.get("group")

    if self.groupId is not None:
      self.attr['name'] = self.groupId

    if tooltip is not None:
      self.tooltip(tooltip)
    self.set_attrs(name="data-count", value=0)

  @property
  def jsQueryData(self):
    """
     Python function used in the javascript side to get an object with all the information of the component during an event.
     Basically this function will allow to get all the mandatory detail for an Ajax call
    """
    if self._code is not None:
      return "{event_val: $(this).html(), %s: $(this).html(), event_groupId: '%s', event_count_click: $(this).data('count')+1}" % (self._code, self.groupId)

    return "{event_val: this.innerHTML, event_groupId: '%s', event_count_click: $(this).data('count')+1}" % self.groupId

  @property
  def _js__builder__(self):
    return "htmlObj.innerHTML = data"

  def disable(self, background_color=None, color=None):
    """

    :param background_color:
    :param color:

    :return:
    """
    css_pmts = {"cursor": "not-allowed"}
    if background_color is not None:
      css_pmts["background"] = background_color
    if color is not None:
      css_pmts["color"] = color
    self.css(css_pmts)
    self.attr['disabled'] = True
    return self

  def click(self, jsFncs, profile=False):
    return self.on("click", jsFncs, profile)

    #if not isinstance(js_fnc, list):
    #  js_fnc = [js_fnc]
    #return super(Button, self).click(self.dom.onclick(js_fnc).toStr())

    # if self.groupId:
    #   js_fnc.append('''
    #     var count = $(this).data('count')+1; $(this).data('count', count);
    #     $("button[name='%(groupId)s']").css({'background-color': 'white', 'color': '%(color)s'});
    #     $(this).css({'background-color': '%(color)s', 'color': 'white'})''' % {"color": self.color, 'groupId': self.groupId})
    # else:
    #   js_fnc.append("var count = $(this).data('count')+1; $(this).data('count', count)")
    # return super(Button, self).click(js_fnc)

  def unClick(self, jsFncs):
    if not 'click' in self.jsFncFrag:
      raise Exception("click event should be fully defined first")

    clickFncs = ";".join(self.jsFncFrag['click'] + ["$(this).data('isChecked', true); $(this).css({'color': '%s', 'background': '%s'})" % (self.getColor('colors', 0), self.color)])
    self.jsFncFrag['click'] = ["if(!$(this).data('isChecked') || ($(this).data('isChecked') === undefined)){%s} else {$(this).css({'color': '%s', 'background': 'inherit'}); $(this).data('isChecked', false); %s}" % (clickFncs, self.color, ";".join(jsFncs))]
    return self

  def color(self, color):
    """
    Change the color of the button background when the mouse is hover
    """
    self.css({"border": "1px solid %s" % color})
    self.set_attrs(name="onmouseover", value="this.style.backgroundColor='%s';this.style.color='white'" % color)
    self.set_attrs(name="onmouseout", value="this.style.backgroundColor=\'white\';this.style.color=\'%s\';" % color)
    return self

  def __str__(self):
    return '<button %s></button>' % (self.get_attrs(pyClassNames=self.defined))

  @staticmethod
  def matchMarkDown(val):
    return val.startswith("[button ")

  @classmethod
  def jsMarkDown(self, vals):
    return '[button url=""](%s)' % vals

  @classmethod
  def to_markdown(cls, val, regExpResult, rptObj):
    res = re.search('\[button url="(.*)"\]\((.*)\)', val)
    if res is not None:
      if rptObj is not None:
        getattr(rptObj, 'button')(res.group(2)).goTo(res.group(1))
      return ["rptObj.ui.%s.button('%s').goTo('%s')" % (cls.category, res.group(2), res.group(1))]

  # No export to this component as no interactivity is expected
  def to_word(self, document): pass
  def to_xls(self, workbook, worksheet, cursor): pass
  def to_ppt(self, workbook, worksheet, cursor): pass


class Checkbox(Html.Html):
  name, category, callFnc = 'Check Box', 'Buttons', 'checkbox'
  __reqCss, __reqJs = ['font-awesome', 'bootstrap'], ['font-awesome', 'bootstrap', 'jquery']

  # CSS Class
  _grpCls = CssGrpClsButton.CssClassButtonCheckBox

  def __init__(self, rptObj, records, title, color, width, height, align, htmlCode, filters, tooltip, icon, options, profile):
    if rptObj.http.get(htmlCode) is not None:
      selectedVals = set(rptObj.http[htmlCode].split(","))
      for rec in records:
        if rec["value"] in selectedVals:
          rec["checked"] = True
    super(Checkbox, self).__init__(rptObj, records, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                       heightUnit=height[1], globalFilter=filters, profile=profile)
    # Add the component title
    self.add_title(title)
    self.css({'text-align': align, 'color': 'inherit' if color is None else color, 'padding': '5px'})
    self._jsStyles = {"tooltip": tooltip, "icon": icon} # fas fa-circle fas fa-check
    self.selectAll = options.get("all_selected", False)

  def tooltip(self, value, location='top'):
    self._jsStyles['tooltip'] = value
    return self

  @property
  def val(self):
    return "%(breadCrumVar)s['params']['%(htmlCode)s']" % {"htmlCode": self.htmlId, 'breadCrumVar': self._report.jsGlobal.breadCrumVar}

  @property
  def jqId(self):
    return "$('#%s div[name=\"checks\"]')" % self.htmlId

  @property
  def jsQueryData(self):
    if self.htmlCode is not None:
      return "{event_label: $(this).text(), %s: %s, event_type: $(this).find('span').data('content'), event_val: isChecked, event_code: '%s'}" % (self.htmlCode, self.val, self.htmlId)

    return "{event_label: $(this).text(), event_type: $(this).find('span').data('content'), event_val: isChecked, event_code: '%s'}" % self.htmlId

  def jsDisable(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None, reset=True):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
        const ldata = %(jsData)s;
        %(jqId)s.find('span').each(function(){
          var pItem = $(this).next(); 
          if(%(reset)s == true) {pItem.removeClass("%(disableCls)s")};
          if(($(this).find("i").attr("class") !== undefined) && (%(reset)s == true) && ($(this).find("i").attr("class").includes('fas fa-times'))){$(this).html('<div style="width:16px;display:inline-block">&nbsp;</div>') };
          if (ldata.indexOf(pItem.text()) > -1){
            var bcIndex = %(breadCrumVar)s['params']['%(htmlCode)s'].indexOf(pItem.text());
            if(bcIndex > -1) {delete %(breadCrumVar)s['params']['%(htmlCode)s'].splice(bcIndex, 1)};
            $(this).html('<i class="fas fa-times %(disableCls)s"></i>'); pItem.addClass("%(disableCls)s")}
        })''' % {'jsData': jsData, 'jqId': self.jqId, 'disableCls': self._report.style.cssName("CssLabelContainerDisabled"),
                 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'htmlCode': self.htmlId, 'reset': json.dumps(reset)}

  def jsAdd(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None, isUnique=False):
    """

    :example: c.jsAdd([{"value": 'A', "name": 'Test'}], isPyData=True, isUnique=True)
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      var existingCols = {};
      if (%(unique)s){%(jqId)s.find('span').each(function(){
        var pItem = $(this); 
        existingCols[pItem.data('content')] = true})};
      %(jsData)s.forEach(function(rec){
        if ((!%(unique)s) || (%(unique)s && (!(rec.value in existingCols))) ){
          var style = {'margin': 0, 'color': rec.color, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'};
          var strCss = []; for (key in style) { strCss.push( key + ":" + style[key])};
          checkData = '&nbsp;';
          if (rec.checked){var checkData = '<i class="'+ %(jsStyles)s.icon + '" style="margin:2px"></i>'};
          var spanContent = '<span data-content="'+ rec.value + '" style="width:16px;display:inline-block;float:left;margin:0">'+ checkData +'</span><p style="margin:0" title="'+ rec.dsc + '">' + rec.name + '</p>';
          %(jqId)s.append($('<label style="' + strCss.join(";") + '">'+ spanContent +'</label>'))}
      })''' % {'jsData': jsData, 'jsStyles': json.dumps(self._jsStyles), 'jqId': self.jqId, 'unique': json.dumps(isUnique)}

  def jsRemove(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    """

    :example: c.jsRemove([1, "A"], isPyData=True)
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      const ldata = %(jsData)s;
      if (ldata === true) {%(jqId)s.empty(); %(breadCrumVar)s['params']['%(htmlCode)s'] = []}
      else {
        %(jqId)s.find('span').each(function(){
          var pItem = $(this).next(); var bcIndex = %(breadCrumVar)s['params']['%(htmlCode)s'].indexOf(pItem.text());
          if(bcIndex > -1) {delete %(breadCrumVar)s['params']['%(htmlCode)s'].splice(bcIndex, 1)};
          if (ldata.indexOf($(this).data('content')) > -1){$(this).parent().remove()}
        })}''' % {'jsData': jsData, 'jqId': self.jqId, 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'htmlCode': self.htmlId}

  def jsItemState(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    """

    :example: c.jsItemState(jsData=True, isPyData=True)
    :example: c.jsItemState(jsData=False, isPyData=True)
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      var ldata = %(jsData)s;
      %(jqId)s.find('span').each(function(){
        var itemCode = $(this).data('content');
        if(typeof ldata === "boolean"){
          if (ldata === true && $(this).find("i").attr("class") === undefined){$(this).trigger("click")}
          if (!ldata && $(this).find("i").attr("class") !== undefined){$(this).trigger("click")}}
        else if (ldata.indexOf(itemCode) > -1){if ($(this).find("i").attr("class") === undefined){$(this).trigger("click")}}
      }) ''' % {'jsData': jsData, 'jqId': self.jqId}

  def onDocumentLoadFnc(self):
    """ Pure Javascript onDocumentLoad Function """
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty() ;
      %(breadCrumVar)s['params'][htmlObj.attr('id')] = [];
      data.forEach(function(rec){
        if (rec.color == undefined) {rec.color = 'inherit'}
        var style = {'margin': 0, 'color': rec.color, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'};
        if (rec.style != undefined) { for (key in rec.style) { style[key] = rec.style[key] }} ;
        if (rec.dsc == undefined) { rec.dsc = ''}
        if (rec.name == undefined) { rec.name = rec.value}
        var strCss = []; for (key in style) { strCss.push( key + ":" + style[key])};
        if (rec.checked == true) { 
          %(breadCrumVar)s['params'][htmlObj.attr('id')].push(rec.value );
          var spanContent = '<span data-content="' + rec.value + '" style="display:inline-block;float:left;margin:0"><i class="'+ jsStyles.icon + '" style="margin:2px"></i></span><p style="margin:0;padding:0" title="'+ rec.dsc + '">' + rec.name + '</p>'; }
        else {var spanContent = '<span data-content="'+ rec.value + '" style="width:16px;display:inline-block;float:left;margin:0">&nbsp;</span><p style="margin:0" title="'+ rec.dsc + '">' + rec.name + '</p>';}     
        htmlObj.append($('<label style="' + strCss.join(";") + '">'+ spanContent +'</label>'))}); htmlObj.find("p").tooltip(); 
        if (jsStyles.tooltip != ""){ 
          var tip = $('<i class="fas fa-info-circle" style="right:0" title="'+ jsStyles.tooltip +'"></i>') ;
          tip.tooltip(); htmlObj.append($("<div style='width:100%%;text-align:right'></div>").append(tip) )}
      ''' % {'breadCrumVar': self._report.jsGlobal.breadCrumVar}, 'Javascript Object builder')

  def jsEvents(self):
    if hasattr(self, 'jsFncFrag'):
      for eventKey, fnc in self.jsFncFrag.items():
        if self.htmlCode is not None:
          fnc.insert(0, self.jsAddUrlParam(self.htmlCode, self.val, isPyData=False))
        self._report.jsOnLoadEvtsFnc.add('''
          $( document ).on('%(eventKey)s', '#%(htmlId)s label', function(event) {
            if(($(this).find("i").attr("class") !== undefined) && ($(this).find("i").attr("class").includes('fas fa-times'))) {return {}};
            var useAsync = false; var isChecked = false; var htmlContent = $(this).find('span').find('i').length; 
            if (htmlContent == 0) {$(this).find('span').html('<i class="%(icon)s" style="padding:2px"></i>'); isChecked = true} else {$(this).find('span').html('<div style="width:16px;display:inline-block">&nbsp;</div>')}
            var data = %(data)s ; var returnVal = undefined;
            %(jsInfo)s; %(jsFnc)s; 
            if (!useAsync) {
              var body_loading_count = parseInt($('#body_loading span').text()); $('#body_loading span').html(body_loading_count - 1);
              if ($('#body_loading span').html() == '0') {$('#body_loading').remove()} }
            if (returnVal != undefined) {return returnVal}
          })''' % {'htmlId': self.htmlId, 'eventKey': eventKey, 'data': self.jsQueryData,
                   'jsFnc': ";".join([f for f in fnc if f is not None]), 'icon': self._jsStyles['icon'],
                   'jsInfo': self._report.jsInfo('process(es) running', 'body_loading')})

  def __str__(self):
    if self.selectAll:
      self.addGlobalFnc("CheckBoxSelectAll(event, srcObj, htmlId)", '''
        $(srcObj).find('div').toggleClass("fa-check");
        var ldata = $(srcObj).find('div').hasClass("fa-check");
        $('#'+ htmlId).find('span').each(function(){
          var itemCode = $(this).data('content');
          if(typeof ldata === "boolean"){
            if (ldata === true && $(this).find("i").attr("class") === undefined){$(this).trigger("click")}
            if (!ldata && $(this).find("i").attr("class") !== undefined){$(this).trigger("click")}}
          else if (ldata.indexOf(itemCode) > -1){if ($(this).find("i").attr("class") === undefined){$(this).trigger("click")}}
        })''')
      selectTag = '''
        <div onclick='event.stopPropagation();CheckBoxSelectAll(event, this, "%(htmlId)s");' style='vertical-align:middle;white-space:nowrap;margin-bottom:5px;cursor:pointer;padding:0'>
          <div style='box-sizing:border-box;margin:0;padding:0;border:1px solid %(color)s;font-size:10px;width:11px;height:11px;display:inline-block;color:%(color)s' class="fas">&nbsp;</div>
          <label style='cursor:inherit;margin:0;padding:0;font-style:italic;color:%(color)s;white-space:nowrap'>Select All</label>
        </div>''' % {"color": self.getColor("colors", 5), 'htmlId': self.htmlId}

    return '<div %(strAttr)s><div name="checks"></div></div>' % {'strAttr': self.get_attrs(pyClassNames=['CssDivNoBorder'])}

  def to_word(self, document):
    from docx.shared import RGBColor

    selections = self._report.http.get(self.htmlCode).split(',')
    for rec in self.vals:
      p = document.add_paragraph(style='ListBullet')
      runner = p.add_run(rec['value'])
      if rec['value'] in selections:
        runner.font.color.rgb = RGBColor(0x42, 0x24, 0xE9)

  def to_xls(self, workbook, worksheet, cursor):
    selections = self._report.http.get(self.htmlCode).split(',')
    cellTitle = self.title if self.title != '' else 'Checkbox:'
    cell_format = workbook.add_format({'bold': True})
    worksheet.write(cursor['row'], 0, cellTitle, cell_format)
    cursor['row'] += 1
    for rec in self.vals:
      cell_format = workbook.add_format({})
      if rec['value'] in selections:
        cell_format = workbook.add_format({'bold': True, 'font_color': self.getColor('colors', 5)})
      worksheet.write(cursor['row'], 0, rec['value'], cell_format)
      cursor['row'] += 1
    cursor['row'] += 1

  @staticmethod
  def matchMarkDown(val):
    return re.match("\+\+\+(.*)", val) or re.match("\-\-\-(.*)", val)

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report):
    param = True if val.startswith("+") else False
    if report is not None:
      getattr(report, cls.callFnc)(param, regExpResult.group(1))
    return ["report.%s(%s, %s)" % (cls.callFnc, param, regExpResult.group(1))]

  @classmethod
  def jsMarkDown(self, vals):
    if vals:
      return "+++" % self.label

    return "---%s" % self.label


class CheckButton(Html.Html):
  name, category, callFnc = 'Check Button', 'Button', 'check'

  # CSS Class
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, flag, tooltip, width, height, icon, label, htmlCode, options, profile):
    super(CheckButton, self).__init__(report, 'Y' if flag else 'N', htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                          heightUnit=height[1], profile=profile)
    self.isDisable = options.get("disable", False)
    self.add_label(label, {"width": "auto"}, position="after")
    self.add_icon(icon, {"float": 'none'}, position="after")
    self.css({'cursor': 'pointer', 'display': 'inline-block', 'margin-right': '10px'})
    self.clickEvent = {'Y': [], 'N': []}
    if tooltip is not None:
      self.tooltip(tooltip)

  # @property
  # def jsQueryData(self):
  #   if self.htmlCode is not None:
  #     return "{event_label: '%(label)s', event_val: $(this).data('isChecked'), event_code: '%(htmlCode)s', %(htmlCode)s: $(this).data('isChecked')}" % {'label': self.label, 'htmlCode': self.htmlCode}
  #
  #   return "{event_label: '%(label)s', event_val: $(this).data('isChecked'), event_code: '%(htmlCode)s'}" % {'label': self.label, 'htmlCode': self.htmlCode}
  #
  # @property
  # def val(self): return "%s.data('isChecked')" % self.jqId
  #
  # @property
  # def jqId(self):
  #   return "$('#%s div[name=\"check_box\"]')" % self.htmlId

  @property
  def _js__builder__(self):
    return ''' htmlObj.empty();
      if (data === true || data == 'Y'){
        htmlObj.append('<i class="fas fa-check" style="color:%(green)s;margin-bottom:2px;margin-left:2px"></i>');
        htmlObj.parent().data('isChecked', true)} 
      else {
        htmlObj.append('<i class="fas fa-times" style="font-size:14px;margin-top:2px;margin-left:5px;color:%(red)s"></i>');
        htmlObj.parent().data('isChecked', false)
      }''' % {'green': self.getColor('success', 1), 'red': self.getColor('danger', 1)}

  def click(self, jsFncs, allevents=True, isChecked=None):
    if allevents:
      jsFncs = [jsFncs] if not isinstance(jsFncs, list) else jsFncs
      self.clickEvent = {"Y": jsFncs, "N": jsFncs}
    else:
      if isinstance(jsFncs, list):
        for jsFnc in jsFncs:
          if isChecked:
            self.clickEvent['Y'].append(jsFnc)
          else:
            self.clickEvent['N'].append(jsFnc)
      else:
        if isChecked:
          self.clickEvent['Y'].append(jsFncs)
        else:
          self.clickEvent['N'].append(jsFncs)
    return self

  def __str__(self):
    # if not self.isDisable:
    #   self._report.jsOnLoadFnc.add('''
    #     %(jqId)s.parent().on('click', function(event){
    #       if (!$(this).data('isChecked')){
    #         $(this).data('isChecked', true);
    #         var data = %(jsQueryData)s; %(isChecked)s; data.event_time = Today(); data.event_time_offset = new Date().getTimezoneOffset();
    #         $(this).find('div[name="check_box"]').html('<i class="fas fa-check" style="margin-bottom:2px;margin-left:2px;color:%(green)s"></i>')}
    #       else {
    #         $(this).data('isChecked', false);
    #         var data = %(jsQueryData)s; %(isNotChecked)s; data.event_time = Today(); data.event_time_offset = new Date().getTimezoneOffset();
    #         $(this).find('div[name="check_box"]').html('<i class="fas fa-times" style="font-size:14px;margin-top:2px;margin-left:5px;color:%(red)s"></i>')}
    #       if ('%(htmlCode)s' != 'None') {%(breadCrumVar)s['params']['%(htmlCode)s'] = $(this).data('isChecked'); breadCrumbPushState()};
    #     })''' % {'jqId': self.dom.jquery.varId, 'htmlCode': self.htmlCode, 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'jsQueryData': "",
    #              'isChecked': ";".join(self.clickEvent['Y']), 'isNotChecked': ";".join(self.clickEvent['N']),
    #              'lightGrey': self.getColor('greys', 2), 'green': self.getColor('success', 1), 'red': self.getColor('danger', 1)})
    return '''
      <div %s>
        <div name="check_box" style="display:inline-block;vertical-align:bottom;margin-right:5px;float:left;width:16px;height:16px"></div>
      </div>''' % (self.get_attrs(pyClassNames=self.defined))


class IconEdit(Html.Html):
  name, category, callFnc = 'Icon', 'Icons', 'iconEdit'
  builder_name = False
  cssCls = ["fa-layers", "fa-fw"]

  def __init__(self, report, position, icon, text, size, tooltip, width, height, htmlCode, profile):
    if position is None:
      position = 'left'
    super(IconEdit, self).__init__(report, '', code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                   heightUnit=height[1], profile=profile)
    if tooltip is not None:
      self.tooltip(tooltip)
    # Add the internal components icons and helper
    self.add_span(text, css=False)
    if text is not None:
      self.span.css({"float": 'right'})
    self.add_icon(icon, {"color": self.getColor('success', 1), "margin": "2px", 'font-size': '%s%s' % (size[0], size[1])})
    self.css({"margin": "5px 0", "float": position, 'cursor': 'pointer'})

  def icon_on(self, event, jsFncs, profile=False):
    """

    Example
    edit = rptObj.ui.icons.edit()
    edit.on('click', rptObj.js.console.log('test'))

    :param event:
    :param jsFncs:
    :param profile:

    :return:
    """
    return self.icon.on(event, jsFncs, profile)

  def icon_css(self, key, value=None, reset=False):
    """

    :param key:
    :param value:
    :param reset:

    :return:
    """
    return self.icon.css(key, value, reset)

  def icon_colors(self, color_hover, color_out=None):
    """
    Change the color of the button background when the mouse is hover

    Example
    rptObj.ui.icons.capture().color("red", "yellow")

    :param color_hover: The color of the icon when mouse hover
    :param color_out: Optional. The color of the icon when mouse out

    """
    if color_out is None:
      color_out = self.getColor('success', 1)
    else:
      self.icon.css({"color": color_out})
    self.icon.set_attrs(name="onmouseover", value="this.style.color='%s'" % color_hover)
    self.icon.set_attrs(name="onmouseout", value="this.style.color='%s'" % color_out)
    return self

  def __str__(self): return "<span %s></span>" % (self.get_attrs(pyClassNames=self.defined))


# class IconThumbtack(IconEdit):
#   name, category, callFnc = 'Icon Thumbtack', 'Button', 'thumbtack'
#   mocks, icon, title = "Comment", 'fas fa-thumbtack', 'Add comment'
#
#   def __init__(self, report, parentJqId, position, icon, tooltip, width, widthUnit, height, heightUnit, htmlCode, profile):
#     if position is None:
#       position = 'right'
#     super(IconEdit, self).__init__(report, '', icon, tooltip, width, widthUnit, height, heightUnit, htmlCode, profile)
#     self.css({"margin-top": "5px", "margin-bottom": "5px", "float": position, "margin-left": "4px", "margin-right": "4px",
#                "color": "%s" % self.getColor('border', 0), 'font-size': '18px', 'cursor': 'pointer'})
#     self.attr.update({'class': set([self.icon]), 'data-original-title': self.title, 'name': "tooltip", 'data-toggle': 'tooltip', 'data-placement': 'top'})
#     # Add the different mouse event in the Html definition
#     self.addAttr("onmouseover", "this.style.color='%s'" % self.getColor('border', 1))
#     self.addAttr("onmouseout", "this.style.color='%s'" % self.getColor('border', 0))
#     self.parentJqId = parentJqId
#     self.addGlobalVar('thumbtack_counter', 0)
#
#   def __str__(self):
#     self._report.jsOnLoadFnc.add('''
#       %(jqId)s.on('click', function(event) {
#           var posX = $(this).offset().left; var posY = $(this).offset().top;
#           var comment = $('<div name="thumbtack" id="'+ thumbtack_counter +'"></div>');
#           comment.append('<div autocorrect="off" spellcheck="false" placeholder="comment" contenteditable=true style="float:left;margin-left:5px;margin-right:10px;">Comment</div>') ;
#           comment.append('<span style="color:%(color)s;margin-left:4px" onmouseover="this.style.color=\\\'grey\\\'" onmouseout="this.style.color=\\\'%(color)s\\\'"  class="far fa-edit" onclick="$(this).prev().focus()"></span>');
#           comment.append('<span id="lock_' + thumbtack_counter + '" onclick="$(this).parent().draggable(\\\'disable\\\'); $(this).remove() ;" style="color:%(color)s;margin-left:4px" onmouseover="this.style.color=\\\'grey\\\'" onmouseout="this.style.color=\\\'%(color)s\\\'" class="fas fa-lock"></span>');
#           comment.append('<span style="color:%(color)s;margin-left:4px" onmouseover="this.style.color=\\\'red\\\'" onmouseout="this.style.color=\\\'%(color)s\\\'"  class="far fa-trash-alt" onclick="$(this).parent().remove()"></span>');
#           %(parent)s.append(comment) ;
#           comment.css({'position': 'absolute', 'top':  event.pageY - posY+10, 'right': event.pageX - posX + 10}) ;
#           comment.draggable()})''' % {'jqId': self.jqId, 'parent': self.parentJqId, 'color': self.getColor('colors', 9)})
#     # self._report.jsOnLoadFnc.add(''' %(jqId)s.on('click', function(event) { $('#%(htmlId)s_content').focus() ; }) ''' % {"jqId": self.jqId, 'htmlId': self.htmlId})
#     return "<div %s></div>" % (self.strAttr(pyClassNames=self.pyStyle))
#
#
# class IconLock(IconEdit):
#   name, category, callFnc = 'Icon Lock', 'Button', 'lock'
#   mocks, icon, iconLock, title = "Lock", 'fas fa-unlock', 'fas fa-lock', 'Lock Comment'
#
#   def click(self, jsListFncLock, jsListFncUnLock):
#     self._report.jsOnLoadFnc.add('''
#       %(jqId)s.on('click', function(event) {
#         if ($(this).hasClass('fa-unlock') == true) {%(jsFncLock)s; $(this).addClass('fa-lock'); $(this).removeClass('fa-unlock'); }
#         else { %(jsFncUnLock)s; $(this).removeClass('fa-lock'); $(this).addClass('fa-unlock'); } ;
#       })''' % {"jqId": self.jqId, "jsFncLock": ";".join(jsListFncLock), "jsFncUnLock": ";".join(jsListFncUnLock)})
#
#
# class IconSum(IconEdit):
#   name, category, callFnc = 'Icon Sum', 'Button', 'calculator'
#   mocks, icon, title = "Sum", 'fas fa-calculator', 'Simple Calculator'
#
#   def __init__(self, report, parentJqId, icon, tooltip, width, widthUnit, height, heightUnit, htmlCode, profile):
#     self.parentJqId = parentJqId
#     super(IconSum, self).__init__(report, '', icon, tooltip, width, widthUnit, height, heightUnit, htmlCode, profile)
#
#   def __str__(self):
#     self._report.jsOnLoadFnc.add('''
#       %(jqId)s.on('click', function(event) {
#          if($("#icon_sum").length == 0) {
#           $('table[name="Table"] td').bind( "click", function( event ) {
#               var sum = parseFloat($("#icon_sum").find('#floating_sum').text().replace(',', '') ) + parseFloat( $(this).text().replace(',', '') );
#               var count = parseFloat($("#icon_sum").find('#floating_count').text().replace(',', '') ) + 1 ;
#               var average = sum / count ;
#               var absSum = parseFloat($("#icon_sum").find('#floating_abs_sum').text().replace(',', '') ) + Math.abs( parseFloat( $(this).text().replace(',', '')) ) ;
#
#               $("#icon_sum").find('#floating_sum').text(sum.formatMoney(2, ',', '.'));
#               $("#icon_sum").find('#floating_count').text(count.formatMoney(0, ',', '.'));
#               $("#icon_sum").find('#floating_average').text(average.formatMoney(2, ',', '.'));
#               $("#icon_sum").find('#floating_abs_sum').text(absSum.formatMoney(2, ',', '.'));
#
#            } ) ;
#           var comment = $('<div id="icon_sum" class="ui-widget-content" style="z-index:100;width:150px;border-radius:5px 5px 0 0;padding:5px"></div>');
#           comment.append("<div style='float:left;font-weight:bold'>Sum:</div><div style='width:100%%;text-align:center;font-size:14px' id='floating_sum'>0</div>") ;
#           comment.append("<div style='float:left;font-weight:bold'>Count:</div><div style='width:100%%;text-align:center;font-size:14px' id='floating_count'>0</div>") ;
#           comment.append("<div style='float:left;font-weight:bold'>Average:</div><div style='width:100%%;text-align:center;font-size:14px' id='floating_average'>0</div>") ;
#           comment.append("<div style='float:left;font-weight:bold'>Abs Sum:</div><div style='width:100%%;text-align:center;font-size:14px' id='floating_abs_sum'>0</div>") ;
#           $('body').append(comment) ;
#           comment.css( {'position': 'fixed', 'left': 200, 'top': 90} ) ; comment.draggable() ;
#         } else {
#           $("#icon_sum").remove() ; $('table[name="Table"] td').unbind( "click" ) ;}
#       })''' % {'jqId': self.jqId, 'color': self.getColor('border', 0)})
#     return "<div %s></div>" % (self.strAttr(pyClassNames=self.pyStyle))

"""
  # def jsDisable(self, bool=None, jsDataKey=None, isPyData=True, jsParse=False, jsFnc=None):
  #   if bool is None:
  #     return "%s.disabled;" % self.jqId
  #
  #   bool = self._jsData(bool, jsDataKey, jsParse, isPyData, jsFnc)
  #   return '''
  #     if(!%(bool)s) {%(jqId)s.css({"cursor": "pointer"})}
  #     else {%(jqId)s.css({"cursor": "not-allowed"})};
  #     %(jqId)s.attr("disabled", %(bool)s);
  #     ''' % {'jqId': self.jqId, 'bool': bool}

  # def isDisable(self, bool=True):
  #   self.css({"cursor": "not-allowed"})
  #   self.disable = True
  #   return self
  #
  # def addAttr(self, key, val=None, isPyData=True):
  #   if val is None and issubclass(key, Html.Html):
  #     self.__battr[key.htmlCode] = key.val
  #     self.isJs = True
  #   else:
  #     if isPyData:
  #       val = json.dumps(val)
  #     else:
  #       self.isJs = True
  #     self.__battr[key] = val
  #   return self

# def addStyles(self, cssAttrIcon=None, cssAttr=None):
  #   if cssAttrIcon is not None:
  #     self._jsStyles.setdefault('styleIcon', {}).update(cssAttrIcon)
  #   if cssAttr is not None:
  #     self._jsStyles.setdefault('styles', {}).update(cssAttr)
  #   return self
"""