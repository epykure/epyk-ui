Json Formatter
==============

- Documentation: https://github.com/mohsen1/json-formatter-js
- NPM alias: ``json-formatter-js``
- Package Type: JavaScript


---------------------


The package json-formatter-js is available in the framework by using the following component::

    js_formatter = page.ui.json({"foo": 42})

The above will display a tree object as shown here. https://azimi.me/json-formatter-js/

Each of the functions and properties, when they are wrapping an core API function, will point from the doc string in the framework to its external documentation.
Do not hesitate to have a look at it and either to challenge the library to get new features or to check with us if something does not seem correct.

Options
*******

Then exactly in the same way it is mentioned in the documentation it is possible to add options to this
component from the Python. All the options are available from the ``component.options`` property::

    js_formatter.options.hoverPreviewEnabled = False


Events
******

All the component events are available from the component ``.js`` property.
Basically by adding the below it will open the tree up to n level::

    btn = page.ui.button("Click")
    btn.click([
        js_formatter.js.openAtDepth(3)
    ])

.. note::
    The js property must be added to a JavaScript event to be rendered as string to the page during the transpiling.
    Any functions called directly from Python will rendered string which will not be captured in the page object.

Style
*****

This component will have some predefined CSS class in order to change the nav bar and the button but it is possible
as any other component to change the style by using the ``style.css`` property.

The below will add a border to the component::

    js_formatter.style.css.border = "1px solid black"


