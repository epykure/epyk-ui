#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
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
    if self.component.sub_rows is None:
      return JsObjects.JsObjects.get(
        "{rows: %s, columns: %s}" % (self.component.rows.dom.content, self.component.columns.dom.content))
    return JsObjects.JsObjects.get(
      "{rows: %s, columns: %s, sub_rows: %s}" % (
        self.component.rows.dom.content,
        self.component.columns.dom.content,
        self.component.sub_rows.dom.content))

  def clear(self, profile: Union[bool, dict] = None):
    """
    Description:
    ------------
    Clear all the items in the list.

    Usage:
    -----


    Attributes:
    ----------
    :param Union[bool, dict] profile: Optional. A flag to set the component performance storage.
    """
    if self.component.sub_rows is not None:
      return JsUtils.jsConvertFncs([
        self.component.sub_rows.dom.clear(), self.component.rows.dom.clear(),
        self.component.columns.dom.clear()], toStr=True, profile=profile)

    return JsUtils.jsConvertFncs([
      self.component.rows.dom.clear(), self.component.columns.dom.clear()], toStr=True, profile=profile)


class JsHtmlColumns(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).
    """
    return JsObjects.JsObjects.get('''{%s: {value: %s.querySelector('[data-select=true]').innerHTML, 
timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}''' % (self.htmlCode, self.varName))

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
})()''' % {"component": self.component.dom.varName})

  @property
  def classList(self):
    """
    Description:
    ------------
    Return the class name of the list item.
    """
    return self.component.dom.getAttribute("class")

  def add(self, item, unique: bool = True, draggable: bool = True):
    """
    Description:
    ------------
    Add a new item to the list.

    Usage:
    -----

    Attributes:
    ----------
    :param item: String. The Item to be added to the list.
    :param bool unique: Optional. Only add the item if it is not already in the list.
    :param bool draggable: Optional. Set the new entry as draggable.
    """
    if hasattr(item, 'dom'):
      item = item.dom.content
    item = JsUtils.jsConvertData(item, None)
    unique = JsUtils.jsConvertData(unique, None)
    draggable = JsUtils.jsConvertData(draggable, None)
    options = JsUtils.jsConvertData(self.component.options, None)
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
      })''' % {"item": item, "component": self.component.dom.varName, 'unique': unique, 'draggable': draggable,
               "options": options})

  def clear(self):
    """
    Description:
    ------------
    Clear all the items in the list.
    """
    return JsObjects.JsVoid("%s.innerHTML = ''" % self.component.dom.varName)

  def loading(self, label: str = "Processing data"):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param str label: Optional. The processing message.
    """
    return JsObjects.JsVoid("%s.innerHTML = '<i style=\"margin-right:5px\" class=\"fas fa-spinner fa-spin\"></i>%s'" % (
      self.component.dom.varName, label))


class JsHtmlTask(JsHtmlNetwork.JsHtmlDropFiles):

  def store(self, delimiter: str = None, format: str = None):
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
    raise ValueError("Not available use load instead")

  def load(self, data):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    """
    return JsObjects.JsVoid('''window['%s_data'] = %s; %s
      ''' % (self.component.htmlCode, JsUtils.jsConvertData(data, None),
             self.component.text.dom.setAttribute("title", self.content.length.toString().add(" rows")).r))
