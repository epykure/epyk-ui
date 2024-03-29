#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, Any
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject
from epyk.core.js.packages import JsPackage

# All the predefined variable types
from epyk.core.js.fncs import JsFncs


class D3ScaleLinear:
  """

  """
  def __init__(self, range):
    self.range = range

  def range(self):
    pass


# class D3Html(JsPackage):
#   lib_alias = {"js": 'd3'}
#
#   def __init__(self, src, selector, tag, setVar=False):
#     self.src, self._selector, self.setVar, self.tag = src, selector, setVar, tag
#     self.__js_uniq_fncs, self.varName, self.setVar, self.src = {}, None, setVar, src
#     self._js, self._u, self._js_enums = [[]], {}, {} # a list of list of object definition
#
#   def append(self, htmlType, setVar=True):
#     """
#     If the specified type is a string, appends a new element of this type (tag name) as the last child of each selected element, or before the next following sibling in the update selection if this is an enter selection.
#
#     Documentation
#     https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selecting-elements
#
#     :param htmlType:
#     """
#     cnv_htmlType = JsUtils.jsConvertData(htmlType, None)
#     return D3Html(self.src, "%s.append(%s)" % (self.toStr(), cnv_htmlType), htmlType, setVar=setVar)
#
#   def rappend(self, htmlType):
#     return self.append(htmlType, setVar=False)
#
#   def attr(self, key, val):
#     """
#
#     :param key:
#     :param val:
#     """
#     return self.fnc("attr(%s, %s)" % (JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None)))
#
#   def text(self, data):
#     return self.fnc("text(function(column) { return column; })")
#
#   def html(self, data):
#     return self.fnc("html(function(d) { return d.value; })")
#
#   def selectAll(self, d3Type):
#     self.fnc("selectAll(%s)" % JsUtils.jsConvertData(d3Type, None))
#     return D3Select(self.src, selector=self.toStr())


