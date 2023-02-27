#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class JsItemsDef:

  def __init__(self, component: primitives.HtmlModel):
    self.component = component

  def _item(self, item_def):
    return '''%(item_def)s; htmlObj.appendChild(item)
      ''' % {'item_def': item_def}

  def text(self, page: primitives.PageModel):
    """
    Add text items to the list
 
    :param page: Page object. The internal page object.
    """
    item_def = '''
    var item = document.createElement("DIV");  
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      item.setAttribute('name', 'value'); item.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = item.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = this.innerHTML; options.click(event, value);
           if(dataValue == 'true'){
             item.classList.remove('list_text_selected');
             item.setAttribute('data-valid', false)}
           else{item.classList.add('list_text_selected'); item.setAttribute('data-valid', true) }
         }
      }
    } else {
      item.setAttribute('name', 'value'); item.setAttribute('data-valid', true);}
    if(options.draggable != false){ 
      item.setAttribute('draggable', true);
      item.style.cursor = 'grab';
      item.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    }
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){item.style[key] = options.style[key] })}
    if(typeof data === 'object'){ 
      if(typeof data.style !== 'undefined'){
        Object.keys(data.style).forEach(function(key){item.style[key] = data.style[key] })}
      item.innerHTML = data.text} else { item.innerHTML = data }'''
    return self._item(item_def)

  def logs(self, page: primitives.PageModel):
    """
    Add text items to the list.
 
    :param page: Page object. The internal page object.
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.fontSize = "%(fontSize)s";  
    var message = document.createElement("DIV"); 
    message.style.display = "inline-block" ;  
    if (typeof data.color !== 'undefined'){item.style.borderLeft = "4px solid " + data.color;}
    else {item.style.borderLeft = "4px solid %(color)s"}
    item.style.borderBottom = "1px solid %(white)s";
    item.style.borderTop = "1px solid %(white)s";
    var log = document.createElement("DIV"); log.style.background = "%(lightGrey)s" ; log.style.margin = "0 5px";
    log.style.display = "inline-block" ;  log.style.fontWeight = 900 ; log.style.minWidth = "95px" ; 
    var elapsedTime = "";
    if ((typeof data.d !== 'undefined') && (data.d != 0)){elapsedTime = data.d + "d";}
    if ((typeof data.h !== 'undefined') && (data.h != 0)){elapsedTime = elapsedTime + " "+ data.h + "h";}
    if ((typeof data.m !== 'undefined') && (data.m != 0)){elapsedTime = elapsedTime + " "+ data.m + "m";}
    if ((typeof data.s !== 'undefined') && (data.s != 0)){elapsedTime = elapsedTime + " "+ data.s + "s";}
    log.innerHTML = elapsedTime + %(label)s;
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = message.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = Object.assign({}, {"value": message.innerHTML, "timestamp": log.innerHTML}, data); 
           options.click(event, value)
           if(dataValue == 'true'){
             message.classList.remove('list_text_selected');
             message.setAttribute('data-valid', false)}
           else{message.classList.add('list_text_selected'); message.setAttribute('data-valid', true) }
         }
      }
    } else {
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', true);}
    if(options.draggable != false){ 
      message.setAttribute('draggable', true);
      message.style.cursor = 'grab';
      message.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    }
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){message.style[key] = options.style[key] })}
    if(typeof data === 'object'){ 
      message.innerHTML = data.text} else { message.innerHTML = data };
    item.appendChild(log);
    item.appendChild(message);
    ''' % {"lightGrey": page.theme.greys[1], "fontSize": page.body.style.globals.font.normal(),
           "color": page.theme.notch(), "white": page.theme.black if page.theme.dark else page.theme.white,
           'label': JsUtils.jsConvertData(self.component.options.label, None)}
    return self._item(item_def)

  def timeline(self, page: primitives.PageModel):
    """
    Add text items to the list
 
    :param page: Page object. The internal page object.
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.fontSize = "%(fontSize)s";  
    var message = document.createElement("DIV"); 
    message.style.display = "inline-block" ;  
    item.style.borderBottom = "1px solid %(white)s";
    item.style.borderTop = "1px solid %(white)s";
    var log = document.createElement("DIV"); log.style.background = "%(lightGrey)s" ; log.style.margin = "0 5px";
    log.style.display = "inline-block" ;  log.style.fontWeight = 900 ; log.style.minWidth = "95px" ; 
    var elapsedTime = "";
    if ((typeof data.d !== 'undefined') && (data.d != 0)){elapsedTime = data.d + "d";}
    if ((typeof data.h !== 'undefined') && (data.h != 0)){elapsedTime = elapsedTime + " "+ data.h + "h";}
    if ((typeof data.m !== 'undefined') && (data.m != 0)){elapsedTime = elapsedTime + " "+ data.m + "m";}
    if ((typeof data.s !== 'undefined') && (data.s != 0)){elapsedTime = elapsedTime + " "+ data.s + "s";}
    log.innerHTML = elapsedTime + %(label)s;
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = message.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = Object.assign({}, {"value": message.innerHTML, "timestamp": log.innerHTML}, data); 
           options.click(event, value)
           if(dataValue == 'true'){
             message.classList.remove('list_text_selected');
             message.setAttribute('data-valid', false)}
           else{message.classList.add('list_text_selected'); message.setAttribute('data-valid', true) }
         }
      }
    } else {
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', true);}
    if(options.draggable != false){ 
      message.setAttribute('draggable', true);
      message.style.cursor = 'grab';
      message.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    }
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){message.style[key] = options.style[key] })}
    if(typeof data.style !== 'undefined'){
      Object.keys(data.style).forEach(function(key){message.style[key] = data.style[key] })}
    if(typeof data === 'object'){ 
      message.innerHTML = data.text} else { message.innerHTML = data };
    var balise = document.createElement("DIV"); 
    var dot = document.createElement("DIV"); dot.style.margin = "4px auto"; 
    if (typeof data.color !== 'undefined'){dot.style.background = data.color;}
    else {dot.style.background = "%(color)s";}
    dot.style.borderRadius = "50px"; dot.style.width = "5px"; dot.style.height = "5px";
    balise.style.border = "1px solid %(black)s"; balise.style.borderRadius = "50px"; balise.style.width = "15px";
    balise.style.height = "15px"; balise.style.float = "left"; balise.appendChild(dot); item.appendChild(balise);
    item.appendChild(log);
    var msgContainer = document.createElement("DIV"); msgContainer.style.display = "block";
    msgContainer.style.height = "auto"; msgContainer.style.marginLeft = "7px"; msgContainer.style.marginTop = "2px";
    msgContainer.style.paddingLeft = "5px";
    if (typeof data.space !== 'undefined'){msgContainer.style.paddingBottom = ""+ data.space + "px";}
    else {msgContainer.style.paddingBottom = "10px";}
    msgContainer.style.borderLeft = "1px solid %(black)s"; msgContainer.style.width = "100%%";
    msgContainer.appendChild(message); item.appendChild(msgContainer);
    ''' % {"lightGrey": page.theme.greys[1], "fontSize": page.body.style.globals.font.normal(),
           "color": page.theme.notch(),
           "black": page.theme.dark_or_white(False), "white": page.theme.black if page.theme.dark else page.theme.white,
           'label': JsUtils.jsConvertData(self.component.options.label, None)}
    return self._item(item_def)

  def status(self, page: primitives.PageModel):
    """
    Add text items to the list
 
    :param page: Page object. The internal page object.
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.fontSize = "%(fontSize)s";  
    var message = document.createElement("DIV"); 
    message.style.display = "inline-block" ;  
    message.style.paddingLeft = "2px" ;  
    item.style.borderBottom = "1px solid %(white)s";
    item.style.borderTop = "1px solid %(white)s";
    var log = document.createElement("DIV");
    log.style.paddingTop = "2px";
    log.style.paddingBottom = "2px";
    if(typeof data.color !== 'undefined'){log.style.color = "%(white)s"; log.style.background = data.color;}
    else {log.style.background = "%(grey)s"} ; 
    log.style.margin = 0;
    log.innerHTML = data.status; log.style.display = "inline-block"; log.style.width = "90px"; 
    log.style.textAlign = "center"; log.style.fontWeight = 900;
    if(options.click != null){ 
      item.style.cursor = 'pointer';
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', false);
      item.onclick = function(event){
         var selectedLen = htmlObj.parentElement.querySelectorAll(".list_text_selected").length;
         var dataValue = message.getAttribute('data-valid');
         if (dataValue == 'true' || options.max_selected == null || selectedLen < options.max_selected ){
           var value = Object.assign({}, {"value": message.innerHTML, "status": log.innerHTML}); 
           options.click(event, value)
           if(dataValue == 'true'){
             message.classList.remove('list_text_selected');
             message.setAttribute('data-valid', false)}
           else{message.classList.add('list_text_selected'); message.setAttribute('data-valid', true) }
        }
      }
    } else {
      message.setAttribute('name', 'value'); message.setAttribute('data-valid', true);}
    if(options.draggable != false){ 
      message.setAttribute('draggable', true);
      message.style.cursor = 'grab';
      message.ondragstart = function(event){ var value = this.innerHTML; options.draggable(event, value)}
    }
    if(typeof options.style !== 'undefined'){
      Object.keys(options.style).forEach(function(key){message.style[key] = options.style[key] })}
    if(typeof data === 'object'){ 
      message.innerHTML = data.text} else { message.innerHTML = data };
      
    if(typeof data.color !== 'undefined'){
      message.style.borderLeft = "1px solid "+ data.color;}
    item.appendChild(log);
    item.appendChild(message);
    ''' % {"grey": page.theme.greys[3], "fontSize": page.body.style.globals.font.normal(),
           "white": page.theme.black if page.theme.dark else page.theme.white}
    return self._item(item_def)

  def tweet(self, page: primitives.PageModel):
    """
    Add text items to the list
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    if(options.showdown){var converter = new showdown.Converter(options.showdown); converter.setOption("display", "inline-block");
      data.content = converter.makeHtml(data.content).replace("<p>", "<p style='display:inline-block;margin:0'>")};
      
    if (typeof data.time === 'undefined'){
      const d = new Date();
      data.time = d.getFullYear() + '-' +('0' + (d.getMonth()+1)).slice(-2)+ '-' +  ('0' + d.getDate()).slice(-2) + ' '+d.getHours()+ ':'+('0' + (d.getMinutes())).slice(-2)+ ':'+d.getSeconds()
    }
    
    function hashCode(str) { // java String#hashCode
      var hash = 0; for (var i = 0; i < str.length; i++) {hash = str.charCodeAt(i) + ((hash << 5) - hash)} return hash}

    function intToRGB(i){
      var c = (i & 0x00FFFFFF).toString(16).toUpperCase(); return "00000".substring(0, 6 - c.length) + c}
    
    var item = document.createElement("DIV"); var title = document.createElement("DIV");  
    var titleValue = document.createElement("DIV");  
    titleValue.innerHTML = data.title;  titleValue.style.fontWeight = "bold"
    titleValue.style.fontSize = "15px"; titleValue.style.display = "inline-block";
    item.style.verticalAlign = "top";
    
    var dtime = document.createElement("DIV"); dtime.style.display = "inline-block"; dtime.style.fontSize = "12px";
    dtime.innerHTML = "@"+ data.time; title.appendChild(titleValue); title.appendChild(dtime);
    dtime.style.fontStyle = 'italic'; dtime.style.marginLeft = '5px';
    
    var msg = document.createElement("DIV"); msg.style.display = "inline-block"; msg.style.width = "calc(100% - 80px)";
    msg.style.padding = "2px";
    
    var avatar = document.createElement("DIV"); avatar.style.color = "white";
    avatar.style.background = "#"+ intToRGB(hashCode(data.author[data.author.length-1])); avatar.innerHTML = data.author;
    avatar.style.width = "30px"; avatar.style.height = "30px"; avatar.style.borderRadius = "30px";
    avatar.style.display = "inline-block"; avatar.style.margin = "5px"; avatar.style.fontWeight = "bold";
    avatar.style.fontSize = "20px"; avatar.style.textAlign = "center"; avatar.style.verticalAlign = "top";
    
    title.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
    
    var content = document.createElement("DIV"); content.innerHTML = data.content;
    msg.appendChild(title); msg.appendChild(content);
    
    item.appendChild(avatar); item.appendChild(msg); item.style.margin = "10px 5px"; 
    item.style.width = "calc(100% - 10px)"; item.style.padding = "5px"; item.style.border = "1px solid #e9e9e9";
    '''
    return self._item(item_def)

  def icon(self, page: primitives.PageModel):
    """
    Add icon items to the list.
 
    :param page: Page object. The internal page object.
    """
    page.jsImports.add('font-awesome')
    page.cssImport.add('font-awesome')
    item_def = '''
    var item = document.createElement("DIV"); var icon = document.createElement("I"); 
    if(typeof data.icon !== 'undefined') {data.icon.split(" ").forEach(function(s){icon.classList.add(s)})}
    else {options.icon.split(" ").forEach(function(s){icon.classList.add(s)}) }
    icon.style.marginRight = '5px'; var span = document.createElement("span");  
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', true); 
    if(typeof data === 'object'){span.innerHTML = data.text} else {span.innerHTML = data};
    if(options.click != null){ item.style.cursor = 'pointer';
      item.onclick = function(event){ var value = span.innerHTML; options.click(event, value)}};
    item.appendChild(icon); item.appendChild(span)'''
    return self._item(item_def)

  def check(self, page: primitives.PageModel):
    """
    Add check components to the list.
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.padding = 0; item.style.whiteSpace = "nowrap";  item.style.display = "block";
    
    var span = document.createElement("span");  
    var input = document.createElement("input");    
    input.setAttribute('type', 'checkbox');
    input.setAttribute('name', 'input_box');
    input.style.verticalAlign = "middle";
    input.onchange = function(event){ 
      event.stopPropagation(); event.cancelBubble = true; span.setAttribute('data-valid', this.checked); 
      var value = span.innerHTML; if(options.click != null){options.click(event, value)}
    };
    
    var span = document.createElement("label"); 
    if (options.text_click){
      span.style.cursor = "pointer";
      span.onclick = function(event){ 
        var isChecked = this.getAttribute('data-valid');
        if (isChecked == 'true'){this.setAttribute('data-valid', false); input.checked = false} 
        else {this.setAttribute('data-valid', true); input.checked = true}
        var value = this.innerHTML; if(options.click != null){options.click(event, value)}
      };
    }
    span.style.marginLeft = '5px'; span.setAttribute('data-valid', false); span.style.marginBottom = '0px'; 
    if(typeof data === 'object'){ 
      if(typeof data.text !== 'undefined'){ span.innerHTML = data.text} else {span.innerHTML = data.value}} 
    else {span.innerHTML = data};
    if(options.checked){ 
      input.setAttribute('checked', options.checked); span.setAttribute('data-valid', options.checked)};
    var checkedCol = "checked";
    if (typeof options.checked_key !== 'undefined'){checkedCol = options.checked_key}
    if(data[checkedCol]){
      input.setAttribute('checked', data[checkedCol]); span.setAttribute('data-valid', data[checkedCol])};
    if (options.position == 'right'){
      span.innerHTML = ""; var labelTag = document.createElement("span"); labelTag.setAttribute('name', 'value');
      labelTag.innerHTML = data; labelTag.style.margin = '5px'; labelTag.style.marginRight = '5px'; 
      item.appendChild(labelTag);
    } else {span.setAttribute('name', 'value');}
    span.style.verticalAlign = "middle";
    item.appendChild(input); item.appendChild(span);
    '''
    return self._item(item_def)

  def radio(self, page: primitives.PageModel):
    """
    Add radio components to the list.
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    item.style.padding = 0; item.style.whiteSpace = "nowrap";  item.style.display = "block";
    var span = document.createElement("span");  
    var input = document.createElement("input");    
    input.setAttribute('type', 'radio'); input.setAttribute('name', options.group);
    input.style.verticalAlign = "middle";
    input.onclick = function(event){
        var value = span.innerHTML; 
        if (input.checked && (span.getAttribute('data-valid') == 'true')){
          input.checked = false;
          span.setAttribute('data-valid', false)} 
        else{
          this.parentNode.parentNode.parentNode.querySelectorAll('[name=value]').forEach(
            function(node){node.setAttribute('data-valid', false)});
          if(options.click != null){options.click(event, value)};
          span.setAttribute('data-valid', input.checked)
        }
    };  
    if (options.text_click){
      span.style.cursor = "pointer";
      span.onclick = function(event){
          var value = span.innerHTML;
          if (this.getAttribute('data-valid') == 'true'){
            input.checked = false; this.setAttribute('data-valid', false)
          } else {
            this.parentNode.parentNode.parentNode.querySelectorAll('[name=value]').forEach(
              function(node){node.setAttribute('data-valid', false)});
            if(options.click != null){options.click(event, value)};
            this.setAttribute('data-valid', true); input.checked = true;
          }
      };  
    }
    span.setAttribute('name', 'value'); span.setAttribute('data-valid', false);
    span.style.marginLeft = "5px";
    if(typeof data === 'object'){ 
      span.innerHTML = data.text;
      var checkedCol = "checked";
      if (typeof options.checked_key !== 'undefined'){checkedCol = options.checked_key};
      if(data[checkedCol]){
        input.setAttribute('checked', data[checkedCol])
        span.setAttribute('data-valid', data[checkedCol]);
      }
    } else { span.innerHTML = data};
    span.style.verticalAlign = "middle";
    item.appendChild(input); item.appendChild(span);
    '''
    return self._item(item_def)

  def badge(self, page: primitives.PageModel):
    """
    Add text object with badges to the list.
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV");  
    var span = document.createElement("span"); span.setAttribute('name', 'value'); span.innerHTML = data.text; 
    item.appendChild(span);
    if(typeof data.value !== 'undefined'){ 
      var badge = document.createElement("span"); badge.innerHTML = data.value;
      badge.style.backgroundColor = 'red'; badge.style.color = 'white'; badge.style.borderRadius = '50%%'; 
      badge.style.padding = '0 3px'; badge.style.marginLeft = '5px'; badge.style.fontSize = '%s'; 
      for(const attr in options.badge){badge.style[attr] = options.badge[attr]};
      item.appendChild(badge)}''' % page.body.style.globals.font.normal(-2)
    return self._item(item_def)

  def link(self, page: primitives.PageModel):
    """
    Add links items to the list.
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("div"); var link = document.createElement("a"); item.style.whiteSpace = "nowrap";
    link.style.color = "inherit"; link.setAttribute('name', 'value'); link.setAttribute('data-valid', false);
    link.innerHTML = data.text; if(typeof data.url !== 'undefined'){link.href = data.url} else {link.href = '#'};
    if(typeof data.target !== "undefined"){link.target = data.target}
    if(typeof data.icon !== 'undefined'){ 
      var iconItem = document.createElement("i"); iconItem.setAttribute("class", data.icon);
      iconItem.style.marginRight = "5px"; iconItem.style.color = "#0056B3"; item.appendChild(iconItem)}
    item.appendChild(link);
    if(typeof data.dsc !== "undefined"){
      var dsc = document.createElement("div"); dsc.style.display = "inline-block"; dsc.style.marginLeft = "5px";
      dsc.innerHTML = data.dsc; item.appendChild(dsc)}
    if(typeof data.image !== "undefined"){
      var img = document.createElement("img"); img.setAttribute('width', "10px"); img.setAttribute('height', "10px");
      img.style.marginRight = "5px"; img.setAttribute('src', data.image); link.prepend(img)}'''
    return self._item(item_def)

  def button(self, page: primitives.PageModel):
    """
    Add button items to the list.
    Data structure expected:
      {'text': f, 'button': 'get',  'event': {'url': '/test', 'data': {'Ok': 45}}
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    var item = document.createElement("DIV"); var text = document.createElement("div");
    item.style.clear = 'both'; text.style.display = 'inline-block'; text.style.padding = 0;
    text.setAttribute('name', 'value'); text.setAttribute('data-valid', false);
    text.innerHTML = data.text ; var button = document.createElement("button"); 
    button.classList.add("cssbuttonbasic"); button.style.float = 'right'; button.style.padding = '0 5px';
    button.style.display = 'inline-block'; button.style.margin = 0; button.style.lineHeight = "18px";
    button.innerHTML = data.button; item.appendChild(text); item.appendChild(button);
    if(typeof data.tooltip !=='undefined'){ button.setAttribute('title', data.tooltip)}
    if(typeof data.event !=='undefined'){
      button.addEventListener("click", function() {
        var xhttp = new XMLHttpRequest();
        var event_data = {}; var event_method = 'POST';
        if(typeof data.event.data !== 'undefined'){ event_data = data.event.data}
        if(typeof data.event.method !== 'undefined'){ event_method = data.event.method}
        xhttp.open(event_method, data.event.url, true);
        xhttp.send(JSON.stringify(event_data));
      });
    }'''
    return self._item(item_def)

  def box(self, page: primitives.PageModel):
    """
    This will represent a title with a text and a list of icons.
 
    :param page: Page object. The internal page object
    """
    page.jsImports.add('font-awesome')
    page.cssImport.add('font-awesome')
    item_def = '''
    var item = document.createElement("DIV"); item.style.borderRadius = "5px"; item.style.padding = "2px";
    item.setAttribute('data-valid', true);
    var title = document.createElement("DIV"); title.setAttribute('name', 'value');
    if (typeof data.color !== 'undefined'){
      item.style.border = "1px solid " + data.color; title.style.color = data.color}
    title.style.fontWeight = 'bold'; title.innerHTML = data.title;
    var text = document.createElement("DIV"); text.innerHTML = data.text;
    item.appendChild(title); item.appendChild(text);
    var icons = document.createElement("DIV"); icons.style.textAlign = 'right';
    if(typeof data.icons !== 'undefined') {
      data.icons.forEach(function(rec){
          var icon_dom = document.createElement("I"); icon_dom.style.marginRight = '5px';
          rec.icon.split(" ").forEach(function(s){icon_dom.classList.add(s)}); 
          if(typeof rec.color !== 'undefined'){ icon_dom.style.color = rec.color}
          if(typeof rec.tooltip !== 'undefined'){ icon_dom.setAttribute('title', rec.tooltip)}
          if(rec.click != null){ icon_dom.style.cursor = 'pointer';
            icon_dom.onclick = function(event){ var value = data.title; eval(rec.click)}};
          icons.appendChild(icon_dom)})}
    item.appendChild(icons)'''
    return self._item(item_def)

  def period(self, page: primitives.PageModel):
    """
    Add text items to the list
 
    :param page: Page object. The internal page object
    """
    item_def = '''
    if(options.showdown){var converter = new showdown.Converter(options.showdown); 
      converter.setOption("display", "inline-block");
      data.content = converter.makeHtml(data.content).replace("<p>", "<p style='display:inline-block;margin:0'>")};

    function hashCode(str) {
      var hash = 0; for (var i = 0; i < str.length; i++) {hash = str.charCodeAt(i) + ((hash << 5) - hash)} return hash}
    function intToRGB(i){
      var c = (i & 0x00FFFFFF).toString(16).toUpperCase(); return "00000".substring(0, 6 - c.length) + c}
      
    var item = document.createElement("DIV"); var title = document.createElement("DIV");  
    var titleValue = document.createElement("DIV");  
    titleValue.innerHTML = data.title;  titleValue.style.fontWeight = "bold"
    titleValue.style.fontSize = "15px"; titleValue.style.display = "inline-block"; 
    item.style.verticalAlign = "top"; title.appendChild(titleValue);
    
    var msg = document.createElement("DIV"); msg.style.display = "inline-block"; msg.style.width = "calc(100% - 80px)";
    msg.style.padding = "2px 2px 2px 5px"; msg.style["margin-left"] = "5px";

    title.setAttribute('name', 'value'); item.setAttribute('data-valid', true);
    if (typeof data.color === 'undefined') {data.color = "#aaaaaa"};
    var content = document.createElement("DIV"); content.innerHTML = data.content;
    msg.appendChild(title); msg.appendChild(content);
    msg.style["border-left"] = "1px solid " + data.color;
    
    var dFrom = document.createElement("DIV"); item.appendChild(dFrom); dFrom.innerHTML = data.from;
    dFrom.style.color = data.color; dFrom.style["font-size"] = "11px";
    
    item.appendChild(msg); item.style.margin = "0 5px 5px 5px";
    
    if (typeof data.to !== 'undefined'){
      var dTo = document.createElement("DIV"); item.appendChild(dTo); dTo.innerHTML = data.to;
      dTo.style.color = data.color; dTo.style["font-size"] = "11px";
    };
    
    item.style.width = "calc(100% - 10px)"; item.style.padding = "5px"; item.style.border = "1px solid #e9e9e9";
    '''
    return self._item(item_def)

  def custom(self, item_def: str):
    """
    Allow the creation of custom items for list.
 
    :param item_def: The JavaScript item definition
    """
    return self._item(item_def)


