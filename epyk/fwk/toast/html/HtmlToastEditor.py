
from epyk.core.html import Html
from epyk.fwk.toast.options import OptToastEditor
from epyk.fwk.toast.js import JsToastEditor


class Editor(Html.Html):
  name = 'ToastEditor'
  requirements = ('@toast-ui/editor', )
  _option_cls = OptToastEditor.OptionsEditor

  def __init__(self, page, width, height, html_code, options, profile):
    self.height = height[0]
    super(Editor, self).__init__(
      page, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.options.height = height[0]

  @property
  def var(self):
    """   Return the editor javaScript object reference after the builder.
    """
    return "window['%s']" % self.htmlCode

  @property
  def options(self) -> OptToastEditor.OptionsEditor:
    """   The Toast UI Editor options.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorCore

    :rtype: OptToastEditor.OptionsEditor
    """
    return super().options

  @property
  def js(self) -> JsToastEditor.Editor:
    """   Javascript module of the items in the menu.

    Related Pages:

      https://nhn.github.io/tui.editor/latest/ToastUIEditorViewer

    :rtype: JsToastEditor.Editor
    """
    if self._js is None:
      self._js = JsToastEditor.Editor(component=self, js_code=self.var, page=self.page)
    return self._js

  _js__builder__ = '''options.el = htmlObj; window[htmlObj.id] = new toastui.Editor(options)'''

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
