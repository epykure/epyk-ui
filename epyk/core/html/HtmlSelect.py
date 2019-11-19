"""
Module for the HTML Selects components
"""

import json

from epyk.core.html import Html
from epyk.core.js.objects import JsNodeDom

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsList

#
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsSelect


class SelectDropDown(Html.Html):
  alias, cssCls = 'dropdown', ['btn', 'dropdown-toggle']
  __reqCss, __reqJs = ['bootstrap'], ['bootstrap', 'jquery']
  _grpCls = CssGrpClsList.CssClassListDropDown
  name, category, callFnc = 'DropDown Select', 'Lists', 'dropdown'

  def __init__(self, report, title, recordSet, size, width, height, htmlCode, dataSrc, globalFilter, profile):
    super(SelectDropDown, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                         heightUnit=height[1], htmlCode=htmlCode, globalFilter=globalFilter, dataSrc=dataSrc, profile=profile)
    if dataSrc is not None and dataSrc.get('on_init', False):
      self.vals = self.onInit(htmlCode, dataSrc)
    if htmlCode is not None and htmlCode in self._report.http:
      self.initVal(self._report.http[htmlCode])
    self.title, self.size = title, "%s%s" % (size[0], size[1])
    # To replace non alphanumeric characters https://stackoverflow.com/questions/20864893/javascript-replace-all-non-alpha-numeric-characters-new-lines-and-multiple-whi
    #self.jsFrg = ["%s = CleanText($(this).text()) ;" % self.htmlId]
    self.allowTableFilter, self._jsStyles = [], {"clearDropDown": True, 'dropdown_submenu': {},
      'a_dropdown_item': {'text-decoration': 'none', "color": 'inherit', 'font-size': self._report.pyStyleDfl['fontSize']}, # {"width": "100%", 'font-size': '12px', 'text-decoration': 'none', 'padding-left': "10px"},
      "li_dropdown_item": {"text-align": "left", 'font-size': self._report.pyStyleDfl['fontSize']}}
    self.css({"margin-top": "5px", "display": "inline-block"})
    # for evts in ['click', 'change']:
    #   # Add the source to the different events
    #   self.jsFrg(evts, '''
    #     event.stopPropagation(); $("#%(htmlId)s_button").html(data.event_val);
    #     if ('%(htmlCode)s' != 'None') {%(breadCrumVar)s['params']['%(htmlCode)s'] = %(jsEventVal)s; breadCrumbPushState()}
    #     ''' % {'htmlId': self.htmlId, 'htmlCode': self.htmlCode, 'jsEventVal': self.jsEventVal, 'breadCrumVar': self._report.jsGlobal.breadCrumVar})

  @property
  def jsQueryData(self):
    if self.htmlCode:
      return "{event_val: %(val)s, event_code: '%(htmlId)s', %(htmlCode)s: %(val)s}" % {'val': self.jsEventVal, 'htmlId': self.htmlId, 'htmlCode': self.htmlCode}

    return "{event_val: %s, event_code: '%s'}" % (self.jsEventVal, self.htmlId)

  @property
  def jsEventVal(self): return "$(this).contents()[0].text"

  def initVal(self, val, isPyData=True):
    """
    This function will set the initial value selected by the SelectDropDown component.

    Example
    myObj.initVal('Test')
    """
    if isPyData:
      val = json.dumps(val)
    self._report.jsOnLoadFnc.add('$("#%(htmlId)s_button").html(%(jsVal)s)' % {"htmlId": self.htmlId, "jsVal": val})

  def setDefault(self, value, isPyData=True):
    """
    Set the default value selected to the dropdown box

    Example
    myObj.setDefault( 'btn-default' )
    """
    if isPyData:
      value = json.dumps(value)
    self._report.jsGlobal.add("%s = %s;" % (self.htmlId, value))

  @property
  def val(self):
    return '$("#%s_button").html()' % self.htmlId

  @property
  def eventId(self): return "$('#%s li')" % self.htmlId

  @property
  def _js__builder__(self):
    return ''' 
        if (jsStyles.clearDropDown) {htmlObj.empty()};
        data.forEach(function(rec){
          if (rec._children != undefined) {
            var li = $('<li class="dropdown-submenu"></li>').css(jsStyles.dropdown_submenu);
            var a = $('<a class="dropdown-item" tabindex="-1" href="#" style="display:inline-block"><span style="display:inline-block;float:left">'+ rec.value +'</span></a>').css(jsStyles.a_dropdown_item);
            li.append(a); var ul = $('<ul class="dropdown-menu"></ul>'); li.append(ul); jsStyles.clearDropDown = false;
            htmlObj.append(li); %(pyCls)s(ul, rec._children, jsStyles)
          } else {
            if (rec.disable == true) {htmlObj.append('<li class="disabled"><a href="#">'+ rec.value +'</a></li>')}
            else {
              if (rec.url == undefined) {var a = $('<a href="#">'+ rec.value +'</a>')}
              else {var a = $('<a href="'+ rec.url +'">'+ rec.value +'</a>')}
              a.css(jsStyles.a_dropdown_item);
              var li = $('<li class="dropdown-item"></li>').css(jsStyles.dropdown_submenu);
              li.append(a); htmlObj.append(li)}
          }
        })''' % {"pyCls": self.__class__.__name__}

  def __str__(self):
    # [s for s in self.defined if not s.startswith("CssDropDown")]
    return ''' 
      <div class="dropdown" %(cssAttr)s>
        <button id="%(htmlId)s_button" style="font-size:%(size)s;width:100%%;height:100%%;background-color:%(darkBlue)s;color:%(color)s" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">%(title)s<span class="caret"></span></button>
        <ul class="dropdown-menu" id="%(htmlId)s" aria-labelledby="dropdownMenu"></ul>
      </div> ''' % {'cssAttr': self.get_attrs(withId=False, pyClassNames=self.defined), 'title': self.title, 'htmlId': self.htmlId,
                    'darkBlue': self.getColor('colors', 7), 'color': self.getColor('greys', 0), 'size': self.size}

  def to_word(self, document):
    p = document.add_paragraph()
    p.add_run("Selected: ")
    runner = p.add_run(self._report.http.get(self.htmlCode, self.vals))
    runner.bold = True

  def to_xls(self, workbook, worksheet, cursor):
    if self.htmlId in self._report.http:
      cellTitle = self.title if self.title != "" else 'Input'
      cell_format = workbook.add_format({'bold': True})
      worksheet.write(cursor['row'], 0, cellTitle, cell_format)
      cursor['row'] += 1
      worksheet.write(cursor['row'], 0, self._report.http[self.htmlId])
      cursor['row'] += 2


