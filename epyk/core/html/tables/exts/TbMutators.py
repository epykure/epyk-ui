
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Enums


class ExtsMutators(Enums):

  @packageImport('tabulator-mutators-inputs')
  def number(self, green=None, red=None, threshold=0, cssMapping=None, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param green:
    :param red:
    :param threshold:
    :param cssMapping:
    :param kwargs:
    """
    self._set_value(value="formatNumbers")
    if cssMapping is None:
      mutatorParams = {True: {}, False: {}}
    else:
      mutatorParams = cssMapping
    mutatorParams['threshold'] = threshold
    mutatorParams[False]['color'] = red or self.component.page.theme.danger.light
    mutatorParams[True]['color'] = green or self.component.page.theme.success.light
    if kwargs:
      mutatorParams.update(kwargs)
    self._set_value(value=mutatorParams, name="mutatorParams")
    return self

  @packageImport('tabulator-mutators-inputs')
  def text(self, cssMapping, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param cssMapping:
    :param kwargs:
    """
    self._set_value(value="formatStrings")
    mutatorParams = {'cssMapping': cssMapping}
    if kwargs:
      mutatorParams.update(kwargs)
    self._set_value(value=mutatorParams, name="mutatorParams")
    return self

  def custom(self, mutator, mutatorParams, moduleAlias):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/mutators

    Attributes:
    ----------
    :param mutator:
    :param mutatorParams:
    :param moduleAlias:
    """
    self.component.jsImports.add(moduleAlias)
    self._set_value(value=mutator)
    self._set_value(value=mutatorParams, name='mutatorParams')
    return self

