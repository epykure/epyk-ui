
from epyk.core.py import types
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class EasePick(JsPackage):
    lib_alias = {'js': '@easepick/bundle'}

    def add(self, duration, unit: str = None):
        """Mutates the original DateTime by adding unit. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param duration:
        :param unit
        """
        duration = JsUtils.jsConvertData(duration, None)
        if unit:
            unit = JsUtils.jsConvertData(duration, unit)
            return JsObject.JsObject.get("%s.add(%s, %s)" % (self.varId, duration, unit))

        return JsObject.JsObject.get("%s.add(%s)" % (self.varId, duration))

    def clear(self):
        """Clear the picker selection.

        `Package Doc <https://easepick.com/packages/core.html#option-plugins>`_
        """
        return JsObject.JsObject.get("%s.clear()" % self.varId)

    def clone(self):
        """Returns a copy of date.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `Package Doc <https://www.npmjs.com/package/@easepick/datetime>`_
        """
        return JsObject.JsObject.get("%s.clone()" % self.varId)

    def destroy(self):
        """Destroy the picker.

        `Package Doc <https://easepick.com/packages/core.html#method-destroy>`_
        """
        return JsObject.JsObject.get("%s.destroy()" % self.varId)

    def diff(self, date, unit: str = None):
        """Returns diff between two DateTime. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.diff(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.diff(%s)" % (self.varId, date))

    def format(self, fmt: str, lang: str = None):
        """Format output. See tokens format for format argument. lang affects month names (MMM, MMMM tokens).

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_

        :param fmt:
        :param lang:
        """
        fmt = JsUtils.jsConvertData(fmt, None)
        if lang:
            lang = JsUtils.jsConvertData(lang, None)
            return JsObject.JsObject.get("%s.format(%s, %s)" % (self.varId, fmt, lang))

        return JsObject.JsObject.get("%s.format(%s)" % (self.varId, fmt))

    def getDate(self):
        """	Get selected date.

        `Package Doc <https://easepick.com/packages/core.html#method-getDate>`_
        """
        return JsObject.JsObject.get("%s.getDate()" % self.varId)

    def getEndDate(self):
        """Return current end of date range as DateTime Object.

        `Package Doc <https://easepick.com/packages/range-plugin.html#method-getEndDate>`_
        """
        return JsObject.JsObject.get("%s.getEndDate()" % self.varId)

    def getStartDate(self):
        """Return current start of date range as DateTime Object.

        `Package Doc <https://easepick.com/packages/range-plugin.html#method-getStartDate>`_
        """
        return JsObject.JsObject.get("%s.getStartDate()" % self.varId)

    def getWeek(self):
        """Returns a week number of date

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `Package Doc <https://www.npmjs.com/package/@easepick/datetime>`_
        """
        return JsObject.JsObject.get("%s.getWeek()" % self.varId)

    def gotoDate(self, date):
        """Change visible month.

        `Package Doc <https://easepick.com/packages/core.html#method-gotoDate>`_
        """
        date = JsUtils.jsConvertData(date, None)
        return JsObject.JsObject.get("%s.gotoDate(%s)" % (self.varId, date))

    def hide(self):
        """Hide the picker.

        `Package Doc <https://easepick.com/packages/core.html#option-plugins>`_
        """
        return JsObject.JsObject.get("%s.hide()" % self.varId)

    def inArray(self, date, inclusivity: bool = False):
        """Find DateTime object in passed DateTime array.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `Package Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param inclusivity:
        """
        date = JsUtils.jsConvertData(date, None)
        inclusivity = JsUtils.jsConvertData(inclusivity, None)
        return JsObject.JsObject.get("%s.inArray(%s, %s)" % (self.varId, date, inclusivity))

    def isAfter(self, date, unit: str = None):
        """Check if a DateTime is after another DateTime.. unit are day, month, year.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `Package Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.isAfter(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.isAfter(%s)" % (self.varId, date))

    def isBefore(self, date, unit: str = None):
        """Check if a DateTime is before another DateTime. unit are day, month, year.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.isBefore(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.isBefore(%s)" % (self.varId, date))

    def isBetween(self, dt1, dt2, inclusivity: bool = False):
        """Check if a DateTime is between two other DateTime.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_

        :param dt1:
        :param dt2:
        :param inclusivity:
        """
        dt1 = JsUtils.jsConvertData(dt1, None)
        dt2 = JsUtils.jsConvertData(dt2, None)
        inclusivity = JsUtils.jsConvertData(inclusivity, None)
        return JsObject.JsObject.get("%s.isBetween(%s, %s, %s)" % (self.varId, dt1, dt2, inclusivity))

    def isShown(self):
        """Determine if the picker is visible or not.

        `Package Doc <https://easepick.com/packages/core.html#option-plugins>`_
        """
        return JsBoolean.JsBoolean.get("%s.isShown()" % self.varId)

    def isSame(self, date, unit: str = None):
        """Check if a DateTime is the same as another DateTime. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.isSame(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.isSame(%s)" % (self.varId, date))

    def isSameOrAfter(self, date, unit: str = None):
        """Check if a DateTime is after or the same as another DateTime. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.isSameOrAfter(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.isSameOrAfter(%s)" % (self.varId, date))

    def isSameOrBefore(self, date, unit: str = None):
        """Check if a DateTime is before or the same as another DateTime. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param date:
        :param unit:
        """
        date = JsUtils.jsConvertData(date, None)
        if unit:
            unit = JsUtils.jsConvertData(unit, None)
            return JsObject.JsObject.get("%s.isSameOrBefore(%s, %s)" % (self.varId, date, unit))

        return JsObject.JsObject.get("%s.isSameOrBefore(%s)" % (self.varId, date))

    def off(self, type, listener = None, options = None):
        """Remove listener from container element.

        `Package Doc <https://easepick.com/packages/core.html#method-off>`_

        :param type:
        :param listener:
        :param options:
        """
        type = JsUtils.jsConvertData(type, None)
        if listener is not None:
            listener = JsUtils.jsConvertData(listener, None)
            if options is not None:
                options = JsUtils.jsConvertData(options, None)
                return JsUtils.jsWrap('''%s.off(%s, %s, %s)''' % (self.varId, type, listener, options))

            return JsUtils.jsWrap('''%s.off(%s, %s)''' % (self.varId, type, listener))

        return JsUtils.jsWrap('''%s.off(%s)''' % (self.varId, type))

    def on(self, type, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, listener: str = None, options = None):
        """Add listener to container element.

        `Package Doc <https://easepick.com/packages/core.html#method-on>`_

        :param type:
        :param js_funcs:
        :param profile:
        :param listener:
        :param options:
        """
        type = JsUtils.jsConvertData(type, None)
        return JsUtils.jsWrap('''%s.on(%s, (e) => { let { view, data, target } = e.detail; %s } )
''' % (self.varId, type, JsUtils.jsConvertFncs(js_funcs, profile=profile, toStr=True)))

    def renderAll(self):
        """Redraw the calendar layout.

        `Package Doc <https://easepick.com/packages/core.html#method-renderAll>`_
        """
        return JsObject.JsObject.get("%s.renderAll()" % self.varId)

    def setDate(self, date):
        """Set date programmatically.

        `Package Doc <https://easepick.com/packages/core.html#method-setDate>`_

        :param date:
        """
        date = JsUtils.jsConvertData(date, None)
        return JsObject.JsObject.get("%s.setDate(%s)" % (self.varId, date))

    def setDateRange(self, date):
        """Set date range. Should be Date Object or Unix Timestamp (with milliseconds) or String (must be equal to
        option format).

        `Package Doc <https://easepick.com/packages/range-plugin.html#method-setDateRange>`_

        :param date:
        """
        date = JsUtils.jsConvertData(date, None)
        return JsObject.JsObject.get("%s.setDateRange(%s)" % (self.varId, date))

    def setEndDate(self, end_date):
        """Set end of date range. Should be Date Object or Unix Timestamp (with milliseconds) or String
        (must be equal to option format).

        `Package Doc <https://easepick.com/packages/range-plugin.html#method-setEndDate>`_
        """
        endDate = JsUtils.jsConvertData(end_date, None)
        return JsObject.JsObject.get("%s.setEndDate(%s)" % (self.varId, endDate))

    def setEndTime(self, end_time):
        """Set end time of date range.

        `Package Doc <https://easepick.com/packages/time-plugin.html#method-setEndTime>`_
        """
        endTime = JsUtils.jsConvertData(end_time, None)
        return JsObject.JsObject.get("%s.setEndTime(%s)" % (self.varId, endTime))

    def setStartDate(self, start_date):
        """Set start of date range. Should be Date Object or Unix Timestamp (with milliseconds) or String
        (must be equal to option format).

        `Package Doc <https://easepick.com/packages/range-plugin.html#method-setStartDate>`_
        """
        startDate = JsUtils.jsConvertData(start_date, None)
        return JsObject.JsObject.get("%s.setStartDate(%s)" % (self.varId, startDate))

    def setStartTime(self, start_time):
        """Set start time of date range.

        `Package Doc <https://easepick.com/packages/time-plugin.html#method-setStartTime>`_
        """
        startTime = JsUtils.jsConvertData(start_time, None)
        return JsObject.JsObject.get("%s.setStartTime(%s)" % (self.varId, startTime))

    def setTime(self, time):
        """Set a time for single date picker.

        `Package Doc <https://easepick.com/packages/time-plugin.html#method-setTime>`_
        """
        time = JsUtils.jsConvertData(time, None)
        return JsObject.JsObject.get("%s.setTime(%s)" % (self.varId, time))

    def show(self):
        """Show the picker.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        """
        return JsObject.JsObject.get("%s.show()" % self.varId)

    def subtract(self, duration, unit: str = None):
        """Mutates the original DateTime by subtracting unit. unit are day, month.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        `NPM Doc <https://www.npmjs.com/package/@easepick/datetime>`_

        :param duration:
        :param unit:
        """
        duration = JsUtils.jsConvertData(duration, None)
        if unit:
            unit = JsUtils.jsConvertData(duration, unit)
            return JsObject.JsObject.get("%s.subtract(%s, %s)" % (self.varId, duration, unit))

        return JsObject.JsObject.get("%s.subtract(%s)" % (self.varId, duration))

    def toJSDate(self):
        """Returns Date object.

        `Package Doc <https://easepick.com/packages/datetime.html#method-getWeek>`_
        """
        return JsObject.JsObject.get("%s.toJSDate()" % self.varId)

    def trigger(self):
        """Dispatch an event.

        `Package Doc <https://easepick.com/packages/core.html#method-trigger>`_
        """
        return JsObject.JsObject.get("%s.trigger()" % self.varId)

    def version(self):
        """return version of picker.

        `Package Doc <https://easepick.com/packages/core.html#option-plugins>`_
        """
        return JsObject.JsObject.get("%s.version" % self.varId)

