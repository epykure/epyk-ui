#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html import Defaults

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsQuery

from epyk.core.html.options import OptTrees

from epyk.core.css.styles import GrpClsList


class Tree(Html.Html):
  name = 'List Expandable'
  requirements = ('font-awesome', )

  def __init__(self, report, records, color, width, height, htmlCode, helper, option, profile):
    super(Tree, self).__init__(report, records, css_attrs={"width": width, 'height': height})
    option['is_root'] = True
    option['icon_open'] = "fas fa-folder-open"
    option['style'] = {"list-style": 'none', 'margin-left': '8px', 'padding-left': 0}
    self.__options = OptTrees.OptionsTree(self, option)
    self.css(option['style'])
    self._jsStyles['click_node'] = None

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptTrees.OptionsTree
    """
    return self.__options

  @property
  def _js__builder__(self):
    return ''' if(options){htmlObj.innerHTML = ''; options.is_root = false};
      data.forEach(function(item, i){
        var li = document.createElement("li");
        var a = document.createElement("a");
        if(typeof item.items !== 'undefined'){
          var ul = document.createElement("ul"); 
          for(const attr in options.style){ul.style[attr] = options.style[attr]};
          %(builder)s(ul, item.items, options);
          var icon = document.createElement("i"); icon.style.marginRight = '5px';
          icon.onclick = function(){ 
            var ulDisplay = this.parentNode.querySelector('ul').style.display;
            if(ulDisplay == 'none'){ this.parentNode.querySelector('ul').style.display = 'block'}
            else{this.parentNode.querySelector('ul').style.display = 'none'}
          };

          options.icon_open.split(" ").forEach(function(s){icon.classList.add(s)});
          var span = document.createElement("span"); 
          span.innerHTML = item.value;
          a.appendChild(icon); a.appendChild(span); a.appendChild(ul);
        } else {
          a.innerHTML = item.value;
          a.style.paddingLeft = '18px';
        }
       
        li.appendChild(a);
        htmlObj.appendChild(li)
      })''' % {"builder": self.builder_name}

  def clickNode(self, jsFncs, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    if not isinstance(jsFncs, list):
      jsFncs = []

    self._jsStyles['click_node'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param source_event: String. The JavaScript DOM source for the event (can be a sug item)
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._jsStyles['click_leaf'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<ul %s></ul>' % self.get_attrs(pyClassNames=self.style.get_classes())


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
        sub_l = self._report.ui.list()
        sub_l.options.managed = False
        ul.add_item(sub_l)[-1].no_decoration
        ul[-1].add_label(l['label'], css={"color": l.get('color', 'none')})
        ul[-1].add_icon(self.options.icon_open if self.options.expanded else self.options.icon_close)
        if not self.options.expanded:
          sub_l.css({"display": 'none'})
        ul[-1].icon.click([
          ul[-1].val.dom.toggle(),
          ul[-1].icon.dom.switchClass(self.options.icon_close.split(" ")[-1], self.options.icon_open.split(" ")[-1])])
        self.set(sub_l, l.get('items'))
      else:
        ul.add_item(self._report.ui.text(l['label']).editable().css({"width": 'none', 'min-width': 'none'}))[-1].no_decoration
        ul[-1].css({"color": l.get('color', 'none')})
    return self


class DropDown(Html.Html):
  requirements = ('bootstrap', 'jquery')
  name = 'DropDown Select'

  def __init__(self, report, data, text, width, height, htmlCode, helper, options, profile):
    self.__options = {}
    super(DropDown, self).__init__(report, text, htmlCode=htmlCode, profile=profile, css_attrs={"width": width, "height": height})
    self._vals, self.text = data, text
    self.css({'padding': 0, 'margin': "1px", "display": "block", "z-index": 10, 'cursor': 'pointer', 'position': 'relative'})
    self._jsStyles = {"a": {'text-decoration': 'none', 'line-height': '%spx' % Defaults.LINE_HEIGHT, 'padding': '0 10px', "width": '%spx' % options.get("width")},
                      "ul": {"left": "%spx" % options.get("width")}}
    self.__options = OptTrees.OptDropDown(self, options)

  @property
  def style(self):
    """
    Description:
    -----------

    :rtype: GrpClsList.ClassDropDown
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassDropDown(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    -----------
    Property to set all the possible object for a dropdown

    :rtype: OptTrees.OptDropDown
    """
    return self.__options

  def click(self, jsFncs, profile=False, source_event=None, onReady=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs: List of Js Functions. A Javascript Python function
    :param profile: A Boolean. Set to true to get the profile for the function on the Javascript console.
    :param source_event: A String. Optional. The source target for the event.
    :param onReady: Boolean. Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(jsFncs, list):
      jsFncs = []
    self._jsStyles['click'] = "function(event, value){%s} " % JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return self

  @property
  def _js__builder__(self):
    return ''' 
      var jqHtmlObj = %(jqId)s; if(options.clearDropDown){jqHtmlObj.empty()};
      data.forEach(function(rec){
        if (rec.items != undefined) {
          var li = $('<li class="dropdown" style="list-style-type:none;display:list-item;text-align:-webkit-match-parent"></li>'); var a = $('<a tabindex=-1>'+ rec.value +'<span class="caret"></span></a>');
          li.append(a); var ul = $('<ul class="submenu"></ul>'); ul.css(options.ul); options.clearDropDown = false; a.css(options.a);
          %(pyCls)s(ul, rec.items, options); li.append(ul); jqHtmlObj.append(li);
        } else {
          if (rec.url == undefined){var a = $('<a href="#">'+ rec.value +'</a>')}
          else {var a = $('<a href="'+ rec.url +'">'+ rec.value +'</a>')}; a.css(options.a);
          a.click(function(event){const value = a.html(); options.click(event, value)} );
          var li = $('<li style="list-style-type:none;display:list-item;text-align:-webkit-match-parent"></li>'); li.append(a); jqHtmlObj.append(li)}
      })''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False), "pyCls": self.__class__.__name__}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<ul %s></ul>" % (self.get_attrs(pyClassNames=self.style.get_classes()))
