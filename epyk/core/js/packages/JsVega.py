
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class VegaChangeset:
  def __init__(self, src, selector, varName=None, setVar=None, parent=None):
    self.src, self._selector, self.varName = src, selector, varName
    self._js, self.setVar, self.component = [], setVar, parent

  def remove(self, jsData):
    """

    https://vega.github.io/vega/docs/api/view/

    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    self._js.append("remove(%s)" % jsData)
    return self

  def removeAll(self):
    """

    """
    self._js.append("remove(vega.truthy)")
    return self

  def insert(self, jsData):
    """

    https://vega.github.io/vega/docs/api/view/

    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    self._js.append("insert(%s)" % jsData)
    return self


class Vega(JsPackage):
  lib_alias = {'js': "vega", 'css': 'vega'}

  def __init__(self, src, varName, setVar=False, report=None):
    super(Vega, self).__init__(src=src, varName=varName, selector=varName, setVar=setVar)
    self._report = report

  @property
  def changeset(self):
    return VegaChangeset(self.src, selector="%s.svg" % self._selector)


class VegaView:

  def __init__(self, src, selector, varName=None, setVar=None, parent=None):
    self.src, self._selector, self.varName = src, selector, varName
    self._js, self.setVar, self.component = [], setVar, parent

  def change(self, name, changeset):
    """
    Description:
    ------------
    Updates the data set with the given name with the changes specified by the provided changeset instance.
    This method does not force an immediate update to the view: invoke the runAsync method when ready.
    To issue a series of changes, insertions, or deletions, be sure to await the results of runAsync before issuing
    the next change.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    Attributes:
    ----------
    :param name:
    :param changeset:
    """
    pass

  def insert(self, name, tuples):
    """
    Description:
    ------------
    Inserts an array of new data tuples into the data set with the given name, then returns this view instance.
    The input tuples array should contain one or more data objects that are not already included in the data set.
    This method does not force an immediate update to the view: invoke the runAsync method when ready.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    Attributes:
    ----------
    :param name:
    :param tuples:
    """
  def remove(self, name, tuples):
    """
    Description:
    ------------
    Removes data tuples from the data set with the given name, then returns this view instance.
    The tuples argument can either be an array of tuples already included in the data set, or a predicate function
    indicating which tuples should be removed. This method does not force an immediate update to the view: invoke the
    runAsync method when ready.

    Related Pages:

      https://vega.github.io/vega/docs/api/view/

    Attributes:
    ----------
    :param name:
    :param tuples:
    """

  def run(self, encode=None, prerun=None, postrun=None):
    """

    https://vega.github.io/vega/docs/api/view/#view_run

    :param encode:
    :param prerun:
    :param postrun:
    """
    pass

  def runAfter(self, callback):
    """
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

  def __init__(self, src, varName, setVar=False, report=None):
    super(VegaChart, self).__init__(src=src, varName=varName, selector=varName, setVar=setVar)
    self._report = report

  def parse(self, jsData):
    return JsUtils.jsWrap("vega.parse(%s)" % JsUtils.jsConvertData(jsData, None))

  def toSVG(self, scaleFactor):
    pass

  def toImageURL(self, kind, scaleFactor):
    pass

  def toCanvas(self, scaleFactor, options=None):
    pass

  def events(self, source, type, filter):
    pass
