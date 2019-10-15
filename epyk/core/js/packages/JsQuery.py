"""
Wrapper to Jquery module

https://jquery.com/
"""

import json

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage

# All the predefined variable types
from epyk.core.js.fncs import JsFncs


class Jsjqxhr(object):
  def __init__(self, ajax):
    self.__ajax = {'request': ajax}

  def done(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the success callback option, refer to deferred.done() for implementation details

    Documentation
    https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("done", []).extend(jsFncs)
    return self

  def fail(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the error callback option, the .fail() method replaces the deprecated .error() method

    Documentation
    https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("fail", []).extend(jsFncs)
    return self

  def always(self, jsFncs):
    """
    AJAX Function

    An alternative construct to the complete callback option

    Documentation
    https://api.jquery.com/jQuery.ajax/#jqXHR

    :param jsFncs: The Javascript Functions

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__ajax.setdefault("always", []).extend(jsFncs)
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    reqResult = [self.__ajax['request']]
    for rType in ["done", "fail", "always"]:
      if self.__ajax.get(rType) is not None:
        reqResult.append("%s(function(){%s})" % (rType, ";".join(JsUtils.jsConvertFncs(self.__ajax[rType]))))
    return ".".join(map(lambda x: str(x), reqResult))


class JQuery(JsPackage):
  """
  Jquery wrapper.
  for more details about the different available functions go on the website: https://jquery.com/
  In order to avoid conflict with any other libraries the $ will not be used in this framework.
  Any JQuery reference will be done using the proper name of the library jQuery()

  Documentation:
    - https://www.w3schools.com/jquery/
    - https://www.w3schools.com/jquery/jquery_noconflict.asp
    - https://www.w3schools.com/jquery/jquery_ref_ajax.asp

  """
  lib_alias = {"js": 'jquery'}
  lib_selector = 'jQuery("body")'

  def this(self, reference=None):
    """
    Force the selector to be this or a specific reference.
    This feature can be useful in functions

    :param reference: The Jquery reference to be used instead example #MyId

    :return: The Jquery Python object
    """
    if len(self._js) > 0:
      raise Exception("Selector can only be changed first")

    if reference is None:
      self._selector = "jQuery(this)"
    else:
      self._selector = "jQuery('%s')" % reference
    return self

  def new(self, tag=None, reference=None):
    if len(self._js) > 0:
      raise Exception("Selector can only be changed first")

    if tag is None and reference is None:
      raise Exception("Tag or / and Reference must be defined")

    if tag is None and reference is not None:
      self._selector = "jQuery('%s')" % reference
    else:
      if reference is not None:
        self._selector = "jQuery('<%s id=\\'%s\\'></%s>')" % (tag, reference, tag)
      else:
        self._selector = "jQuery('<%s></%s>')" % (tag, tag)
    return self

  def toggle(self, speed=None, easing=None, jsCallback=None):
    """

    :param speed:
    :param easing:
    :param jsCallback:

    :return:
    """
    return self.fnc("toggle()")

  def trigger(self, jsData, jsFnc=None):
    """

    :param jsData:
    :param jsFnc:

    :return:
    """
    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    return self.fnc("trigger(%(jsData)s)" % {"jsData": jsData})

  def hide(self, speed=None, callback=None):
    """

    Documentation:
    https://www.w3schools.com/jquery/jquery_hide_show.asp
    http://api.jquery.com/hide/

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "hide(%(speed)s, function(){%(callback)s})" % {'speed': speed,  'callback': ";".join(callback)}
      else:
        jqFnc = "hide(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "hide()"
    return self.fnc(jqFnc)

  def show(self, speed=None, callback=None):
    """

    Documentation:
    https://www.w3schools.com/jquery/jquery_hide_show.asp
    http://api.jquery.com/show/

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "show(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "show(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "show()"
    return self.fnc(jqFnc)

  def fadeIn(self, speed=None, callback=None):
    """

    Documentation:
    https://www.w3schools.com/jquery/jquery_fade.asp
    http://api.jquery.com/fadein/

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeIn(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeIn(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeIn()"
    return self.fnc(jqFnc)

  def fadeOut(self, speed=None, callback=None):
    """

    Documentation:
    https://www.w3schools.com/jquery/jquery_fade.asp
    http://api.jquery.com/fadeout/

    :param speed:
    :param callback:
    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeOut(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeOut(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeOut()"
    return self.fnc(jqFnc)

  def fadeToggle(self, speed=None, callback=None):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_fade.asp

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeToggle(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeToggle()"
    return self.fnc(jqFnc)

  def fadeTo(self, speed=None, callback=None):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_fade.asp

    :param speed:
    :param jsCallback:
    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "fadeTo(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "fadeTo(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "fadeTo()"
    return self.fnc(jqFnc)

  def slideDown(self, speed=None, callback=None):
    """

    Documentation:
    https://www.w3schools.com/jquery/jquery_slide.asp

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideDown(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideDown(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideDown()"
    return self.fnc(jqFnc)

  def slideUp(self, speed=None, callback=None):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_slide.asp

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideUp(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideUp(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideUp()"
    return self.fnc(jqFnc)

  def slideToggle(self, speed=None, callback=None):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_slide.asp

    :param speed:
    :param callback:

    :return:
    """
    if speed is not None:
      if callback is not None:
        if not isinstance(callback, list):
          callback = [callback]
        jqFnc = "slideToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
      else:
        jqFnc = "slideToggle(%(speed)s)" % {'speed': speed}
    else:
      jqFnc = "slideToggle()"
    return self.fnc(jqFnc)

  def animate(self, params, speed, callback):
    """

    Example
    myObj.animate(0.25, "+=50")

    Documentation
    https://www.w3schools.com/jquery/jquery_animate.asp

    :param params:
    :param speed:
    :param callback:

    :return:
    """
    return self.fnc("animate()")

  def stop(self, stopAll='false', goToEnd='false'):
    """
    Documentation:
      - https://www.w3schools.com/jquery/jquery_stop.asp

    :param stopAll: Javascript.
    :param goToEnd: Javascript.

    :return:
    """
    return self.fnc("stop(%(stopAll)s, %(goToEnd)s)" % {'stopAll': stopAll, 'goToEnd': goToEnd})

  def remove(self):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_dom_remove.asp

    :return:
    """
    return self.fnc("remove()")

  def empty(self):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_dom_remove.asp

    :return:
    """
    return self.fnc("empty()")

  def siblings(self, tag):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_siblings.asp

    :return:
    """
    return self.fnc("siblings()")

  def next(self):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_siblings.asp

    :return:
    """
    return self.fnc("next()")

  def prev(self):
    """

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_siblings.asp

    :return:
    """
    return self.fnc("prev()")

  def first(self):
    """
    The first() method returns the first element of the specified elements.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_filtering.asp

    :return:
    """
    return self.fnc("first()")

  def children(self, filter=None):
    """
    The children() method returns all direct children of the selected element

    Documentation:
      - https://www.w3schools.com/jquery/traversing_children.asp

    :param filter: Optional. Specifies a selector expression to narrow down the search for children
    :return:
    """
    if filter is None:
      return self.fnc("children()")

    return self.fnc("children(%s)" % filter)

  def last(self):
    """
    The last() method returns the last element of the specified element

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_filtering.asp

    :return:
    """
    return self.fnc("last()")

  def appendTo(self, dstJqId, jsFnc=None):
    """

    :param dstJqId:
    :param jsFnc:

    :rtype: str

    :return:
    """
    return self.fnc("appendTo(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, jsFnc)})

  def append(self, dstJqId, jsFnc=None):
    """

    :param dstJqId:
    :param jsFnc:
    :rtype: str

    :return:
    """
    return self.fnc("append(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, jsFnc)})

  def prepend(self, jsData, jsFnc=None):
    """

    :param jsData:
    :param jsFnc:

    :return:
    """
    return self.fnc("prepend(%(data)s)" % {"data": JsUtils.jsConvertData(jsData, jsFnc)})

  def eq(self, i):
    """
    The eq() method returns an element with a specific index number of the selected elements.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_traversing_filtering.asp

    :param i: The index numbers start at 0, so the first element will have the index number 0 and not 1
    :return:
    """
    return self.fnc("eq(%(index)s)" % {'index': i})

  def filter(self):
    """

    :return:
    """

  def _not(self):
    """

    :return:
    """

  def find(self, criteria):
    """

    :return:
    """
    return self.fnc("find('%s')" % criteria)

  def each(self, jsFncs):
    """

    :param jsFncs:

    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return self.fnc("each(function(index, data){%s})" % ";".join(jsFncs))

  def css(self, key, value=None):
    """

    :param key:
    :param value:

    :return:
    """
    self.src.style.css(key, value)
    return self.src

  def attr(self, key, value):
    """

    :param key:
    :param value:

    :return:
    """
    if key.lower() in ["style", 'class']:
      raise Exception("Only the css() function can be used to change the style")

    self.src._attrs[key] = value
    return self.src

  def val(self, jsData=None, jsFnc=None):
    """

    :param jsData:
    :param jsFnc:
    :return:
    """
    if jsData is None:
      self.fnc("val()")

    return self.fnc("val(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def text(self, jsData, jsFnc=None):
    """

    :param jsData:
    :param jsFnc:

    :return:
    """
    if jsData is None:
      return self.fnc("text()")

    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    return self._js.append("text(%s)" % jsData)

  def html(self, jsData=None, jsFnc=None):
    """

    :param jsData:
    :param jsFnc:

    :return:
    """
    if jsData is None:
      return self.fnc("html()")

    return self.fnc("html(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def toggleClass(self, clsName):
    """

    :rtype: str
    :return:
    """
    return self.fnc('toggleClass("%(data)s")' % {'data': clsName})

  def addClass(self, clsName, attrs=None, eventAttrs=None):
    """

    :param clsName:
    :return:
    """
    self.src.style.cssCls(clsName, attrs, eventAttrs, False)
    return self.src

  def getJSON(self, url, jsData, success, dataType='json', jsDataKey=None, isPyData=True, jsFnc=None):
    """
    Load JSON-encoded data from the server using a GET HTTP request.

    Documentation:
    https://api.jquery.com/jQuery.getJSON/#jQuery-getJSON-url-data-success

    :return:
    """
    success = JsUtils.jsConvertFncs(success)
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return Jsjqxhr("jQuery.getJSON('%s', {data: JSON.stringify(%s)}, function(data) {%s}, '%s')" % (url, jsData, ";".join(success), dataType))

  def getJsScript(self, url, jsData, success, dataType='json', jsDataKey=None, isPyData=True, jsFnc=None):
    """
    Load a JavaScript file from the server using a GET HTTP request, then execute it.

    Documentation:
    https://api.jquery.com/jQuery.getScript/

    :param url:
    :param jsData:
    :param success:
    :param dataType:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    :return:
    """
    success = JsUtils.jsConvertFncs(success)
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return Jsjqxhr("jQuery.getScript('%s', {data: JSON.stringify(%s)}, function(data, textStatus, jqxhr) {%s}, '%s')" % (url, jsData, ";".join(success), dataType))

  def getPyScript(self, script, data=None, successFncs=None, options=None, timeout=None, props=None):
    """

    Documentation:
    https://api.jquery.com/jQuery.getJSON/#jQuery-getJSON-url-data-success

    :param script:
    :param jsData:
    :param success:
    :param dataType:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:

    :return:
    """

    if not hasattr(self.src, "aresObj"):
      if not hasattr(self.src, "run"):
        raise Exception("Cannot work without a proper rptObj")

      else:
        rptObj = self.src
    else:
      rptObj = self.src.aresObj
    if data is None:
      data = {}
    qParams = self.getParams('%s/data/%s/%s' % (rptObj._urlsApp['report'], rptObj.run.report_name, script.replace(".py", "")), data, successFncs, None, options, timeout, props)
    return Jsjqxhr("jQuery.post(%s)" % qParams)

  def load(self, url, jsData, successFncs=None):
    """
    Load data from the server and place the returned HTML into the matched elements.

    Documentation
    https://api.jquery.com/load/#load-url-data-complete

    :param url: A string containing the URL to which the request is sent.
    :param jsData: A plain object or string that is sent to the server with the request.
    :param successFncs: A callback function that is executed when the request completes.
    :return:
    """
    if successFncs is None:
      return "%s.load('%s', {data: JSON.stringify(%s)})" % (self.src.jqId, url, jsData)

    return "%s.load('%s', {data: JSON.stringify(%s)}, function(data) {%s})" % (self.src.jqId, url, jsData, successFncs)

  def ajaxError(self, jsFncs):
    """

    Documentation
    https://api.jquery.com/ajaxError/

    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxError(function(event, jqxhr, settings, thrownError) {%s})" % ";".join(jsFncs)

  def ajaxStart(self, jsFncs):
    """
    Register a handler to be called when the first Ajax request begins. This is an Ajax Event.

    Documentation
    https://api.jquery.com/ajaxStart/

    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxStart(function() {%s})" % ";".join(jsFncs)

  def ajaxStop(self, jsFncs):
    """
    Register a handler to be called when all Ajax requests have completed. This is an Ajax Event.

    Documentation
    https://api.jquery.com/ajaxStop/

    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxStop(function() {%s})" % ";".join(jsFncs)

  def ajaxSuccess(self, jsFncs):
    """
    Attach a function to be executed whenever an Ajax request completes successfully. This is an Ajax Event.

    Documentation
    https://api.jquery.com/ajaxSuccess/

    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxSuccess(function(event, xhr, settings) {%s})" % ";".join(jsFncs)

  def ajaxSend(self, jsFncs):
    """

    Documentation
    https://api.jquery.com/ajaxSend/

    :param jsFncs:
    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxSend(function(event, jqxhr, settings) {%s})" % ";".join(jsFncs)

  def ajaxComplete(self, jsFncs):
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return "jQuery(document).ajaxComplete(function() {%s})" % ";".join(jsFncs)

  def getParams(self, url, data, successFncs, errorFncs, options, timeout, props):
    """

    :return:
    """
    ajaxData = []
    if props is not None:
      data["_system"] = props
    if options is not None:
      for k, v in options.items():
        ajaxData.append("%s: %s" % (k, json.dumps(v)))
    ajaxData.extend(["data: {data: JSON.stringify(%s)}" % data, "url: '%s'" % url])
    if timeout is not None:
      ajaxData.append("timeout: %s" % timeout)
    if successFncs is not None:
      ajaxData.append("success: function(result,status,xhr){%s}" % ";".join(JsUtils.jsConvertFncs(successFncs)))
    if errorFncs is not None:
      ajaxData.append("error: function(xhr, status, error){%s}" % ";".join(JsUtils.jsConvertFncs(errorFncs)))
    return "{%s}" % ", ".join(ajaxData)

  def get(self, url, data, successFncs=None, options=None, timeout=None, props=None):
    """
    Load data from the server using a HTTP GET request.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_ajax_get_post.asp

    :return:
    """
    return Jsjqxhr("jQuery.get(%s)" % self.getParams(url, data, successFncs, None, options, timeout, props))

  def post(self, url, data=None, successFncs=None, options=None, timeout=None, props=None):
    """
    Load data from the server using a HTTP POST request.

    Documentation:
      - https://www.w3schools.com/jquery/jquery_ajax_get_post.asp

    :rtype: Jsjqxhr
    :return:
    """
    if data is None:
      data = {}
    return Jsjqxhr("jQuery.post(%s)" % self.getParams(url, data, successFncs, None, options, timeout, props))

  def ajax(self, type, url, data, successFncs=None, errorFncs=None, options=None, timeout=None, props=None):
    """
    The ajax() method is used to perform an AJAX (asynchronous HTTP) request.

    Example


    Documentation:
    https://www.w3schools.com/jquery/ajax_ajax.asp

    :return:
    :param type: Specifies the type of request. (GET or POST)
    :param url: Specifies the URL to send the request to. Default is the current page
    :param data: Specifies data to be sent to the server
    :param successFncs: A function to be run when the request succeeds
    :param errorFncs: A function to run if the request fails.
    :param options: The other parameters specifies one or more name/value pairs for the AJAX request
    :param timeout: The local timeout (in milliseconds) for the request
    :return:
    """
    if type.upper() not in ['POST', 'GET']:
      raise Exception("Method %s not recognised" % url)

    return Jsjqxhr("jQuery.ajax(%s)" % self.getParams(url, data, successFncs, errorFncs, options, timeout, props))

