Security and Control
====================

External libraries
*******************************

It is possible to restrict the list of packages or even to update / extend it.
Those packages have be tested to work with a dedicated version but it is quite easy to check if the latest version will
not put any regression to your page.


Restrict the scope
__________________


Change versions
_______________


Add packages
____________

Adding a new package means creating a new component.
It is very easy to add a new package by just using the importManager.



Google extensions
*****************

As google extensions are used to collect the information by default components using those modules are blocked.
It will require a specific line of code in order to enable them otherwise the transpilation will raise an error::

    # Enable Google Maps

    # By default all Google products are disabled
    page.imports.google_products(['maps'])

    map = page.ui.geo.google.terrain(-33.92, 151.25)

    # Click event to add interactivity on the page
    page.ui.button("Click").click([
      map.js.setMapTypeId('satellite'),
      map.js.setHeading(45),
    ])

