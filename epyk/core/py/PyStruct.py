

class OrderedSet(list):
  def __init__(self):
    super(OrderedSet, self).__init__()

  def add(self, key):
    if key not in self:
      self.append(key)
