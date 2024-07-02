#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core import html


class Poller:

    def __init__(self, ui):
        self.page = ui.page

    def toggle(self, time, js_funcs=None, components=None, label: str = None, color: str = None,
               width: Union[tuple, int] = (None, '%'), height: Union[tuple, int] = (20, 'px'),
               align: str = "left", html_code: str = None, options: dict = None,
               profile: Union[dict, bool] = None) -> html.HtmlContainer.Div:
        """

        :tags:
        :categories:

        :param time: Integer. Interval time in second.
        :param js_funcs: String | List. The Javascript functions.
        :param components: List. HTML components to be triggered when activated.
        :param label: String. Optional. The text of label to be added to the component
        :param color: String. Optional. The font color in the component. Default inherit.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param align: String. Optional. A string with the horizontal position of the component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        """
        if components is not None:
            js_funcs = js_funcs or []
            for component in components:
                js_funcs.append(component.dom.trigger("click"))
        container = self.page.ui.div(align=align, height=height, width=width, profile=profile, options=options)
        toggle = self.page.ui.buttons.toggle(None, label, color, width, height, align, html_code, options, profile)
        toggle.style.css.display = "inline-block"
        toggle.switch_text.style.css.hide()
        icon = self.page.ui.icon("clock")
        toggle.toggle(on_funcs=[
            icon.dom.spin(),
            icon.dom.css({"color": self.page.theme.success.base}).r,
            self.page.js.window.setInterval(js_funcs, "%s_timer" % toggle.htmlCode, time * 1000, profile=profile)
        ],
            off_funcs=[
                icon.dom.spin(False),
                icon.dom.css({"color": self.page.theme.danger.base}).r,
                self.page.js.window.clearInterval("%s_timer" % toggle.htmlCode)]
        )
        container.toggle = toggle
        container.add(toggle)
        icon.style.css.margin = "2px 5px 5px 0px"
        # icon.spin()
        container.icon = icon
        container.add(icon)
        html.Html.set_component_skin(container)
        return container

    def live(self, time, js_funcs=None, components=None, icon: str = "circle", width: Union[tuple, int] = (15, "px"),
             height: Union[tuple, int] = (15, "px"), align: str = "left",
             html_code: str = None, profile: Union[dict, bool] = None,
             options: dict = None) -> html.HtmlButton.IconEdit:
        """

        :tags:
        :categories:

        :param time: Integer. Interval time in second.
        :param js_funcs: String | List. The Javascript functions.
        :param components: List. HTML components to be triggered when activated.
        :param icon: String. Optional. The font awesome icon reference.
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
        :param align: String. Optional. A string with the horizontal position of the component.
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
        :param options: Dictionary. Optional. Specific Python options available for this component.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
        """
        if components is not None:
            js_funcs = js_funcs or []
            for component in components:
                js_funcs.append(component.dom.trigger("click"))
        toggle = self.page.ui.buttons.live(time, js_funcs, icon, width, height, align, html_code, profile, options)
        html.Html.set_component_skin(toggle)
        return toggle
