"""
This below module is defining HTML components expecting Javascript events. Each of them are using specific function in
order to update their content or to run some functions on the server side.

Components using Ajax functions will be fully working only if a server is defined.
"""

import re
import json

from epyk.core.html import Html
from epyk.core.html.entities import EntHtml4

from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.Imports import requires
from epyk.core.js.packages import JsQuery

# The list of CSS classes
from epyk.core.css.categories import CssGrpCls
from epyk.core.css.categories import CssGrpClsText
from epyk.core.css.categories import CssGrpClsImage
from epyk.core.css.categories import CssGrpClsList
from epyk.core.css.categories import CssGrpClsTable


class ProgressBar(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jquery', 'jqueryui']
  name, category, callFnc = 'Progress Bar', 'Sliders', 'progressbar'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, number, total, width, height, attrs, helper, profile):
    value = number / total * 100
    super(ProgressBar, self).__init__(report, value, width=width[0], widthUnit=width[1], height=height[0],
                                      heightUnit=height[1], profile=profile)
    self.add_helper(helper)
    self._jsStyles = {"background": self._report.theme.success[1]}
    self.attr["title"] = "%.2f%% (%s / %s)" % (value, number, total)

  @property
  def _js__builder__(self):
    return "jQuery(htmlObj).progressbar({value: parseFloat(data)}).find('div').css(options)"

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object
    :rtype: JsHtml.JsHtmlProgressBar
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlProgressBar(self, report=self._report)
    return self._dom

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.defined), self.helper)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @staticmethod
  def matchMarkDown(val):
    return re.match("%%%%([0-9]*)%", val)

  @classmethod
  def convertMarkDown(cls, val, regExpResult, report):
    if report is not None:
      getattr(report, 'progressbar')(regExpResult.group(1))
    return ["report.progressbar(%s)" % regExpResult.group(1)]

  @classmethod
  def to_markdown(self, vals):
    return "%%%%" + str(vals) + "%"


