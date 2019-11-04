"""
Wrapper to the predefined Forms

Documentation
https://www.w3schools.com/html/html_forms.asp
"""

from epyk.core.html import Html

# The list of CSS classes
from epyk.core.css.groups import CssGrpCls


class Row(object):
  input, button, label = None, None, None

  def __init__(self):
    self.attrs = []

  def attr(self, name, obj):
    """
    Add simple components to the rows.
    Not all the components can be added to the forms

    :param name: The name of the component in the row
    :param obj: The HTML component

    :return:
    """
    self.attrs.append(name)
    setattr(self, name, obj)
    return self

  def toStr(self):
    pass


class Form(Html.Html):
  name, category, callFnc = 'Generic Form', 'Forms', 'form'
  _grpCls = CssGrpCls.CssGrpClassBase

  def __init__(self, report, action, method, helper):
    super(Form, self).__init__(report, None)
    self.rows = []
    self.css({"padding": '5px'})
    self.attr.update({"action": action, "method": method})
    self.add_helper(helper)

  def row(self, i=None):
    """
    Returns the current row

    :rtype: Row
    """
    if i is None:
      return self.rows[-1]

    return self.rows[i]

  def add_input(self, text, name, label=None, css=None, attrs=None, position="after", row=None):
    """
    Add an elementary input component

    Example

    :param text: The title content
    :param name: The component name in the form (used as ID)
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param attrs: Optional
    :param position:
    :param row:

    """
    if css is None:
      css = {"width": '200px', 'vertical-align': 'top', 'margin': '0 4px'}
    if row is None:
      row = self.add_row()
    if label is not None:
      self.add_label(label, row=row)
    if text is not None:
      row.attr("input", self._report.ui.inputs.input(text))
      if position == "before":
        self.prepend_child(row.input)
      else:
        self.append_child(row.input)
      if css is not None:
        row.input.css(css)
      if attrs is not None:
        row.input.set_attrs(attrs=attrs)
    return self

  def add_label(self, text, css=None, position="after", for_=None, row=None):
    """
    Add an elementary label component

    Example

    Documentation
    https://www.w3schools.com/tags/tag_label.asp

    :param text: The label content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param for_: Specifies which form element a label is bound to
    :param row:

    """
    if row is None:
      row = self.add_row()
    if text is not None:
      row.attr("label", self._report.ui.texts.label(text))
      if for_ is not None:
        # Attach the label to another HTML component based on the ID
        row.label.attr['for'] = for_
      if position == "before":
        self.prepend_child(row.label)
      else:
        self.append_child(row.label)
      if css is not None:
        row.label.css(css)
    return self

  def add_button(self, text, css=None, position="after", row=None, attrs=None):
    """
    Add an elementary label component

    Example

    Documentation
    https://www.w3schools.com/tags/tag_label.asp

    :param text: The label content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param row:

    """
    if row is None:
      row = self.add_row()
    if text is not None:
      row.attr("button", self._report.ui.button(text))
      if position == "before":
        self.prepend_child(row.button)
      else:
        self.append_child(row.button)
      if css is not None:
        row.button.css(css)
      if attrs is not None:
        row.button.set_attrs(attrs=attrs)
    return self

  def add_title(self, text, css=None, position="after", row=None):
    """
    Add an elementary title component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param row:

    """
    if row is None:
      row = self.add_row()
    if text is not None:
      row.attr("title", self._report.ui.texts.title(text))
      if position == "before":
        self.prepend_child(row.title)
      else:
        self.append_child(row.title)
      if css is not None:
        row.title.css(css)
    return self

  def add_date(self, text, css=None, position="after", row=None):
    """
    Add an elementary date component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param row:

    """
    if row is None:
      row = self.add_row()
    if text is not None:
      row.attr("date", self._report.ui.dates.cob(label=text))
      if position == "before":
        self.prepend_child(row.date)
      else:
        self.append_child(row.date)
      if css is not None:
        row.date.css(css)
    return self

  def add_text(self, text, name, css=None, position="after", row=None):
    """
    Add an elementary textarea component

    :param text:
    :param name: The component name in the form (used as ID)
    :param css:
    :param position:
    :param row:

    :return:
    """
    if row is None:
      row = self.add_row()
    if text is not None:
      row.attr("text", self._report.ui.inputs.textarea(text))
      if position == "before":
        self.prepend_child(row.text)
      else:
        self.append_child(row.text)
      if css is not None:
        row.text.css(css)
    return self

  def add_row(self):
    """
    Add a row to the form
    """
    new_row = Row()
    self.rows.append(new_row)
    return new_row

  def __str__(self):
    self.add_button("Run", css={"margin": 0}, attrs={"type": 'submit', "value": "Submit"})
    return '<form %s></form>%s' % (self.get_attrs(pyClassNames=self.defined), self.helper)
