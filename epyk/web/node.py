
import subprocess


class Node(object):

  def __init__(self, app_path, name=None):
    self._app_path, self._app_name = app_path, name
    self._route, self._fmw_modules = None, None
    self._page = None

  def npm(self, packages):
    """
    Description:
    ------------
    Use npm install on a package.
    Can be done directly on the nodeJs app using the command line:
      npm install package1 package2 .....

    Attributes:
    ----------
    :param packages: List. The list of packages to install retrieved from requirements()
    """
    subprocess.run('npm install %s --save' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages installed" % len(packages))

  def ls(self):
    """
    Description:
    ------------
    Search the registry for packages matching terms
    """
    subprocess.run('npm ls', shell=True, cwd=self._app_path)

  def docs(self, package):
    """
    Description:
    ------------
    Display the README.md / documentation / npmjs.org page of a give library

    :param package: String. The package alias
    """
    subprocess.run('npm docs %s' % package, shell=True, cwd=self._app_path)

  def update(self, packages):
    """
    Description:
    ------------
    Update all the packages listed to the latest version (specified by the tag config). Also install missing packages

    Attributes:
    ----------
    :param packages: List. The list of packages to be installed
    """
    subprocess.run('npm update %s' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages updated" % len(packages))

  def uninstall(self, packages):
    """
    Description:
    ------------
    Uninstall a package, completely removing everything npm installed on its behalf

    Attributes:
    ----------
    :param packages: List. The list of packages to be installed
    """
    subprocess.run('npm uninstall %s' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages uninstalled" % len(packages))

  def install(self):
    """
    Description:
    ------------
    Install or update Vue.Js on the defined path
    """
    subprocess.run('npm install -g @vue/cli', shell=True, cwd=self._app_path)
    print("Angular CLI installed")
