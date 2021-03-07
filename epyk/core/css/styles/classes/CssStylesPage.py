
from epyk.core.css.styles.classes import CssStyle


class CssPageContentEditable(CssStyle.Style):
  classname = "[contenteditable]:focus"

  def customize(self):
    self.css({'outline': '1px solid %s' % self.page.theme.success[1]})
