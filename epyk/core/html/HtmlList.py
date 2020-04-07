"""
List of all the different templates configurations available for displaying bespoke lists.
This list can be extended and it is easy to test a new configuration by different defining the HTML template in the common list object.
List are standard and very popular HTML objects, please have a look at the below websites if you need further information to manipulate them in your report

"""

import re
import json

from epyk.core.js import JsUtils
from epyk.core.html import Html
from epyk.core.html.options import OptList

# The list of Javascript classes
from epyk.core.js.html import JsHtml

# The list of CSS classes
from epyk.core.css.styles import GrpCls
# from epyk.core.css.styles import CssGrpClsList


class Li(Html.Html):
  name, category, callFnc = 'Entries', 'Lists', 'list_entries'

  def __init__(self, report, text):
    super(Li, self).__init__(report, text)
    self.css({'font-size': 'inherit', 'margin': "1px 5px", 'padding': 0})

  @property
  def no_decoration(self):
    """
    Property to remove the list default style
    """
    self.css({"text-decoration": "none", "list-style-type": 'none'})
    return self

  def add_label(self, text, css=None, position="before", for_=None):
    """
    Add an elementary label component

    Example

    Documentation
    https://www.w3schools.com/tags/tag_label.asp

    :param text: The label content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param for_: Specifies which form element a label is bound to
    """
    self.label = ""
    if text is not None:
      dfl_css = {"float": 'none', 'width': 'none'}
      if css is not None:
        dfl_css.update(css)
      self.label = self._report.ui.texts.label(text)
      if for_ is not None:
        # Attach the label to another HTML component based on the ID
        self.label.attr['for'] = for_
      if position == "before":
        self.prepend_child(self.label)
      else:
        self.append_child(self.label)
      self.label.css(dfl_css)
    return self

  def set_html_content(self, htmlObj):
    """
    Set the cell content to be an HTML object

    :param htmlObj: Python HTML object
    :return: self, the cell object to allow the chaining
    """
    htmlObj.inReport = False
    self.innerPyHTML = htmlObj
    return self

  def click(self, jsFncs, profile=False):
    if self.innerPyHTML is not None:
      return self.innerPyHTML.click(jsFncs, profile)

    return super(Li, self).click(jsFncs, profile)

  def __str__(self):
    return "<li %s>%s</li>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)


class List(Html.Html):
  name, category, callFnc = 'List', 'Lists', 'list'
  # The CSS Group attached to this component
  # grpCls = CssGrpClsList.CssClassList

  def __init__(self, report, data, color, width, height, htmlCode, helper, options, profile):
    super(List, self).__init__(report, data, css_attrs={"width": width, "height": height}, code=htmlCode, profile=profile)
    self.__options = OptList.OptionsLi(self, options)
    self.add_helper(helper)
    self.color = color if color is not None else self._report.theme.greys[9]
    self.css({'padding': 0, 'margin': "1px", 'list-style-position': 'inside'})
    self.items = None
    for item in data:
      self.add_item(item)
    if len(data) > 0:
      self.set_items()

  @property
  def options(self):
    """

    :rtype: OptList.OptionsLi
    """
    return self.__options

  @property
  def dom(self):
    """

    :rtype: JsHtml.JsHtmlIcon
    :return:
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlList(self, report=self._report)
    return self._dom

  def __getitem__(self, i):
    """

    :param i:
    :rtype: Li
    """
    return self.items[i]

  def add_item(self, d):
    """

    :param d:
    :return:
    """
    if self.items is None:
      self.items = []
    li_obj = Li(self._report, d)
    if hasattr(d, 'inReport'):
      d.inReport = False
    self.items.append(li_obj)
    return self

  def set_items(self):
    """
    """
    if self.items is None:
      self.items = []
    for d in self.val:
      li_obj = Li(self._report, d)
      li_obj.inReport = False
      self._report.ui.register(li_obj)
      li_obj.css(self.options.li_css)
      if self.options.li_class:
        li_obj.attr["class"].add(self.options.li_class)
      self.items.append(li_obj)
    return self

  def on_items(self, event, jsFncs, profile=False):
    """

    :return:
    """
    for i in self.items:
      i.on(event, jsFncs, profile)
    return self

  def click_items(self, jsFncs, profile=False):
    """

    :param jsFncs:
    :param profile:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    for i, item in enumerate(self.items):
      fnc = JsUtils.jsConvertFncs([
        self._report.js.getElementsByName("divs_%s" % self.htmlId).all(self._report.js.objects.dom("elt").hide().r),
        self._report.js.getElementsByName("divs_%s" % self.htmlId)[i].toggle().r])
      item.click(fnc + jsFncs, profile)
    return self

  def __str__(self):
    self._vals = "".join([i.html() for i in self.items]) if self.items is not None else ""
    #self.builder_name = self.__class__.__name__
    #self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<ul %s>%s</ul>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self._vals)


