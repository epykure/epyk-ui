
from typing import Optional, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.customs.data.js import JsHtmlDashboard


class Pivots(Html.Html):
  name = 'Dashboard Pivots'

  def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, html_code: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Pivots, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self.container = self.page.ui.row(position="top", options={"responsive": False})
    self.container.options.managed = False
    # Will be defined from the interface
    self.columns, self.rows, self.sub_rows = None, None, None

  @property
  def dom(self) -> JsHtmlDashboard.JsHtmlPivot:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :rtype: JsHtmlDashboard.JsHtmlPivot
    """
    if self._dom is None:
      self._dom = JsHtmlDashboard.JsHtmlPivot(self, page=self.page)
    return self._dom

  def items_style(self, style: str):
    """
    Description:
    ------------
    Function to load a predefined style for the items of the components.

    Usage:
    -----

    Attributes:
    ----------
    :param str style: The alias of the style to apply.
    """
    if style == "bullets":
      bullter_style = {"display": 'inline-block', 'padding': '0 5px', 'margin-right': '2px',
                       'background': self.page.theme.greys[2], 'border-radius': '10px',
                       'border': '1px solid %s' % self.page.theme.greys[2]}
      self.columns.options.li_css = bullter_style
      self.columns.set_items()
      self.rows.options.li_css = bullter_style
      if self.sub_rows is not None:
        self.sub_rows.options.li_css = bullter_style
    return self

  def clear(self, profile: Union[dict, bool] = None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param Union[dict, bool] profile:
    """
    return JsUtils.jsConvertFncs([self.rows.dom.clear(), self.columns.dom.clear()], toStr=True, profile=profile)

  def __str__(self):
    self.container._vals = []
    if "ondrop" not in self.rows.attr:
      self.rows.drop()
    if "ondrop" not in self.columns.attr:
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
            "Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3)).css(
            {"display": "block"}), self.rows])
      else:
        self.container.add([
          self.page.ui.text(
            "Rows <i style='font-size:%s'>(multiple field)</i>" % self.page.body.style.globals.font.normal(-3)).css(
            {"display": "block"}), self.rows])
    self.container.add([
      self.page.ui.text(
        "Values <i style='font-size:%s'>(multiple fields)</i>" % self.page.body.style.globals.font.normal(-3)).css(
        {"display": "block"}), self.columns])
    html = [h.html() for h in self._vals]
    return "<div %s>%s%s</div>" % (
      self.get_attrs(css_class_names=self.style.get_classes()), self.container.html(), "".join(html))