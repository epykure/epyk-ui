
from typing import Any


class OrderedSet(list):
  def __init__(self):
    super(OrderedSet, self).__init__()

  def discard(self, value: Any):
    """
    remove a specific class from the component class attributes.

    :param Any value: The class reference.
    """
    self.remove(value)

  def add(self, key: Any):
    """
    Add a class to the component class attributes.

    Class needs to be defined, this will just add the reference to the component.
    :param Any key: The class name.
    """
    if key not in self:
      self.append(key)

  def initialise(self, classes):
    """
    Reset the classes for the component.
    Remove all the default ones.

    :param classes: List the classes to be added to the component class attribute
    """
    self.clear()
    for cls in classes:
      self.append(cls)
