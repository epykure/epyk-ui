"""
Module dedicated to produce icon components
"""

from epyk.core import html


class Icons(object):
  def __init__(self, context):
    self.context = context

  def awesome(self, icon, tooltip=None, position=None, size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """

    Example
    rptObj.ui.icons.awesome(icon="fas fa-align-center")

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, icon, size, tooltip, width,
                                                          height, htmlCode, profile))

  def edit(self, position=None, tooltip="Edit", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """

    Example
    rptObj.ui.icons.edit()
    rptObj.ui.icons.edit().color("red")

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'far fa-edit', size, tooltip, width,
                                                          height, htmlCode, profile))

  def clock(self, position=None, tooltip="Last Updated Time", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-clock', size, tooltip, width,
                                                          height, htmlCode, profile))

  def refresh(self, position=None, tooltip="Refresh Component", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-sync-alt', size, tooltip, width,
                                                          height, htmlCode, profile))

  def pdf(self, position=None, tooltip="Convert to PDF", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
          htmlCode=None,  profile=None):
    """

    Example
    rptObj.ui.icons.pdf(tooltip="helper")

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'far fa-file-pdf', size, tooltip, width,
                                                          height, htmlCode, profile))

  def plus(self, position=None, tooltip="Add line", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-plus-square', size, tooltip, width,
                                                          height, htmlCode, profile))

  def excel(self, position=None, tooltip="Convert to Excel", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'far fa-file-excel', size, tooltip, width,
                                                          height, htmlCode, profile))

  def download(self, position=None, tooltip="Download", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-download', size, tooltip, width,
                                                          height, htmlCode, profile))

  def delete(self, position=None, tooltip="Delete Component on the page", size=(None, 'px'), width=(None, 'px'),
             height=(None, 'px'), htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'far fa-trash-alt', size, tooltip, width,
                                                          height, htmlCode, profile))

  def zoom(self, position=None, tooltip="Zoom on Component", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-search-plus', size, tooltip, width,
                                                          height, htmlCode, profile))

  def capture(self, position=None, tooltip="Save to clipboard", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'far fa-clipboard', size, tooltip, width,
                                                          height, htmlCode, profile))

  def remove(self, position=None, tooltip="Remove Item", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-times-circle', size, tooltip, width,
                                                          height, htmlCode, profile))

  def table(self, position=None, tooltip="Convert to Table", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """

    Example
    rptObj.ui.icons.table(tooltip="helper")

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-table', size, tooltip, width,
                                                          height, htmlCode, profile))

  def wrench(self, position=None, tooltip="Processing Time", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlButton.IconEdit

    :return: The Html Icon object
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlButton.IconEdit(self.context.rptObj, position, 'fas fa-wrench', size, tooltip, width,
                                                          height, htmlCode, profile))

