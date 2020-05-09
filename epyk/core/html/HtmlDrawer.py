
from epyk.core.html import Html

from epyk.core.html import Defaults
from epyk.core.html.options import OptPanel
from epyk.core.css.styles import GrpClsContainer
from epyk.core.js.html import JsHtmlStepper


class Drawer(Html.Html):

  def __init__(self, report, width, height, options, helper, profile):
    super(Drawer, self).__init__(report, None, css_attrs={"width": width, "height": height})
    self.add_helper(helper, css={"line-height": '%spx' % Defaults.LINE_HEIGHT})
    self.__options = OptPanel.OptionDrawer(self, options)
    self.style.css.position = 'relative'

    self.panels = report.ui.div()
    self.panels.inReport = False
    self.panels.attr['name'] = 'drawer_panels'

    self.handle = report.ui.div()
    self.handle.style.clear_all()
    self.handle.style.css.cursor = 'pointer'

    self.handle.inReport = False
    self.handle.attr['name'] = 'drawer_handle'

    self.drawers = report.ui.div()
    self.drawers.style.clear_all()
    self.drawers.inReport = False
    self.drawers.attr['name'] = 'drawer_content'

  @property
  def dom(self):
    """
    Description:
    ------------
    Property to get the common dom features

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
    Property to set all the possible object for a drawer

    :rtype: OptPanel.OptionDrawer
    """
    return self.__options

  def add_panel(self, link, container, display=False):
    """
    Description:
    ------------
    Add panel to the drawer object.

    Attributes:
    ----------
    :param link: String | HTML object. The value in the drawer
    :param container: HTML object. The component to be displayed
    :param display: String. The CSS Display property
    """
    if not hasattr(link, 'inReport'):
      link = self._report.ui.div(link)
      link.inReport = False
    if not hasattr(container, 'inReport'):
      container = self._report.ui.div(container)
    container.style.css.display = display
    container.inReport = False
    self.panels += container
    self.drawers += link

  @property
  def style(self):
    """
    Description:
    ------------
    Get the CSS Style of the object

    :rtype: GrpClsContainer.ClassDrawer
    """
    if self._styleObj is None:
      self._styleObj = GrpClsContainer.ClassDrawer(self)
    return self._styleObj

  def set_handle(self, component):
    """
    Description:
    ------------
    Set the handle used to trigger the open / close events
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
        <div name='drawer' style='%(side)s:0'>
          %(handle)s%(drawer)s
        </div>
      </div>''' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'htmlId': self.htmlId,
                   'drawer': self.drawers.html(), 'handle': self.handle.html(), 'panels': self.panels.html(), 'side': position[self.options.side]}
