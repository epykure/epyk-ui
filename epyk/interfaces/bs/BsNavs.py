

class Bars(object):

  def __init__(self, context):
    self.context = context

  def bar(self, values, active=None):
    """
    Description:
    ------------

    """
    schema = {"type": 'list', 'class': 'nav', 'css': None, 'children': []}
    for v in values:
      schema['children'].append({"type": 'item', 'css': None, 'class': 'nav-item', 'children': [
        {"type": 'link', 'class': 'nav-link', 'args': {'text': v, 'url': '#'}}
      ]})
      if active == v:
        schema['children'][-1]['children'][0]['class'] = 'nav-link active'
    nav = self.context.rptObj.web.bs.composite(schema, options={"reset_class": True})
    nav.attr['data-toggle'] = "button"
    return nav

  def vertical(self, values, type=None, active=None):
    """
    Description:
    ------------

    """
    nav = self.bar(values, active)
    nav.attr['class'].add("flex-column")
    if type is not None:
      nav.attr['class'].add("nav-%s" % type)
    return nav

  def tabs(self, values, active=None):
    """
    Description:
    ------------

    """
    nav = self.bar(values, active)
    nav.attr['class'].add("nav-tabs")
    return nav

  def pills(self, values, active=None):
    """
    Description:
    ------------

    Related Pages:

      https://getbootstrap.com/docs/4.4/components/navs/
    """
    nav = self.bar(values, active)
    nav.attr['class'].add("nav-pills")
    return nav
