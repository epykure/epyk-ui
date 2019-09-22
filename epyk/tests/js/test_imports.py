""" """

import collections

from epyk.core.js import Imports
from epyk.core.Page import Report

#Imports.installed_packages()


report = Report()
imports = Imports.ImportManager(report=report)

modules = collections.OrderedDict()
print(imports.getModules(modules, 'c3'))

i = imports.cleanImports(['c3'], Imports.JS_IMPORTS)
print(i)

i = imports.cssResolve(['c3'])
print(i)

f = imports.getFiles(['c3'], ['c3'])
print(f['css'][0]['file']['script'])
#

p = imports.getPackage('jqueryui', static_path=r"..\outs")
p = imports.getFullPackage('font-awesome', static_path=r"..\outs")
