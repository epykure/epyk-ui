import importlib, subprocess, sys, os



class Pyk(object):
  """

  """

  __stack = None

  def __init__(self):
    self.__stack = []

  @staticmethod
  def requires(pyk_file, components=None, autoinstall=False):
    """
    Description:
    ------------------

      This function will allow you to import components from another pyk file.
      The pyk file can be located on your file system, or it can be on pypi or even github
      if it's the latter options (pypi or github) you will need to use autoinstall=True

    Usage:
    -----------
      pyk.requires(pyk_name, autoinstall=True)

      pyk.requires('/usr/local/my_pyk_file.py', components=['obj1', 'obj2'])

    :param pyk_file: the pyk to be imported into your project, this will be a name if installing from pypi or github or just a path if it's a local pyk)
    :param components: list of objects to import, if None all the objects declared in the pyk file will be available
    :param autoinstall: specify whether we need to check github or pypi
    :return: a pyk object
    """

    if pyk_file.endswith('.py'):
      pass

    try:
      mod = importlib.import_module(pyk_file)
      print(mod)
    except (ModuleNotFoundError, ImportError):
      if not autoinstall:
        print("The package is not found on your environment, you will need to install it manually or use the autoinstall argument")
        raise

      subprocess.check_call([sys.executable, '-m', 'pip', 'install', pyk_file])
      mod = importlib.import_module((pyk_file))




if __name__ == '__main__':
  Pyk.requires('flask2')