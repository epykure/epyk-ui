
from epyk.core.css.styles.classes import CssStyle


class CMEditor(CssStyle.Style):
  classname = "CodeMirror"

  def customize(self):
    self.css({'background-color': self.page.theme.greys[0], 'color': self.page.theme.greys[-1]})


class CMEditorGutters(CssStyle.Style):
  classname = "CodeMirror-gutter"

  def customize(self):
    self.css({'background-color': self.page.theme.colors[1], 'color': self.page.theme.colors[-1]})


class CMEditorActiveLine(CssStyle.Style):
  classname = "CodeMirror-activeline-background"

  def customize(self):
    self.css({'background-color': self.page.theme.colors[0]})


class Mjx(CssStyle.Style):
  classname = "mjx-container"
  is_class = False

  def customize(self):
    self.css({"padding-top": "10px", "padding-bottom": "10px", "margin": "0 !IMPORTANT"})


class MjxContainer(CssStyle.Style):
  classname = "MathJax:focus, .mjx-chtml:focus, .MathJax_SVG:focus"

  def customize(self):
    self.css({'outline': "1px solid %s" % self.page.theme.notch()})
