
from epyk.core.py import primitives


class BsStyles:

  def __init__(self, page):
    self.page = page

  def remove(self, style: str):
    """   Remove a specific CSS class for all the components.
 
    :param style: String the css style to be removed
    """
    self.replate(style, None)
    return self

  def replace(self, style: str, new_style: str):
    """   Apply a style change on all the components.

    Usage::

      page.styles.replace('btn', 'btn btn-custom')
 
    :param style: String the css style to be replaced
    :param new_style: String. The new CSS Style to be added (multiple should be a string with spaces)
    """
    for v in self.page.components.values():
      if style in v.attr['class']:
        if new_style is None:
          v.attr['class'].discard(style)
        else:
          index = v.attr['class'].index(style)
          v.attr['class'][index] = new_style
    return self

  def apply_calc(self, component: primitives.HtmlModel, style_map: dict):
    """   Apply a style calc on a component and its hierarchy of underlying components

    Usage::

      page.styles.apply_calc(d, {'btn': 'toto'})
 
    :param component: The HTML component
    :param style_map: The CSS style map definition
    """
    for s, t in style_map.items():
      if s in component.attr['class']:
        if t is None:
          component.attr['class'].discard(s)
        else:
          index = component.attr['class'].index(s)
          component.attr['class'][index] = t
    return self
