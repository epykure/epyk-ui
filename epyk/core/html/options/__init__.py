
import sys

from epyk.core.data import DataClass


class Options(DataClass):

  def __init__(self, report, attrs=None, options=None):
    super(Options, self).__init__(report, attrs, options)
    if attrs is not None:
      for k, v in attrs.items():
        if hasattr(self, k):
          setattr(self, k, v)
        else:
          self._report._jsStyles[k] = v

  def _config_get(self, dflt=None, name=None):
    """
    Description:
    ------------
    Get the option attribute to be added on the Javascript side during the component build

    :param name: String. The attribute name
    """
    return self._report._jsStyles.get(name, dflt)

  def _config(self, value, name=None):
    """
    Description:
    ------------
    Set the option attribute to be added on the Javascript side during the component build

    :param value: Object. The value for the name
    :param name: String. The attribute name
    """
    self._report._jsStyles[sys._getframe().f_back.f_code.co_name] = value
