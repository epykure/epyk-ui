from epyk.core.html.options import Options, OptionsWithTemplates


class OptionsTableRow(Options):
    @property
    def cssClasses(self):
        """
    """
        return self._config_get([])

    @cssClasses.setter
    def cssClasses(self, values):
        self._config(values)


class OptionsTableCell(OptionsWithTemplates):

    @property
    def cssClasses(self):
        """
    """
        return self._config_get([])

    @cssClasses.setter
    def cssClasses(self, values):
        self._config(values)

    @property
    def center(self):
        """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
        return self._config_get()

    @center.setter
    def center(self, flag):
        if flag:
            self.component.attr["class"].add("text-center")

    def position(self, alias):
        """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
        self.component.attr["class"].add("text-%s" % alias)

    def align(self, alias):
        """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
        self.component.attr["class"].add("align-%s" % alias)

    def padding(self, value, position="s"):
        """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/utilities/spacing/
    """
        self.component.attr["class"].add("p%s-%s" % (position, value))

    def margin(self, value, position="s"):
        """
    Use the predefined bootstrap classes to align the cells content.

    Related Pages:

      https://getbootstrap.com/docs/5.1/utilities/spacing/
    """
        self.component.attr["class"].add("m%s-%s" % (position, value))


class OptionsBasic(OptionsWithTemplates):
    @property
    def bordered(self):
        """
    Add .table-bordered for borders on all sides of the table and cells.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
        return self._config_get()

    @bordered.setter
    def bordered(self, flag):
        if flag:
            self.component.attr["class"].add("table-bordered")
        else:
            self.component.attr["class"].add("table-borderless")

    @property
    def hover(self):
        """
    Add .table-hover to enable a hover state on table rows within a <tbody>.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
        return self._config_get()

    @hover.setter
    def hover(self, flag):
        if flag:
            self.component.attr["class"].add("table-hover")

    def size(self, alias):
        """
    Add .table-sm to make any .table more compact by cutting all cell padding in half.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/#small-tables
    """
        self.component.attr["class"].add("table-%s" % alias)

    @property
    def striped(self):
        """
    Add the striped CSS class from Bootstrap.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
        return self._config_get()

    @striped.setter
    def striped(self, flag):
        if flag:
            self.component.attr["class"].add("table-striped")

    @property
    def responsive(self):
        """
    Make the table responsive using Bootstrap class.

    Related Pages:

      https://getbootstrap.com/docs/5.1/content/tables/
    """
        return self._config_get()

    @responsive.setter
    def responsive(self, flag):
        if flag:
            self.component.attr["class"].add("table-responsive")

    @property
    def rowCssClasses(self):
        """
    """
        return self._config_get([])

    @rowCssClasses.setter
    def rowCssClasses(self, values):
        self._config(values)

    @property
    def colCssClasses(self):
        """
    """
        return self._config_get([])

    @colCssClasses.setter
    def colCssClasses(self, values):
        self._config(values)

    @property
    def with_header(self):
        """
    """
        return self._config_get(True)

    @with_header.setter
    def with_header(self, flag):
        self._config(flag)

    @property
    def with_hover(self):
        """
    """
        return self._config_get(True)

    @with_hover.setter
    def with_hover(self, flag):
        self._config(flag)