class Groups(Html.Html):
  name, category, callFnc = 'Groups', 'Lists', 'groups'

  def __init__(self, report, data, categories, size, color, width, height, htmlCode, helper, profile):
    super(Groups, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0],
                                 heightUnit=height[1], code=htmlCode, profile=profile)
    self.add_helper(helper)
    self.color = color if color is not None else self._report.theme.greys[9]
    self.css({'font-size': "%s%s" % (size[0], size[1]) if size is not None else 'inherit',
              'margin': "1px", 'padding': '0 2px'})
    self.builder_name, self._lists__map, self._lists__map_index = False, {}, []
    for i, cat in enumerate(categories):
      self.add_list(data[i], cat)

  def __getitem__(self, i):
    return self.val[i]

  def add_list(self, data, category="", color='inherit', width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, helper=None, options=None, profile=False):
    """

    :param data:
    :param category:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    self._lists__map[category] = len(self.val)
    html_li = List(self._report, data, color, width, height, htmlCode, helper, options, profile)
    html_li.inReport = False
    html_li.css({"margin-bottom": '5px'})
    self.val.append(html_li)
    self._lists__map_index.append(category)
    return self

  def __str__(self):
    self._vals = "".join(['''
      <a onclick='this.nextElementSibling.querySelectorAll("li").forEach(
        function(evt){evt.style.display = evt.style.display === "none" ? "" : "none"})' style='cursor:pointer'>%s</a>%s
      ''' % (self._lists__map_index[i] if len(self._lists__map_index) > i else "Category %s" % i, l.html()) for i, l in enumerate(self.val)])
    self.builder_name = self.__class__.__name__
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.defined), self._vals)


class Badges(List):
  name, category, callFnc = 'List Badges', 'Lists', 'Badges'

  def __init__(self, report, data, color, width, height, htmlCode, helper, options, profile):
    super(Badges, self).__init__(report, data, color, width, height, htmlCode, helper, options, profile)
    for l in self.items:
      l.set_html_content(report.ui.div([
        report.ui.texts.label(l.val['label']).css({"width": 'auto'}),
        report.ui.images.badge(l.val['value'], url=l.val.get('url')).css({"background": 'green', "color": 'white'})
      ])).no_decoration


class Buttons(List):
  name, category, callFnc = 'List Buttons', 'Lists', 'buttons'

  def __init__(self, report, data, color, width, height, htmlCode, helper, options, profile):
    super(Buttons, self).__init__(report, data, color, width, height, htmlCode, helper, options, profile)
    for l in self.items:
      l.set_html_content(
        report.ui.buttons.button(l.val, width=width).css({"text-align": 'center'})).no_decoration


class Checks(List):
  name, category, callFnc = 'List Checked', 'Lists', 'checklist'

  def __init__(self, report, data, color, width, height, htmlCode, helper, options, profile):
    super(Checks, self).__init__(report, data, color, width, height, htmlCode, helper, options, profile)
    for l in self.items:
      c = report.ui.buttons.check(l.val['value'])
      c.click([
        c.input.dom.switchClass("fa-check", "fa-times")])
      l.set_html_content(report.ui.div([
        report.ui.texts.label(l.val['label']).css({"width": 'auto'}).click([
          report.js.alert(report.js.objects.this)]), c])).no_decoration

  @classmethod
  def matchMarkDownBlock(cls, data): return re.match(">>>%s" % cls.callFnc, data[0])

  @staticmethod
  def matchEndBlock(data): return data.endswith("<<<")

  @classmethod
  def convertMarkDownBlock(cls, data, report=None):
    recordSet = []
    for val in data[1:-1]:
      line = val.strip()
      if line.startswith("- [x] "):
        recordSet.append({'value': line[5:], "isChecked": 1})
      else:
        recordSet.append({'value': line[5:], 'disabled': 1})
    if report is not None:
      getattr(report, 'checklist')(recordSet)
    return ["report.checklist(%s)" % json.dumps(recordSet)]

  @classmethod
  def jsMarkDown(cls, vals):
    result = []
    for rec in vals:
      if rec.get('isChecked') == 1:
        result.append("- [X] %s" % rec['value'])
      else:
        result.append("- [ ] %s" % rec['value'])
    return [">>>%s" % cls.callFnc, result, "<<<"]


class ListTournaments(Html.Html):
  name, category, callFnc = 'Brackets', 'Container', 'brackets'
  __reqCss, __reqJs = ['jquery-brackets'], ['jquery-brackets']

  def __init__(self, report, records, width, height, options, profile):
    self.options = {} if options is None else options
    super(ListTournaments, self).__init__(report, {'vals': records, 'save': 'null', 'edit': 'null', 'render': 'null',
                                                   'options': self.options}, width=width[0], widthUnit=width[1],
                                                   height=height[0], heightUnit=height[1], profile=profile)
    self.css({'overflow': 'auto', "padding": "auto", "margin": "auto"})

  def addFnc(self, fncName, jsFncs):
    if isinstance(jsFncs, list):
      jsFncs = ";".join(jsFncs)
    self.vals[fncName] = jsFncs

  def onDocumentLoadFnc(self):
    # , disableToolbar: true, disableTeamEdit: false
    self.addGlobalFnc("%s(htmlObj, data)" % self.__class__.__name__, ''' htmlObj.empty() ;
      parameters = {centerConnectors: true, init: data.vals }; 
      if (data.save != "null"){parameters['save'] = new Function('rec', 'userData', 'var data = {challenge: JSON.stringify(rec), userProno: JSON.stringify(userData) } ;' + data.save) };
      if (data.render != "null"){parameters['decorator'] = {render: new Function('rec', 'userData', data.save), edit: function(container, data, doneCb) { } } };
      if (data.edit != "null"){ 
        if ( data.render == "null" ) { parameters['decorator']['render'] = function(rec, userData) {} } ;
        parameters['decorator']['edit'] = new Function('container', 'data', 'doneCb', data.edit); };
      for (var k in data.options) { parameters[k] = data.options[k] ;};
      htmlObj.bracket( parameters )''', 'Javascript Object builder')

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.defined)
