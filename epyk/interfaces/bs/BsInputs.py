

class Inputs:

  def __init__(self, ui):
    self.page = ui.page

  def input(self, value, label=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param label:
    """
    if label is None:
      schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
        {"type": 'input', 'class': 'form-control', 'css': None, 'args': {'text': value}}
      ]}
    else:
      schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
        {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
          {"type": 'span', 'class': 'input-group-text', 'ref': 'basic-addon1', 'css': None, 'args': {'text': label}}
        ]},
        {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'}, 'args': {'text': value}}]}

    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def inputs(self, values, label=None):
    """
    Description:
    ------------

    :param value:
    :param label:
    """
    if label is None:
      schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': []}
    else:
      schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
        {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
          {"type": 'span', 'class': 'input-group-text', 'ref': 'basic-addon1', 'css': None, 'args': {'text': label}}
        ]}]}

    for v in values:
      schema['children'].append({"type": 'input', 'class': 'form-control', 'css': None, 'args': {'text': v}})
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def button(self, text, label="", category='secondary'):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param text:
    :param label:
    :param category:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'button', 'class': 'btn btn-outline-%s' % category, 'ref': 'basic-addon1', 'css': None, 'args': {'text': label}}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': text}}]}
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def select(self, values, label="", category='secondary'):
    """
    Description:
    ------------

    https://getbootstrap.com/docs/4.4/components/input-group/

    :param text:
    :param label:
    :param category:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'button', 'class': 'btn btn-outline-%s' % category, 'ref': 'basic-addon1', 'css': None, 'args': {'text': label}}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': values}}]}
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def segment(self, values, label="", category='secondary'):
    """
    Description:
    ------------

    Related Pages:

      ttps://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param values:
    :param label:
    :param category:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'button', 'class': 'btn btn-outline-%s' % category, 'ref': 'basic-addon1', 'css': None, 'args': {'text': label}},
        {"type": 'button', 'class': 'btn btn-outline-%s  dropdown-toggle dropdown-toggle-split' % category,
         'attrs': {"data-toggle": 'dropdown'}, 'arias': {"haspopup": True, 'expanded': False}, 'css': None, 'children': [
            {"type": 'span', 'class': 'sr-only', 'css': None, 'args': {"text": 'Toggle Dropdown'}}
        ]},
        {"type": 'div', 'class': 'dropdown-menu', 'css': None, 'children': []},
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'}}
    ]}
    self.page.jsImports.add("@popperjs/core")
    for v in values:
      schema['children'][0]['children'][2]['children'].append(
        {"type": 'link', 'class': 'dropdown-item', 'css': None, 'args': {"text": v, 'url': '#'}},)
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def dropdown(self, values, label="", category='secondary'):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param values: List.
    :param label:
    :param category:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'button', 'class': 'btn btn-outline-%s' % category, 'ref': 'basic-addon1', 'css': None,
         'args': {'text': label}}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': values}}]}
    self.page.jsImports.add("@popperjs/core")
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def custom(self, values, label="", category='secondary'):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param values:
    :param label:
    :param category:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'button', 'class': 'btn btn-outline-%s' % category, 'ref': 'basic-addon1', 'css': None,
         'args': {'text': label}}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': values}}]}
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def radio(self, text, flag=False):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param flag:
    :param flag:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'css': None, 'children': [
        {"type": 'div', 'class': 'input-group-text', 'css': None, 'children': [
          {"type": 'radio', 'ref': 'basic-addon1', 'css': None, 'args': {'flag': flag}}
        ]}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': text}}]}
    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp

  def checkbox(self, text, flag=False, width=(None, "%"), height=(None, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/input-group/

    Attributes:
    ----------
    :param flag:
    :param flag:
    """
    schema = {"type": 'div', 'class': 'input-group mb-3', 'css': None, 'args': {"width": width, "height": height}, 'children': [
      {"type": 'div', 'class': 'input-group-prepend', 'args': {"width": width, "height": height}, 'css': None, 'children': [
        {"type": 'div', 'class': 'input-group-text', 'css': None, 'children': [
          {"type": 'checkbox', 'ref': 'basic-addon1', 'css': None, 'args': {'flag': flag}}
        ]}
      ]},
      {"type": 'input', 'class': 'form-control', 'css': None, 'arias': {"describedby": 'basic-addon1'},
       'args': {'text': text, "width": width, "height": height}}]}

    comp = self.page.web.bs.composite(schema, options={"reset_class": True})
    return comp
