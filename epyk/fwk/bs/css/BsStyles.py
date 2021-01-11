

class BsStyles(object):

  def __init__(self, rptObj):
    self._report = rptObj

  def remove(self, style):
    """
    Description:
    -----------
    Remove a specific CSS class for all the components

    Attributes:
    ----------
    :param style: String the css style to be removed
    """
    self.replate(style, None)

  def replace(self, style, new_style):
    """
    Description:
    -----------
    Apply a style change on all the components

    Usage
    rptObj.styles.replace('btn', 'btn btn-custom')

    Attributes:
    ----------
    :param style: String the css style to be replaced
    :param new_style: String. The new CSS Style to be added (multiple should be a string with spaces)
    """
    for v in self._report.components.values():
      if style in v.attr['class']:
        if new_style is None:
          v.attr['class'].discard(style)
        else:
          index = v.attr['class'].index(style)
          v.attr['class'][index] = new_style

  def apply_calc(self, component, style_map):
    """
    Description:
    -----------
    Apply a style calc on a component and its hierarchy of underlying components

    Usage
    rptObj.styles.apply_calc(d, {'btn': 'toto'})

    Attributes:
    ----------
    :param component:
    :param style_map:
    """
    for s, t in style_map.items():
      if s in component.attr['class']:
        if t is None:
          component.attr['class'].discard(s)
        else:
          index = component.attr['class'].index(s)
          component.attr['class'][index] = t
