#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
List of all the different templates configurations available for displaying bespoke lists.
This list can be extended and it is easy to test a new configuration by different defining the HTML template in the common list object.
List are standard and very popular HTML objects, please have a look at the below websites if you need further information to manipulate them in your report

"""

from epyk.core.js import Imports
from epyk.core.js import JsUtils
from epyk.core.html import Html
from epyk.core.html.options import OptList

# The list of Javascript classes
from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlList


class Li(Html.Html):
  name = 'Entries'

  def __init__(self, report, text):
    super(Li, self).__init__(report, text)
    self.css({'font-size': 'inherit', 'margin': "1px 5px", 'padding': 0})

  def __add__(self, htmlObj):
    """ Add items to a container """
    if not hasattr(htmlObj, 'options'):
      raise Exception("This can only be used for HTML components")

    self.set_html_content(htmlObj)
    return self

  @property
  def no_decoration(self):
    """
    Description:
    ------------
    Property to remove the list default style
    """
    self.css({"text-decoration": "none", "list-style-type": 'none'})
    return self

  def add_label(self, text, css=None, position="before", for_=None):
    """
    Description:
    ------------
    Add an elementary label component

    Usage::


    Related Pages:

      https://www.w3schools.com/tags/tag_label.asp

    Attributes:
    ----------
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
    Description:
    ------------
    Set the cell content to be an HTML object

    Attributes:
    ----------
    :param htmlObj: Python HTML object

    :return: self, the cell object to allow the chaining
    """
    htmlObj.options.managed = False
    if self.innerPyHTML is not None:
      if not isinstance(self.innerPyHTML, list):
        self.innerPyHTML = [self.innerPyHTML]
      self.innerPyHTML.append(htmlObj)
    else:
      self.innerPyHTML = htmlObj
    return self

  def click(self, jsFncs, profile=False, source_event=None):
    if self.innerPyHTML is not None:
      return self.innerPyHTML.click(jsFncs, profile)

    return super(Li, self).click(jsFncs, profile, source_event)

  def __str__(self):
    return "<li %s>%s</li>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.content)


class List(Html.Html):
  name = 'List'

  def __init__(self, report, data, color, width, height, htmlCode, helper, options, profile):
    super(List, self).__init__(report, [], css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
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
    Description:
    ------------

    :rtype: OptList.OptionsLi
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtml.JsHtmlList
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlList(self, report=self._report)
    return self._dom

  def __add__(self, htmlObj):
    """ Add items to a container """
    if not isinstance(htmlObj, Li):
      raise Exception("This can only be used for Li")

    self.items = self.items or []
    htmlObj.options.managed = False
    self.items.append(htmlObj)
    return self

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i:

    :rtype: Li
    """
    return self.items[i] if self.items is not None else None

  def add_item(self, d):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param d:
    """
    self.items = self.items or []
    li_obj = Li(self._report, d)
    if hasattr(d, 'options'):
      d.options.managed = False
    li_obj.options.managed = False
    self.items.append(li_obj)
    return self

  def set_items(self):
    """
    Description:
    ------------

    """
    self.items = self.items or []
    for d in self.val:
      li_obj = Li(self._report, d)
      li_obj.options.managed = False
      li_obj.css(self.options.li_css)
      if self.options.li_class:
        li_obj.attr["class"].add(self.options.li_class)
      self.items.append(li_obj)
    return self

  def on_items(self, event, jsFncs, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param event:
    :param jsFncs:
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    for i in self.items:
      i.on(event, jsFncs, profile)
    return self

  def click_items(self, jsFncs, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    for i, item in enumerate(self.items):
      fnc = JsUtils.jsConvertFncs([
        self._report.js.getElementsByName("divs_%s" % self.htmlCode).all(self._report.js.objects.dom("elt").hide().r),
        self._report.js.getElementsByName("divs_%s" % self.htmlCode)[i].toggle().r])
      item.click(fnc + jsFncs, profile)
    return self

  def __str__(self):
    self._vals = "".join([i.html() for i in self.items]) if self.items is not None else ""
    #self.builder_name = self.__class__.__name__
    #self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<ul %s>%s</ul>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self._vals)


class Groups(Html.Html):
  name = 'Groups'

  def __init__(self, report, data, categories, size, color, width, height, htmlCode, helper, profile):
    super(Groups, self).__init__(report, [], css_attrs={"width": width, "height": height}, htmlCode=htmlCode, profile=profile)
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
    Description:
    ------------

    Attributes:
    ----------
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
    html_li.options.managed = False
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
    return "<div %s>%s</div>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self._vals)


class Items(Html.Html):
  name = 'List'

  def __init__(self, report, type, records, width, height, options, htmlCode, profile, helper):
    super(Items, self).__init__(report, records, css_attrs={"width": width, 'height': height})
    self.__options = OptList.OptionsItems(self, options)
    self._prefix, self._jsStyles['items_type'] = "ListDyn_", type
    self._jsStyles['click'], self._jsStyles['draggable'] = None, False

  @property
  def _js__builder__(self):
    return ''' htmlObj.innerHTML = "";
      data.forEach(function(item, i){
        if(options.showdown){var converter = new showdown.Converter(options.showdown); converter.setOption("display", "inline-block");
          var item = converter.makeHtml(item).replace("<p>", "<p style='display:inline-block;margin:0'>")};
        var li = document.createElement("li");
        if(typeof item.type === 'undefined'){window['%(alias)s'+ options.items_type](li, item, options)}
        else{window['%(alias)s' + item.type](li, item, options)};
        
        if(options.delete){
          var close = document.createElement("i");
          close.classList.add("fas"); close.classList.add(options.delete_icon);
          close.style.marginLeft = '10px'; close.style.cursor = 'pointer';
          close.onclick = function(event){this.parentNode.remove()};
          for (const [key, value] of Object.entries(options.delete_position)) {
            close.style[key] = value}
          li.lastChild.style.display = 'inline-block';
          li.appendChild(close);
        }
        li.style.margin = "5px 0";
        htmlObj.appendChild(li)})''' % {"alias": self._prefix}

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptList.OptionsItems
    """
    return self.__options

  @property
  def dom(self):
    """
    Description:
    ------------

    :rtype: JsHtmlList.JsItem
    """
    if self._dom is None:
      self._dom = JsHtmlList.JsItem(self, report=self._report)
    return self._dom

  def click(self, jsFncs, profile=False, source_event=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    :param source_event:
    """
    if not isinstance(jsFncs, list):
      jsFncs = []
    self._jsStyles['click'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def draggable(self, jsFncs=None, options=None, profile=False, source_event=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param options:
    :param profile:
    :param source_event:
    """
    jsFncs = jsFncs or []
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs.append('event.dataTransfer.setData("text", value)')
    self._jsStyles['draggable'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def add_type(self, type, item_def, dependencies=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param type: String.
    :param item_def: String.
    :param dependencies: List. Optional. The external module dependencies
    """
    if dependencies is not None:
      for d in dependencies:
        if d in Imports.JS_IMPORTS:
          self._report.jsImports.add(d)
        if d in Imports.CSS_IMPORTS:
          self._report.cssImport.add(d)
    self.style.css.padding_left = 0
    self.css({"list-style": 'none'})
    self._jsStyles['items_type'] = type
    item_type_name = "%s%s" % (self._prefix, self._jsStyles['items_type'])
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[item_type_name] = "function %s(htmlObj, data, options){%s}" % (item_type_name, JsHtmlList.JsItemsDef().custom(item_def))
    return self

  def __str__(self):
    item_type_name = "%s%s" % (self._prefix, self._jsStyles['items_type'])
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    if not item_type_name in constructors:
      # add all the shape definitions
      shapes = JsHtmlList.JsItemsDef()
      constructors[item_type_name] = "function %s(htmlObj, data, options){%s}" % (item_type_name, getattr(shapes, self._jsStyles['items_type'])(self._report))
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<ul %s></ul>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ListTournaments(Html.Html):
  name = 'Brackets'
  requirements = ('jquery-brackets', )

  def __init__(self, report, records, width, height, options, profile):
    self.options = options
    super(ListTournaments, self).__init__(report, {'vals': records, 'save': 'null', 'edit': 'null', 'render': 'null', 'options': self.options},
                                          css_attrs={"width": width, "height": height}, profile=profile)
    self.css({'overflow': 'auto', "padding": "auto", "margin": "auto"})

  def addFnc(self, fncName, jsFncs):
    if isinstance(jsFncs, list):
      jsFncs = ";".join(jsFncs)
    self.vals[fncName] = jsFncs

  @property
  def _js__builder__(self):
    return '''
      htmlObj.empty(); parameters = {centerConnectors: true, init: data.vals }; 
      if (data.save != "null"){parameters['save'] = new Function('rec', 'userData', 'var data = {challenge: JSON.stringify(rec), userProno: JSON.stringify(userData) } ;' + data.save) };
      if (data.render != "null"){parameters['decorator'] = {render: new Function('rec', 'userData', data.save), edit: function(container, data, doneCb) { } } };
      if (data.edit != "null"){ 
        if (data.render == "null") { parameters['decorator']['render'] = function(rec, userData) {} } ;
        parameters['decorator']['edit'] = new Function('container', 'data', 'doneCb', data.edit); };
      for (var k in data.options) { parameters[k] = data.options[k] ;};
      htmlObj.bracket( parameters )
      '''

  def __str__(self):
    return "<div %s></div>" % self.get_attrs(pyClassNames=self.style.get_classes())
