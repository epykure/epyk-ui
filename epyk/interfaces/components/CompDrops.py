"""

"""

from epyk.core import html


class DropData(object):
  def __init__(self, context):
    self.context = context

  def dropfile(self, placeholder='Drop your files here', tooltip=None, report_name=None, file_type="OUTPUTS", profile=None):
    """
    Description:
    ------------
    Add an HTML component to drop files. The files will be dropped by default to the OUTPUT folder of the defined environment.
    Files will also be recorded in the database in order to ensure that those data will not be shared.
    The data sharing is and should be defined only by the user from the UI.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlFiles.DropFile`

    Usage::

      rptObj.ui.drops.dropfile()

    Related Pages:
Attributes:
    ----------
    :param placeholder:
    :param tooltip:
    :param report_name:
    :param file_type:
    :param profile:

    :rtype: html.HtmlFiles.DropFile

    :return:
    """
    return html.HtmlFiles.DropFile(self.context.rptObj, placeholder, tooltip, report_name, file_type, profile)
