"""
"""
import sys
import argparse
import pkg_resources
import shutil
#to delete
import os
sys.path.append(os.getcwd())
from epyk.core.js import Imports

def main():
  """"""
  parser_map = { 'env':           (create_env_parser,         '''Create new environment'''),
                 'deploy':        (create_deploy_parser,      '''Deploy latest changes'''),
                  'db':           (create_db_parser,          '''Performs operation on local DB (Sqlite)'''),
                  'get_packages': (create_import_pkg_parser,  '''Downloads Javascript and CSS packages to allow offline development'''),
                  'version':      (create_version_parser,     '''Informs on current package version'''),
                  'notebooks':    (create_notebook_parser,    '''Donwloads or Upload Jupyter notebooks online''')
                }
  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparser = arg_parser.add_subparsers(title='Commands', dest='command')
  subparser.required = True
  for func, parser_init in parser_map.items():
    new_parser = subparser.add_parser(func, help=parser_init[1])
    parser_init[0](new_parser)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)


def create_env_parser(subparser):
  """"""
  subparser.set_defaults(func=env)
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-n', '--name', default='NewEnv', help='''The name of the new environment: -n MyEnv''')
  subparser.add_argument('--from', help='''Path or URL of the environment to be copied from: --from /foo/bar/oldEnv or --from http://repo/env1/getEnv''')
  subparser.add_argument('--only', nargs='+', help='''If the from option is specified this will allow only certain folder/files to be copied: --only script1.py folder/scripts*.py''')

def create_deploy_parser(subparser):
  """"""
  subparser.set_defaults(func=deploy)
  subparser.add_argument('-p', '--path', nargs='+', required=True, help='''The path where the environment you want to deploy is: -p /foo/bar/myEnv''')

def create_db_parser(subparser):
  """"""
  subparser.set_defaults(func=db)
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-m', '--migrate', help='''The path where the new environment will be created: -p /foo/bar''')

def create_import_pkg_parser(subparser):
  """"""
  subparser.set_defaults(func=get_packages)
  subparser.add_argument('-p', '--path', required=True, help='''The path of the project where the package will be download: -p /foo/bar''')
  subparser.add_argument('-o', '--only', nargs='+', default=['all'], help='''The name of the package to be downloaded (by default we will download all packages): -n d3.min.js''')
  subparser.add_argument('-x', '--exclude', help='''packages to be excluded: -x d3.min.js''')


def create_version_parser(subparser):
  """"""
  subparser.set_defaults(func=version)

def create_notebook_parser(subparser):
  """"""
  subparser.set_defaults(func=notebooks)

def env(args):
  """
   Creates a new epyk environment on disk
  """
  pass

def deploy(args):
  """

  """
  pass

def db(args):
  """"""
  pass

def get_packages(args):
  """"""
  print(args)
  static_path = args.path
  try:
    shutil.copytree(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', 'static'),
                      os.path.join(static_path, 'static'))
  except FileExistsError:
    pass

  if 'all' in args.only:
    exclude = args.exclude if args.exclude else None
    Imports.ImportManager().getPackages(static_path=static_path, exclude=exclude)
  else:
    for package in args.only:
      Imports.ImportManager().getPackage(package, reload=True, static_path=static_path)

def version(args):
  """
  Returns the package version for Epyk
  """
  print('Epyk Version: %s' % pkg_resources.get_distribution('epyk').version)

def notebooks(args):
  """Allows you to download or upload notebooks"""
  pass

if __name__ == '__main__':
  import os
  print(os.getcwd())
  main()
