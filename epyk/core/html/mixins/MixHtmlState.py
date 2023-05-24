import os
from pathlib import Path
from typing import Optional

from epyk.core.py import types
from epyk.core.js import JsUtils
from epyk.core.html import Defaults as Default_html


class HtmlStates:

    def loading(
            self,
            status: bool = True,
            label: str = None,
            data: types.JS_DATA_TYPES = None
    ):
        """
        Display a loading message in the component.

        Usage::

          btn.click([
              t.loading(True, label="`Loading: ${data.result}`", data={"result": "Waiting for response"}),
          ])

        :param status: The message status (true is active)
        :param label: The message template
        :param data: The message parameter to feed the template
        """
        if label is not None:
            self.options.templateLoading = label
        if self.options.templateLoading is None:
            self.options.templateLoading = Default_html.TEMPLATE_LOADING_ONE_LINE
        if status:
            return self.build(data, options={"templateMode": 'loading'})

        if data is None:
            return self.build(self.dom.getAttribute("data-content"))

        return self.build(data)

    def error(
            self,
            status: bool = True,
            label: str = None,
            data: types.JS_DATA_TYPES = None
    ):
        """
        Display an error message in the component.

        Usage::

          btn.click([
              t.error(True, label="`Error: ${data.result}`", data={"result": "Wrong Parameter"}),
          ])

        :param status: The message status (true is active)
        :param label: The message template
        :param data: The message parameter to feed the template
        """
        if label is not None:
            self.options.templateError = label
        if self.options.templateError is None:
            self.options.templateError = Default_html.TEMPLATE_ERROR_ONE_LINE
        if status:
            return self.build(data, options={"templateMode": 'error'})

        if data is None:
            return self.build(self.dom.getAttribute("data-content"))

        return self.build(data)


class HtmlOverlayStates:

    def _add_resource(self) -> str:
      native_path = os.environ.get("NATIVE_JS_PATH")
      js_state_file = "StateTemplate.js"
      js_state_name = "stateTemplate"
      internal_native_path = Path(Path(__file__).resolve().parent, "..", "..", "js", "native", "utils")
      if native_path is None:
        native_path = internal_native_path
      native_builder = Path(native_path, js_state_file)
      internal_native_builder = Path(internal_native_path, js_state_file)
      if native_builder.exists():
        self.page.js.customFile(js_state_file, path=native_path, authorize=True)
        self.page.properties.js.add_constructor(js_state_name, None)
      elif internal_native_builder.exists():
        self.page.js.customFile(js_state_file, path=internal_native_builder, authorize=True)
        self.page.properties.js.add_constructor(js_state_name, None)
      else:
        raise ValueError("%s does not exist" % js_state_file)

      return js_state_name

    def hide_state(
            self,
            component_id: Optional[str] = None
    ):
        """
        Hide the state component.

        :param component_id: The component id if different
        """
        self._add_resource()
        return "hideState(%s)" % (component_id or self.dom.container)

    def state(
            self,
            status: bool = True,
            label: str = None,
            data: types.JS_DATA_TYPES = None,
            options: types.OPTION_TYPE = None,
            css_attrs: types.JS_DATA_TYPES = None,
            component_id: Optional[str] = None,
            mode: str = "loading"
    ):
        """
        Loading component on a chart.

        Usage::

            chart_obj.loading()
            ....
            chart_obj.loading(False)

        :param status: Optional. Specific the status of the display of the loading component
        :param label: Optional. The label to be displayed
        :param data: Optional.
        :param options: Optional.
        :param css_attrs: Optional. Special CSS attributes for the state component
        :param component_id: Optional. The component id if different
        :param mode: Optional. The modal mode error / loading for the message and style
        """
        js_state_name = self._add_resource()
        if label is not None:
            if mode == "loading":
                self.options.templateLoading = label
            elif mode == "error":
                self.options.templateError = label
        if isinstance(data, dict):
            tmp_data = ["%s: %s" % (JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)) for k, v in
                        data.items()]
            js_data = "{%s}" % ",".join(tmp_data)
        else:
            js_data = JsUtils.jsConvertData(data, None)
        css_attrs = css_attrs or {}
        dflt_css_attrs = {"background": self.page.theme.greys[0]}
        for k, v in dflt_css_attrs.items():
            if k not in css_attrs:
                css_attrs[k] = v
        options = options or {}
        options["templateMode"] = mode
        return "%s(%s, %s, %s, %s, %s)" % (
            js_state_name,
            JsUtils.jsConvertData(status, None),
            component_id or self.dom.container,
            js_data,
            self.options.config_js(options),
            JsUtils.jsConvertData(css_attrs, None)
        )

    def loading(
            self,
            status: bool = True,
            label: str = None,
            data: types.JS_DATA_TYPES = None,
            options: types.OPTION_TYPE = None,
            css_attrs: types.JS_DATA_TYPES = None,
            component_id: Optional[str] = None
    ):
        """


        Usage::

          tabledata = []
          tbl = page.ui.tables.tabulator(tabledata)
          btn1 = page.ui.buttons.refresh("refresh")
          btn1.click([
              btn1.loading(),
              tbl.loading(),
              page.js.delay([tbl.error(True)], 10)
          ])


        :param status:
        :param label:
        :param data:
        :param options:
        :param css_attrs:
        :param component_id:
        """
        if label is None and self.options.templateLoading is None:
            label = Default_html.TEMPLATE_LOADING_ONE_LINE
        return self.state(status, label, data, options, css_attrs, component_id, mode="loading")

    def error(
            self,
            status: bool = True,
            label: str = None,
            data: types.JS_DATA_TYPES = None,
            options: types.OPTION_TYPE = None,
            css_attrs: types.JS_DATA_TYPES = None,
            component_id: Optional[str] = None
    ):
        """


        Usage::

          tabledata = []
          tbl = page.ui.tables.tabulator(tabledata)
          btn1 = page.ui.buttons.refresh("refresh")
          btn1.click([
              btn1.loading(),
              tbl.loading(),
              page.js.delay([tbl.error(True)], 10)
          ])


        :param status:
        :param label:
        :param data:
        :param options:
        :param css_attrs:
        :param component_id:
        """
        if label is None and self.options.templateError is None:
            label = Default_html.TEMPLATE_ERROR_ONE_LINE
        return self.state(status, label, data, options, css_attrs, component_id, mode="error")
