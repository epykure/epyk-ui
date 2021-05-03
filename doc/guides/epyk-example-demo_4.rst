Webscraping
===========

This will focus on the UI section of the template used to get data from an external website.

This will create the page object and add a predefined configuration to the ``page.body``::

  page = pk.Page()
  page.body.template.style.configs.margins()

Add a QR Code component with the link of the example::

  qrcode = page.ui.qrcode("https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_webscraping.py")
  qrcode.style.css.fixed(bottom=60, right=70)
  qrcode.style.css.cursor = "pointer"
  qrcode.style.css.z_index = 300

Add date components and change the CSS properties::

  dt_from = page.ui.date(html_code='from', width=(120, "px"))
  dt_from.input.style.css.margin_bottom = 10
  dt_to = page.ui.date("2021-05-15", html_code='to', width=(120, "px"))
  dt_to.input.style.css.margin_bottom = 10

Add a button component and change the CSS properties::

  prices = page.ui.button("Get Prices", icon="fab fa-python")
  prices.style.css.padding_left = 10
  prices.style.css.padding_right = 10
  prices.style.css.color = page.theme.colors[-1]

Create a navbar and attach the components to it::

  bar = page.ui.navbar()
  bar.style.css.background = page.theme.colors[-1]
  bar.style.css.color = "white"
  bar.add(dt_from)
  bar.add(dt_to)
  bar.add(prices)

  page.ui.title("Eurostar average prices")
  line = page.ui.charts.chartJs.line(y_columns=['standard', 'premier', 'business'], x_axis='full_date')
  bar = page.ui.charts.chartJs.bar(y_columns=['average'], x_axis='category')
  row = page.ui.row([line, bar])
  row.set_size_cols(8)

Create a event when button is clicked::

  prices.click([
    prices.icon.dom.spin(True),

Link this example to an entry point on the server::

    page.js.post("/web_scrapping", components=[dt_from, dt_to]).onSuccess([
      line.build(pk.events.data["prices"]),
      bar.build(pk.events.data["average"]),
      prices.icon.dom.spin(False)
    ])
  ])

This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_webscraping.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
