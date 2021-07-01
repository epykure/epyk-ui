
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Enums


class ExtsEditors(Enums):

  def text(self, cssMapping, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: Boolean. Optional. use search type input element with clear button.
    :param elementAttributes: Dictionary. Optional. set attributes directly on the input element.
    """
    elementAttributes = elementAttributes or {}
    elementAttributes.update({'search': search})
    if kwargs:
      elementAttributes.update(kwargs)
    self.item.text(cssMapping)
    self._set_value(value=elementAttributes, name="editorParams")
    return self._set_value()

  def number(self, red=None, green=None, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: use search type input element with clear button
    :param elementAttributes: set attributes directly on the input element
    """
    elementAttributes = elementAttributes or {}
    elementAttributes.update({'search': search})
    if kwargs:
      elementAttributes.update(kwargs)
    self.item.mutators.number(red, green)
    self._set_value(value=elementAttributes, name="editorParams")
    return self._set_value(value="input")

  @packageImport('editors-inputs')
  def input(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="inputPlus")

  @packageImport('editors-inputs')
  def input_excel(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="inputExcel")

  @packageImport('editors-dates')
  def date(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="datePlus")

  @packageImport('editors-selects')
  def select(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="datePlus")

  @packageImport('editors-selects')
  def select_rule(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="selectConditiions")

  @packageImport('editors-selects')
  def select_multi_rules(self):
    """
    Description:
    -----------
    """
    return self._set_value(value="selectMultiConditions")

  def custom(self, formatter, formatterParams, moduleAlias):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param formatter:
    :param formatterParams:
    :param moduleAlias:
    """
    self.component.jsImports.add(moduleAlias)
    self._set_value(value=formatterParams, name='editorParams')
    return self._set_value(value=formatter)
