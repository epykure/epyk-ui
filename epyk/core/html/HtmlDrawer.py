#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.html import Html

from epyk.core.js import expr
from epyk.core.css import Selector

from epyk.core.html import Defaults
from epyk.core.html.options import OptPanel
from epyk.core.css.styles import GrpClsContainer
from epyk.core.js.html import JsHtmlStepper


class Drawer(Html.Html):
    name = 'Drawer'
    _option_cls = OptPanel.OptionDrawer

    def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, options: Optional[dict],
                 helper: Optional[str], profile: Optional[Union[dict, bool]]):
        super(Drawer, self).__init__(page, None, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        self.style.css.position = 'relative'

        self.panels = page.ui.div()
        self.panels.options.managed = False
        self.panels.style.css.padding_right = 10
        self.panels.attr['name'] = 'drawer_panels'

        self.handle = page.ui.div()
        self.handle.style.clear_all()
        self.handle.style.css.cursor = 'pointer'

        self.handle.options.managed = False
        self.handle.attr['name'] = 'drawer_handle'

        self.drawers = page.ui.div()
        self.drawers.style.clear_all()
        self.drawers.style.css.overflow_y = 'auto'
        self.drawers.options.managed = False
        self.drawers.attr['name'] = 'drawer_content'

    @property
    def dom(self) -> JsHtmlStepper.Drawer:
        """ Property to get the common dom features. """
        if self._dom is None:
            self._dom = JsHtmlStepper.Drawer(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptPanel.OptionDrawer:
        """ Property to set all the possible object for a drawer. """
        return super().options

    def add_panel(self, link: Union[Html.Html, str], container: Html.Html, display: bool = False):
        """
        Add panel to the drawer object.

        :param link: The value in the drawer
        :param container: The component to be displayed
        :param display: Optional. The CSS Display property
        """
        if not hasattr(link, 'options'):
            link = self.page.ui.div(link)
            link.style.css.padding = "0 5px"
            link.options.managed = False
        if not hasattr(container, 'options'):
            container = self.page.ui.div(container)
        container.style.css.display = display
        container.options.managed = False
        self.panels += container
        self.drawers += link

    @property
    def style(self) -> GrpClsContainer.ClassDrawer:
        """ Get the CSS Style of the object. """
        if self._styleObj is None:
            self._styleObj = GrpClsContainer.ClassDrawer(self)
        return self._styleObj

    def set_handle(self, component: Html.Html):
        """
        Set the handle used to trigger the open / close events.

        :param component: An HTML component.
        """
        self.handle = self.page.ui.div()
        self.handle.style.clear_all()
        if self.options.side == 'left':
            component.click([self.drawers.dom.toggle_transition("margin-right", "0px", "-%s" % self.options.width)])
        else:
            component.click([self.drawers.dom.toggle_transition("margin-left", "0px", "-%s" % self.options.width)])

    def __str__(self):
        self.handle.style.css.float = self.options.side
        if self.options.side == 'left':
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_right = "-%s" % self.options.width
            self.handle.click([self.drawers.dom.toggle_transition("margin-right", "0px", "-%s" % self.options.width)])
        else:
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_left = "-%s" % self.options.width
            self.handle.click([self.drawers.dom.toggle_transition("margin-left", "0px", "-%s" % self.options.width)])
        position = {"left": 'right', 'right': 'left'}
        return '''
      <div %(attr)s>
        %(panels)s
        <div name='drawer' style='clear:both;%(side)s:0;overflow-y:hidden'>
          %(helper)s
          %(handle)s%(drawer)s
        </div>
      </div>''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.htmlCode,
                   'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
                   'side': position[self.options.side], 'helper': self.helper}


class DrawerMulti(Html.Html):
    name = 'Multi Drawers'
    _option_cls = OptPanel.OptionDrawer

    def __init__(self, page: primitives.PageModel, component: Html.Html, width: tuple, height: tuple,
                 options: Optional[dict], helper: Optional[str], profile: Optional[Union[bool, dict]]):
        super(DrawerMulti, self).__init__(page, None, options=options, css_attrs={"width": width, "height": height},
                                          profile=profile)
        self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
        self.style.css.position = 'relative'

        self.panels = component
        self.panels.options.managed = False
        self.panels.style.css.display = "inline-block"
        self.panels.style.css.width = "auto"
        self.panels.style.css.padding_right = 10

        self.handle = page.ui.div()
        self.handle.style.clear_all()
        self.handle.style.css.z_index = 10
        self.handle.style.css.position = 'relative'

        self.handle.options.managed = False
        self.handle.attr['name'] = 'drawer_handle'

        self.drawers = page.ui.div()
        self.drawers.style.clear_all()
        self.drawers.style.css.overflow_y = 'auto'
        self.drawers.options.managed = False
        self.drawers.attr['name'] = 'drawer_content'

    @property
    def dom(self) -> JsHtmlStepper.Drawer:
        """ Property to get the common dom features. """
        if self._dom is None:
            self._dom = JsHtmlStepper.Drawer(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptPanel.OptionDrawer:
        """ Property to set all the possible object for a drawer. """
        return super().options

    def add_drawer(self, link: Union[str, Html.Html], container: Html.Html):
        """
        Add panel to the drawer object.

        :param link: The value in the drawer
        :param container: The component to be displayed
        """
        if not hasattr(link, 'options'):
            link = self.page.ui.div(link)
        link.style.css.padding = "5px 0"
        link.style.css.color = self.page.theme.colors[0]
        link.style.css.margin = "0 2px"
        link.style.css.cursor = "pointer"
        link.options.managed = False
        if not hasattr(container, 'options'):
            container = self.page.ui.div(container)
            container.style.css.padding = 5
        container.options.managed = False
        link.style.css.writing_mode = "vertical-rl"
        link.style.css.text_orientation = "mixed"
        self.handle += link
        self.drawers += container
        link.click([
            self.page.js.querySelectorAll(
                Selector.Selector(self.drawers).with_child_element("div").excluding(container)).css(
                {"display": 'none'}),
            expr.if_(self.panels.dom.getAttribute("data-panel") == container.htmlCode, [
                self.drawers.dom.toggle_transition(
                    "margin-right" if self.options.side == 'left' else "margin-left", "-%s" % self.options.width,
                    "0px"),
                container.dom.css({"display": 'none'}),
                self.panels.dom.setAttribute("data-panel", '')])
            .else_([
                expr.if_(self.page.js.querySelector(Selector.Selector(self.drawers)).css("margin-left") != "0px", [
                    self.drawers.dom.toggle_transition(
                        "margin-right" if self.options.side == 'left' else "margin-left", "0px",
                        "-%s" % self.options.width),
                ]),
                self.panels.dom.setAttribute("data-panel", container.htmlCode),
                container.dom.css({'display': 'block'})
            ])
        ])
        return self

    @property
    def style(self) -> GrpClsContainer.ClassDrawer:
        """ Get the CSS Style of the object. """
        if self._styleObj is None:
            self._styleObj = GrpClsContainer.ClassDrawer(self)
        return self._styleObj

    def __str__(self):
        self.handle.style.css.float = self.options.side
        if self.options.side == 'left':
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_right = "-%s" % self.options.width
        else:
            self.drawers.style.css.width = self.options.width
            self.drawers.style.css.margin_left = "-%s" % self.options.width
        return '''
      <div %(attr)s>
        %(panels)s
        <div name='drawer' style='clear:both;%(side)s:0;overflow-y:hidden'>
          %(drawer)s
        </div>
        %(handle)s
      </div>''' % {'attr': self.get_attrs(css_class_names=self.style.get_classes()), 'htmlCode': self.htmlCode,
                   'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
                   'side': self.options.side}
