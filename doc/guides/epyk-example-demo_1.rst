Show case report
================

This is the demo page available from the below command line::

    epyk.exe demo
    epyk.exe transpile

Python script will have the below sections.

This will create the page object and add a predefined configuration to the ``page.body``::

    page = pk.Page()
    page.headers.dev()
    page.body.template.style.configs.doc(background="white")

Add the 3 components to the page (they will be automatically added to the body)::

    table = page.ui.table(mocks.popularity_2020)
    table.options.paginationSize = 10

    toggle = page.ui.toggle({"on": "Trend", "off": "Share"})
    bar = page.ui.charts.bar(mocks.popularity_2020, y_columns=["Share"], x_axis="Language")

Create a JavaScript click event on the toggle component::

    toggle.click([
      # Store the variable to myData on the JavaScript side

Then use the standard library in order to use core JavaScript features like:
- Creating / updating a variable::

      pk.std.var("myData", sorted(mocks.popularity_2020, key=lambda k: k['Language'])),
      # Use the standard build and dom.content to respectively update and get the component value

- Defining a if / else statement::

      pk.expr.if_(toggle.input.dom.content.toStr(), [
        # Use the variable to update the chart
        bar.build(pk.std.var("myData"), options={"y_columns": ["Trend"]})
      ]).else_([
        bar.build(pk.std.var("myData"), options={"y_columns": ["Share"]})
      ])
    ])

The examples using a Flask app is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/flask_demo.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
