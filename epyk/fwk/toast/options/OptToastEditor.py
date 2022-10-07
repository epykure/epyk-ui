
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumStyleOptions(Enums):

  def vertical(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example02-editor-with-horizontal-preview
    """
    self._set_value()

  def tab(self):
    """
    Set type of curve interpolation.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example02-editor-with-horizontal-preview
    """
    self._set_value()


class OptionsEditor(Options):
  component_properties = ("initialEditType", )

  @property
  def height(self):
    """
    Editor's height style value. Height is applied as border-box ex) '300px', '100%', 'auto'.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorCore
    """
    return self._config_get("500px")

  @height.setter
  def height(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    self._config(val)

  @property
  def initialValue(self):
    """
    Initial editor type (markdown, wysiwyg).

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example02-editor-with-horizontal-preview
    """
    return self._config_get("")

  @initialValue.setter
  def initialValue(self, val):
    self._config(val)

  @property
  def language(self):
    """
    language.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example16-i18n
    """
    return self._config_get("en-US")

  @language.setter
  def language(self, val: str):
    self._config(val)

  @property
  def placeholder(self):
    """
    The placeholder text of the editable element.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example17-placeholder
    """
    return self._config_get()

  @placeholder.setter
  def placeholder(self, val):
    self._config(val)

  @property
  def theme(self):
    """
    The theme to style the editor with. The default is included in toastui-editor.css.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/tutorial-example06-dark-theme
    """
    return self._config_get()

  @theme.setter
  def theme(self, val):
    self._config(val)

  @property
  def viewer(self):
    """
    """
    return self._config_get(None)

  @viewer.setter
  def viewer(self, flag: bool):
    self._config(flag)

  @property
  def initialEditType(self):
    """
    Initial editor type (markdown, wysiwyg).

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorCore
    """
    return self._config_get("markdown")

  @initialEditType.setter
  def initialEditType(self, val: str):
    self._config(val)

  @property
  def previewStyle(self):
    """
    Markdown editor's preview style (tab, vertical).

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorCore
    """
    return self._config_get("vertical")

  @previewStyle.setter
  def previewStyle(self, val: str):
    self._config(val)

  @property
  def previewStyles(self) -> EnumStyleOptions:
    """
    Highlight a preview element corresponds to the cursor position in the markdown editor.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorCore
    """
    return EnumStyleOptions(self, "previewStyle")
