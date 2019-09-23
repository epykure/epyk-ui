"""
Dom properties

Documentation
- https://www.w3schools.com/jsref/dom_obj_event.asp
- https://www.w3schools.com/jsref/dom_obj_all.asp

"""

from epyk.core.js.fncs import JsFncs

from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsBoolean

from epyk.core.js import JsUtils


class JsDomEvents(object):
  class __internal(object):
    htmlId = None

  def __init__(self, src=None):
    self._src = src if src is not None else self.__internal()
    self._js = []

  def stopPropagation(self):
    """
    The stopPropagation() method prevents propagation of the same event from being called.

    Documentation
    https://www.w3schools.com/jsref/event_stoppropagation.asp

    :return: The Python Dom object
    """
    self._js.append('stopPropagation()')
    return self

  def blur(self, jsFncs):
    """
    FocusEvent

    The event occurs when an element loses focus

    Documentation
    https://www.w3schools.com/jsref/event_onblur.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("blur", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def click(self, jsFncs):
    """
    The event occurs when the user clicks on an element

    Example
    select.label.dom.events.click(rptObj.js.console.log("test"))

    Documentation
    https://www.w3schools.com/jsref/event_onclick.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("click", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def change(self, jsFncs):
    """
    The event occurs when the content of a form element, the selection, or the checked state have changed (for <input>, <select>, and <textarea>)

    Example
    select.dom.events.change(rptObj.js.window.alert("test"))

    Documentation
    https://www.w3schools.com/jsref/event_onchange.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("change", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def dblclick(self, jsFncs):
    """
    The event occurs when the user double-clicks on an element

    Documentation
    https://www.w3schools.com/jsref/event_ondblclick.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("dblclick", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focus(self, jsFncs):
    """
    The event occurs when an element gets focus

    Documentation
    https://www.w3schools.com/jsref/event_onfocusin.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focus", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focusin(self, jsFncs):
    """
    The event occurs when an element is about to get focus

    Documentation
    https://www.w3schools.com/jsref/event_onfocusin.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def focusout(self, jsFncs):
    """
    The event occurs when an element is about to lose focus

    Documentation
    https://www.w3schools.com/jsref/event_onfocusout.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("focusin", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keydown(self, jsFncs):
    """
    The event occurs when the user is pressing a key

    Documentation
    https://www.w3schools.com/jsref/event_onkeydown.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keydown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keypress(self, jsFncs):
    """
    The event occurs when the user presses a key

    Documentation
    https://www.w3schools.com/jsref/event_onkeypress.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keypress", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def keyup(self, jsFncs):
    """
    The event occurs when the user releases a key

    Documentation
    https://www.w3schools.com/jsref/event_onkeyup.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("keyup", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mousedown(self, jsFncs):
    """
    The event occurs when the user presses a mouse button over an element

    Documentation
    https://www.w3schools.com/jsref/event_onmousedown.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseenter(self, jsFncs):
    """
    The event occurs when the pointer is moved onto an element

    Documentation
    https://www.w3schools.com/jsref/event_onmouseenter.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mousedown", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseleave(self, jsFncs):
    """
    The event occurs when the pointer is moved out of an element

    Example
    select.label.dom.events.mouseleave(rptObj.js.console.log("test"))

    Documentation
    https://www.w3schools.com/jsref/event_onmouseleave.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseleave", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseover(self, jsFncs):
    """
    The event occurs when the pointer is moved onto an element, or onto one of its children

    Documentation
    https://www.w3schools.com/jsref/event_onmouseover.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseup(self, jsFncs):
    """
    The event occurs when a user releases a mouse button over an element

    Documentation
    https://www.w3schools.com/jsref/event_onmouseup.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseover", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def mouseout(self, jsFncs):
    """
    The event occurs when a user releases a mouse button over an element

    Documentation
    https://www.w3schools.com/jsref/event_onmouseout.asp

    :param jsFncs: An array of Js functions or string. Or a string with the Js

    :return: The Python Dom object
    """
    self._js.append('addEventListener("mouseout", function(){%s})' % ";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def trigger(self, event, withFocus=True):
    """
    Trigger a javascript event

    Documentation
    https://www.w3schools.com/jsref/met_html_focus.asp
    https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Creating_and_triggering_events

    :param event: The event name
    :param withFocus: Optional, a boolean to define if the focus needs to be set to this component

    :return: The Javascript string of this function
    """
    item = "document.getElementById('%(htmlId)s')" % {'htmlId': self._src.htmlId}
    if withFocus:
      return JsFncs.JsFunction('(function(){var clickEvent = new Event("%(event)s"); %(elem)s.focus(); %(elem)s.dispatchEvent(clickEvent)})()' % {"event": event, "elem": item})

    return JsFncs.JsFunction('(function(){var clickEvent = new Event("%(event)s"); %(elem)s.dispatchEvent(clickEvent)})()' % {"event": event, "elem": item})

  def toStr(self):
    if self._src.htmlId is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._src.htmlId

    strData = "document.getElementById('%(htmlId)s').%(items)s" % {'htmlId': self._src.htmlId, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return strData


class JsDoms(JsObject.JsObject):
  @classmethod
  def new(cls, tagName=None, varName=None, isPyData=True, setVar=True):
    """
    Create a new dom object to be added to the HTML page

    Documentation
    https://www.w3schools.com/jsref/jsref_obj_date.asp

    :param tagName: The tag name to be created
    :param varName: Optional,
    :param isPyData: Optional,
    :return: The Python Javascript Date primitive
    """
    return cls(data="document.createElement('%s')" % tagName, varName=varName, setVar=setVar, isPyData=isPyData)

  def innerText(self, jsString=None):
    """
    The innerText property sets or returns the text content of the specified node, and all its descendants.

    Example
    select.label.dom.innerText("test Change")

    Documentation:
    https://www.w3schools.com/jsref/prop_node_innertext.asp

    :param jsString: Optional, The Javascript String to be added
    :return: THe JsObj
    """
    if jsString is None:
      return "%s.innerText" % self.varId

    self._js.append("%s.innerText = %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    return self

  def innerHTML(self, jsString=None):
    """
    Sets or returns the content of an element

    Example
    select.label.dom.innerHTML("<p style='color:red'>Changed !</p>")

    Documentation:
    https://www.w3schools.com/jsref/prop_html_innerhtml.asp

    :param jsString: Optional, The Javascript String to be added
    :return: THe JsObj
    """
    if jsString is None:
      return "%s.innerHTML" % self.varId

    self._js.append("%s.innerHTML = %s" % (self.varId, JsUtils.jsConvertData(jsString, None)))
    return self

  def attr(self, type, jsObject=None):
    """
    The attr() method adds the specified attribute to an element, and gives it the specified value.
    It will use the underlying setAttribute() method

    Example
    select.label.dom.attr("title", "Tooltip")
    select.label.dom.attr({"title": "Tooltip"})

    Documentation:
    https://www.w3schools.com/jsref/met_element_setattribute.asp

    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set
    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        self._js.append("%s.setAttribute('%s', %s)" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    else:
      self._js.append("%s.setAttribute('%s', %s)" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  def setAttribute(self, attributename, attributevalue):
    """
    The setAttribute() method adds the specified attribute to an element, and gives it the specified value.

    Example
    select.label.dom.setAttribute("title", "Tooltip")

    Documentation
    https://www.w3schools.com/jsref/met_element_setattribute.asp

    :param attributename: Required. The name of the attribute you want to add
    :param attributevalue: Required. The value of the attribute you want to add
    :return:
    """
    self._js.append("%s.setAttribute('%s', %s)" % (self.varId, attributename, JsUtils.jsConvertData(attributevalue, None)))
    return self

  def css(self, type, jsObject=None):
    """
    Replicate in plain Js the Jquery CSS function

    Example
    select.label.dom.css({"color": "red"})

    Documentation:
    https://www.w3schools.com/jsref/met_element_setattribute.asp

    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set
    :return: A JsObj
    """
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        self._js.append("%s.style.%s = %s" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif jsObject is None:
      return JsObject.JsObject("%s.style.%s" % (self.varId, type))
    else:
      self._js.append("%s.style.%s = %s" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return self

  @property
  def firstChild(self):
    """
    The firstChild property returns the first child node of the specified node, as a Node object.

    Example
    select.dom.firstChild
    select.dom.firstChild.css({"color": "yellow"})

    Documentation
    https://www.w3schools.com/jsref/prop_node_firstchild.asp

    :return: A new JsDom python object
    """
    return JsDoms("%s.firstChild" % self.varId)

  def contains(self, node):
    """
    The contains() method returns a Boolean value indicating whether a node is a descendant of a specified node.

    Documentation
    https://www.w3schools.com/jsref/met_node_contains.asp

    :param node: Required. Specifies the node that may be contained by (a descendant of) a specified node
    :return: A Boolean
    """
    return JsBoolean.JsBoolean('%s.contains(%s)' % (self.varId, node))

  def getAttribute(self, attributename):
    """
    The getAttribute() method returns the value of the attribute with the specified name, of an element.

    Example
    select.dom.getAttribute("class")

    Documentation
    https://www.w3schools.com/jsref/met_element_getattribute.asp

    :param attributename: Required. The name of the attribute you want to get the value from
    :return: A String, representing the specified attribute's value.
    """
    return JsString.JsString("%s.getAttribute(%s)" % (self.varId, JsUtils.jsConvertData(attributename, None)), isPyData=False)

  def getAttributeNode(self, attributename):
    """
    The getAttributeNode() method returns the attribute node with the specified name of an element, as an Attr object.

    Documentation
    https://www.w3schools.com/jsref/met_element_getattributenode.asp

    :param attributename: Required. The name of the attribute you want to return
    :return: An Attr object, representing the specified attribute node.
    """
    return JsString.JsString("%s.getAttributeNode('%s')" % (self.varId, attributename), isPyData=False)

  @property
  def hasChildNodes(self):
    """
    Returns true if an element has any child nodes, otherwise false

    Example
    select.dom.hasChildNodes

    Documentation
    https://www.w3schools.com/jsref/met_node_haschildnodes.asp

    :return: A Boolean, returns true if the node has child nodes, false otherwise
    """
    return JsBoolean.JsBoolean("%s.hasChildNodes()" % self.varId, isPyData=False)

  def text(self, jsString):
    """
    Javascript Function

    Shortcut in charge oa creating a text node object and adding the text.

    Documentation

    :param jsString: The Javascript String of the text node component
    :return: The main Python Dom Object
    """
    return self.appendChild("document.createTextNode(%s)" % JsUtils.jsConvertData(jsString, None))



  @property
  def childNodes(self):
    """
    The childNodes property returns a collection of a node's child nodes, as a NodeList object.

    The nodes in the collection are sorted as they appear in the source code and can be accessed by index numbers. The index starts at 0.

    Documentation:
      - https://www.w3schools.com/jsref/prop_node_childnodes.asp

    :return: A NodeList object, representing a collection of nodes. The nodes in the returned collection are sorted as they appear in the source code
    """
    self._js.append("%s.childNodes" % self.varId)
    return self

  @property
  def tagName(self):
    """
    The tagName property returns the tag name of the element

    Example
    select.dom.tagName

    Documentation:
    https://www.w3schools.com/jsref/prop_element_tagname.asp

    :return: A String, representing the tag name of the element in uppercase
    """
    return JsString.JsString("%s.tagName" % self.varId, isPyData=False)

  def className(self, className=None):
    """
    The className property sets or returns the class name of an element (the value of an element's class attribute).

    Example
    select.dom.className()

    Documentation:
    https://www.w3schools.com/jsref/prop_html_classname.asp

    :param className: Specifies the class name of an element. To apply multiple classes, separate them with spaces, like "test demo"
    :return: A String, representing the class, or a space-separated list of classes, of an element
    """
    if className is None:
      return JsString.JsString("%s.className" % self.varId, isPyData=False)

    return JsString.JsString("%s.className = %s" % (self.varId, JsUtils.jsConvertData(className, None)), isPyData=False)

  def cloneNode(self, deep=True):
    """
    The cloneNode() method creates a copy of a node, and returns the clone.

    The cloneNode() method clones all attributes and their values.

    Example
    select.dom.cloneNode()

    Documentation:
    https://www.w3schools.com/jsref/met_node_clonenode.asp

    :param deep: Optional. Specifies whether all descendants of the node should be cloned.
    :return: A Node object, representing the cloned node
    """
    return JsDoms("%s.cloneNode(%s)" % (self.varId, JsUtils.jsConvertData(deep, None)))

  def remove(self):
    """
    Remove the current dom object from the page

    Example
    select.dom.remove()

    Documentation
    https://developer.mozilla.org/fr/docs/Web/API/ChildNode/remove

    :return:
    """
    return JsFncs.JsFunction("%s.remove()" % self.varId)

  def removeChild(self, jsDom):
    """
    Removes a child node from an element

    Documentation
    https://www.w3schools.com/jsref/met_node_removechild.asp

    :param jsDom: Required. The node object you want to remove
    :return: A Node object, representing the removed node, or null if the node does not exist
    """
    return JsDoms("%s.removeChild(%s)" % (self.varId, jsDom))

  def appendChild(self, jsDom):
    """
    The appendChild() method appends a node as the last child of a node.

    Example
    select.dom.appendChild(select.label.dom.cloneNode())

    Documentation:
    https://www.w3schools.com/jsref/met_node_appendchild.asp

    :param jsDom: Required. The node object you want to append
    :return: 	A Node Object, representing the appended node
    """
    self._js.append("%s.appendChild(%s)" % (self.varId, JsUtils.jsConvertData(jsDom, None)))
    return self

  def insertBefore(self, newnode, existingnode=None):
    """
    The insertBefore() method inserts a node as a child, right before an existing child, which you specify.

    Example
    select.dom.insertBefore(select.label.dom.cloneNode())

    Documentation
    https://www.w3schools.com/jsref/met_node_insertbefore.asp

    :param newnode: Required. The node object you want to insert
    :param existingnode: Optional. The child node you want to insert the new node before. If set to null, the insertBefore method will insert the newnode at the end
    :return:
    """
    if existingnode is None:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, newnode, self.firstChild))
    else:
      self._js.append("%s.insertBefore(%s, %s)" % (self.varId, newnode, existingnode))
    return self

  def click(self, jsFnc):
    """

    :param jsFnc:
    :return:
    """
    self._js.append("%s.click(%s)" % (self.varId, JsUtils.jsConvertFncs(jsFnc)))
    return self

  def onclick(self, jsFncs, autoStyle=True):
    """
    Execute a JavaScript when a button is clicked

    Documentation
    https://www.w3schools.com/jsref/event_onclick.asp

    :param jsFnc: The Javascript function
    :param autoStyle: Some predefined style attributes added to this event (self.css({"cursor": "pointer"}))
    :return: The PyDom object
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if autoStyle:
      self.css({"cursor": "pointer"})
    self._js.append("%s.onclick = function(){%s}" % (self.varId, ";".join([str(JsUtils.jsConvertData(jsFnc, None)) for jsFnc in jsFncs])))
    return self
