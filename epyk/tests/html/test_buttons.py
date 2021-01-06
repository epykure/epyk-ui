
from epyk.core.Page import Report


def test_button_tags():
  """
  Test the default CSS classname for the component.
  """
  page = Report()
  div = page.ui.buttons.check()
  assert(div.attr["class"][0].classname == "cssdivnoborder")


def test_button_attributes():
  """
  Check if a change on the CSS style is correctly added to the final HTML object definition.
  """
  page = Report()
  div = page.ui.button("Click Me")
  div.style.css.color = "green"
  assert("color:green" in str(div))


def test_button_value():
  """
  Check if the value is correctly defined in the val property.
  """
  page = Report()
  div = page.ui.button("Click Me")
  assert(div.val == ["Click Me"])


def test_button_no_background():
  """
  Check the change to a transparent background.
  """
  page = Report()
  div = page.ui.button("Click Me")
  div.no_background()
  assert("background-color:#11ffee00" in str(div))


def test_button_disable():
  """

  """
  page = Report()
  div = page.ui.button("Click Me")
  div.disable()
  assert(' disabled="True" ' in str(div))


def test_button_dom():
  """

  """
  page = Report()
  div = page.ui.button("Click Me", htmlCode="button")
  assert("document.getElementById('button').innerHTML" == div.dom.content.toStr())


def test_button_goto():
  """

  """
  page = Report()
  but = page.ui.button("Click Me")
  but.goto("http://www.epyk-studio.com")
  return but


def test_button_properties():
  """

  """
  page = Report()
  but = page.ui.button("Click Me")
  but.goto("http://www.epyk-studio.com")
  return but.properties()


def test_button_requirements():
  """
  Check the button external requirements.
  """
  page = Report()
  but = page.ui.button("Click Me")
  assert(but.require.js == {})


def test_button_groups():
  """
  Check if the group is added to the buttons.
  """
  page = Report()
  but = page.ui.button("Click Me")
  but.options.group = "Group"
  but2 = page.ui.button("Click Me")
  but2.options.group = "Group"
  assert(but2.attr["name"] == but.attr["name"])


def test_checkbox_requirements():
  """
  Check the button external requirements.
  """
  page = Report()
  but = page.ui.buttons.checkboxes()
  assert(len(but.require.js) == 3)
  assert(but.require.js["bootstrap"] == '*')


def test_checkbox_tooltip():
  """

  """
  page = Report()
  but = page.ui.buttons.checkboxes("Click Me")
  but.tooltip("Tooltip message")
  return but


print(test_checkbox_requirements())
