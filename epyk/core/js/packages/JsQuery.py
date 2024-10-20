import json
import sys

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsString
from epyk.core.py import types
from epyk.core.js.packages import JsPackage
from typing import Optional, Union, List

# All the predefined variable types
from epyk.core.js.fncs import JsFncs

JQUERY_ALIAS = "$"


def decorate_var(var_name: str, convert_var: bool = True):
    """
    Return the String Jquery variable reference for a given component id.

    :param var_name: The variable name
    :param convert_var:

    :return: The decorated Jquery reference
    """
    if not convert_var:
        return '%s(%s)' % (JQUERY_ALIAS, var_name)

    return '%s(%s)' % (JQUERY_ALIAS, JsUtils.jsConvertData(var_name, None))


class Jsjqxhr:

    def __init__(self, ajax):
        self.__ajax = {'request': ajax}
        self.profile = False

    def done(self, js_funcs):
        """AJAX Function.

        An alternative construct to the success callback option, refer to deferred.done() for implementation details

        `jQuery <https://api.jquery.com/jQuery.ajax/#jqXHR>`_

        :param js_funcs: The Javascript Functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__ajax.setdefault("done", []).extend(js_funcs)
        return self

    def fail(self, js_funcs):
        """AJAX Function.

        An alternative construct to the error callback option, the .fail() method replaces the deprecated .error()
        method.

        `jQuery <https://api.jquery.com/jQuery.ajax/#jqXHR>`_

        :param js_funcs: The Javascript Functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__ajax.setdefault("fail", []).extend(js_funcs)
        return self

    def always(self, js_funcs):
        """AJAX Function.

        An alternative construct to the complete callback option.

        `jQuery <https://api.jquery.com/jQuery.ajax/#jqXHR>`_

        :param js_funcs: The Javascript Functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__ajax.setdefault("always", []).extend(js_funcs)
        return self

    def toStr(self):
        """Javascript representation

        :return: Return the Javascript String
        """
        reqResult = [self.__ajax['request']]
        for rType in ["done", "fail", "always"]:
            if self.__ajax.get(rType) is not None:
                reqResult.append("%s(function(){%s})" % (
                    rType, JsUtils.jsConvertFncs(self.__ajax[rType], toStr=True, profile=self.profile)))
        return ".".join(map(lambda x: str(x), reqResult))


class Deferred:

    def __init__(self, beforeStart):
        self.__ajax = {'beforeStart': beforeStart}
        self.profile = False
        self.__pmts = []
        self.__order = []

    @property
    def pmts(self) -> List[str]:
        return self.__pmts

    @pmts.setter
    def pmts(self, values: List[str]):
        self.__pmts = values

    def func(self, name: str, js_funcs):
        """

        :param name:
        :param js_funcs: The Javascript Functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__ajax.setdefault(name, []).extend(js_funcs)
        self.__order.append(name)
        return self

    def always(self, js_funcs):
        """Add handlers to be called when the Deferred object is either resolved or rejected.

        `jQuery <https://api.jquery.com/deferred.always/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def catch(self, js_funcs):
        """Add handlers to be called when the Deferred object is rejected.

        `jQuery <https://api.jquery.com/deferred.catch/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def done(self, js_funcs):
        """Add handlers to be called when the Deferred object is resolved.

        `jQuery <https://api.jquery.com/deferred.done/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def fail(self, js_funcs):
        """Add handlers to be called when the Deferred object is rejected.

        `jQuery <https://api.jquery.com/deferred.fail/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def pipe(self, js_funcs):
        """Utility method to filter and/or chain Deferreds.

        `jQuery <https://api.jquery.com/deferred.pipe/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def progress(self, js_funcs):
        """Add handlers to be called when the Deferred object generates progress notifications.

        `jQuery <https://api.jquery.com/deferred.progress/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def promise(self, js_funcs):
        """Return a Deferred’s Promise object.

        `jQuery <https://api.jquery.com/deferred.promise/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def reject(self, js_funcs):
        """Reject a Deferred object and call any failCallbacks with the given args.

        `jQuery <https://api.jquery.com/deferred.reject/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def rejectWith(self, js_funcs):
        """Reject a Deferred object and call any failCallbacks with the given context and args.

        `jQuery <https://api.jquery.com/deferred.rejectWith/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def resolve(self, **kwargs):
        """Resolve a Deferred object and call any doneCallbacks with the given args.

        `jQuery <https://api.jquery.com/deferred.resolve/>`_

        :param kwargs: Optional arguments that are passed to the doneCallbacks.
        """
        if not kwargs:
            return JsUtils.jsWrap("%s.resolve()")

        # kwargs must be linked to pmts values
        args = []
        for k in self.__pmts:
            args.append(JsUtils.jsConvertData(kwargs.get(k), None))
        return JsUtils.jsWrap("%s.resolve(%s)" % (", ".join(args)))

    def resolveWith(self, js_funcs):
        """Resolve a Deferred object and call any doneCallbacks with the given context and args.

        `jQuery <https://api.jquery.com/deferred.resolveWith/>`_

        :param js_funcs: The Javascript Functions
        """
        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs)

    def state(self, js_funcs):
        """Determine the current state of a Deferred object.

        `jQuery <https://api.jquery.com/deferred.state/>`_

        :param js_funcs: The Javascript Functions
        """
        return JsString.JsString.get("%s.state()")

    def then(self, js_funcs_success, js_funcs_error = None):
        """Add handlers to be called when the Deferred object is resolved, rejected, or still in progress.

        `jQuery <https://api.jquery.com/deferred.then/>`_

        :param js_funcs_success: The Javascript Functions
        :param js_funcs_error: The Javascript Functions
        """
        if not js_funcs_error:
            ...
            return

        return self.func(sys._getframe().f_back.f_code.co_name, js_funcs_success)


