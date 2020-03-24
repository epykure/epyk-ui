from epyk.core.data import DataClass



class SearchPanes(DataClass):

  @property
  def cascadePanes(self):
    """
    Description:
    -----------
    As standard, SearchPanes will display all of the options for that column throughout its operation.
    When searchPanes.cascadePanes is set to true, the panes will remove options which are no longer present in the currently displayed DataTable.
    The cascade action will occur when a selection or a deselection is made in one of the panes.

    This is useful when dealing with large data sets with many different options as they are narrowed down accordingly as selections proceed.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.cascadePanes
    """
    return self._attrs['cascadePanes']

  @cascadePanes.setter
  def cascadePanes(self, val):
    self._attrs['cascadePanes'] = val

  @property
  def clear(self):
    """
    Description:
    -----------
    As standard, SearchPanes will display the buttons which allow selections to be cleared in individual panes and across all panes.
    When searchPanes.clear is set to false, the clear buttons will not be present.

    The searchPanes.clear functionality is useful when wanting to quickly deselect all of the options in a pane.
    It is useful to be able to disable these buttons, for example on smaller tables with less options it may be preferrable to employ a custom user interface.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.clear
    """
    return self._attrs['clear']

  @clear.setter
  def clear(self, val):
    self._attrs['clear'] = val

  @property
  def columns(self):
    """
    Description:
    -----------
    As standard, SearchPanes will consider all of the columns when creating searchPanes.
    When searchPanes.columns is defined with an array of numbers, then only the columns with those indexes will be considered when creating panes.
    Note they still may not be displayed based upon the calculations of searchPanes.threshold or columns.searchPanes.threshold.

    The searchPanes.columns functionality is useful when wanting to restrict which columns will be considered when displaying panes.
    This may result in faster load times as there is not as much validation to be done.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.columns
    """
    return self._attrs['columns']

  @columns.setter
  def columns(self, val):
    self._attrs['columns'] = val

  @property
  def controls(self):
    """
    Description:
    -----------
    As standard, SearchPanes will be displayed with the control buttons included in the interface with searching enabled.
    However if the value of searchPanes.controls is set to false then the control buttons will no longer be displayed and searching will be disabled in all of the panes.

    The control buttons can be hidden and searching disabled for individual panes by the columns.searchPanes.controls option.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.controls
    """
    return self._attrs['controls']

  @controls.setter
  def controls(self, val):
    self._attrs['controls'] = val

  @property
  def dataLength(self):
    """
    Description:
    -----------
    This is useful as it prevents the searchPanes cells becoming mishapen and overpopulated when the table contains long strings.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.dataLength
    """
    return self._attrs['dataLength']

  @dataLength.setter
  def dataLength(self, val):
    self._attrs['dataLength'] = val

  @property
  def emptyMessage(self):
    """
    Description:
    -----------
    Empty cells will be represented in the panes by the option searchPanes.emptyMessage. This is useful as it's a more user-friendly way than just having a blank cell.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.emptyMessage
    """
    return self._attrs['emptyMessage']

  @emptyMessage.setter
  def emptyMessage(self, val):
    self._attrs['emptyMessage'] = val

  @property
  def hideCount(self):
    """
    Description:
    -----------
    As standard, SearchPanes will be displayed with the count column included in the table.
    However if the value of searchPanes.hideCount is set to true then the count column won't be displayed in any of the panes.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.hideCount
    """
    return self._attrs['hideCount']

  @hideCount.setter
  def hideCount(self, val):
    self._attrs['hideCount'] = val

  @property
  def layout(self):
    """
    Description:
    -----------
    By setting the searchPanes.layout parameter to columns-3, the panes will be displayed in 3 columns.

    There are 6 sizes supported from 1 pane in a row to 6 panes in a row. Altering the number at the end of columns- will alter the number of panes on a row.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.layout
    """
    return self._attrs['layout']

  @layout.setter
  def layout(self, val):
    self._attrs['layout'] = val

  @property
  def orderable(self):
    """
    Description:
    -----------
    As standard, SearchPanes will be displayed with the ordering buttons included in the interface, allowing the user to change the order of the selections in each pane.
    However if the value of searchPanes.orderable is set to false then the ordering buttons will no longer be displayed in any of the panes.
    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.orderable
    """
    return self._attrs['orderable']

  @orderable.setter
  def layout(self, val):
    self._attrs['orderable'] = val

  @property
  def orderable(self):
    """
    Description:
    -----------
    As standard, SearchPanes will be displayed with the ordering buttons included in the interface, allowing the user to change the order of the selections in each pane.
    However if the value of searchPanes.orderable is set to false then the ordering buttons will no longer be displayed in any of the panes.
    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.orderable
    """
    return self._attrs['orderable']

  @orderable.setter
  def layout(self, val):
    self._attrs['orderable'] = val





  """!!!!!!!!!!!!!!! TODO All composite options !!!!!!!!!!!!!!!!!"""

  @property
  def dtOpts(self):
    """
    Description:
    -----------
    This is useful as it prevents the searchPanes cells becoming mishapen and overpopulated when the table contains long strings.

    Related Pages:
    --------------
    https://datatables.net/reference/option/searchPanes.dtOpts
    """
    return self._attrs['dtOpts']

  @dtOpts.setter
  def dtOpts(self, val):
    self._attrs['dtOpts'] = val