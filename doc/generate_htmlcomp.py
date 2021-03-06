import os
import importlib, inspect

import sys
sys.path.append(r'C:\Users\nelso\PycharmProjects\epyk-ui')

output_path = r'C:\Users\nelso\PycharmProjects\epyk-ui\doc\report\html_components'
initial_path = r'C:\Users\nelso\PycharmProjects\epyk-ui\epyk\core\html\\'
fol_lst = ['entities', 'geo', 'graph', 'options', 'symboles', 'tables', 'templates']


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
    print(suffix)
    if suffix:
      suffix = suffix.split(os.pathsep)
      suffix.append(mod_file)
    else:
      suffix = [mod_file]
    suffix = '.'.join(suffix)
    print(suffix)
    mod = importlib.import_module("epyk.core.html.%s" % suffix)
    with open(r'%s\%s.rst' % (outpath, mod_file), 'w') as doc_file:
      title_str = '%s Module' % mod_file
      doc_file.write('%s\n%s\n\n' % (title_str, '=' * len(title_str)))
      for member, memclass in inspect.getmembers(mod, inspect.isclass):
        doc_file.write('.. autoclass:: %s\n\t:members:\n\n' % str(memclass).split("'")[1])


if __name__== '__main__':
  parse_folder(initial_path, output_path)
