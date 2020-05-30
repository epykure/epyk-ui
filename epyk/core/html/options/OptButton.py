
from epyk.core.html.options import Options


class OptionsButton(Options):

  @property
  def multiple(self):
    """
    Description:
    ------------
    Property to define if multiple buttons can be selected at the same time
    Default value is false
    """
    return self.get(False)

  @multiple.setter
  def multiple(self, bool):
    self.set(bool)

  @property
  def group(self):
    """
    Description:
    ------------
    Property to set the group name of a button
    """
    return self._report.attr.get('name')

  @group.setter
  def group(self, val):
    self._report.set_attrs(name='name', value=val)


class OptionsBadge(Options):

  @property
  def badge_css(self):
    """
    Description:
    ------------
    """
    return self.get()

  @badge_css.setter
  def badge_css(self, css):
    if hasattr(self, '_report') and hasattr(self._report, 'link'):
      self._report.link.css(css)
    cssOpts = self.get({})
    cssOpts.update(css)
    self.set(cssOpts)

  @property
  def badge_position(self):
    """
    Description:
    ------------

    :param position:
    """
    return self.get()

  @badge_position.setter
  def badge_position(self, position):
    if position == 'left':
      self.set({"position": 'relative'}, name='badge_css')
    else:
      self.set({"position": 'relative', "top": "-4px", "right": "11px"}, name='badge_css')
    self.set(position)