class Option(Html.Html):
  name, category, callFnc = 'Select Option', 'Lists', None
  builder_name = False

  def __init__(self, report, value, text, icon, selected):
    super(Option, self).__init__(report, text)
    self.set_attrs(name="value", value=value)
    if selected:
      self.set_attrs(name="selected", value=selected)
    if icon is not None:
      self.set_attrs(name="data-icon", value=icon)

  def __str__(self):
    return "<option %s>%s</option>" % (self.get_attrs(pyClassNames=self.defined), self.val)


class Optgroup(Html.Html):
  name, category, callFnc = 'Select Option', 'Lists', None
  builder_name = False

  def __init__(self, report, data, label):
    super(Optgroup, self).__init__(report, data)
    self.set_attrs(name="label", value=label)

  def __str__(self):
    val = "".join([v.html() for v in self.val])
    return "<optgroup %s>%s</optgroup>" % (self.get_attrs(pyClassNames=self.defined), val)


class Select(Html.Html):
  __reqCss, __reqJs = ['select'], ['select']
  name, category, callFnc = 'Select', 'Lists', 'select'

  def __init__(self, report, records, htmlCode, width, height, filter, profile, multiple, options):
    super(Select, self).__init__(report, records, htmlCode=htmlCode, width=width[0], widthUnit=width[1],
                                 height=height[0],  heightUnit=height[1], globalFilter=filter, profile=profile)
    self.selected = None

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsSelect.JSelect(self, report=self._report)
    return self._dom


  @property
  def _js__builder__(self):
    return ''' %s.selectpicker(options).selectpicker('refresh') ''' % JsQuery.decorate_var("htmlObj")

  def change(self, jsFncs, profile=False):
    return self.on("change", jsFncs, profile)

  def __str__(self):
    options, opt_groups = [], []
    for val in self.val:
      opt = Option(self._report, val['value'], val['name'], None, self.selected is not None and self.selected == val['value'])
      opt.inReport = False
      options.append(opt)
    #
    opt_rp = Optgroup(self._report, options, "test Group")
    opt_rp.inReport = False
    opt_groups.append(opt_rp.html())

    return "<select %s>%s</select>" % (self.get_attrs(pyClassNames=self.defined), "".join(opt_groups))


