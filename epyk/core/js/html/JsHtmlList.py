#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom
from epyk.core.js import JsUtils
from epyk.core.css import Defaults

from epyk.core.js.primitives import JsObjects


class JsItemsDef(object):

  def _item(self, item_def):
    return '''%(item_def)s; htmlObj.appendChild(item)
      ''' % {'item_def': item_def}

  def text(self, report):
    """
    Description:
    ------------
    Add text items to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      item.onclick = function(event){ var value = this.innerHTML; options.click(event, value) }  };
    if(options.draggable != false){ 
      item.setAttribute('draggable', true);
      item.style.cursor = 'grab';
      item.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value) }
    };
    if(typeof data === 'object'){ item.innerHTML = data.text} else { item.innerHTML = data }'''
    return self._item(item_def)

  def icon(self, report):
    """
    Description:
    ------------
    Add icon items to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    report.jsImports.add('font-awesome')
    report.cssImport.add('font-awesome')
    item_def = '''
    var item = document.createElement("DIV"); var icon = document.createElement("I"); 
    if(typeof data.icon !== 'undefined') {data.icon.split(" ").forEach(function(s){icon.classList.add(s)})}
    else {options.icon.split(" ").forEach(function(s){icon.classList.add(s)}) }
    icon.style.marginRight = '5px'; var span = document.createElement("span");  
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', true); 
    if(typeof data === 'object'){ span.innerHTML = data.text} else { span.innerHTML = data };
    if(options.click != null){ item.style.cursor = 'pointer';
      item.onclick = function(event){ var value = span.innerHTML; options.click(event, value) }  };
    item.appendChild(icon); item.appendChild(span)'''
    return self._item(item_def)

  def check(self, report):
    """
    Description:
    ------------
    Add check components to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.padding = 0; item.style.whiteSpace = "nowrap";  item.style.display = "block";
    
    var span = document.createElement("span");  
    var input = document.createElement("input");    
    input.setAttribute('type', 'checkbox');
    input.setAttribute('name', 'input_box');
    input.style.verticalAlign = "middle";
    input.onchange = function(event){ event.stopPropagation(); event.cancelBubble = true; span.setAttribute('data-valid', this.checked ); 
      var value = span.innerHTML; if(options.click != null){options.click(event, value)} };
    
    var span = document.createElement("span"); span.style.marginLeft = '5px'; 
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', false); 
    
    if(typeof data === 'object'){ span.innerHTML = data.text} else { span.innerHTML = data };
    if(options.checked){ input.setAttribute('checked', options.checked); span.setAttribute('data-valid', options.checked) };
    if(data.checked){ input.setAttribute('checked', data.checked); span.setAttribute('data-valid', data.checked) };
    
    span.style.verticalAlign = "middle";
    item.appendChild(input); item.appendChild(span);
    '''
    return self._item(item_def)

  def radio(self, report):
    """
    Description:
    ------------
    Add radio components to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.padding = 0; item.style.whiteSpace = "nowrap";  item.style.display = "block";
    
    var span = document.createElement("span");  
    var input = document.createElement("input");    
    input.setAttribute('type', 'radio'); input.setAttribute('name', options.group);
    input.style.verticalAlign = "middle";
    input.onchange = function(event){ 
      this.parentNode.parentNode.parentNode.querySelectorAll('[name=value]').forEach(function(node){
        node.setAttribute('data-valid', false); }); var value = span.innerHTML; 
        span.setAttribute('data-valid', this.checked ); if(options.click != null){options.click(event, value)} };
    
    var span = document.createElement("span");  
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', false);
    if(typeof data === 'object'){ span.innerHTML = data.text} else { span.innerHTML = data };
    span.style.verticalAlign = "middle";
    
    item.appendChild(input); item.appendChild(span);
    '''
    return self._item(item_def)

  def badge(self, report):
    """
    Description:
    ------------
    Add text object with badges to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    var span = document.createElement("span"); span.setAttribute('name', 'value'); span.innerHTML = data.text;  
    var badge = document.createElement("span"); badge.innerHTML = data.value;
    badge.style.backgroundColor = 'red'; badge.style.color = 'white'; badge.style.borderRadius = '50%%'; badge.style.padding = '0 3px';
    badge.style.marginLeft = '5px'; badge.style.fontSize = '%s'; 
    for(const attr in options.badge){badge.style[attr] = options.badge[attr]};
    item.appendChild(span); item.appendChild(badge)''' % Defaults.font(-2)
    return self._item(item_def)

  def link(self, report):
    """
    Description:
    ------------
    Add links items to the list

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("a");  
    item.setAttribute('name', 'value'); item.setAttribute('data-valid', false);
    item.innerHTML = data ; item.href ='#' '''
    return self._item(item_def)

  def box(self, report):
    """
    Description:
    ------------
    This will represent a title with a text and a list of icons

    Attributes:
    ----------
    :param report: Page object. The internal page object
    """
    report.jsImports.add('font-awesome')
    report.cssImport.add('font-awesome')
    item_def = '''
    var item = document.createElement("DIV"); 
    item.style.borderRadius = "5px";
    item.style.padding = "2px";
    
    item.setAttribute('data-valid', true);
    var title = document.createElement("DIV"); 
    title.setAttribute('name', 'value');
    if (typeof data.color !== 'undefined'){
      item.style.border = "1px solid " + data.color;
      title.style.color = data.color;
    }
    title.style.fontWeight = 'bold';
    title.innerHTML = data.title;
    var text = document.createElement("DIV"); 
    text.innerHTML = data.text;
    
    item.appendChild(title); item.appendChild(text);
    var icons = document.createElement("DIV"); 
    icons.style.textAlign = 'right';
    if(typeof data.icons !== 'undefined') {
      data.icons.forEach(function(rec){
          var icon_dom = document.createElement("I"); 
          icon_dom.style.marginRight = '5px';
          rec.icon.split(" ").forEach(function(s){icon_dom.classList.add(s)}); 
          if(typeof rec.color !== 'undefined'){ icon_dom.style.color = rec.color}
          if(typeof rec.tooltip !== 'undefined'){ icon_dom.setAttribute('title', rec.tooltip)}
          if(rec.click != null){ icon_dom.style.cursor = 'pointer';
            icon_dom.onclick = function(event){ var value = data.title; eval(rec.click)}};
          icons.appendChild(icon_dom)
      })
    }
    item.appendChild(icons);
    '''
    return self._item(item_def)

  def custom(self, item_def):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param item_def:
    """
    return self._item(item_def)