class Slider(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Slider', 'Sliders', 'slider'

  def __init__(self, report, value, typeObj, range, animate, step, min, max, width, height,
               globalFilter, recordSet, color, attrs, helper, profile):
    data = {'animate': animate, 'min': min, 'max': max, 'step': step}
    super(Slider, self).__init__(report, data, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1],
                                 globalFilter=globalFilter, profile=profile)

  @property
  def dom(self):
    """
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSlider(self, report=self._report)
    return self._dom

  @property
  def _js__builder__(self):
    return '''
      if (options.type == 'date'){
        data.step = data.step * 86400000; data.min = DateToTimeStamp(data.min); data.max = DateToTimeStamp(data.max);
        if (data.values != undefined) {data.values = [DateToTimeStamp(data.values[0]), DateToTimeStamp(data.values[1])]}
        else if(data.value != 0) {data.value = DateToTimeStamp(data.value)}};
      if(!isNaN(data)){data = {value: data}};
      %(jqId)s.slider(data);
      $('#'+ %(jqId)s.attr('id') +' .ui-slider-range').css("background-color", options.backgroundColor);
      $('#'+ %(jqId)s.attr('id') +' .ui-slider-handle').css({"outline": 0, "white-space": "nowrap"});
      $('#'+ %(jqId)s.attr('id') +' .ui-slider-handle').css("color", options.backgroundColor);
      $('#'+ %(jqId)s.attr('id') +' .ui-state-default, .ui-widget-content .ui-state-default' ).css("background-color", options.backgroundDotColor)
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''
      <div %(strAttr)s>
        <div style="width:100%%;height:20px">
          <span style="float:left;display:inline-block">%(min)s</span>
          <span style="float:right;display:inline-block">%(max)s</span>
        </div>
        <div id="%(htmlId)s"></div>
      </div>%(helper)s''' % {"strAttr": self.get_attrs(withId=False), "min": self.val['min'], "htmlId": self.htmlId,
                             "max": self.val['max'], "helper": self.helper}


class SliderOld(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Slider', 'Sliders', 'slider'

  def __init__(self, report, value, typeObj, range, animate, step, min, max, width, height,
               globalFilter, recordSet, color, attrs, helper, profile):
    if recordSet is not None:
      series = recordSet
      if range is None and min == True:
        operation, range = 'below', 'min'
      elif range is None and max == True:
        operation, range = 'above', 'max'
      elif range is not None:
        operation = 'between'
      else:
        operation = "="
      min, max = series[0], series[-1]
      value, typeObj = value, typeObj
    if typeObj == 'integer':
      try:
        int(value)
      except:
        report.log("Slider is expected type as a number by default - value = %s, change type variable to range " % value)
        raise Exception("Slider is expected type as a number by default - value = %s, change type variable to range " % value)

    self.type = typeObj
    val = {'animate': animate, 'min': min, 'max': max, 'step': step}
    if range is not None:
      val['range'] = range
    if isinstance(value, list) and len(value) == 2:
      val['range'] = True
      val['values'] = value
    else:
      val['value'] = value
    super(SliderOld, self).__init__(report, val, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                 globalFilter=globalFilter, profile=profile)
    self._jsStyles = {'type': typeObj}
    #
    self.add_helper(helper)

    self.css({'text-align': 'center', 'padding-top': '-50px', 'padding': '10px', 'margin': '0 0 10px 0'})
    self.setColor(self._report.theme.colors[7] if color is None else color)
    if self.htmlCode is not None:
      self._report.htmlCodes[self.htmlCode] = self
      if 'values' in self.vals:
        if typeObj == 'date':
          self.jsFrg('slidechange', self.jsAddUrlParam(self.htmlCode, '[FormatDate(ui.values[0]), FormatDate(ui.values[1])]', isPyData=False))
        else:
          self.jsFrg('slidechange', self.jsAddUrlParam(self.htmlCode, "ui.values", isPyData=False))
      else:
        if typeObj == 'date':
          self.jsFrg('slidechange', self.jsAddUrlParam(self.htmlCode, "FormatDate(ui.value)", isPyData=False))
        else:
          self.jsFrg('slidechange', self.jsAddUrlParam(self.htmlCode, "ui.value", isPyData=False))

    # if typeObj == 'date':
    #   self.change('''var value = new Date(ui.value);
    #     if(ui.handleIndex == 0) { $(ui.handle).html("<div style='margin-top:12px'>" + FormatDate(value) + "</div>" )}
    #     else {$(ui.handle).html("<div style='margin-top:-17px'>" + FormatDate(value) + "</div>")}''')
    # else:
    #   self.js.objects.proto("formatMoney")
    #   self.change('''
    #     if(ui.handleIndex == 0) {$(ui.handle).html("<div style='margin-top:12px'>"+ ui.value.formatMoney(0, ",", ".") +"</div>")}
    #     else {$(ui.handle).html("<div style='margin-top:-17px'>"+ ui.value.formatMoney(0, ",", ".") +"</div>")}''')
    if typeObj == 'date':
      self.addGlobalFnc('DateToTimeStamp(date)', '''
        var splitDt = date.split("-") ; var dateTime = new Date(splitDt[0], parseInt(splitDt[1])-1, splitDt[2]);
        return dateTime.getTime(); ''', 'Javascript function to convert a string date YYYY-MM-DD to a Javascript timestamp')
      self.addGlobalFnc('FormatDate(timeStamp)', '''
        var d = new Date(timeStamp), month = '' + (d.getMonth() + 1), day = '' + d.getDate(), year = d.getFullYear();
        if (month.length < 2) month = '0' + month;
        if (day.length < 2) day = '0' + day;
        return [year, month, day].join('-'); ''', 'Javascript function to convert a Js timestamp to a string date YYYY-MM-DD')
    #self.change("var data = {event_val: ui.value, event_code:'%(htmlId)s'}; $('#%(htmlId)s_val').html(data.event_val);" % {'htmlId': self.htmlId } )

  @property
  def dom(self):
    """
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSlider(self, report=self._report)
    return self._dom

  @property
  def id_container(self):
    return self.htmlId

  def jsEvents(self):
    if hasattr(self, 'jsFncFrag'):
      for eventKey, fnc in self.jsFncFrag.items():
        #fnc.insert(0, self.jsAddUrlParam(self.htmlId, self.val, isPyData=False))
        self._report.jsOnLoadEvtsFnc.add(''' 
            %(jqId)s.on('%(eventKey)s', function(event, ui) {
              var useAsync = false; var data = %(data)s;
              %(jsInfo)s; %(jsFnc)s; %(urlUpdate)s;
              if(!useAsync) {
                var body_loading_count = parseInt($('#body_loading span').text()); $('#body_loading span').html(body_loading_count - 1);
                if ($('#body_loading span').html() == '0') {$('#body_loading').remove()}}
            })''' % {'jqId': self.eventId, 'eventKey': eventKey, 'data': self.jsQueryData, 'lightGreyColor': self._report.theme.greys[2],
                     'urlUpdate': self.js.window.history.updateState(self.htmlId, self.val).toStr(),
                     'jsFnc': ";".join([f for f in fnc if f is not None]), 'jsInfo': self._report.jsInfo('process(es) running', 'body_loading')})

  # data.slide: function( event, ui ) {  $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] ); }
  @property
  def _js__builder__(self):
    return '''
    if (options.type == 'date'){
      data.step = data.step * 86400000; data.min = DateToTimeStamp(data.min); data.max = DateToTimeStamp(data.max);
      if (data.values != undefined) {data.values = [DateToTimeStamp(data.values[0]), DateToTimeStamp(data.values[1])]}
      else if(data.value != 0) {data.value = DateToTimeStamp(data.value)}};
    if(!isNaN(data)){data = {value: data}};
    htmlObj.slider(data);
    $('#'+ htmlObj.attr('id') +' .ui-slider-range').css("background-color", options.backgroundColor);
    $('#'+ htmlObj.attr('id') +' .ui-slider-handle').css({"outline": 0, "white-space": "nowrap"});
    $('#'+ htmlObj.attr('id') +' .ui-slider-handle').css("color", options.backgroundColor);
    $('#'+ htmlObj.attr('id') +' .ui-state-default, .ui-widget-content .ui-state-default' ).css("background-color", options.backgroundDotColor)
    '''

  def addAttr(self, key, val):
    """
    :category: Javascript features
    :rubric: JS
    :example: >>> myObj.change( report.addAttr('value', 20) )
    :returns: Javascript string with the function to define some slider properties
    :dsc:
      This function will change or add some javascript attributes attached to the slider object
    :link Jquery documentation: https://jqueryui.com/slider/
    """
    self.vals[key] = val

  def setColor(self, color, colorDot=None):
    """
    :category: Color Change
    :rubric: CSS
    :type: Style
    :dsc:
      Set the color of the Slider object
    :return: The Python object
    """
    if colorDot is None:
      colorDot = color
    self._jsStyles['backgroundColor'] = color
    self._jsStyles['backgroundDotColor'] = colorDot
    return self

  def __str__(self):
    return '''
      <div %(strAttr)s>
        <div style="width:100%%;height:20px">
          <span style="float:left;display:inline-block">%(min)s</span>
          <span style="float:right;display:inline-block">%(max)s</span>
        </div>
        <div id="%(htmlId)s"></div>
      </div>%(helper)s''' % {"strAttr": self.get_attrs(withId=False), "min": self.val['min'], "htmlId": self.htmlId,
                     "max": self.val['max'], "helper": self.helper}

  def click(self, jsFnc):
    return self.change(jsFnc)

  def change(self, jsFnc):
    """
    :category: Javascript event
    :rubric: JS
    :example: myObj.change( report.jsAlert() )
    :returns: Javascript string with the function to trigger other functions with the slider value is changed
    :dsc:
      Python wrapper to a javascript function to trigger events on slider changes
    :link Jquery documentation: https://api.jqueryui.com/slider/
    """
    return self.jsFrg('slidechange', jsFnc)

  def jsUpdate(self, jsData, isPyData=True):
    """
    :category: Javascript function
    :rubric: JS
    :example: myObj.jsUpdate( 20 )
    :example: myObj.jsUpdate( "2018-07-21" )
    :example: myObj.jsUpdate( ["2018-07-21", "2018-07-22"] ) # if the type is a date
    :return: Javascript string with the function to change the value of the component
    :dsc:
      Python wrapper to a javascript function to change the value of a Jquery slider object
    :link Jquery documentation: https://jqueryui.com/slider/
    """
    if isPyData:
      if ('values' in self.vals or self.vals.get('range', False) == True) and not isinstance(jsData, list):
        self._report.log("Problem in Slider jsUpdate expect a list")
        raise Exception("Problem in Slider jsUpdate expect a list")

      jsData = json.dumps(jsData)
    if 'values' in self.vals or self.vals.get('range', False) == True:
      if self.type == 'date':
        return "%(jqId)s.slider('values', 0, DateToTimeStamp(%(jsData)s[0])); %(jqId)s.slider('values', 1, DateToTimeStamp(%(jsData)s[1]));" % {'jqId': self.jqId, 'jsData': jsData}
      else:
        return "%(jqId)s.slider('values', 0, %(jsData)s[0]); %(jqId)s.slider('values', 1, %(jsData)s[1]);" % {'jqId': self.jqId, 'jsData': jsData}

    if self.type == 'date':
      return "%s.slider('value', DateToTimeStamp(%s)); " % (self.jqId, jsData)
    else:
      return "%s.slider('value', %s); " % (self.jqId, jsData)

  # @property
  # def val(self):
  #   """
  #   :category: Javascript function
  #   :rubric: JS
  #   :example: myObj.val
  #   :returns: Javascript string with the function to get the current value of the component
  #   :dsc:
  #     Property to get the jquery value of the HTML object in a python HTML object.
  #     This method can be used in any jsFunction to get the value of a component in the browser.
  #     This method will only be used on the javascript side, so please do not consider it in your algorithm in Python
  #   """
  #   if 'values' in self.val or self.val.get('range', False) == True:
  #     if self.type == 'date':
  #       return '[FormatDate(%(jqId)s.slider("values")[0]), FormatDate( %(jqId)s.slider("values")[1] )]' % {'jqId': self.jqId}
  #
  #     return self.js.objects.get('%(jqId)s.slider("values")' % {'jqId': self.jqId})
  #
  #   if self.type == 'date':
  #     return 'FormatDate(%(jqId)s.slider("value"))' % {'jqId': self.jqId}
  #
  #   return self.js.objects.get('%(jqId)s.slider("value")' % {'jqId': self.jqId})

  @property
  def jsQueryData(self):
    """
    :category: Javascript function
    :rubric: JS
    :example: >>> myObj.jsQueryData
    :dsc:
      Python function to define the Javascript object to be passed in case of Ajax call internally or via external REST service with other languages
    :return: Javascript String of the data to be used in a jQuery call
    :link ajax call: http://api.jquery.com/jquery.ajax/
    """
    if 'values' in self.vals or self.vals.get('range', False) == True:
      if self.type == 'date':
        return "{event_val: [FormatDate(ui.values[0]), FormatDate(ui.values[1])], event_code: '%(htmlId)s', event_min: %(min)s, event_max: %(max)s, event_range: '%(range)s' }" % {"htmlId":  self.htmlId, 'min': self.vals['min'], 'max': self.vals['max'], 'range': self.vals.get('range') }
      else:
        return "{event_val: ui.values, event_code: '%(htmlId)s', event_min: %(min)s, event_max: %(max)s, event_range: '%(range)s'}" % {"htmlId":  self.htmlId, 'min': self.vals['min'], 'max': self.vals['max'], 'range': self.vals.get('range') }

    if self.type == 'date':
      return "{ event_val: FormatDate(ui.value), event_code: '%(htmlId)s', event_min: %(min)s, event_max: %(max)s, event_range: '%(range)s' }" % {"htmlId":  self.htmlId, 'min': self.vals['min'], 'max': self.vals['max'], 'range': self.vals.get('range') }

    return "{ event_val: ui.value, event_code: '%(htmlId)s', event_min: %(min)s, event_max: %(max)s, event_range: '%(range)s' }" % {"htmlId":  self.htmlId, 'min': self.vals['min'], 'max': self.vals['max'], 'range': self.vals.get('range') }


  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_word(self, document):
    label = self.title if self.title != "" else 'Input'
    p = document.add_paragraph("%s: %s [%s, %s]" % (label, self._report.http.get(self.htmlCode, ''), self.vals['min'], self.vals['max']))

  def to_xls(self, workbook, worksheet, cursor):
    """

    Documentation
    https://xlsxwriter.readthedocs.io/format.html
    """
    cellTitle = self.title if self.title != "" else 'Input'
    cell_format = workbook.add_format({'bold': True})
    worksheet.write(cursor['row'], 0, cellTitle, cell_format)
    cursor['row'] += 1
    worksheet.write(cursor['row'], 0, self._report.http.get(self.htmlCode, ''))
    worksheet.write(cursor['row'], 1, "[%s, %s]" % (self.vals['min'], self.vals['max']))
    cursor['row'] += 2