class SelectOld(Html.Html):
  __reqCss, __reqJs = ['select'], ['select', 'jquery']
  _grpCls = CssGrpClsList.CssClassListSelect
  name, category, callFnc = 'Select', 'Lists', 'select'

  def __init__(self, report, records, htmlCode, label, width, height, filter, profile, multiple, options):
    super(SelectOld, self).__init__(report, records, htmlCode=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], globalFilter=filter, profile=profile)
    self.add_label(label)
    self._jsStyles = {"liveSearch": options.get("liveSearch", False), "style": "show-menu-arrow class_select", "width": '100px'}
    self._jsStyles.update(options)
    self.css({'display': 'block'})
    self.multiple = multiple
    # This object does not work well without Jquery
    self.dom.val = self.dom.jquery.val

  @property
  def id_container(self):
    return self.htmlId

  @property
  def id_jquery(self):
    return JsNodeDom.JsDoms.get("$('#%s select')" % self.htmlId)

  @property
  def id_html(self):
    """

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/Element/getElementsByTagName

    :return:
    """
    return JsNodeDom.JsDoms.get("document.getElementById('%s').getElementsByTagName('select')" % self.htmlId)

  @property
  def jqId(self):
    return "$('#%s select')" % self.htmlId

  @property
  def jsQueryData(self):
    if self.multiple:
      if self.htmlCode is not None:
        return "{%s: %s.val(), event_val: %s.val(), event_code: '%s', event_icon: %s.find(':selected').data('icon')}" % (
            self.htmlCode, self.jqId, self.jqId, self.htmlId, self.jqId)

      return "{event_val: %s.val(), event_code: '%s', event_icon: %s.find(':selected').data('icon')}" % (
          self.jqId, self.htmlId, self.jqId)

    if self.htmlCode is not None:
      return "{%(htmlCode)s: %(jqId)s.val(), event_val: %(jqId)s.val(), event_code: '%(htmlId)s', event_icon: %(jqId)s.find(':selected').data('icon')}" % {
        'htmlCode': self.htmlCode, 'jqId': self.jqId, 'htmlId': self.htmlId}

    return "{event_val: %s.val(), event_code: '%s', event_icon: %s.find(':selected').data('icon')}" % (
    self.jqId, self.htmlId, self.jqId)

  def options(self, attrs):
    """
    Add options to the select component

    All the options available to the underlying library can be added.

    Example


    Documentation
    https://developer.snapappointments.com/bootstrap-select/options/

    :param attrs:
    :return:
    """
    self._jsStyles.update(attrs)

  def callPy(self, script_name, jsData=None, success="", cacheObj=None, isPyData=True, isDynUrl=False, httpCodes=None,
             datatype='json', context=None, profile=False, loadings=None, report_name=None, before=None, jsFnc=''):
    if not script_name.endswith(".py"):
      script_name = "%s.py" % script_name
    if success != "":
      jsFnc = success
    if before is not None:
      if not isinstance(before, list):
        before = [before]
    else:
      before = []
    return self.change(before + [self._report.jsPost(script_name, jsData, jsFnc, cacheObj, isPyData, isDynUrl, httpCodes,
                                          datatype, context, profile, loadings, report_name)])

  def onDocumentLoadFnc(self):
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, ''' htmlObj.empty();
      var categories = {}; var cats = []; var selectedVals = [];
      data.forEach(function(rec){
        if (rec.category == undefined){rec.category = 'None'}
        if (rec.category in categories){categories[rec.category].push(rec)}
        else {categories[rec.category] = [rec]; cats.push(rec.category)}});
      cats.forEach(function(cat){
        if (cat != 'None') {
          var optgroup = $('<optgroup label="'+ cat + '">'+ cat +'</optgroup>');
          categories[cat].forEach(function(rec){
            if (rec.selected == true){var selected = 'selected=true'} else{var selected = ''};
            if (rec.name == undefined){rec.name = rec.value};
            if (rec.icon != undefined){options = options +'data-icon="'+ rec.icon +'"'};
            optgroup.append('<option value="'+ rec.value + '" '+ selected +'>'+ rec.name +'</option>')});
          htmlObj.append(optgroup)}
        else {
          categories[cat].forEach(function(rec){
            var options = ' ';
            if (rec.selected == true) {var selected = 'selected'; selectedVals.push(rec.value)} else{var selected = ''};
            if (rec.name == undefined) {rec.name = rec.value};
            if (rec.icon != undefined) {options = options +'data-icon="'+ rec.icon +'"'};
            if (rec['data-subtext'] != undefined){options = options +' data-subtext="'+ rec['data-subtext'] +'"'};
            htmlObj.append('<option value="'+ rec.value +'" '+ selected + options +'>'+ rec.name +'</option>')});
        }}); htmlObj.selectpicker(jsStyles).selectpicker('refresh')''')

  def __str__(self):
    if self.label != "":
      self.label.html()
    if self.multiple:
      return '''<div %(strAttr)s>%(label)s<select multiple></select></div>''' % {"strAttr": self.get_attrs(pyClassNames=self.defined), "label": self.label}

    return '''<div %(strAttr)s>%(label)s<select></select></div>''' % {"strAttr": self.get_attrs(pyClassNames=self.defined), "label": self.label}

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_xls(self, workbook, worksheet, cursor):
    if self.htmlId in self._report.http:
      cell_title = self._jsStyles["title"] if self._jsStyles.get("title") is not None else 'Input'
      cell_format = workbook.add_format({'bold': True})
      worksheet.write(cursor['row'], 0, cell_title, cell_format)
      cursor['row'] += 1
      worksheet.write(cursor['row'], 0, self._report.http[self.htmlId])
      cursor['row'] += 2

  def to_word(self, document):
    p = document.add_paragraph()
    p.add_run("Selected: ")
    selected = ""
    for rec in self.vals:
      if rec.get('selected', False):
        selected = rec['value']
    runner = p.add_run(selected)
    runner.bold = True
