#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core import html
from epyk.core.py import types as etypes
from epyk.core.data import tree as data_tree
from epyk.interfaces import Arguments


class Trees:

    def __init__(self, ui):
        self.page = ui.page

    def tree(self, data: List[dict] = None, width: etypes.SIZE_TYPE = (100, "%"),
             height: etypes.SIZE_TYPE = (None, 'px'),
             html_code: str = None, helper: str = None, options: etypes.OPTION_TYPE = None,
             profile: etypes.PROFILE_TYPE = None) -> html.HtmlTrees.Tree:
        """Addd a tree / hierarchy component to the page.

        Usage::

          data = [{"value": 'test', 'items': [{"value": 'child 1', 'color': 'red'}]}]
          page.ui.lists.tree(data)

          data = [{"value": 'test', 'icon': "fas fa-check", "css": {'color': 'green'}, 'items': [{
            "value": 'child 1', "css": {'color': 'red'}, 'icon': "fas fa-times"}]},
                  {"value": 'test 2', 'icon': "fas fa-exclamation-triangle", "css": {'color': 'orange'}, 'items': [{
                    "value": 'child 1', "css": {'color': 'red'}, 'icon': "fas fa-times"}],
                   }]

          hyr = page.ui.tree(data)
          hyr.options.icon_close = "fas fa-caret-right"
          hyr.options.icon_open = "fas fa-caret-down"
          hyr.options.with_badge = True
          hyr.options.with_icon = "icon"
          hyr.click_node([page.js.alert(pk.events.value)])
          hyr.click([page.js.alert(pk.events.value)])

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTrees.Tree`

        `Template Tree <https://github.com/epykure/epyk-templates/blob/master/locals/components/tree.py>`_

        :param data: Optional. The records
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: Optional. A tooltip helper
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        html_tree = html.HtmlTrees.Tree(self.page, data or [], width, height, html_code, helper, options or {}, profile)
        html.Html.set_component_skin(html_tree)
        return html_tree

    def inputs(
            self, data: List[dict] = None,
            width: etypes.SIZE_TYPE = (100, "%"), height: etypes.SIZE_TYPE = (None, 'px'),
            html_code: str = None, helper: str = None, options: etypes.OPTION_TYPE = None,
            profile: etypes.PROFILE_TYPE = None) -> html.HtmlTrees.TreeInput:
        """

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTrees.TreeInput`

        :param data: Optional. The records
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: Optional. A tooltip helper
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        html_tree = html.HtmlTrees.TreeInput(
            self.page, data or [], width, height, html_code, helper, options or {}, profile)
        html.Html.set_component_skin(html_tree)
        return html_tree

    def menu(self, component: html.HtmlTrees.Tree, title: Union[str, dict] = None, add: bool = False, height=(18, 'px'),
             update_funcs=None, options: etypes.OPTION_TYPE = None, profile: etypes.PROFILE_TYPE = None):
        commands = [
            ("", "fas fa-compress-arrows-alt", "Compress", 15),
            ("", "fas fa-expand-arrows-alt", "Expand", 15),
        ]
        if add:
            commands.append(("Add&nbsp;", "fas fa-plus", "Add", 15))
        options = options or {}
        menu_items = []
        for typ, icon, tooltip, size in commands:
            if icon:
                if isinstance(icon, tuple):
                    icon = icon[0]
                r = self.page.ui.icons.awesome(
                    icon, align="center", tooltip=tooltip, text=typ, height=height, width=(size, 'px'),
                    options=options, profile=profile)
                r.span.style.css.line_height = r.style.css.height
                r.icon.style.css.font_factor(-4)
                r.style.css.font_factor(-3)
                if tooltip == "Add&nbsp;":
                    r.click([
                        component.dom.add(""),
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
                    ])
                elif tooltip == "Compress":
                    r.click([
                        component.dom.hide()
                    ])
                elif tooltip == "Expand":
                    r.click([
                        component.dom.expand()
                    ])
                menu_items.append(r)
        if update_funcs is not None:
            r = self.page.ui.icons.awesome(
                "refresh", align="center", tooltip="Sync", height=height, width=(15, 'px'), options=options,
                profile=profile)
            r.icon.style.css.font_factor(-4)
            r.style.css.font_factor(-3)
            r.click([
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
                    ] + update_funcs, profile=profile)
            menu_items.append(r)
        container = self.page.ui.menu(component, title=title, menu_items=menu_items, editable=False)
        if options.get("filter"):
            input_hyr_filt = self.page.ui.input(placeholder="filter...")
            input_hyr_filt.attr["type"] = "search"
            input_hyr_filt.style.css.background = None
            input_hyr_filt.style.css.text_align = "left"
            input_hyr_filt.style.css.padding_left = 5
            input_hyr_filt.style.css.color = "grey"
            input_hyr_filt.style.css.font_factor(-4)
            input_hyr_filt.style.css.italic()
            input_hyr_filt.style.css.border_bottom = "1px solid %s" % self.page.theme.greys[3]
            container.insert(1, input_hyr_filt)
            input_hyr_filt.enter([
                component.build(
                    self.page.js.objects.get("%s_data" % component.html_code),
                    options={"filter_on": input_hyr_filt.dom.content})
            ])
        html.Html.set_component_skin(container)
        return container

    def dropdown(self, record: List[dict] = None, text: str = "", width: etypes.SIZE_TYPE = (100, "%"),
                 height: etypes.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
                 options: etypes.OPTION_TYPE = None, profile: etypes.PROFILE_TYPE = None) -> html.HtmlTrees.DropDown:
        """

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTrees.DropDown`

        Related Pages:

          http://getbootstrap.com/docs/4.0/components/dropdowns/
          https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_ref_js_dropdown_multilevel_css&stacked=h
          https://codepen.io/svnt/pen/beEgre

          https://codepen.io/raneio/pen/NbbZEM
          https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_js_dropdown_hover
          https://codepen.io/antoniputra/pen/BzyWmb

        :param record: Optional. The records
        :param text: Optional. Dropdown label
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: Optional. A tooltip helper
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {"width": 70}
        dfl_options.update(options or {})
        html_d = html.HtmlTrees.DropDown(
            self.page, record, text, width, height, html_code, helper, dfl_options, profile)
        html.Html.set_component_skin(html_d)
        return html_d

    def folder(self, folder: str = None, width: etypes.SIZE_TYPE = (100, "%"), height: etypes.SIZE_TYPE = (None, 'px'),
               html_code: str = None, helper: str = None, options: etypes.OPTION_TYPE = None,
               profile: etypes.PROFILE_TYPE = None) -> html.HtmlTrees.Tree:
        """Add a tree component from a folder structure.

        :param folder: The path to be displayed
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: Optional. A tooltip helper
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        options = options or {}
        if folder is not None:
            data = data_tree.folders(
                folder, excluded_folders=options.get("excluded_folders", ["outs", "static"]),
                make_url=options.get("make_url"))
        else:
            data = []
        tree = self.tree(
            data, width=width, height=height, html_code=html_code, helper=helper, options=options, profile=profile)
        if height[0] is not None:
            tree.style.css.overflow = "auto"
        html.Html.set_component_skin(tree)
        return tree
