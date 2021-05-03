TESLA Shares
============

This is another example of interactive report running without server.

All data are extracted on the Python side and the page will be built based on the data retrieved

This will create the page object and add a predefined configuration to the ``page.body``::

    page = Report()
    page.theme = ThemeBlue.BlueGrey()

Add components to the page::

    from_dt = page.ui.fields.date(value=None, html_code="from_date", label="From")
    to_dt = page.ui.fields.date(value=None, html_code="to_date", label="To")
    button = page.ui.buttons.colored("Update")
    text = page.ui.calendars.pill("1Y", group="chart_time")
    text_6m = page.ui.calendars.pill("6M", group="chart_time")
    text_2m = page.ui.calendars.pill("2M", group="chart_time")
    text_1m = page.ui.calendars.pill("1M", group="chart_time")
    text_all = page.ui.calendars.pill("All", group="chart_time")
    title = page.ui.title("Tesla Share Price")
    buttons = page.ui.div([text, text_6m, text_2m, text_1m, text_all])

    chart = page.ui.charts.chartJs.line([], y_columns=columns, x_axis='Date')

Set some specific ChartJs options::

    chart.options.scales.y_axis().ticks.scale(1000)
    chart.options.scales.y_axis().add_label("Stock Price (USD)")
    chart.options.scales.x_axes().add_label("Date")
    chart.options.tooltips.callbacks.labelCurrency("$")

Load the records on the JavaScript side and create a filter group to be able to apply transformations::

    grp = page.data.js.record(records).filterGroup("aggData")

Add events::

    text.click([from_dt.input.build(text.dom.content), button.dom.events.trigger("click")])
    text_6m.click([from_dt.input.build(text_6m.dom.content), button.dom.events.trigger("click")])
    text_2m.click([from_dt.input.build(text_2m.dom.content), button.dom.events.trigger("click")])
    text_1m.click([from_dt.input.build(text_1m.dom.content), button.dom.events.trigger("click")])
    text_all.click([from_dt.input.build(records[0]["Date"]), chart.build(grp)])

    tag = page.ui.rich.powered()
    tag.style.css.margin_bottom = 5
    tag.style.css.margin_top = 5

    box = page.studio.containers.box()
    box.extend([
      title, from_dt, to_dt, button, page.ui.layouts.hr(margins=5), buttons, chart,
      page.ui.layouts.hr().css({"margin-top": "20px"}), tag])
    box.style.configs.doc(background="white")

    button.click([
      text.dom.classList.select(False),
      text_all.dom.classList.select(False),
      text_2m.dom.classList.select(False),
      text_1m.dom.classList.select(False),
      text_6m.dom.classList.select(False),

Use the group to be able to filter on values defined in the components on the UI::

      chart.build(grp.sup("Date", from_dt.dom.content).inf("Date", to_dt.dom.content).group().sumBy(columns, ['Date']))
        ])


This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/demo_5.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
