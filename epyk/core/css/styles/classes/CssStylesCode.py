
from epyk.core.css.styles.classes import CssStyle


class CMEditor(CssStyle.Style):
  classname = "CodeMirror"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.greys[0], 'color': self.rptObj.theme.greys[-1]})


class CMEditorGutters(CssStyle.Style):
  classname = "CodeMirror-gutter"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[1], 'color': self.rptObj.theme.colors[-1]})


class CMEditorActiveLine(CssStyle.Style):
  classname = "CodeMirror-activeline-background"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[0]})
