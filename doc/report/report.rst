Page
====================

This class is your your main entry point to the epyk framework, this is where you'll be able to access
UI components through the :doc:`report/ui` interfaces or the :doc:`report/js` features.
It takes care of writing the `body <https://www.w3schools.com/tags/tag_body.asp>`_ section of your html page and also populating the `style <https://www.w3schools.com/tags/tag_style.asp>`_ and `scripts <https://www.w3schools.com/tags/tag_script.asp>`_ parts.

The below 2 lines of codes will show how to create a page object::

    import epyk as pk

    page  = pk.Page()


There are 6 main interfaces available through this object which will enable you to build a complete HTML page:

- :doc:`ui`
- :doc:`components`
- :doc:`js`
- :doc:`outs`
- :doc:`py`
- :doc:`data`
- :doc:`web`

.. toctree::
    :maxdepth: 5
    :hidden:
    
    ui
    html_components
    js
    outs
    py
    data
    web

Example
*******

::

    import epyk as pk

    page = pk.Page()
    page.ui.title("This is a title")
    paragraph = page.ui.texts.paragraph("This is a paragraph")
    paragraph.click([
        page.js.console("This is a log on the JavaScript side")
    ])
    page.outs.html()


Technical Documentation
***********************

.. autoclass:: epyk.core.Page.Report
    :members: