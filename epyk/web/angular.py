
from epyk.core.js import Imports

import os
import subprocess


def app(path, name=None):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param path:
  """
  return Angular(path, name)


def requirements(report):
  """
  Description:
  ------------
  Get the list of all the packages required in the Angular Application

  Packages can be installed in the app using the command
    > nmp install package1 package2 .....

  Attributes:
  ----------
  :param report: Python object. The report object
  """
  npms = []
  importMng = Imports.ImportManager(online=True, report=report)
  for req in importMng.cleanImports(report.jsImports, Imports.JS_IMPORTS):
    if 'register' in Imports.JS_IMPORTS[req]:
      if 'npm' in Imports.JS_IMPORTS[req]['register']:
        npms.append(Imports.JS_IMPORTS[req]['register']['npm'])
      else:
        print("No npm requirement defined for %s" % req)
    else:
      print("No npm requirement defined for %s" % req)
  return npms


class NGModule(object):

  def __init__(self, ang_app_path):
    self._ang_app_path = ang_app_path

  def class_(self, name):
    """
    Description:
    ------------
    Creates a new generic class definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#class-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate class %s' % name, shell=True, cwd=self._ang_app_path)

  def component(self, name):
    """
    Description:
    ------------
    Creates a new generic component definition in the given or default project.

    Related Pages:

			https://angular.io/cli/generate#component-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate component %s' % name, shell=True, cwd=self._ang_app_path)

  def directive(self, name):
    """
    Description:
    ------------
    Creates a new generic directive definition in the given or default project.

    Related Pages:

			https://angular.io/cli/generate#directive-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate directive %s' % name, shell=True, cwd=self._ang_app_path)

  def enum(self, name):
    """
    Description:
    ------------
    Generates a new, generic enum definition for the given or default project.

    Related Pages:

			https://angular.io/cli/generate#enum-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate enum %s' % name, shell=True, cwd=self._ang_app_path)

  def guard(self, name):
    """
    Description:
    ------------
    Generates a new, generic route guard definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#guard-command

    Attributes:
    ----------
    :param name: String. The name of the new route guard.
    """
    subprocess.run('ng generate guard %s' % name, shell=True, cwd=self._ang_app_path)

  def interceptor(self, name):
    """
    Description:
    ------------
    Creates a new, generic interceptor definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#interceptor-command

    Attributes:
    ----------
    :param name: String. The name of the interceptor.
    """
    subprocess.run('ng generate interceptor %s' % name, shell=True, cwd=self._ang_app_path)

  def interface(self, name, type):
    """
    Description:
    ------------
    Creates a new generic interface definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#interface-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    :param type: String. Adds a developer-defined type to the filename, in the format "name.type.ts".
    """
    subprocess.run('ng generate interface %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def library(self, name, type):
    """
    Description:
    ------------
    Creates a new generic library project in the current workspace.

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate library %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def module(self, name, type):
    """
    Description:
    ------------
    Creates a new generic NgModule definition in the given or default project

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate module %s %s' % (name, type), shell=True, cwd=self._ang_app_path)

  def service(self, name, type):
    """
    Description:
    ------------
    Creates a new, generic service definition in the given or default project.

    Related Pages:

      https://angular.io/cli/generate#library-command

    Attributes:
    ----------
    :param name: String. The name of the interface
    """
    subprocess.run('ng generate service %s %s' % (name, type), shell=True, cwd=self._ang_app_path)


class NG(object):
  def __init__(self, app_path, app_name=None):
    self._app_path, self._app_name = app_path, app_name

  def e2e(self, app_name=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

      https://angular.io/cli/e2e

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng e2e %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def lint(self, app_name=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/lint

		Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng lint %s' % app_name, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def new(self, name, path=None):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/new

		Attributes:
    ----------
    :param name:
    :param path:
    """
    if path is not None:
      subprocess.run('ng new %s --directory %s' % (name, path), shell=True, cwd=self._app_path)
    else:
      subprocess.run('ng new %s' % name, shell=True, cwd=self._app_path)
    print('ng new %s' % name)

  def doc(self, keyword):
    """
    Description:
    ------------
    Opens the official Angular documentation (angular.io) in a browser, and searches for a given keyword.

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param keyword:
    """
    subprocess.run('ng doc %s' % keyword, shell=True, cwd=self._app_path)

  def add(self, package):
    """
    Description:
    ------------

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param package:
    """
    subprocess.run('ng add %s' % package, shell=True, cwd=os.path.join(self._app_path, self._app_name))
    print("%s packages installed" % package)

  def analytics(self):
    """
    https://angular.io/cli
    """
    pass

  def help(self, options=None):
    """
    Description:
    ------------
    Lists available commands and their short descriptions.

    Related Pages:

			https://angular.io/cli

		Attributes:
    ----------
    :param app_name:
    """
    if options is None:
      subprocess.run('ng help', shell=True, cwd=self._app_path)
    else:
      subprocess.run('ng help %s' % options, shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def test(self, app_name=None):
    """
    Description:
    ------------

    Related Pages:

			https://angular.io/cli

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng test %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

  def build(self, app_name=None):
    """
    Description:
    ------------
    Compiles an Angular app into an output directory named dist/ at the given output path. Must be executed from within a workspace directory.

    Related Pages:

			https://angular.io/cli

    Attributes:
    ----------
    :param app_name:
    """
    app_name = app_name or self._app_name
    if app_name is None:
      raise Exception("An Angular aplication name is required!")

    subprocess.run('ng build %s' % app_name, shell=True, cwd=os.path.join(self._app_path, app_name))

  def version(self):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.
    """
    subprocess.run('ng version', shell=True, cwd=os.path.join(self._app_path, self._app_name))

  def serve(self):
    """
    Description:
    ------------
    Builds and serves an Angular app, then runs end-to-end tests using Protractor.

    Related Pages:

			https://angular.io/cli/serve
    """
    subprocess.run('ng serve --open', shell=True, cwd=os.path.join(self._app_path, self._app_name))

  @property
  def create(self):
    """
    Description:
    ------------
    Shortcut to the various generate entry points in the Angular Framework
    """
    return NGModule(os.path.join(self._app_path, self._app_name))

  def generate(self, schematic, name):
    """
    Description:
    ------------
    Generates and/or modifies files based on a schematic.

    Related Pages:

			https://angular.io/cli/generate

    Attributes:
    ----------
    :param schematic:
    :param name:
    """
    subprocess.run('ng generate %s %s' % (schematic, name), shell=True, cwd=os.path.join(self._app_path, self._app_name))


class Angular(object):

  def __init__(self, app_path, name=None):
    self._app_path, self._app_name = app_path, name

  def create(self, node_path):
    """
    Description:
    ------------

    """

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
    :param packages:
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
    :param packages:
    """
    subprocess.run('npm uninstall %s' % " ".join(packages), shell=True, cwd=self._app_path)
    print("%s packages uninstalled" % len(packages))

  def install(self):
    """
    Description:
    ------------
    Install or update Angular on the defined path
    """
    subprocess.run('npm install -g @angular/cli', shell=True, cwd=self._app_path)
    print("Angular CLI installed")

  def ng(self, app_name=None):
    """
    Description:
    ------------
    Angular specific command lines

    Related Pages:

			https://angular.io/cli/

    Attributes:
    ----------
    :param app_name: String. The angular application name
    """
    app_name = app_name or self._app_name
    return NG(self._app_path, app_name)

