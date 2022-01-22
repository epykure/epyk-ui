
from typing import Union
from epyk.core.py import primitives

from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils


class JsAttributes(JsObject.JsObject):
  """

  Related Pages:

      https://www.w3schools.com/jsref/dom_obj_attributes.asp

  """

  @property
  def name(self):
    """
    Description:
    ------------
    The name property returns the name of the attribute.

    This property is read-only.

    Related Pages:

      https://www.w3schools.com/jsref/prop_attr_name.asp

    :return: A String, representing the name of the attribute.
    """
    return "name"

  @property
  def value(self):
    """
    Description:
    ------------
    The value property sets or returns the value of the attribute.

    Related Pages:

      https://www.w3schools.com/jsref/prop_attr_value.asp

    :return: Specifies the value of the attribute
    """
    return "value"

  @property
  def specified(self):
    """
    Description:
    ------------
    The specified property returns true if the attribute is specified.

    Related Pages:

      https://www.w3schools.com/jsref/prop_attr_specified.asp

    :return: A Boolean, returns true if the attribute is specified, otherwise false
    """
    return "specified"

  def item(self, i: Union[int, primitives.JsDataModel]):
    """
    Description:
    ------------
    The item() method returns the node at the specified index in a NamedNodeMap, as a Node object.

    Related Pages:

      https://www.w3schools.com/jsref/met_namednodemap_item.asp

    :param Union[int, primitives.JsDataModel] i: The index of the node in the NamedNodeMap you want to return

    :return: A Node object, representing the attribute node at the specified index.
    """
    return "item(%s)" % i

  def removeNamedItem(self, type: str):
    """
    Description:
    ------------
    The removeNamedItem() method removes the node with the specified name in a NamedNodeMap object.

    Related Pages:

      https://www.w3schools.com/jsref/met_namednodemap_removenameditem.asp

    :param str type: The name of the node in the namedNodeMap you want to remove.

    :return: 	A Node object, representing the removed attribute node
    """
    return "removeNamedItem(%s)" % type

  def setNamedItem(self, attrs: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The setNamedItem() method adds the specified node to the NamedNodeMap.

    If the node already exists, it will be replaced, and the replaced node will be the return value, otherwise
    the return value will be null.

    Related Pages:

      https://www.w3schools.com/jsref/met_namednodemap_setnameditem.asp

    :return: A Node object, representing the replaced node (if any), otherwise null.
    """
    attrs = JsUtils.jsConvertData(attrs, None)
    return "setNamedItem(%s)" % attrs

  def getNamedItem(self, node_name: Union[str, primitives.JsDataModel]):
    """
    Description:
    ------------
    The getNamedItem() method returns the attribute node with the specified name from a NamedNodeMap object.

    Related Pages:

      https://www.w3schools.com/jsref/met_namednodemap_getnameditem.asp

    :param node_name: The name of the node in the namedNodeMap you want to return.

    :return: A Node object, representing the attribute node with the specified name.
    """
    node_name = JsUtils.jsConvertData(node_name, None)
    return "getNamedItem(%s)" % node_name
