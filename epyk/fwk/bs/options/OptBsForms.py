
from epyk.core.html.options import Options


class Check(Options):
  component_properties = ("container_class", )

  @property
  def disabled(self):
    """
    Description:
    -----------

    """
    return self._config_get()

  @disabled.setter
  def disabled(self, flag):
    self._config(flag)

  @property
  def container_class(self):
    """
    Description:
    -----------

    """
    return self._config_get(["form-check"])

  @container_class.setter
  def container_class(self, cls):
    self._config(cls)

  @property
  def switch(self):
    """
    Description:
    -----------

    """
    return self._config_get()

  @switch.setter
  def switch(self, flag):
    if flag:
      self.js_tree["container_class"].append("form-switch")
