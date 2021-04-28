import os
import importlib
import inspect
import shutil
import sys
import collections

file_path = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(file_path, '..', '..'))

output_path = os.path.join(file_path, "..", "report", "components")
initial_path = os.path.join(file_path, "..", "..", "epyk", "core", "html")
if os.path.exists(output_path):
  shutil.rmtree(output_path)
os.makedirs(output_path, exist_ok=True)

fol_lst = ['entities', 'geo', 'graph', 'options', 'symboles', 'tables', 'templates']
sub_components = collections.defaultdict(list)


def parse_folder(path, outpath):

  for f in os.listdir(path):
    if f in fol_lst:
      out_path = os.path.join(outpath, f)
      os.makedirs(out_path, exist_ok=True)
      parse_folder(os.path.join(path, f), out_path)
      continue

    if f.startswith('__'):
      continue

    mod_file = f.replace('.py', '')
    suffix = path.replace(initial_path, '')
    if suffix:
      suffix = suffix.split(os.pathsep)
      suffix.append(mod_file)
    else:
      suffix = [mod_file]
    suffix = '.'.join(suffix)
    if suffix.startswith("\\"):
      suffix = suffix[1:]

    if suffix.startswith("Html") and suffix != "Html":
      sub_components["html"].append("    /report/components/%s" % mod_file)
    if suffix.startswith("tables"):
      sub_components["table"].append("    /report/components/tables/%s" % mod_file)
    mod = importlib.import_module("epyk.core.html.%s" % suffix)
    with open(r'%s\%s.rst' % (outpath, mod_file), 'w') as doc_file:
      title_str = '%s Module' % mod_file
      doc_file.write('%s\n%s\n\n' % (title_str, '=' * len(title_str)))
      for member, memclass in inspect.getmembers(mod, inspect.isclass):
        doc_file.write('.. autoclass:: %s\n\t:members:\n\n' % str(memclass).split("'")[1])


if __name__ == '__main__':
  parse_folder(initial_path, output_path)

  with open(os.path.join(os.path.dirname(__file__), "..", "report", "components", 'htmls.rst'), "w") as fp:
    fp.write('''
HTML / Vanilla Components
=========================

.. toctree::
    :maxdepth: 1
    
%s
''' % "\n".join(sub_components["html"]))

  with open(os.path.join(os.path.dirname(__file__), "..", "report", "components", 'tables.rst'), "w") as fp:
      fp.write('''
Table Components
================

.. toctree::
    :maxdepth: 1
    
%s
''' % "\n".join(sub_components["table"]))

  with open(os.path.join(os.path.dirname(__file__), "..", "report", "components", 'graphs.rst'), "w") as fp:
      fp.write('''
Graph Components
===============
''')

  with open(os.path.join(os.path.dirname(__file__), "..", "report", "components", 'geos.rst'), "w") as fp:
    fp.write('''
Geo Components
===============
''')

  with open(os.path.join(os.path.dirname(__file__), "..", "report", 'components.rst'), "w") as fp:
    fp.write('''
Epyk Components
===============

The Core Html Components all inherit from :py:class:`epyk.core.html.Html`, they're the base for every objects you see on your html page.

The core Html Components are divided into 4 categories:

- :doc:`report/components/htmls`
- :doc:`report/components/tables`
- :doc:`report/components/graphs`
- :doc:`report/components/geos`

.. toctree::
    :maxdepth: 1

    /report/components/htmls
    /report/components/tables
    /report/components/graphs
    /report/components/geos


Plus

.. toctree::
    :maxdepth: 1

    /report/components/options
    /report/components/entities
    /report/components/symboles

.. currentmodule:: epyk.core.html
''')
