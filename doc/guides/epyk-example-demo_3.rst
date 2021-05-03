Log Viewer
==========



This will create the page object and add a predefined configuration to the ``page.body``::

      page = pk.Page()
      template = page.body.add_template(defined_style="margins")
      template.style.css.background = "white"

Add a date object::

      dt = page.ui.texts.date("Y-0", html_code='date_from', width=(100, "%"))

Create a navbar with components::

      page.ui.navigation.shortcut([
        page.ui.layouts.hr(),
        page.ui.titles.title("Dates"),
        page.ui.titles.bold("From:", align="left"),
        dt,
        page.ui.titles.bold("To:", align="left"),
        page.ui.texts.date(html_code='date_to', width=(100, "%"), options={"date_from_js": "COB"}),
        page.ui.layouts.hr(),
        page.ui.titles.title("Actions"),

Use ``html_Code`` on the components in order to get this alias when they are passed to services::

      page.ui.input("GS", html_code="input"),
      page.ui.buttons.refresh("Load", html_code="button"),
      page.ui.icons.date(),
      page.ui.div([
        page.ui.icons.awesome("far fa-file-pdf", width=15),
        page.ui.icons.awesome("fas fa-at", width=15),
      ]).css({"bottom": '10px', 'position': 'absolute', 'display': 'block'})
      ], size=(100, 'px'), options={"position": 'left'})

      page.body.style.css.margin_left = 10
      content = ""
      title = page.ui.title(content, options={"markdown": True})
      table = page.ui.tables.tabulators.figures(
        rows=["Date", "Name"], cols=["Low", "High", 'Open', 'Close', 'Volume', 'Adj Close'])

      footer = page.ui.navigation.footer('@Data from pandas_datareader using yahoo as source.')

Create a ``click`` event on the page by finding the component from the ``page.components`` dictionary based on it ``html_code``::

      page.components['button'].click([
        page.components["button"].icon.dom.spin(True),

Define an AJAX post to an underlying service::

        page.js.post("/viewer", {"button": 'Data 1'}, components=[page.components["input"],

Update the components::

      page.components['date_from'], page.components['date_to']]).onSuccess([
      title.build(pk.events.data["title"]),
      table.build(pk.events.data["table"]),
      page.components["button"].icon.dom.spin(False)
        ]),
      ])
      page.components["input"].enter([page.components['button'].dom.events.trigger("click")])
      footer.style.css.padding_left = 110

This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_viewer.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
