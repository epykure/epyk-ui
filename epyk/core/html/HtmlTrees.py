#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.html import Html
from epyk.core.html import Defaults

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlTree

from epyk.core.html.options import OptTrees

from epyk.core.css.styles import GrpClsList
from epyk.core.css import Defaults as cssDefaults


class Tree(Html.Html):
  name = 'List Expandable'
  _option_cls = OptTrees.OptionsTree

  def __init__(self, report, records, width, height, html_code, helper, options, profile):
    options['is_root'] = True
    icon_details = cssDefaults.get_icon("folder_open")
    options['icon_open'] = icon_details["icon"]
    if icon_details['icon_family'] != 'bootstrap-icons':
      self.requirements = (icon_details['icon_family'],)
    options['style'] = {"list-style": 'none', 'margin-left': '8px', 'padding-left': 0}
    super(Tree, self).__init__(report, records, profile=profile, options=options,
                               css_attrs={"width": width, 'height': height})
    self.add_helper(helper)
    self.css(options['style'])
    self._jsStyles['click_node'] = None

  @property
  def dom(self) -> JsHtmlTree.JsHtmlTree:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlTree.JsHtmlTree
    """
    if self._dom is None:
      self._dom = JsHtmlTree.JsHtmlTree(self, report=self.page)
    return self._dom

  @property
  def options(self) -> OptTrees.OptionsTree:
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptTrees.OptionsTree
    """
    return super().options

  _js__builder__ = ''' if(options){htmlObj.innerHTML = ''; options.is_root = false};
      data.forEach(function(item, i){
        var li = document.createElement("li");
        var a = document.createElement("a");
        if(typeof item.items !== 'undefined'){
          var ul = document.createElement("ul"); 
          for(const attr in options.style){ul.style[attr] = options.style[attr]};
          options.builder(ul, item.items, options);
          var icon = document.createElement("i"); icon.style.marginRight = '5px';
          icon.onclick = function(){ 
            var ulDisplay = this.parentNode.querySelector('ul').style.display;
            if(ulDisplay == 'none'){ 
              this.parentNode.querySelector('ul').style.display = 'block';
              icon.setAttribute("class", options.icon_open)}
            else{
              this.parentNode.querySelector('ul').style.display = 'none';
              icon.setAttribute("class", options.icon_close)}
          };
          icon.style.cursor = "pointer";
          options.icon_open.split(" ").forEach(function(s){icon.classList.add(s)});
          var span = document.createElement("span"); 
          span.innerHTML = item.value;
          span.style.whiteSpace = 'nowrap';
          if (typeof item.tooltip !== "undefined"){span.setAttribute('title', item.tooltip);};
          var badge = document.createElement("span"); 
          if(options.with_badge){
            badge.setAttribute("class", "badge badge-pill");
            badge.innerHTML = item.items.length;
            badge.style.padding = 0;
            badge.style.verticalAlign = "top";
            icon.appendChild(badge);
          };
          a.appendChild(icon); a.appendChild(span); a.appendChild(ul);
        } else {
          a.innerHTML = item.value;
          a.style.whiteSpace = 'nowrap';
          if(item.draggable != false){ 
            a.setAttribute('draggable', true);
            if (typeof item._path !== "undefined"){a.setAttribute("data-path", item._path)};
            if (typeof item.tooltip !== "undefined"){a.setAttribute('title', item.tooltip);};
            a.style.cursor = 'grab';
            a.ondragstart = function(event){var value = this.innerHTML; 
              var file_path = this.getAttribute("data-path");
              if (file_path === null){event.dataTransfer.setData("text", value)}
              else{ event.dataTransfer.setData("text", file_path)}}
          }
          if (typeof item.url !== "undefined"){
            a.setAttribute("target", item.target || "_blank");
            a.href = item.url}
          a.style.paddingLeft = '18px';
        }
        li.appendChild(a);
        htmlObj.appendChild(li)
      })'''

  def click_node(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles['click_node'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile)
    return self

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] source_event: The JavaScript DOM source for the event (can be a sug item).
    :param bool on_ready: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._jsStyles['click_leaf'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(js_funcs, toStr=True)
    return self

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<ul %s></ul>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)


