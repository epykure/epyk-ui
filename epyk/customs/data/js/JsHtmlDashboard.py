#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.html import JsHtmlNetwork
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsHtmlPivot(JsHtml.JsHtml):

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    if self._src.sub_rows is None:
      return JsObjects.JsObjects.get(
        "{rows: %s, columns: %s}" % (self._src.rows.dom.content, self._src.columns.dom.content))
    return JsObjects.JsObjects.get(
      "{rows: %s, columns: %s, sub_rows: %s}" % (
        self._src.rows.dom.content,
        self._src.columns.dom.content,
        self._src.sub_rows.dom.content))

  def clear(self, profile=None):
    """
    Description:
    ------------
    Clear all the items in the list.

    Usage:
    -----


    Attributes:
    ----------
    :param profile: Boolean. Optional. Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if self._src.sub_rows is not None:
      return JsUtils.jsConvertFncs([
        self._src.sub_rows.dom.clear(), self._src.rows.dom.clear(),
        self._src.columns.dom.clear()], toStr=True, profile=profile)

    return JsUtils.jsConvertFncs([
      self._src.rows.dom.clear(), self._src.columns.dom.clear()], toStr=True, profile=profile)


class JsHtmlColumns(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get('''
      (function(){
         var values = []; %(component)s.querySelectorAll("li").forEach(function(dom){values.push(dom.innerText)});
         return values
      })()''' % {"component": self._src.dom.varName})

  @property
  def classList(self):
    """
    Description:
    ------------
    Return the class name of the list item.
    """
    return self._src.dom.getAttribute("class")

  def add(self, item, unique=True, draggable=True):
    """
    Description:
    ------------
    Add a new item to the list.

    Usage:
    -----

    Attributes:
    ----------
    :param item: String. The Item to be added to the list.
    :param unique: Boolean. Optional. Only add the item if it is not already in the list.
    :param draggable: Boolean. Optional. Set the new entry as draggable.
    """
    if hasattr(item, 'dom'):
      item = item.dom.content
    item = JsUtils.jsConvertData(item, None)
    unique = JsUtils.jsConvertData(unique, None)
    draggable = JsUtils.jsConvertData(draggable, None)
    options = JsUtils.jsConvertData(self._src.options, None)
    return JsObjects.JsVoid('''
      var listItems = %(item)s; 
      if(!Array.isArray(listItems)){listItems = [listItems]};
      var listItemOptions = %(options)s; 
      listItems.forEach(function(item){
        var li = document.createElement("li");
        if(%(unique)s){
          var hasItems = false;
          %(component)s.querySelectorAll("li").forEach(function(dom){
            if (dom.innerText == item){hasItems = true}})
          if(!hasItems){
            var text = document.createElement("div"); text.innerText = item;
            text.style.display = 'inline-block';
            text.style['margin-right'] = '10px';
            text.addEventListener("click", function(event){
              
              if (document.selection) {
                var range = document.body.createTextRange();
                range.moveToElementText(event.srcElement);
                range.select().createTextRange();
                document.execCommand("copy");
              } else if (window.getSelection) { 
                var x = document.createElement("input");
                x.setAttribute("type", "text");
                x.setAttribute("value", event.srcElement.innerText);
                document.body.appendChild(x); var initColor = event.srcElement.style.color; 
                event.srcElement.style.color = 'green';
                x.select(); setTimeout(function(){ event.srcElement.style.color = initColor}, 1000)
                document.execCommand("copy"); x.remove();
              }
            });
            if (%(draggable)s){
              text.setAttribute('draggable', true);
              text.addEventListener('dragstart', function(event){
                event.dataTransfer.setData("text", event.target.innerHTML)})
            }
            var div = document.createElement("div"); div.appendChild(text);
            var span = document.createElement("span"); span.innerHTML = '&#10006';  div.appendChild(span);
            span.addEventListener("click", function(){
              if(typeof listItemOptions.source !== 'undefined'){
                var column = li.firstChild.firstChild.innerText;
                window[listItemOptions.source].forEach(function(rec){
                  delete rec[column]
                })
              }
              li.remove()});
            span.style.display = 'inline-block';
            
            li.appendChild(div); li.style.cursor = "pointer"; li.style['text-align'] = "left";
            %(component)s.appendChild(li)}
        }else{
          var text = document.createElement("div"); text.innerText = item;
          if (%(draggable)s){
            text.setAttribute('draggable', true);
            text.addEventListener('dragstart', function(event){event.dataTransfer.setData("text", event.target.innerHTML)} )
          }
          var div = document.createElement("div"); div.appendChild(text);
          li.appendChild(div); li.style.cursor = "pointer"; li.style['text-align'] = "left";
          %(component)s.appendChild(li)
        }
      })''' % {"item": item, "component": self._src.dom.varName, 'unique': unique, 'draggable': draggable, "options": options})

  def clear(self):
    """
    Description:
    ------------
    Clear all the items in the list.
    """
    return JsObjects.JsVoid("%s.innerHTML = ''" % self._src.dom.varName)

  def loading(self, label="Processing data"):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param label: String. Optional. The processing message.
    """
    return JsObjects.JsVoid("%s.innerHTML = '<i style=\"margin-right:5px\" class=\"fas fa-spinner fa-spin\"></i>%s'" % (self._src.dom.varName, label))


class JsHtmlTask(JsHtmlNetwork.JsHtmlDropFiles):

  def store(self, delimiter=None, format=None):
    """
    Description:
    ------------
    Not available for a task object as the data will be directly returned and there is not need to
    perform some string transformation before loading.

    Usage:
    -----

    Attributes:
    ----------
    :param delimiter:
    :param format:
    """
    raise Exception("Not available use load instead")

  def load(self, jsData):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param jsData:
    """
    return JsObjects.JsVoid('''window['%s_data'] = %s; %s
      ''' % (self._src.htmlCode, JsUtils.jsConvertData(jsData, None),
             self._src.text.dom.setAttribute("title", self.content.length.toString().add(" rows")).r))
