
from epyk.core.js import JsUtils
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsObjects


class SpeechGrammarList:
    """
    webkitSpeechGrammarList

    https://developer.mozilla.org/en-US/docs/Web/API/SpeechGrammarList
    """

    @property
    def length(self):
        return

    def items(self):
        pass

    def addFromString(self, value, index):
        pass


class SpeechRecognition:
    __grammars = "en-US"
    lang: str = "en-US"
    continuous: bool = False
    interimResults: bool = False
    maxAlternatives: int = 1

    @property
    def grammars(self):
        return self.__grammars

    @grammars.setter
    def grammars(self, value: str):
      self.__grammars = value

    def abort(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def addEventListener(self, event, jsFuncs, profile=False):
        pass

    def audiostart(self, jsFuncs, profile=False):
        """
        Fired when the user agent has started to capture audio. Also available via the onaudiostart property.

        https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

        :param jsFuncs:
        :param profile:
        :return:
        """
        return self.addEventListener("audiostart", jsFuncs, profile)

    def audioend(self, jsFuncs, profile=False):
        return self.addEventListener("audioend", jsFuncs, profile)

    def end(self, jsFuncs, profile=False):
        return self.addEventListener("end", jsFuncs, profile)

    def error(self, jsFuncs, profile=False):
        return self.addEventListener("error", jsFuncs, profile)

    def nomatch(self, jsFuncs, profile=False):
        return self.addEventListener("nomatch", jsFuncs, profile)

    def result(self, jsFuncs, profile=False):
        return self.addEventListener("result", jsFuncs, profile)

    def soundstart(self, jsFuncs, profile=False):
        return self.addEventListener("soundstart", jsFuncs, profile)

    def soundend(self, jsFuncs, profile=False):
        return self.addEventListener("soundend", jsFuncs, profile)

    def speechstart(self, jsFuncs, profile=False):
        return self.addEventListener("speechstart", jsFuncs, profile)

    def speechend(self, jsFuncs, profile=False):
        return self.addEventListener("speechend", jsFuncs, profile)

    def start(self, jsFuncs, profile=False):
        return self.addEventListener("start", jsFuncs, profile)