class TreeInput(Tree):

  def set(self, ul, data):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param ul:
    :param data:
    """
    for l in data:
      if l.get('items') is not None:
        sub_l = self.page.ui.list()
        sub_l.options.managed = False
        ul.add_item(sub_l)[-1].no_decoration()
        ul[-1].add_label(l['label'], css={"color": l.get('color', 'none')})
        ul[-1].add_icon(self.options.icon_open if self.options.expanded else self.options.icon_close)
        if not self.options.expanded:
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options.icon_close.split(" ")[-1], self.options.icon_open.split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(self.page.ui.text(l['label']).editable().css(
          {"width": 'none', 'min-width': 'none'}))[-1].no_decoration()
        ul[-1].css({"color": l.get('color', 'none')})
    return self


class DropDown(Html.Html):
  requirements = ('bootstrap', )
  name = 'DropDown Select'
  _option_cls = OptTrees.OptDropDown

  def __init__(self, page, data, text, width, height, html_code, helper, options, profile):
    options.update({"a": {'text-decoration': 'none', 'line-height': '%spx' % Defaults.LINE_HEIGHT,
                          'padding': '0 10px', "min-width": '%spx' % options.get("width")},
                    "ul": {"left": "%spx" % options.get("width")}})
    super(DropDown, self).__init__(page, text, html_code=html_code, profile=profile, options=options,
                                   css_attrs={"width": width, "height": height})
    self.add_helper(helper)
    self._vals, self.text = data, text
    self.attr["class"].add("menu")
    self.css(
      {'padding': 0, 'margin': "1px", "display": "block", "z-index": 10, 'cursor': 'pointer', 'position': 'relative'})
    self.style.css.border = "1px solid %s" % page.theme.greys[2]

  @property
  def style(self) -> GrpClsList.ClassDropDown:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    :rtype: GrpClsList.ClassDropDown
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassDropDown(self)
    return self._styleObj

  @property
  def options(self) -> OptTrees.OptDropDown:
    """
    Description:
    -----------
    Property to set all the possible object for a DropDown.

    :rtype: OptTrees.OptDropDown
    """
    return super().options

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None, on_ready: bool = False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: A Javascript Python function
    :param Optional[Union[bool, dict]] profile: Optional. Set to true to get the profile for the function on the Javascript console.
    :param Optional[str] source_event: Optional. The source target for the event.
    :param bool on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    self.options.onClick(js_funcs)
    return self

  _js__builder__ = '''
      if(options.clearDropDown){htmlObj.innerHTML = ""};
      data.forEach(function(rec){
        if ((rec.items != undefined) && (rec.items.length > 0)) {
          var li = document.createElement("li"); li.classList.add("dropdown"); li.style.listStyleType = 'none'; 
          li.style.display = 'list-item'; li.style.textAlign = '-webkit-match-parent'; 
          var a = document.createElement("a"); a.setAttribute('tabindex', -1); 
          a.appendChild(document.createTextNode(rec.value)); options.clearDropDown = false;
          var span = document.createElement("span"); span.classList.add("caret"); a.appendChild(span); 
          li.appendChild(a); 
          var ul = document.createElement("ul"); ul.classList.add("submenu");
          if(typeof options.ul !== "undefined"){
            Object.keys(options.ul).forEach(function(key){ul.style[key] = options.ul[key]})}
          if(typeof options.a !== "undefined"){
            Object.keys(options.a).forEach(function(key){a.style[key] = options.a[key]})}
          options.builder(ul, rec.items, options); li.appendChild(ul); htmlObj.appendChild(li);
        } else {
          var a = document.createElement("a"); a.innerHTML = rec.value;
          if(typeof rec.url !== "undefined"){a.href= rec.url}; 
          if(typeof options.a !== "undefined"){
            Object.keys(options.a).forEach(function(key){a.style[key] = options.a[key]})}
          if(typeof options.click !== "undefined"){
            a.onclick = function(event){const value = a.innerText; options.click(event, value)}};
          var li = document.createElement("li"); li.style.listStyleType = 'none'; li.style.display = 'list-item';
          li.style.textAlign = '-webkit-match-parent'; li.appendChild(a); htmlObj.appendChild(li)}
      })'''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<ul %s></ul>%s" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.helper)