class D3Select(JsPackage):
  lib_alias = {"js": 'd3'}

  def data(self, datasets: Union[list, primitives.JsDataModel] = None):
    """   Binds the specified array of data with the selected elements,
    returning a new selection that represents the update selection: the elements successfully bound to data.

    The data is specified for each group in the selection.
    If the selection has multiple groups (such as d3.selectAll followed by selection.selectAll),
    then data should typically be specified as a function.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selection_data

    :param Union[list, primitives.JsDataModel] datasets: The data set object.
    """
    if datasets is None:
      self.fnc("data()")
    else:
      #datasets = JsUtils.jsConvertData(datasets, None)
      self.fnc("data(%s)" % datasets)
    return self

  def dataRecord(self, columns: Union[list, primitives.JsDataModel]):
    """   Convert a list of dictionaries to an iterator which will return ordered arrays based on the columns definition.

    Related Pages:

      http://bl.ocks.org/gka/17ee676dc59aa752b4e6

    :param Union[list, primitives.JsDataModel] columns: The columns to be retrieved for each row.
    """
    return self.fnc('''data(function(row, i) { var cell = []; %s.forEach(function(k) { cell.push(row[k]);
        }); return cell; }) ''' % JsUtils.jsConvertData(columns, None))

  def dataFncRows(self, columns):
    """   

    :param columns:
    """
    self.fnc("data(function(row) {return %s.map(function(c, i) {return {column: c, value: row[i]}; }); })" % columns)
    return self

  def datum(self, datasets: Union[list, primitives.JsDataModel] = None):
    """   Gets or sets the bound data for each selected element.
    Unlike selection.data, this method does not compute a join and does not affect indexes or the enter and
    exit selections.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selection_datum

    :param Union[list, primitives.JsDataModel] datasets: If a value is not specified, returns the bound datum for the first (non-null) element in the selection.
    """
    if datasets is None:
      self.fnc("datum()")
    else:
      self.fnc("datum(%s)" % JsUtils.jsConvertData(datasets, None))
    return self

  def filter(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   You can filter a selection using D3’s .filter method.
    The first argument is a function which returns true if the element should be included.
    The filtered selection is returned by the filter method so you can continue chaining selection methods.

    Related Pages:

      https://www.d3indepth.com/selections/

    :param Union[list, str] js_funcs: The Javascript events when the DatePicker selection changes.
    :param Union[dict, bool] profile: Optional. Set to true to get the profile for the function on the Javascript console.
    """
    return self.fnc("filter(function(d, i) {%s} )" % (
      JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def sort(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   

    Related Pages:

      https://www.d3indepth.com/selections/

    :param js_funcs: String | List. The Javascript events when the DatePicker selection changes.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    """
    return self.fnc("sort(function(a, b) {%s} )" % (
      JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def enter(self):
    """   Returns the enter selection: placeholder nodes for each datum that had no corresponding DOM element in the
    selection. (The enter selection is empty for selections not returned by selection.data.)

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selection_enter
    """
    return self.fnc("enter()")

  def exit(self):
    """   Returns the exit selection: existing DOM elements in the selection for which no new datum was found.
    (The exit selection is empty for selections not returned by selection.data.)

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selection_exit
    """
    return self.fnc("exit()")

  def append(self, html_type, set_var=True):
    """   If the specified type is a string, appends a new element of this type (tag name) as the last child of each
    selected element, or before the next following sibling in the update selection if this is an enter selection.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selecting-elements

    :param html_type:
    :param bool set_var:
    """
    return self.fnc("append(%s)" % JsUtils.jsConvertData(html_type, None))

  def rappend(self, html_type):
    """   Recursive append function without defining the variable on the javascript side.

    :param html_type:
    """
    return self.append(html_type, set_var=False)

  def insert(self, html_type, id):
    pass

  def style(self, key, val=None, callback=None):
    """   Update the style.

    Related Pages:

      https://www.d3indepth.com/selections/

    :param key: String. The attribute key.
    :param val: String. Optional. The attribute value.
    :param callback: String. Optional. A javascript callback function using d (data) and i (index).
    """
    if val is None and callback is None:
      raise ValueError("Either val or callback must be defined")

    if callback is not None:
      return self.fnc("style(%s, function(d, i){return %s})" % (JsUtils.jsConvertData(key, None), callback))

    return self.fnc("style(%s, %s)" % (JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None)))

  def property(self, key, val=None, callback=None):
    """   Update an element's property.

    Related Pages:

      https://www.d3indepth.com/selections/

    :param key: String. The attribute key.
    :param val: String. Optional. The attribute value.
    :param callback: String. Optional. A javascript callback function using d (data) and i (index).
    """
    if val is None and callback is None:
      raise ValueError("Either val or callback must be defined")

    if callback is not None:
      return self.fnc("property(%s, function(d, i){return %s})" % (JsUtils.jsConvertData(key, None), callback))

    return self.fnc("property(%s, %s)" % (JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None)))

  def attr(self, key, val=None, callback=None):
    """   Update an attribute.

    Related Pages:

      https://gramener.github.io/d3js-playbook/events.html
      https://www.d3indepth.com/selections/

    :param key: String. The attribute key.
    :param val: String. Optional. The attribute value.
    :param callback: String. Optional. A javascript callback function using d (data) and i (index).
    """
    if val is None and callback is None:
      raise ValueError("Either val or callback must be defined")

    if callback is not None:
      return self.fnc("attr(%s, function(d, i){return %s})" % (JsUtils.jsConvertData(key, None), callback))

    return self.fnc("attr(%s, %s)" % (JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None)))

  def text(self, data=None, column=None):
    """   Update the text content.

    Related Pages:

      https://www.d3indepth.com/selections/

    :param data: Value. Optional. A Javascript function or a fixed value.
    :param column: String. Optional. the column name in the record.
    """
    if data is None and column is None:
      return self.fnc("text(function(d) { return d })")

    if column is not None:
      return self.fnc("text(function(d) { return d[%s]; })" % JsUtils.jsConvertData(column, None))

    return self.fnc("text(%s)" % JsUtils.jsConvertData(data, None))

  def transition(self, duration=None):
    """   

    Related Pages:

      https://gramener.github.io/d3js-playbook/events.html

    :param duration: Integer. Optional. The time in ms used for the transition state.
    """
    if duration is None:
      return self.fnc("transition()")

    return self.fnc("transition().duration(%s)" % duration)

  def html(self, data=None):
    """   

    :param data:
    """
    if data is None:
      return self.fnc("html(function(d) { return d; })")

    return self.fnc("html(function(d) { return %s; })" % data)

  def htmlByKey(self, data):
    """   

    :param data:
    """
    return self.fnc("html(function(d) {console.log('rrr'+ d); return d[%s]; })" % JsUtils.jsConvertData(data, None))

  def call(self, fnc_name):
    """   The .call method allows a function to be called into which the selection itself is passed as the first argument.

    :param fnc_name: String. A function name.
    """
    return self.fnc("call(%s)" % fnc_name)

  def on(self, event_type, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   Add an event to the component.

    :param event_type: String. The event name.
    :param js_funcs: String | List. The Javascript events when the DatePicker selection changes.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    """
    self.style("cursor", "pointer")
    return self.fnc("on(%s, function(data) {%s} )" % (
      JsUtils.jsConvertData(event_type, None), JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def hover(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   Mouse pointer has moved onto the element or its children.

    Related Pages:

      https://gramener.github.io/d3js-playbook/events.html
      https://www.d3indepth.com/selections/

    :param js_funcs: String | List. The Javascript events when the DatePicker selection changes.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    """
    return self.on("mouseover", js_funcs, profile)

  def click(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   Element has been clicked.

    Related Pages:

      https://gramener.github.io/d3js-playbook/events.html
      https://www.d3indepth.com/selections/

    :param js_funcs: String | List. The Javascript events when the DatePicker selection changes.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    """
    return self.on("click", js_funcs, profile)

  def remove(self):
    """   Removes the selected elements from the document.
    Returns this selection (the removed elements) which are now detached from the DOM.
    There is not currently a dedicated API to add removed elements back to the document; however, you can pass a
    function to selection.append or selection.insert to re-add elements.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selecting-elements
    """
    return self.fnc("remove()")

  def clone(self, deep: bool = False):
    """   Inserts clones of the selected elements immediately following the selected elements and returns a selection of
    the newly added clones.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selecting-elements

    :param bool deep: Optional. If deep is truthy, the descendant nodes of the selected elements will be cloned as well.
    """
    return self.fnc("clone(%s)" % JsUtils.jsConvertData(deep, None))

  def order(self):
    """   Re-inserts elements into the document such that the document order of each group matches the selection order.
    This is equivalent to calling selection.sort if the data is already sorted, but much faster.

    Related Pages:

      https://github.com/d3/d3-selection/blob/v1.4.0/README.md#selection_append
    """
    return self.fnc("order()")
  #
  # def select(self, id):
  #   return 'd3.select("%s")' % id

  def selectAll(self, d3_type):
    """   

    :param d3_type:
    """
    return self.fnc("selectAll(%s)" % JsUtils.jsConvertData(d3_type, None))


class D3ForceSimulation:
  _package = ['d3-force']

  def __init__(self, id=None, d3_type=None):
    """

    Documentation:
      - https://github.com/d3/d3-force

    :param id:
    :param d3_type:
    """
    pass

  def force(self, force_type, fnc):
    pass

  def restart(self):
    pass

  def stop(self):
    pass

  def tick(self, tick):
    pass

  def nodes(self, nodes):
    pass

  def alpha(self, number):
    pass

  def alphaDecay(self, number):
    pass

  def alphaTarget(self, target):
    pass

  def alphaTarget(self, number):
    pass

  def velocityDecay(self, decay):
    pass

  def find(self):
    pass

  def on(self):
    pass


class D3ForceManyBody:
  def strength(self):
    pass

  def distanceMax(self, x):
    pass

  def distanceMin(self, x):
    pass


class D3ForceCollide:
  def __init__(self, radius=None):
    """
    Creates a new circle collision force with the specified radius.
    If radius is not specified, it defaults to the constant one for all nodes.

    Documentation:
        - https://github.com/d3/d3-force#forceCollide

    :param radius:
    """
    pass

  def radius(self, func):
    """   If radius is specified, sets the radius accessor to the specified number or function,
    re-evaluates the radius accessor for each node, and returns this force.
    If radius is not specified, returns the current radius accessor

    Related Pages:

      https://github.com/d3/d3-force#forceCollide

    :param func:
    """
    pass

  def strength(self, strength):
    """   If strength is specified, sets the force strength to the specified number in the range [0,1] and returns this force.
    If strength is not specified, returns the current strength which defaults to 0.

    Related Pages:

      https://github.com/d3/d3-force#forceCollide

    :param strength:
    """
    pass

  def iterations(self, iterations):
    """   If iterations is specified, sets the number of iterations per application to the specified number and returns this
    force.

    Related Pages:

      https://github.com/d3/d3-force#forceCollide

    :param iterations:
    """
    raise NotImplementedError()


class D3ForceCenter:
  def __init__(self):
    pass

  def x(self):
    pass

  def y(self):
    pass


class D3Event:
  def __init__(self):
    """

    Documentation:
      - https://github.com/d3/d3-selection/blob/v1.4.0/README.md#event

    """
    pass

  def on(self):
    pass

  @property
  def active(self):
    pass

  @property
  def x(self):
    pass

  @property
  def y(self):
    pass

  def timeStamp(self):
    pass


class D3Pack:
  def __init__(self):
    """

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    """

  def radius(self, number):
    pass

  def size(self, number):
    """   If size is specified, sets this pack layout’s size to the specified two-element array of numbers [width, height]
    and returns this pack layout. If size is not specified, returns the current size, which defaults to [1, 1]

    Related Pages:

      https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param number:
    """
    pass

  def padding(self, number):
    """   If padding is specified, sets this pack layout’s padding accessor to the specified number or function and returns
    this pack layout. If padding is not specified, returns the current padding accessor, which defaults to the constant
    zero.

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param number:
    """
    pass

  def packSiblings(self, circles):
    """   Packs the specified array of circles, each of which must have a circle.r property specifying the circle’s radius.

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param circles:
    """
    pass

  def packEnclose(self, circles):
    """   Computes the smallest circle that encloses the specified array of circles, each of which must have a circle.r
    property specifying the circle’s radius, and circle.x and circle.y properties specifying the circle’s center

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param circles:
    """
    raise NotImplementedError()


class D3Band:
  """
  https://github.com/d3/d3-scale/blob/master/README.md#band-scales
  """

  def __init__(self, selector):
    """

    """
    self._selector = selector
    self._js = []

  def domain(self, domain=None):
    """   

    :param domain:
    """
    if domain is None:
      self._js.append("domain()")
    return self

  def range(self, range=None):
    """   

    :param range:
    """

  def rangeRound(self, range):
    """   

    :param range:
    """

  def round(self):
    """

    :return:
    """

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise ValueError("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    data = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return data


class D3File:

  def __init__(self, component: primitives.HtmlModel, filename: str, selector: str, page: primitives.PageModel = None):
    self._f, self.component, self._selector, self.page = filename, component, selector, page
    self._js_frg, self._js_ids, self._js_thens, self.profile = [], set(), [], None
    if page is None and self.component is not None:
      self.page = self.component.page

  def records(self, js_code: str):
    """   

    :param str js_code: The variable id to store the records.
    """
    self._js_frg.append("%s.push(row)" % js_code)
    return self

  def unpack(self, js_code: str, column: Union[str, primitives.JsDataModel] = None):
    """   

    :param str js_code: The variable id to store the records.
    :param Union[str, primitives.JsDataModel] column: The column name.
    """
    if js_code not in self._js_ids:
      column = JsUtils.jsConvertData(column, None)
      self._js_frg.append("%s.push(row[%s])" % (js_code, column))
      self._js_ids.add(js_code)
    return JsObject.JsObject(js_code, is_py_data=False)

  def filter(self, rules: list, keep: bool = True):
    """   Add a filter on a row. The rule needs to be fully defined.

    Usage::

      csv.filter("row['direction'] != 'Decreasing'")

    :param list rules: The javascript if expressions.
    :param bool keep: Boolean. Optional.
    """
    if not isinstance(rules, list):
      rules = [rules]
    if not keep:
      self._js_frg.append("if(%s){ return; }" % "&&".join(rules))
    else:
      self._js_frg.append("if(!(%s)){ return; }" % "&&".join(rules))
    return self

  def filterCol(self, column: Union[str, primitives.JsDataModel], value: Any, operator: str = "==", keep: bool = True):
    """   Add a filter on a specific column. Those functions can be chained.

    Usage::

      text = page.ui.input("Italy")
        page.ui.button("Click").click([
          page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).filterCol("Year", "2000", ">").row(
            page.js.console.log("row", skip_data_convert=True)).get(page.js.console.log("data", skip_data_convert=True))
        ])

    :param Union[str, primitives.JsDataModel] column: The column name.
    :param Any value: The column value.
    :param str operator: Optional. The comparison operator.
    :param bool keep: Optional.
    """
    column = JsUtils.jsConvertData(column, None)
    value = JsUtils.jsConvertData(value, None)
    if not keep:
      self._js_frg.append("if(row[%s] %s %s){ return; }" % (column, operator, value))
    else:
      self._js_frg.append("if(!(row[%s] %s %s)){ return; }" % (column, operator, value))
    return self

  def callback(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """   

    :param js_funcs: String. Javascript function.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._js_frg.append(js_funcs)
    self.profile = profile
    return self

  def then(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
    """   As the file loading with D3 is a promise, it is possible to put events when the response is received.
    This could allow the loading of components.

    Add a post process after on the entire data.

    This function can be chained.

    Usage::

      text = page.ui.input("Italy")
        page.ui.button("Click").click([
          page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).filterCol("Year", "2000", ">").row(
            page.js.console.log("row", skip_data_convert=True)).get(page.js.console.log("data", skip_data_convert=True))
        ])

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._js_thens.append(
      "then(function(data) {%s; return data})" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
    return self

  def cast(self, columns: list, to: str = "float", profile: Union[bool, dict] = None):
    """   

    :param list columns:
    :param str to:
    :param Union[dict, bool] profile:
    """
    for column in columns:
      if to == "float":
        self._js_frg.append(JsUtils.jsConvertFncs(
          "row['%(col)s'] = parseFloat(row['%(col)s'])" % {"col": column}, toStr=True, profile=profile))
      elif to == "int":
        self._js_frg.append(JsUtils.jsConvertFncs(
          "row['%(col)s'] = parseInt(row['%(col)s'])" % {"col": column}, toStr=True, profile=profile))
    return self

  def row(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   

    :param Union[list, str] js_funcs: Javascript functions.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._js_frg.append(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
    return self

  def get(self, js_funcs: Union[list, str], profile: Union[dict, bool] = None):
    """   

    Related Pages:

      https://github.com/d3/d3-request

    Usage::

      text = page.ui.input("Italy")
      page.ui.button("Click").click([
        page.js.d3.csv(data_urls.DEMO_COUNTRY).filterCol("Country Name", text.dom.content).filterCol("Year", "2000", ">").row(
          page.js.console.log("row", skip_data_convert=True)).get(page.js.console.log("data", skip_data_convert=True))
      ])

    :param Union[list, str] js_funcs: Javascript functions.
    :param Union[dict, bool] profile: Optional. A flag to set the component performance storage.
    """
    return self.then(js_funcs, profile)

  def toStr(self):
    file = JsUtils.jsConvertData(self._f, None)
    if self._js_ids:
      if self._js_thens:
        return "%s; %s(%s, function(row, err){%s; return row}).%s" % (
          ";".join(["var %s = []" % i for i in self._js_ids]), self._selector, file,
          JsUtils.jsConvertFncs(self._js_frg, toStr=True, profile=self.profile), ".".join(self._js_thens))

      return "%s; %s(%s, function(row, err){%s; return row})" % (
        ";".join(["var %s = []" % i for i in self._js_ids]), self._selector, file,
        JsUtils.jsConvertFncs(self._js_frg, toStr=True, profile=self.profile))

    if self._js_thens:
      return "%s(%s, function(row, err){%s; return row}).%s" % (
        self._selector, file, JsUtils.jsConvertFncs(
          self._js_frg, toStr=True, profile=self.profile), ".".join(self._js_thens))

    return "%s(%s, function(row, err){%s; return row})" % (
      self._selector, file, JsUtils.jsConvertFncs(self._js_frg, toStr=True, profile=self.profile))


class D3Svg:
  def __init__(self, component: primitives.HtmlModel, selector: str, js_code: str = None, set_var: bool = None,
               page: primitives.PageModel = None, container: primitives.HtmlModel = None):
    self.component, self._selector, self.varName = component, selector, js_code
    self._js, self.setVar, self.page, self.container = [], set_var, page, container

  def line(self):
    self._js.append("line()")
    return self

  def x(self):
    self._js.append("x(function(d) { return x(d.date1); })")
    return self

  def y(self):
    self._js.append("y(function(d) { return x(d.date1); })")
    return self

  def selectAll(self, tag):
    """   

    :param tag:
    """
    self._js.append("selectAll(%s)" % JsUtils.jsConvertData(tag, None))
    return D3Select(self.component, selector=self.toStr(), set_var=self.setVar, page=self.page)

  def toStr(self):
    content = [self._selector] + self._js
    if self.varName is not None and self.setVar:
      return "var %s = %s" % (self.varName, ".".join(content))

    return ".".join(content)


class D3Request(JsPackage):

  def header(self, key, value):
    """   

    :param key:
    :param value:
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    return self.fnc('header(%s, %s)' % (key, value))

  def timeout(self, value):
    """   If timeout is specified, sets the timeout attribute of the request to the specified number of milliseconds and
    returns this request instance. If timeout is not specified, returns the current response timeout,
    which defaults to 0.

    Related Pages:

      https://github.com/d3/d3-request

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return self.fnc('timeout(%s)' % value)

  def mimeType(self, mine_type):
    """   If type is specified, sets the request mime type to the specified value and returns this request instance.
    If type is null, clears the current mime type (if any) instead.
    If type is not specified, returns the current mime type, which defaults to null.
    The mime type is used to both set the "Accept" request header and for overrideMimeType, where supported.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.tsv
      https://github.com/d3/d3-request

    :param mine_type:
    """
    mine_type = JsUtils.jsConvertData(mine_type, None)
    return self.fnc('mimeType(%s)' % mine_type)

  def response(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   

    The response text object is in the variable data.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.tsv

    :param js_funcs:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return self.fnc(
      'response(function(xhr) {var data = xhr.responseTex; %s})' % JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile))

  def get(self, js_funcs: Union[list, str], profile: Union[dict, bool] = False):
    """   

    The function parameters is defined with tee variable data

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.tsv

    :param js_funcs:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return self.fnc('get(function(data) {%s})' % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))


class D3GeoProjection(JsPackage):
  lib_alias = {"js": 'd3'}

  def center(self, lat, long):
    """   """
    return self.fnc("center([%s, %s])" % (lat, long))

  def scale(self, num):
    """   

    :param num:
    """
    return self.fnc("scale(%s)" % num)

  def rotate(self):
    pass

  def translate(self):
    pass


class D3GeoPath(JsPackage):
  lib_alias = {"js": 'd3'}

  def projection(self, proj):
    pass


class D3Geo:

  def mercator(self):
    pass

  def equirectangular(self):
    pass

  def path(self):
    return D3GeoPath()


class JsD3(JsPackage):

  lib_alias = {"js": 'd3'}
  lib_selector = 'd3'

  @property
  def svg(self):
    return D3Svg(component=self.component, selector="%s.svg" % self._selector, page=self.page)

  @JsUtils.fromVersion({"d3": "4.0.0"})
  def csv(self, url):
    """   Sends http request to the specified url to load .csv file or data and executes callback function with parsed
    csv data objects.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.csv

    :param url: String. The url path of the file.
    """
    return D3File(component=self.component, filename=url, selector="%s.csv" % self._selector, page=self.page)

  @JsUtils.fromVersion({"d3": "4.0.0"})
  def tsv(self, url):
    """   Sends http request to the specified url to load a .tsv file or data and executes callback function with parsed
    tsv data objects.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.tsv

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.tsv" % self._selector)

  @JsUtils.fromVersion({"d3": "4.0.0"})
  def xml(self, url):
    """   Sends http request to the specified url to load an .xml file or data and executes callback function with parsed
    xml data objects.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.xml
      https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.tsv" % self._selector)

  @JsUtils.fromVersion({"d3": "4.0.0"})
  def json(self, url):
    """   Sends http request to the specified url to load .json file or data and executes callback function with parsed
    json data objects.

    Related Pages:

      https://www.tutorialsteacher.com/d3js/loading-data-from-file-in-d3js#d3.json

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.json" % self._selector)

  def text(self, url):
    """   Returns a new request to get the text file at the specified url with the default mime type text/plain.
    If no callback is specified, this is equivalent to:

    Related Pages:

        https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.text" % self._selector)

  def blob(self, url):
    """   Fetches the binary file at the specified input URL as a Blob.
    If init is specified, it is passed along to the underlying call to fetch; see RequestInit for allowed fields.

    Related Pages:

        https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.blob" % self._selector)

  def html(self, url):
    """   Fetches the file at the specified input URL as text and then parses it as HTML.
    f init is specified, it is passed along to the underlying call to fetch; see RequestInit for allowed fields.

    Related Pages:

        https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.html" % self._selector)

  def image(self, url):
    """   Fetches the image at the specified input URL.
    If init is specified, sets any additional properties on the image before loading.

    Related Pages:

        https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.image" % self._selector)

  def dsv(self, url):
    """   Fetches the DSV file at the specified input URL.
    If init is specified, it is passed along to the underlying call to fetch; see RequestInit for allowed fields.
    An optional row conversion function may be specified to map and filter row objects to a more-specific
    representation; see dsv.parse for details.

    Related Pages:

        https://github.com/d3/d3-fetch

    :param url: String. The url path of the file.
    """
    return D3File(self.component, url, selector="%s.tsv" % self._selector)

  def min(self, dataset, js_funcs):
    return JsNumber.JsNumber("d3.min(%s, %s)" % (dataset, js_funcs))

  def max(self, dataset, js_funcs):
    return JsNumber.JsNumber("d3.max(%s, %s)" % (dataset, js_funcs))

  def select(self, tag, js_code: str = None):
    tag = JsUtils.jsConvertData(tag, None)
    if js_code is not None:
      return D3Select(self.component, selector="d3.select(%s)" % tag, js_code=js_code, set_var=True)

    return D3Select(self.component, selector="d3.select(%s)" % tag, set_var=False)

  def selectAll(self, d3_type, set_var=False) -> D3Select:
    return D3Select(d3_type=d3_type, set_var=set_var)

  def scaleLinear(self, range) -> D3ScaleLinear:
    return D3ScaleLinear(range)

  def scaleBand(self, range=None) -> D3Band:
    """   Constructs a new band scale with the specified domain and range, no padding, no rounding and center alignment.
    If domain is not specified, it defaults to the empty domain.
    If range is not specified, it defaults to the unit range [0, 1].

    :param range:

    :rtype: D3Band
    """
    if range is None:
      self._js.append("scaleBand()")
    return D3Band(self.toStr())

  def forceSimulation(self, nodes=None):
    return D3ForceSimulation(nodes)

  def forceManyBody(self):
    return D3ForceManyBody()

  def scaleOrdinal(self, colors):
    pass

  def forceX(self):
    pass

  def forceY(self):
    pass

  def drag(self):
    pass

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise ValueError("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    data = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return data
