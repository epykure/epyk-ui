"""

"""


class Effects(object):
  """

  """

  def __init__(self, ovrs_attrs=None):
    if ovrs_attrs is not None:
      self.attrs = dict(self.attrs)
      self.attrs.update(ovrs_attrs)

  def get_attrs(self):
    """ Return the effect CSS attributes """
    return self.attrs
