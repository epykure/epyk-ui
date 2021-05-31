Jquery UI
==========

- Documentation: https://github.com/jquery/jqueryui.com
- NPM alias: ``jqueryui``
- Package Type: JavaScript

---------------------

This package is a set of UI components which can be used on top of Jquery in order to create input for Dashboards.

DatePicker
**********

To add a data picker::

    import epyk as pk

    page = pk.Page()
    date = page.ui.date()
    page.outs.jupyter(closure=False)

Event
_____

Get the selected value::

    page.ui.button("Get Value").click([
        page.js.alert(date.dom.content)
    ])

Or when it has changed::

    date.select([
        page.js.alert(date.dom.content)
    ])


Slider
**********

To add a slider::

    import epyk as pk

    page = pk.Page()
    page.ui.slider()
    page.outs.jupyter(closure=False)

Event
_____

To get the content when the value has changed::

    slider.change([
        page.js.alert(slider.dom.content)
    ])


Autocompletion
**************

To get toe autocompletion based on an external data source::

    items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})
    selected = page.ui.text()
    items.enter([
        selected.build(items.dom.content)
    ])
    page.js.customFile("FR.js", r"http://pypl.github.io/PYPL")
    page.body.onReady([items.js.source(pk.js_std.var("graphData")[0])])

or from an hard coded source using the component options::

    items = page.ui.inputs.autocomplete(placeholder="select a language and press enter", options={"select": True})
    items.options.source = values


Events
_____

Use components in an external service call::

    page.js.post("url", components=[slider, date]).onSuccess([
        ...
    ])
