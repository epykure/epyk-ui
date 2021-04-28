Welcome to
================================

.. image:: _static/epykIcon.PNG
    :alt: Epyk: HTML/JS Development in Python
    :align: center
    :target: https://github.com/epykure/epyk-ui

Presentation
================================
The target of Epyk is to ensure the implementation of a coherent system using a minimum of layers.
With Epyk the user stays in the Python layer to drive and optimize the data transformation.
This Framework also encourages the implementation of Micro services and cloud based architecture.

Compatibility
================================

Epik is compatible with the most common Web Python Frameworks (Flask and Django).
By default, the server package embeds a Flask app as it is easier to install and ready to use.

The Framework can be included within a :doc:`jupyter/Jupyter` or :doc:`jupyter/JupyterLab` project. But this will lead to some limitations - for example Ajax and Socket will not be available.

Install
=================================

Epyk is an open source package available on pypi::

    pip install epyk


Get Started
=================================

Quick start
***********

The below will illustrate how to start with Epyk and build your first report.
This will write the web artifacts locally::

    import epyk as pk

    page = pk.Page()
    page.ui.text("This is a test")
    page.outs.html()

The best to get more familiar with Epyk is to use PyCharm and the code autocompletion or to start
with examples on the template Github repository: https://github.com/epykure/epyk-templates

CLI Features
************

Epyk comes also with a series of CLI tools to simplify the report create or definition of structures.

.. toctree::
    :maxdepth: 1

    cli.rst


Main categories
***************

In the following sections you will learn how to build complex HTML/JS reports using only python through the followings concepts:

.. toctree::
    :maxdepth: 5
    
    report
    themes
    html_builtins
    css_builtins
    js_builtins
    

Those are the basics of the Epyk framework, then you can move to using complex objects relying on Javascript Libraries such as:

- `D3 <https://d3js.org/>`_
- `ChartJs <https://d3js.org/>`_
- `Tabulator <https://d3js.org/>`_
- `DataTables <https://d3js.org/>`_
- and more, for an exhaustive list of supported libraries and frameworks please see :doc:`supported_ext`


Example
================================

You can find example of what Epyk can do right here:
- `Jupyter Playground <https://nbviewer.jupyter.org/github/epykure/epyk-templates-notebooks/blob/master/tutorials/components/00_components.ipynb>`_

Coming Soon
================================

Please get in touch if there is any feature you feel Epyk-UI needs.


