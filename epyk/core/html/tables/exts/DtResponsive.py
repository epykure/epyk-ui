
from epyk.core.data import DataClass


class DataBreakPoints(DataClass):

  @property
  def name(self):
    """
    Description:
    -----------

    Related Pages:

			https://datatables.net/reference/option/responsive.breakpoints
    """
    return self._attrs["name"]

  @name.setter
  def name(self, val):
    self._attrs["name"] = val

  @property
  def width(self):
    """
    Description:
    -----------

    Related Pages:

			https://datatables.net/reference/option/responsive.breakpoints
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val


class DataDetails(DataClass):

  @property
  def type(self):
    """
    Description:
    -----------

    Related Pages:

			https://datatables.net/reference/option/responsive.details
    """
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def display(self):
    """
    Description:
    -----------
    Responsive provides the ability to show information about the columns it has hidden using DataTables child rows feature (row().child()), but you may wish to display the data in a different manner (potentially so you can use the child rows for other actions such as editing) - this parameter provides that ability.

    Related Pages:

			https://datatables.net/reference/option/responsive.details.display
    """
    return self._attrs["display"]

  @display.setter
  def display(self, val):
    self._attrs["display"] = val

  @property
  def renderer(self):
    """
    Description:
    -----------


    Related Pages:

			https://datatables.net/reference/option/responsive.details.renderer
    """
    return self._attrs["renderer"]

  @renderer.setter
  def renderer(self, val):
    self._attrs["renderer"] = val

  @property
  def target(self):
    """
    Description:
    -----------

    Related Pages:

			https://datatables.net/reference/option/responsive.details.target
    """
    return self._attrs["target"]

  @target.setter
  def target(self, val):
    self._attrs["target"] = val


class Responsive(DataClass):

  def activate(self):
    self.details.type = "column"
    return self

  @property
  def details(self):
    """
    Description:
    -----------
    Responsive has the ability to use DataTables' child rows feature to show information about any columns which have been removed from the display as a child row, which can be particularly useful for displaying complex information on small screen devices. Please see the Responsive manual on the details rows for further information.

    Related Pages:

			https://datatables.net/reference/option/responsive.details

    :rtype: DataDetails
    """
    return self.sub_data("details", DataDetails)

  @property
  def breakpoints(self):
    """
    Description:
    -----------
    The visibility of columns in a DataTable with Responsive enabled can be controlled by breakpoints and class names matching those breakpoints (and other logical operations) .
    This provides the ability to exactly control which columns in a table will be visible for each device type. See the Responsive manual for more information.

    Related Pages:

			https://datatables.net/reference/option/responsive.breakpoints

    :rtype: DataBreakPoints
    """
    return self.sub_data("breakpoints", DataBreakPoints)

  @property
  def orthogonal(self):
    """
    Description:
    -----------
    When Responsive is asked to show the hidden information about a DataTable row,
    it uses the cell().render() method to access this data for each cell in the row.
    This method provides DataTables ability to make use of orthogonal data - that is,
    the same data but formatted in a different way for different uses.

    Related Pages:

			https://datatables.net/reference/option/responsive.details.target
    """
    return self._attrs["orthogonal"]

  @orthogonal.setter
  def orthogonal(self, val):
    self._attrs["orthogonal"] = val
