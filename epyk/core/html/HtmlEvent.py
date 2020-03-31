
import re
import json

from epyk.core.html import Html
from epyk.core.html.options import OptSliders
from epyk.core.html.entities import EntHtml4

from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.Imports import requires
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi

# The list of CSS classes
from epyk.core.css.styles import GrpClsJqueryUI


class ProgressBar(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Progress Bar', 'Sliders', 'progressbar'

  def __init__(self, report, number, total, width, height, attrs, helper, options, profile):
    options['max'] = total
    super(ProgressBar, self).__init__(report, number, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self._jsStyles = {'css': {"background": self._report.theme.success[1]}}
    self.__options = OptSliders.OptionsProgBar(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    The progress bar is designed to display the current percent complete for a process.
    The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar

    :rtype: OptSliders.OptionsProgBar
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      options.value = parseFloat(data); jQuery(htmlObj).progressbar(options).find('div').css(options.css);
      jQuery(htmlObj).progressbar(options).find('div').attr("title", ""+ (parseFloat(data) / options.max * 100).toFixed(2) +"% ("+ parseFloat(data) +" / "+ options.max +")");
      '''

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.ProgressBar
    """
    if self._js is None:
      self._js = JsQueryUi.ProgressBar(self, report=self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    ------------
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
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)

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


class Menu(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jquery', 'jqueryui']
  name, category, callFnc = 'Menu', 'Sliders', 'menu'

  def __init__(self, report, records, width, height, attrs, helper, options, profile):
    super(Menu, self).__init__(report, records, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.__options = OptSliders.OptionsMenu(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    The progress bar is designed to display the current percent complete for a process.
    The bar is coded to be flexibly sized through CSS and will scale to fit inside its parent container by default.

    Related Pages:
    --------------
    https://api.jqueryui.com/menu

    :rtype: OptSliders.OptionsMenu
    """
    return self.__options

  @property
  def _js__builder__(self):
    return "jQuery(htmlObj).menu({value: parseFloat(data)}).find('div').css(options)"

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Related Pages:
    --------------
    https://api.jqueryui.com/menu

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Menu
    """
    if self._js is None:
      self._js = JsQueryUi.Menu(self, report=self._report)
    return self._js

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
    return '<div %s></div>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Slider(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Slider', 'Sliders', 'slider'

  def __init__(self, report, value, typeObj, range, animate, step, min, max, width, height,
               globalFilter, recordSet, color, attrs, helper, profile):
    data = {'animate': animate, 'min': min, 'max': max, 'step': step}
    super(Slider, self).__init__(report, data, width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1],
                                 globalFilter=globalFilter, profile=profile)
    #self.__options = OptSliders.OptionsSlider(self, options)

  @property
  def options(self):
    """

    :rtype: OptSliders.OptionsSlider
    """
    return self.__options

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component

    :rtype: GrpClsJqueryUI.ClassSlider
    """
    if self._styleObj is None:
      self._styleObj = GrpClsJqueryUI.ClassSlider(self)
    return self._styleObj

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Slider
    """
    if self._js is None:
      self._js = JsQueryUi.Slider(self, report=self._report)
    return self._js

  @property
  def dom(self):
    """
    Description:
    -----------
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


class SkillBar(Html.Html):
  name, category, callFnc = 'Skill Bars', 'Chart', 'skillbars'

  def __init__(self, report, data, y_column, x_axis, title, width, height, htmlCode, colUrl, colTooltip, filters, profile):
    super(SkillBar, self).__init__(report, "", css_attrs={"width": width, "height": height}, htmlCode=htmlCode,
                                   globalFilter=filters, profile=profile)
    self.add_title(title, options={'content_table': False})
    self.innerPyHTML = report.ui.layouts.table(data, y_column, x_axis)
    self.innerPyHTML.inReport = False
    for c in self.innerPyHTML.col(i=1):
      if c.val not in y_column:
        c.set_html_content(report.ui.div(EntHtml4.NO_BREAK_SPACE).css({"width": '%spx' % c.val, 'margin-left': "2px",
                                                                       "background": report.theme.success[0]}))
    self.innerPyHTML.style.clear()
    self.css({"margin": '5px 0'})

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
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)

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
  # _grpCls = CssGrpClsText.CssClassTextItem

  def __init__(self, report, recordSet, width, height, visible, options, profile):
    for rec in recordSet:
      if isinstance(rec.get('event'), list):
        rec['event'] = ";".join(rec['event'])
    super(ContextMenu, self).__init__(report, recordSet, css_attrs={"width": width, "height": height}, profile=profile)
    self.css({'display': 'block' if visible else 'none', 'position': 'absolute', 'z-index': 200,
              'padding': 0, 'margin': 0, 'background-color': self._report.theme.greys[0],
              'border': '1px solid %s' % self._report.theme.colors[5], 'border-radius': '2px'})
    for rec in recordSet:
      if "icon" in rec:
        self._report.jsImports.add("font-awesome")
        self._report.cssImport.add("font-awesome")
    # self.addGlobalVar("CONTEXT_MENU_VAL", "{}")
    self._jsStyles = {'liStyles': ""}

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
  # _grpCls = CssGrpClsImage.CssClassIcon

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

  def __init__(self, report, text, size, icon):
    super(SignIn, self).__init__(report, text, css_attrs={"width": size, 'height': size})
    self.size, self.icon = "%s%s" % (size[0]-8, size[1]), icon
    self.css({"text-align": "center", "padding": 0, 'color': self._report.theme.colors[3],
              "margin": 0, "border-radius": "%s%s" % (size[0], size[1]),
              "border": "1px solid %s" % self._report.theme.colors[3], 'cursor': 'pointer'})

  def __str__(self):
    if not hasattr(self._report, 'user') or self._report.user == 'local':
      self.attr["class"].add(self.icon or "fas fa-user-tie")
      self.style.css.font_family = "Font Awesome 5 Free"
      self.style.css.padding = "2px"
      self.style.css.font_size = self.size
      return '<i title="Guest Mode" %(attrs)s></i>' % {'size': self.size, 'attrs': self.get_attrs(pyClassNames=self.style.get_classes())}

    return '''
      <div title="%(user)s" %(attrs)s>
        <p style="font-size:%(size)s;margin-top:-2px">%(letter)s</p>
      </div> ''' % {'size': self.size, 'letter': self._report.user[0].upper(), 'user': self._report.user,
                    'attrs': self.get_attrs(pyClassNames=self.style.get_classes())}


class Filters(Html.Html):
  name, category, callFnc = 'Multi Filter', 'Event', 'multiFilter'
  __reqCss, __reqJs = ['jquery-scrollbar'], ['jquery', 'jquery-scrollbar']
  # _grpCls = CssGrpClsList.CssClassListFilters

  def __init__(self, report, items, title, width, height, htmlCode, helper, profile):
    super(Filters, self).__init__(report, items, css_attrs={"width": width, "height": height}, code=htmlCode, profile=profile)
    self.add_title(title, options={'content_table': False})
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
