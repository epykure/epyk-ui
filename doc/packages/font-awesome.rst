Font awesome
============

- Documentation: https://fontawesome.com/
- NPM alias: ``font-awesome``
- Package Type: JavaScript

---------------------

The package ``Font-Awesome`` is available in the framework by using the following component.
It is the default package used for the various icons in the framework::

    import epyk as pk
    from epyk.core.js.packages import JsFontAwesome

    page = pk.Page()
    icon = page.ui.icons.next()
    icon.click([
            page.js.alert("This is a test")
    ])

    icon = page.ui.icon("fab fa-python")
    icon.pulse()

    icon = page.ui.icon(JsFontAwesome.ICON_CARET_SQUARE_O_UP)

It is possible to use the module JsFontAwesome to get all the available icons on the IDE using the autocompletion.

Events
******

All the component events are available from the component ``.js`` property.
Basically by adding the below it will open the tree up to n level::

    icon = page.ui.icons.next()
    icon.click([page.js.alert("ok")])

.. note::
    The js property must be added to a JavaScript event to be rendered as string to the page during the transpiling.
    Any functions called directly from Python will rendered string which will not be captured in the page object.

Style
*****

This component will have some predefined CSS class in order to change the nav bar and the button but it is possible
as any other component to change the style by using the ``style.css`` property.

The below will add a border to the component::

    icon.style.css.color = "1px solid black"
