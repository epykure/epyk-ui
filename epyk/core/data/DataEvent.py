

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
