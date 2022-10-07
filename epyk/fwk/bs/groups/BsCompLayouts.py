
from epyk.core.py import types


class Components:
  def __init__(self, ui):
    self.page = ui.page

  def grid(self, rows: list = None, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
           align: str = None, position: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  
    Use our powerful mobile-first flexbox grid to build layouts of all shapes and sizes thanks to a twelve column
    system, six default responsive tiers, Sass variables and mixins, and dozens of predefined classes.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/grid/

    :param rows:
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param position: String. Optional. The position compared to the main component tag.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    grid = self.page.web.std.grid(rows, position, width, height, align, options, profile)
    grid.add_style(["container"], clear_first=True)
    return grid

  def row(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """  
    Add a row container.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/grid/#row-columns

    :param components: Array<Component>. A list of HTML components.
    :param position: String. Optional. The position compared to the main component tag.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    row = self.page.web.std.row(components, position, width, height, align, helper, options, profile)
    row.add_style(["row"], clear_first=True)
    return row

  def col(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """  
    Add a column container.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/columns/

    :param components: Array<Component>. A list of HTML components.
    :param position: String. Optional. The position compared to the main component tag.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. The text-align property within this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    col = self.page.web.std.col(components, position, width, height, align, helper, options, profile)
    return col

  def container(self, components=None, label=None, color=None, width=(100, "%"), icon=None,
                height=(None, "px"), editable=False, align='left', padding=None, html_code=None, helper=None,
                options=None, profile=None, position=None):
    """  
    Containers are a fundamental building block of Bootstrap that contain, pad, and align your content within a
    given device or viewport.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/containers/
      https://getbootstrap.com/docs/5.1/layout/grid/#sass

    :param components: Array<Component>. A list of HTML components.
    :param label: String. Optional. The text of label to be added to the component.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple | Number. Optional. A tuple with the integer for the component width and its unit.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param height: Tuple | Number. Optional. A tuple with the integer for the component height and its unit.
    :param editable: Boolean. Optional.
    :param align: String. The text-align property within this component.
    :param padding:
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param position: String. Optional. The position compared to the main component tag.
    """
    component = self.page.web.std.div(components, label, color, width, icon, height, editable, align, padding,
                                      html_code, 'div', helper, options, profile, position)
    component.add_style(["container"], clear_first=True)
    return component
