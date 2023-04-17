from epyk.core.html.options import Options


class FixedHeater(Options):

    def activate(self):
        self.header = True
        return self

    @property
    def header(self):
        return self._config_get()

    @header.setter
    def header(self, val):
        self._config(val)

    @property
    def headerOffset(self):
        return self._config_get()

    @headerOffset.setter
    def headerOffset(self, val):
        self._config(val)

    @property
    def footer(self):
        return self._config_get()

    @footer.setter
    def footer(self, val):
        self._config(val)

    @property
    def footerOffset(self):
        return self._config_get()

    @footerOffset.setter
    def footerOffset(self, val):
        self._config(val)
