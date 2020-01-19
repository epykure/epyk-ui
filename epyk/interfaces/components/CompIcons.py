"""
Module dedicated to produce icon components
"""

from epyk.core import html
from epyk.core.js.packages import JsFontAwesome


class Icons(object):
  def __init__(self, context):
    self.context = context

  @property
  def get(self):
    return JsFontAwesome

  def awesome(self, icon, text=None, tooltip=None, position=None, size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
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
    """
    size = self.context._size(size)
    html_edit = html.HtmlButton.IconEdit(self.context.rptObj, position, icon, text, size, tooltip, width, height, htmlCode, profile)
    html_edit.css({"display": "inline-block", "float": position})
    self.context.register(html_edit)
    return html_edit

  def edit(self, text=None, position=None, tooltip="Edit", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
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
    """
    return self.awesome('far fa-edit', text, position, tooltip, size, width, height, htmlCode, profile)

  def clock(self, text=None, position=None, tooltip="Last Updated Time", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-clock', text, position, tooltip, size, width, height, htmlCode, profile)

  def refresh(self, text=None, position=None, tooltip="Refresh Component", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-sync-alt', text, position, tooltip, size, width, height, htmlCode, profile)

  def pdf(self, text=None, position=None, tooltip="Convert to PDF", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
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
    """
    return self.awesome('far fa-file-pdf', text, position, tooltip, size, width, height, htmlCode, profile)

  def plus(self, text=None, position=None, tooltip="Add line", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
           htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-plus-square', text, position, tooltip, size, width, height, htmlCode, profile)

  def excel(self, text=None, position=None, tooltip="Convert to Excel", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-file-excel', text, position, tooltip, size, width, height, htmlCode, profile)

  def download(self, text=None, position=None, tooltip="Download", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
               htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-download', text, position, tooltip, size, width, height, htmlCode, profile)

  def delete(self, text=None, position=None, tooltip="Delete Component on the page", size=(None, 'px'), width=(None, 'px'),
             height=(None, 'px'), htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-trash-alt', text, position, tooltip, size, width, height, htmlCode, profile)

  def zoom(self, text=None, position=None, tooltip="Zoom on Component", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'), htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-search-plus', text, position, tooltip, size, width, height, htmlCode, profile)

  def capture(self, text=None, position=None, tooltip="Save to clipboard", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
              htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('far fa-clipboard', text, position, tooltip, size, width, height, htmlCode, profile)

  def remove(self, text=None, position=None, tooltip="Remove Item", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-times-circle', text, position, tooltip, size, width, height, htmlCode, profile)

  def table(self, text=None, position=None, tooltip="Convert to Table", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
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
    """
    return self.awesome('fas fa-table', text, position, tooltip, size, width, height, htmlCode, profile)

  def wrench(self, text=None, position=None, tooltip="Processing Time", size=(None, 'px'), width=(None, 'px'), height=(None, 'px'),
             htmlCode=None, profile=None):
    """

    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.awesome('fas fa-wrench', text, position, tooltip, size, width, height, htmlCode, profile)

  def signin(self, text, size=(None, "px"), icon=None):
    """

    :return:
    """
    size = self.context._size(size)
    bar = html.HtmlEvent.SignIn(self.context.rptObj, text, size, icon)
    self.context.register(bar)
    return bar
