
from epyk.core.py import types
from epyk.interfaces import Arguments


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def icon(self, icon: str = None, width: types.SIZE_TYPE = (None, 'px'),
           html_code: str = None, height: types.SIZE_TYPE = (None, "px"), color: str = None,
           tooltip: str = None, align: str = "left", options: dict = None,
           profile: types.PROFILE_TYPE = None):
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    family = 'material-design-icons'
    return self.page.ui.icon(icon=icon, width=width, family=family, html_code=html_code, height=height, color=color,
                             tooltip=tooltip, align=align, options=options, profile=profile)

  def refresh(self, text=None, position=None, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'),
              html_code=None, options=None, profile=None, align: str = "left", size=(None, 'px')):
    return self.icon("refresh")
