
from epyk.core.html import Html
from epyk.fwk.toast.options import OptToastGrid
from epyk.fwk.toast.js import JsToastGrid


class Grid(Html.Html):
  requirements = ('tabulator-tables', )
  name = 'Tabulator Table'
  _option_cls = OptToastGrid.GridConfig

  def __init__(self, page, records, width, height, html_code, options, profile):
    data, columns, self._json_config = [], [], {}
    super(Grid, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                               css_attrs={"width": width, "height": height})
    if records is not None:
      self.options.data = records
    self.style.css.background = None

  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new tui.Grid(options)'''

  @property
  def var(self):
    """   Return the calendar javaScript object reference after the builder.
    """
    return "window['%s']" % self.htmlCode

  @property
  def js(self) -> JsToastGrid.JsGrid:
    """   Javascript module of the items in the menu.

    :rtype: JsToastGrid.JsGrid
    """
    if self._js is None:
      self._js = JsToastGrid.JsGrid(component=self, js_code=self.var, page=self.page)
    return self._js

  @property
  def options(self) -> OptToastGrid.GridConfig:
    """   The component options.

    :rtype: OptToastGrid.GridConfig
    """
    return super().options

  def add_column(self, field, title=None):
    """  
    Add new column to the underlying Tabulator object.

    :param field: String. Mandatory. The key in the row.
    :param title: String. Optional. The title for the column. Default to the field.
    """
    return self.options.add_column(field, title)

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '''<div %s></div>''' % self.get_attrs(css_class_names=self.style.get_classes())
