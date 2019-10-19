"""
"""
import sys
import argparse
import pkg_resources


def main():
  """"""
  arg_parser = argparse.ArgumentParser(prog='epyk')
  args = arg_parser.parse_args(sys.argv[1:])
  define_arguments(args.command, arg_parser)
  return {ep.name: ep for ep in pkg_resources.iter_entry_points(group='cli.epyk_actions')}[args.command].load()(args)

def define_arguments(func, arg_parser):
   """"""
   try:
     {'new':          create_env_parser,
      'deploy':       create_deploy_parser,
      'migrate_db':   create_migrate_parser,
      'get_packages': create_import_pkg_parser,
      'version':      do_nothing,
      }[func](arg_parser)
   except KeyError as e:
     raise argparse.ArgumentError('Function %s is not defined as a command line function for epyk' % func)

def create_env_parser(arg_parser):
  """"""
  arg_parser.add_argument('-p', '--path', default='.', help='''The path where the new environment will be created: -p /foo/bar''')
  arg_parser.add_argument('-n', '--name', default='NewEnv', help='''The name of the new environment: -n MyEnv''')
  arg_parser.add_argument('--from', help='''Path or URL of the environment to be copied from: --from /foo/bar/oldEnv or --from http://repo/env1/getEnv''')
  arg_parser.add_argument('--only', help='''If the from option is specified this will allow only certain folder/files to be copied''')

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

def version(args):
  """
  Returns the package version for Epyk
  """
  pass