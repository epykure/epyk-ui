
from typing import Optional, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.customs.data.js import JsHtmlDashboard
from epyk.customs.data.options import OptDashboard


class Pivots(Html.Html):
  name = 'Dashboard Pivots'
  _option_cls = OptDashboard.OptionsPivot

  def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, html_code: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Pivots, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self.container = self.page.ui.row(position="top", options={"responsive": False})
    self.container.options.managed = False
    # Will be defined from the interface
    self.columns, self.rows, self.sub_rows = None, None, None

  @property
  def options(self) -> OptDashboard.OptionsPivot:
    """   Property to set all the possible object for a button.
    """
    return super().options

  @property
  def dom(self) -> JsHtmlDashboard.JsHtmlPivot:
    """  
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage::
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlPivot(self, page=self.page)
    return self._dom

  def items_style(self, style: str = None, css_attrs: dict = None):
    """  
    Function to load a predefined style for the items of the components.

    Usage::

    :param style: The alias of the style to apply.
    :param css_attrs: Css attributes.
    """
    li_item_style = {}
    if style == "bullets":
      li_item_style = {
        "display": 'inline-block', 'padding': '0 5px', 'margin-right': '2px',
        'background': self.page.theme.greys[2], 'border-radius': '10px',
        'border': '1px solid %s' % self.page.theme.greys[2]}
    if css_attrs is not None:
      li_item_style.update(css_attrs)
    self.columns.options.li_css = li_item_style
    self.columns.set_items()
    self.rows.options.li_css = li_item_style
    if self.sub_rows is not None:
      self.sub_rows.options.li_css = li_item_style
    return self

  def clear(self, profile: Union[dict, bool] = None):
    """  

    Usage::

    :param profile:
    """
    return JsUtils.jsConvertFncs([self.rows.dom.clear(), self.columns.dom.clear()], toStr=True, profile=profile)

  def __str__(self):
    self.container._vals = []
    if self.options.sortable:
      if not self.options.readonly_rows:
        self.rows.sortable()
      if not self.options.readonly_columns:
        self.columns.sortable()
    if not self.options.readonly_rows and "ondrop" not in self.rows.attr:
      self.rows.drop()
    if not self.options.readonly_columns and "ondrop" not in self.columns.attr:
      self.columns.drop()
    if self.sub_rows is not None:
      self.container.add([
        self.page.ui.text(
          "Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)).css(
          {"display": "block"}), self.rows,
        self.page.ui.text(
          "Sub Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)).css(
          {"display": "block"}),
        self.sub_rows])
    else:
      if self.rows.options.max == 1:
        self.container.add([
          self.page.ui.text(
            self.options.title_rows).css(
            {"display": "block"}), self.rows])
      else:
        self.container.add([
          self.page.ui.text(
            self.options.title_rows).css(
            {"display": "block"}), self.rows])
    self.container.add([
      self.page.ui.text(
        self.options.title_values).css(
        {"display": "block"}), self.columns])
    html = [h.html() for h in self._vals]
    return "<div %s>%s%s</div>" % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.container.html(), "".join(html))
