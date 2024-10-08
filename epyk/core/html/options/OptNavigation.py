
from epyk.core.html.options import Options


class OptionsBar(Options):

    @property
    def avatar(self) -> bool:
        """Add avatar icon to the component"""
        return self.get(False)

    @avatar.setter
    def avatar(self, value: bool):
        self.set(value)
        if value and not self.component.avatar:
            if isinstance(value, bool):
                value = ""
            self.component.avatar = self.page.ui.images.avatar(
                value, options={"status": False}, html_code=self.component.sub_html_code("avatar"))
            self.component.avatar.style.css.display = "inline-block"
            self.component.avatar.options.managed = False
            self.component.avatar.classList.add("html-navbar-avatar")

    @property
    def orient(self) -> str:
        """ Orient definition for the component"""
        return self.get("horizontal")

    @orient.setter
    def orient(self, value: str):
        self.set(value)

    @property
    def scroll(self) -> bool:
        """ Set Scrolling hide effect to the component (only when orient is horizontal)"""
        return self.get(True)

    @scroll.setter
    def scroll(self, flag: bool):
        self.set(flag)

    @property
    def size(self) -> tuple:
        """ Component size (width or height)"""
        return self.get()

    @size.setter
    def size(self, value: tuple):
        self.set(value)

    @property
    def status(self) -> bool:
        """ """
        return self.get(False)

    @status.setter
    def status(self, flag: bool):
        self.set(flag)