
from epyk.core.html.options import Options


class Slider(Options):

  @property
  def max(self):
    """
    Description:
    -----------

    Related Pages:

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

    Related Pages:

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

    Related Pages:

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
    Add the disabled attribute and the associated <label>s are automatically styled to match with a lighter color to
    help indicate the input’s state.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/#disabled-1
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
    Change the CSS class of the main container.
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
    Change the input style to a switch component.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/#switches
    """
    return self._config_get()

  @switch.setter
  def switch(self, flag):
    if flag:
      self.js_tree["container_class"].append("form-switch")

  @property
  def inline(self):
    """
    Description:
    -----------
    Group checkboxes or radios on the same horizontal row by adding .form-check-inline to any .form-check.

    Related Pages:

      https://getbootstrap.com/docs/5.1/forms/checks-radios/#inline

    """
    return "form-check-inline" in self.js_tree["container_class"]

  @inline.setter
  def inline(self, flag):
    if flag:
      self.js_tree["container_class"].append("form-check-inline")

