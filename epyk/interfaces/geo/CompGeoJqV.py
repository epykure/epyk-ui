
import logging

from epyk.core.html import geo
from epyk.core.html.geo import mappings


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
        {'script': 'jquery.vmap.%s.js' % name, 'node_path': 'dist/maps/continents/' if continent else 'dist/maps/',
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

  def france(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage:
    -----


    Attributes:
    ----------
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("france")
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.france.r:
              if options.get("verbose", False) or self.parent.context.rptObj.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.france.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "france_fr"
    chart.options.values = data
    return chart

  def europe(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage:
    -----

    Attributes:
    ----------
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("europe", continent=options.get("continent", True))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.europe.r:
              if options.get("verbose", False) or self.parent.context.rptObj.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.europe.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "europe_en"
    chart.options.values = data
    return chart

  def world(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage:
    -----

    Attributes:
    ----------
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("world", continent=options.get("continent", False))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.world.r:
              if options.get("verbose", False) or self.parent.context.rptObj.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.world.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "world_en"
    chart.options.values = data
    return chart

  def usa(self, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage:
    -----

    Attributes:
    ----------
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("usa")
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            state = mappings.usa.r.get(rec[x_axis], rec[x_axis])
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              if rec[x_axis] not in mappings.usa.r:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.map = "usa_en"
    chart.options.values = data
    return chart

  def map(self, name, record=None, y_column=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage:
    -----

    Attributes:
    ----------
    :param name: String. The map alias.
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            state = rec[x_axis]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.parent.context.rptObj.verbose:
              logging.warning(rec)
              logging.warning(err)

    self.add_map(name, continent=options.get("continent", False))
    chart = geo.GeoJqv.JqueryVectorMap(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    chart.options.values = data
    return chart
