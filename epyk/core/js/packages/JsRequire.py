"""

"""

from epyk.core.js import Imports


class JsRequire(object):
  """

  Documentation
    - https://requirejs.org/docs/api.html#mechanics

  """

  def __init__(self, requireJs=False):
    """

    :param requireJs:
    """
    self. requireJs = requireJs

  def resolveImports(self, modules, moduleStack, level, modulesBase):
    """

    :param modules:
    :param moduleStack:
    :param level:

    :return:
    """
    for m in modules:
      mDef = UIDeps.PACKAGES.get(m, {})
      reqModules = []
      for req in mDef.get('req', []):
        reqModules.append(req['alias'])
      if len(reqModules) > 0:
        moduleStack.append([])
        self.resolveImports(reqModules, moduleStack, level+1, modulesBase)
      else:
        modulesBase.append(m)
      moduleStack[level].append(m)

  def getImports(self, modules):
    result = {'header': [], 'requireJs': ''}
    moduleStack, modulesBase = [[]], []
    self.resolveImports(modules, moduleStack, 0, modulesBase)
    moduleStack[-1].extend(modulesBase)
    mOrdered, reqJs = [], []
    for mLevel in moduleStack[::-1]:
      reqJs.append([])
      for m in mLevel:
        if m not in mOrdered:
          mOrdered.append(m)
          reqJs[-1].append(m)
      if len(reqJs[-1]) == 0:
        reqJs.pop()
    return {'header': mOrdered, 'reqJs': reqJs}

  def fullHeader(self, modules, repoPath=None):
    header = []
    for alias in modules:
      mDef = UIDeps.PACKAGES.get(alias, {})
      for m in mDef.get('modules', []):
        path = m["path"] % m
        if repoPath is None:
          fullPath = '%s/%s%s' % (mDef['cdnjs'], path, m['script'])
        else:
          fullPath = '%s/%s%s' % (repoPath, path, m['script'])
        if m['script'].endswith(".css"):
          header.append("<link rel='stylesheet' href='%s'>" % fullPath)
        else:
          header.append("<script  src='%s' type='text/javascript'=></script>" % fullPath)
    return header
