"""
Main command lines for Epyk

epyk.exe
"""

import sys
import os
import importlib
import argparse

from epyk.core.cli import utils
from epyk.core.Page import Report
from epyk.core.py.PyMarkdown import MarkDown


def new_parsers(subparser):
  """
  Description:
  ------------
  Paser for the new CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=new)
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-n', '--name', default='NewEnv', help='''The name of the new environment: -n MyEnv''')


def new(args):
  """
  Description:
  ------------
  Create a new Epyk Structure.

  The project structure is as below:
  /ui
    /reports
      Folder with all the Python scripts
    /templates
      Folder with the shared report structure
    /views
      Folder with the transpiled scripts
    ui_settings.py, configuration module for the UI framework

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  :param parser: -n, The name of the new environment: -n MyEnv
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  args.path = os.path.join(project_path, args.name)
  add(args)


def app_parser(subparser):
  """
  Description:
  ------------
  Paser for the app CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=app)
  subparser.add_argument('-t', '--type', required=True, help='''The application framework''')
  subparser.add_argument('-s', '--server', required=True, help='''The NodeJs server path''')
  subparser.add_argument('-n', '--name', required=True, help='''The Application name''')


def app(args):
  """

  :param args:
  """
  if args.type.upper() == 'REACT':
    from epyk.web import react

    node_app = react.React(args.server)
    node_app.clis.react()
    node_app.create(args.name)

  elif args.type.upper() == 'VUE':
    from epyk.web import vue

    node_app = vue.VueJs(args.server)
    node_app.clis.vue()
    node_app.create(args.name)
    node_app.cli(args.name).linter()
    node_app.cli(args.name).add_router()

  elif args.type.upper() == 'ANGULAR':
    from epyk.web import angular

    node_app = angular.Angular(args.server)
    node_app.clis.angular()
    node_app.create(args.name)
    node_app.router(args.name)


def add_parser(subparser):
  """
  Description:
  ------------
  Paser for the add CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=add)
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def add(args):
  """
  Description:
  ------------
  Add the UI structure to an existing project.
  This will not create a new workspace it will only add the mandatory structure for a valid UI project.

  The project structure is as below:
  /ui
    /links
      ui end points definition and data structures communication with the backend
    /reports
      Folder with all the Python scripts
    /templates
      Folder with the shared report structure
    /views
      Folder with the transpiled scripts
    ui_settings.py, configuration module for the UI framework

  Attributes:
  ----------
  :param parser: -p, The path where the new environment will be created: -p /foo/bar
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  for folder in ['reports', 'templates', 'links']:
    ui_path = os.path.join(project_path, 'ui', folder)
    if not os.path.exists(ui_path):
      os.makedirs(ui_path)
    if folder != 'views':
      with open(os.path.join(ui_path, '__init__.py'), "w") as f:
        pass

  settings_path = os.path.join(project_path, 'ui', 'ui_settings.py')
  if not os.path.exists(settings_path):
    with open(settings_path, "w") as f:
      f.write('''
SPLIT_FILES = False # Split the HTML, JS and CSS 
INSTALL_MODULES = False # Install the modules locally
VIEWS_FOLDER = 'ui/views' # Destination folder for the transpiled files

PACKAGE_PATH = "static" # 
SERVER_PACKAGE_URL = None # When using a server the path for the static folder

# Section dedicated to the web Applications
NODE_SERVER_PATH = None

#
ANGULAR_APP_PATH = None
ANGULAR_AUTO_ROUTE = False
ANGULAR_VIEWS_PATH = None

#
REACT_APP_PATH = None
REACT_AUTO_ROUTE = False
REACT_VIEWS_PATH = None

#
VUE_APP_PATH = None
VUE_AUTO_ROUTE = False
VUE_VIEWS_PATH = None
''')


def compile_parser(subparser):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param subparser:
  """
  subparser.set_defaults(func=page)
  subparser.add_argument('-n', '--name',  required=True, help='''The page / report name to be created (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-t', '--theme', help='''The theme in the studio for the page''')


def compile(args):
  """
  Description:
  ------------
  Compile a markdown file to a valid HTML page.

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  reports_path = utils.get_report_path(project_path)
  with open(os.path.join(reports_path, "%s.md" % args.name), "w") as md:
    md_dta = md.read()
  page = Report()
  page.py.markdown.resolve(md_dta)
  try:
    settings = __import__("ui_settings", fromlist=['object'])
    if not os.path.exists(settings.VIEWS_FOLDER):
      # If it is not an absolute path
      settings.VIEWS_FOLDER = os.path.join(reports_path, '..', '..', settings.VIEWS_FOLDER)
    output = page.outs.html_file(path=settings.VIEWS_FOLDER, name=args.name, split_files=settings.SPLIT_FILES,
                                 install_modules=settings.INSTALL_MODULES, options={"css_route": '/css', "js_route": '/js'})
  except:
    output = page.outs.html_file(name=args.name, split_files=False, install_modules=False)
  print(output)


def translate_parser(subparser):
  """
  Description:
  ------------

  Attributes:
  ----------
  :param subparser:
  """
  subparser.set_defaults(func=page)
  subparser.add_argument('-n', '--name',  required=True, help='''The page / report name to be created (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-t', '--theme', help='''The theme in the studio for the page''')


def translate(args):
  """
  Description:
  ------------
  Translate a markdown file to a valid Epyk python page.

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  reports_path = utils.get_report_path(project_path)
  with open(os.path.join(reports_path, "%s.md" % args.name), "w") as md:
    md_dta = md.read()
  results = MarkDown.translate(md_dta)
  with open(os.path.join(reports_path, "%s.py" % args.name), "w") as f:
    f.write('''
from epyk.core.Page import Report

# Create a basic report object
page = Report()
page.headers.dev()

%s
''' % "\n".join(results))


def page_parser(subparser):
  """
  Description:
  ------------
  Paser for the page CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=page)
  subparser.add_argument('-n', '--name',  required=True, help='''The page / report name to be created (without the extension)''')
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-t', '--type', help='''''')


def page(args):
  """
  Description:
  ------------
  Create a new page in the current project.

  Attributes:
  ----------
  :param parser: -p, The page / report name to be created (without the extension)
  :param parser: -n, The path where the new environment will be created: -p /foo/bar
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  reports_path = utils.get_report_path(project_path)

  name = args.name
  if name.endswith(".py"):
    name = name[:-3]
  with open(os.path.join(reports_path, "%s.py" % name), "w") as f:
    f.write('''
from epyk.core.Page import Report
from epyk.core.data import datamap, events, primitives


# Create a basic report object
page = Report()
page.headers.dev()
''')


def transpile_all_parser(subparser):
  """
  Description:
  ------------
  Paser for the transpile_all CLI

  Attributes:
  ----------
  :param subparser: subparser
  """
  subparser.set_defaults(func=transpile_all)
  subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')


def transpile_all(args):
  """
  Description:
  ------------
  Transpile to HTML all the reports in the project
  Views are generated by default at the same level than the ui_setting file

  Attributes:
  ----------
  :param args:
  """
  project_path = args.path or os.getcwd()
  sys.path.append(project_path)
  reports_path = utils.get_report_path(project_path)
  sys.path.append(reports_path)
  sys.path.append(os.path.join(reports_path, '..'))
  settings = __import__("ui_settings", fromlist=['object'])
  for report in os.listdir(reports_path):
    if report.endswith(".py") and report != "__init__.py":
      view_name = report[:-3]
      mod = __import__(view_name, fromlist=['object'])
      importlib.reload(mod)
      try:
        page = utils.get_page(mod)
        page.node_modules(settings.PACKAGE_PATH, alias=settings.SERVER_PACKAGE_URL)
        if not os.path.exists(settings.VIEWS_FOLDER):
          # If it is not an aboslute path
          settings.VIEWS_FOLDER = os.path.join(reports_path, '..', '..', settings.VIEWS_FOLDER)
        output = page.outs.html_file(path=settings.VIEWS_FOLDER, name=view_name, split_files=settings.SPLIT_FILES, install_modules=settings.INSTALL_MODULES, options={"css_route": '/css', "js_route": '/js'})
        print(output)
      except Exception as err:
        print("Error with view: %s" % view_name)
        print(err)


def main():
  """
  Description:
  ------------
  Main entry point for the various project command lines
  """
  parser_map = {
    'new': (new_parsers, '''Create new environment'''),
    'add': (add_parser, '''Add UI framework to an existing project'''),
    'app': (app_parser, '''Create a new App'''),
    'page': (page_parser, '''Add a page to the views'''),
    'compile': (compile_parser, '''Compile Markdown file to a valid HTML page'''),
    'translate': (compile_parser, '''Translate a Markdown file to a valid Epyk python page'''),
    'transpile_all': (transpile_all_parser, '''Transpile all the pages in the project'''),
  }
  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparser = arg_parser.add_subparsers(title='Commands', dest='command')
  subparser.required = True
  for func, parser_init in parser_map.items():
    new_parser = subparser.add_parser(func, help=parser_init[1])
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)
