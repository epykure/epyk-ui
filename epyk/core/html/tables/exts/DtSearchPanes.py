from epyk.core.html.options import Options


class SearchPanes(Options):
    class DtOps(Options):
        @property
        def paging(self):
            return self._config_get()

        @paging.setter
        def paging(self, val):
            self._config(val)

        @property
        def pagingType(self):
            return self._config_get()

        @pagingType.setter
        def pagingType(self, val):
            self._config(val)

        @property
        def searching(self):
            return self._config_get()

        @searching.setter
        def searching(self, val):
            self._config(val)

    class Panes(Options):
        class Options(Options):

            @property
            def label(self):
                return self._config_get()

            @label.setter
            def label(self, val):
                self._config(val)

        class DtOps(Options):
            @property
            def paging(self):
                return self._config_get()

            @paging.setter
            def paging(self, val):
                self._config(val)

            @property
            def pagingType(self):
                return self._config_get()

            @pagingType.setter
            def pagingType(self, val):
                self._config(val)

            @property
            def searching(self):
                return self._config_get()

            @searching.setter
            def searching(self, val):
                self._config(val)

        @property
        def className(self):
            return self._config_get()

        @className.setter
        def className(self, val):
            self._config(val)

        @property
        def header(self):
            return self._config_get()

        @header.setter
        def header(self, val):
            self._config(val)

        @property
        def panes_options(self):
            return self._config_sub_data_enum('options', self.Options)

        @property
        def dtOpts(self):
            return self._config_sub_data('dtOpts', self.DtOps)

    @property
    def cascadePanes(self):
        """
        As standard, SearchPanes will display all of the options for that column throughout its operation.

        When searchPanes.cascadePanes is set to true, the panes will remove options which are no longer present in the
        currently displayed DataTable.
        The cascade action will occur when a selection or a deselection is made in one of the panes.

        This is useful when dealing with large data sets with many different options as they are narrowed down accordingly
        as selections proceed.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.cascadePanes
        """
        return self._config_get()

    @cascadePanes.setter
    def cascadePanes(self, val):
        self._config(val)

    @property
    def clear(self):
        """
        As standard, SearchPanes will display the buttons which allow selections to be cleared in individual panes and
        across all panes.

        When searchPanes.clear is set to false, the clear buttons will not be present.

        The searchPanes.clear functionality is useful when wanting to quickly deselect all of the options in a pane.
        It is useful to be able to disable these buttons, for example on smaller tables with less options it may be
        preferrable to employ a custom user interface.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.clear
        """
        return self._config_get()

    @clear.setter
    def clear(self, val):
        self._config(val)

    @property
    def columns(self):
        """
        As standard, SearchPanes will consider all of the columns when creating searchPanes.

        When searchPanes.columns is defined with an array of numbers, then only the columns with those indexes will be
        considered when creating panes.
        Note they still may not be displayed based upon the calculations of searchPanes.threshold or
        columns.searchPanes.threshold.

        The searchPanes.columns functionality is useful when wanting to restrict which columns will be considered when
        displaying panes.
        This may result in faster load times as there is not as much validation to be done.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.columns
        """
        return self._config_get()

    @columns.setter
    def columns(self, val):
        self._config(val)

    @property
    def controls(self):
        """
        As standard, SearchPanes will be displayed with the control buttons included in the interface with searching
        enabled.

        However if the value of searchPanes.controls is set to false then the control buttons will no longer be displayed
        and searching will be disabled in all of the panes.

        The control buttons can be hidden and searching disabled for individual panes by the columns.searchPanes.controls
        option.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.controls
        """
        return self._config_get()

    @controls.setter
    def controls(self, val):
        self._config(val)

    @property
    def dataLength(self):
        """
        This is useful as it prevents the searchPanes cells becoming mishapen and overpopulated when the table contains
        long strings.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.dataLength
        """
        return self._config_get()

    @dataLength.setter
    def dataLength(self, val):
        self._config(val)

    @property
    def emptyMessage(self):
        """
        Empty cells will be represented in the panes by the option searchPanes.emptyMessage. This is useful as it's a more
        user-friendly way than just having a blank cell.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.emptyMessage
        """
        return self._config_get()

    @emptyMessage.setter
    def emptyMessage(self, val):
        self._config(val)

    @property
    def hideCount(self):
        """
        As standard, SearchPanes will be displayed with the count column included in the table.

        However if the value of searchPanes.hideCount is set to true then the count column won't be displayed in any of
        the panes.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.hideCount
        """
        return self._config_get()

    @hideCount.setter
    def hideCount(self, val):
        self._config(val)

    @property
    def layout(self):
        """
        By setting the searchPanes.layout parameter to columns-3, the panes will be displayed in 3 columns.

        There are 6 sizes supported from 1 pane in a row to 6 panes in a row. Altering the number at the end of columns-
        will alter the number of panes on a row.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.layout
        """
        return self._config_get()

    @layout.setter
    def layout(self, val):
        self._config(val)

    @property
    def orderable(self):
        """
        As standard, SearchPanes will be displayed with the ordering buttons included in the interface, allowing the user
        to change the order of the selections in each pane.

        However if the value of searchPanes.orderable is set to false then the ordering buttons will no longer be displayed
        in any of the panes.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.orderable
        """
        return self._config_get()

    @orderable.setter
    def orderable(self, val):
        self._config(val)

    @property
    def threshold(self):
        """
        Set the minimum number of unique values needed in the columns to display that pane.

        As standard, columns must have a uniqueness ratio of 0.6. This is the ratio of different values throughout the
        column to the number of total rows.
        If all rows are unique, this will be 1; as the value drops towards 0, this means values are more often repeated.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.threshold
        """
        return self._config_get()

    @threshold.setter
    def threshold(self, val):
        self._config(val)

    @property
    def viewTotal(self):
        """
        Update the count column when searching to show visible count.

        By setting the searchPanes.viewTotal parameter to true, the message displayed in the count column will change when
        a search is applied to the DataTable.

        As standard, SearchPanes will set the count column to display the total number of different values visible in the
        column when no filtering is applied.
        When filtering is active the count column will display the number of entries that satisfy this condition currently
        on display followed in brackets by the total in the table which satisfy the condition.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.viewTotal
        """
        return self._config_get()

    @viewTotal.setter
    def viewTotal(self, val):
        self._config(val)

    @property
    def dtOpts(self):
        """
        This is useful as it prevents the searchPanes cells becoming mishapen and overpopulated when the table contains
        long strings.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.dtOpts
        """
        return self._config_sub_data('dtOps', self.DtOps)

    @property
    def panes(self):
        """
        Define custom panes to filter across all columns.

        Related Pages:

          https://datatables.net/reference/option/searchPanes.panes
        """
        return self._config_sub_data_enum('panes', self.Panes)
