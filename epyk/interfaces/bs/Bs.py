
from epyk.interfaces.bs import BsButtons
from epyk.interfaces.bs import BsDropDowns
from epyk.interfaces.bs import BsLists
from epyk.interfaces.bs import BsNavs
from epyk.interfaces.bs import BsInputs
from epyk.interfaces.bs import BsCarousel
from epyk.interfaces.bs import BsModals
from epyk.interfaces.bs import BsDates
from epyk.interfaces.bs import BsChecks
from epyk.interfaces.bs import BsIcons


from epyk.fwk.bs.html import BsHtml


class Bootstrap:

  def __init__(self, page):
    self.page = page
    self.button = self.buttons.button
    self.input = self.inputs.input

  @property
  def buttons(self):
    """
    Description:
    ------------
    Use Bootstrap’s custom button styles for actions in forms, dialogs, and more with support for multiple sizes,
    states, and more.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/buttons/
    """
    return BsButtons.Buttons(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    Free, high quality, open source icon library with nearly 1,200 icons.

    Related Pages:

      https://icons.getbootstrap.com/
    """
    self.page.cssImport.add("bootstrap-icons")
    return BsIcons.Icons(self)

  @property
  def checks(self):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.0/forms/checks-radios/#switches
    """
    return BsDates.Dates(self)

  @property
  def dates(self):
    """
    Description:
    ------------
    """
    return BsDates.Dates(self)

  @property
  def modals(self):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/modal/
    """
    return BsModals.Modals(self)

  @property
  def carousels(self):
    """
    Description:
    ------------
    A slideshow component for cycling through elements—images or slides of text—like a carousel.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/carousel/
    """
    return BsCarousel.Carousels(self)

  @property
  def inputs(self):
    """
    Description:
    ------------
    Easily extend form controls by adding text, buttons, or button groups on either side of textual inputs,
    custom selects, and custom file inputs.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/
    """
    return BsInputs.Inputs(self)

  @property
  def navs(self):
    """
    Description:
    ------------
    Documentation and examples for how to use Bootstrap’s included navigation components.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/navs/
    """
    return BsNavs.Bars(self)

  @property
  def dropdowns(self):
    """
    Description:
    ------------
    Toggle contextual overlays for displaying lists of links and more with the Bootstrap dropdown plugin.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/dropdowns/
    """
    return BsDropDowns.Dropdowns(self)

  @property
  def lists(self):
    """
    Description:
    ------------
    List groups are a flexible and powerful component for displaying a series of content.
    Modify and extend them to support just about any content within.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/list-group/
    """
    return BsLists.Lists(self)

  def badge(self, value, pill=False, category='primary'):
    """
    Description:
    ------------
    Documentation and examples for badges, our small count and labeling component.

    Related Pages:

      hhttps://getbootstrap.com/docs/4.4/components/badge/

    Attributes:
    ----------
    :param value:
    :param pill:
    :param category:
    """
    container = self.page.web.std.texts.span(value)
    container.style.clear_all()
    container.attr["class"].add("badge badge-%s" % category)
    if pill:
      container.attr["class"].add("badge-pill")
    return container

  def breadcrumb(self, values, selected=None):
    """
    Description:
    ------------
    Indicate the current page’s location within a navigational hierarchy that automatically adds separators via CSS.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/breadcrumb/

    Attributes:
    ----------
    :param values:
    :param selected:
    """
    schema = {"type": 'nav', 'css': False, 'arias': {'label': 'breadcrumb'}, 'children': [
        {"type": 'ol', 'class': 'breadcrumb', 'css': False, 'children': []}]}

    for v in values:
      schema['children'][0]['children'].append({"type": 'item', 'class': 'breadcrumb-item', 'css': False, 'children': [
        {"type": 'link', 'css': False, 'args': {'text': v, 'url': '#'}}]})
      if selected == v:
        schema['children'][0]['children'][-1]['class'] = 'breadcrumb-item active'
        schema['children'][0]['children'][-1]['aria'] = {'current': 'page'}

    h = self.page.web.bs.composite(schema, options={"reset_class": True})
    return h

  def pagination(self, values, selected=None, sizing=None):
    """
    Description:
    ------------
    Documentation and examples for showing pagination to indicate a series of related content exists across
    multiple pages.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/pagination/

    Attributes:
    ----------
    :param values:
    :param selected:
    :param sizing:
    """
    schema = {"type": 'nav', 'css': False, 'children': [
      {"type": 'list', 'class': 'pagination', 'css': False, 'children': [
        {"type": 'item', 'class': 'page-item', 'css': False, 'children': [
          {"type": 'link', 'css': False, 'class': 'page-link', 'args': {'text': 'Previous', 'url': '#'}}]}
      ]}]}
    if sizing is not None:
      schema['children'][0]['class'] = "pagination pagination-%s" % sizing
    for v in values:
      schema['children'][0]['children'].append({"type": 'item', 'class': 'page-item', 'css': False, 'children': [
        {"type": 'link', 'css': False, 'class': 'page-link', 'args': {'text': v, 'url': '#'}}]})
      if v == selected:
        schema['children'][0]['children'][-1]['class'] = 'page-item active'
        schema['children'][0]['children'][-1]['arias'] = {'current': 'page'}
        schema['children'][0]['children'][-1]['children'][0]['args']['text'] = "%s <span class='sr-only'>(current)</span>" % v
    schema['children'][0]['children'].append({"type": 'item', 'class': 'page-item', 'css': False, 'children': [
      {"type": 'link', 'css': False, 'class': 'page-link', 'args': {'text': 'Next', 'url': '#'}}]})
    h = self.page.web.bs.composite(schema, options={"reset_class": True})
    return h

  def jumbotron(self, components):
    """
    Description:
    ------------
    Lightweight, flexible component for showcasing hero unit style content.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/jumbotron/

    Attributes:
    ----------
    :param components:
    """
    container = self.page.web.std.div(components)
    container.style.clear_all()
    container.attr["class"].add("jumbotron jumbotron-fluid")
    return container

  def progress(self, value, valuemin=0, valuemax=100, stripped=False, category='success'):
    """
    Description:
    ------------
    Documentation and examples for using Bootstrap custom progress bars featuring support for stacked bars,
    animated backgrounds, and text labels.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/progress/

    Attributes:
    ----------
    :param value:
    :param valuemin:
    :param valuemax:
    :param category:
    """
    container = self.page.web.std.div()
    container.style.clear_all()
    container.attr["class"].add("progress")
    d = self.page.web.std.div("%s%%" % value)
    d.style.clear_all()
    d.attr["role"] = 'progressbar'
    d.attr["class"].add("progress-bar bg-%s" % category)
    if stripped:
      d.attr["class"].add("progress-bar-striped")
    d.style.css.width = "%s%%" % value
    d.aria.valuenow = value
    d.aria.valuemin = valuemin
    d.aria.valuemax = valuemax
    container += d
    return container

  def card(self, component=None, title=None, width=(100, "%"), height=(None, "px"), options=None, profile=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/card/

    Attributes:
    ----------
    :param component:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = BsHtml.BsCards(self.page, component or [], title, width, height, options, profile)
    container.style.clear_all()
    container.attr["class"].add("card")
    return container

  def toast(self, component=None, title=None, width=(100, "%"), height=(None, "px"), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    if component is not None and not isinstance(component, list):
      component = [component]
    h_toast = BsHtml.BsToasts(self.page, component or [], title, width, height, options, profile)
    return h_toast

  def alert(self, test, dismissing=True, category='primary'):
    """
    Description:
    ------------
    Provide contextual feedback messages for typical user actions with the handful of available and flexible alert
    messages.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/alerts/

    Attributes:
    ----------
    :param test:
    :param dismissing:
    :param category:
    """
    container = self.page.web.std.div(test)
    container.style.clear_all()
    container.attr['class'].add('alert alert-%s' % category)
    container.attr['role'] = 'alert'
    if dismissing:
      container.attr['class'].add('alert-dismissible fade show')
      span = self.page.web.std.texts.span("&times;")
      span.style.clear_all()
      button = self.page.web.std.button([span])
      button.style.clear_all()
      button.attr['class'].add('close')
      button.attr['data-dismiss'] = "alert"
      button.aria.label = "Close"
      container += button
    return container

  def composite(self, schema, width=(None, "%"), height=(None, "px"), html_code=None, helper=None, options=None,
                profile=None):
    """
    Description:
    ------------
    Composite bespoke object.

    This object will be built based on its schema. No specific CSS Style and class will be added to this object.
    The full definition will be done in the nested dictionary schema.

    Usage::

      schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
          {'type': : {...}}
          ...
      ]}

    Attributes:
    ----------
    :param schema: Dictionary. The schema of the composite item with the different sub items
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param html_code: Optional. String. The component identifier code (for both Python and Javascript)
    :param helper: Optional. String. Optional. The helper message
    :param options: Optional. Dictionary. the component specific items
    :param profile: Optional. Not yet available
    """
    html_help = BsHtml.BsComposite(self.page, schema, width=width, height=height, html_code=html_code,
                                   profile=profile, options=options or {}, helper=helper)
    return html_help

  def spinner(self, category='primary', grow=False):
    """
    Description:
    ------------
    Indicate the loading state of a component or page with Bootstrap spinners, built entirely with HTML, CSS,
    and no JavaScript.

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/spinners/

    Attributes:
    ----------
    :param category:
    :param grow:
    """
    container = self.page.web.std.div()
    container.style.clear_all()
    if grow:
      container.attr["class"].add("spinner-grow text-%s" % category)
    else:
      container.attr["class"].add("spinner-border text-%s" % category)
    container.attr["role"] = "status"
    span = self.page.web.std.texts.span("Loading...")
    span.style.clear_all()
    span.attr["class"].add("sr-only")
    return container