class JsItem(JsHtml.JsHtmlRich):

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.page, '''
      (function(dom){var values = []; dom.childNodes.forEach( function(dom, k){  
          const item = dom.querySelector('[name=value]');
          if (item != null){
            const valid = item.getAttribute("data-valid");
            if (valid == null){
              const checkItems = dom.querySelector('[data-valid=true]');
              if (checkItems != null){values.push(item.innerHTML)}
            } else {if (valid === 'true'){values.push(item.innerHTML)}}
          }
      }); return values})(%s)''' % self.varName)

  @property
  def all(self):
    return JsHtml.ContentFormatters(self.page, '''
(function(dom){var values = []; dom.childNodes.forEach(function(dom, k){  
  const item = dom.querySelector('[name=value]'); 
  if (item != null){values.push(dom.querySelector('[name=value]').innerHTML)}
}); return values})(%s)''' % self.varName)

  @property
  def selected(self):
    """
    Return a list with all the selected values.
    """
    return self.content

  @property
  def unselected(self):
    """
    Return a list with all the unselected values.
    """
    return JsHtml.ContentFormatters(self.page, '''
        (function(dom){var values = []; dom.childNodes.forEach( function(dom, k){   
          const item = dom.querySelector('[name=value]');
          if (item != null){
            const valid = item.getAttribute("data-valid");
            if (valid == null){
              const checkItems = dom.querySelector('[data-valid=true]');
              if (checkItems != null){values.push(item.innerHTML)}
            } else {if (valid === 'true'){values.push(item.innerHTML)}}
          }
        }); return values })(%s)''' % self.varName)

  @property
  def first(self):
    """
    Get the first value in the list.
    """
    return JsObjects.JsVoid("%s.firstChild.querySelector('[name=value]').innerHTML" % self.varName)

  @property
  def last(self):
    """
    Get the last value in the list.
    """
    return JsObjects.JsVoid("%s.lastChild.querySelector('[name=value]').innerHTML" % self.varName)

  @property
  def current(self):
    """
    Get the current value from a LI item event.
    """
    return JsObjects.JsVoid('''(function(){
var source = this; if (typeof this.querySelector === 'undefined'){source = event.target || event.srcElement}
if(source.getAttribute("name")){return source.innerHTML} 
else {return source.querySelector('[name=value]').innerHTML} 
})(event, this)''')

  @property
  def values(self):
    """
    Get all the values in the list.
    """
    return JsObjects.JsArray.JsArray.get("")

  def copy(self):
    return JsObjects.JsVoid('''
let listData = %s;
var dummy = document.createElement("textarea");
document.body.appendChild(dummy);
dummy.value = JSON.stringify(listData);
dummy.select();
document.execCommand("copy");
document.body.removeChild(dummy);
''' % self.all.toStr())

  def getItemByValue(self, value: Union[str, primitives.JsDataModel]):
    """
    Get an item from the list based on its value.
 
    :param value: The value to find in the list
    """
    value = JsUtils.jsConvertData(value, None)
    return JsNodeDom.JsDoms.get('''
      (function(dom, value){var children = dom.childNodes; var values = null;
        for (var i = 0; i < children.length; i++) { 
          if(children[i].querySelector('[name=value]').innerHTML == value){values = children[i]; break} };
        return values })(%s, %s)''' % (self.varName, value))

  def selectAll(self, with_input_box: bool = False):
    """
    Select all the items in the list.
 
    :param with_input_box: If the items have a dedicated input box for the check
    """
    if self.component.options.items_type == "radio":
      raise ValueError("It is not possible to select all radios from a same group, use check instead")

    if self.component.options.items_type == "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach( function(dom, k){  
          const item = dom.querySelector('[name=input_box]');
          if (item != null){ 
            item.checked = true;
            dom.querySelector('[data-valid]').setAttribute("data-valid", true);
        }})''' % self.varName)

    return JsObjects.JsVoid('''
      %s.childNodes.forEach( function(dom, k){ 
        dom.querySelector('[name=value]').classList.add('list_%s_selected'); 
        dom.querySelector('[name=value]').setAttribute("data-valid", true);
      })''' % (self.varName, self.component.options.items_type))

  def unSelectAll(self, with_input_box: bool = False):
    """
    UnSelect all the items in the list.
 
    :param with_input_box: If the items have a dedicated input box for the check
    """
    if self.component.options.items_type in "check" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach(function(dom, k){  
          const item = dom.querySelector('[name=input_box]');
          if (item != null){ 
            dom.querySelector('[name=input_box]').checked = false;
            dom.querySelector('[data-valid]').setAttribute("data-valid", false);
        }})''' % self.varName)

    if self.component.options.items_type in "radio" or with_input_box:
      return JsObjects.JsVoid('''
        %s.childNodes.forEach(function(dom, k){  
          const item = dom.querySelector('[type=radio]');
          if (item != null){ 
            dom.querySelector('[type=radio]').checked = false;
            dom.querySelector('[data-valid]').setAttribute("data-valid", false);
        }})''' % self.varName)

    return JsObjects.JsVoid('''
      %s.childNodes.forEach( function(dom, k){  
        dom.querySelector('[name=value]').classList.remove('list_%s_selected');
        dom.querySelector('[name=value]').setAttribute("data-valid", false);
      })''' % (self.varName, self.component.options.items_type))

  def add(self, value: Union[str, dict], css_attrs: dict = None, css_cls: str = None, before: bool = False,
          options: dict = None):
    """
    Add items to the list.
 
    :param value:
    :param css_attrs: All the CSS attributes to be added to the LI component
    :param css_cls: The CSS class to be added to the LI component
    :param before:
    :param options:
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
      if(itemOptions.showdown){
          var converter = new showdown.Converter({}); converter.setOption("display", "inline-block");
          var content = item; if(typeof item.content !== 'undefined'){content = item.content};
          content = converter.makeHtml(content).replace("<p>", "<p style='display:inline-block;margin:0'>");
          item.content = content
      };
      var li = document.createElement("LI"); %(shape)s(li, item, %(options)s); 
      if(itemOptions.items_space){li.style.margin = "5px 0"; li.style.padding = "2px 0"};
      %(comp)s.%(event)s(li)
      if(itemOptions.delete){
        var close = document.createElement("i");
        close.setAttribute("class", itemOptions.delete_icon);
        close.style.cursor = 'pointer'; close.style.position = 'absolute'; close.style.right = "0";
        li.style.position = "relative";
        close.onclick = function(event){this.parentNode.remove()};
        for (const [key, value] of Object.entries(itemOptions.delete_position)){close.style[key] = value}
        li.lastChild.style.display = 'inline-block'; li.appendChild(close);
        const cls = %(cls)s;
        if (cls != null){li.classList.add(cls)}
      } ''' % {'comp': self.varName, 'options': self.component.options.config_js(options), 'value': value,
               'event': "prepend" if before else 'appendChild', 'cls': JsUtils.jsConvertData(css_cls, None),
               'shape': "%s%s" % (self.component.options.prefix, self.component.options.items_type)})

  def append(self, items: list, css_attrs: dict = None, css_cls: str = None, options: dict = None):
    """
    Add items to the list.
 
    :param items: The items
    :param css_attrs: Optional. All the CSS attributes to be added to the LI component
    :param css_cls: Optional. The CSS class to be added to the LI component
    :param options: Optional.
    """
    items = JsUtils.jsConvertData(items, None)
    return JsObjects.JsVoid(
      "%s.forEach(function(newItem){%s})" % (items, self.add(
        JsUtils.jsWrap("newItem"), css_attrs=css_attrs, css_cls=css_cls, before=False, options=options).toStr()))

  def prepend(self, items: str, css_attrs: dict = None, css_cls: str = None, options: dict = None):
    """
    Insert items to the beginning of the list.
 
    :param items: The items.
    :param css_attrs: Optional. All the CSS attributes to be added to the LI component
    :param css_cls: Optional. The CSS class to be added to the LI component
    :param options: Optional.
    """
    items = JsUtils.jsConvertData(items, None)
    return JsObjects.JsVoid(
      "%s.forEach(function(newItem){%s})" % (items, self.add(
        JsUtils.jsWrap("newItem"), css_attrs=css_attrs, css_cls=css_cls, before=True, options=options).toStr()))

  def tags(self, values: list, css_attrs: dict = None, css_cls: str = None):
    """
    Add tags to an item in the list.
 
    :param values: The tags to be added to the current item
    :param css_attrs: All the CSS attributes to be added to the LI component
    :param css_cls: The CSS class to be added to the LI component
    """
    return JsObjects.JsVoid('''
      var enumTags = %(values)s;
      if(enumTags != ''){
        if(typeof enumTags === 'string'){ enumTags = [enumTags]};
        enumTags.forEach(function(val){
          var item = document.createElement("DIV"); item.innerHTML = val;
          item.style.display = "inline-block"; item.style.padding = "1px 2px"; item.style.margin = "0 1px";
          item.style.color = "black"; item.style.fontSize = "8px"; item.style.background = "white";
          item.style.border = "1px solid white"; item.style.borderRadius = "5px"; const css = %(css)s;
          if (css != null){
            for (const [key, value] of Object.entries(css)) {
              item.style[key] = value
            }
          }
          const cls = %(cls)s;
          if(cls != null){item.classList.add(cls)}
          %(comp)s.lastChild.appendChild(item)
      })}''' % {'comp': self.varName, 'css': JsUtils.jsConvertData(css_attrs, None),
                'cls': JsUtils.jsConvertData(css_cls, None), 'values': JsUtils.jsConvertData(values, None)})

  def contextMenu(self, menu, js_funcs: Union[list, str] = None, menu_funcs: Union[list, str] = None,
                  profile: Optional[Union[bool, dict]] = False):
    """
    Add a context menu to an item in the list.
 
    :param menu:
    :param menu_funcs:
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
    if not hasattr(menu, 'source'):
      menu = self.component.page.ui.menus.contextual(menu)
    for i, item in enumerate(menu):
      funcs = ['''
        var data = {"action": event.srcElement.innerText};
        if(window.context_menu_source.getAttribute("name")){
          data["source"] = window.context_menu_source.innerHTML} 
        else {data["source"] = window.context_menu_source.querySelector('[name=value]').innerHTML} 
        ''']
      if menu_funcs is not None:
        if not isinstance(menu_funcs[i], list):
          menu_funcs[i] = [menu_funcs[i]]
        funcs.extend(menu_funcs[i])
      funcs.append(menu.dom.hide())
      item.click(funcs)
    self.context_menu = menu
    menu.source = self
    new_js_funcs = (js_funcs or []) + [self.page.js.objects.mouseEvent.stopPropagation(), self.context_menu.dom.css(
            {"display": 'block', 'left': self.page.js.objects.mouseEvent.clientX + "'px'",
             'top': self.page.js.objects.mouseEvent.clientY + "'px'"}),
          self.page.js.objects.mouseEvent.preventDefault()]
    return JsObjects.JsVoid('''
      %s.lastChild.addEventListener("contextmenu", function(event){
        window.context_menu_source = this; %s});
      ''' % (self.varName, JsUtils.jsConvertFncs(new_js_funcs, toStr=True, profile=profile)))

  def clear(self):
    """
    Clear all the items in the list.
    """
    return JsObjects.JsVoid(
      "while(%(comp)s.firstChild){%(comp)s.removeChild(%(comp)s.firstChild)}" % {'comp': self.varName})

  def select_item(self, value: Union[str, primitives.JsDataModel]):
    """
    Force the selection of an item in the list.
 
    :param value: The value of the item to be selected
    """
    value = JsUtils.jsConvertData(value, None)
    if self.component.options.items_type == "check":
      return JsObjects.JsVoid('''
var select_items = %(value)s;
%(varName)s.childNodes.forEach(function(dom, k){ 
  var value = dom.querySelector('[name=value]').innerHTML;
  if (((typeof select_items === 'string') && value == select_items) || ((Array.isArray(select_items) && (select_items.includes(value))))){
    dom.querySelector("span").setAttribute('data-valid', true); dom.querySelector("input").checked = true}
})''' % {'value': value, 'varName': self.varName})

    return JsObjects.JsVoid('''
          %(varName)s.childNodes.forEach(function(dom, k){ 
            var value = dom.querySelector('[name=value]').innerHTML;
            if (value == %(value)s){dom.classList.add('list_%(styleSelect)s_selected')}
          })''' % {'value': value, 'varName': self.varName, 'styleSelect': self.component.options.items_type})


