

from epyk.core.html.options import Enums


class ExtsValidators(Enums):

  def custom(self, validator, moduleAlias):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/mutators

    Attributes:
    ----------
    :param validator:
    :param moduleAlias:
    """
    self.component.jsImports.add(moduleAlias)
    self._set_value(value=validator)
    return self
