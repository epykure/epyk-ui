
class Lists(object):

  def __init__(self, context):
    self.context = context

  def list(self, values):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values:
    :return:
    """
    container = self.context.rptObj.web.std.list(values)
    container.style.clear_all()
    for c in container:
      c.style.clear_all()
      c.attr['class'].add("list-group-item")
    container.attr['class'].add("list-group")
    return container

  def horizontal(self, values, sizing='sm'):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values:
    :return:
    """
    container = self.context.rptObj.web.std.list(values)
    container.style.clear_all()
    for c in container:
      c.style.clear_all()
      c.attr['class'].add("flex-fill list-group-item")
    container.attr['class'].add("list-group list-group-horizontal-%s")
    return container

  def buttons(self):
    """

    :return:
    """

  def badges(self):
    """

    :return:
    """