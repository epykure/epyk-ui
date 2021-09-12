

class Components:
  def __init__(self, ui):
    self.page = ui.page

  def grid(self, rows=None, width=(100, '%'), height=(None, 'px'), align=None, position=None, options=None,
           profile=None):
    """
    Description:
    ------------
    Use our powerful mobile-first flexbox grid to build layouts of all shapes and sizes thanks to a twelve column
    system, six default responsive tiers, Sass variables and mixins, and dozens of predefined classes.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/grid/

    Attributes:
    ----------
    :param rows:
    :param width:
    :param height:
    :param align:
    :param position:
    :param options:
    :param profile:
    """
    grid = self.page.web.std.grid(rows, position, width, height, align, options, profile)
    grid.attr["class"].initialise(["container"])
    return grid

  def row(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/grid/#row-columns

    Attributes:
    ----------
    :param components:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    row = self.page.web.std.row(components, position, width, height, align, helper, options, profile)
    row.attr["class"].initialise(["row"])
    return row

  def col(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          options=None, profile=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/columns/

    Attributes:
    ----------
    :param components:
    :param position:
    :param width:
    :param height:
    :param align:
    :param helper:
    :param options:
    :param profile:
    """
    col = self.page.web.std.col(components, position, width, height, align, helper, options, profile)
    return col

  def container(self, components=None, label=None, color=None, width=(100, "%"), icon=None,
                height=(None, "px"), editable=False, align='left', padding=None, html_code=None, helper=None,
                options=None, profile=None, position=None):
    """
    Description:
    ------------
    Containers are a fundamental building block of Bootstrap that contain, pad, and align your content within a
    given device or viewport.

    Related Pages:

      https://getbootstrap.com/docs/5.1/layout/containers/
      https://getbootstrap.com/docs/5.1/layout/grid/#sass

    Attributes:
    ----------
    :param components:
    :param label:
    :param color:
    :param width:
    :param icon:
    :param height:
    :param editable:
    :param align:
    :param padding:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    :param position:
    """
    component = self.page.web.std.div(components, label, color, width, icon, height, editable, align, padding,
                                      html_code, 'div', helper, options, profile, position)
    component.attr["class"].initialise(["container"])
    return component

  def inline(self, components=None, width=(None, "%"), height=(None, "px"), align='left', html_code=None, options=None,
             profile=None):
    pass

  def centered(self, components=None, width=("auto", ""), height=(None, "px"), align='left', html_code=None,
               options=None, profile=None):
    pass

  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    pass
