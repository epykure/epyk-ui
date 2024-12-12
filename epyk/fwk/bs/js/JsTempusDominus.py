from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class TempusDominus(JsPackage):

    @property
    def dates(self):
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates" % self.varId)

        return ""

    def disable(self):
        """Returns an array of DateTime of the selected date(s).

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.disable()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('disable')" % self.varId)

    def enable(self):
        """Enables the input element, the component is attached to, by removing disabled attribute from it.

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.disable()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('enable')" % self.varId)

    def clear(self):
        """Returns an array of DateTime of the selected date(s).

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates.clear()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('clear')" % self.varId)

    def viewDate(self, date):
        """Returns an array of DateTime of the selected date(s).

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        date = JsUtils.jsConvertData(date, None)
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.viewDate = %s" % (self.varId, date))

        return JsUtils.jsWrap("%s.datetimepicker('viewDate', %s)" % (self.varId, date))

    def isPicked(self, date):
        """Returns true if the target date is part of the selected dates array. If unit is provided then a granularity
        to that unit will be used.

        """
        date = JsUtils.jsConvertData(date, None)
        return JsUtils.jsWrap("%s.isPicked(%s)" % (self.varId, date))

    def parseInput(self, value):
        """Returns an array of DateTime of the selected date(s).

        """
        value = JsUtils.jsConvertData(value, None)
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates.parseInput(%s)" % (self.varId, value))

        return JsUtils.jsWrap("new Date(%s)" % value)

    def picked(self):
        """Returns an array of DateTime of the selected date(s).

        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates.picked" % self.varId)

        return ""

    def lastPicked(self):
        """Returns the last picked DateTime of the selected date(s).

        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates.lastPicked" % self.varId)

        return ""

    def lastPickedIndex(self):
        """Returns the length of picked dates -1 or 0 if none are selected.

        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.dates.lastPickedIndex" % self.varId)

        return ""

    def date(self, value):
        """Change the selected dat value"""
        value = JsUtils.jsConvertData(value, None)
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return ""

        return JsUtils.jsWrap('''$(function(){let date = new Date(%s); %s.datetimepicker('date', date)})''' % (
            value, self.varId))

    def setOption(self, name: str, value):
        """Set a DatePicker option"""
        name = JsUtils.jsConvertData(name, None)
        value = JsUtils.jsConvertData(value, None)
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return ""

        return JsUtils.jsWrap("$(function(){%s.datetimepicker(%s, %s)})" % (self.varId, name, value))

    def hide(self):
        """Hides the widget

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.hide()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('hide')" % self.varId)

    def show(self):
        """Shows the widget

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.hide()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('show')" % self.varId)

    def toggle(self):
        """Shows or hides the widget

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.hide()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('toggle')" % self.varId)

    def destroy(self):
        """Destroys the widget and removes all attached event listeners

        `DatePicker Functions <https://getdatepicker.com/5-4/Functions/>`_
        """
        if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
            return JsUtils.jsWrap("%s.hide()" % self.varId)

        return JsUtils.jsWrap("%s.datetimepicker('destroy')" % self.varId)
