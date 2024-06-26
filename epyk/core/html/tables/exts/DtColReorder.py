from epyk.core.html.options import Options


class ColReorder(Options):

    def activate(self):
        """
        ColReorder provides the option for end users to reorder columns in a DataTable by click and drag, or for yourself,
        the developer using DataTable, through the API.

        Related Pages:

          https://datatables.net/reference/option/colReorder
        """
        self.realtime = True
        return self

    @property
    def enable(self):
        """
        It can be useful to disable ColReorder's user input controls at certain times, depending on the state of your
        application. This option provides that ability when the table is initially created,
        while the colReorder.enable() and colReorder.disable() methods provide the option to enabling the user
        interaction after the table has been created.

        Related Pages:

          https://datatables.net/reference/option/colReorder.enable
        """
        return self._config_get()

    @enable.setter
    def enable(self, val):
        self._config(val)

    @property
    def fixedColumnsLeft(self):
        """
        When allowing reordering of columns in a table, you may often wish to disallow reordering of certain columns
        (for example locking an index, select or action column to the start of a table). This option provides that ability,
        locking columns counting from the left (colReorder.fixedColumnsRight provides the option to count from the right).

        Related Pages:

          https://datatables.net/reference/option/colReorder.fixedColumnsLeft
        """
        return self._config_get()

    @fixedColumnsLeft.setter
    def fixedColumnsLeft(self, val):
        self._config(val)

    @property
    def fixedColumnsRight(self):
        """
        When allowing reordering of columns in a table, you may often wish to disallow reordering of certain columns
        (for example locking an index, select or action column to the start of a table).
        This option provides that ability, locking columns counting from the right (colReorder.fixedColumnsLeft
        provides the option to count from the left).

        Related Pages:

          https://datatables.net/reference/option/colReorder.fixedColumnsRight
        """
        return self._config_get()

    @fixedColumnsRight.setter
    def fixedColumnsRight(self, val):
        self._config(val)

    @property
    def order(self):
        """
        This option provides the option to define a default order for the columns in a table. Typically you will wish to
        have the columns in the order defined in the HTML, or from state saving (stateSave), but if required,
        this option can be used to define an initial default order.

        Related Pages:

          https://datatables.net/reference/option/colReorder.order
        """
        return self._config_get()

    @order.setter
    def order(self, val):
        self._config(val)

    @property
    def realtime(self):
        """ """
        return self._config_get()

    @realtime.setter
    def realtime(self, val):
        self._config(val)
