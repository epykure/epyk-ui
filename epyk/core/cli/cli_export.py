"""

epyk_export.exe
"""

import os
import sys
import argparse

from epyk.core.cli import utils


def transpile_parser(subparser):
  """
  Description:
  ------------
  Paser for the transpile CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=transpile)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def transpile(args):
  """
  Description:
  ------------
  Transpile a specific report

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  :param parser: -n, The name of the page to be transpiled: -n home
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  report_path = utils.get_report_path(project_path, raise_error=False)
  sys.path.append(report_path)
  ui_setting_path = os.path.join(report_path, '..', 'ui_settings.py')
  install_modules, split_files, view_folder, packages_path, package_url = False, False, 'views', 'static', None
  if os.path.exists(ui_setting_path):
    settings = __import__('ui_settings')
    install_modules = settings.INSTALL_MODULES
    split_files = settings.SPLIT_FILES
    view_folder = settings.VIEWS_FOLDER
    packages_path = settings.PACKAGE_PATH
    package_url = settings.SERVER_PACKAGE_URL
  mod = __import__(args.name, fromlist=['object'])
  page = utils.get_page(mod)
  page.node_modules(os.path.join(report_path, '..', packages_path), alias=package_url)
  output = page.outs.html_file(path=view_folder, name=args.name, split_files=split_files, install_modules=install_modules,
                               options={"css_route": '/css', "js_route": '/js'})
  print(output)


def angular_parser(subparser):
  """
  Description:
  ------------
  Paser for the angular CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=angular)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def angular(args):
  """
  Description:
  ------------
  Generate an Angular Application from the Epyk page

  Attributes:
  ----------
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  report_path = utils.get_report_path(project_path, raise_error=False)
  sys.path.append(report_path)
  ui_setting_path = os.path.join(report_path, '..', 'ui_settings.py')
  auto_route, install_modules, view_folder, angular_app_path = False, False, 'views', None
  if os.path.exists(ui_setting_path):
    settings = __import__('ui_settings')
    install_modules = settings.INSTALL_MODULES
    angular_app_path = settings.ANGULAR_APP_PATH
    auto_route = settings.ANGULAR_AUTO_ROUTE
    view_folder = settings.ANGULAR_VIEWS_PATH
  mod = __import__(args.name, fromlist=['object'])
  page = utils.get_page(mod)
  app = page.outs.publish(server="angular", app_path=angular_app_path, module="MyModule", selector='mymodule', target_folder=view_folder, auto_route=auto_route)
  if install_modules:
    app.cli().npm(page.imports().requirements)


def vue_parser(subparser):
  """
  Description:
  ------------
  Paser for the vue CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=vue)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def vue():
  pass


def react_parser(subparser):
  """
  Description:
  ------------
  Paser for the react CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=react)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def react():
  pass


def node_parser(subparser):
  """
  Description:
  ------------
  Paser for the node CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=node)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def node():
  pass


def deno_parser(subparser):
  """
  Description:
  ------------
  Paser for the deno CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=deno)
  subparser.add_argument('-n', '--name',  required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def deno():
  pass


def html_parser(subparser):
  """
  Description:
  ------------
  Paser for the transpile CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=transpile)
  subparser.add_argument('-n', '--name', required=True, help='''The name of the page to be transpiled (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-split', '--split', default="N", help='''Split the files: -split N''')


def html(args):
  """
  Description:
  ------------
  Transpile a specific report

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  :param parser: -n, The name of the page to be transpiled: -n home
  :param parser: -split, Y / N Flag to specify if the result should be splitting in several files
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  report_path = utils.get_report_path(project_path, raise_error=False)
  sys.path.append(report_path)
  mod = __import__(args.name, fromlist=['object'])
  page = utils.get_page(mod)
  output = page.outs.html_file(path="", name=args.name, split_files=args.split)
  print(output)


def main():
  """

  """
  parser_map = {
    'transpile': (transpile_parser, '''Transpile a script to web objects'''),
    'html': (html_parser, '''Fast HTML transpilation'''),

    'deploy': (create_deploy_parser,      '''Deploy latest changes'''),
    'db': (create_db_parser, '''Performs operation on local DB (Sqlite)'''),
    'get_packages': (create_import_pkg_parser,  '''Downloads Javascript and CSS packages to allow offline development'''),
    'version': (create_version_parser, '''Informs on current package version'''),
    'notebooks': (create_notebook_parser, '''Donwloads or Upload Jupyter notebooks online''')
  }
  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparser = arg_parser.add_subparsers(title='Commands', dest='command')
  subparser.required = True
  for func, parser_init in parser_map.items():
    new_parser = subparser.add_parser(func, help=parser_init[1])
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)
