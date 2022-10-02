
from typing import Union
from epyk.core.py import primitives


class Selector:

  def __init__(self, component: primitives.HtmlModel = None):
    self._js = []
    if component is not None:
      self._js.append("#%s" % component.htmlCode)

  def with_attribute(self, name: str, value: str = None, startswith: bool = False, containing: bool = False,
                     endswith: bool = False):
    """	Specify HTML attributes to select.

    Related Pages:

      https://www.w3schools.com/cssref/sel_attribute_value.asp

    :param str name: The attribute name.
    :param str value: Optional. The attribute value.
    :param bool startswith: Optional.
    :param bool containing: Optional.
    :param bool endswith: Optional.
    """
    if value is None:
      self._js.append("[%s]" % name)
    elif startswith:
      self._js.append("[%s|=%s]" % (name, value))
    elif containing:
      self._js.append("[%s~=%s]" % (name, value))
    elif endswith:
      self._js.append("[%s$=%s]" % (name, value))
    else:
      self._js.append("[%s=%s]" % (name, value))
    return self

  def with_next_element(self, element: str):
    """	The element>element selector is used to select elements with a specific parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_gt.asp

    :param str element: The HTML type (tag).
    """
    self._js.append(" + %s" % element)
    return self

  def with_child_element(self, element: str):
    """	The element>element selector is used to select elements with a specific parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_gt.asp

    :param str element: The HTML type (tag).
    """
    self._js.append(" > %s" % element)
    return self

  def elements(self, tags: list):
    """
    :param list tags: The HTML types (tags).
    """
    self._js.append(" %s" % ",".join(tags))
    return self

  def state(self, value: str):
    """	Selects a specific status for the item.

    Usage::

        self.state("disabled")

    Related Pages:

      https://www.w3schools.com/cssref/css_selectors.asp

    :params str value: The state value.
    """
    self._js.append(":%s" % value)
    return self

  def focus(self):
    """	Selects the input element which has focus.

    Usage::

    Related Pages:

      https://www.w3schools.com/cssref/sel_focus.asp
    """
    self._js.append(":focus")
    return self

  def hover(self):
    """	Selects links on mouse over.

    Related Pages:

      https://www.w3schools.com/cssref/sel_hover.asp
    """
    self._js.append(":hover")
    return self

  def element(self, tag: str):
    """

    :param str tag: The HTML tag.
    """
    self._js.append(" %s" % tag)
    return self

  def with_htmlcode(self, html_code: str):
    """	Add the component HTML reference to the CSS Class definition.

    :param str html_code: Optional. An identifier for this component (on both Python and Javascript side).
    """
    self._js.append("#%s" % html_code)
    return self

  def with_class(self, class_name: str):
    """	Specify the class to use as a filter.

    Related Pages:

      https://www.w3schools.com/cssref/css_selectors.asp

    :param str class_name: The CSS Class name.
    """
    self._js.append(".%s" % class_name)
    return self

  def excluding(self, selector: Union[str, primitives.HtmlModel]):
    """	Specify the element to exclude from the selection.

    Related Pages:

      https://www.w3schools.com/cssref/css_selectors.asp

    :param Union[str, primitives.HtmlModel] selector: The id to exclude.
    """
    if hasattr(selector, 'htmlCode'):
      selector = "[id='%s']" % selector.htmlCode
    self._js.append(":not(%s)" % selector)
    return self

  def first_child(self):
    """	Selects every <> element that is the first child of its parent.
    """
    self._js.append(":first-child")
    return self

  def last_child(self):
    """	Selects every <> element that is the last child of its parent.
    """
    self._js.append(":last-child")
    return self

  def first_letter(self):
    """	Selects the first letter of every <> element.
    """
    self._js.append("::first-letter")
    return self

  def first_of_type(self, item_type: str):
    """	Selects every <> element that is the first <> element of its parent.

    :param str item_type: The HTML type (tag).
    """
    self._js.append("%s:first-of-type" % item_type)
    return self

  def last_of_type(self, item_type: str):
    """	Selects every <> element that is the last <> element of its parent.

    :param str item_type: The HTML type (tag).
    """
    self._js.append("%s:last-of-type" % item_type)
    return self

  def nth_child(self, i: int):
    """	Selects every <> element that is the second child of its parent.

    :param int i: The index (starting from 1).
    """
    self._js.append(":nth-child(%s)" % i)
    return self

  def nth_last_child(self, i: int):
    """	Selects every <> element that is the second child of its parent, counting from the last child.

    :param int i: The index (starting from 1).
    """
    self._js.append(":nth-last-child(%s)" % i)
    return self

  def nth_last_of_type(self, item_type: str, i: int):
    """	Selects every <p> element that is the second <> element of its parent, counting from the last child.

    :param str item_type: The HTML type (tag).
    :param int i: The index (starting from 1).
    """
    self._js.append("%s:nth-last-of-type(%s)" % (item_type, i))
    return self

  def nth_of_type(self, item_type: str, i: int):
    """	Selects every <p> element that is the only <> element of its parent.

    :param str item_type: The HTML type (tag).
    :param int i: The index (starting from 1).
    """
    self._js.append("%s:nth-of-type(%s)" % (item_type, i))
    return self

  def only_of_type(self, item_type: str):
    """	The :only-of-type selector matches every element that is the only child of its type, of its parent.

    :param str item_type: The HTML type (tag).
    """
    self._js.append("%s:only-of-type" % item_type)
    return self

  def only_child(self):
    """	The :only-child selector matches every element that is the only child of its parent.

    Usage::

    """
    self._js.append(":only-child")
    return self

  def toStr(self):
    from epyk.core.js import JsUtils

    return JsUtils.jsConvertData("".join(self._js), None)

  def __str__(self):
    return str(self.toStr())
