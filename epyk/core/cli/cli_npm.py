"""
Dedicated CLI for the External packages management.

epyk_npm.exe
"""

import sys
import os
import argparse

from epyk.core.js import Imports
from epyk.core.py import PyNpm
from epyk.core.cli import utils


def install_all_parser(subparser):
  """
  Description:
  ------------
  Parser for the install all CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=install_all)
  subparser.add_argument('-p', '--path', help='''The UI project path''')


def install_all(args):
  """
  Description:
  ------------
  Install all the internally defined packages locally.
  This will mimic the structure of NPM in order to facilitate the links.

  Attributes:
  ----------
  :param parser: -p, The project path
  """
  packages = set(Imports.CSS_IMPORTS.keys()) | set(Imports.JS_IMPORTS.keys())
  project_path = args.path or os.getcwd()
  reports_path = utils.get_report_path(project_path, raise_error=False)

  sys.path.append(os.path.join(reports_path, '..'))
  static_path = "static"
  if os.path.exists(os.path.join(reports_path, '..', "ui_settings.py")):
    settings = __import__("ui_settings", fromlist=['object'])
    static_path = settings.PACKAGE_PATH
  module_path = os.path.join(reports_path, static_path)
  if not os.path.exists(module_path):
    os.makedirs(module_path)
  PyNpm.install(packages, path=module_path, is_node_server=False, update=False)


def install_parser(subparser):
  """
  Description:
  ------------
  Parser for the install CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=install)
  subparser.add_argument('-pkg', '--packages', required=True, help='''The packages list comma separated''')
  subparser.add_argument('-p', '--path', required=True, help='''The UI project path''')


def install(args):
  """
  Description:
  ------------
  Install only the defined packages locally.
  Those packages can be only the ones that the React or Vue scripters will be using.

  The install will rely on the version and configuration in the Imports module

  Attributes:
  ----------
  :param parser: -pkg, String, The packages list comma separated
  :param parser: -p, The project path
  """
  PyNpm.install(args.packages.split(","), path=args.path, is_node_server=False, update=False)


def update_parser(subparser):
  """
  Description:
  ------------
  Parser for the update CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=update)
  subparser.add_argument('-pkg', '--packages', required=True, help='''The packages list comma separated''')
  subparser.add_argument('-p', '--path', required=True, help='''The UI project path''')


def update(args):
  """
  Description:
  ------------
  Install only the defined packages locally.

  The install will rely on the version and configuration in the Imports module

  Attributes:
  ----------
  :param parser: -pkg, String, The packages list comma separated
  :param parser: -p, The project path
  """
  PyNpm.install(args.packages.split(","), path=args.path, is_node_server=False, update=True)


def npm_parser(subparser):
  """
  Description:
  ------------
  Parser for the npm CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=npm)
  subparser.add_argument('-pkg', '--packages', required=True, help='''The packages list comma separated''')
  subparser.add_argument('-s', '--server', required=True, help='''''')


def npm(args):
  """
  Description:
  ------------
  Install the external packages relying on the NPM Javascript command line availabke on the NodeJs server.
  This will not install the packages using the definition in Imports but on the ones in the NPM configuration.

  Attributes:
  ----------
  :param parser: -pkg, String, The packages list comma separated
  :param parser: -s, Path of the NodeJs server
  """
  PyNpm.install(args.packages.split(","), path=args.server, is_node_server=True, update=False)


def requirements_parser(parser):
  """
  Description:
  ------------
  Paser for the requirements CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  parser.set_defaults(func=requirements)
  parser.add_argument('-p', "--path", help="The UI work ath")
  parser.add_argument('-r', "--page", required=True, help="The report name")


def requirements(args):
  """
  Description:
  ------------
  Get the list of external modules required for a script.

  Attributes:
  ----------
  :param parser: -p, the workspace path (Optional if run directly in the project root)
  :param parser: -r, The page name (without the .py extension)
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)

  reprot_path = utils.get_report_path(project_path)
  sys.path.append(reprot_path)
  mod = __import__(args.page, fromlist=['object'])
  page = utils.get_page(mod)
  page.html()
  return page.imports().requirements


def angular_parser(parser):
  """
  Description:
  ------------
  Paser for the angular CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  parser.set_defaults(func=angular)
  parser.add_argument('-s', "--server", required=True, help="The nodeJs server path")
  parser.add_argument('-n', "--name", required=True, help="The Angular application name")


def angular(args):
  """
  Description:
  ------------
  Create an Angular application derived from the main NodeJs server.
  Then Angular CLI must be available on the NodeJs server.

  Attributes:
  ----------
  :param parser: -s, The nodeJs server path
  :param parser: -n, The Angular application name
  """
  from epyk.web import angular

  node_app = angular.Angular(args.server)
  node_app.clis.angular()
  node_app.create(args.name)
  node_app.router(args.name)


def vue_parser(parser):
  """
  Description:
  ------------
  Paser for the vue CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  parser.set_defaults(func=vue)
  parser.add_argument('-s', "--server", required=True, help="The nodeJs server path")
  parser.add_argument('-n', "--name", required=True, help="The Vue application name")


def vue(args):
  """
  Description:
  ------------
  Create the VueJs application

  Attributes:
  ----------
  :param parser: -s, The nodeJs server path
  :param parser: -n, The Angular application name
  """
  from epyk.web import vue

  node_app = vue.VueJs(args.server)
  node_app.clis.vue()
  node_app.create(args.name)
  node_app.cli(args.name).linter()
  node_app.cli(args.name).add_router()


def react_parser(parser):
  """
  Description:
  ------------
  Paser for the vue CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  parser.set_defaults(func=react)
  parser.add_argument('-s', "--server", required=True, help="The nodeJs server path")
  parser.add_argument('-n', "--name", required=True, help="The React application name")


def react(args):
  """
  Description:
  ------------
  Create the React application

  Attributes:
  ----------
  :param parser: -s, The nodeJs server path
  :param parser: -n, The Angular application name
  """
  from epyk.web import react

  node_app = react.React(args.server)
  node_app.clis.react()
  node_app.create(args.name)


def main():
  """
  Description:
  ------------

  """
  parser_map = {'npm': (npm_parser, '''Add packages to the Nodejs server'''),
                'update': (update_parser, '''Update the selected external modules on the Python server'''),
                'install': (install_parser, '''Install the selected external module on the Python server'''),
                'required': (requirements_parser, '''Get all the external packages required for a page'''),
                'install_all': (install_all_parser, '''Install all the external packages defined in the framework'''),
                'angular': (install_all_parser, '''Create an Angular Application'''),
                'vue': (install_all_parser, '''Create an Vue Application'''),
                'react': (install_all_parser, '''Create an React Application'''),
  }
  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparser = arg_parser.add_subparsers(title='Commands', dest='command')
  subparser.required = True
  for func, parser_init in parser_map.items():
    new_parser = subparser.add_parser(func, help=parser_init[1])
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)
