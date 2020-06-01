

class DataEvents(object):

  @property
  def data(self):
    """
    Description:
    ------------
    Interface to a standard data object available in any Event.
    This is the default variable name in all the JavaScript embedded methods
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("data")

  @property
  def event(self):
    """
    Description:
    ------------
    Interface to the standard event
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.Event()

  @property
  def mouse(self):
    """
    Description:
    ------------
    Interface to the standard mouse event
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.MouseEvent()

  @property
  def ui(self):
    """
    Description:
    ------------
    Interface to the UI generic event
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.UIEvent()

  @property
  def touch(self):
    """
    Description:
    ------------
    Interface to a standard touch event.
    This object is available in any event specific to touch screens
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.TouchEvent()

  @property
  def key(self):
    """
    Description:
    ------------
    Interface to a standard keyboard event.
    This object is available in any keyup, keydown... events
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.KeyboardEvent()


class DataLoops(object):

  @property
  def value(self):
    """
    Description:
    -----------
    The value returned by forEach statement.

    Note. For nested loop make sure you store the important information in new variable names.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObject.JsObject.get("value")

  @property
  def dom(self):
    """
    Description:
    -----------

    :return:
    """
    from epyk.core.js.objects import JsNodeDom
    return JsNodeDom.JsDoms.new(varName="value", setVar=False)

  @property
  def i(self):
    """
    Description:
    ------------
    The index value return in loop statement
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsNumber.JsNumber.get("index")


class DataPrimitives(object):

  def list(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. The Python object used to feed the list
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsArray.JsArray(data, varName=name, setVar=setVar)

    return JsObjects.JsArray.JsArray.get(name)

  def dict(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsObject.JsObject(data, varName=name, setVar=setVar)

    return JsObjects.JsObject.JsObject.get(name)

  def str(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsString.JsString(data, varName=name, setVar=setVar)

    return JsObjects.JsString.JsString.get(name)

  def float(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=setVar)

    return JsObjects.JsNumber.JsNumber.get(name)

  def int(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=setVar)

    return JsObjects.JsNumber.JsNumber.get(name)