class Tags(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """   Returns the list of data available on the filters panel.
    """
    return JsHtml.ContentFormatters(self.page, '''
      (function(dom){var content = {}; 
        dom.childNodes.forEach(function(rec){
          var label = rec.getAttribute('data-category');
          if(!(label in content) && (label != null)){ content[label] = [] }; 
          var listItem = rec.querySelector('span[name=chip_value]');
          if (listItem != null && (label != null)){content[label].push(listItem.textContent)}}); 
        return content})(%s)
      ''' % self.querySelector("div[name=panel]"))

  def is_duplicated(self, text: str, category: str = None):
    """
    Check the duplicates in the filter panel for a given category.
 
    :param text: The item text
    :param category: The item category
    """
    return JsObjects.JsObjects.get(''' 
      (function(dom){var index = -1; var children = dom.childNodes; var count = 0; 
        for(child in children){if((typeof children[child] === 'object') && (children[child].querySelector('span[name=chip_value]') != null) && children[child].querySelector('span[name=chip_value]').textContent == %(tezt)s){
            if(children[child].getAttribute('data-category') == %(category)s){ index = count; break; }
        }; count++; }; return index})(%(panel)s)''' % {"tezt": text, "category": category, "panel": self.querySelector("div[name=panel]")})

  def values(self, category: Union[str, primitives.JsDataModel] = None):
    if category is None:
      return JsObjects.JsArray.JsArray.get("(function(dom){var content = []; dom.childNodes.forEach(function(rec){content.push(rec.querySelector('span[name=chip_value]').textContent)}); return content})(%s)" % self.querySelector("div[name=panel]"))

    category = JsUtils.jsConvertData(category, None)
    return JsObjects.JsObjects.get(''' 
          (function(dom){var children = dom.childNodes; var values = [];
            for(child in children){if(typeof children[child] === 'object'){
                if(children[child].getAttribute('data-category') == %s){ 
                    var listItem = children[child].querySelector('span[name=chip_value]');
                    if (listItem != null){values.push(listItem.textContent)}}
            }}; return values})(%s)''' % (category, self.querySelector("div[name=panel]")))

  def hide(self):
    """
    Hide the filters panel.
    """
    return self.querySelector("div[name=panel]").show()

  def show(self):
    """
    Show the filters panel.
    """
    return self.querySelector("div[name=panel]").show()

  def toggle(self):
    """
    Toggle the display of the filters panel.
    """
    return self.querySelector("div[name=panel]").toggle()

  def add(self, text: Union[str, primitives.JsDataModel], category: Union[str, primitives.JsDataModel] = None,
          name: str = None, fixed: bool = False, no_duplicate: bool = True):
    """
    Add item on the filters panel.
    When no_duplicate is set to False it is possible to pass a list.
 
    :param text: The value to be added on the filter panel
    :param category: Optional. The item category
    :param name: Optional. The item name
    :param fixed: Optional.
    :param no_duplicate: Optional. An optional check on duplicated entries
    """
    text = JsUtils.jsConvertData(text, None)
    fixed = JsUtils.jsConvertData(fixed, None)
    if category is None:
      category = name or self.component._jsStyles['category']
    name = name or category
    category = JsUtils.jsConvertData(category, None)
    name = JsUtils.jsConvertData(name, None)
    # Convert the option to a javascript object
    # TODO move this in a centralised place
    options, js_options = self.component._jsStyles, []
    for k, v in options.items():
      if isinstance(v, dict):
        row = ["'%s': %s" % (s_k, JsUtils.jsConvertData(s_v, None)) for s_k, s_v in v.items()]
        js_options.append("'%s': {%s}" % (k, ", ".join(row)))
      else:
        if str(v).strip().startswith("function"):
          js_options.append("%s: %s" % (k, v))
        else:
          js_options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))

    if no_duplicate:
      return JsObjects.JsObjects.get('''if ((%(duplicated)s == -1) && (%(text)s != '')){ 
        chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: %(text)s, disabled: false, fixed: %(fixed)s}, {%(options)s})  }
      ''' % {'name': name, 'category': category, 'duplicated': self.is_duplicated(text, category),
             'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text,
             'options': ",".join(js_options)})

    return JsObjects.JsObjects.get('''var itemLabel = %(text)s;
        if(Array.isArray(itemLabel)){
          itemLabel.forEach(function(item){
            chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: item, disabled: false, fixed: %(fixed)s}, {%(options)s})})}
        else {chipAdd(%(panel)s, {name: %(name)s, category: %(category)s, value: itemLabel, disabled: false, fixed: %(fixed)s}, {%(options)s})}
        ''' % {'name': name, 'category': category, 'panel': self.querySelector("div[name=panel]"), 'fixed': fixed, 'text': text,
               'options': ",".join(js_options), "maxHeight": self.component._jsStyles["max_height"]})

  @property
  def input(self):
    """
    Clear the content of the filters panel.
    """
    return JsObjects.JsObjects.get("%s.value" % self.querySelector("input"))

  def clear(self):
    """
    Clear the content of the filters panel.
    """
    return self.querySelector("div[name=panel]").empty()

  def remove(self, text: Union[str, primitives.JsDataModel], category: Union[str, primitives.JsDataModel] = None):
    """
    Remove an item from the filters panel.
 
    :param text: The test of the items to be removed
    :param category: The test of the items to be removed
    """
    if category is None:
      category = self.component._jsStyles['category']
    category = JsUtils.jsConvertData(category, None)
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsObjects.get('''var itemPos = %(duplicated)s; if (itemPos >= 0){ %(panel)s.childNodes[itemPos].remove()}
      ''' % {'duplicated': self.is_duplicated(text, category), 'panel': self.querySelector("div[name=panel]")})

  def count(self):
    """
    Return a count of number of values defined in the filters across all the categories.
    """
    return self.values().length

  def categories(self):
    """
    Return a count of categories currently used to filter the data.
    """
    return self.content.dict.keys()