class SkillBar(Html.Html):
  name, category, callFnc = 'Skill Bars', 'Chart', 'skillbars'
  _grpCls = CssGrpClsTable.CssClassTable

  def __init__(self, report, data, y_column, x_axis, title, width, height, htmlCode, colUrl, colTooltip, filters, profile):
    super(SkillBar, self).__init__(report, "", width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                   htmlCode=htmlCode, globalFilter=filters, profile=profile)
    self.add_title(title)
    self.innerPyHTML = report.ui.layouts.table(data, y_column, x_axis)
    self.innerPyHTML.inReport = False
    for c in self.innerPyHTML.col(i=1):
      if c.val not in y_column:
        c.set_html_content(report.ui.div(EntHtml4.NO_BREAK_SPACE).css({"width": '%spx' % c.val, "background": 'red'}))
    self.innerPyHTML.style.clear()
    self.css({"margin": '5px 0'})
    #self._jsStyles = {'val': list(self.data._schema['values'])[0], 'label': list(self.data._schema['keys'])[0],
    #                  'color': self.getColor('colors', 7), 'fontColor': self.getColor('greys', 0), 'colUrl': colUrl, 'colTooltip': colTooltip}

  @property
  def _js__builder__(self):
    return '''
      htmlObj.empty();
      data.forEach(function(rec, i){
        if (options.colTooltip != undefined) {var tooltip = 'title="'+ rec[options.colTooltip] +'"'} else {var tooltip = ''};
        if (options.colUrl != undefined) {var content = '<a href="'+ rec[options.colUrl] +'" style="color:white">'+ valPerc.toFixed(2) +'%</a>'} 
        else {var content = rec[options.val].toFixed( 2 ) +"%"};
        htmlObj.append('<tr '+ tooltip +'><td style="width:100px;"><p style="margin:2px;text-align:center;word-wrap:break-word;cursor:pointer">'+ rec[options.label] +'</p></td><td style="width:100%"><div style="margin:2px;display:block;height:100%;padding-bottom:5px;padding:2px 0 2px 5px;width:'+ parseInt( rec[options.val] ) +'%;background-color:'+ jsStyles.color +';color:'+ options.fontColor +'">' + content + '</div></td></tr>');
        htmlObj.find('tr').tooltip()})
      '''

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.defined), self.content)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data): return True if data[0].strip() == "---SkillBar" else None

  @staticmethod
  def matchEndBlock(data): return data.endswith("---")

  @classmethod
  def convertMarkDownBlock(cls, data, report):
    """
    :category:
    :rubric:
    :example:
      ---SkillBar
      label|value|color
      Test 1|35|yellow
      Test 2|25|blue
      ---
    :dsc:

    """
    recordSet = []
    header = data[1].strip().split("|")
    for val in data[2:-1]:
      label, value, color = val.strip().split("|")
      recordSet.append({'value': value, 'label': label, 'color': color})
    if report is not None:
      getattr(report, 'skillbars')(recordSet)
    return ["report.skillbars(%s)" % json.dumps(recordSet)]

  @classmethod
  def jsMarkDown(self, vals):
    recordSet = ["---SkillBar", 'label|value|color']
    for rec in vals:
      recordSet.append("%(label)s|%(value)s|%(color)s" % rec)
    recordSet.append("---")
    return "&&".join(recordSet)

  # -----------------------------------------------------------------------------------------
  #                                    EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def to_img(self):
    """

    :return:
    """
    pkg_matplotlib = requires("matplotlib.pyplot", reason='Missing Package', install='matplotlib', source_script=__file__)
    pkg_numpy = requires("numpy", reason='Missing Package', install='numpy', source_script=__file__)

    pkg_matplotlib.rcdefaults()
    fig, ax = pkg_matplotlib.subplots()

    # Example data
    aggDf = self.vals.data.groupby([self.vals.xAxis])[self.vals.seriesNames[0]].sum().reset_index()
    labels = aggDf[self.vals.xAxis]
    values = aggDf[self.vals.seriesNames[0]]

    y_pos = pkg_numpy.arange(len(labels))
    performance = values
    error = pkg_numpy.random.rand(len(labels))
    ax.barh(y_pos, performance, xerr=error, align='center', color=self._report.theme.colors[7], ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(self.vals.xAxis)
    ax.set_title(self.title)
    return fig

  def to_word(self, document):
    """

    :param document:

    :return:
    """
    pkg_matplotlib = requires("matplotlib.pyplot", reason='Missing Package', install='matplotlib', source_script=__file__)
    import os

    fig = self.to_img()
    imgsPath = os.path.join(self._report.run.local_path, "imgs")
    if not os.path.exists(imgsPath):
      os.mkdir(imgsPath)

    # Add the picture to the document
    pkg_matplotlib.savefig(os.path.join(imgsPath, "%s.png" % id(fig)))
    document.add_picture(os.path.join(imgsPath, "%s.png" % id(fig)))
    os.remove(os.path.join(imgsPath, "%s.png" % id(fig)))


class ContextMenu(Html.Html):
  name, category, callFnc = 'Context Menu', None, 'contextmenu'
  source = None # The container
  _grpCls = CssGrpClsText.CssClassTextItem

  def __init__(self, report, recordSet, width, height, visible, profile):
    for rec in recordSet:
      if isinstance(rec['event'], list):
        rec['event'] = ";".join(rec['event'])
    super(ContextMenu, self).__init__(report, recordSet, width=width[0], widthUnit=width[1], height=height[0],
                                      heightUnit=height[1], profile=profile)
    self.css({'display': 'block' if visible else 'none', 'position': 'absolute', 'z-index': 200,
              'padding': 0, 'margin': 0, 'background-color': self._report.theme.greys[0],
              'border': '1px solid %s' % self._report.theme.colors[5], 'border-radius': '2px'})
    for rec in recordSet:
      if "icon" in rec:
        self._report.jsImports.add("font-awesome")
        self._report.cssImport.add("font-awesome")
    self.addGlobalVar("CONTEXT_MENU_VAL", "{}")
    self._jsStyles = {'liStyles': ""}

  @property
  def defined(self):
    """
    Return the static CSS style definition of this component
    """
    if self.pyStyle is None:
      self.pyStyle = self.CssClassDef()
    return self.pyStyle

  def onDocumentLoadFnc(self):
    """ Pure Javascript onDocumentLoad Function """
    self.addGlobalFnc("%s(htmlObj, data, jsStyles)" % self.__class__.__name__, '''
      var jsList = htmlObj.find('ul'); jsList.empty();
      data.forEach(function(rec){ 
        if(rec.icon != undefined) {var li = $('<li>').addClass(jsStyles.liStyles).html("<i class='"+ rec.icon +"' style='margin-right:5px'></i>" + rec.text)}
        else {var li = $('<li>').addClass(jsStyles.liStyles).html(rec.text)};
        li.click(function(event){var data = CONTEXT_MENU_VAL; eval(rec.event)}); jsList.append(li)})
      ''', 'Javascript Object builder')

  def __str__(self):
    self._report._scroll.add("$('nav[name=context_menus]').hide()")
    # TODO: Add a condition in the init to display the context menu only for some columns or rows when table for example
    if getattr(self, 'source') is None:
      raise Exception("Context Menu should be added to a component with the function attachMenu")

    if self.source.jqDiv is not None:
      if self.source.name == 'Tabulator':
        self._report.jsOnLoadFnc.add("$('html').click(function(){$('nav[name=context_menus]').hide()})")
        self.source._options['rowContext'] = '''
          function(event, row){
            if(row.getTable().options.dataTree){
              if(row.getTreeParent()) {CONTEXT_MENU_VAL = row.getTreeParent().getData()}
              else {CONTEXT_MENU_VAL = row.getData()}
            } else{CONTEXT_MENU_VAL = row.getData()};
            event.stopPropagation(); %(jqId)s.css({left: event.pageX + 1, top: event.pageY + 1, display: 'block'}); event.preventDefault()
          } ''' % {'jqDiv': self.source.jqDiv, 'jqId': self.jqId}
      else:
        self._report.jsOnLoadFnc.add('''
          $('html').click(function(){$('nav[name=context_menus]').hide()});
          %(jqDiv)s.on('contextmenu', function(event, i) {CONTEXT_MENU_VAL = %(val)s;
            event.stopPropagation(); %(jqId)s.css({left: event.pageX + 1, top: event.pageY + 1, display: 'block'}); event.preventDefault()
          })''' % {'jqDiv': self.source.jqDiv, 'val': self.source.contextVal, 'jqId': self.jqId})
    return '''
      <nav %(attr)s name='context_menus'>
        <ul style='list-style:none;padding:0px;margin:0'></ul>
      </nav>''' % {'attr': self.get_attrs(pyClassNames=self.defined)}


class OptionsBar(Html.Html):
  name, category, callFnc = 'Options', 'Event', 'optionsbar'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  _grpCls = CssGrpClsImage.CssClassIcon

  def __init__(self, report, recordset, width, height, size, color, border_color, options):
    super(OptionsBar, self).__init__(report, recordset, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1])
    self.css({'padding': '0', 'display': 'block', 'text-align': 'middle', 'color': color, 'margin-left': '5px',
              'background': self._report.theme.greys[0]})
    self.border_color = border_color
    if options.get("draggable", False):
      self.draggable()
    self.size = size

  def draggable(self, options=None):
    self.css({"border": "1px solid %s" % self.border_color})
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.dom.jquery_ui.draggable(options).toStr())
    #self._report.js.addOnLoad(self.dom.jquery_ui.draggable(options).toStr())
    return self

  def __str__(self):
    cssIcon = self._report.style.cssName('CssIcon')
    icons = []
    for rec in self.val:
      rec.update({'cssIcon': cssIcon, 'size': "%s%s" % (self.size[0], self.size[1])})
      if isinstance(rec.get('jsFnc', []), list):
        rec['jsFnc'] = ";".join(rec.get('jsFnc', []))
      if not 'tooltip' in rec:
        rec['tooltip'] = ''
      icons.append('<i class="%(icon)s %(cssIcon)s" style="font-size:%(size)s" title="%(tooltip)s" onclick="var data={event_val:\'%(icon)s\'};%(jsFnc)s"></i>' % rec)
    return '<div %(attrs)s>%(icons)s</div>' % {'attrs': self.get_attrs(pyClassNames=self.defined), 'icons': "".join(icons)}


