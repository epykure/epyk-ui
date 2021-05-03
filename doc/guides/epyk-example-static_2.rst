COVID Dashboard
===============


This will create the page object and add a predefined configuration to the ``page.body``::

    page = Report()
    page.theme = ThemeBlue.BlueGrey()

Get the external data from a URL directly::

    data = page.py.requests.csv(data_urls.COUNTRY_WISE_COVID)

Add components to the page::

    title = page.ui.title("Country wise COVID")
    button_all = page.ui.button("All")
    button_all.style.css.margin_top = 5
    button_clear = page.ui.button("Clear")

Change the CSS style of the button::

    button_clear.style.css.margin_top = 5
    button_clear.style.css.margin_left = 5

    cols_keys = page.ui.panels.filters(html_code="data_filters", options={"max_height": 90})
    cols_keys.style.css.min_height = 20

Add a autocomplete input component and set an event when enter is pressed::

    items = page.ui.inputs.autocomplete(placeholder="select a country", options={"select": True})
    items.enter([cols_keys.dom.add(items.dom.content, category='Country/Region'), items.dom.empty()])

    button = page.ui.button("Show")
    button.style.css.margin_top = 5

Add component specific options, in this case it is an event when selected::

    items.options.on_select([
      cols_keys.dom.add(events.value, category='Country/Region'),
      button.dom.events.trigger("click")
    ])

Add other components to the page::

    bar = page.ui.charts.chartJs.bar([], ['Confirmed', 'Deaths', 'Recovered'], 'Country/Region')
    bar.options.scales.y_axis().ticks.toNumber()

    ref = page.ui.texts.references.website(author="rsharankumar", name="Learn Data Science in 100Days", site="github",
                                           url="https://github.com/rsharankumar/Learn_Data_Science_in_100Days")

    box = page.studio.containers.box()
    box.extend([title, items, page.ui.div([button_all, button_clear]), cols_keys, button, bar, ref])
    box.style.standard()

    grp = page.data.js.record(std.var("covidData", global_scope=True)).filterGroup("aggData")

Add events on the button and button_all object ::

    button.click([
      page.js.console.log(cols_keys.dom.content),
      bar.build(grp.match(cols_keys.dom.content).group().sumBy(['Confirmed', 'Deaths', 'Recovered'], ['Country/Region']))
    ])

    countries = set()
    for rec in data:
      countries.add(rec['Country/Region'])

    button_all.click([
      cols_keys.dom.clear(), cols_keys.dom.add(list(countries), category='Country/Region', no_duplicate=False)])
    button_clear.click([cols_keys.dom.clear()])

This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/demo_4.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
