
import os
import subprocess

from epyk.core.py import primitives
from epyk.web.components.angular.assets import mat

MODULE = "@angular/material"


class Package:

  def __init__(self, page: primitives.PageModel, app):
    self.page, self.app = page, app
    self.path = os.path.join(self.app._node_path, self.app._app_name)

  def install(self):
    """  
    Install Bootstrap Framework on top of your Angular framework.

    This will trigger the automatic install defined on the official website.

    Related Pages:

      https://material.angular.io/guide/getting-started
    """
    subprocess.run('npm add %s' % MODULE, shell=True, cwd=self.path)

  def update(self):
    """  
    Install Clarity Framework on top of your Angular framework.

    This will trigger the automatic install defined on the official website.

    Related Pages:

      https://material.angular.io/guide/getting-started
    """
    subprocess.run('npm update %s' % MODULE, shell=True, cwd=self.path)

  @property
  def components(self):
    return Components(self.page, self.app)


class Components:

  def __init__(self, page: primitives.PageModel, app):
    self.page, self.app = page, app
    self.path = os.path.join(self.app._node_path, self.app._app_name)
    self.check()

  def check(self):
    """  
    Check if the package is installed on the server
    """
    if not os.path.exists(os.path.join(self.path, 'node_modules', MODULE)):
      raise ValueError("Components package missing on the target server, please run install() first")

  def autocomplete(self):
    """  

    https://material.angular.io/components/autocomplete/examples
    """
    return mat.AutoComplete()

  def date(self):
    return mat.DatePicker(self.page, "Test")
