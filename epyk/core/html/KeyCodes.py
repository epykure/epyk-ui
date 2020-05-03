
from epyk.core.js import JsUtils


class KeyCode(object):

  def __init__(self):
    self.__events = {}

  def custom(self, rule, jsFnc, profile=False):
    """
    Description:
    -----------

    :param rule:
    :param jsFnc:
    :param profile:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self.__events[rule] = jsFnc

  def key(self, key_code, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    :param key_code:
    :param jsFnc:
    :param profile:
    :param reset:
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    tag = "event.which == %s" % key_code
    if reset or tag not in self.__events:
      self.__events[tag] = []
    self.__events[tag].extend(jsFnc)

  def enter(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(13, jsFnc, profile, reset)

  def tab(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(9, jsFnc, profile, reset)

  def backspace(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(8, jsFnc, profile, reset)

  def shift_with(self, key, jsFnc, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param key:
    :param jsFnc:
    :param profile:
    """
    self.custom("(event.shiftKey) && (event.which == %s)" % ord(key), jsFnc, profile)

  def shift(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(16, jsFnc, profile, reset)

  def control(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(17, jsFnc, profile, reset)

  def alt(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(18, jsFnc, profile, reset)

  def space(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(32, jsFnc, profile, reset)

  def right(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(39, jsFnc, profile, reset)

  def left(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(37, jsFnc, profile, reset)

  def up(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(38, jsFnc, profile, reset)

  def down(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(40, jsFnc, profile, reset)

  def delete(self, jsFnc, profile=False, reset=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    """
    self.key(46, jsFnc, profile, reset)

  def get_event(self):
    """
    Description:
    -----------

    """
    event = []
    for k, jsFnc in self.__events.items():
      event.append("if(%s){ %s }" % (k, JsUtils.jsConvertFncs(jsFnc, toStr=True)))
    return event
