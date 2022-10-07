"""
Module dedicated to ensure the encoding between the two languages.

This will ensure a good data transfer between Python and Javascript.

This will rely on the standard json conversion but some extra checks are added in order to handle
some specific data structures in the Python languages.

For example Numpy and Pandas data structures (not correctly converted) are encoded thanks to this layer.
"""

import json
import datetime


class Encoder(json.JSONEncoder):
  """  Python to Js Encoding.

  Class in charge of encoding the data to be written on the Javascript side.
  In most of the function the simple json module is used but this module is there to encode more complex object
  frequently coming from Pandas.

  Usage::

    >>> json.dumps({"test": ""}, cls=Encoder, allow_nan=False)
    '{"test": ""}'

  :return: A serializable item.
  """
  def default(self, obj):
    try:
      import pandas

      if isinstance(obj, pandas.core.series.Series):
        return list(obj)

      elif isinstance(obj, datetime.datetime):
        if isinstance(obj, type(pandas.NaT)):
          return ''

        return obj.strftime('%Y-%m-%d')
    except ImportError: pass

    try:
      import numpy

      if isinstance(obj, (numpy.int_, numpy.intc, numpy.intp, numpy.int8, numpy.int16, numpy.int32, numpy.int64,
                          numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint64, numpy.integer)):
        return int(obj)

      elif isinstance(obj, (numpy.float_, numpy.float16, numpy.float32, numpy.float64, numpy.floating)):
        return float(obj)

      elif isinstance(obj, numpy.ndarray):
        return obj.tolist()

    except ImportError: pass

    return super(Encoder, self).default(obj)

