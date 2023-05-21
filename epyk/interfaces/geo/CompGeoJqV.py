
import logging

from typing import Union
from epyk.core.html import geo
from epyk.core.html.geo import mappings
from epyk.core.html import Defaults_html


class JqueryVertorMap:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "JqV"

  def add_map(self, name: str, continent: bool = False):
    """ Add the Javascript external package defining the map to the page.

    Related Pages::

      https://www.10bestdesign.com/jqvmap/

    :param name: String. The map alias.
    :param continent: Boolean. Optional.
    """
    version = self.page.imports.jsImports["jqvmap"]['versions'][0]
    self.page.imports.addPackage('jqvm-%s' % name, {
      'version': version, 'req': [{'alias': 'jqvmap'}],
      'register': {'alias': 'map_%s' % name, 'module': 'jquery.vmap.%s' % name, 'npm_path': 'dist/maps/continents/'},
      'modules': [
        {'script': 'jquery.vmap.%s.js' % name, 'node_path': 'dist/maps/continents/' if continent else 'dist/maps/',
         'path': 'jqvmap/%(version)s/maps/continents/' if continent else 'jqvmap/%(version)s/maps/'}]})
    self.page.jsImports.add("jqvm-%s" % name)

  def asia(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
           options: dict = None, width: Union[int, tuple] = (100, "%"),
           height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::


    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("asia", continent=options.get("continent", True))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.asia.c:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.asia.c[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "asia_en"
    chart.options.values = data
    return chart

  def australia(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
                options: dict = None, width: Union[int, tuple] = (100, "%"),
                height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::


    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("australia", continent=options.get("continent", True))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.australia.c:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.australia.c[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "australia_en"
    chart.options.values = data
    return chart

  def north_america(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
                    options: dict = None, width: Union[int, tuple] = (100, "%"),
                    height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::


    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("north-america", continent=options.get("continent", True))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.america.n_c:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.america.n_c[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "north-america_en"
    chart.options.values = data
    return chart

  def south_america(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
                    options: dict = None, width: Union[int, tuple] = (100, "%"),
                    height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("south-america", continent=options.get("continent", True))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.america.s_c:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.america.s_c[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)
    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "south-america_en"
    chart.options.values = data
    return chart

  def africa(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
             options: dict = None, width: Union[int, tuple] = (100, "%"),
             height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::


    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("africa", continent=True)
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.africa.c:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.africa.c[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "africa_en"
    chart.options.values = data
    return chart

  def france(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
             options: dict = None, width: Union[int, tuple] = (100, "%"),
             height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

      fr = page.ui.geo.jqv.france()
      fr.options.multiSelectRegion = True
      fr.click([
        page.js.console.log(libs.jqvmap.region),
        page.js.console.log(libs.jqvmap.code),
        page.js.console.log(libs.jqvmap.element),
        page.js.console.log("data", skip_data_convert=True),
      ])

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("france")
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.france.r:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.france.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "france_fr"
    chart.options.values = data
    return chart

  def germany(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
              options: dict = None, width: Union[int, tuple] = (100, "%"),
              height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("germany")
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.germany.r:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.germany.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "germany_en"
    chart.options.values = data
    return chart

  def europe(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
             options: dict = None, width: Union[int, tuple] = (100, "%"),
             height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("europe", continent=options.get("continent", True))
    mapping_mp = mappings.europe.c if options.get("continent", True) else mappings.europe.r
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mapping_mp:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mapping_mp[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "europe_en"
    chart.options.values = data
    return chart

  def world(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
            options: dict = None, width: Union[int, tuple] = (100, "%"),
            height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("world", continent=options.get("continent", False))
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            if rec[x_axis] not in mappings.world.r:
              if options.get("verbose", False) or self.page.verbose:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
              continue

            state = mappings.world.r[rec[x_axis]]
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "world_en"
    chart.options.values = data
    return chart

  def usa(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
          options: dict = None, width: Union[int, tuple] = (100, "%"),
          height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    self.add_map("usa")
    data = {}
    if record is not None:
      for rec in record:
        if rec[y_column]:
          try:
            state = mappings.usa.r.get(rec[x_axis], rec[x_axis])
            if options.get("verbose", False) or self.page.verbose:
              if rec[x_axis] not in mappings.usa.r:
                logging.warning("Missing country mapping for %s" % rec[x_axis])
            data[state] = data.get(state, 0) + float(rec[y_column])
          except Exception as err:
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.map = "usa_en"
    chart.options.values = data
    return chart

  def map(self, name: str, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
          options: dict = None, width: Union[int, tuple] = (100, "%"),
          height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Related Pages:

      https://www.10bestdesign.com/jqvmap/

    Usage::

    :param name: String. The map alias.
    :param record: List. Optional. The records
    :param y_column: String. Optional. The column in the record for the keys.
    :param x_axis: String. Optional. The column in the record for the values.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
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
            if options.get("verbose", False) or self.page.verbose:
              logging.warning(rec)
              logging.warning(err)

    self.add_map(name, continent=options.get("continent", False))
    chart = geo.GeoJqv.JqueryVectorMap(self.page, width, height, html_code, options or {}, profile)
    chart.options.values = data
    return chart
