
from epyk.core.js.packages import packageImport
from epyk.core.data import DataGroup


class ExtsEditors(DataGroup):

  def text(self, cssMapping, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text

    Related Pages:
    --------------
    http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: use search type input element with clear button
    :param elementAttributes: set attributes directly on the input element
    """
    self._attrs["editor"] = 'input'
    self._attrs["editorParams"] = {'search': search}
    if elementAttributes is not None:
      self._attrs["editorParams"][elementAttributes] = elementAttributes
    if kwargs:
      self._attrs["editorParams"].update(kwargs)
    self._parent.mutators.text(cssMapping)
    return self

  def number(self, red=None, green=None, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text

    Related Pages:
    --------------
    http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: use search type input element with clear button
    :param elementAttributes: set attributes directly on the input element
    """
    self._attrs["editor"] = 'input'
    self._attrs["editorParams"] = {'search': search}
    if elementAttributes is not None:
      self._attrs["editorParams"][elementAttributes] = elementAttributes
    if kwargs:
      self._attrs["editorParams"].update(kwargs)
    self._parent.mutators.number(red, green)
    return self

  @packageImport('editors-inputs')
  def input(self):
    self._attrs["editor"] = 'inputPlus'
    return self

  @packageImport('editors-inputs')
  def input_excel(self):
    self._attrs["editor"] = 'inputExcel'
    return self

  @packageImport('editors-dates')
  def date(self):
    self._attrs["editor"] = 'datePlus'
    return self

  @packageImport('editors-dates')
  def date(self):
    self._attrs["editor"] = 'datePlus'
    return self

  @packageImport('editors-selects')
  def select(self):
    self._attrs["editor"] = 'datePlus'
    return self

  @packageImport('editors-selects')
  def select_rule(self):
    self._attrs["editor"] = 'selectConditiions'
    return self

  @packageImport('editors-selects')
  def select_multi_rules(self):
    self._attrs["editor"] = 'selectMultiConditions'
    return self

  def custom(self, formatter, formatterParams, moduleAlias):
    """

    :param formatter:
    :param formatterParams:
    :param moduleAlias:
    """
    self._report.jsImports.add(moduleAlias)
    self._attrs["editor"] = formatter
    self._attrs['editorParams'] = formatterParams
    return self
