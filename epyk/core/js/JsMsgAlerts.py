#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObject


class Msg:

  def __init__(self, page: Optional[primitives.PageModel] = None):
    self._src = page

  def status(self, timer: int = 3000, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------
    This function will display a popup message using the key status from the service return.

    Usage::

      page.js.msg.status()
      page.js.msg.status(200, {"color": "red"})

    Attributes:
    ----------
    :param int timer: Optional. The time the popup will be displayed.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "fixed", "padding": "5px 10px", 'border-radius': "5px",
                  "bottom": "10px", 'right': "10px"}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
      if 'left' in css_attrs:
        del dfl_attrs["right"]
    return '''
      (function(event, content, response){
        var popup = document.createElement("div"); 
        if (typeof content.background === 'undefined'){
          if (response.status == 200){
            popup.style.background = 'green'; popup.style.color = 'white';}
          else {popup.style.background = 'white'}
        }
        if (typeof content.css !== 'undefined'){
          for (var key in content.css) {popup.style[key] = content.css[key]}}
        %s
        popup.innerHTML = content.status; document.body.appendChild(popup);
        setTimeout(function(){ document.body.removeChild(popup)}, %s);
      })(event, data, response)''' % (JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, timer)

  def mouse(self, content: str, timer: int = 3000, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------
    Display a popup message close to the mouse.

    Usage::

      page.js.msg.mouse("This is a message")

    Attributes:
    ----------
    :param str content: The content of the popup.
    :param int timer: Optional. The time the popup will be displayed.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "absolute", "background": "white", "padding": "5px 10px", 'border-radius': "5px",
                 "top": JsObject.JsObject.get('event.clientY + "px"'),
                 'left': JsObject.JsObject.get('event.clientX + "px"')}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'bottom' in css_attrs:
        del dfl_attrs["top"]
      if 'right' in css_attrs:
        del dfl_attrs["left"]
    return '''
      (function(event, content){
        var popup = document.createElement("div"); %s
        popup.innerHTML = content; document.body.appendChild(popup);
        setTimeout(function(){ document.body.removeChild(popup); }, %s);
      })(event, %s)''' % (JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, timer, JsUtils.jsConvertData(content, None))

  def text(self, content: str, timer: int = 3000, fixed: bool = True, css_attrs: Optional[dict] = None,
           options: Optional[dict] = None):
    """
    Description:
    ------------
    Display a text message from a Javascript event for a specific period of time.

    Usage::

      page.js.msg.text("This is a message")

    Attributes:
    ----------
    :param str content: The content of the popup.
    :param int timer: Optional. The time the popup will be displayed.
    :param bool fixed: Optional.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    :param Optional[dict] options: Optional. Specific Python options available for this component.
    """
    dfl_attrs = {"position": "fixed" if fixed else "absolute", "background": "white", "padding": "5px 10px",
                  'border-radius': "5px", "bottom": "10px", 'right': "10px"}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
      if 'left' in css_attrs:
        del dfl_attrs["right"]
    options = options or {}
    if options.get("markdown", False) or options.get("showdown", False):
      self._src.jsImports.add("showdown")
      options["showdown"] = {}
    return '''
      (function(event, content, options){
        var popup = document.createElement("div"); %s;
        if(options.showdown){
          var converter = new showdown.Converter(options.showdown); content = converter.makeHtml(content)};
        popup.innerHTML = content; document.body.appendChild(popup);
        setTimeout(function(){ document.body.removeChild(popup); }, %s);
      })(event, %s, %s)''' % (
      JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, timer, JsUtils.jsConvertData(content, None),
      JsUtils.jsConvertData(options, None))

  def count(self, value: int, content: Optional[str] = None, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param int value:
    :param Optional[str] content: Optional. The content of the popup.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "absolute", "background": "white", "padding": "5px 10px", 'border-radius': "5px",
                 "bottom": "40px", 'right': "10px"}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
      if 'left' in css_attrs:
        del dfl_attrs["right"]
    return '''
      (function(event, inc, content){
        var currentVal;
        if(content == null){
          var currentVal = parseFloat(window['globalPoopup'].querySelector('div').innerHTML) + inc;
          window['globalPoopup'].querySelector('div').innerHTML = currentVal;
        } else{
          if(typeof window['globalPoopup'] === 'undefined'){
            window['globalPoopup'] = document.createElement("div");
            var globalValue = document.createElement("div");
            globalValue.innerHTML = inc; 
            globalValue.style.marginRight = '5px';
            globalValue.style.display = 'inline-block';
            var globalContent = document.createElement("div");
            globalContent.innerHTML = inc; globalContent.style.display = 'inline-block';
            globalContent.innerHTML = content;
            window['globalPoopup'].appendChild(globalValue);
            window['globalPoopup'].appendChild(globalContent);
            document.body.appendChild(window['globalPoopup']);
          } else {
            var currentVal = parseFloat(window['globalPoopup'].querySelector('div').innerHTML) + inc;
            window['globalPoopup'].querySelector('div').innerHTML = currentVal;
          } 
        }
      %s
      if(currentVal == 0){
        document.body.removeChild(window['globalPoopup']); window['globalPoopup'] = undefined}
      })(event, %s, %s)''' % (
      JsNodeDom.JsDoms.get("window['globalPoopup']").css(dfl_attrs).r, value, JsUtils.jsConvertData(content, None))

  def fixed(self, content: str, fixed: bool = True, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str content: The content of the popup.
    :param bool fixed: Optional.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "fixed" if fixed else "absolute", "background": "white", "padding": "10px 20px",
                  'border-radius': "5px", "bottom": "10px", 'right': "10px"}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
      if 'left' in css_attrs:
        del dfl_attrs["right"]
    return '''
      (function(event, content){
        var popup = document.createElement("div"); %s 
        var popupSpan = document.createElement("span");
        popupSpan.innerHTML = "&times;";
        popupSpan.style.position = 'absolute';
        popupSpan.style.top = 0;
        popupSpan.style.cursor = 'pointer';
        popupSpan.addEventListener('click', function(){ document.body.removeChild(popup) });
        popupSpan.style.right = '5px';
        popup.appendChild(popupSpan);
        var popupContent = document.createElement("div");
        popupContent.innerHTML = content;
        popup.appendChild(popupContent); document.body.appendChild(popup);
      })(event, %s)''' % (JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, JsUtils.jsConvertData(content, None))

  def center(self, content: str, timer: int = None, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str content: The content of the popup.
    :param int timer: Optional. The time the popup will be displayed.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "absolute", "background": "white", "padding": "10px 20px", 'border-radius': "5px",
                  "top": "50%", 'left': "50%", 'zIndex': 110, 'border': '1px solid black'}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
      if 'left' in css_attrs:
        del dfl_attrs["right"]
    return '''
      (function(event, content){
        var popup = document.createElement("div"); %(dom)s
        var popupSpan = document.createElement("span");
        popupSpan.innerHTML = "&times;";
        popupSpan.style.position = 'absolute';
        popupSpan.style.top = 0;
        popupSpan.style.cursor = 'pointer';
        popupSpan.addEventListener('click', function(){ document.body.removeChild(popup) });
        popupSpan.style.right = '5px';
        popup.appendChild(popupSpan);
        var popupContent = document.createElement("div");
        popupContent.innerHTML = content;
        popup.appendChild(popupContent); document.body.appendChild(popup);
        if(%(timer)s != null){
          setTimeout(function(){ document.body.removeChild(popup); }, %(timer)s);
        }
      })(event, %(content)s)''' % {'dom': JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, 'timer': timer,
                                   'content': JsUtils.jsConvertData(content, None)}

  def banner(self, content: str, timer: Optional[int] = None, css_attrs: Optional[dict] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str content: The content of the popup.
    :param Optional[int] timer: Optional. The time the popup will be displayed.
    :param Optional[dict] css_attrs: Optional. The CSS attributes for the popup.
    """
    dfl_attrs = {"position": "absolute", "padding": "10px", "bottom": "0", "width": '100%', 'background': 'pink'}
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'top' in css_attrs:
        del dfl_attrs["bottom"]
    return '''
      (function(event, content){
        var popup = document.createElement("div"); %(dom)s
        var popupSpan = document.createElement("span");
        popupSpan.innerHTML = "&times;";
        popupSpan.style.position = 'absolute';
        popupSpan.style.top = 0;
        popupSpan.style.cursor = 'pointer';
        popupSpan.addEventListener('click', function(){ document.body.removeChild(popup) });
        popupSpan.style.right = '5px';
        popup.appendChild(popupSpan);
        var popupContent = document.createElement("div");
        popupContent.innerHTML = content;
        popup.appendChild(popupContent); document.body.appendChild(popup);
        if(%(timer)s != null){
          setTimeout(function(){ document.body.removeChild(popup); }, %(timer)s)}
      })(event, %(content)s)''' % {'dom': JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, 'timer': timer,
                                   'content': JsUtils.jsConvertData(content, None)}
