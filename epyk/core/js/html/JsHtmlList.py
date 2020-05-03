
from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects.JsNodeDom import JsDoms


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
    Check the duplicates in the filter panel

    Attributes:
    ----------
    :param text:
    :param cateory:
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
    if no_duplicte:
      return JsObjects.JsObjects.get(''' 
      if (%(duplicated)s == -1){ chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: %(text)s, disabled: false, fixed: %(fixed)s}, %(options)s)  }
      ''' % {'name': name, 'category': category, 'duplicated': self.is_duplicated(text, category), 'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text, 'options': JsUtils.jsConvertData(self._src._jsStyles, None)})

    return JsObjects.JsObjects.get(''' 
      chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: %(text)s, disabled: false, fixed: %(fixed)s}, %(options)s)
      ''' % {'name': name, 'category': category, 'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text, 'options': JsUtils.jsConvertData(self._src._jsStyles, None)})

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
