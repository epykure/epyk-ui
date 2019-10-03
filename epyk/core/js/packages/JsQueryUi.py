"""

"""

import json

from epyk.core.js import JsUtils


class JQueryUI(object):
  class __internal(object):
    jqId, htmlId, jsImports, cssImport = '', '', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.src.jsImports.add('jqueryui')
    self.src.cssImport.add('jqueryui')
    self.selector = self.src.jqId if hasattr(self.src, 'jqId') else None
    self._js = []

  def draggable(self, options=None):
    """

    :return:
    """
    if options is not None:
      self._js.append("draggable(%s)" % JsUtils.jsConvertData(options, None))
    else:
      self._js.append("draggable()")
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self.selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self.selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self.selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return strData


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
