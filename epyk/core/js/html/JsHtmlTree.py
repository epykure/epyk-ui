#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsNodeDom


class JsHtmlTree(JsHtml.JsHtmlRich):

  def hide(self, i: int = None):
    """

    TODO: Extend this for tree with multiple dimensions.

    :param i: Optional. The item index in the tree.
    """
    if i is not None:
      return JsObjects.JsVoid('''
let treeItem = document.querySelectorAll("#%(htmlCode)s i[name=item_arrow]")[%(index)s];
if (treeItem.getAttribute("class") == "%(iconOpen)s"){dom.click();}
''' % {"htmlCode": self.component.html_code, "iconOpen": self.component.options.icon_open, "index": i})

    return JsObjects.JsVoid('''
document.querySelectorAll("#%(htmlCode)s i[name=item_arrow]").forEach( function(dom, k){
  if(dom.getAttribute("class") == "%(iconOpen)s"){dom.click();}
})''' % {"htmlCode": self.component.html_code, "iconOpen": self.component.options.icon_open})

  def expand(self, i: int = None):
    """

    TODO: Extend this for tree with multiple dimensions.

    :param i: Optional. The item index in the tree.
    """
    if i is not None:
      return JsObjects.JsVoid('''
let treeItem = document.querySelectorAll("#%(htmlCode)s i[name=item_arrow]")[%(index)s];
if (treeItem.getAttribute("class") == "%(iconClose)s"){dom.click();}
''' % {"htmlCode": self.component.html_code, "iconClose": self.component.options.icon_close, "index": i})
    return JsObjects.JsVoid('''
document.querySelectorAll("#%(htmlCode)s i[name=item_arrow]").forEach( function(dom, k){
   if(dom.getAttribute("class") == "%(iconClose)s"){dom.click();}
})
''' % {"htmlCode": self.component.html_code, "iconClose": self.component.options.icon_close})

  def copy(self):
    return JsObjects.JsVoid('''
let treeData = {}; var curBranch = [];
document.querySelectorAll("#%(htmlCode)s span[name=item_value]").forEach( function(dom, k){
  let nodeDepth = parseInt(dom.parentNode.parentNode.parentNode.getAttribute("data-depth"))-1;
  let nodeParent = dom.parentNode.parentNode.parentNode.getAttribute("data-parent");
  let childNodes = dom.parentNode.querySelector("ul");
  if (nodeDepth < curBranch.length){
    curBranch = curBranch.slice(0, nodeDepth)}
  if(childNodes){
    if(nodeParent){
      var curNode = treeData;
      curBranch.forEach(function(node){curNode = curNode[node]})
      curNode[dom.innerHTML] = {} 
      curBranch.push(dom.innerHTML)
    }
    else{
      treeData[dom.innerHTML] = {} 
      curBranch = [dom.innerHTML]}
  } else {
    var curNode = treeData;
    curBranch.forEach(function(node){curNode = curNode[node]})
    curNode[dom.innerHTML] = {} 
    curNode[dom.innerHTML] = dom.innerHTML
  }
})
var dummy = document.createElement("textarea");
document.body.appendChild(dummy);
dummy.value = JSON.stringify(treeData);
dummy.select();
document.execCommand("copy");
document.body.removeChild(dummy);
''' % {"htmlCode": self.component.html_code})
