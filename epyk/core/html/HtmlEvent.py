#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptSliders
from epyk.core.html.options import OptList

from epyk.core.html.entities import EntHtml4

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlJqueryUI
from epyk.core.js.html import JsHtmlList
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi

# The list of CSS classes
from epyk.core.css.styles import GrpClsJqueryUI


class ProgressBar(Html.Html):
  requirements = ('jqueryui', )
  name = 'Progress Bar'

  def __init__(self, report, number, total, width, height, attrs, helper, options, htmlCode, profile):
    options['max'] = total
    super(ProgressBar, self).__init__(report, number, htmlCode=htmlCode, css_attrs={"width": width, "height": height, 'box-sizing': 'border-box'}, profile=profile)
    self.add_helper(helper)
    self.__options = OptSliders.OptionsProgBar(self, options)
    self.options.background = self._report.theme.success[1]

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

  def to(self, number, timer=10):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param timer: Integer. the spped of the increase in millisecond
    """
    self._report.body.onReady([
      self._report.js.objects.number(self.val, varName="%s_counter" % self.htmlCode, setVar=True),
      self._report.js.window.setInterval([
        self._report.js.if_(
          self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self._report.js.objects.number(
              self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              varName="window.%s_counter" % self.htmlCode, setVar=True),
            self.build(self._report.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ])
    return self

  @property
  def _js__builder__(self):
    return '''
      options.value = parseFloat(data);
      %(jqId)s.progressbar(options).find('div').attr("data-toggle", "tooltip").attr("title", ""+ (parseFloat(data) / options.max * 100).toFixed(2) +"%% ("+ parseFloat(data) +" / "+ options.max +")").css(options.css);
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


class Menu(Html.Html):
  requirements = ('jqueryui', )
  name = 'Menu'

  def __init__(self, report, records, width, height, helper, options, htmlCode, profile):
    super(Menu, self).__init__(report, records, css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
    self.add_helper(helper)
    self.__options = OptSliders.OptionsMenu(self, options)
    self.style.css.display = 'block'
    self.style.css.position = 'relative'

  @property
  def style(self):
    """
    Description:
    -----------

    :rtype: rpClsJqueryUI.ClassMenu
    """
    if self._styleObj is None:
      self._styleObj = GrpClsJqueryUI.ClassMenu(self)
    return self._styleObj

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
          var isRoot =  options.isRoot; if(typeof isRoot === 'undefined'){isRoot = true}
          data.forEach(function(rec){
            if (rec.items != undefined) {
              var li = $('<li></li>'); var div = $('<div>'+ rec.value +'</div>');
              li.append(div); var ul = $('<ul aria-hidden="true"></ul>'); 
              options.clearDropDown = false; options.isRoot = false;
              %(pyCls)s(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
            } else {
              var div = $('<div>'+ rec.value +'</div>').css({"width": '150px'}); var li = $('<li></li>');
              li.append(div); jqHtmlObj.append(li)};
          }); if(isRoot){jqHtmlObj.menu(options)}''' % {"pyCls": self.__class__.__name__}

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
    Description:
    -----------
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
  requirements = ('jqueryui', )
  name = 'Menu'

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
  requirements = ('jqueryui', )
  name = 'Slider'

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
        <div id="%(htmlCode)s"></div>
      </div>%(helper)s''' % {"strAttr": self.get_attrs(withId=False), "min": self.options.min, "htmlCode": self.htmlCode,
                             "max": self.options.max, "helper": self.helper}


class Range(Slider):
  name = "Slider Range"

  @property
  def _js__builder__(self):
    return '''options.values = [Math.min(...data), Math.max(...data)]; %(jqId)s.slider(options).css(options.css)
        ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}


class SliderDate(Slider):
  name = "Slider Date"

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

    :rtype: JsHtmlJqueryUI.JsHtmlSliderDate
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDate(self, report=self._report)
    return self._dom


class SliderDates(SliderDate):

  @property
  def _js__builder__(self):
    return '''
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

    :rtype: JsHtmlJqueryUI.JsHtmlSliderDates
    """
    if self._dom is None:
      self._dom = JsHtmlJqueryUI.JsHtmlSliderDates(self, report=self._report)
    return self._dom


class SkillBar(Html.Html):
  name = 'Skill Bars'

  def __init__(self, report, data, y_column, x_axis, title, width, height, htmlCode, options, profile):
    super(SkillBar, self).__init__(report, "", css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
    self.add_title(title, options={'content_table': False})
    self.innerPyHTML = report.ui.layouts.table(options={"header": False}) # data, y_column, x_axis)
    self.innerPyHTML.options.managed = False
    for rec in data:
      value = report.ui.div(EntHtml4.NO_BREAK_SPACE).css({"width": '%s%s' % (rec[y_column], options.get("unit", 'px')), 'margin-left': "2px",  "background": options.get("background", report.theme.success[0])})
      value.options.managed = False
      if options.get("values", False):
        self.innerPyHTML += [rec[x_axis], value, "%s%s" % (int(rec[y_column]), options.get("unit", 'px'))]
        self.innerPyHTML[-1][2].style.css.padding = "0 5px"
      else:
        self.innerPyHTML += [rec[x_axis], value]
      self.innerPyHTML[-1][1].attr["align"] = 'left'
      self.innerPyHTML[-1][0].style.css.padding = "0 5px"
      self.innerPyHTML[-1][1].style.css.width = "100%"
      if options.get("borders", False):
        self.innerPyHTML[-1][1].style.css.border = "1px solid %s" % report.theme.greys[4]
        self.innerPyHTML[-1][1][0].style.css.margin_left = 0
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


class OptionsBar(Html.Html):
  requirements = ('font-awesome', )
  name = 'Options'

  def __init__(self, report, recordset, width, height, color, options, profile):
    super(OptionsBar, self).__init__(report, [], css_attrs={"width": width, 'height': height}, profile=profile)
    self.__options = OptSliders.OptionBar(self, options)
    self.css({'padding': '0', 'display': 'block', 'text-align': 'middle', 'color': color, 'margin-left': '5px',
              'background': self._report.theme.greys[0]})
    for rec in recordset:
      self += rec
    if self.options.draggable:
      self.draggable()

  @property
  def options(self):
    """
    :rtype: OptSliders.OptionBar
    """
    return self.__options

  def __add__(self, icon):
    """ Add items to a container """
    icon = self._report.ui.icon(icon)
    icon.style.css.margin = "5px"
    super(OptionsBar, self).__add__(icon)
    return self

  def draggable(self, options=None):
    self.css({'border-radius': '5px', "border": "1px dotted %s" % self._report.theme.success[1]})
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.dom.jquery_ui.draggable(options).toStr())
    return self

  def __str__(self):
    str_html = "".join([v.html() for v in self.val])
    return '<div %(attrs)s>%(icons)s</div>' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()), 'icons': str_html}


