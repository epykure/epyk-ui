
import os
import sys

file_path = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(file_path, '..', '..'))

from epyk.core.js import Imports

import_frgs, count_libs = [], 1
for k, v in Imports.JS_IMPORTS.items():
  import_frgs.append("- %s, version %s, %s" % (k, v.get("version", ""), v.get("website", "")))
  count_libs += 1

with open(os.path.join(os.path.dirname(__file__), "..", 'supported_ext.rst'), "w") as fp:
  fp.write('''
Supported Libraries and Frameworks
==================================

A toolbox to multiple external libraries. Epyk will interface with the most popular JavaScript and Css libraries from 
the vast number of components.


%s Libraries
============

%s

Framework
==========

Import Manager
**************

The import Manager is one of the entry point directly accessible from Epyk.

.. autoclass:: epyk.core.js.Imports.ImportManager
  :members:

''' % (count_libs, "\n".join(import_frgs)))


with open(os.path.join(os.path.dirname(__file__), "..", 'css_builtins.rst'), "w") as fp:
  fp.write('''
CSS Built-Ins
=============

- CSS Properties.
- CSS Classes (Catalog).
- Effects.
- Themes.


Core Modules
*************

CSS Class
---------

.. autoclass:: epyk.core.css.styles.GrpCls.ClassPage
  :members:

CSS Style
---------

.. autoclass:: epyk.core.css.styles.classes.CssStyle.Style
  :members:
  
Colors
------

.. autoclass:: epyk.core.css.Colors.HexColors
  :members:
  
''')
