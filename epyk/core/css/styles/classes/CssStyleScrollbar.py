from epyk.core.css.styles.classes import CssStyle


class CssWebkitScrollbar(CssStyle.Style):
  classname = "::-webkit-scrollbar"
  _attrs = {'width': '8px', 'height': '8px'}


class CssWebkitScrollbarTrack(CssStyle.Style):
  classname = "::-webkit-scrollbar-track"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[0]})


class CssWebkitScrollbarThumb(CssStyle.Style):
  classname = "::-webkit-scrollbar-thumb"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[2]})


class CssWebkitSelection(CssStyle.Style):
  classname = "::selection"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[1]})


class CssWebkitMozSelection(CssStyle.Style):
  classname = "::-moz-selection"

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[1]})
