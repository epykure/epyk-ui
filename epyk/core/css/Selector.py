

class Selector(object):

  def __init__(self, component=None):
    self._js = []
    if component is not None:
      self._js.append("#%s" % component.htmlCode)

  def with_attribute(self, name, value=None, startswith=False, containing=False, endswith=False):
    """
    Description:
    -----------
    Specify HTML attributes to select

    Related Pages:

      https://www.w3schools.com/cssref/sel_attribute_value.asp

    Attributes:
    ----------
    :param name: String. The attribute name
    :param value: String. The attribute value
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

  def with_next_element(self, element):
    """
    Description:
    -----------
    The element>element selector is used to select elements with a specific parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_gt.asp

    Attributes:
    ----------
    :param element: String. The HTML type (tag)
    """
    self._js.append(" + %s" % element)
    return self

  def with_child_element(self, element):
    """
    Description:
    -----------
    The element>element selector is used to select elements with a specific parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_gt.asp

    Attributes:
    ----------
    :param element: String. The HTML type (tag)
    """
    self._js.append(" > %s" % element)
    return self

  def elements(self, tags):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param tags: List. The HTML types (tags)
    """
    self._js.append(" %s" % ",".join(tags))
    return self

  def state(self, value):
    """
    Description:
    -----------
    Selects a specific status for the item

    usage:

        self.state("disabled")

    Related Pages:

      https://www.w3schools.com/cssref/css_selectors.asp

    Attributes:
    ----------
    :params value: String. The state value
    """
    self._js.append(":%s" % value)
    return self

  def focus(self):
    """
    Description:
    -----------
    Selects the input element which has focus

    Related Pages:

      https://www.w3schools.com/cssref/sel_focus.asp
    """
    self._js.append(":focus")
    return self

  def hover(self):
    """
    Description:
    -----------
    Selects links on mouse over

    Related Pages:

      https://www.w3schools.com/cssref/sel_hover.asp
    """
    self._js.append(":hover")
    return self

  def element(self, tag):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param tag: String. The HTML tag
    """
    self._js.append(" %s" % tag)
    return self

  def with_htmlcode(self, htmlCode):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param htmlCode:
    """
    self._js.append("#%s" % htmlCode)
    return self

  def with_class(self, class_name):
    """
    Description:
    -----------
    Specify the class to use as a filter

    https://www.w3schools.com/cssref/css_selectors.asp

    Attributes:
    ----------
    :param class_name: String. The CSS Class name
    """
    self._js.append(".%s" % class_name)
    return self

  def excluding(self, selector):
    """
    Description:
    -----------
    Specify the element to exclude from the selection

    https://www.w3schools.com/cssref/css_selectors.asp

    Attributes:
    ----------
    :param selector: String or Selector. The id to exclude
    """
    if hasattr(selector, 'htmlCode'):
      selector = "[id='%s']" % selector.htmlCode
    self._js.append(":not(%s)" % selector)
    return self

  def first_child(self):
    """
    Description:
    -----------
    Selects every <> element that is the first child of its parent
    """
    self._js.append(":first-child")
    return self

  def last_child(self):
    """
    Description:
    -----------
    Selects every <> element that is the last child of its parent
    """
    self._js.append(":last-child")
    return self

  def first_letter(self):
    """
    Description:
    -----------
    Selects the first letter of every <> element
    """
    self._js.append("::first-letter")
    return self

  def first_of_type(self, type):
    """
    Description:
    -----------
    Selects every <> element that is the first <> element of its parent

    Attributes:
    ----------
    :param type: String. The HTML type (tag)
    """
    self._js.append("%s:first-of-type" % type)
    return self

  def last_of_type(self, type):
    """
    Description:
    -----------
    Selects every <> element that is the last <> element of its parent

    Attributes:
    ----------
    :param type: String. The HTML type (tag)
    """
    self._js.append("%s:last-of-type" % type)
    return self

  def nth_child(self, i):
    """
    Description:
    -----------
    Selects every <> element that is the second child of its parent

    Attributes:
    ----------
    :param i: Integer. The index (starting from 1)
    """
    self._js.append(":nth-child(%s)" % i)
    return self

  def nth_last_child(self, i):
    """
    Description:
    -----------
    Selects every <> element that is the second child of its parent, counting from the last child

    Attributes:
    ----------
    :param i: Integer. The index (starting from 1)
    """
    self._js.append(":nth-last-child(%s)" % i)
    return self

  def nth_last_of_type(self, type, i):
    """
    Description:
    -----------
    Selects every <p> element that is the second <> element of its parent, counting from the last child

    Attributes:
    ----------
    :param type: String. The HTML type (tag)
    :param i:  Integer. The index (starting from 1)
    """
    self._js.append("%s:nth-last-of-type(%s)" % (type, i))
    return self

  def nth_of_type(self, type, i):
    """
    Description:
    -----------
    Selects every <p> element that is the only <> element of its parent

    Attributes:
    ----------
    :param type: String. The HTML type (tag)
    :param i:  Integer. The index (starting from 1)
    """
    self._js.append("%s:nth-of-type(%s)" % (type, i))
    return self

  def only_of_type(self, type):
    """
    Description:
    -----------
    The :only-of-type selector matches every element that is the only child of its type, of its parent.

    Attributes:
    ----------
    :param type: String. The HTML type (tag)
    """
    self._js.append("%s:only-of-type" % type)
    return self

  def only_child(self):
    """
    Description:
    -----------
    The :only-child selector matches every element that is the only child of its parent.
    """
    self._js.append(":only-child")
    return self

  def toStr(self):
    from epyk.core.js import JsUtils

    return JsUtils.jsConvertData("".join(self._js), None)

  def __str__(self):
    return str(self.toStr())
