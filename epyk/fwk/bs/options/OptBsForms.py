
from epyk.core.html.options import Options


class Slider(Options):

  @property
  def max(self):
    """
    Description:
    -----------

    https://getbootstrap.com/docs/5.0/forms/range/
    """
    return self.component.attr.get("max")

  @max.setter
  def max(self, num):
    self.component.attr["max"] = num

  @property
  def min(self):
    """
    Description:
    -----------

    https://getbootstrap.com/docs/5.0/forms/range/
    """
    return self.component.attr.get("min")

  @min.setter
  def min(self, num):
    self.component.attr["min"] = num

  @property
  def step(self):
    """
    Description:
    -----------

    https://getbootstrap.com/docs/5.0/forms/range/
    """
    return self.component.attr.get("step")

  @step.setter
  def step(self, num):
    self.component.attr["step"] = num


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

  @property
  def inline(self):
    """
    https://getbootstrap.com/docs/5.0/forms/checks-radios/

    """
    return "form-check-inline" in self.js_tree["container_class"]

  @inline.setter
  def inline(self, flag):
    if flag:
      self.js_tree["container_class"].append("form-check-inline")

