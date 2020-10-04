
from epyk.web.components.angular.assets import asset


class AssetClr(asset.Asset):
  pass


class Acordeon(AssetClr):
  name = 'clr-accordeon'

  def __str__(self):
    return '''
<clr-accordion>
  <clr-accordion-panel>
    <clr-accordion-title>Item 1</clr-accordion-title>
    <clr-accordion-content *clrIfExpanded>Content 1</clr-accordion-content>
  </clr-accordion-panel>
</clr-accordion>
'''


class Panel(AssetClr):
  pass


class Alert(AssetClr):
  pass


class Badge(AssetClr):
  pass


class Button(AssetClr):
  pass


class ButtonGroup(AssetClr):
  pass


class Checkbox(AssetClr):
  pass


class DataList(AssetClr):
  pass


class DatePicker(AssetClr):
  pass


class Dropdown(AssetClr):
  pass


class Radio(AssetClr):
  pass


class ProgressBar(AssetClr):
  pass


class Range(AssetClr):
  pass


class Select(AssetClr):
  pass


class SignPost(AssetClr):
  pass


class StackView(AssetClr):
  pass


class Timeline(AssetClr):
  pass
