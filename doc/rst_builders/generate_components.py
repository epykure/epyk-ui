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
    elif suffix.startswith("tables"):
      sub_components["table"].append("    /report/components/tables/%s" % mod_file)
    elif mod_file.startswith("Geo"):
      sub_components["geo"].append("    /report/components/geo/%s" % mod_file)
    elif mod_file.startswith("Chart"):
      sub_components["charts"].append("    /report/components/graph/%s" % mod_file)
    mod = importlib.import_module("epyk.core.html.%s" % suffix)
    with open(r'%s\%s.rst' % (outpath, mod_file), 'w') as doc_file:
      title_str = '%s Module' % mod_file
      doc_file.write('%s\n%s\n\n' % (title_str, '=' * len(title_str)))
      for member, memclass in inspect.getmembers(mod, inspect.isclass):
        if "'" in str(memclass):
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

.. toctree::
    :maxdepth: 1
    
%s
''' % "\n".join(sub_components["charts"]))

  with open(os.path.join(os.path.dirname(__file__), "..", "report", "components", 'geos.rst'), "w") as fp:
    fp.write('''
Geo Components
===============

.. toctree::
    :maxdepth: 1
    
%s
''' % "\n".join(sub_components["geo"]))

  with open(os.path.join(os.path.dirname(__file__), "..", "report", 'all_components.rst'), "w") as fp:
    fp.write('''
Epyk Components
===============

The Core Html Components all inherit from :py:class:`epyk.core.html.Html`, they're the base for every objects you see on your html page.

The core Html Components are divided into 4 categories:

- :doc:`components/htmls`
- :doc:`components/tables`
- :doc:`components/graphs`
- :doc:`components/geos`

.. toctree::
    :maxdepth: 1

    /components/htmls
    /components/tables
    /components/graphs
    /components/geos


Plus

.. toctree::
    :maxdepth: 1

    /components/options
    /components/entities
    /components/symboles

.. currentmodule:: epyk.core.html
''')


with open(os.path.join(os.path.dirname(__file__), "..", "report", 'html_builtins.rst'), "w") as fp:
  fp.write('''
HTML Built-Ins
==============

.. toctree::
    :maxdepth: 1

    /components/htmls
    /components/tables
    /components/graphs
    /components/geos

''')
