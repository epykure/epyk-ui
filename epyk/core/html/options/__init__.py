

from epyk.core.data import DataClass


class Options(DataClass):

  def __init__(self, report, attrs=None, options=None):
    super(Options, self).__init__(report, attrs, options)
    if attrs is not None:
      self._report._jsStyles.update(attrs)
