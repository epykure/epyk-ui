
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

    :param report:
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      item.onclick = function(event){ var value = this.innerHTML; options.click(event, value) }  };
    if(typeof data === 'object'){ item.innerHTML = data.text} else { item.innerHTML = data }'''
    return self._item(item_def)

  def icon(self, report):
    """
    Description:
    ------------
    Set an list of icons

    Attributes:
    ----------
    :param report:
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

    Attributes:
    ----------
    :param report:
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

    Attributes:
    ----------
    :param report:
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

    Attributes:
    ----------
    :param report:
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

    Attributes:
    ----------
    :param report:
    """
    item_def = '''
    var item = document.createElement("a");  
    item.setAttribute('name', 'value'); item.setAttribute('data-valid', false);
    item.innerHTML = data ; item.href ='#' '''
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
          const valid = dom.querySelector('[name=value]').getAttribute("data-valid");
          if (valid === 'true'){values.push(dom.querySelector('[name=value]').innerHTML)}
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
            const valid = dom.querySelector('[name=value]').getAttribute("data-valid");
            if (valid === 'false'){values.push(dom.querySelector('[name=value]').innerHTML)}
        }); return values })(%s)''' % self.varName)

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
    :param with_input_box:
    """
    if self._src._jsStyles['items_type'] == "radio":
      raise Exception("It is not possible to select all radios from a same group, use check instead")

    if self._src._jsStyles['items_type'] == "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach( function(dom, k){  
          dom.querySelector('[name=input_box]').checked = true;
          dom.querySelector('[name=value]').setAttribute("data-valid", true);
        })''' % self.varName)

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
    :param with_input_box:
    """
    if self._src._jsStyles['items_type'] == "radio":
      raise Exception("It is not possible to select all radios from a same group, use check instead")

    if self._src._jsStyles['items_type'] == "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach( function(dom, k){  
          dom.querySelector('[name=input_box]').checked = false;
          dom.querySelector('[name=value]').setAttribute("data-valid", false);
        })''' % self.varName)

    return JsObjects.JsVoid('''
      %s.childNodes.forEach( function(dom, k){  
        dom.querySelector('[name=value]').setAttribute("data-valid", false);
      })''' % self.varName)

  def add(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value: String | Dictionary.
    """
    if isinstance(value, dict):
      js_values = []
      for k, v in value.items():
        js_values.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
      value = "{%s}" % ",".join(js_values)
    else:
      value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid('''
      var li = document.createElement("LI"); %(shape)s(li, %(value)s, %(options)s); li.style.margin = "5px 0"; %(comp)s.appendChild(li)
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'value': value, 'shape': "%s%s" % (self._src._prefix, self._src._jsStyles['items_type'])})


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
