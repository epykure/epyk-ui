"""
Wrapper to the predefined Forms

Documentation
https://www.w3schools.com/html/html_forms.asp
"""

from epyk.core.html import Html


class Row(object):

  def __init__(self):
    self.attrs = []

  def attr(self, name, obj):
    """

    :param name:
    :param obj:

    :return:
    """
    self.attrs.append(name)
    setattr(self, name, obj)
    return self

  def toStr(self):
    print(self.attrs)


class Form(Html.Html):
  name, category, callFnc = 'Generic Form', 'Forms', 'form'
  __pyStyle = ['CssDivNoBorder']

  def __init__(self, report, action, method, helper):
    super(Form, self).__init__(report, None)
    self.rows = []
    self.attr["action"] = action
    self.attr["method"] = method
    self.add_helper(helper)

  def add_input(self, text, label=None, css=None, attrs=None, position="before", row=None):
    """
    Add an elementary input component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param attrs: Optional
    :param position:
    :param row:

    """
    if row is None:
      row = self.add_row([])
    if text is not None:
      row.attr("input", self._report.ui.inputs.input(text))
      if position == "before":
        self.prepend_child(row.input)
      else:
        self.append_child(row.input)
      if css is not None:
        row.input.css(css)
      if attrs is not None:
        row.input.add_attrs(attrs)
    if label is not None:
      self.add_label(label, row=row)
    return self

  def add_label(self, text, css=None, position="before", for_=None, row=None):
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
      row = self.add_row([])
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

  def add_title(self, text, css=None, position="before", row=None):
    """
    Add an elementary title component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param row:

    """
    if row is None:
      row = self.add_row([])
    if text is not None:
      row.attr("title", self._report.ui.texts.title(text))
      if position == "before":
        self.prepend_child(row.title)
      else:
        self.append_child(row.title)
      #self.title.inReport = False
      if css is not None:
        row.title.css(css)
    return self

  def add_row(self, html_containers):
    """

    :return:
    """
    new_row = Row()
    self.rows.append(new_row)
    return new_row

  def __str__(self):
    return '<form %s><input type="submit" value="Submit">%s</form>' % (self.strAttr(pyClassNames=self.pyStyle), self.helper)
