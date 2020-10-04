
import os
import subprocess

MODULE = "primeng"


class Package(object):

  def __init__(self, page, app):
    self.page, self.app = page, app
    self.path = os.path.join(self.app._node_path, self.app._app_name)

  def install(self):
    """
    Description:
    ------------
    PrimeNG is available at npm, if you have an existing application run the following command to download it to your project.

    https://primefaces.org/primeng/showcase/#/setup
    """
    subprocess.run('npm install %s' % MODULE, shell=True, cwd=self.path)
    subprocess.run('npm install primeicons', shell=True, cwd=self.path)

  def sdk(self):
    """
    Description:
    ------------
    VirtualScrolling enabled Dropdown depends on @angular/cdk's ScrollingModule so begin with installing CDK if not already installed.

    https://primefaces.org/primeng/showcase/#/dropdown
    """
    subprocess.run('npm install @angular/cdk --save', shell=True, cwd=self.path)

  def update(self):
    """
    Description:
    ------------
    Install PrimeNG Framework on top of your Angular framework.

    This will trigger the automatic install defined on the official website.

    https://clarity.design/documentation/get-started
    """
    subprocess.run('npm update %s' % MODULE, shell=True, cwd=self.path)
    subprocess.run('npm update primeicons', shell=True, cwd=self.path)

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
