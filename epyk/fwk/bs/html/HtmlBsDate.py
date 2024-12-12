from epyk.core.py import primitives, types
from epyk.core.html.Html import Component
from epyk.core.js.packages import JsQuery
from epyk.fwk.bs.options import OptBsDT
from epyk.fwk.bs.dom import DomBsDatePicker
from epyk.fwk.bs.js import JsTempusDominus


class BsDatePicker(Component):
    css_classes = ["input-group", "date"]
    name = "DatePicker Tempus Dominus"
    version: str = None
    str_repr = '''
<div class="form-group">
    <div {attrs} data-target-input="nearest">
        <input type="text" class="form-control datetimepicker-input" data-target="#{htmlCode}"/>
        <div class="input-group-append" data-target="#{htmlCode}" data-toggle="datetimepicker">
            <div class="input-group-text" style="height:100%"><i class="{calendar}"></i></div>
        </div>
    </div>
</div>'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.options, "display"):
            self.options.display.icons.next = self.page.icons.get("next")['icon']
            self.options.display.icons.previous = self.page.icons.get("previous")['icon']
            self.options.display.icons.today = self.page.icons.get("today")['icon']
            self.options.display.icons.close = self.page.icons.get("close")['icon']
            self.options.display.icons.time = self.page.icons.get("time")['icon']
        else:
            self.options.icons.next = self.page.icons.get("next")['icon']
            self.options.icons.previous = self.page.icons.get("previous")['icon']
            self.options.icons.today = self.page.icons.get("today")['icon']
            self.options.icons.close = self.page.icons.get("close")['icon']
            self.options.icons.time = self.page.icons.get("time")['icon']

    def get_requirements(self, page: primitives.PageModel, options: types.OPTION_TYPE = None) -> tuple:
        """Change the list of requirements for this package depending on the defined version.

        :param page;
        :param options;
        """
        version = self.version or page.imports.pkgs.get('tempus-dominus').version[0]
        if version > "6.0.0":
            # recent versions
            self._option_cls = OptBsDT.DT6
            self.set_builder("tempusDominus6", in_module="DateTempusDominus")
            return '@popperjs/core', 'tempus-dominus'

        if version.startswith("5."):
            self._option_cls = OptBsDT.DT
            self.set_builder("tempusDominus5", in_module="DateTempusDominus")
            return 'tempusdominus-bootstrap-5', page.icons.family

        # Old versions
        self._option_cls = OptBsDT.DT
        self.set_builder("tempusDominus4", in_module="DateTempusDominus")
        return 'tempusdominus-bootstrap-4', page.icons.family

    @property
    def options(self) -> OptBsDT.DT:
        """The component options"""
        return super().options

    @property
    def dom(self) -> DomBsDatePicker.DomDate:
        """The common DOM properties"""
        if self._dom is None:
            self._dom = DomBsDatePicker.DomDate(component=self, page=self.page)
        return self._dom

    @property
    def js(self) -> JsTempusDominus.TempusDominus:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            if self.page.imports.pkgs.get('tempus-dominus').version[0] > "6.0.0":
                self._js = JsTempusDominus.TempusDominus(page=self.page, js_code="window['%sId']" % self.html_code, set_var=False, component=self)
            else:
                self._js = JsTempusDominus.TempusDominus(
                    page=self.page, js_code=JsQuery.decorate_var("#%s" % self.html_code), set_var=False, component=self)
        return self._js

    def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs;
        :param profile;
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self.on(
            "change.datetimepicker", js_funcs=js_funcs, profile=profile,
            source_event=JsQuery.decorate_var("#%s" % self.html_code), method="on")

    def write_values(self) -> dict:
        return {"calendar": self.page.icons.get("calendar")['icon']}
