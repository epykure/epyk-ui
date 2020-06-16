
import subprocess

from epyk.core import Page
from epyk.web import node


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


class NpxCli(object):
  def __init__(self, vue_app_path):
    self._vue_app_path = vue_app_path

  def create(self, name=None):
    """
    https://fr.reactjs.org/docs/create-a-new-react-app.html

    :param name:
    """
    if name is None:
      subprocess.run('npx create-react-app --help', shell=True, cwd=self._vue_app_path)
    else:
      subprocess.run('npx create-react-app %s' % name, shell=True, cwd=self._vue_app_path)

  def build(self):
    """
    Description:
    ------------
    Builds the app for production to the build folder.
    It correctly bundles React in production mode and optimizes the build for the best performance.

    https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm run build', shell=True, cwd=self._vue_app_path)

  def start(self):
    """
    Description:
    ------------
    Runs the app in development mode. Open http://localhost:3000 to view it in the browser.

    https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._vue_app_path)

  def test(self):
    """
    Description:
    ------------
    Runs the test watcher in an interactive mode. By default, runs tests related to files changed since the last commit.

    https://create-react-app.dev/docs/getting-started/
    """
    subprocess.run('npm test', shell=True, cwd=self._vue_app_path)


class React(node.Node):

  def cli(self, app_name=None):
    """
    Description:
    ------------
    Create React App is an officially supported way to create single-page React applications.
    It offers a modern build setup with no configuration.

    Related Pages:

      https://create-react-app.dev/docs/getting-started

    Attributes:
    ----------
    :param app_name: String. The React.js application name
    """
    return NpxCli(self._app_path)
