
from epyk.core.py import types
from epyk.core.html import Defaults as Default_html


class HtmlStates:

  def loading(
          self,
          status: bool = True,
          label: str = None,
          data: types.JS_DATA_TYPES = None
  ):
    """ Display a loading message in the component.

    Usage::

      btn.click([
          t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"}),
      ])

    :param status: The message status (true is active)
    :param label: The message template
    :param data: The message parameter to feed the template
    """
    if label is not None:
      self.options.templateLoading = label
    if self.options.templateLoading is None:
      self.options.templateLoading = Default_html.TEMPLATE_LOADING_ONE_LINE
    if status:
      return self.build(data, options={"templateMode": 'loading'})

    if data is None:
      return self.build(self.dom.getAttribute("data-content"))

    return self.build(data)

  def error(
          self,
          status: bool = True,
          label: str = None,
          data: types.JS_DATA_TYPES = None
  ):
    """ Display an error message in the component.

    Usage::

      btn.click([
          t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"}),
      ])

    :param status: The message status (true is active)
    :param label: The message template
    :param data: The message parameter to feed the template
    """
    if label is not None:
      self.options.templateError = label
    if self.options.templateError is None:
      self.options.templateError = Default_html.TEMPLATE_ERROR_ONE_LINE
    if status:
      return self.build(data, options={"templateMode": 'error'})

    if data is None:
      return self.build(self.dom.getAttribute("data-content"))

    return self.build(data)
