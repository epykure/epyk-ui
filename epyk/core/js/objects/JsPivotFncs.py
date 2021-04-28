
import sys
import inspect

factory = None


def getAggFnc():
  """
  Description:
  -----------
  Load all the aggregation definitions defined in this module in a factory.

  This will be structured as a dictionary with as key the name of the aggregator and as value the object.
  This factory will store directly the object as the structure cannot be dynamic and it is not expecting any input.
  The dynamic part will be added as input of the toJs() function.
  """
  global factory

  if factory is None:
    tmpFactory = {}
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
      if getattr(obj, 'name', None) not in [None, '__main__'] and issubclass(obj, JsPivotAggFnc):
        tmpFactory[obj.name] = obj()
    # Atomic function to avoid asynchronous clashes on the server
    factory = tmpFactory
  return factory


class JsPivotAggFnc:
  """
  Description:
  -----------
  Based abstract class for the Javascript Pivot aggregator.

  The base class will define the slots of the expected class variables that the child classes should defined.
  The toJs function will, thanks to the options inputs, will create the Javascript dictionary that the PivotTable
  library is expecting.
  """
  name = None
  __slots__ = ['keyAgg', 'key2Agg', 'numInputs', 'push', 'value', 'format']

  def toJs(self, options):
    """
    Description:
    -----------
    Convert the aggregator object to a Javascript dictionary usable in the Pivot Table javascript library.
    All the parameters will be standard to the Js module and this will convert the Python object to the
    corresponding Javascript ones.
    """
    jsPivot = ["tmpVal: 0"]
    jsMapFncs = {'push': "function(record) {%s}", 'value': "function() {%s}", 'format': 'function(x) {%s}'}
    _opts = dict(getattr(self, '_dflts', {}))
    _opts.update(options)
    self.numInputs = 2 if getattr(self, "key2Agg", None) is not None else 1
    for slot in self.__slots__:
      slotVal = getattr(self, slot) % _opts if slot in ['push', 'value', 'format'] else getattr(self, slot)
      if slotVal is None:
        continue

      if slot in jsMapFncs:
        if slot in ['value', 'format'] and not 'return ' in slotVal:
          raise Exception("value and format should return a value")

        jsPivot.append("%s: %s" % (slot, jsMapFncs[slot] % slotVal))
      else:
        jsPivot.append("%s: %s" % (slot, slotVal))
    return "{%s}" % ", ".join(jsPivot)


# -------------------------------------------------------------------------------------------------------------------
#                           SIMPLE TRANSFORMATION USING ONE KEY
#
class JsPivotSumAgg(JsPivotAggFnc):
  """
  Description:
  -----------
  Aggregator in charge of adding up all the values based on the defined rows.
  This aggregator will generically sum the selected values per rows and columns.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "Sum Agg", 'digits': 0})
  """
  _dflts = {'digits': 0}  # Cannot be changed directly in the class

  name = "Sum Agg"
  keyAgg, key2Agg = 0, None
  push = 'this.keyAgg += parseFloat(record[attributeArray[0]])'
  value = 'return this.keyAgg'
  format = 'return numberWithCommas(x.toFixed(%(digits)s))'


class JsPivotAbsSumAgg(JsPivotSumAgg):
  """
  Description:
  -----------
  Aggregator in charge of adding up all the absolute values based on the defined rows.
  This aggregator will generically sum the absolute selected values per rows and columns.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "Abs Sum Agg", 'digits': 0})
  """
  name = "Abs Sum Agg"
  push = 'this.keyAgg += Math.abs(parseFloat(record[attributeArray[0]]))'


class JsPivotMaxAgg(JsPivotSumAgg):
  """
  Description:
  -----------
  Aggregator in charge of retrieving the maximum value in a recordset.
  This aggregator will retrieve the maximum value for the given rows and columns.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "Max Agg", 'digits': 0})
  """
  name = "Max Agg"
  keyAgg = '-Infinity'
  push = "this.keyAgg = Math.max(this.keyAgg, parseFloat(record[attributeArray[0]]))"
  value = 'return this.keyAgg'


class JsPivotMinAgg(JsPivotSumAgg):
  """
  Description:
  -----------
  Aggregator in charge of retrieving the minimum value in a recordset.
  This aggregator will retrieve the minimum value for the given rows and columns.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "Min Agg", 'digits': 0})
  """
  name = "Min Agg"
  keyAgg = 'Infinity'
  push = "this.keyAgg = Math.min(this.keyAgg, parseFloat(record[attributeArray[0]]))"
  value = 'return this.keyAgg'


class JsPivotAvgAgg(JsPivotSumAgg):
  """
  Description:
  -----------
  Aggregator in charge of computing the average value in a recordset.
  This aggregator will compute the average value for the given rows and columns.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "Avg Agg", 'digits': 0})
  """
  name = "Avg Agg"
  keyAgg = 0
  push = "this.keyAgg += parseFloat(record[attributeArray[0]]); this.tmpVal += 1"
  value = "return this.keyAgg / this.tmpVal"


# -------------------------------------------------------------------------------------------------------------------
#                           COMPLEX TRANSFORMATION USING TWO KEYS
#
class JsPivotDiff(JsPivotAggFnc):
  """
  Description:
  -----------
  Aggregator in charge of producing the difference.

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "diff Agg", 'digits': 0})
  """
  name = "diff Agg"
  keyAgg, key2Agg = 0, 0
  push = 'this.key1Agg += parseFloat(record[attributeArray[0]]); this.key2Agg += parseFloat(record[attributeArray[1]])'
  value = 'return this.key1Agg - this.key2Agg'
  format = 'return numberWithCommas(x.toFixed(2))'


class JsPivotDiffPct(JsPivotDiff):
  """
  Description:
  -----------


  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "diff Pct Agg", 'digits': 0})
  """
  name = "diff Pct Agg"
  value = 'return (this.key1Agg - this.key2Agg) / this.key1Agg'


class JsPivotDiffAbs(JsPivotDiff):
  """
  Description:
  -----------


  Usage::

      report.pivot(df, rows=['Date'], cols=['direction'],
        valCol=['AAPL.Low'], aggOptions={'name': "diff Abs Agg", 'digits': 0})
  """
  name = "diff Abs Agg"
  value = 'return Math.abs(this.key1Agg - this.key2Agg)'


class JsPivotDiffPctAbs(JsPivotDiff):
  """
  Description:
  -----------


  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'], valCol=['AAPL.Low'],
        aggOptions={'name': "diff Abs Pct Agg", 'digits': 0})
  """
  name = "diff Abs Pct Agg"
  value = 'return Math.abs((this.key1Agg - this.key2Agg) / this.key1Agg)'


class JsPivotSumOverSumAgg(JsPivotDiff):
  """
  Description:
  -----------

  Usage::

      page.pivot(df, rows=['Date'], cols=['direction'], valCol=['AAPL.Low'],
        aggOptions={'name': "sum Over Sum Agg", 'digits': 0})
  """
  name = "sum Over Sum Agg"
  push = "this.key1Agg += parseFloat(record[attributeArray[0]]); this.key2Agg += parseFloat(record[attributeArray[1]])"
  value = 'return this.key1Agg / this.key2Agg'
