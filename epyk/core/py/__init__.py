

class OrderedSet(list):
  def __init__(self):
    super(OrderedSet, self).__init__()

  def discard(self, value):
    """
    Description:
    ------------
    remove a specific class from the component class attributes.

    Attributes:
    ----------
    :param value: String. The class reference.
    """
    self.remove(value)

  def add(self, key):
    """
    Description:
    ------------
    Add a class to the component class attributes.

    Class needs to be defined, this will just add the reference to the component.
    Attributes:
    ----------
    :param key: String. The class name.
    """
    if key not in self:
      self.append(key)

  def initialise(self, classes):
    """
    Description:
    ------------
    Reset the classes for the component.
    Remove all the default ones.

    Attributes:
    ----------
    :param classes: List the classes to be added to the component class attribute
    """
    self.clear()
    for cls in classes:
      self.append(cls)
