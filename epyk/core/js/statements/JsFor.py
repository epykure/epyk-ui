
from epyk.core.js import JsUtils


class JsFor:

  def __init__(self, end, options=None, profile=None):
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
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    self.options = {"var": 'i', 'start': 0, 'step': 1, 'end': end}
    if options is not None:
      self.options.update(options)
    self.__jsFncs = []
    self.profile = profile

  @property
  def var(self):
    """
    Description:
    -----------
    Get the for loop iterable variable name.

    :return: A string corresponding to the variable.
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """
    Description:
    -----------
    Set the for loop iterable variable name.
    """
    self.options['var'] = value

  @property
  def start(self):
    """
    Description:
    -----------

    """
    return self.options['start']

  @start.setter
  def start(self, value):
    if hasattr(value, 'toStr'):
      self.options['start'] = "parseFloat(%s)" % JsUtils.jsConvertData(value, None)
    else:
      self.options['start'] = value

  @property
  def end(self):
    """
    Description:
    -----------

    """
    return self.options['end']

  @end.setter
  def end(self, value):
    if hasattr(value, 'toStr'):
      self.options['end'] = "parseFloat(%s)" % JsUtils.jsConvertData(value, None)
    else:
      self.options['end'] = value

  @property
  def step(self):
    """
    Description:
    -----------

    """
    return self.options['step']

  @step.setter
  def step(self, value):
    if hasattr(value, 'toStr'):
      self.options['step'] = "parseFloat(%s)" % JsUtils.jsConvertData(value, None)
    else:
      self.options['step'] = value

  def fncs(self, jsFncs, reset=True, profile=None):
    """
    Description:
    -----------
    Add JavaScript functions to the content of the for loop.

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param reset: Boolean. Optional. Reset the functions in the for loop.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    self.profile = profile
    return self

  def toStr(self):
    self.options['expr'] = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True, profile=self.profile)
    return "for(var %(var)s = %(start)s; %(var)s < %(end)s; %(var)s += %(step)s){%(expr)s}" % self.options


class JsIterable:

  def __init__(self, jsIterable, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsIterable:
    """
    self.__js_it = jsIterable
    self.options = {"var": 'x', 'type': 'in'}
    if options is not None:
      self.options.update(options)
    self.profile = False

  @property
  def var(self):
    """
    Description:
    -----------
`   Return the variable reference for this loop.
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """
    Description:
    -----------
`   Return the variable reference for this loop.

    Attributes:
    ----------
    :param value: String. The value reference for the JavaScript variable
    """
    self.options['var'] = value

  def fncs(self, jsFncs, reset=True, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param reset:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if reset:
      self.__jsFncs = jsFncs
    else:
      self.__jsFncs.extend(jsFncs)
    self.profile = profile
    return self

  def toStr(self):
    jsNfncs = JsUtils.jsConvertFncs(self.__jsFncs, toStr=True, profile=self.profile)
    jsIter = JsUtils.jsConvertData(self.__js_it, None)
    return "for(var %s %s %s){%s}" % (self.var, self.options['type'], jsIter, jsNfncs)
