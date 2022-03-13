
from epyk.core.js import JsUtils


class Samples:

  def __init__(self, page):
    self.page = page

  def scale_linear(self, count_: int = None, attrs: dict = None):
    """
    Description:
    ------------
    Add linear scale definition from JavaScript.

    Usage::

      page.js.samples.scale_linear(count_=12)

    Attributes:
    ----------
    :param count_: The number of items in the list.
    :param attrs: Any other parameters in this function.
    """
    self.page._props['js'].setdefault('functions', {})["scaleLinear"] = {
      'content': '''
var cfg = config || {}; var count = cfg.count || 12; var labels = [];
for (let i = 0; i < count; ++i) {
  labels.push(i.toString());
} return labels ''',
      'pmt': ["config"]}
    attrs = attrs or {}
    if count_ is not None:
      attrs["count"] = count_
    return JsUtils.jsWrap("scaleLinear({})".format(JsUtils.jsConvertData(attrs, None)))

  def rand(self, min_: int = 0, max_: int = 1, seed: int = None, from_: int = 0, attrs: dict = None):
    """
    Description:
    ------------
    Get a random number.

    Usage::

      page.js.samples.rand(min_=-100, max_=100)

    Attributes:
    ----------
    :param min_: The min value for the items.
    :param max_: The max value for the items.
    :param seed: The seed for the random function.
    :param attrs: Any other parameters in this function.
    """
    self.page._props['js'].setdefault('functions', {})["sampleRand"] = {
      'content': '''
    var cfg = config || {}; var min = cfg.min || 0; var max = cfg.max || 1; var from = cfg.from || 0;
    var _seed = cfg.seed || Date.now() + Math.floor(Math.random() * 100);
    var seed = _seed; min = min === undefined ? 0 : min;
    max = max === undefined ? 1 : max; _seed = (seed * 9301 + 49297) % 233280;
    value = from +  min + (_seed / 233280) * (max - min);
    return value''',
      'pmt': ["config"]}
    attrs = attrs or {}
    attrs["from"] = from_
    if seed is not None:
      attrs["seed"] = seed
    if min_ is not None:
      attrs["min"] = min_
    if max_ is not None:
      attrs["max"] = max_
    return JsUtils.jsWrap("sampleRand({})".format(JsUtils.jsConvertData(attrs, None)))

  def months(self, count_: int = None, section: int = None, attrs: dict = None):
    """
    Description:
    ------------
    Return a list with the months labels..

    Usage::

      page.js.samples.months(count_=7)

    Attributes:
    ----------
    :param count_: The number of items in the list.
    :param section: The number of characters for the labels.
    :param attrs: Any other parameters in this function.
    """
    self.page._props['js'].setdefault('functions', {})["sampleMonths"] = {
      'content': '''
var engMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
'November', 'December'];
var cfg = config || {}; var count = cfg.count || 12; var section = cfg.section; var values = []; var i, value;
for (i = 0; i < count; ++i) {
  value = engMonths[Math.ceil(i) % 12]; values.push(value.substring(0, section)); }; return values''',
      'pmt': ["config"]}
    attrs = attrs or {}
    if count_ is not None:
      attrs["count"] = count_
    if section is not None:
      attrs["section"] = section
    return JsUtils.jsWrap("sampleMonths({})".format(JsUtils.jsConvertData(attrs, None)))

  def numbers(self, count_: int = None, min_: int = 0, max_: int = 1, decimals: int = 8, attrs: dict = None):
    """
    Description:
    ------------
    Return a list of random numbers.

    Usage::

      page.js.samples.numbers(count_=7, min_=-100, max_=100)

    Attributes:
    ----------
    :param count_: The number of items in the returned list.
    :param min_: The min value for the items.
    :param max_: The max value for the items.
    :param decimals: Number of decimals.
    :param attrs: Any other parameters in this function.
    """
    self.page._props['js'].setdefault('functions', {})["sampleNumbers"] = {
      'content': '''
var cfg = config || {}; var min = cfg.min || 0; var max = cfg.max || 1; var from = cfg.from || [];
var count = cfg.count || 8; var decimals = cfg.decimals || 8;
var continuity = cfg.continuity || 1; var dfactor = Math.pow(10, decimals) || 0; var data = []; var i, value;
var _seed = Date.now() + Math.floor(Math.random() * 100);
for (i = 0; i < count; ++i) {
  var seed = _seed; min = min === undefined ? 0 : min;
  max = max === undefined ? 1 : max; _seed = (seed * 9301 + 49297) % 233280;
  value = (from[i] || 0) +  min + (_seed / 233280) * (max - min);
  data.push(Math.round(dfactor * value) / dfactor);
}; return data''',
      'pmt': ["config"]}
    attrs = attrs or {}
    attrs["decimals"] = decimals
    if count_ is not None:
      attrs["count"] = count_
    if min_ is not None:
      attrs["min"] = min_
    if max_ is not None:
      attrs["max"] = max_
    return JsUtils.jsWrap("sampleNumbers({})".format(JsUtils.jsConvertData(attrs, None)))

  def points(self, count_: int = None, min_: int = 0, max_: int = 1, attrs: dict = None):
    """
    Description:
    ------------
    Return a list of random series of points with x, y coordinates.

    Usage::

      page.js.samples.points(count_=7, min_=-100, max_=100)

    Attributes:
    ----------
    :param count_: The number of items in the returned list.
    :param min_: The min value for the items.
    :param max_: The max value for the items.
    :param attrs: Any other parameters in this function.
    """
    self.rand(min_, max_) # to register the JavaScript function
    attrs = attrs or {}
    if count_ is not None:
      attrs["count"] = count_
    if min_ is not None:
      attrs["min"] = min_
    if max_ is not None:
      attrs["max"] = max_
    return JsUtils.jsWrap('''(function(config){
var records = []; var count = config.count || 12; var labels = [];
for (let i = 0; i < count; ++i) {records.push({x: sampleRand(config), y: sampleRand(config)})}
return records})(%s)
      '''% JsUtils.jsConvertData(attrs, None))

  def bubble(self, count_: int = None, min_: int = 0, max_: int = 1, r_min: int = 1, r_max: int = 10, attrs: dict = None):
    """
    Description:
    ------------
    Return a list of random series with x, y and r coordinates.

    Usage::

      page.js.samples.bubble(count_=7, min_=-100, max_=100)

    Attributes:
    ----------
    :param count_: The number of items in the returned list.
    :param min_: The min value for the items.
    :param max_: The max value for the items.
    :param r_min: The radius minimum for the point.
    :param r_max: The radius maximum for the point.
    :param attrs: Any other parameters in this function.
    """
    self.rand(min_, max_)   # to register the JavaScript function
    attrs = attrs or {}
    if count_ is not None:
      attrs["count"] = count_
    if r_min is not None:
      attrs["r_min"] = r_min
    if r_max is not None:
      attrs["r_max"] = r_max
    if min_ is not None:
      attrs["min"] = min_
    if max_ is not None:
      attrs["max"] = max_
    return JsUtils.jsWrap('''(function(config){
var records = []; var count = config.count || 12; var labels = [];
for (let i = 0; i < count; ++i) {records.push({r: sampleRand({min: config.r_min, max: config.r_max}), x: sampleRand(config), y: sampleRand(config)})}
return records})(%s)
      '''% JsUtils.jsConvertData(attrs, None))