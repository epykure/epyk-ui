
from epyk.core.js import JsUtils


class JsFor(object):

  def __init__(self, end, options=None):
    """
    Description:
    -----------
    The for statement creates a loop that is executed as long as a condition is true.

    The loop will continue to run as long as the condition is true. It will only stop when the condition becomes false.

    Related Pages:

			https//www.w3schools.com/jsref/jsref_for.asp
    https://www.w3schools.com/js/js_performance.asp

    Attributes:
    ----------
    :param end:
    :param options: Dictionary
    """
    self.options = {"var": 'i', 'start': 0, 'step': 1, 'end': end}
    if options is not None:
      self.options.update(options)
    self.__jsFncs = []

  @property
  def var(self):
    """

    :return:
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """

    :return:
    """
    self.options['var'] = value

  @property
  def start(self):
    """

    :return:
    """
    return self.options['start']

  @start.setter
  def start(self, value):
    """

    :return:
    """
    self.options['start'] = value

  @property
  def end(self):
    """

    :return:
    """
    return self.options['end']

  @end.setter
  def end(self, value):
    """

    :return:
    """
    self.options['end'] = value

  @property
  def step(self):
    """

    :return:
    """
    return self.options['step']

  @step.setter
  def step(self, value):
    """

    :return:
    """
    self.options['step'] = value

  def fncs(self, jsFncs, reset=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param reset:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    return self

  def toStr(self):
    """

    """
    self.options['expr'] = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True)
    return "for(var %(var)s = %(start)s; %(var)s < %(end)s; %(var)s++){%(expr)s}" % self.options


class JsIterable(object):

  def __init__(self, jsIterable, options=None):
    """

    Attributes:
    ----------
    :param jsIterable:
    """
    self.__js_it = jsIterable
    self.options = {"var": 'x', 'type': 'in'}
    if options is not None:
      self.options.update(options)

  @property
  def var(self):
    """
    Description:
    -----------
`   Return the variable reference for this loop
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """
    Description:
    -----------
`   Return the variable reference for this loop

    Attributes:
    ----------
    :param value: String. The value reference for the JavaScript variable
    """
    self.options['var'] = value

  def fncs(self, jsFncs, reset=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param reset:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    return self

  def toStr(self):
    """

    """
    jsNfncs = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True)
    jsIter = JsUtils.jsConvertData(self.__js_it, None)
    return "for(var %s %s %s){%s}" % (self.var, self.options['type'], jsIter, jsNfncs)
