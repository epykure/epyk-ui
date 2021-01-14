
from epyk.core.html import geo


class JqueryVertorMap(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "JqV"

  def add_map(self, name, continent=False):
    """
    Description:
    ------------
    Add the Javascript external package defining the map to the page.

    Related Pages:
    --------------

      https://www.10bestdesign.com/jqvmap/

    Attributes:
    ----------
    :param name: String. The map alias.
    :param continent: Boolean. Optional.
    """
    version = self.parent.context.rptObj.imports.jsImports["jqvmap"]['versions'][0]
    self.parent.context.rptObj.imports.addPackage('jqvm-%s' % name, {
      'version': version, 'req': [{'alias': 'jqvmap'}],
      'modules': [
        {'script': 'jquery.vmap.%s.js' % name, 'node_path': 'dist/',
         'path': 'jqvmap/%(version)s/maps/continents/' if continent else 'jqvmap/%(version)s/maps/'}]})
    self.parent.context.rptObj.jsImports.add("jqvm-%s" % name)

  def asia(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("asia", continent=options.get("continent", True))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "asia_en"
    return chart

  def australia(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("australia", continent=options.get("continent", True))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "australia_en"
    return chart

  def north_america(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("north-america", continent=options.get("continent", True))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "north-america_en"
    return chart

  def south_america(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("south-america", continent=options.get("continent", True))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "south-america_en"
    return chart

  def africa(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("africa", continent=True)
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "africa_en"
    return chart

  def france(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    self.add_map("france")
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "france_fr"
    return chart

  def europe(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("europe", continent=options.get("continent", True))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "europe_en"
    return chart

  def world(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map("world", continent=options.get("continent", False))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "world_en"
    return chart

  def usa(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    self.add_map("usa")
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "usa_en"
    return chart

  def map(self, name, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    options = options or {}
    self.add_map(name, continent=options.get("continent", False))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    return chart
