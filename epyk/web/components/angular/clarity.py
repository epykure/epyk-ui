
import os
import subprocess

from epyk.web.components.angular.assets import clr

MODULE = "@clr/ui"


class Package(object):

  def __init__(self, page, app):
    self.page, self.app = page, app
    self.path = os.path.join(self.app._node_path, self.app._app_name)

  def install(self):
    """
    Description:
    ------------
    Install Clarity Framework on top of your Angular framework.

    This will trigger the automatic install defined on the official website.

    https://clarity.design/documentation/get-started
    """
    subprocess.run('npm install @clr/ui --save', shell=True, cwd=self.path)

  def update(self):
    """
    Description:
    ------------
    Install Clarity Framework on top of your Angular framework.

    This will trigger the automatic install defined on the official website.

    https://clarity.design/documentation/get-started
    """
    subprocess.run('npm update %s' % MODULE, shell=True, cwd=self.path)

  @property
  def components(self):
    return Components(self.page, self.app)


class Components(object):

  def __init__(self, page, app):
    self.page, self.app = page, app
    self.path = os.path.join(self.app._node_path, self.app._app_name)
    self.check()

  def check(self):
    """
    Description:
    ------------
    Check if the package is installed on the server

    :return:
    """
    if not os.path.exists(os.path.join(self.path, 'node_modules', MODULE)):
      raise Exception("Components package missing on the target server, please run install() first")

  def accordeon(self):
    return clr.Acordeon(self.page, "Test")
