Simple Workflow
===============

This is a more complex example illustrating how to use workflow components and tabs in a page.

This will create the page object and add a predefined configuration to the body::

  page = pk.Page()
  page.body.template.style.configs.doc(background="white")

Add a stepper component and put it in a container for the display::

  stepper = page.ui.steppers.arrow([
    {"value": 'test 1', "status": 'pending', 'label': 'test'},
    {"value": 'test 2'},
    {"value": 'test 3', "status": 'waiting'}],
    options={"media": False, "line": False})
  page.ui.div(stepper, align="center")

Attach to this component a JavaScript event. This will only display a JavaScript standard alert::

  stepper[1].click([
    page.js.alert("This ")
  ])


.. note:: Components and event can be added anywhere in the page. The page.components variable will keep the order when it will transpile the script.

Add a tabs and button components::

  tabs = page.ui.panels.tabs()
  tabs.add_panel("Status 1", "Description for status 1", selected=True)
  tabs.add_panel("Status 2", "Description for status 2")
  tabs.add_panel("Status 3", "Description for status 3")

  btn1 = page.ui.button("Previous", icon="fas fa-caret-left")
  btn1.style.css.padding_h = 5

Add a click event to the button::

  btn1.click([
    stepper.dom[pk.std.var("state")].arrow(),
    stepper.dom[pk.std.var("state")].waiting(),
    stepper.dom[pk.std.var("state")].text("Waiting", color="black"),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid white", "padding-bottom": "5px"}),
    pk.std.var("state", pk.std.maths.max(pk.std.parseInt(pk.std.var("state")) - 1, 0), global_scope=True),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid green", "padding-bottom": "5px"}),
    stepper.dom[pk.std.var("state")].circle(),
    stepper.dom[pk.std.var("state")].pending(),
    stepper.dom[pk.std.var("state")].text("Pending", color="black"),
    tabs.dom[pk.std.var("state")].select(),
  ])

  btn2 = page.ui.button("Next", icon="fas fa-caret-right")
  btn2.style.css.padding_h = 5
  btn2.click([

Use the DOM and JS properties in the click events since this will be run by the browser once the code will be transpiled
to JavaScript. Python will only perform some sanity checks on the pre defined features::

    stepper.dom[pk.std.var("state")].success(),
    stepper.dom[pk.std.var("state")].arrow(),
    stepper.dom[pk.std.var("state")].text("Completed", color="black"),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid white", "padding-bottom": "5px"}),
    pk.std.var("state", pk.std.maths.min(pk.std.parseInt(pk.std.var("state")) + 1, 2), global_scope=True),
    stepper.dom[pk.std.var("state")].css({"border-bottom": "1px solid green", "padding-bottom": "5px"}),
    stepper.dom[pk.std.var("state")].circle(),
    stepper.dom[pk.std.var("state")].pending(),
    stepper.dom[pk.std.var("state")].text("Pending", color="black"),
    tabs.dom[pk.std.var("state")].select(),
    page.js.console.log(tabs.dom[pk.std.var("state")].innerText())
  ])

Create a variable when the browser will load the page::

  page.body.onReady([
    pk.std.var("state", 0, global_scope=True)
  ])

This example is available `here <https://github.com/epykure/epyk-templates/blob/master/tutos/onepy/flask_steppers.py>`_

More example of the templates on `Github <https://github.com/epykure/epyk-templates>`_
