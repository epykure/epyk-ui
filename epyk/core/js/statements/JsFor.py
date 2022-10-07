
from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.js import JsUtils


PARSE_FLOAT_EXPR = "parseFloat({})"


class JsFor:

  def __init__(self, end, options: Optional[dict] = None, profile: Optional[Union[dict, bool]] = None):
    """   The for statement creates a loop that is executed as long as a condition is true.

    The loop will continue to run as long as the condition is true. It will only stop when the condition becomes false.

    Related Pages:

      https//www.w3schools.com/jsref/jsref_for.asp
      https://www.w3schools.com/js/js_performance.asp

    :param end:
    :param Optional[dict] options: Optional. Specific Python options available for this component.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.options = {"var": 'i', 'start': 0, 'step': 1, 'end': end}
    if options is not None:
      self.options.update(options)
    self.__js_funcs = []
    self.profile = profile

  @property
  def var(self) -> str:
    """   Get the for loop iterable variable name.

    :return: A string corresponding to the variable.
    """
    return self.options['var']

  @var.setter
  def var(self, value):
    """   Set the for loop iterable variable name.
    """
    self.options['var'] = value

  @property
  def start(self):
    """   Set the start value for the for loop.
    """
    return self.options['start']

  @start.setter
  def start(self, value: Union[int, primitives.JsDataModel]):
    if hasattr(value, 'toStr'):
      self.options['start'] = PARSE_FLOAT_EXPR.format(JsUtils.jsConvertData(value, None))
    else:
      self.options['start'] = value

  @property
  def end(self):
    """   Set the end value for the for loop.
    """
    return self.options['end']

  @end.setter
  def end(self, value: Union[int, primitives.JsDataModel]):
    if hasattr(value, 'toStr'):
      self.options['end'] = PARSE_FLOAT_EXPR.format(JsUtils.jsConvertData(value, None))
    else:
      self.options['end'] = value

  @property
  def step(self):
    """   Set the step value to be used in the for loop to increment the variable.
    """
    return self.options['step']

  @step.setter
  def step(self, value: Union[int, primitives.JsDataModel]):
    if hasattr(value, 'toStr'):
      self.options['step'] = PARSE_FLOAT_EXPR.format(JsUtils.jsConvertData(value, None))
    else:
      self.options['step'] = value

  def fncs(self, js_funcs: Union[list, str], reset: bool = True, profile: Optional[Union[dict, bool]] = None):
    """   Add JavaScript functions to the content of the for loop.

    :param Union[list, str] js_funcs: The PyJs functions.
    :param bool reset: Optional. Reset the JavaScript functions for this loop.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if reset:
      self.__js_funcs = js_funcs
    else:
      self.__js_funcs.extend(js_funcs)
    self.profile = profile
    return self

  def toStr(self):
    self.options['expr'] = JsUtils.jsConvertFncs(self.__js_funcs, toStr=True, profile=self.profile)
    return "for(var %(var)s = %(start)s; %(var)s < %(end)s; %(var)s += %(step)s){%(expr)s}" % self.options


class JsIterable:

  def __init__(self, iterable: Union[primitives.JsDataModel, str], options: Optional[dict] = None,
               profile: Optional[Union[dict, bool]] = None):
    """   

    :param Union[primitives.JsDataModel, str] iterable:
    :param Optional[dict] options: Optional. Specific Python options available for this component.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.__js_it = iterable
    self.options = {"var": 'x', 'type': 'in'}
    if options is not None:
      self.options.update(options)
    self.profile = profile

  @property
  def var(self):
    """   
`   Return the variable reference for this loop.
    """
    return self.options['var']

  @var.setter
  def var(self, value: str):
    """   
`   Return the variable reference for this loop.

    :param str value: The value reference for the JavaScript variable.
    """
    self.options['var'] = value

  def fncs(self, js_funcs: Union[list, str], reset: bool = True, profile: Optional[Union[dict, bool]] = None):
    """   Add expression to the for loop.

    :param Union[list, str] js_funcs: The PyJs functions.
    :param bool reset: Optional. Reset the JavaScript functions for this loop.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if reset:
      self.__js_funcs = js_funcs
    else:
      self.__js_funcs.extend(js_funcs)
    self.profile = profile
    return self

  def toStr(self):
    js_n_funcs = JsUtils.jsConvertFncs(self.__js_funcs, toStr=True, profile=self.profile)
    js_iter = JsUtils.jsConvertData(self.__js_it, None)
    return "for(var %s %s %s){%s}" % (self.var, self.options['type'], js_iter, js_n_funcs)
