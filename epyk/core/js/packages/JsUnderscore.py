
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Underscore(JsPackage):

    lib_alias = {"js": 'underscore'}
    lib_selector = '_'

    def custom(self, func_name: str, **kwargs):
        """

        Usage::

        page.body.onReady([page.js.console.log(page.data.js._.custom(
            "reduce", iteratee=[1, 2, 3], memo=pk.js_callback("function(memo, num){ return memo + num; }"), context=0))])

        """
        _args = ["%s=%s" % (k, JsUtils.jsConvertData(v, None)) for k, v in kwargs.items()]
        return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (self._selector, func_name, ", ".join(_args)))

    def each(self, data, iteratee, context: dict = None):
        """
        Iterates over a list of elements, yielding each in turn to an iteratee function.
        The iteratee is bound to the context object, if one is passed. Each invocation of iteratee is called with three
        arguments: (element, index, list).
        If list is a JavaScript object, iteratee's arguments will be (value, key, list). Returns the list for chaining.

        Usage::

            page.body.onReady([page.data.js._.each([1, 9], pk.js_callback("alert"))])

        :param data:
        :param iteratee:
        :param context:
        """
        data = JsUtils.jsConvertData(data, None)
        iteratee = JsUtils.jsConvertData(iteratee, None)
        if context is not None:
            context = JsUtils.jsConvertData(context, None)
            return JsObjects.JsObject.JsObject.get(
                "%s.each(%s, %s, %s)" % (self._selector, data, iteratee, context))

        return JsObjects.JsObject.JsObject.get("%s.each(%s, %s)" % (
            self._selector, data, iteratee))

    def map(self, data, iteratee, context: dict = None):
        """
        Produces a new array of values by mapping each value in list through a transformation function (iteratee).
        The iteratee is passed three arguments: the value, then the index (or key) of the iteration, and finally a
        reference to the entire list.

        Usage::

            page.body.onReady([page.data.js._.map([1, 9], pk.js_callback("alert"))])

        :param data:
        :param iteratee:
        :param context:
        """
        data = JsUtils.jsConvertData(data, None)
        iteratee = JsUtils.jsConvertData(iteratee, None)
        if context is not None:
            context = JsUtils.jsConvertData(context, None)
            return JsObjects.JsObject.JsObject.get(
                "%s.map(%s, %s, %s)" % (self._selector, data, iteratee, context))

        return JsObjects.JsObject.JsObject.get("%s.map(%s, %s)" % (
            self._selector, data, iteratee))
