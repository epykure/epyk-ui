"""

"""

import json

from epyk.core.js import JsUtils


class JQueryUiDatePicker(object):

  class __internal(object):
    jqId, htmlId, jsImports, cssImport = '', '', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.src.jsImports.add('jqueryui')
    self.src.cssImport.add('jqueryui')
    #self.selector = self.src.jqId if hasattr(self.src, 'jqId') else None
    self._js = []

  def setDefaults(self):
    """

    :return:
    """

  def formatDate(self):
    """

    :return:
    """

  def option(self, name, value):
    """

    :return:
    """
    return "$('#%s input').datepicker( 'option', '%s', %s)" % (self.src.htmlId, name, json.dumps(value))

  def refresh(self):
    """

    :return:
    """


class JQueryUiSlider(object):
  """

  Documentation
  https://api.jqueryui.com/slider/

  """

  def destroy(self):
    """

    :return:
    """

  def disable(self):
    """

    :return:
    """

  def option(self, name, value):
    """

    :return:
    """

  def enable(self):
    pass

  def value(self):
    pass

  def values(self):
    pass

  def widget(self):
    pass

  def instance(self):
    pass
