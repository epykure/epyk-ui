"""
Wrapper to D3 package

https://d3js.org/
"""

import json

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsNumber


class D3ScaleLinear(object):
  """

  """
  def __init__(self, range):
    self.range = range

  def range(self):
    pass


class D3Select(object):
  """

  """

  def __init__(self, id=None, d3Type=None):
    if id is None and d3Type is None:
      raise Exception()

  def data(self, dataset):
    pass

  def filter(self, fnc):
    pass

  def enter(self):
    pass

  def append(self, htmlType):
    pass

  def insert(self, htmlType, id):
    pass

  def style(self, key, val):
    pass

  def attr(self, key, val):
    pass

  def call(self, fnc):
    pass

  def on(self, eventType, fnc):
    pass

  def remove(self):
    pass

  def select(self, id):
    return D3Select(id)

  def selectAll(self, d3Type):
    return D3Select(d3Type=d3Type)


class D3ForceSimulation(object):
  _package = ['d3-force']

  def __init__(self, id=None, d3Type=None):
    """

    Documentation:
      - https://github.com/d3/d3-force

    :param id:
    :param d3Type:
    """
    pass

  def force(self, forceType, fnc):
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


class D3ForceManyBody(object):
  def strength(self):
    pass

  def distanceMax(self, x):
    pass

  def distanceMin(self, x):
    pass


class D3ForceCollide(object):
  def __init__(self, radius=None):
    """
    Creates a new circle collision force with the specified radius. If radius is not specified, it defaults to the constant one for all nodes.

    Documentation:
        - https://github.com/d3/d3-force#forceCollide

    :param radius:
    :return:
    """
    pass

  def radius(self, fnc):
    """
    If radius is specified, sets the radius accessor to the specified number or function, re-evaluates the radius accessor for each node, and returns this force. If radius is not specified, returns the current radius accessor

    Documentation:
      - https://github.com/d3/d3-force#forceCollide

    :param fnc:
    :return:
    """
    pass

  def strength(self, strength):
    """
    If strength is specified, sets the force strength to the specified number in the range [0,1] and returns this force. If strength is not specified, returns the current strength which defaults to 0.

    Documentation:
      - https://github.com/d3/d3-force#forceCollide

    :param strength:
    :return:
    """
    pass

  def iterations(self, iterations):
    """
    If iterations is specified, sets the number of iterations per application to the specified number and returns this force

    Documentation:
      - https://github.com/d3/d3-force#forceCollide

    :param iterations:
    :return:
    """
    pass


class D3ForceCenter(object):
  def __init__(self):
    pass

  def x(self):
    pass

  def y(self):
    pass


class D3Event(object):
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


class D3Pack(object):
  def __init__(self):
    """

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    """

  def radius(self, number):
    pass

  def size(self, number):
    """
    If size is specified, sets this pack layout’s size to the specified two-element array of numbers [width, height] and returns this pack layout. If size is not specified, returns the current size, which defaults to [1, 1]

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param number:
    :return:
    """
    pass

  def padding(self, number):
    """
    If padding is specified, sets this pack layout’s padding accessor to the specified number or function and returns this pack layout. If padding is not specified, returns the current padding accessor, which defaults to the constant zero

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param number:
    :return:
    """
    pass

  def packSiblings(self, circles):
    """
    Packs the specified array of circles, each of which must have a circle.r property specifying the circle’s radius

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param circles:
    :return:
    """
    pass

  def packEnclose(self, circles):
    """
    Computes the smallest circle that encloses the specified array of circles, each of which must have a circle.r property specifying the circle’s radius, and circle.x and circle.y properties specifying the circle’s center

    Documentation:
      - https://github.com/d3/d3-hierarchy/blob/v1.1.8/README.md#pack

    :param circles:
    :return:
    """
    pass



class JsD3(object):
  class __internal(object):
    jqId, _context = '', {}

  def __init__(self, src=None):
    """

    Documentation:
      - https://github.com/d3/d3/blob/master/API.md

    :param src:
    """
    self.src = src if src is not None else self.__internal()
    self.src._context.setdefault("modules", set()).add('d3')
    self.selector = self.src.jqId
    self._js = []

  def min(self, dataset, jsFnc):
    return JsNumber.JsNumber("d3.min(%s, %s)" % (dataset, jsFnc))

  def min(self, dataset, jsFnc):
    return JsNumber.JsNumber("d3.max(%s, %s)" % (dataset, jsFnc))

  def select(self, id):
    return D3Select(id)

  def selectAll(self, d3Type):
    return D3Select(d3Type=d3Type)

  def scaleLinear(self, range):
    return D3ScaleLinear(range)

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
