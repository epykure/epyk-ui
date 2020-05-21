import importlib, subprocess, sys, os, inspect

class EpykMissingPykException(Exception):
  pass


class Pyk(object):
  """

  """

  __pyk_dict = None
  __instance = None


  class __Pyk(object):
    pass

  def __new__(cls):
    if cls.__instance is None:
      cls.__instance = super(Pyk, cls).__new__(cls)
      cls.__pyk_dict = {}
    return cls.__instance

  @classmethod
  def requires(cls, pyk_file, components=None, autoinstall=False):
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
    cls()

    if pyk_file.endswith('.py'):
      path_split = pyk_file.split(os.sep)
      sys.path.append(os.sep.join(path_split[:-1]))
      mod = importlib.import_module(path_split[-1].replace('.py', ''))
    else:
      try:
        importlib.import_module(pyk_file)
      except (ModuleNotFoundError, ImportError):
        if not autoinstall:
          print("The package is not found on your environment, you will need to install it manually or use the autoinstall argument")
          raise

        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pyk_file])
        importlib.import_module((pyk_file))

      if pyk_file not in cls.__pyk_dict:
        raise EpykMissingPykException('The specified pyk file: %s does not call the exports function, if this is your file make sure to call this!' % pyk_file)

    pyk_obj = cls.__Pyk()
    if components:
      for component in components:
        setattr(pyk_obj, component, cls.__pyk_dict[pyk_file].get(component, 'Missing component'))
    else:
      for obj_name, obj in cls.__pyk_dict[pyk_file].items():
        print(obj_name, obj)
        setattr(pyk_obj, obj_name, obj)

    return pyk_obj



  @classmethod
  def exports(cls, obj_list=None):
    pass





if __name__ == '__main__':
  Pyk.requires(r"C:\Users\nelso\Downloads\list_filter.py")