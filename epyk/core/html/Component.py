#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    Change the name of the file in the destination framework.

    Usage::

    Attributes:
    ----------
    :param name: String. The name of the file.
    """
    self.name = name.capitalize()
    self.folder = self.name.lower()
    return self

  @property
  def tag(self):
    """
    Description:
    -----------
    Create a tag for the HTML component. This will be used by some JavaScript framework like Angular.

    Usage::

    """
    return "%s-%s" % (Defaults.COMP_PREFIX, self.folder)

  def ts(self, name=None):
    """
    Description:
    -----------
    Component export for an Angular app.
    This will allow to build apps directly from reports using each underlying components available in the framework.

    Usage::

    Attributes:
    ----------
    :param name: String. Optional. The component name. Can be set to define test components.
    """
    if name is not None:
      self.rename(name)
    self._out_mode = "angular"
    html = self._html.html()
    return {'folder': self.folder, 'class': "Epyk%sComponent" % self.name, 'externalVars': '',
            'css': self._html.attr['css'], 'htmlTag': self.tag, 'build': self._html._js__builder__.strip(),
            'html': html, 'options': self._html._jsStyles}
