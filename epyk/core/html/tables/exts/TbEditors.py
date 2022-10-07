
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Enums


class ExtsEditors(Enums):

  def text(self, css_mapping: dict, search: bool = True, attrs: dict = None, **kwargs):
    """   The input editor allows entering of a single line of plain text.

    Usage::

      c = table.get_column("Language")
      c.exts.editors.text({"Python": {"background": "green"}, "Java": {"background": "red"}})

    :param css_mapping:
    :param search: Optional. use search type input element with clear button.
    :param attrs: Optional. set attributes directly on the input element.
    """
    attrs = attrs or {}
    attrs.update({'search': search})
    if kwargs:
      attrs.update(kwargs)
    self.item.exts.mutators.text(css_mapping)
    self._set_value(value=attrs, name="editorParams")
    return self._set_value(value="input")

  def number(self, red: str = None, green: str = None, search: bool = True, attrs: dict = None, **kwargs):
    """   The input editor allows entering of a single line of plain text

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    :param red: The color when condition is false.
    :param green: The color when condition is true.
    :param search: use search type input element with clear button
    :param attrs: set attributes directly on the input element
    """
    attrs = attrs or {}
    attrs.update({'search': search})
    if kwargs:
      attrs.update(kwargs)
    self.item.exts.mutators.number(red, green)
    self._set_value(value=attrs, name="editorParams")
    return self._set_value(value="input")

  @packageImport('editors-inputs')
  def input(self, empty_first: bool = True, refresh: bool = True, **kwargs):
    """   Add an input fields to the cell.

    Usage::

      c = table.get_column("Type")
      c.exts.editors.input(spellcheck=False)
    """
    props = {"emptyFirst": empty_first, refresh: refresh}
    if kwargs:
      props.update(kwargs)
    self._set_value(value=props, name="editorParams")
    return self._set_value(value="inputPlus")

  @packageImport('editors-inputs')
  def input_excel(self, empty_first: bool = True, refresh: bool = True, **kwargs):
    """

    Usage::

      c = table.get_column("Type")
      c.exts.editors.input_excel(empty_first=False, refresh=False, style={"background-color": "red"})
    """
    props = {"emptyFirst": empty_first, refresh: refresh}
    props.update(kwargs)
    self._set_value(value=props, name="editorParams")
    return self._set_value(value="inputExcel")

  @packageImport('editors-dates')
  def date(self):
    """   Add a date input selector.
    """
    return self._set_value(value="datePlus")

  @packageImport('editors-selects')
  def select(self, values: list):
    """   Add a select object to the cell.

    Usage::

      c = table.get_column("Type")
      c.exts.editors.select(["Script", "Code"])
    """
    self._set_value(value=values, name="editorParams")
    return self._set_value(value="selectPlus")

  @packageImport('editors-selects')
  def select_rule(self, key: str, values: dict, default: list = None):
    """   Display selection based on a value of another column in the table.

    Usage::

      c = table.get_column("Type")
      c.exts.editors.select_rule(key="Language", values={"Python": ["script", "code"]})
    """
    self._set_value(value={"key": key, "values": values, "default": default or []}, name="editorParams")
    return self._set_value(value="selectConditions")

  @packageImport('editors-selects')
  def select_multi_rules(self):
    """   """
    return self._set_value(value="selectMultiConditions")

  def custom(self, formatter: str, formatter_params: dict, module_alias):
    """

    :param formatter:
    :param formatter_params:
    :param module_alias:
    """
    self.component.jsImports.add(module_alias)
    self._set_value(value=formatter_params, name='editorParams')
    return self._set_value(value=formatter)
