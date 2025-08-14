import json

from typing import Union

from epyk.core.js.html import JsHtml
from epyk.core.js import JsUtils

from epyk.core.js.primitives import JsObjects


class Console(JsHtml.JsHtmlRich):

    def write(self, data, timestamp=None, stringify: bool = False, skip_data_convert: bool = False, format: str = None,
              profile: Union[bool, dict] = False):
        """

        :param data:
        :param timestamp:
        :param profile:
        :param stringify:
        :param skip_data_convert:
        :param format: A string output format using %s to define the data in the string
        """
        extra_expr = ""
        js_data = data if skip_data_convert else JsUtils.jsConvertData(data, None)
        if self.component.options.scroll_to_bottom:
            extra_expr = ";%(varId)s.scrollTop = %(varId)s.scrollHeight" % {"varId": self.component.dom.varId}
        if stringify:
            js_data = "JSON.stringify(%s)" % js_data
        if self.component.options.showdown is not False:
            js_data = '''
(function(d){ var conv = new showdown.Converter(%s);
    let frag = document.createRange().createContextualFragment(conv.makeHtml(d)); 
    if((frag.firstChild === null) || (typeof frag.firstChild.style == "undefined")){return d}
    else{frag.firstChild.style.display = 'inline-block';frag.firstChild.style.margin = 0 ;  
         return frag.firstChild.outerHTML}})(%s) ''' % (json.dumps(self.component.options.showdown), js_data)
        if format is not None:
            js_data = JsUtils.jsConvertData(format, None).toStr().replace("%s", '"+ %s +"') % js_data
        if timestamp or (self.component.options.timestamp and timestamp != False):
            return JsObjects.JsObjects.get(
                "%s.innerHTML += ' > '+ new Date().toISOString().replace('T', ' ').slice(0, 19) +', '+ %s +'<br/>'%s" % (
                    self.varName, js_data, extra_expr))

        return JsObjects.JsObjects.get("%s.innerHTML += ' > '+ %s +'<br/>'%s" % (self.component.dom.varId, js_data, extra_expr))

    def clear(self):
        """Clear the editor. """
        return JsObjects.JsObjects.get('%s.innerHTML = ""' % self.varName)

