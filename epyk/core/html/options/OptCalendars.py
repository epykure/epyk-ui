#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Union, Any
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes
from epyk.core.html.options import Options, OptInputs, OptText


class OptionDays(Options):

    @property
    def style(self):
        """ CSS attributes """
        return self.get({})

    @style.setter
    def style(self, css: dict):
        self.set(css)

    @property
    def unit(self):
        """
        Change the unit to the calendar.
        Default is in percentage.

        :prop num: Change the scale
        """
        return self.get(100)

    @unit.setter
    def unit(self, num: float):
        self.set(num)

    @property
    def overload(self):
        """
        Overload style of the day number when workload is above 100%.

        :prop css_attrs: Dictionary. CSS attributes.
        """
        return self.get({})

    @overload.setter
    def overload(self, css_attrs: dict):
        self.set(css_attrs)

    @property
    def number(self):
        """
        CSS Style for the day number.

        :prop css: CSS attributes.
        """
        return self.get({})

    @number.setter
    def number(self, css: dict):
        self.set(css)

    @property
    def today(self):
        """
        CSS Style for the today cell.

        :prop css: CSS attributes
        """
        return self.get({})

    @today.setter
    def today(self, css: dict):
        self.set(css)

    @property
    def header(self):
        """
        CSS Style for the table header.

        :prop css: Dictionary. CSS attributes.
        """
        return self.get({})

    @header.setter
    def header(self, css: dict):
        self.set(css)


class OptionDatePicker(Options):

    @property
    def input(self) -> OptInputs.OptionsDatePicker:
        """ """
        return self._config_sub_data("input", OptInputs.OptionsDatePicker)

    @property
    def label(self) -> OptText.OptionsText:
        """ """
        return self._config_sub_data("label", OptText.OptionsText)


class AmpPlugin(Options):

    @property
    def darkMode(self):
        """Allows dark mode to be used if the user's system settings are set to dark mode.

        `Doc <https://easepick.com/packages/amp-plugin.html#option-darkMode>`_
        """
        return self._config_get(True)

    @darkMode.setter
    def darkMode(self, value: bool):
        self._config(value)

    @property
    def dropdown(self):
        """Enable dropdowns for months, years. If maxYear is null then maxYear will be equal to
        (new Date()).getFullYear(). years can be equal to asc string to change the sort direction.

        `Doc <https://easepick.com/packages/amp-plugin.html#option-dropdown>`_
        """
        return self._config_get(True)

    @dropdown.setter
    def dropdown(self, values: dict):
        self._config(values)

    @property
    def locale(self):
        """Texts for Amp plugin options.

        `Doc <https://easepick.com/packages/amp-plugin.html#option-locale>`_
        """
        return self._config_get()

    @locale.setter
    def locale(self, value: bool):
        self._config(value)

    @property
    def resetButton(self):
        """	Adds a reset button to clear the current selection. It is allowed to pass a custom function that must
        return true to clear the selection.

        `Doc <https://easepick.com/packages/amp-plugin.html#option-resetButton>`_
        """
        return self._config_get(False)

    @resetButton.setter
    def resetButton(self, value: bool):
        self._config(value)

    @property
    def weekNumbers(self):
        """Show week numbers.

        `Doc <https://easepick.com/packages/amp-plugin.html#option-weekNumbers>`_
        """
        return self._config_get(False)

    @weekNumbers.setter
    def weekNumbers(self, value: bool):
        self._config(value)


class KbdPlugin(Options):

    @property
    def dayIndex(self):
        """tabIndex for days elements.

        `Doc <https://easepick.com/packages/kbd-plugin.html#option-dayIndex>`_
        """
        return self._config_get(2)

    @dayIndex.setter
    def dayIndex(self, value: int):
        self._config(value)

    @property
    def unitIndex(self):
        """tabIndex for elements except days elements.

        `Doc <https://easepick.com/packages/kbd-plugin.html#option-unitIndex>`_
        """
        return self._config_get(1)

    @unitIndex.setter
    def unitIndex(self, value: int):
        self._config(value)


