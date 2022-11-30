#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class JsHtmlTree(JsHtml.JsHtmlRich):

  def hide(self, i: int = None):
    """ Hide the node for a given index.
    If no index defined all tree will be collapsed.

    TODO: Extend this for tree with multiple dimensions.

    :param i: Optional. The item index in the tree
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
    """ Expand a specific node in the tree.

    If no index defined it will expand the entire tree.

    TODO: Extend this for tree with multiple dimensions.

    :param i: Optional. The item index in the tree
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
    """ Copy the tree data to clipboard
    """
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

  def current_path(self):
    """ Get the path of the selected item in the tree

    Usage::

      hyr = page.ui.tree(data)
      hyr.click([page.js.alert(hyr.dom.current_path())])
    """
    return JsObjects.JsArray.JsArray.get('''
(function(src, parentCode){
let childParentNode = src.parentNode; let childPath = []; childPath.push(src.outerText);
  while (childParentNode.id != parentCode){
    childParentNode = childParentNode.parentNode;
    if (childParentNode.hasAttribute('data-parent')){
      childPath.push(childParentNode.getAttribute('data-parent'))
    };
  }; return childPath; })(event.srcElement, '%s')''' % self.component.html_code)

  def active(self):
    return JsObjects.JsArray.JsArray.get('''
    (function(src, parentCode){
    let childParentNode = src.parentNode; let childPath = []; childPath.push(src.outerText);
      while (childParentNode.id != parentCode){
        childParentNode = childParentNode.parentNode;
        if (childParentNode.hasAttribute('data-parent')){
          childPath.push(childParentNode.getAttribute('data-parent'))
        };
      }; return childPath; })(event.srcElement, '%s')''' % self.component.html_code)
