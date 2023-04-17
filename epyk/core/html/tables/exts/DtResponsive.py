from epyk.core.html.options import Options


class DataBreakPoints(Options):

    @property
    def name(self):
        """

        Related Pages:

          https://datatables.net/reference/option/responsive.breakpoints
        """
        return self._config_get()

    @name.setter
    def name(self, val):
        self._config(val)

    @property
    def width(self):
        """

        Related Pages:

          https://datatables.net/reference/option/responsive.breakpoints
        """
        return self._config_get()

    @width.setter
    def width(self, val):
        self._config(val)


class DataDetails(Options):

    @property
    def type(self):
        """

        Related Pages:

          https://datatables.net/reference/option/responsive.details
        """
        return self._config_get()

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def display(self):
        """
        Responsive provides the ability to show information about the columns it has hidden using DataTables child rows
        feature (row().child()), but you may wish to display the data in a different manner (potentially so you can use
        the child rows for other actions such as editing) - this parameter provides that ability.

        Related Pages:

          https://datatables.net/reference/option/responsive.details.display
        """
        return self._config_get()

    @display.setter
    def display(self, val):
        self._config(val)

    @property
    def renderer(self):
        """


        Related Pages:

          https://datatables.net/reference/option/responsive.details.renderer
        """
        return self._config_get()

    @renderer.setter
    def renderer(self, val):
        self._config(val)

    @property
    def target(self):
        """

        Related Pages:

          https://datatables.net/reference/option/responsive.details.target
        """
        return self._config_get()

    @target.setter
    def target(self, val):
        self._config(val)


class Responsive(Options):

    def activate(self):
        self.details.type = "column"
        return self

    @property
    def details(self) -> DataDetails:
        """
        Responsive has the ability to use DataTables' child rows feature to show information about any columns which have
        been removed from the display as a child row, which can be particularly useful for displaying complex information
        on small screen devices. Please see the Responsive manual on the details rows for further information.

        Related Pages:

          https://datatables.net/reference/option/responsive.details
        """
        return self._config_sub_data("details", DataDetails)

    @property
    def breakpoints(self) -> DataBreakPoints:
        """
        The visibility of columns in a DataTable with Responsive enabled can be controlled by breakpoints and class names
        matching those breakpoints (and other logical operations) .
        This provides the ability to exactly control which columns in a table will be visible for each device type.
        See the Responsive manual for more information.

        Related Pages:

          https://datatables.net/reference/option/responsive.breakpoints
        """
        return self._config_sub_data("breakpoints", DataBreakPoints)

    @property
    def orthogonal(self):
        """
        When Responsive is asked to show the hidden information about a DataTable row,

        it uses the cell().render() method to access this data for each cell in the row.
        This method provides DataTables ability to make use of orthogonal data - that is,
        the same data but formatted in a different way for different uses.

        Related Pages:

          https://datatables.net/reference/option/responsive.details.target
        """
        return self._config_get()

    @orthogonal.setter
    def orthogonal(self, val):
        self._config(val)
