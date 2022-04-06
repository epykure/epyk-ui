
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Enums


class ExtsMutators(Enums):

  @packageImport('tabulator-mutators-inputs')
  def number(self, green: str = None, red: str = None, threshold: int = 0, cssMapping: dict = None, **kwargs):
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
    mutator_params = cssMapping or {}
    mutator_params['red'] = red or self.component.page.theme.danger.base
    mutator_params['green'] = green or self.component.page.theme.success.base
    if kwargs:
      mutator_params.update(kwargs)
    self._set_value(value=mutator_params, name="mutatorParams")
    return self

  @packageImport('tabulator-mutators-inputs')
  def number_threshold(self, green: str = None, red: str = None, threshold: int = 0, css_mapping: dict = None, **kwargs):
    """
    Description:
    -----------

    # TODO: Add this mutator

    Attributes:
    ----------
    :param green:
    :param red:
    :param threshold:
    :param css_mapping:
    :param kwargs:
    """
    self._set_value(value="formatNumbers")
    if css_mapping is None:
      mutator_params = {True: {}, False: {}}
    else:
      mutator_params = css_mapping
    mutator_params['threshold'] = threshold
    mutator_params[False]['color'] = red or self.component.page.theme.danger.light
    mutator_params[True]['color'] = green or self.component.page.theme.success.light
    if kwargs:
      mutator_params.update(kwargs)
    self._set_value(value=mutator_params, name="mutatorParams")
    return self

  @packageImport('tabulator-mutators-inputs')
  def text(self, css_mapping: dict, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param css_mapping:
    :param kwargs:
    """
    self._set_value(value="formatStrings")
    mutator_params = {'cssMapping': css_mapping}
    if kwargs:
      mutator_params.update(kwargs)
    self._set_value(value=mutator_params, name="mutatorParams")
    return self

  def custom(self, mutator, mutator_params, module_alias):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/mutators

    Attributes:
    ----------
    :param mutator:
    :param mutator_params:
    :param module_alias:
    """
    self.component.jsImports.add(module_alias)
    self._set_value(value=mutator)
    self._set_value(value=mutator_params, name='mutatorParams')
    return self

