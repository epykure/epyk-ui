"""

"""

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsDate
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString


class loop(object):
  """
  Data Class used for all the loop and map in the Javascript side.
  This will get the below attributes

  val   : The current value in the loop
  index : The index item
  arr   : The full array (only available in case of arrays, map, filter, every  )
  """
  val, index, arr = JsObject.JsObject("value"), JsNumber.JsNumber("index", isPyData=False), JsArray.JsArray("arr")


class reduce(object):
  """

  rVal  :
  val   :
  index :
  """
  rVal, val, index = JsObject.JsObject("r"), JsNumber.JsNumber("o", isPyData=False), JsNumber.JsNumber("i", isPyData=False)


class sort(object):
  """

  """


class each(object):
  """
  Data Class for the Jquery each loop

  index : index
  data  : element
  """
  index, data = JsNumber.JsNumber("index", isPyData=False), JsObject.JsObject("data", isPyData=False)