class SignIn(Html.Html):
  requirements = ('font-awesome', )
  name = 'SignIn'

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
  name = 'Filters'
  requirements = ('font-awesome', )

  def __init__(self, report, items, width, height, htmlCode, helper, options, profile):
    super(Filters, self).__init__(report, items, css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
    self.__options = OptList.OptionsTagItems(self, options)
    self._jsStyles['delete'] = 'function(){this.parentNode.remove()}'
    self.input = self._report.ui.input()
    self.input.style.css.text_align = 'left'
    self.input.style.css.padding = '0 5px'
    self.input.options.managed = False
    self.selections = self._report.ui.div()
    self.selections.options.managed = False
    self.selections.attr["name"] = "panel"
    self.selections.css({'height': '30px', 'padding': '5px 2px'})
    self.add_helper(helper)
    self.__enter_def = False

  @property
  def options(self):
    """
    :rtype: OptList.OptionsTagItems
    """
    return self.__options

  @property
  def _js__builder__(self):
    return '''
      var panel = htmlObj.querySelector('[name=panel]'); panel.innerHTML = '';
      data.forEach(function(val){
        if(typeof val === 'string'){ val = {name: options.category, category: options.category, value: val, disabled: false, fixed: false} }
        else{
          if(val.category === undefined){ if(val.name === undefined) {val.category = options.category} else {val.category = val.name}}
          if(val.name === undefined){ val.name = val.category }};
        chipAdd(panel, val, options)})'''

  def enter(self, jsFncs, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    self.__enter_def = True
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.keydown.enter([JsUtils.jsConvertFncs(jsFncs, toStr=True), self.dom.add(self.dom.input)] + jsFncs + [self.input.dom.empty()], profile)
    return self

  def drop(self, jsFncs, preventDefault=True, profile=False):
    """
    Description:
    -----------

    :param jsFncs:
    :param preventDefault:
    :param profile:
    """
    self.style.css.border = "1px dashed black"
    self.tooltip("Drag and drop values here")
    return super(Filters, self).drop(jsFncs, preventDefault, profile)

  def delete(self, jsFncs, profile=False):
    """
    Description:
    -----------

    :param jsFncs:
    :param profile:
    """
    if self.__enter_def:
      raise Exception("delete on chip must be triggered before enter")

    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._jsStyles['delete'] = 'function(){ this.parentNode.remove(); %s}' % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self # function(event){ this.parentNode.remove()}

  def append(self, value, category=None, name=None, disabled=False, fixed=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param value:
    :param category:
    :param disabled:
    :param fixed:
    """
    rec = {"value": value, 'disabled': disabled, 'fixed': fixed, 'category': category, 'name': name}
    if category is None:
      rec['category'] = name or self.options.category
    rec['name'] = name or rec['category']
    self._vals.append(rec)

  @property
  def dom(self):
    """
    Description:
    -----------
    The Javascript Dom object

    :rtype: JsHtmlList.Tags
    """
    if self._dom is None:
      self._dom = JsHtmlList.Tags(self, report=self._report)
    return self._dom

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    #
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors['ChipAdd'] = '''function chipAdd(panel, record, options){
        var div = document.createElement("div"); for (var key in options.item_css){ div.style[key] = options.item_css[key]};
        div.setAttribute('data-category', record.category);
        var content = document.createElement("span"); for (var key in options.value_css){ content.style[key] = options.value_css[key]};
        content.setAttribute('name', 'chip_value'); content.innerHTML = record.value; 
        if(options.visible){
          var p = document.createElement("p"); for (var key in options.category_css){ p.style[key] = options.category_css[key]};
          p.innerHTML = record.name; div.appendChild(p)
        };
        div.appendChild(content);
        if(!record.fixed){
          var icon = document.createElement("i"); for (var key in options.icon_css){ icon.style[key] = options.icon_css[key] };
          icon.classList.add('fas'); icon.classList.add('fa-times');  icon.addEventListener('click', options.delete );
          div.appendChild(icon)}
        panel.appendChild(div);
    }'''
    if not self.options.visible:
      self.input.style.css.display = False
    return '''<div %(attrs)s>%(input)s%(selections)s</div>%(helper)s''' % {'attrs': self.get_attrs(pyClassNames=self.style.get_classes()),
          'input': self.input.html(), 'selections': self.selections.html(),  'helper': self.helper}
