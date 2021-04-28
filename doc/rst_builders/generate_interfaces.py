import os
import importlib
import inspect
import sys
import shutil
import collections

file_path = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(file_path, '..', '..'))

interfaces, group_interfaces = [], collections.defaultdict(list)
output_path = os.path.join(os.path.dirname(__file__), '..', "report", "ui")
if os.path.exists(output_path):
  shutil.rmtree(output_path)

for fol in ['components', 'geo', 'graphs', 'tables']:
  for f in os.listdir(os.path.join(os.path.dirname(__file__), '..', '..', 'epyk', 'interfaces', fol)):
    if f.startswith('__'):
      continue
      
    os.makedirs(os.path.join(output_path, fol), exist_ok=True)
    mod_file = f.replace('.py', '')
    mod = importlib.import_module("epyk.interfaces.%s.%s" % (fol, mod_file))
    for member, memclass in inspect.getmembers(mod, inspect.isclass):
      interfaces.append("    /report/ui/%s/%s" % (fol, member))
      group_interfaces[fol].append("    /report/ui/%s/%s" % (fol, member))
      with open(r'%s\%s\%s.rst' % (output_path, fol, member), 'w') as doc_file:
        title_str = '%s Interface' % member
        doc_file.write('%s\n%s\n\n' % (title_str, '=' * len(title_str)))
        doc_file.write('.. autoclass:: %s\n\t:members:' % str(memclass).split("'")[1])

for fol in ['components', 'geo', 'graphs', 'tables']:
  with open(os.path.join(os.path.dirname(__file__), "..", "report", "ui", '%s.rst' % fol), "w") as fp:
    fp.write('''
%(name)s Interface
==================

.. toctree::
    :maxdepth: 1
    
%(dir_interfaces)s

.. currentmodule:: epyk.interfaces.Interface
''' % {"name": fol,  "dir_interfaces": "\n".join(group_interfaces[fol])})


with open(os.path.join(os.path.dirname(__file__), "..", "report", 'ui.rst'), "w") as fp:
  fp.write('''
UI Interface
============

The UI interface allows you to access the different parts of the framework without having to know the underlying details how these components
are built.

These interfaces are grouped per category as follows:

Interfaces per Categories:
**************************

.. toctree::
    :maxdepth: 1
    
    /report/ui/components
    /report/ui/geo
    /report/ui/graphs
    /report/ui/tables

There are links to existing Web Framework to rely on their components:


Full list of %(num_interfaces)s Interfaces:
*******************************************

.. toctree::
    :maxdepth: 1
    
%(dir_interfaces)s

.. autoclass:: epyk.interfaces.Interface.Components
  :members:

.. currentmodule:: epyk.interfaces.Interface
''' % {"num_interfaces": len(interfaces), "dir_interfaces": "\n".join(interfaces)})
