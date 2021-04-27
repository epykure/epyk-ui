#!/usr/bin/python
# -*- coding: utf-8 -*-

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

  def __init__(self, report, width, height, options, helper, profile):
    super(Drawer, self).__init__(report, None, profile=profile, options=options,
                                 css_attrs={"width": width, "height": height})
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    self.style.css.position = 'relative'

    self.panels = report.ui.div()
    self.panels.options.managed = False
    self.panels.style.css.padding_right = 10
    self.panels.attr['name'] = 'drawer_panels'

    self.handle = report.ui.div()
    self.handle.style.clear_all()
    self.handle.style.css.cursor = 'pointer'

    self.handle.options.managed = False
    self.handle.attr['name'] = 'drawer_handle'

    self.drawers = report.ui.div()
    self.drawers.style.clear_all()
    self.drawers.style.css.overflow_y = 'auto'
    self.drawers.options.managed = False
    self.drawers.attr['name'] = 'drawer_content'

  @property
  def dom(self):
    """
    Description:
    ------------
    Property to get the common dom features.

    Usage::

    :rtype: JsHtmlStepper.Drawer
    """
    if self._dom is None:
      self._dom = JsHtmlStepper.Drawer(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a drawer.

    Usage::

    :rtype: OptPanel.OptionDrawer
    """
    return super().options

  def add_panel(self, link, container, display=False):
    """
    Description:
    ------------
    Add panel to the drawer object.

    Usage::

    Attributes:
    ----------
    :param link: String | HTML. The value in the drawer.
    :param container: HTML. The component to be displayed.
    :param display: String. Optional. The CSS Display property.
    """
    if not hasattr(link, 'options'):
      link = self._report.ui.div(link)
      link.style.css.padding = "0 5px"
      link.options.managed = False
    if not hasattr(container, 'options'):
      container = self._report.ui.div(container)
    container.style.css.display = display
    container.options.managed = False
    self.panels += container
    self.drawers += link

  @property
  def style(self):
    """
    Description:
    ------------
    Get the CSS Style of the object.

    Usage::

    :rtype: GrpClsContainer.ClassDrawer
    """
    if self._styleObj is None:
      self._styleObj = GrpClsContainer.ClassDrawer(self)
    return self._styleObj

  def set_handle(self, component):
    """
    Description:
    ------------
    Set the handle used to trigger the open / close events.

    Usage::

    Attributes:
    ----------
    :param component: HTML. An HTML component.
    """
    self.handle = self._report.ui.div()
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
      </div>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlCode': self.htmlCode,
                   'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
                   'side': position[self.options.side], 'helper': self.helper}


class DrawerMulti(Html.Html):
  name = 'Multi Drawers'
  _option_cls = OptPanel.OptionDrawer

  def __init__(self, report, component, width, height, options, helper, profile):
    super(DrawerMulti, self).__init__(report, None, options=options, css_attrs={"width": width, "height": height},
                                      profile=profile)
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    self.style.css.position = 'relative'

    self.panels = component
    self.panels.options.managed = False
    self.panels.style.css.display = "inline-block"
    self.panels.style.css.width = "auto"
    self.panels.style.css.padding_right = 10

    self.handle = report.ui.div()
    self.handle.style.clear_all()
    self.handle.style.css.z_index = 10
    self.handle.style.css.position = 'relative'

    self.handle.options.managed = False
    self.handle.attr['name'] = 'drawer_handle'

    self.drawers = report.ui.div()
    self.drawers.style.clear_all()
    self.drawers.style.css.overflow_y = 'auto'
    self.drawers.options.managed = False
    self.drawers.attr['name'] = 'drawer_content'

  @property
  def dom(self):
    """
    Description:
    ------------
    Property to get the common dom features.

    Usage::

    :rtype: JsHtmlStepper.Drawer
    """
    if self._dom is None:
      self._dom = JsHtmlStepper.Drawer(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a drawer.

    Usage::

    :rtype: OptPanel.OptionDrawer
    """
    return super().options

  def add_drawer(self, link, container):
    """
    Description:
    ------------
    Add panel to the drawer object.

    Usage::

    Attributes:
    ----------
    :param link: String | HTML. The value in the drawer.
    :param container: HTML. The component to be displayed.
    """
    if not hasattr(link, 'options'):
      link = self._report.ui.div(link)
    link.style.css.padding = "5px 0"
    link.style.css.color = self._report.theme.colors[0]
    link.style.css.margin = "0 2px"
    link.style.css.cursor = "pointer"
    link.options.managed = False
    if not hasattr(container, 'options'):
      container = self._report.ui.div(container)
      container.style.css.padding = 5
    container.options.managed = False
    link.style.css.writing_mode = "vertical-rl"
    link.style.css.text_orientation = "mixed"
    self.handle += link
    self.drawers += container
    link.click([
      self._report.js.querySelectorAll(
        Selector.Selector(self.drawers).with_child_element("div").excluding(container)).css({"display": 'none'}),
      expr.if_(self.panels.dom.getAttribute("data-panel") == container.htmlCode, [
        self.drawers.dom.toggle_transition(
          "margin-right" if self.options.side == 'left' else "margin-left", "-%s" % self.options.width, "0px"),
        container.dom.css({"display": 'none'}),
        self.panels.dom.setAttribute("data-panel", '')])
      .else_([
        expr.if_(self._report.js.querySelector(Selector.Selector(self.drawers)).css("margin-left") != "0px", [
          self.drawers.dom.toggle_transition(
            "margin-right" if self.options.side == 'left' else "margin-left", "0px", "-%s" % self.options.width),
        ]),
        self.panels.dom.setAttribute("data-panel", container.htmlCode),
        container.dom.css({'display': 'block'})
      ])
    ])

  @property
  def style(self):
    """
    Description:
    ------------
    Get the CSS Style of the object.

    Usage::

    :rtype: GrpClsContainer.ClassDrawer
    """
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
      </div>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlCode': self.htmlCode,
                   'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(),
                   'side': self.options.side}
