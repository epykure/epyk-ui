"""The Crypto interface represents basic cryptography features available in the current context.
It allows access to a cryptographically strong random number generator and to cryptographic primitives.

The Crypto is available in windows using the Window.crypto property and in workers using the WorkerGlobalScope.crypto
property.
"""

from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsArray


class JsCrypto:

    def __init__(self, page):
        self.page = page

    @classmethod
    def randomUUID(cls):
        """ Returns a randomly generated, 36 character long v4 UUID. """
        return JsString.JsString.get("window.crypto.randomUUID()")

    @classmethod
    def getRandomValues(cls, n: int):
        """The Crypto.getRandomValues() method lets you get cryptographically strong random values.
        The array given as the parameter is filled with random numbers (random in its cryptographic meaning)."""
        return JsArray.JsArray.get("(function(n){const array = new Uint32Array(n);self.crypto.getRandomValues(array); return array})(%s)" % n)
