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
   parser_map = { 'new':          create_env_parser,
                  'deploy':       create_deploy_parser,
                  'migrate_db':   create_migrate_parser,
                  'get_packages': create_import_pkg_parser,
                  'version':      do_nothing,
                }
   for func, parser_init in parser_map.items():
     new_parser = subparsers.add_parser(func)
     new_parser.set_defaults(func=func)
     parser_init(new_parser)

def create_env_parser(subparser):
  """"""
  subparser.add_argument('-p', '--path', default='.', help='''The path where the new environment will be created: -p /foo/bar''')
  subparser.add_argument('-n', '--name', default='NewEnv', help='''The name of the new environment: -n MyEnv''')
  subparser.add_argument('--from', help='''Path or URL of the environment to be copied from: --from /foo/bar/oldEnv or --from http://repo/env1/getEnv''')
  subparser.add_argument('--only', nargs='+', help='''If the from option is specified this will allow only certain folder/files to be copied: --only script1.py folder/scripts*.py''')

def create_deploy_parser(arg_parser):
  """"""
  pass

def create_migrate_parser(arg_parser):
  """"""
  pass

def create_import_pkg_parser(arg_parser):
  """"""
  pass

def do_nothing(arg_parser):
  """"""
  pass

def env(args):
  """
   Creates a new epyk environment on disk
  """

def version(args):
  """
  Returns the package version for Epyk
  """
  print('Epyk Version %s' % pkg_resources.get_distribution('epyk').version)

if __name__ == '__main__':
  def test():
    print('toto')

  arg_parser = argparse.ArgumentParser(prog='epyk')
  subparsers = arg_parser.add_subparsers()
  test = subparsers.add_parser('test')
  test.add_argument('-l', nargs='+')
  test.add_argument('-y', type=int)
  test.set_defaults(func='test')
  args = arg_parser.parse_args(sys.argv[1:])
  print(args)
  print(args.func)