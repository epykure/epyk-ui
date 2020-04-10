from epyk.core.css.styles.classes import CssStyle


class CssWebkitScrollbar(CssStyle.Style):
  classname = "::-webkit-scrollbar"
  _attrs = {'width': '10px'}


class CssWebkitScrollbarTrack(CssStyle.Style):
  classname = "::-webkit-scrollbar-track"
  _attrs = {'border-radius': '10px'}

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[0]})


class CssWebkitScrollbarThumb(CssStyle.Style):
  classname = "::-webkit-scrollbar-thumb"
  _attrs = {'border-radius': '10px'}

  def customize(self):
    self.css({'background-color': self.rptObj.theme.colors[-2]})

