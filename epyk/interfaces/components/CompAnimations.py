
from epyk.core.css.styles.classes import CssStylesLoadings
from typing import Union, Optional
from epyk.core.js import JsUtils


class Animations:

  def __init__(self, ui):
    self.page = ui.page

  def loading_line(self, height: Union[str, int, tuple] = (3, "px"), profile: Optional[Union[dict, bool]] = None,
                   html_code: Optional[str] = None, options: Optional[dict] = None):
    """
    Description:
    -----------
    Add a loading line component.

    Related Pages:

      https://codepen.io/ziafatali/pen/mxVwpq

    Attributes:
    ----------
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.page.ui.div(html_code=html_code, height=height, options=options, profile=profile)
    component.style.css.background_color = "#ddd"
    component.style.css.margin = 0
    component.style.add_classes.custom(CssStylesLoadings.CssLoadingLine)

    def stop():
      """ Stop the loading animation """
      return component.dom.removeClass("cssloadingline").r

    def start():
      """ Start the loading animation """
      return component.dom.addClass("cssloadingline").r

    component.stop = stop
    component.start = start
    return component

  def progress_cursor(self):
    """
    Description:
    -----------

    Related Pages:


    :return:
    """
    cursor = self.page.body.style.css.cursor
    component = self.page.ui.div()

    def stop():
      return self.page.body.dom.css("cursor", cursor or "default").r

    def start():
      return self.page.body.dom.css("cursor", "progress").r

    component.stop = stop
    component.start = start
    return component
