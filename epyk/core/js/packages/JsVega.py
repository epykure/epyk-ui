
from typing import Any
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class VegaChangeset:
  def __init__(self, component: primitives.HtmlModel, selector, js_code=None, set_var=None, parent=None):
    self.component, self._selector, self.varName = component, selector, js_code
    self._js, self.setVar, self.component = [], set_var, parent

  def remove(self, data: Any):
    """

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    self._js.append("remove(%s)" % data)
    return self

  def removeAll(self):
    """

    Related Pages:


    """
    self._js.append("remove(vega.truthy)")
    return self

  def insert(self, data: Any):
    """

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    self._js.append("insert(%s)" % data)
    return self


class Vega(JsPackage):
  lib_alias = {'js': "vega", 'css': 'vega'}

  def __init__(self, component: primitives.HtmlModel, js_code: str, set_var: bool = False,
               page: primitives.PageModel = None):
    super(Vega, self).__init__(component=component, js_code=js_code, selector=js_code, set_var=set_var, page=page)

  @property
  def changeset(self):
    return VegaChangeset(self.component, selector="%s.svg" % self._selector)


class VegaView:

  def __init__(self, component: primitives.HtmlModel, selector: str, js_code: str = None, set_var: bool = None,
               page: primitives.PageModel = None):
    self.component, self._selector, self.varName = component, selector, js_code
    self._js, self.setVar, self.component = [], set_var, page

  def change(self, name, changeset):
    """
    Updates the data set with the given name with the changes specified by the provided changeset instance.
    This method does not force an immediate update to the view: invoke the runAsync method when ready.
    To issue a series of changes, insertions, or deletions, be sure to await the results of runAsync before issuing
    the next change.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    :param name:
    :param changeset:
    """
    pass

  def insert(self, name, tuples):
    """
    Inserts an array of new data tuples into the data set with the given name, then returns this view instance.
    The input tuples array should contain one or more data objects that are not already included in the data set.
    This method does not force an immediate update to the view: invoke the runAsync method when ready.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    :param name:
    :param tuples:
    """
  def remove(self, name, tuples):
    """
    Removes data tuples from the data set with the given name, then returns this view instance.
    The tuples argument can either be an array of tuples already included in the data set, or a predicate function
    indicating which tuples should be removed. This method does not force an immediate update to the view: invoke the
    runAsync method when ready.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    :param name:
    :param tuples:
    """

  def run(self, encode=None, prerun=None, postrun=None):
    """

    Related Pages:

      https://vega.github.io/vega/docs/api/view/#view_run

    :param encode:
    :param prerun:
    :param postrun:
    """
    pass

  def runAfter(self, callback):
    """

    Related Pages:

      https://vega.github.io/vega/docs/api/view/#view_runAfter

    :param callback:
    """

  def runAsync(self, encode=None, prerun=None, postrun=None):
    """

    :param encode:
    :param prerun:
    :param postrun:
    """


class VegaChart(JsPackage):
  lib_alias = {'js': "vega", 'css': 'vega'}

  def parse(self, data):
    return JsUtils.jsWrap("vega.parse(%s)" % JsUtils.jsConvertData(data, None))

  def toSVG(self, scale_factor):
    pass

  def toImageURL(self, kind, scale_factor):
    pass

  def toCanvas(self, scale_factor, options=None):
    pass

  def events(self, source, type, filter):
    pass
