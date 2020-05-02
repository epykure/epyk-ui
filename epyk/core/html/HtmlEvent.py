
import re
import json

from epyk.core.html import Html
from epyk.core.html.options import OptSliders
from epyk.core.html.options import OptList
from epyk.core.html.HtmlList import Li

from epyk.core.html.entities import EntHtml4

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.html import JsHtmlList
from epyk.core.js.Imports import requires
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi

# The list of CSS classes
from epyk.core.css.styles import GrpClsJqueryUI


class ProgressBar(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Progress Bar', 'Sliders', 'progressbar'

  def __init__(self, report, number, total, width, height, attrs, helper, options, htmlCode, profile):
    options['max'] = total
    super(ProgressBar, self).__init__(report, number, htmlCode=htmlCode, css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'}, profile=profile)
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

			https://api.jqueryui.com/progressbar

    :rtype: OptSliders.OptionsProgBar
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      options.value = parseFloat(data); jQuery(htmlObj).progressbar(options).find('div').css(options.css);
      %(jqId)s.progressbar(options).find('div').attr("title", ""+ (parseFloat(data) / options.max * 100).toFixed(2) +"%% ("+ parseFloat(data) +" / "+ options.max +")");
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

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
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Menu', 'Menus', 'menu'

  def __init__(self, report, records, width, height, attrs, helper, options, htmlCode, profile):
    super(Menu, self).__init__(report, records, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.__options = OptSliders.OptionsMenu(self, options)
    self.css({"display": 'block', 'position': 'relative'})

  @property
  def options(self):
    """
    Description:
    -----------

    Related Pages:

			https://api.jqueryui.com/menu

    :rtype: OptSliders.OptionsMenu
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
          var jqHtmlObj = jQuery(htmlObj); if (options.clearDropDown) {jqHtmlObj.empty()};
          data.forEach(function(rec){
            if (rec.items != undefined) {
              var li = $('<li></li>'); var div = $('<div>'+ rec.value +'</div>').css({"width": '150px'});
              li.append(div); var ul = $('<ul aria-hidden="true"></ul>'); options.clearDropDown = false;
              %(pyCls)s(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
            } else {
              var div = $('<div>'+ rec.value +'</div>').css({"width": '150px'}); var li = $('<li></li>');
              li.append(div); jqHtmlObj.append(li)};
          }); jqHtmlObj.menu(options)''' % {"pyCls": self.__class__.__name__}

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Related Pages:

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
    return '<ul %s></ul>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Dialog(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Menu', 'Menus', 'menu'

  def __init__(self, report, text, width, height, attrs, helper, options, htmlCode, profile):
    super(Dialog, self).__init__(report, text, css_attrs={"width": width, "height": height}, profile=profile)
    self.add_helper(helper)
    self.__options = OptSliders.OptionDialog(self, options)

  @property
  def options(self):
    """
    Description:
    -----------
    Open content in an interactive overlay.

    Related Pages:

			https://jqueryui.com/dialog/

    :rtype: OptSliders.OptionDialog
    """
    return self.__options

  @property
  def _js__builder__(self):
    return "jQuery(htmlObj).empty(); jQuery(htmlObj).append('<p>'+ data +'</p>'); jQuery(htmlObj).dialog(options)"

  @property
  def js(self):
    """
    Description:
    -----------
    Open content in an interactive overlay.

    Related Pages:

			https://jqueryui.com/dialog/

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Dialog
    """
    if self._js is None:
      self._js = JsQueryUi.Dialog(self, report=self._report)
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
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class Slider(Html.Html):
  __reqCss, __reqJs = ['jqueryui'], ['jqueryui']
  name, category, callFnc = 'Slider', 'Sliders', 'slider'

  def __init__(self, report, number, min, max, width, height, attrs, helper, options, htmlCode, profile):
    options.update({'max': max, 'min': min})
    super(Slider, self).__init__(report, number, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._jsStyles = {'css': {"background": self._report.theme.success[0]}}
    self.__options = OptSliders.OptionsSlider(self, options)
    self.style.css.padding = "0 10px"
    self.style.css.margin = "15px 0"

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

			https://api.jqueryui.com/slider

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsQueryUi.Slider
    """
    if self._js is None:
      self._js = JsQueryUi.Slider(self, report=self._report)
    return self._js

  def change(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered after the user slides a handle, if the value has changed; or if the value is changed programmatically via the value method.

    Related Pages:

			https://api.jqueryui.com/slider/#event-change

    Attributes:
    ----------
    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["change"] = "function(event, ui){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def start(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered when the user starts sliding.

    Related Pages:

			https://api.jqueryui.com/slider/#event-start

    Attributes:
    ----------
    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["start"] = "function(event, ui){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def slide(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered when the user starts sliding.

    Related Pages:

			https://api.jqueryui.com/slider/#event-slide

    Attributes:
    ----------
    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["slide"] = "function(event, ui){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

  def stop(self, jsFnc, profile=None):
    """
    Description:
    -----------
    Triggered after the user slides a handle.

    Related Pages:

			https://api.jqueryui.com/slider/#event-stop

    Attributes:
    ----------
    :param jsFnc:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self._jsStyles["stop"] = "function(event, ui){ %s }" % JsUtils.jsConvertFncs(jsFnc, toStr=True)
    return self

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
    return ''' options.value = data; %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '''
      <div %(strAttr)s>
        <div style="width:100%%;height:20px">
          <span style="float:left;display:inline-block">%(min)s</span>
          <span style="float:right;display:inline-block">%(max)s</span>
        </div>
        <div id="%(htmlId)s"></div>
      </div>%(helper)s''' % {"strAttr": self.get_attrs(withId=False), "min": self.options.min, "htmlId": self.htmlId,
                             "max": self.options.max, "helper": self.helper}


class Range(Slider):

  @property
  def _js__builder__(self):
    return '''options.values = [Math.min(...data), Math.max(...data)]; %(jqId)s.slider(options).css(options.css)
        ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}


class SliderDate(Slider):

  def __init__(self, report, number, min, max, width, height, attrs, helper, options, htmlCode, profile):
    super(SliderDate, self).__init__(report, number, min, max, width, height, attrs, helper, options, htmlCode, profile)
    self.options.min = min
    self.options.max = max
    self.options.step = 86400

  @property
  def _js__builder__(self):
    return '''
      const minDt = new Date(options.min).getTime() / 1000;
      const maxDt = new Date(options.max).getTime() / 1000;
      
      options.min = minDt; options.max = maxDt;
      options.value = new Date(data).getTime() / 1000;
      %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDate(self, report=self._report)
    return self._dom


class SliderDates(SliderDate):

  @property
  def _js__builder__(self):
    return ''' console.log(options);
      const minDt = new Date(options.min).getTime() / 1000;
      const maxDt = new Date(options.max).getTime() / 1000;

      options.min = minDt; options.max = maxDt;
      options.values = [new Date(data[0]).getTime() / 1000, new Date(data[1]).getTime() / 1000];
      %(jqId)s.slider(options).css(options.css)
      ''' % {"jqId": JsQuery.decorate_var("jQuery(htmlObj)", convert_var=False)}

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDates(self, report=self._report)
    return self._dom


class SkillBar(Html.Html):
  name, category, callFnc = 'Skill Bars', 'Chart', 'skillbars'

  def __init__(self, report, data, y_column, x_axis, title, width, height, htmlCode, colUrl, colTooltip, filters, profile):
    super(SkillBar, self).__init__(report, "", css_attrs={"width": width, "height": height}, htmlCode=htmlCode,
                                   globalFilter=filters, profile=profile)
    self.add_title(title, options={'content_table': False})
    self.innerPyHTML = report.ui.layouts.table(options={"header": False}) # data, y_column, x_axis)
    self.innerPyHTML.inReport = False
    for rec in data:
      value = report.ui.div(EntHtml4.NO_BREAK_SPACE).css({"width": '%spx' % rec[y_column], 'margin-left': "2px",  "background": report.theme.success[0]})
      value.inReport = False
      self.innerPyHTML += [rec[x_axis], value]
      self.innerPyHTML[-1][1].attr["align"] = 'left'
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

  def __init__(self, report, recordSet, width, height, visible, options, profile):
    super(ContextMenu, self).__init__(report, [], css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = OptList.OptionsLi(self, options)
    self.css({'display': 'block' if visible else 'none', 'position': 'absolute', 'z-index': 200,
              'padding': 0, 'margin': 0, 'background-color': self._report.theme.greys[0],
              'border': '1px solid %s' % self._report.theme.colors[5], 'border-radius': '2px'})
    for rec in recordSet:
      self += rec

  @property
  def options(self):
    """

    :rtype: OptList.OptionsLi
    """
    return self.__options

  def __add__(self, htmlObj):
    """

    :param d:
    """
    if not hasattr(htmlObj, 'inReport'):
      htmlObj = self._report.ui.div(htmlObj)
    htmlObj.inReport = False
    li_obj = Li(self._report, htmlObj) if not isinstance(htmlObj, Li) else htmlObj
    li_obj.css({"padding": "5px", 'cursor': 'pointer'})
    if hasattr(htmlObj, 'inReport'):
      htmlObj.inReport = False
    self.val.append(li_obj)
    return self

  def __getitem__(self, i):
    return self.val[i].val

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
    #self._report._scroll.add("$('nav[name=context_menus]').hide()")
    # TODO: Add a condition in the init to display the context menu only for some columns or rows when table for example
    if getattr(self, 'source') is None:
      raise Exception("Context Menu should be added to a component with the function contextMenu")

    str_vals = "".join([i.html() for i in self.val]) if self.val is not None else ""
    self.mouse(out_fncs=[self.dom.hide()]) # hide when mouse leave the component
    return '''
      <nav %(attr)s name='context_menus'>
        <ul style='list-style:none;padding:0px;margin:0'>%(val)s</ul>
      </nav>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': str_vals}


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

  def __init__(self, report, items, title, width, height, htmlCode, helper, options, profile):
    super(Filters, self).__init__(report, [], css_attrs={"width": width, "height": height}, code=htmlCode, profile=profile)
    self.add_title(title, options={'content_table': False, 'managed': False})
    self._jsStyles = {'items': {'display': 'inline-block', 'padding': '1px 4px',
                                'color': self._report.theme.colors[-1], 'margin': '2px', 'border-radius': '5px', 'background-color': self._report.theme.colors[0]}}
    self.__options = OptList.OptionsTagItems(self, options)
    for item in items:
      self += item

  @property
  def options(self):
    """

    :rtype: OptList.OptionsTagItems
    """
    return self.__options

  def __getitem__(self, i):
    return self.val[i]

  def __add__(self, htmlObj):
    """ Add items to a container """
    if not hasattr(htmlObj, 'inReport'):
      htmlObj = self._report.ui.div(htmlObj)
      icon = self._report.ui.icon("fas fa-times").css({"margin-left": '2px'})
      htmlObj += icon
      icon.click([htmlObj.dom.remove()])
    htmlObj.style.css.display = 'inline'
    htmlObj.css(self.options.item_css)
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    self.val.append(htmlObj)
    return self

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object

    :rtype: JsHtmlJqueryUI.JsHtmlSlider
    """
    if self._dom is None:
      self._dom = JsHtmlList.Tags(self, report=self._report)
    return self._dom

  def __str__(self):
    str_data = "".join([s.html() for s in self.val])
    return '''
      <div %(cssAttr)s>
        %(title)s
        <div name="panel" style="width:100%%">%(data)s</div>
      </div>''' % {'title': self.title, 'cssAttr': self.get_attrs(pyClassNames=self.style.get_classes()), 'data': str_data}
