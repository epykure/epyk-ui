from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObjects


class Cache:

    def __init__(self, name: str, page):
        self.__name = name
        self.page = page

    @property
    def varId(self):
        return ""

    def match(self, request, options = None) -> JsObjects.JsObject.JsObject:
        """Returns a Promise that resolves to the response associated with the first matching request in the Cache
        object.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/match>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        :param options:
        """
        request = JsUtils.jsConvertData(request, None)
        if not options:
            return JsObjects.JsObject.JsObject.get("await %s.match(%s)" % (self.varId, request))

        options = JsUtils.jsConvertData(options, None)
        return JsObjects.JsObject.JsObject.get("await %s.match(%s, %s)" % (self.varId, request, options))

    def matchAll(self, request, options = None):
        """Returns a Promise that resolves to an array of all matching responses in the Cache object.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/matchAll>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        :param options:
        """
        request = JsUtils.jsConvertData(request, None)
        if not options:
            return JsUtils.jsWrap("await %s.matchAll(%s)" % (self.varId, request))

        options = JsUtils.jsConvertData(options, None)
        return JsUtils.jsWrap("await %s.matchAll(%s, %s)" % (self.varId, request, options))

    def add(self, request):
        """Takes a URL, retrieves it and adds the resulting response object to the given cache.
        This is functionally equivalent to calling fetch(), then using put() to add the results to the cache.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/add>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        """
        request = JsUtils.jsConvertData(request, None)
        return JsUtils.jsWrap("%s.add(%s)" % (self.varId, request))

    def addAll(self, requests):
        """Takes an array of URLs, retrieves them, and adds the resulting response objects to the given cache.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/addAll>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param requests: Array of urls as string or a request objects
        """
        requests = JsUtils.jsConvertData(requests, None)
        return JsUtils.jsWrap("%s.addAll(%s)" % (self.varId, requests))

    def put(self, request, response = None):
        """Takes both a request and its response and adds it to the given cache.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/put>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        :param response: The response object
        """
        request = JsUtils.jsConvertData(request, None)
        if not response:
            return JsUtils.jsWrap("%s.put(%s)" % (self.varId, request))

        response = JsUtils.jsConvertData(response, None)
        return JsUtils.jsWrap("%s.put(%s, %s)" % (self.varId, request, response))

    def delete(self, request, options = None):
        """Finds the Cache entry whose key is the request, returning a Promise that resolves to true if a matching
        Cache entry is found and deleted. If no Cache entry is found, the promise resolves to false.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/delete>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        """
        request = JsUtils.jsConvertData(request, None)
        if not options:
            return JsUtils.jsWrap("%s.delete(%s)" % (self.varId, request))

        options = JsUtils.jsConvertData(options, None)
        return JsUtils.jsWrap("%s.delete(%s, %s)" % (self.varId, request, options))

    def keys(self, request, options = None):
        """Returns a Promise that resolves to an array of Cache keys.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/Cache/keys>`_
        `Example <https://blog.logrocket.com/javascript-cache-api/>`_

        :param request: Url as string or a request object
        """
        request = JsUtils.jsConvertData(request, None)
        if not options:
            return JsUtils.jsWrap("%s.keys(%s)" % (self.varId, request))

        options = JsUtils.jsConvertData(options, None)
        return JsUtils.jsWrap("%s.keys(%s, %s)" % (self.varId, request, options))


class CacheStorage:

    def __init__(self, page):
        self.page = page

    def match(self, request, options = None) -> JsObjects.JsPromise:
        """Checks if a given Request is a key in any of the Cache objects that the CacheStorage object tracks, and
        returns a Promise that resolves to that match.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/match>`_

        :param request: The Request you want to match. This can be a Request object or a URL string.
        :param options: An object whose properties control how matching is done in the match operation.
        """
        request = JsUtils.jsConvertData(request, None)
        if not options:
            return JsObjects.JsPromise("window.caches.match(%s)" % request)

        options = JsUtils.jsConvertData(options, None)
        return JsObjects.JsPromise("window.caches.match(%s, %s)" % (request, options))

    def has(self, name) -> JsBoolean.JsBoolean:
        """Returns a Promise that resolves to true if a Cache object matching the cacheName exists.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/has>`_
        """
        name = JsUtils.jsConvertData(name, None)
        return JsBoolean.JsBoolean.get("window.caches.has(%s)" % name)

    def open(self, name: str) -> Cache:
        """Returns a Promise that resolves to the Cache object matching the cacheName (a new cache is created
        if it doesn't already exist.)

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/open>`_

        :param name: The name of the cache
        """
        return Cache(name, self.page)

    def delete(self, name: str):
        """Finds the Cache object matching the cacheName, and if found, deletes the Cache object and returns a
        Promise that resolves to true. If no Cache object is found, it resolves to false.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/delete>`_
        """
        name = JsUtils.jsConvertData(name, None)
        return JsUtils.jsWrap("window.caches.delete(%s)" % name)

    def keys(self) -> JsObjects.JsPromise:
        """Returns a Promise that will resolve with an array containing strings corresponding to all of the named
        Cache objects tracked by the CacheStorage. Use this method to iterate over a list of all the Cache objects.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage/keys>`_
        """
        return JsObjects.JsPromise("window.caches.keys()")