class JsItem(JsHtml.JsHtmlRich):

  @property
  def content(self):
    return JsHtml.ContentFormatters(self._report, '''
      (function(dom){var values = []; dom.childNodes.forEach( function(dom, k){  
          const item = dom.querySelector('[name=value]');
          if (item != null){
            const valid = item.getAttribute("data-valid");
            if (valid === 'true'){values.push(dom.querySelector('[name=value]').innerHTML)}
          }
      }); return values })(%s)''' % self.varName)

  @property
  def selected(self):
    """
    Description:
    ------------
    Return a list with all the selected values
    """
    return self.content

  @property
  def unselected(self):
    """
    Description:
    ------------
    Return a list with all the unselected values
    """
    return JsHtml.ContentFormatters(self._report, '''
        (function(dom){var values = []; dom.childNodes.forEach( function(dom, k){   
          const item = dom.querySelector('[name=value]');
          if (item != null){
            const valid = item.getAttribute("data-valid");
            if (valid === 'false'){values.push(dom.querySelector('[name=value]').innerHTML)}
          }
        }); return values })(%s)''' % self.varName)

  @property
  def first(self):
    """
    Description:
    ------------
    Get the first value in the list
    """
    return JsObjects.JsVoid("%s.firstChild.querySelector('[name=value]').innerHTML" % self.varName)

  @property
  def last(self):
    """
    Description:
    ------------
    Get the last value in the list
    """
    return JsObjects.JsVoid("%s.lastChild.querySelector('[name=value]').innerHTML" % self.varName)

  @property
  def current(self):
    """
    Description:
    ------------
    Get the current value from a LI item event
    """
    return JsObjects.JsVoid("this.querySelector('[name=value]').innerHTML")

  @property
  def values(self):
    """
    Description:
    ------------
    Get all the values in the list
    """
    return JsObjects.JsArray.JsArray.get("")

  def getItemByValue(self, value):
    """
    Description:
    ------------
    Get an item from the list based on its value

    Attributes:
    ----------
    :param value: String. The value to find in the list
    """
    value = JsUtils.jsConvertData(value, None)
    return JsNodeDom.JsDoms.get('''
      (function(dom, value){var children = dom.childNodes; var values = null;
        for (var i = 0; i < children.length; i++) { if(children[i].querySelector('[name=value]').innerHTML == value){ values = children[i]; break} };
        return values })(%s, %s)''' % (self.varName, value))

  def selectAll(self, with_input_box=False):
    """
    Description:
    ------------
    Select all the items in the list

    Attributes:
    ----------
    :param with_input_box: Boolean. If the items have a dedicated input box for the check
    """
    if self._src._jsStyles['items_type'] == "radio":
      raise Exception("It is not possible to select all radios from a same group, use check instead")

    if self._src._jsStyles['items_type'] == "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach( function(dom, k){  
          const item = dom.querySelector('[name=input_box]');
          if (item != null){ 
            item.checked = true;
            dom.querySelector('[name=value]').setAttribute("data-valid", true);
        }})''' % self.varName)

    return JsObjects.JsVoid('''
      %s.childNodes.forEach( function(dom, k){  
        dom.querySelector('[name=value]').setAttribute("data-valid", true);
      })''' % self.varName)

  def unSelectAll(self, with_input_box=False):
    """
    Description:
    ------------
    UnSelect all the items in the list

    Attributes:
    ----------
    :param with_input_box: Boolean. If the items have a dedicated input box for the check
    """
    if self._src._jsStyles['items_type'] == "radio":
      raise Exception("It is not possible to select all radios from a same group, use check instead")

    if self._src._jsStyles['items_type'] == "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach( function(dom, k){  
          const item = dom.querySelector('[name=input_box]');
          if (item != null){ 
            dom.querySelector('[name=input_box]').checked = false;
            dom.querySelector('[name=value]').setAttribute("data-valid", false);
        }})''' % self.varName)

    return JsObjects.JsVoid('''
      %s.childNodes.forEach( function(dom, k){  
        dom.querySelector('[name=value]').setAttribute("data-valid", false);
      })''' % self.varName)

  def add(self, value, css_attrs=None, css_cls=None):
    """
    Description:
    ------------
    Add items to the list

    Attributes:
    ----------
    :param value: String | Dictionary.
    :param css_attrs: Dictionary. All the CSS attributes to be added to the LI component
    :param css_cls: String. The CSS class to be added to the LI component
    """
    if isinstance(value, dict):
      js_values = []
      for k, v in value.items():
        js_values.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
      value = "{%s}" % ",".join(js_values)
    else:
      if hasattr(value, 'dom'):
        value = value.dom.content
      value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid('''
      var item = %(value)s; var itemOptions = %(options)s;
      if(itemOptions.showdown){var converter = new showdown.Converter({}); converter.setOption("display", "inline-block");
          item = converter.makeHtml(%(value)s).replace("<p>", "<p style='display:inline-block;margin:0'>")};
      var li = document.createElement("LI"); %(shape)s(li, item, %(options)s); li.style.margin = "5px 0"; %(comp)s.appendChild(li)
      if(itemOptions.delete){
        var close = document.createElement("i");
        close.classList.add("fas"); 
        close.classList.add(itemOptions.delete_icon);
        close.style.cursor = 'pointer';
        close.onclick = function(event){this.parentNode.remove()};
        for (const [key, value] of Object.entries(itemOptions.delete_position)) {
            close.style[key] = value}
        li.lastChild.style.display = 'inline-block'; li.appendChild(close);
        const cls = %(cls)s;
        if (cls != null){li.classList.add(cls)}
      } ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'value': value,
             'cls': JsUtils.jsConvertData(css_cls, None), 'shape': "%s%s" % (self._src._prefix, self._src._jsStyles['items_type'])})

  def tags(self, values, css_attrs=None, css_cls=None):
    """
    Description:
    ------------
    Add tags to an item in the list

    Attributes:
    ----------
    :param values: List. The tags to be added to the current item
    :param css_attrs: Dictionary. All the CSS attributes to be added to the LI component
    :param css_cls: String. The CSS class to be added to the LI component
    """
    return JsObjects.JsVoid('''
      var enumTags = %(values)s;
      if(enumTags != ''){
        if(typeof enumTags === 'string'){ enumTags = [enumTags]};
        enumTags.forEach(function(val){
          var item = document.createElement("DIV"); item.innerHTML = val;
          item.style.display = "inline-block";
          item.style.padding = "1px 2px";
          item.style.margin = "0 1px";
          item.style.color = "black";
          item.style.fontSize = "8px";
          item.style.background = "white";
          item.style.border = "1px solid white";
          item.style.borderRadius = "5px";
          const css = %(css)s;
          if (css != null){
            for (const [key, value] of Object.entries(css)) {
              item.style[key] = value
            }
          }
          const cls = %(cls)s;
          if(cls != null){item.classList.add(cls)}
          %(comp)s.appendChild(item)
      })}''' % {'comp': self.varName, 'css': JsUtils.jsConvertData(css_attrs, None),
                'cls': JsUtils.jsConvertData(css_cls, None), 'values': JsUtils.jsConvertData(values, None)})

  def contextMenu(self, menu, jsFncs=None, profile=False):
    """
    Description:
    ------------
    Add a context menu to an item in the list.

    Attributes:
    ----------
    :param menu:
    :param jsFncs: List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    if not hasattr(menu, 'source'):
      menu = self._src._report.ui.menus.contextual(menu)
    menu.source = self
    new_js_fncs = (jsFncs or []) + [self._report.js.objects.mouseEvent.stopPropagation(),
          menu.dom.css(
            {"display": 'block', 'left': self._report.js.objects.mouseEvent.clientX + "'px'",
             'top': self._report.js.objects.mouseEvent.clientY + "'px'"}),
          self._report.js.objects.mouseEvent.preventDefault()]
    return JsObjects.JsVoid('''
      %s.lastChild.addEventListener("contextmenu", function(event){%s});
      ''' % (self.varName, JsUtils.jsConvertFncs(new_js_fncs, toStr=True)))

  def clear(self):
    """
    Description:
    ------------
    Clear all the items in the list
    """
    return JsObjects.JsVoid("while(%(comp)s.firstChild){%(comp)s.removeChild(%(comp)s.firstChild)}" % {'comp': self.varName})


class Tags(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    -----------
    Returns the list of data available on the filters panel
    """
    return JsHtml.ContentFormatters(self._report, '''
      (function(dom){var content = {}; 
        dom.childNodes.forEach(function(rec){
          var label = rec.getAttribute('data-category');
          if(!(label in content)){ content[label] = [] }; 
          content[label].push(rec.querySelector('span[name=chip_value]').textContent);
        }); 
        return content})(%s)
      ''' % self.querySelector("div[name=panel]"))

  def is_duplicated(self, text, category=None):
    """
    Description:
    ------------
    Check the duplicates in the filter panel for a given category

    Attributes:
    ----------
    :param text: String. The item text
    :param category: String. The item category
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsObjects.get(''' 
      (function(dom){var index = -1; var children = dom.childNodes; var count = 0;
        for(child in children){if((typeof children[child] === 'object') && children[child].querySelector('span[name=chip_value]').textContent == %s){
            if(children[child].getAttribute('data-category') == %s){ index = count; break; }
        }; count++; }; return index})(%s)''' % (text, category, self.querySelector("div[name=panel]")))

  def values(self, category=None):
    if category is None:
      return JsObjects.JsObjects.get("(function(dom){var content = []; dom.childNodes.forEach(function(rec){content.push(rec.querySelector('span[name=chip_value]').textContent)}); return content})(%s)" % self.querySelector("div[name=panel]"))

    category = JsUtils.jsConvertData(category, None)
    return JsObjects.JsObjects.get(''' 
          (function(dom){var children = dom.childNodes; var values = [];
            for(child in children){if(typeof children[child] === 'object'){
                if(children[child].getAttribute('data-category') == %s){ values.push(children[child].querySelector('span[name=chip_value]').textContent); }
            }}; return values})(%s)''' % (category, self.querySelector("div[name=panel]")))

  def hide(self):
    """
    Description:
    ------------
    Hide the filters panel
    """
    return self.querySelector("div[name=panel]").show()

  def show(self):
    """
    Description:
    ------------
    Show the filters panel
    """
    return self.querySelector("div[name=panel]").show()

  def toggle(self):
    """
    Description:
    ------------
    Toggle the display of the filters panel
    """
    return self.querySelector("div[name=panel]").toggle()

  def add(self, text, category=None, name=None, fixed=False, no_duplicte=True):
    """
    Description:
    ------------
    Add item on the filters panel

    Attributes:
    ----------
    :param text: String. The value to be added on the filter panel
    """
    text = JsUtils.jsConvertData(text, None)
    fixed = JsUtils.jsConvertData(fixed, None)
    if category is None:
      category = name or self._src._jsStyles['category']
    name = name or category
    category = JsUtils.jsConvertData(category, None)
    name = JsUtils.jsConvertData(name, None)
    # Convert the option to a javascript object
    # TODO move this in a centralised place
    options, js_options = self._src._jsStyles, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("'%s': {%s}" % (k, ", ".join(row)))
      else:
        if str(v).strip().startswith("function"):
          js_options.append("%s: %s" % (k, v))
        else:
          js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))

    if no_duplicte:
      return JsObjects.JsObjects.get(''' 
      if ((%(duplicated)s == -1) && (%(text)s != '')){ chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: %(text)s, disabled: false, fixed: %(fixed)s}, {%(options)s})  }
      ''' % {'name': name, 'category': category, 'duplicated': self.is_duplicated(text, category), 'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text, 'options': ",".join(js_options)})

    return JsObjects.JsObjects.get(''' 
      chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: %(text)s, disabled: false, fixed: %(fixed)s}, {%(options)s})
      ''' % {'name': name, 'category': category, 'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text, 'options': ",".join(js_options)})

  @property
  def input(self):
    """
    Description:
    ------------
    Clear the content of the fitlers panel
    """
    return JsObjects.JsObjects.get("%s.value" % self.querySelector("input"))

  def clear(self):
    """
    Description:
    ------------
    Clear the content of the fitlers panel
    """
    return self.querySelector("div[name=panel]").empty()

  def remove(self, text, category=None):
    """
    Description:
    ------------
    Remove an item from the filters panel

    Attributes:
    ----------
    :param text: String. The test of the items to be removed
    :param category: String. The test of the items to be removed
    """
    if category is None:
      category = self._src._jsStyles['category']
    category = JsUtils.jsConvertData(category, None)
    return JsObjects.JsObjects.get('''var itemPos = %(duplicated)s; if (itemPos >= 0){ %(panel)s.childNodes[itemPos].remove()}
      ''' % {'duplicated': self.is_duplicated(text, category), 'panel': self.querySelector("div[name=panel]")})
