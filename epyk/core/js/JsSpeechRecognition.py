"""
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var recognition = new SpeechRecognition();
recognition.lang = 'fr-FR';

var grammar = '#JSGF V1.0; grammar colors; public <color> = aqua | azure | beige | bisque | black | blue | brown | chocolate | coral | crimson | cyan | fuchsia | ghostwhite | gold | goldenrod | gray | green | indigo | ivory | khaki | lavender | lime | linen | magenta | maroon | moccasin | navy | olive | orange | orchid | peru | pink | plum | purple | red | salmon | sienna | silver | snow | tan | teal | thistle | tomato | turquoise | violet | white | yellow ;';

var speechRecognitionList = new webkitSpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.interimResults = false;
recognition.maxAlternatives = 1;

// This runs when the speech recognition service starts
recognition.onstart = function() {
    console.log("We are listening. Try speaking into the microphone.");
};

recognition.onspeechend = function() {
    // when user is done speaking
    recognition.stop();
}

// This runs when the speech recognition service returns result
recognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript;
    var confidence = event.results[0][0].confidence;
	console.log(transcript);
};

recognition.start();

"""

import json

from typing import Union
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class SpeechGrammarList:
    """
    webkitSpeechGrammarList

    Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/SpeechGrammarList
    """

    @property
    def length(self):
        return

    def items(self):
        pass

    def addFromString(self, value, index):
        pass


class SpeechRecognitionEvent:
    transcript = JsUtils.jsWrap("transcript")
    confidence = JsUtils.jsWrap("confidence")


class SpeechRecognition:
    __grammars = "en-US"
    lang: str = "en-US"
    continuous: bool = False
    interimResults: bool = False
    maxAlternatives: int = 1

    def __init__(self, js_code: str, page: primitives.PageModel = None):
      self.page = page
      self.js_code = js_code
      self._js = [
        "var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition",
        "var %s = new SpeechRecognition()" % js_code]

    @property
    def event(self):
      return SpeechRecognitionEvent()

    @property
    def grammars(self):
        return self.__grammars

    @grammars.setter
    def grammars(self, value: str):
      self.__grammars = value

    def abort(self):
        """
        Stops the speech recognition service from listening to incoming audio, and doesn't attempt to return a
        SpeechRecognitionResult.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition/abort
        """
        return JsObjects.JsVoid("%s.abort()" % self.js_code)

    def start(self):
        """
        Starts the speech recognition service listening to incoming audio with intent to recognize grammars associated
        with the current SpeechRecognition.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition/start
        """
        return JsObjects.JsVoid("%s.start()" % self.js_code)

    def stop(self):
        """
        Stops the speech recognition service from listening to incoming audio, and attempts to return a
        SpeechRecognitionResult using the audio captured so far.

        Related Pages:

            https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition/stop
        """
        return JsObjects.JsVoid("%s.stop()" % self.js_code)

    def addEventListener(self, event: str, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        self._js.append("%(selector)s.%(event)s = function(event) {var transcript = event.results[0][0].transcript; var confidence = event.results[0][0].confidence;%(funcs)s}" % {
          "selector": self.js_code, "event": event,
          "funcs": JsUtils.jsConvertFncs(js_funcs, profile=profile, toStr=True)})
        return self

    def audiostart(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        """
        Fired when the user agent has started to capture audio. Also available via the onaudiostart property.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        return self.addEventListener("audiostart", js_funcs, profile)

    def audioend(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("audioend", js_funcs, profile)

    def onend(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("end", js_funcs, profile)

    def error(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("error", js_funcs, profile)

    def nomatch(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("nomatch", js_funcs, profile)

    def result(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("result", js_funcs, profile)

    def soundstart(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("soundstart", js_funcs, profile)

    def soundend(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("soundend", js_funcs, profile)

    def speechstart(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("speechstart", js_funcs, profile)

    def speechend(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("speechend", js_funcs, profile)

    def onstart(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        return self.addEventListener("start", js_funcs, profile)

    def onresult(self, js_funcs: Union[list, str], profile: Union[bool, dict] = None):
        """

        Usage::

          page = pk.Page()
          rec = page.js.speechRecognition("reco")

          test = page.ui.button("test")
          test.click([rec.start()])

          rec.speechend([rec.stop()])
          rec.onresult([page.js.console.log(pk.js_callback("ProcessData(transcript, confidence)"))])

          page.body.onReady([
            page.js.import_js(
              'function ProcessData(transcript, confidence){console.log(transcript); return "Test"}', [], self_contained=True), rec])

        :param js_funcs:
        :param profile:
        """
        return self.addEventListener("onresult", js_funcs, profile)

    def toStr(self):
        obj_content = []
        # Add the object properties
        self._js.insert(2, "%s.lang = %s" % (self.js_code, json.dumps(self.lang)))
        self._js.insert(3, "%s.continuous = %s" % (self.js_code, json.dumps(self.continuous)))
        self._js.insert(4, "%s.interimResults = %s" % (self.js_code, json.dumps(self.interimResults)))
        self._js.insert(5, "%s.maxAlternatives = %s" % (self.js_code, json.dumps(self.maxAlternatives)))
        for js in self._js:
          obj_content.append(js)
        self._js = []
        return "; ".join(obj_content)

