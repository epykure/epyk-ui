#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils


class KeyCode(object):

  def __init__(self, component, source_event=None):
    self.__events_per_source, self._component, self.source_event = {}, component, source_event or component.dom.varId

  def custom(self, rule, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param rule:
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source component for the event
    """
    source_event = source_event or self.source_event
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if source_event not in self.__events_per_source:
      self.__events_per_source[source_event] = {}
    self.__events_per_source[source_event].setdefault(rule, {})["content"] = js_funcs
    self.__events_per_source[source_event][rule]['profile'] = profile

  def key(self, key_code, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param key_code:
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset:
    :param source_event: String. Optional. The source component for the event
    """
    source_event = source_event or self.source_event
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    tag = "event.which == %s" % key_code
    if reset or source_event not in self.__events_per_source:
      self.__events_per_source[source_event] = {}
    self.__events_per_source[source_event].setdefault(tag, {}).setdefault("content", []).extend(js_funcs)
    self.__events_per_source[source_event][tag]['profile'] = profile

  def any(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------
    Trigger event for any keycodes.

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source component for the event
    """
    self.custom("true", js_funcs, profile, source_event)

  def enter(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(13, js_funcs, profile, reset, source_event)

  def tab(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(9, js_funcs, profile, reset, source_event)

  def backspace(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(8, js_funcs, profile, reset, source_event)

  def shift_with(self, key, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param key:
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source component for the event
    """
    self.custom("(event.shiftKey) && (event.which == %s)" % ord(key), js_funcs, profile, source_event)

  def save(self, js_funcs, profile=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event: String. Optional. The source component for the event
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.custom("(event.ctrlKey) && (event.which == 83)", ["event.preventDefault()"] + js_funcs + ["return false"], profile, source_event)

  def shift(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(16, js_funcs, profile, reset, source_event)

  def control(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(17, js_funcs, profile, reset, source_event)

  def alt(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(18, js_funcs, profile, reset, source_event)

  def space(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Add an event on the space key

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event:
    """
    self.key(32, js_funcs, profile, reset, source_event)

  def right(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(39, js_funcs, profile, reset, source_event)

  def left(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(37, js_funcs, profile, reset, source_event)

  def up(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed.
    :param source_event: String. Optional. The source component for the event.
    """
    self.key(38, js_funcs, profile, reset, source_event)

  def down(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(40, js_funcs, profile, reset, source_event)

  def delete(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Keycode 46, the sup key

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(46, js_funcs, profile, reset, source_event)

  def escape(self, js_funcs, profile=False, reset=False, source_event=None):
    """
    Description:
    -----------
    Keycode 27, the escape key

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param reset: Boolean. To set if the event should be refreshed
    :param source_event: String. Optional. The source component for the event
    """
    self.key(27, js_funcs, profile, reset, source_event)

  def get_event(self):
    """
    Description:
    -----------
    Return the complete definition for the key event.
    """
    event = {}
    for source, event_fncs in self.__events_per_source.items():
      event[source] = {"content": [], 'profile': False}
      for rule, js_funcs in event_fncs.items():
        event[source]["content"].append("if(%s){%s}" % (rule, JsUtils.jsConvertFncs(js_funcs['content'], toStr=True)))
    return event
