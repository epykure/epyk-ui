#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options


class OptionsDt(Options):

    @property
    def date(self):
        """Returns the component's model current date, a moment object or null if not set.

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/#date>`_
        """
        return self._config_get()

    @date.setter
    def date(self, dt):
        self._config(dt)

    @property
    def dayViewHeaderFormat(self) -> str:
        """Changes the heading of the datepicker when in "days" view.

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/#dayviewheaderformat>`_
        """
        return self._config_get('MMMM YYYY')

    @dayViewHeaderFormat.setter
    def dayViewHeaderFormat(self, dt):
        self._config(dt)

    @property
    def sideBySide(self) -> bool:
        """

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get(False)

    @sideBySide.setter
    def sideBySide(self, flag: bool):
        self._config(flag)

    @property
    def inline(self) -> bool:
        """

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get(False)

    @inline.setter
    def inline(self, flag: bool):
        self._config(flag)

    @property
    def daysOfWeekDisabled(self) -> bool:
        """

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get()

    @daysOfWeekDisabled.setter
    def daysOfWeekDisabled(self, flag: bool):
        self._config(flag)

    @property
    def viewMode(self) -> bool:
        """

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get()

    @viewMode.setter
    def viewMode(self, flag: bool):
        self._config(flag)

    @property
    def defaultDate(self) -> bool:
        """

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get(False)

    @defaultDate.setter
    def defaultDate(self, flag: bool):
        self._config(flag)

    @property
    def format(self) -> bool:
        """See momentjs' docs for valid formats.
        Format also dictates what components are shown, e.g. MM/dd/YYYY will not display the time picker.

        `bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/#format>`_
        """
        return self._config_get(False)

    @format.setter
    def format(self, flag: bool):
        self._config(flag)

    @property
    def locale(self) -> bool:
        """

        `eonasdan <https://eonasdan.github.io/bootstrap-datetimepicker/Options/>`_
        """
        return self._config_get(False)

    @locale.setter
    def locale(self, flag: bool):
        self._config(flag)

    @property
    def options(self) -> dict:
        """Returns the components current options object.
        Note that the changing the values of the returned object does not change the components actual configuration.
        Use options(options) to set the components options massively or the other methods for setting config options
        individually.

        `Bootstrap-datetimepicker <https://eonasdan.github.io/bootstrap-datetimepicker/Options/#options_1>`_
        """
        return self.page._jsStyles

    @options.setter
    def options(self, otps):
        if otps is not None:
            self.page._jsStyles.update(otps)

    @property
    def stepping(self) -> int:
        """Number of minutes the up/down arrow's will move the minutes value in the time picker.

        `eonasdan <https://eonasdan.github.io/bootstrap-datetimepicker/Options/#stepping>`_
        """
        return self._config_get(1)

    @stepping.setter
    def stepping(self, num: int):
        self._config(num)
