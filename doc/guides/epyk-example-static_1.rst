Language comparison
===================

The below line to create a new web page::

    page = pk.Page()
    page.headers.dev()
    page.theme = ThemeBlue.BlueGrey()


This will add an external JavaScript page online::

    page.js.customFile("FR.js", r"http://pypl.github.io/PYPL")


Add two components::

    title = page.ui.title("PYPL PopularitY of Programming Language")
    items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})
    cols_keys = page.ui.lists.drop(html_code="cols_agg_keys")

Change the slyde and add event to the list object::

    cols_keys.style.css.min_height = 20
    cols_keys.items_style(style="bullets")
    cols_keys.drop()

    button = page.ui.buttons.colored("Display")
    button.style.css.margin_top = 5

    items.options.on_select([
      cols_keys.dom.add(events.value),
      button.dom.events.trigger("click")
    ])

Add the chart component and change the style::

    line = page.ui.charts.chartJs.line(x_axis="Date", profile=True)
    line.options.scales.x_axes().type = "time"
    line.options.elements.point.radius = 0
    line.options.scales.x_axes().distribution = 'linear'

Add a powered component to illustrate the external modules used from Epykt::

    tag = page.ui.rich.powered()
    tag.style.css.margin_bottom = 5
    tag.style.css.margin_top = 5

    box = page.studio.containers.box()
    box.extend([title, tag, items, cols_keys, button, line])
    box.style.standard()

Add extra events to the components::

    items.enter([cols_keys.dom.add(items.dom.content), items.dom.empty()])

    button.click([
      std.var("graphData").fromArrayToRecord().setVar("records"),
      line.build(std.var("records"), options={"y_columns": cols_keys.dom.content, "x_axis": "Date"})
    ])

Run some functions when the page is loaded in the browser::

    page.body.onReady([items.js.source(std.var("graphData")[0])])

This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/demo_1.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
