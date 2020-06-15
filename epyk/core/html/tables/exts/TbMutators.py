
from epyk.core.js.packages import packageImport
from epyk.core.data.DataClass import DataGroup


class ExtsMutators(DataGroup):

  @packageImport('tabulator-mutators-inputs')
  def number(self, green=None, red=None, threshold=0, cssMapping=None, **kwargs):
    """
    Description:
    -----------

    :param green:
    :param red:
    :param css:
    :param kwargs:
    """
    self._attrs["mutator"] = 'formatNumbers'
    if cssMapping is None:
      self._attrs["mutatorParams"] = {True: {}, False: {}}
    else:
      self._attrs["mutatorParams"] = cssMapping
    self._attrs["mutatorParams"]['threshold'] = threshold
    self._attrs["mutatorParams"][False]['color'] = red or self._report.theme.danger[0]
    self._attrs["mutatorParams"][True]['color'] = green or self._report.theme.success[0]
    if kwargs:
      self._attrs["mutatorParams"].update(kwargs)
    return self

  @packageImport('tabulator-mutators-inputs')
  def text(self, cssMapping, **kwargs):
    """
    Description:
    -----------

    :param green:
    :param red:
    :param css:
    :param kwargs:
    """
    self._attrs["mutator"] = 'formatStrings'
    self._attrs["mutatorParams"] = {'cssMapping': cssMapping}
    if kwargs:
      self._attrs["mutatorParams"].update(kwargs)
    return self

  def custom(self, mutator, mutatorParams, moduleAlias):
    """
    Description:
    -----------

    http://tabulator.info/docs/4.0/mutators

    :param mutator:
    :param mutatorParams:
    :param moduleAlias:
    """
    self._report.jsImports.add(moduleAlias)
    self._attrs["mutator"] = mutator
    self._attrs['mutatorParams'] = mutatorParams
    return self

