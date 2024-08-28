#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.js import JsUtils


class KeyCode:

    def __init__(self, component: Optional[primitives.HtmlModel] = None, source_event: Optional[str] = None, page=None):
        self.__events_per_source, self._component, self.source_event = {}, component, source_event or component.dom.varId
        self._page = page or self._component.page

    def custom(self, rule: str, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
               source_event: Optional[str] = None):
        """
        :param rule: Bespoke keys combination
        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source component for the event
        """
        if not profile and self._page.profile:
            if self._component is not None:
                profile = {"name": "%s[key=%s]" % (self._component.html_code, rule)}
            else:
                profile = {"name": "Page[key=%s]" % rule}
        source_event = source_event or self.source_event
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if source_event not in self.__events_per_source:
            self.__events_per_source[source_event] = {}
        self.__events_per_source[source_event].setdefault(rule, {})["content"] = js_funcs
        self.__events_per_source[source_event][rule]['profile'] = profile

    def key(self, key_code: int, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            reset: bool = False, source_event: Optional[str] = None):
        """

        :param key_code: The key code
        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        if not profile and self._page.profile:
            if self._component is not None:
                profile = {"name": "%s[key=%s]" % (self._component.html_code, key_code)}
            else:
                profile = {"name": "Page[key=%s]" % key_code}
        source_event = source_event or self.source_event
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        tag = "event.which == %s" % key_code
        if reset or source_event not in self.__events_per_source:
            self.__events_per_source[source_event] = {}
        self.__events_per_source[source_event].setdefault(tag, {}).setdefault("content", []).extend(js_funcs)
        self.__events_per_source[source_event][tag]['profile'] = profile

    def any(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            source_event: Optional[str] = None):
        """   Trigger event for any keycodes.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source component for the event
        """
        self.custom("true", js_funcs, profile, source_event)

    def enter(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(13, js_funcs, profile, reset, source_event)

    def tab(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(9, js_funcs, profile, reset, source_event)

    def backspace(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                  reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(8, js_funcs, profile, reset, source_event)

    def shift_with(self, key: str, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                   source_event: Optional[str] = None):
        """

        :param str key:
        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source component for the event
        """
        self.custom("(event.shiftKey) && (event.which == %s)" % ord(key), js_funcs, profile, source_event)

    def save(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
             source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The source component for the event
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.custom("(event.ctrlKey) && (event.which == 83)", ["event.preventDefault()"] + js_funcs + ["return false"],
                    profile, source_event)

    def shift(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(16, js_funcs, profile, reset, source_event)

    def control(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
                reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(17, js_funcs, profile, reset, source_event)

    def alt(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
            reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(18, js_funcs, profile, reset, source_event)

    def space(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              reset: bool = False, source_event: Optional[str] = None):
        """
        Add an event on the space key.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(32, js_funcs, profile, reset, source_event)

    def right(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
              reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(39, js_funcs, profile, reset, source_event)

    def left(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
             reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(37, js_funcs, profile, reset, source_event)

    def up(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
           reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(38, js_funcs, profile, reset, source_event)

    def down(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
             reset: bool = False, source_event: Optional[str] = None):
        """

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(40, js_funcs, profile, reset, source_event)

    def delete(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
               reset: bool = False, source_event: Optional[str] = None):
        """
        Keycode 46, the sup key

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(46, js_funcs, profile, reset, source_event)

    def escape(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None,
               reset: bool = False, source_event: Optional[str] = None):
        """
        Keycode 27, the escape key.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param reset: Optional. Flag to reset the events sequence
        :param source_event: Optional. The source component for the event
        """
        self.key(27, js_funcs, profile, reset, source_event)

    def get_event(self):
        """ Return the complete definition for the key event. """
        event = {}
        for source, event_funcs in self.__events_per_source.items():
            event[source] = {"content": [], 'profile': self._page.profile}
            for rule, js_funcs in event_funcs.items():
                event[source]["content"].append("if(%s){%s}" % (rule, JsUtils.jsConvertFncs(
                    js_funcs['content'], toStr=True, profile=js_funcs['profile'])))
        return event
