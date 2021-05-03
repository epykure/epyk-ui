Advanced Documentation viewer
=============================

This example is a bit more sophisticated as it will use a FAST Api server and a database in order to
store version of the documentation.

Database structure will be defined when the server will start.

First create the page object::

  page = pk.Page()

Create a bespoke CSS inline object::

  css = pk.CssInline()
  css.margin_bottom = 5
  css.margin_left = 5
  css.important(["margin_bottom", "margin_left"])

Create an autocomplete input components and change some options::

  autocomp = page.ui.inputs.autocomplete(placeholder="script name", html_code="name", options={"borders": "bottom"})
  autocomp.options.select = True
  version = page.ui.select(width=(100, 'px'), html_code="selected_version")

Add the CSS object to this components with a specific name::

  version.attr["class"].add(css.to_class("cssTestClass"))
  version.options.noneSelectedText = "None"

Add components to the page::

  button = page.ui.buttons.colored("Load")
  button.style.css.margin_left = 10
  page.ui.navbar(components=[autocomp, version, button])
  script = page.ui.text("script name", html_code="script")
  script.options.editable = True
  script.style.css.bold()
  pkg_version = page.ui.text("Version")
  pkg_number = page.ui.text("0.0.0", html_code="version")

Change css styles and options::

  pkg_number.options.editable = True
  pkg_number.style.css.margin_left = 10
  v = page.ui.div([pkg_version, pkg_number], width="auto")
  v.style.css.float = "right"
  v.style.css.display = "inline-block"

Add icon components::

  i1 = page.ui.icon("fas fa-edit")
  i2 = page.ui.icon("fas fa-lock")
  i3 = page.ui.icon("fas fa-save")
  actions = page.ui.div([i1, i2, i3], width=(20, 'px'))

Add CSS style properties using ``actions.style.css``::

  actions.style.css.position = "absolute"
  actions.style.css.top = 60
  actions.style.css.right = 0
  actions.style.css.padding_left = "3px"
  actions.style.css.border_radius = "5px 0 0 5px"
  actions.style.css.background = page.theme.greys[3]

  header = page.ui.div([script, v])
  header.style.css.background = page.theme.greys[2]
  header.style.css.display = "block"
  header.style.css.padding_h = 15

  title = page.ui.title("Documentation Viewer", html_code="title")
  title.options.editable = True
  content = page.ui.rich.markdown(__doc__, html_code="content")
  content.options.editable = True

  banner = page.ui.text("Editable", width=(75, 'px'))
  banner.style.css.background = page.theme.success[1]
  banner.style.css.border_radius = "0 0 20px 0"
  banner.style.css.padding_h = 10
  banner.style.css.font_factor(-2)
  banner.style.css.color = page.theme.greys[-1]
  banner.style.css.position = "absolute"
  banner.style.css.bold()
  banner.style.css.top = 0
  banner.style.css.left = 0

  container = page.ui.div([banner, header, title, content, actions])
  container.style.configs.doc(background="white")
  container.style.css.position = "relative"
  container.style.css.padding_top = 30

  updt = page.ui.rich.update(align="right", html_code="last_update")
  updt.style.css.italic()
  updt.style.css.font_factor(-2)
  container.add(updt)

Add events to the components::

  i3.click([

Call an underlying service in the FAST API server::

    page.js.post("/save", components=[banner, script, pkg_number, title, content, updt]).onSuccess([
      page.js.msg.status(),
      updt.refresh()
    ])])

Add click event on to the first icon::

  i1.click([

Change the dom properties using the common JavaScript features ``dom.setAttribute``::

    script.dom.setAttribute("contenteditable", True).r,
    pkg_number.dom.setAttribute("contenteditable", True).r,
    title.dom.setAttribute("contenteditable", True).r,
    content.dom.setAttribute("contenteditable", True).r,

Display a temporary message in the page::

    page.js.msg.text("Components editable"),

Update the banner component::

    banner.build("Editable"),
    banner.dom.css({"background": page.theme.success[1], "color": page.theme.greys[-1]})
    ])

In the same way click events are added on the other components::

  i2.click([
    script.dom.setAttribute("contenteditable", False).r,
    pkg_number.dom.setAttribute("contenteditable", False).r,
    title.dom.setAttribute("contenteditable", False).r,
    content.dom.setAttribute("contenteditable", False).r,
    page.js.msg.text("Components locked"),
    banner.build("Locked"),
    banner.dom.css({"background": page.theme.colors[-1], "color": page.theme.greys[0]})
  ])

  autocomp.enter([
    page.js.post("/versions", components=[autocomp]).onSuccess([
      version.build(pk.events.data["versions"]),
      version.js.val(pk.events.data["selected"]),
      version.js.refresh(),
      page.js.msg.status()
    ])
  ])

  button.click([
    page.js.post("/details", components=[autocomp, version]).onSuccess([
      title.build(pk.events.data["title"]),
      content.build(pk.events.data["content"]),
      script.build(pk.events.data["script"]),
      pkg_number.build(pk.events.data["number"]),
      updt.build(pk.events.data["last_date"]),
    ])
  ])

Add an ``body.onReady`` to load the autocompletion when the page is ready::

  page.body.onReady([
    page.js.post("/templates").onSuccess([
      autocomp.js.source(pk.events.data["values"])
    ])
  ])


This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/fastapi_db.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
