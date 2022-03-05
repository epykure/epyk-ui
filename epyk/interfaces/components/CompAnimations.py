
from epyk.core.css.styles.classes import CssStylesLoadings
from typing import Union, Optional


class Animations:

  def __init__(self, ui):
    self.page = ui.page

  def loading_line(self, height: Union[str, int, tuple] = (3, "px"), profile: Optional[Union[dict, bool]] = None,
                   html_code: Optional[str] = None, options: Optional[dict] = None):
    """
    https://codepen.io/ziafatali/pen/mxVwpq

    :return:
    """
    component = self.page.ui.div(html_code=html_code, height=height, options=options, profile=profile)
    component.style.css.background_color = "#ddd"
    component.style.css.margin = 0
    component.style.add_classes.custom(CssStylesLoadings.CssLoadingLine)

    def stop():
      return component.dom.removeClass("cssloadingline").r

    def start():
      return component.dom.addClass("cssloadingline").r

    component.stop = stop
    component.start = start
    return component
