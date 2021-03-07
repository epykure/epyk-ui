

class Dropdowns:

  def __init__(self, ui):
    ui.page.jsImports.add("@popperjs/core")
    self.page = ui.page

  def buttons(self, text, values, category="primary"):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/dropdowns/

    Attributes:
    ----------
    :param text:
    :param values:
    :param category:
    """
    schema = {"type": 'div', 'class': 'dropdown', 'attrs': {'role': 'group'}, 'css': None, 'children': [
      {'type': 'button', 'css': None, 'class': 'btn btn-%s dropdown-toggle' % category,
       'attrs': {'data-toggle': 'dropdown'}, 'args': {'text': text}},
      {"type": 'div', 'css': None, 'class': 'dropdown-menu', 'children': []}
    ]}

    for v in values:
      schema['children'][1]['children'].append(
        {'type': 'link', 'css': None, 'class': 'dropdown-item', 'args': {'text': v, 'url': '#'}})
    button = self.page.web.bs.composite(schema, options={"reset_class": True})
    return button

  def menu(self, text, values):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/dropdowns/

    Attributes:
    ----------
    :param text:
    :param values:
    """
    schema = {"type": 'div', 'class': 'dropdown-menu', 'css': None, 'children': [
      {'type': 'span', 'css': None, 'class': 'dropdown-item-text', 'args': {'text': text}},
    ]}

    for v in values:
      schema['children'].append({'type': 'link', 'css': None, 'class': 'dropdown-item',
                                 'args': {'text': v, 'url': '#'}})
    button = self.page.web.bs.composite(schema, options={"reset_class": True})
    return button

  def text(self, values):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/dropdowns/

    Attributes:
    ----------
    :param values:
    """
    schema = {"type": 'div', 'class': 'dropdown-menu p-4 text-muted', 'css': None, 'children': []}
    for v in values:
      schema['children'].append({'type': 'p', 'css': None, 'class': None, 'args': {'text': v}})
    button = self.page.web.bs.composite(schema, options={"reset_class": True})
    return button
