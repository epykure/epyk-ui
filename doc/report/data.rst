Data Interface
==============

Data is key for Visualisation so this is why Epyk provides ways to retrieve / connect the data.

Data Transformers
*****************

Those will transform the data to fit the format expected by the various containers.
Basically this is the format expected in the HTML components in the **__init__** or in the **build** method.

Those functions can be used from the page object from **page.data** or directly from the module by using **pk.**

This module should be moved to a dedicated package in future releases to make the use on the backend side lighter.

.. automodule:: epyk.core.data.DataPy
  :members: