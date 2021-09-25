

class Components:

  def __init__(self, ui):
    self.page = ui.page

  def icon(self, icon=None, width=(None, 'px'), html_code=None, height=(None, "px"), color=None,
           tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------
    Add a Bootstrap icon to the page.

    Usage::

      page.web.bs.icon("bi-x-square-fill")

    Related Pages:

      https://icons.getbootstrap.com/#install

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.web.std.icon(
      icon, 'bootstrap-icons', width, html_code, height, color, tooltip, align, options, profile)
    component.add_style(["bi", icon], clear_first=True)
    return component

  def close(self, width=(None, 'px'), html_code=None, height=(None, "px"), color=None, tooltip=None, align="left",
            options=None, profile=None):
    """
    Description:
    ------------
    Add a Bootstrap close icon to the page.

    Usage::

      page.web.bs.icons.close()

    Related Pages:

      https://icons.getbootstrap.com

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.icon("bi-x", width, html_code, height, color, tooltip, align, options, profile)

  def edit(self, width=(None, 'px'), html_code=None, height=(None, "px"), color=None, tooltip=None, align="left",
           options=None, profile=None):
    """
    Description:
    ------------
    Add a Bootstrap edit icon to the page.

    Usage::

      e = page.web.bs.icons.edit()
      e.style.css.color = "red"

    Related Pages:

      https://icons.getbootstrap.com

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.icon("bi-pencil-fill", width, html_code, height, color, tooltip, align, options, profile)

  def clock(self, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None,
            profile=None):
    return self.icon("bi-clock", width, html_code, height, tooltip, options, profile)

  def next(self, tooltip="", width=(None, 'px'), height=(None, 'px'),
           html_code=None, options=None, profile=None):
    return self.icon("bi-caret-right-fill", width, html_code, height, tooltip, options, profile)

  def previous(self, tooltip="", width=(None, 'px'), height=(None, 'px'),
               html_code=None, options=None, profile=None):
    return self.icon("bi-caret-left-fill", width, html_code, height, tooltip, options, profile)

  def play(self, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None, profile=None):
    return self.icon("bi-play-circle-fill", width, html_code, height, tooltip, options, profile)

  def stop(self, tooltip="", width=(None, 'px'), height=(None, 'px'),
           html_code=None, options=None, profile=None):
    return self.icon("bi-stop-fill", width, html_code, height, tooltip, options, profile)

  def warning(self, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None, profile=None):
    return self.icon("bi-exclamation-octagon-fill", width, html_code, height, tooltip, options, profile)

  def error(self, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None, profile=None):
    return self.icon("bi-exclamation-triangle-fill", width, html_code, height, tooltip, options, profile)

  def info(self, tooltip="", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None, profile=None):
    return self.icon("bi-info-circle", width, html_code, height, tooltip, options, profile)

  def refresh(self, tooltip="Refresh Component", width=(None, 'px'), height=(None, 'px'), html_code=None, options=None,
              profile=None):
    return self.icon("bi-arrow-clockwise", width, html_code, height, tooltip, options, profile)