class SignIn(Html.Html):
  name, category, callFnc = 'SignIn', 'Event', 'signin'
  __reqCss, __reqJs = ['font-awesome'], ['font-awesome']
  builder_name = False

  def __init__(self, report, text, size, icon):
    super(SignIn, self).__init__(report, text, width=size, widthUnit="px", height=size, heightUnit="px")
    self.size, self.icon = size, icon
    self.css({"text-align": "center", "font-size": "%s%s" % (size[0], size[1]), "padding": "5px", 'color': self._report.theme.colors[3],
              "margin": 0, "border-radius": "%s%s" % (size[0], size[1]), "border": "1px solid %s" % self._report.theme.colors[3], 'cursor': 'pointer'})

  def __str__(self):
    self._report.user = "o"
    if self._report.user == 'local':
      self.style.addCls(self.icon)
      return '<i title="Guest Mode" %(attrs)s></i>' % {'size': self.size, 'attrs': self.get_attrs(pyClassNames=self.pyStyle)}

    return '''
      <div title="%(user)s" %(attrs)s>
        <p style="margin:auto">%(letter)s</p>
      </div> ''' % {'size': self.size, 'letter': self._report.user[0].upper(), 'user': self._report.user, 'attrs': self.get_attrs(pyClassNames=self.pyStyle)}


