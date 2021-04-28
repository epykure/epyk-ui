Javascript Interface
====================

The Page object will allow you to write plain JavaScript from the js property.
It will then make available most of the common features defined in the JavaScript world.

No need to move to JavaScript, to edit some extra configuration files or even to write wrappers in Strings, this interface
will provide you autocompletion and links to the underlying web site to learn more about those concepts.

Each component will have a JavaScript entry point which will either redirect to this or will
define a specific one in line with the external package definition. More details
one the component design `a link`_.

.. _a link: report/html

.. toctree::
    :maxdepth: 1

    rst_frgs/js_console
    rst_frgs/js_window
    rst_frgs/js_location


Shortcut and Features
*********************

This will provide common features like:

- math
- navigator
- performance
- web socket
- primitives


Technical Documentation
***********************

The below secion will provide the technical documentation of the base class for JavaScript.

.. autoclass:: epyk.core.js.Js.JsBase
  :members:


.. currentmodule:: epyk.core.html