class LockPlugin(Options):

    def filter(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Lock days by custom function.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-filter>`_
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile).strip()
        if not str_func.startswith("function(date, picked)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(date, picked){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def inseparable(self):
        """Disable date range selection with locked days.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-inseparable>`_
        """
        return self._config_get(False)

    @inseparable.setter
    def inseparable(self, value: bool):
        self._config(value)

    @property
    def maxDate(self):
        """	The maximum/latest date that can be selected.
        Date Object or Unix Timestamp (with milliseconds) or ISO String.
        When a date is provided as a string, it must be equal to the format option.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-maxDate>`_
        """
        return self._config_get()

    @maxDate.setter
    def maxDate(self, value):
        self._config(value, js_type=True)

    @property
    def maxDays(self):
        """The maximum days of the selected range.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-maxDays>`_
        """
        return self._config_get()

    @maxDays.setter
    def maxDays(self, value: int):
        self._config(value)

    @property
    def minDate(self):
        """The minimum/earliest date that can be selected.
        Date Object or Unix Timestamp (with milliseconds) or ISO String.
        When a date is provided as a string, it must be equal to the format option.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-minDate>`_
        """
        return self._config_get()

    @minDate.setter
    def minDate(self, value):
        self._config(value, js_type=True)

    @property
    def minDays(self):
        """The minimum days of the selected range.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-minDays>`_
        """
        return self._config_get()

    @minDays.setter
    def minDays(self, value: int):
        self._config(value)

    @property
    def presets(self):
        """Disable unallowed presets (when PresetPlugin is included).

        `Doc <https://easepick.com/packages/lock-plugin.html#option-presets>`_
        """
        return self._config_get(True)

    @presets.setter
    def presets(self, value: bool):
        self._config(value)

    @property
    def selectBackward(self):
        """Select second date before the first selected date.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-selectBackward>`_
        """
        return self._config_get(False)

    @selectBackward.setter
    def selectBackward(self, value: bool):
        self._config(value)

    @property
    def selectForward(self):
        """Select second date after the first selected date.

        `Doc <https://easepick.com/packages/lock-plugin.html#option-selectForward>`_
        """
        return self._config_get(False)

    @selectForward.setter
    def selectForward(self, value: bool):
        self._config(value)


class PresetPlugin(Options):

    @property
    def customLabels(self):
        """Define your own labels.

        `Doc <https://easepick.com/packages/preset-plugin.html#option-customLabels>`_
        """
        return self._config_get(True)

    @customLabels.setter
    def customLabels(self, value):
        self._config(value)

    @property
    def customPreset(self):
        """Define your own ranges.

        `Doc <https://easepick.com/packages/preset-plugin.html#option-customPreset>`_
        """
        return self._config_get(True)

    @customPreset.setter
    def customPreset(self, values):
        result = []
        for k, v in values.items():
            result.append("'%s': [%s]" % (k, ",".join(v)))
        self._config("{%s}" % ",".join(result), js_type=True)

    @property
    def position(self):
        """Position of preset block.

        `Doc <https://easepick.com/packages/preset-plugin.html#option-position>`_
        """
        return self._config_get('left')

    @position.setter
    def position(self, value: str):
        self._config(value)


class TimePlugin(Options):

    @property
    def format12(self):
        """Display 12H time.

        `Doc <https://easepick.com/packages/time-plugin.html#option-format12>`_
        """
        return self._config_get(False)

    @format12.setter
    def format12(self, value: bool):
        self._config(value)

    @property
    def seconds(self):
        """Enable seconds picker.

        `Doc <https://easepick.com/packages/time-plugin.html#option-seconds>`_
        """
        return self._config_get(False)

    @seconds.setter
    def seconds(self, value: bool):
        self._config(value)

    @property
    def stepHours(self):
        """Step for hours.

        `Doc <https://easepick.com/packages/time-plugin.html#option-stepHours>`_
        """
        return self._config_get(1)

    @stepHours.setter
    def stepHours(self, value: int):
        self._config(value)

    @property
    def stepMinutes(self):
        """Step for minutes.

        `Doc <https://easepick.com/packages/time-plugin.html#option-stepMinutes>`_
        """
        return self._config_get(5)

    @stepMinutes.setter
    def stepMinutes(self, value: int):
        self._config(value)

    @property
    def stepSeconds(self):
        """Step for minutes.

        `Doc <https://easepick.com/packages/time-plugin.html#option-stepSeconds>`_
        """
        return self._config_get(5)

    @stepSeconds.setter
    def stepSeconds(self, value: int):
        self._config(value)


class RangePlugin(Options):

    @property
    def delimiter(self):
        """Delimiter between dates.

        `Doc <https://easepick.com/packages/range-plugin.html#option-delimiter>`_
        """
        return self._config_get(' - ')

    @delimiter.setter
    def delimiter(self, value: str):
        self._config(value)

    @property
    def elementEnd(self):
        """Bind the datepicker to a element for end date.

        `Doc <https://easepick.com/packages/range-plugin.html#option-elementEnd>`_
        """
        return self._config_get()

    @elementEnd.setter
    def elementEnd(self, value):
        self._config(value)

    @property
    def endDate(self):
        """Preselect end date. Date Object or Unix Timestamp (with milliseconds) or String
        (must be equal to option format).

        `Doc <https://easepick.com/packages/range-plugin.html#option-endDate>`_
        """
        return self._config_get()

    @endDate.setter
    def endDate(self, value):
        self._config(value)

    @property
    def tooltip(self):
        """Showing tooltip with how much days will be selected.

        `Doc <https://easepick.com/packages/range-plugin.html#option-tooltip>`_
        """
        return self._config_get(True)

    @tooltip.setter
    def tooltip(self, value: bool):
        self._config(value)

    def tooltipNumber(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """Handling the tooltip number.

        `Doc <https://easepick.com/packages/range-plugin.html#option-tooltipNumber>`_
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile).strip()
        if not str_func.startswith("function(num)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(num){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def repick(self):
        """If date range is already selected, then user can change only one of start date or end date
        (depends on clicked field) instead of new date range.

        `Doc <https://easepick.com/packages/range-plugin.html#option-repick>`_
        """
        return self._config_get(False)

    @repick.setter
    def repick(self, value: bool):
        self._config(value)

    @property
    def startDate(self):
        """Preselect start date. Date Object or Unix Timestamp (with milliseconds) or String
        (must be equal to option format).

        `Doc <https://easepick.com/packages/range-plugin.html#option-startDate>`_
        """
        return self._config_get()

    @startDate.setter
    def startDate(self, value):
        self._config(value)

    @property
    def strict(self):
        """	Disabling the option allows you to select an incomplete range.

        `Doc <https://easepick.com/packages/range-plugin.html#option-strict>`_
        """
        return self._config_get(True)

    @strict.setter
    def strict(self, value: bool):
        self._config(value)

    @property
    def locale(self):
        """Text for the tooltip. Keys depends on option lang (see Intl.PluralRules (opens new window)).


        `Doc <https://easepick.com/packages/range-plugin.html#option-locale>`_
        """
        return self._config_get()

    @locale.setter
    def locale(self, value):
        self._config(value)


class OptionEasePick(Options):
    component_properties = ("css", "plugins")

    @property
    def AmpPlugin(self) -> AmpPlugin:
        """ """
        if "AmpPlugin" not in self.plugins:
            self.plugins.append("AmpPlugin")
        return self._config_sub_data("AmpPlugin", AmpPlugin)

    @property
    def autoApply(self):
        """Hide the apply and cancel buttons, and automatically apply a new date range as soon as two dates are clicked.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(True)

    @autoApply.setter
    def autoApply(self, value: bool):
        self._config(value)

    @property
    def calendars(self):
        """Number of visible months.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(1)

    @calendars.setter
    def calendars(self, value: int):
        self._config(value)

    @property
    def css(self):
        """Pass a CSS file for picker. Don't mix types, if you are using css link then array should only contain links.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(['https://cdn.jsdelivr.net/npm/@easepick/bundle@1.2.1/dist/index.css'])

    @css.setter
    def css(self, css_cls: list):
        self._config(css_cls)

    @property
    def date(self):
        """Preselect date. Date Object or Unix Timestamp (with milliseconds) or String (must be equal to option format).

        `Doc <https://easepick.com/packages/core.html#option-date>`_
        """
        return self._config_get()

    @date.setter
    def date(self, value):
        self._config(value)

    @property
    def element(self):
        """Bind the datepicker to a element. Also is possible to bind to any element (not input) for example you need
        inline calendar.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get([])

    @element.setter
    def element(self, value: str):
        self._config(value, js_type=True)

    @property
    def firstDay(self):
        """Day of start week. (0 - Sunday, 1 - Monday, 2 - Tuesday, etc…).

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get([])

    @firstDay.setter
    def firstDay(self, value: int):
        self._config(value)

    @property
    def format(self):
        """The default output format. See tokens format.

        `Doc <https://easepick.com/packages/core.html>`_
        `Token <https://easepick.com/packages/datetime.html>`_
        """
        return self._config_get([])

    @format.setter
    def format(self, value: str):
        self._config(value)

    @property
    def grid(self):
        """Number of calendar columns.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(1)

    @grid.setter
    def grid(self, value: int):
        self._config(value)

    @property
    def header(self):
        """Add header to calendar.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(False)

    @header.setter
    def header(self, value: Union[bool, str]):
        self._config(value)

    @property
    def inline(self):
        """Show calendar inline.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(False)

    @inline.setter
    def inline(self, value: bool):
        self._config(value)

    @property
    def KbdPlugin(self) -> KbdPlugin:
        """ """
        if "KbdPlugin" not in self.plugins:
            self.plugins.append("KbdPlugin")
        return self._config_sub_data("KbdPlugin", KbdPlugin)

    @property
    def lang(self):
        """Preselect date. Date Object or Unix Timestamp (with milliseconds) or String (must be equal to option format).

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get([])

    @lang.setter
    def lang(self, value: str):
        self._config(value)

    @property
    def locale(self):
        """Icon and text for buttons.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get([])

    @property
    def LockPlugin(self) -> LockPlugin:
        """ """
        if "LockPlugin" not in self.plugins:
            self.plugins.append("LockPlugin")
        return self._config_sub_data("LockPlugin", LockPlugin)

    @locale.setter
    def locale(self, value: str):
        self._config(value)

    @property
    def plugins(self):
        """Add readonly attribute to element.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get([])

    @plugins.setter
    def plugins(self, values: list):
        self._config(values)

    @property
    def PresetPlugin(self) -> PresetPlugin:
        """ """
        if "PresetPlugin" not in self.plugins:
            if "RangePlugin" not in self.plugins:
                self.plugins.append("RangePlugin")
            self.plugins.append("PresetPlugin")
        return self._config_sub_data("PresetPlugin", PresetPlugin)

    @property
    def RangePlugin(self) -> RangePlugin:
        """ """
        range_plugin = self._config_sub_data("RangePlugin", RangePlugin)
        if "RangePlugin" not in self.plugins:
            self.plugins.append("RangePlugin")
            range_plugin.delimiter = range_plugin.delimiter
        return range_plugin

    @property
    def readonly(self):
        """Add readonly attribute to element.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(True)

    @readonly.setter
    def readonly(self, value: bool):
        self._config(value)

    def setup(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile).strip()
        if not str_func.startswith("function(picker)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(picker){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def TimePlugin(self) -> TimePlugin:
        """ """
        if "TimePlugin" not in self.plugins:
            self.plugins.append("TimePlugin")
        return self._config_sub_data("TimePlugin", TimePlugin)

    @property
    def zIndex(self):
        """zIndex of picker.

        `Doc <https://easepick.com/packages/core.html>`_
        """
        return self._config_get(None)

    @zIndex.setter
    def zIndex(self, value: int):
        self._config(value)


class OptionDatesRange(Options):

    @property
    def input(self) -> OptionEasePick:
        """ """
        return self._config_sub_data("input", OptionEasePick)

    @property
    def label(self) -> OptText.OptionsText:
        """ """
        return self._config_sub_data("label", OptText.OptionsText)
