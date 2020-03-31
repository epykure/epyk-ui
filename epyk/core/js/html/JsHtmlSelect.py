
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects


class JsHtmlSwitch(JsHtml.JsHtmlRich):

  def set_text(self, value, is_on_val=True):
    """
    Description:
    ------------
    Change the value of the text component

    Usage:
    ------
    sw = rptObj.ui.buttons.switch()
    rptObj.ui.button("test").click([
      sw.dom.set_text("ok")])

    Attributes:
    ----------
    :param value: String. The new value
    :param is_on_val: Boolean. Change either the on or the off value displayed
    """
    value = JsUtils.jsConvertData(value, None)
    return ''' if(%(text)s == %(htmlId)s_data.%(switch_type)s){ %(htmlObj)s };
       %(htmlId)s_data.%(switch_type)s = %(value)s
       ''' % {'htmlId': self._src.htmlCode, 'switch_type': 'on' if is_on_val else 'off', 'value': value,
              'text': self._src.switch_text.dom.content, 'htmlObj': self._src.switch_text.build(value)}


class DomSelect(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, text: %s, options_text: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlId, self.content, self.text, self.options_text))

  @property
  def content(self):
    """
    Description:
    ------------
    Get the selected content from the Select component

    """
    return JsObjects.JsObjects.get("%s.val()" % self.jquery.varId)

  @property
  def text(self):
    """
    Description:
    ------------
    Get the selected content from the Select component

    """
    return JsObjects.JsObjects.get("%s.find('option:selected').text()" % self.jquery.varId)

  @property
  def index(self):
    """
    Description:
    ------------
    Get the selected content from the Select component

    """
    return JsObjects.JsObjects.get("%s.find('option:selected').index()" % self.jquery.varId)

  @property
  def options_text(self):
    """
    Description:
    ------------
    Get the selected content from the Select component

    """
    return JsObjects.JsObjects.get("%s.text()" % self.jquery.varId)
