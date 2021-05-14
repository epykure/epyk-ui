Ready to use examples
=====================

This section will details some examples available on `Github <https://github.com/epykure/epyk-templates>`_

It will illustrate some example and provide more explanation concerning the modules and functions used.

More ready to use dashboards are available in the `Epyk Gallery <https://epykure.github.io/demos/>`_

Important features
__________________

Only **12** functions are needed to be able to write interactive dashboards.

.. list-table:: Epyk common features
   :widths: 10 20 70
   :header-rows: 1

   * - Scope
     - Function
     - Description
   * - Page
     - theme
     - Change theme of the page
   * - Page
     - theme.colors
     - Get the theme colors
   * - Page
     - ui
     - Get all the components in the framework
   * - Page
     - body
     - Get the body (main component) of the page on which components will be attached to.
   * - Page
     - js
     - Get access to the JavaScript standard features
   * - Page
     - js.post / js.get
     - Call a backend REST API
   * - Page
     - outs
     - Page output property (html, codepen, Jupyter....)
   * - Component
     - style.css
     - Get all the CSS properties
   * - Component
     - js
     - Get the component specific js features
   * - Component
     - dom.content
     - Get the component value on the UI side
   * - Component
     - click
     - Add UI click event on the component
   * - Component
     - build
     - Update a component in a UI event function


.. note:: This is a collaborative framework so not hesitate to share your work to add more examples to this list.


Epyk for beginners
____________________

This should a easy start for people not really familiar with either Python or JavaScript but eager to learn and produce results
quickly (without to deal with thousand of packages, technologies and concepts).

The below links will propose two approaches according to your appetite:

.. raw:: html

    <ul>
        <li><a href="../guides/beginner-py.html">Python beginner</a></li>
        <li><a href="../guides/beginner-js.html">JavaScript beginner</a></li>
        <li><a href="../guides/cheatsheet.html">Epyk cheatsheet</a></li>
    </ul>


Statics Page
_______________

Those examples are interactive pages working as standalone HTML pages. No server is required to run them.

This is usually the starting point of any web pages.

.. toctree::
    :maxdepth: 1

    /../guides/epyk-example-static_1.rst
    /../guides/epyk-example-static_2.rst
    /../guides/epyk-example-static_3.rst
    /../guides/epyk-example-static_4.rst
    /../guides/epyk-example-static_5.rst

Web server integration
_______________________

Flask
*****

.. toctree::
    :maxdepth: 1

    /../guides/epyk-example-demo_1.rst
    /../guides/epyk-example-demo_2.rst


Fast API
********

.. toctree::
    :maxdepth: 1

    /../guides/epyk-example-demo_3.rst
    /../guides/epyk-example-demo_4.rst
    /../guides/epyk-example-demo_5.rst
