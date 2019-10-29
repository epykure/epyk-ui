"""
"""
import sys
import argparse
import pkg_resources

arg_parser = argparse.ArgumentParser(prog='epyk')

def main():
  """"""
  init_parsers()
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)

def init_parsers():
   """"""
   parser_map = { 'env':          (create_env_parser,         '''Create new environment'''),
                  'deploy':       (create_deploy_parser,      '''Deploy latest changes'''),
                  'db':           (create_db_parser,          '''Performs operation on local DB (Sqlite)'''),
                  'get_packages': (create_import_pkg_parser,  '''Downloads Javascript and CSS packages to allow offline development'''),
                  'version':      (create_version_parser,     '''Informs on current package version'''),
                  'notebooks':    (create_notebook_parser,    '''Donwloads or Upload Jupyter notebooks online''')
                }
   arg_parser.add_argument('command', help='''Choose one command from the following: %s''' % ', '.join(parser_map.keys()))
   for func, parser_init in parser_map.items():
     print(func)
     new_parser = argparse.ArgumentParser(parents=[arg_parser], usage=parser_init[1])
     parser_init[0](new_parser)

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
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-p', '--path', required=True, help='''The path where the new environment will be created: -p /foo/bar''')

def create_import_pkg_parser(subparser):
  """"""
  subparser.set_defaults(func=get_packages)

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
  pass

def version(args):
  """
  Returns the package version for Epyk
  """
  print('Epyk Version: %s' % pkg_resources.get_distribution('epyk').version)

def notebooks(args):
  """Allows you to download or upload notebooks"""
  pass

if __name__ == '__main__':
  main()
