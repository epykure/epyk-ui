"""
"""
import sys
import argparse
import pkg_resources


def main():
  """"""
  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparsers = arg_parser.add_subparsers()
  init_parsers(subparsers)
  args = arg_parser.parse_args(sys.argv[1:])
  return args.func(args)

def init_parsers(subparsers):
   """"""
   parser_map = { 'env':          create_env_parser,
                  'deploy':       create_deploy_parser,
                  'migrate_db':   create_migrate_parser,
                  'get_packages': create_import_pkg_parser,
                  'version':      create_version_parser,
                }
   for func, parser_init in parser_map.items():
     new_parser = subparsers.add_parser(func)
     parser_init(new_parser)

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

def create_migrate_parser(subparser):
  """"""
  subparser.set_defaults(func=migrate_db)

def create_import_pkg_parser(subparser):
  """"""
  subparser.set_defaults(func=get_packages)

def create_version_parser(subparser):
  """"""

  subparser.set_defaults(func=version)

def env(args):
  """
   Creates a new epyk environment on disk
  """
  pass

def deploy(args):
  """

  """
  pass

def migrate_db(args):
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

if __name__ == '__main__':
  main()