class JQuery(JsPackage):
    """Jquery wrapper.
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

    def this(self, reference: str = None):
        """Force the selector to be this or a specific reference.
        This feature can be useful in functions.

        :param reference: The Jquery reference to be used instead example #MyId

        :return: The Jquery Python object
        """
        if len(self._js) > 0:
            raise ValueError("Selector can only be changed first")

        if reference is None:
            self._selector = "jQuery(this)"
        else:
            self._selector = "jQuery('%s')" % reference
        return self

    def new(self, tag=None, reference: str = None):
        """

        :param tag:
        :param reference:
        """
        if len(self._js) > 0:
            raise ValueError("Selector can only be changed first")

        if tag is None and reference is None:
            raise ValueError("Tag or / and Reference must be defined")

        if tag is None and reference is not None:
            self._selector = "jQuery('%s')" % reference
        else:
            if reference is not None:
                self._selector = "jQuery('<%s id=\\'%s\\'></%s>')" % (tag, reference, tag)
            else:
                self._selector = "jQuery('<%s></%s>')" % (tag, tag)
        return self

    def parseHTML(self, text, context=None, keepScripts: bool = False):
        """Parses a string into an array of DOM nodes.

        `jQuery <https://api.jquery.com/jquery.parsehtml/>`_

        :param text: HTML String to be parsed
        :param context: Document element to serve as the context in which the HTML fragment will be created
        :param keepScripts: A Boolean indicating whether to include scripts passed in the HTML string
        """
        text = JsUtils.jsConvertData(text, None)
        return "%s.parseHTML(%s)" % (JQUERY_ALIAS, text)

    def toggle(self, speed=None, easing=None, callback=None):
        """

        :param speed:
        :param easing:
        :param callback:
        """
        return self.fnc("toggle()")

    def trigger(self, data: types.JS_DATA_TYPES, js_func: types.JS_FUNCS_TYPES = None):
        """Execute all handlers and behaviors attached to the matched elements for the given event type.

        `jQuery <https://api.jquery.com/trigger/>`_

        :param data:
        :param js_func: Javascript functions.
        """
        data = JsUtils.jsConvertData(data, js_func)
        return self.fnc("trigger(%(data)s)" % {"data": data})

    def hide(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Hide the matched elements.

        `w3schools <https//www.w3schools.com/jquery/jquery_hide_show.asp>`_
        `jQuery <http://api.jquery.com/hide/>`_

        :param speed:
        :param callback: Javascript functions.
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "hide(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
            else:
                jq_func = "hide(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "hide()"
        return self.fnc(jq_func)

    def show(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Display the matched elements.

        `w3schools <https//www.w3schools.com/jquery/jquery_hide_show.asp>`_
        `jQuery <http://api.jquery.com/show/>`_

        :param speed:
        :param callback: Javascript functions.
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "show(%(speed)s, function(){%(callback)s})" % {'speed': speed, 'callback': ";".join(callback)}
            else:
                jq_func = "show(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "show()"
        return self.fnc(jq_func)

    def fadeIn(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Display the matched elements by fading them to opaque.

        `w3schools <https//www.w3schools.com/jquery/jquery_fade.asp>`_
        `jQuery <http://api.jquery.com/fadein/>`_

        :param speed:
        :param callback:
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "fadeIn(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                           'callback': ";".join(callback)}
            else:
                jq_func = "fadeIn(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "fadeIn()"
        return self.fnc(jq_func)

    def fadeOut(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Hide the matched elements by fading them to transparent.

        `w3schools <https//www.w3schools.com/jquery/jquery_fade.asp>`_
        `jquery <http://api.jquery.com/fadeout/>`_

        :param speed:
        :param callback: Javascript functions.
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "fadeOut(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                            'callback': ";".join(callback)}
            else:
                jq_func = "fadeOut(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "fadeOut()"
        return self.fnc(jq_func)

    def fadeToggle(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Display or hide the matched elements by animating their opacity.

        `jquery <https://www.w3schools.com/jquery/jquery_fade.asp>`_

        :param speed:
        :param callback: Javascript functions.
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "fadeToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                               'callback': ";".join(callback)}
            else:
                jq_func = "fadeToggle(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "fadeToggle()"
        return self.fnc(jq_func)

    def fadeTo(self, duration, opacity, easing=None, complete=None):
        """Adjust the opacity of the matched elements.

        `w3schools <https//www.w3schools.com/jquery/jquery_fade.asp>`_
        `jquery <https://api.jquery.com/fadeto/>`_

        :param duration: A string or number determining how long the animation will run.
        :param opacity: A number between 0 and 1 denoting the target opacity.
        :param easing: A string indicating which easing function to use for the transition.
        :param complete: A function to call once the animation is complete.
        """
        if complete is not None:
            if not isinstance(complete, list):
                complete = [complete]
            complete = "function(){%s}" % ";".join(complete)
        if easing is not None:
            if complete is not None:
                jq_func = "fadeTo(%(speed)s, %(opacity)s, %(easing)s, %(callback)s)" % {
                    'speed': duration, 'opacity': opacity, 'easing': easing, 'callback': complete}
            else:
                jq_func = "fadeTo(%(speed)s, %(opacity)s, %(easing)s)" % {
                    'speed': duration, 'opacity': opacity, 'easing': easing}
        elif complete is not None:
            jq_func = "fadeTo(%(speed)s, %(opacity)s, %(complete)s)" % {
                'speed': duration, 'opacity': opacity, 'complete': complete}
        else:
            jq_func = "fadeTo(%(speed)s, %(opacity)s)" % {'speed': duration, 'opacity': opacity}
        return self.fnc(jq_func)

    def slideDown(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Display the matched elements with a sliding motion.

        `w3schools <https//www.w3schools.com/jquery/jquery_slide.asp>`_
        `jquery <https://api.jquery.com/slideDown/#slideDown-duration-complete>`_

        :param speed: A string or number determining how long the animation will run.
        :param callback: A string indicating which easing function to use for the transition.
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "slideDown(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                              'callback': ";".join(callback)}
            else:
                jq_func = "slideDown(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "slideDown()"
        return self.fnc(jq_func)

    def slideUp(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Hide the matched elements with a sliding motion.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_slide.asp
          https://api.jquery.com/slideUp/#slideUp-duration-complete

        :param speed: A string or number determining how long the animation will run.
        :param callback: A function to call once the animation is complete, called once per matched element
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "slideUp(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                            'callback': ";".join(callback)}
            else:
                jq_func = "slideUp(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "slideUp()"
        return self.fnc(jq_func)

    def slideToggle(self, speed: int = None, callback: types.JS_FUNCS_TYPES = None):
        """Display or hide the matched elements with a sliding motion.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_slide.asp
          https://api.jquery.com/slideToggle/#slideToggle-duration-complete

        :param speed: A string or number determining how long the animation will run
        :param callback: A function to call once the animation is complete, called once per matched element
        """
        if speed is not None:
            if callback is not None:
                if not isinstance(callback, list):
                    callback = [callback]
                jq_func = "slideToggle(%(speed)s, function(){%(callback)s})" % {'speed': speed,
                                                                                'callback': ";".join(callback)}
            else:
                jq_func = "slideToggle(%(speed)s)" % {'speed': speed}
        else:
            jq_func = "slideToggle()"
        return self.fnc(jq_func)

    def animate(self, params, speed: int = 400, easing: str = 'swing', callback: types.JS_FUNCS_TYPES = None):
        """Perform a custom animation of a set of CSS properties.

        Usage::

          myObj.animate(0.25, "+=50")

        Related Pages:

          https://www.w3schools.com/jquery/jquery_animate.asp
          https://api.jquery.com/animate/#animate-properties-duration-easing-complete

        :param params: An object of CSS properties and values that the animation will move toward
        :param speed: A string or number determining how long the animation will run
        :param easing: A string indicating which easing function to use for the transition
        :param callback: A function to call once the animation is complete, called once per matched element
        """
        easing = JsUtils.jsConvertData(easing, None)
        if callback is not None:
            return self.fnc("animate(%s, %s, %s, %s)" % (params, speed, easing, callback))

        return self.fnc("animate(%s, %s, %s)" % (params, speed, easing))

    def stop(self, stop_all: bool = False, go_to_end: bool = False):
        """Stop the currently-running animation on the matched elements.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_stop.asp
          https://api.jquery.com/stop/#stop-clearQueue-jumpToEnd

        :param stop_all: A Boolean indicating whether to remove queued animation as well
        :param go_to_end: A Boolean indicating whether to complete the current animation immediately
        """
        stop_all = JsUtils.jsConvertData(stop_all, None)
        go_to_end = JsUtils.jsConvertData(go_to_end, None)
        return self.fnc("stop(%(stopAll)s, %(goToEnd)s)" % {'stopAll': stop_all, 'goToEnd': go_to_end})

    def remove(self, selector=None):
        """Remove the set of matched elements from the DOM.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_dom_remove.asp
          https://api.jquery.com/remove/#remove-selector

        :param selector: A selector expression that filters the set of matched elements to be removed
        """
        if selector is not None:
            selector = JsUtils.jsConvertData(selector, None)
            return self.fnc("remove(%s)" % selector)

        return self.fnc("remove()")

    def empty(self):
        """Remove all child nodes of the set of matched elements from the DOM.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_dom_remove.asp
          https://api.jquery.com/empty/#empty
        """
        return self.fnc("empty()")

    def siblings(self, selector: types.JS_DATA_TYPES = None):
        """Get the siblings of each element in the set of matched elements, optionally filtered by a selector.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
          https://api.jquery.com/siblings/#siblings-selector

        :param selector: A string containing a selector expression to match elements against
        """
        if selector is not None:
            selector = JsUtils.jsConvertData(selector, None)
            return self.fnc("siblings(%s)" % selector)

        return self.fnc("siblings()")

    def next(self, selector: types.JS_DATA_TYPES = None):
        """Get the immediately following sibling of each element in the set of matched elements.
        If a selector is provided, it retrieves the next sibling only if it matches that selector.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
          https://api.jquery.com/next/#next-selector

        :param selector: A string containing a selector expression to match elements against
        """
        if selector is not None:
            selector = JsUtils.jsConvertData(selector, None)
            return self.fnc("next(%s)" % selector)

        return self.fnc("next()")

    def prev(self, selector: types.JS_DATA_TYPES = None):
        """Get the immediately preceding sibling of each element in the set of matched elements.
        If a selector is provided, it retrieves the previous sibling only if it matches that selector.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_traversing_siblings.asp
          https://api.jquery.com/prev/#prev-selector

        :param selector: A string containing a selector expression to match elements against
        """
        if selector is not None:
            selector = JsUtils.jsConvertData(selector, None)
            return self.fnc("prev(%s)" % selector)

        return self.fnc("prev()")

    def first(self):
        """The first() method returns the first element of the specified elements.

        Related Pages:

          https//www.w3schools.com/jquery/jquery_traversing_filtering.asp
          https://api.jquery.com/first/#first
        """
        return self.fnc("first()")

    def children(self, selector: types.JS_DATA_TYPES = None):
        """The children() method returns all direct children of the selected element

        `jquery <https//www.w3schools.com/jquery/traversing_children.asp>`_

        :param selector: Optional. Specifies a selector expression to narrow down the search for children
        """
        if selector is None:
            return self.fnc("children()")

        return self.fnc("children(%s)" % selector)

    def last(self):
        """The last() method returns the last element of the specified element.

        `w3schools <https//www.w3schools.com/jquery/jquery_traversing_filtering.asp>`_
        """
        return self.fnc("last()")

    def appendTo(self, dstJqId, js_func: types.JS_FUNCS_TYPES = None):
        """Insert every element in the set of matched elements to the end of the target.

        `jquery <ttps://api.jquery.com/appendTo/>`_

        :param dstJqId: A selector, element, HTML string, array of elements, or jQuery object; the matched set of
          elements will be inserted at the end of the element(s) specified by this parameter.
        :param js_func:
        """
        return self.fnc("appendTo(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, js_func)})

    def append(self, dstJqId, js_func: types.JS_FUNCS_TYPES = None):
        """Insert content, specified by the parameter, to the end of each element in the set of matched elements.

        `jquery <https://api.jquery.com/append/>`_

        :param dstJqId:
        :param js_func:
        """
        return self.fnc("append(%(dstJqId)s)" % {'dstJqId': JsUtils.jsConvertData(dstJqId, js_func)})

    def prepend(self, data, js_func: types.JS_FUNCS_TYPES = None):
        """Insert content, specified by the parameter, to the beginning of each element in the set of matched elements.

        `jquery <https://api.jquery.com/prepend/#prepend-content-content>`_

        :param data:
        :param js_func: Javascript functions
        """
        return self.fnc("prepend(%(data)s)" % {"data": JsUtils.jsConvertData(data, js_func)})

    def eq(self, i: int):
        """The eq() method returns an element with a specific index number of the selected elements.

        `w3schools <https://www.w3schools.com/jquery/jquery_traversing_filtering.asp>`_

        :param i: The index numbers start at 0, so the first element will have the index number 0 and not 1
        """
        return self.fnc("eq(%(index)s)" % {'index': i})

    def filter(self, selector=None):
        """

        :return:
        """

    def _not(self):
        """ """

    def find(self, criteria):
        """Get the descendants of each element in the current set of matched elements, filtered by a selector, jQuery object,
        or element.

        `jquery <https://api.jquery.com/find/#entry-examples>`_

        :param criteria: Selector or element An element or a jQuery object to match elements against
        """
        criteria = JsUtils.jsConvertData(criteria, None)
        return self.fnc("find(%s)" % criteria)

    def each(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Iterate over a jQuery object, executing a function for each matched element.

        `jquery <https://api.jquery.com/each/#each-function>`_

        :param js_funcs: A function to execute for each matched element
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return self.fnc("each(function(index, data){%s})" % js_funcs)

    def css(self, key, value=None):
        """Hook directly into jQuery to override how particular CSS properties are retrieved or set, normalize CSS property
        naming, or create custom properties.

        `jquery <https://api.jquery.com/jQuery.cssHooks/#jQuery-cssHooks1>`_

        :param key:
        :param value:
        """
        if hasattr(self.component, "style"):
            self.component.style.css(key, value)
            return self

        else:
            if value is None:
                return self.fnc("css(%s)" % JsUtils.jsConvertData(key, None))

            return self.fnc("css('%s', %s)" % (key, JsUtils.jsConvertData(value, None)))

    def attr(self, key, value):
        """Get the value of an attribute for the first element in the set of matched elements.

        `jquery <https://api.jquery.com/attr/#attr-attributeName>`_

        :param key: The name of the attribute to get
        :param value: A value to set for the attribute. If null, the specified attribute will be removed
        """
        if key.lower() in ["style", 'class']:
            raise ValueError("Only the css() function can be used to change the style")

        self.component.set_attrs(value=value, name=value)
        return self.component

    def prop(self, key: types.JS_DATA_TYPES, value=None):
        """The jQuery prop() method gets or sets the value of specified property to the DOM element(s).

        `jquery <https://api.jquery.com/attr/#attr-attributeName>`_

        :param key: The name of the attribute to get
        :param value: A value to set for the attribute. If null, the specified attribute will be removed
        """
        if value is None:
            return self.fnc("prop()")

        return self.fnc("prop(%s, %s)" % (JsUtils.jsConvertData(key, None), value))

    def val(self, data=None, js_func: types.JS_FUNCS_TYPES = None):
        """Get the current value of the first element in the set of matched elements.

        `jquery <https://api.jquery.com/val/#val>`_

        :param data:
        :param js_func: Javascript functions.
        """
        if data is None:
            return self.fnc("val()")

        return self.fnc("val(%s)" % JsUtils.jsConvertData(data, js_func))

    def text(self, data, js_func: types.JS_FUNCS_TYPES = None):
        """Get the combined text contents of each element in the set of matched elements, including their descendants,
        or set the text contents of the matched elements.

        `jquery <https://api.jquery.com/text/#text>`_

        :param data:
        :param js_func: Javascript functions
        """
        if data is None:
            return self.fnc("text()")

        data = JsUtils.jsConvertData(data, js_func)
        return self.fnc("text(%s)" % data)

    def html(self, data=None, js_func: types.JS_FUNCS_TYPES = None):
        """Get the HTML contents of the first element in the set of matched elements or set the HTML contents of
        every matched element

        :param data:
        :param js_func: Javascript functions.
        """
        if data is None:
            return self.fnc("html()")

        return self.fnc("html(%s)" % JsUtils.jsConvertData(data, js_func))

    def toggleClass(self, clsName, propagate: bool = False):
        """Add or remove one or more classes from each element in the set of matched elements, depending on either
        the class’s presence or the value of the state argument.

        `jquery <https://api.jquery.com/toggleClass/>`_

        :param clsName:
        :param propagate:
        """
        if propagate:
            self.fnc_closure(
                'parentNode.childNodes.forEach(function(e){e.classList.remove("%(data)s")})' % {'data': clsName})
        return self.fnc('toggleClass("%(data)s")' % {'data': clsName})

    def addClass(self, clsName, attrs=None, eventAttrs=None):
        """Adds the specified class(es) to each element in the set of matched elements.

        This function can either use an existing class or create one if the attrs or eventAttrs are defined

        :param clsName: The Css classname
        :param attrs: A python dictionary with the css attributes
        :param eventAttrs: A nested python dictionary with the css attributes for each events
        """
        if attrs is not None or eventAttrs is not None:
            clsName = self.component.style.cssName(clsName)
            self.component.style.cssCls(clsName, attrs, eventAttrs, False)
        return self.fnc('addClass("%s")' % clsName)

    def getJSON(self, url, data, success, dataType='json', jsDataKey=None, isPyData=True, js_func=None, profile=None):
        """Load JSON-encoded data from the server using a GET HTTP request.

        `jquery <https//api.jquery.com/jQuery.getJSON/#jQuery-getJSON-url-data-success>_
        """
        success = JsUtils.jsConvertFncs(success, toStr=True, profile=profile)
        data = JsUtils.jsConvert(data, jsDataKey, isPyData, js_func)
        return Jsjqxhr("jQuery.getJSON('%s', {data: JSON.stringify(%s)}, function(data) {%s}, '%s')" % (
            url, data, success, dataType))

    def getJsScript(self, url, data, success, dataType='json', jsDataKey=None, isPyData=True, js_func=None,
                    profile=None):
        """Load a JavaScript file from the server using a GET HTTP request, then execute it.

        `jquery <https//api.jquery.com/jQuery.getScript/>`_

        :param url:
        :param data:
        :param success:
        :param dataType:
        :param jsDataKey:
        :param isPyData:
        :param js_func:
        """
        success = JsUtils.jsConvertFncs(success, toStr=True, profile=profile)
        data = JsUtils.jsConvert(data, jsDataKey, isPyData, js_func)
        return Jsjqxhr(
            "jQuery.getScript('%s', {data: JSON.stringify(%s)}, function(data, textStatus, jqxhr) {%s}, '%s')" % (
                url, data, success, dataType))

    def load(self, url, data=None, success_funcs=None, profile=None):
        """Load data from the server and place the returned HTML into the matched elements.

        Usage::

          div.dom.jquery.load(r"./report_list.html")

        `jquery <https://api.jquery.com/load/#load-url-data-complete>`_

        :param url: A string containing the URL to which the request is sent
        :param data: A plain object or string that is sent to the server with the request
        :param success_funcs: A callback function that is executed when the request completes
        :param profile:
        """
        url = JsUtils.jsConvertData(url, None)
        if success_funcs is None:
            if data is None:
                return "%s.load(%s)" % (self.varId, url)
            return "%s.load(%s, {data: JSON.stringify(%s)})" % (self.varId, url, data)

        str_fncs = JsUtils.jsConvertFncs(success_funcs, toStr=True, profile=profile)
        if data is None:
            return "%s.load(%s, function(data) {%s})" % (self.varId, url, str_fncs)

        return "%s.load(%s, {data: JSON.stringify(%s)}, function(data) {%s})" % (self.varId, url, data, str_fncs)

    def ajaxError(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE =False):
        """Register a handler to be called when Ajax requests complete with an error. This is an Ajax Event.

        `jquery <https://api.jquery.com/ajaxError/>`_

        :param js_funcs:
        :param profile:
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxError(function(event, jqxhr, settings, thrownError) {%s})" % js_funcs

    def ajaxStart(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Register a handler to be called when the first Ajax request begins. This is an Ajax Event.

        `jquery <https://api.jquery.com/ajaxStart/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxStart(function() {%s})" % js_funcs

    def ajaxStop(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Register a handler to be called when all Ajax requests have completed. This is an Ajax Event.

        `jquery <https://api.jquery.com/ajaxStop/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxStop(function() {%s})" % js_funcs

    def ajaxSuccess(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Attach a function to be executed whenever an Ajax request completes successfully. This is an Ajax Event.

        `jquery <https://api.jquery.com/ajaxSuccess/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxSuccess(function(event, xhr, settings) {%s})" % js_funcs

    def ajaxSend(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Attach a function to be executed before an Ajax request is sent. This is an Ajax Event.

        `jquery <https://api.jquery.com/ajaxSend/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxSend(function(event, jqxhr, settings) {%s})" % js_funcs

    def ajaxComplete(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Register a handler to be called when Ajax requests complete. This is an AjaxEvent.

        `jquery <https://api.jquery.com/ajaxComplete-shorthand/>`_

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return "jQuery(document).ajaxComplete(function() {%s})" % js_funcs

    def getParams(self, url, data, success_funcs, error_funcs, options, timeout, props, profile=None):
        """

        :param url:
        :param data:
        :param success_funcs:
        :param error_funcs:
        :param options:
        :param timeout:
        :param props:
        :param profile:
        """
        ajax_data = []
        if props is not None:
            data["_system"] = props
        if options is not None:
            for k, v in options.items():
                ajax_data.append("%s: %s" % (k, json.dumps(v)))
        ajax_data.extend(["data: {data: JSON.stringify(%s)}" % data, "url: '%s'" % url])
        if timeout is not None:
            ajax_data.append("timeout: %s" % timeout)
        if success_funcs is not None:
            ajax_data.append("success: function(result,status,xhr){%s}" % JsUtils.jsConvertFncs(
                success_funcs, toStr=True, profile=profile))
        if error_funcs is not None:
            ajax_data.append("error: function(xhr, status, error){%s}" % JsUtils.jsConvertFncs(
                error_funcs, toStr=True, profile=profile))
        return "{%s}" % ", ".join(ajax_data)

    def get(self, url, data, success_funcs=None, options=None, timeout=None, props=None) -> Jsjqxhr:
        """Load data from the server using a HTTP GET request.

        `w3schools <https://www.w3schools.com/jquery/jquery_ajax_get_post.asp>`_

        :param url:
        :param data:
        :param success_funcs:
        :param options:
        :param timeout:
        :param props:
        """
        return Jsjqxhr("jQuery.get(%s)" % self.getParams(url, data, success_funcs, None, options, timeout, props))

    def post(self, url, data=None, success_funcs=None, options=None, timeout=None, props=None) -> Jsjqxhr:
        """Load data from the server using a HTTP POST request.

        `w3schools <https://www.w3schools.com/jquery/jquery_ajax_get_post.asp>`_

        :param url:
        :param data:
        :param success_funcs:
        :param options:
        :param timeout:
        :param props:
        """
        data = data or {}
        return Jsjqxhr("jQuery.post(%s)" % self.getParams(url, data, success_funcs, None, options, timeout, props))

    def ajax(self, type, url, data=None, success_funcs=None, error_funcs=None, options=None, timeout=None, props=None):
        """The ajax() method is used to perform an AJAX (asynchronous HTTP) request.

        `w3schools <https//www.w3schools.com/jquery/ajax_ajax.asp>`_

        :param type: Specifies the type of request. (GET or POST)
        :param url: Specifies the URL to send the request to. Default is the current page
        :param data: Specifies data to be sent to the server
        :param success_funcs: A function to be run when the request succeeds
        :param error_funcs: A function to run if the request fails
        :param options: The other parameters specifies one or more name/value pairs for the AJAX request
        :param timeout: The local timeout (in milliseconds) for the request
        """
        if type.upper() not in ['POST', 'GET']:
            raise ValueError("Method %s not recognised" % url)

        data = data or {}
        return Jsjqxhr(
            "jQuery.ajax(%s)" % self.getParams(url, data, success_funcs, error_funcs, options, timeout, props))

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        self.css("cursor", "pointer")
        return self.fnc("click(function(event){%s})" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))

    def on(self, event: Union[str, List[str]], js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
           source_event: Optional[str] = None):
        """Attach an event handler function for one or more events to the selected elements.

        `jquery <https://api.jquery.com/on/>`_

        Usage::

          btn = page.ui.button("Click")
          btn.js.jquery.on("click", [btn.js.jquery.after('<div style="background-color:yellow"> New div </div>')])

        :param event:
        :param js_funcs:
        :param profile:
        :param source_event:
        """
        source_event = source_event or self.varId
        if isinstance(event, list):
            event = " ".join(event)
        js_event = self.component.on(event, js_funcs=js_funcs, profile=profile, source_event=source_event)
        self.component._browser_data['mouse'][event][source_event]['fncType'] = "on"
        return js_event

    def after(self, html_frg: types.JS_DATA_TYPES):
        """Inserts content (new or existing DOM elements) after an element(s) which is specified by a selector.

        `jquery <https://api.jquery.com/after/>`_

        Usage::

          btn = page.ui.button("Click")
          btn.js.jquery.on("click", [btn.js.jquery.after('<div style="background-color:yellow"> New div </div>'),])

        :param html_frg:
        """
        html_frg = JsUtils.jsConvertData(html_frg, None)
        return self.fnc("after(%s)" % html_frg)

    def before(self, html_frg: types.JS_DATA_TYPES):
        """Inserts content (new or existing DOM elements) before an element(s) which is specified by a selector.

        `jquery <https://api.jquery.com/before/>`_

        Usage::

          btn = page.ui.button("Click")
          btn.js.jquery.on("click", [btn.js.jquery.before('<div style="background-color:yellow"> New div </div>')])

        :param html_frg:
        """
        html_frg = JsUtils.jsConvertData(html_frg, None)
        return self.fnc("before(%s)" % html_frg)

    def when(self, **kwargs):
        """Provides a way to execute callback functions based on zero or more Thenable objects, usually Deferred
        objects that represent asynchronous events.

        `jQuery <https://api.jquery.com/jQuery.when/>`_
        """
        if not kwargs:
            return Deferred("$.when()")

        r, p = [], []
        for k, v in kwargs.items():
            p.append(k)
            r.append(JsUtils.jsConvertData(v, None))
        d = Deferred("$.when(%s)" % ", ".join(r))
        d.pmts = p
        return d

    def Deferred(self, beforeStart: types.JS_FUNCS_TYPES = None):
        """A factory function that returns a chainable utility object with methods to register multiple callbacks into
        callback queues, invoke callback queues, and relay the success or failure state of any synchronous or asynchronous function.

        `jQuery <https://api.jquery.com/jQuery.Deferred/>`_
        `Examples <https://learn.jquery.com/code-organization/deferreds/examples/>`_

        :param beforeStart: A function that is called just before the constructor returns.
        """
        return Deferred(beforeStart)
