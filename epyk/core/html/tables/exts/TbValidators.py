

from epyk.core.js.packages import packageImport
from epyk.core.data import DataGroup


class ExtsValidators(DataGroup):

  def custom(self, validator, moduleAlias):
    """
    Description:
    -----------

    http://tabulator.info/docs/4.0/mutators

    :param validator:
    :param moduleAlias:
    """
    self._report.jsImports.add(moduleAlias)
    self._attrs["validator"] = validator
    return self