class Filters(Html.Html):
  name, category, callFnc = 'Multi Filter', 'Event', 'multiFilter'
  __reqCss, __reqJs = ['jquery-scrollbar'], ['jquery', 'jquery-scrollbar']
  _grpCls = CssGrpClsList.CssClassListFilters

  def __init__(self, report, items, title, size, width, height, htmlCode, helper, profile):
    super(Filters, self).__init__(report, items, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode, profile=profile)
    self.add_title(title)
    self.css({"font-size": "%s%s" % (size[0], size[1]), "font-family": report.style.defaults.font.family})
    self._jsStyles = {'items': {'display': 'inline-block', 'padding': '1px 4px',
                                'color': self._report.theme.colors[-1], 'margin': '2px', 'border-radius': '5px', 'background-color': self._report.theme.colors[0]}}
    self.style.addCls('scroll_content')

  @property
  def jqId(self): return "$('#%s_div')" % self.htmlId

  @property
  def val(self):
    return '''
      function(){
        var existingItems = {}; 
        %(jqId)s.find('div[name=item]').each(function(){
          if ($(this).find('span').length > 0){existingItems[$(this).find('span').text()] = $(this).find('div').text()}
          else {existingItems[$(this).text()] = $(this).text()}}); 
        return existingItems}()''' % {'jqId': self.jqId}

  @property
  def _js__builder__(self):
    return '''htmlObj.empty();
      var col = null;
      if (Array.isArray(data)){data.forEach(function(rec){%(jsAddItem)s})}
      else {for (var col in data){var rec = data[col]; %(jsAddItem)s}} 
      ''' % {"jsAddItem": self.jsAddItem('rec', jsColumn="col")}

  def _jsCloseItem(self, jsFnc=None):
    if jsFnc is None:
      return "$(this).parent().remove()"

    return "(function(e){%s}(event)); $(this).parent().remove()" % ";".join(jsFnc).replace("'", "\\'")

  def jsToggleItem(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None, jsColumn="null", jsFlag=None, jsFncClosure=None):
    if jsFlag is None:
      raise Exception("A flag should be defined to toggle the items")

    add = self.jsAddItem(jsData, jsDataKey, isPyData, jsParse, jsFnc, jsColumn, jsFncClosure)
    remove = self.jsRemoveItems(jsData, jsDataKey, isPyData, jsParse, jsFnc)
    return "if(%(jsFlag)s){%(add)s} else {%(remove)s}" % {"jsFlag": jsFlag, "add": add, "remove": remove}

  def jsAddItem(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None, jsColumn="null", jsFncClosure=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    cssItem = self._report.style.cssCls('CssDivFilterItems')
    if jsFncClosure == False:
      return '''
            var idata = %(jsData)s; var existingItems = %(existingItems)s; var jsColumn = %(jsColumn)s;
            if (typeof jsStyles === "undefined"){var jsStyles = %(jsStyles)s};
            if (jsColumn !== null){
              if (jsColumn != '' && !(jsColumn in existingItems)){
                %(jqId)s.append('<div class="%(pyClass)s" name="item" style="'+ %(CssStyleBuilder)s(jsStyles.items) +'"><span style="font-style:bold;color:%(color)s">'+ %(jsColumn)s + '</span><div id="%(htmlId)s_'+ jsColumn +'" style="padding-left:18px">'+ idata +'</div></div>')}
              else if(jsColumn in existingItems){$('#%(htmlId)s_'+ jsColumn).text(idata)}
            } else{
              if (idata != '' && !(idata in existingItems)){
                %(jqId)s.append('<div class="%(pyClass)s" name="item" style="'+ %(CssStyleBuilder)s(jsStyles.items) +'">'+ idata +'</div>')
            }}''' % {'jqId': self.jqId, 'jsData': jsData, 'existingItems': self.val,
                     "CssStyleBuilder": self._report.js.fncs.cssStyle,
                     "jsStyles": json.dumps(self._jsStyles), "jsColumn": jsColumn,
                     'color': self._report.theme.colors[7], 'htmlId': self.htmlId, 'pyClass': cssItem}

    return '''
      var idata = %(jsData)s; var existingItems = %(existingItems)s; var jsColumn = %(jsColumn)s;
      if (typeof jsStyles === "undefined"){ var jsStyles = %(jsStyles)s};
      if (jsColumn !== null){
        if (jsColumn != '' && !(jsColumn in existingItems)){
          %(jqId)s.append('<div class="%(pyClass)s" name="item" style="'+ %(CssStyleBuilder)s(jsStyles.items) +'"><i onclick="%(jsCloseItem)s" style="font-size:9px;padding-right:2px;margin-right:10px;cursor:pointer" class="fas fa-times"></i><span style="font-style:bold;color:%(color)s">'+ %(jsColumn)s + '</span><div id="%(htmlId)s_'+ jsColumn +'" style="padding-left:18px">'+ idata +'</div></div>')}
        else if(jsColumn in existingItems){
          $('#%(htmlId)s_'+ jsColumn).text(idata)}
      } else{
        if (idata != '' && !(idata in existingItems)){
          %(jqId)s.append('<div class="%(pyClass)s" name="item" style="'+ %(CssStyleBuilder)s(jsStyles.items) +'"><i onclick="%(jsCloseItem)s" style="font-size:9px;padding-right:2px;margin-right:10px;cursor:pointer" class="fas fa-times"></i>'+ idata +'</div>')
      }}''' % {'jqId': self.jqId, 'jsData': jsData, 'existingItems': self.val, "jsStyles": json.dumps(self._jsStyles),
               "jsColumn": jsColumn, "jsCloseItem": self._jsCloseItem(jsFncClosure),
               "CssStyleBuilder": self._report.js.fncs.cssStyle, 'color': self._report.theme.colors[7],
               'htmlId': self.htmlId, 'pyClass': cssItem}

  def jsAddItems(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      var jsStyles = %(jsStyles)s;
      var fData = %(jsData)s; fData.forEach(function(rec){%(jsAddItem)s})
      ''' % {'jsData': jsData, 'jsAddItem': self.jsAddItem('rec'), "jsStyles": json.dumps(self._jsStyles)}

  def jsClear(self):
    return "%(jqId)s.find('div[name=item]').each(function(){$(this).remove()})" % {'jqId': self.jqId}

  def jsRemoveItems(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      var fData = %(jsData)s; 
      if (Array.isArray(fData)){
        fData.forEach(function(rec){
          %(jqId)s.find('div[name=item]').each(function(){if($(this).text() == rec){$(this).remove()}})}) 
      } else {
        %(jqId)s.find('div[name=item]').each(function(){
          if($(this).find('div').text() == fData){$(this).remove()} })
      }''' % {'jsData': jsData, 'jqId': self.jqId}

  def __str__(self):
    return '''
      <div %(cssAttr)s>
        <div id='%(htmlId)s'></div>
      </div>
      <div style='font-size:9px;margin:0 0 5px auto;width:40px;font-style:italic;cursor:pointer' onclick="%(click)s"><i class="fas fa-times-circle" style="font-size:9px;margin-right:2px"></i>clear</div>
      ''' % {'htmlId': "%s_div" % self.htmlId, 'cssAttr': self.get_attrs(pyClassNames=[s for s in self.defined if s not in ['CssDivFilterItems']]),
             'click': self.jsClear()}
