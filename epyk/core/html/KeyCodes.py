#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils


class KeyCode(object):

  def __init__(self, component, source_event=None):
    self.__events_per_source, self._component, self.source_event = {}, component, source_event or component.dom.varId

  def custom(self, rule, jsFnc, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param rule:
    :param jsFnc:
    :param profile:
    :param source_event: String. Optional. The source component for the event
    """
    source_event = source_event or self.source_event
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    if source_event not in self.__events_per_source:
      self.__events_per_source[source_event] = {}
    self.__events_per_source[source_event].setdefault(rule, {})["content"] = jsFnc
    self.__events_per_source[source_event][rule]['profile'] = profile

  def key(self, key_code, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param key_code:
    :param jsFnc:
    :param profile:
    :param reset:
    :param source_event: String. Optional. The source component for the event
    """
    source_event = source_event or self.source_event
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    tag = "event.which == %s" % key_code
    if reset or source_event not in self.__events_per_source:
      self.__events_per_source[source_event] = {}
    self.__events_per_source[source_event].setdefault(tag, {}).setdefault("content", []).extend(jsFnc)
    self.__events_per_source[source_event][tag]['profile'] = profile

  def enter(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(13, jsFnc, profile, reset, source_event)

  def tab(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(9, jsFnc, profile, reset, source_event)

  def backspace(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(8, jsFnc, profile, reset, source_event)

  def shift_with(self, key, jsFnc, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param key:
    :param jsFnc:
    :param profile:
    :param source_event: String. Optional. The source component for the event
    """
    self.custom("(event.shiftKey) && (event.which == %s)" % ord(key), jsFnc, profile, source_event)

  def save(self, jsFnc, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc:
    :param profile:
    :param source_event: String. Optional. The source component for the event
    """
    if not isinstance(jsFnc, list):
      jsFnc = [jsFnc]
    self.custom("(event.ctrlKey) && (event.which == 83)", ["event.preventDefault()"] + jsFnc + ["return false"], profile, source_event)

  def shift(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(16, jsFnc, profile, reset, source_event)

  def control(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(17, jsFnc, profile, reset, source_event)

  def alt(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(18, jsFnc, profile, reset, source_event)

  def space(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Add an event on the space key

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event:
    """
    self.key(32, jsFnc, profile, reset, source_event)

  def right(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(39, jsFnc, profile, reset, source_event)

  def left(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(37, jsFnc, profile, reset, source_event)

  def up(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(38, jsFnc, profile, reset, source_event)

  def down(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(40, jsFnc, profile, reset, source_event)

  def delete(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Keycode 46, the sup key

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(46, jsFnc, profile, reset, source_event)

  def escape(self, jsFnc, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Keycode 27, the escape key

    Attributes:
    ----------
    :param jsFnc: Array. Tje Javascript events
    :param profile:
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(27, jsFnc, profile, reset, source_event)

  def get_event(self):
    """
    Description:
    -----------
    Return the complete definition for the key event.
    """
    event = {}
    for source, event_fncs in self.__events_per_source.items():
      event[source] = {"content": [], 'profile': False}
      for rule, jsFnc in event_fncs.items():
        event[source]["content"].append("if(%s){%s}" % (rule, JsUtils.jsConvertFncs(jsFnc['content'], toStr=True)))
    return event
