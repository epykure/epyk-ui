
from epyk.core.data import DataClass


class OptionsText(DataClass):

  @property
  def reset(self):
    """
    Description:
    ------------

    """
    return self._attrs.get('reset', False)

  @reset.setter
  def reset(self, bool):
    self.src._jsStyles["reset"] = bool
    return self.set(bool)

  @property
  def markdown(self):
    """
    Description:
    ------------

    """
    return self._attrs.get('markdown', False)

  @markdown.setter
  def markdown(self, bool):
    self.src._jsStyles["markdown"] = bool
    return self.set(bool)

  @property
  def limit_char(self):
    """
    Description:
    ------------

    """
    return self._attrs.get('limit_char')

  @limit_char.setter
  def limit_char(self, value):
    self.src._jsStyles["maxlength"] = value
    return self.set(value)


class OptionsTitle(OptionsText):

  @property
  def content_table(self):
    """
    Description:
    ------------

    """
    return self._attrs.get('content_table', True)

  @content_table.setter
  def content_table(self, bool):
    return self.set(bool)
