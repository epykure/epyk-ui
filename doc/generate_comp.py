import os
import importlib, inspect

import sys
sys.path.append(r'C:\Users\nelso\PycharmProjects\epyk-ui')

output_path = r'C:\Users\nelso\PycharmProjects\epyk-ui\doc\report\ui'

for fol in ['components', 'geo', 'graphs', 'tables']:
  for f in os.listdir(os.path.join(r'C:\Users\nelso\PycharmProjects\epyk-ui\epyk\interfaces', fol)):
    if f.startswith('__'):
      continue
      
    os.makedirs(os.path.join(output_path, fol), exist_ok=True)
    mod_file = f.replace('.py', '')
    mod = importlib.import_module("epyk.interfaces.%s.%s" % (fol, mod_file))
    for member, memclass in inspect.getmembers(mod, inspect.isclass):
      with open(r'%s\%s\%s.rst' % (output_path, fol, member), 'w') as doc_file:
        title_str = '%s Interface' % member
        doc_file.write('%s\n%s\n\n' % (title_str, '=' * len(title_str)))
        doc_file.write('.. autoclass:: %s\n\t:members:' % str(memclass).split("'")[1])


