
from epyk.core.html import Defaults


class Component(object):

  def __init__(self, html):
    self._html = html
    self.name = html.__class__.__name__
    self.folder = self.name.lower()

  def rename(self, name):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    """
    self.name = name.capitalize()
    self.folder = self.name.lower()
    return self

  @property
  def tag(self):
    """

    """
    return "%s-%s" % (Defaults.COMP_PREFIX, self.folder)

  def ts(self, name=None):
    """
    Description:
    -----------
    Component export for an Angular app.
    This will allow to build apps directly from reports using each underlying components available in the framework.

    Attributes:
    ----------
    :param name: Optional. The component name. Can be set to define test components
    """
    if name is not None:
      self.rename(name)
    self._out_mode = "angular"
    html = self._html.html()
    return {'folder': self.folder, 'class': "Epyk%sComponent" % self.name, 'externalVars': '', 'css': self._html.attr['css'],
            'htmlTag': self.tag, 'build': self._html._js__builder__.strip(), 'html': html, 'options': self._html._jsStyles}