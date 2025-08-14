from . import Catalog

from ..styles.classes import CssStylesPivot, CssStylesTableExcel, CssStylesTable, \
    CssStylesDiv, CssStylesTableAgGrid


class CatalogTable(Catalog.CatalogGroup):

    def table(self) -> CssStylesTable.CssTableBasic:
        """
    """
        return self._set_class(CssStylesTable.CssTableBasic)

    def row_hover(self) -> CssStylesTable.CssTrHover:
        """
    """
        return self._set_class(CssStylesTable.CssTrHover)

    def new_row(self) -> CssStylesTable.CssTableNewRow:
        """
    """
        return self._set_class(CssStylesTable.CssTableNewRow)

    def selected(self) -> CssStylesTable.CssTableSelected:
        """
    """
        return self._set_class(CssStylesTable.CssTableSelected)

    def cell_comment(self) -> CssStylesTable.CssCellComment:
        """
    """
        return self._set_class(CssStylesTable.CssCellComment)

    def cell_save(self) -> CssStylesTable.CssCellSave:
        """
    """
        return self._set_class(CssStylesTable.CssCellSave)

    def editable(self) -> CssStylesTable.CssTdEditor:
        """
    """
        return self._set_class(CssStylesTable.CssTdEditor)

    def row_details(self) -> CssStylesTable.CssTdDetails:
        """
    """
        return self._set_class(CssStylesTable.CssTdDetails)

    def row_details_shown(self) -> CssStylesTable.CssTdDetailsShown:
        """
    """
        return self._set_class(CssStylesTable.CssTdDetailsShown)

    def grid_headers(self) -> CssStylesTable.CssTdGridHeaderCols:
        """
    """
        return self._set_class(CssStylesTable.CssTdGridHeaderCols)

    def grid_no_header(self) -> CssStylesTable.CssTdGridNoHeaderCols:
        """  """
        return self._set_class(CssStylesTable.CssTdGridNoHeaderCols)

    def grid_row_header(self) -> CssStylesTable.CssTdGridHeaderRows:
        """  """
        return self._set_class(CssStylesTable.CssTdGridHeaderRows)

    def grid_vals(self) -> CssStylesTable.CssTdGridVals:
        """  """
        return self._set_class(CssStylesTable.CssTdGridVals)

    def pivot_head(self) -> CssStylesPivot.CssPivotHead:
        """  """
        return self._set_class(CssStylesPivot.CssPivotHead)

    def datatable(self) -> CssStylesTable.CssDataTable:
        """  """
        return self._set_class(CssStylesTable.CssDataTable)

    def datatable_header(self) -> CssStylesTable.CssDataTableHeader:
        """  """
        return self._set_class(CssStylesTable.CssDataTableHeader)

    def datatable_footer(self) -> CssStylesTable.CssDataTableFooter:
        """  """
        return self._set_class(CssStylesTable.CssDataTableFooter)

    def datatable_even(self) -> CssStylesTable.CssDataTableEven:
        """  """
        return self._set_class(CssStylesTable.CssDataTableEven)

    def datatable_odd(self):
        """  """
        return self._set_class(CssStylesTable.CssDataTableOdd)

    def pivot_cell(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotCells)

    def pivot_axis(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotAxis)

    def pivot_filter_box(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBox)

    def pivot_filter_val(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterVals)

    def pivot_filter_label(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotLabel)

    def pivot_filter_popup(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUp)

    def pivot_filter_popup_header(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUpHeader)

    def pivot_filter_popup_button(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUpButton)

    def pivot_filter_popup_checks(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUpCheck)

    def pivot_filter_popup_checks_label(self):
        """  """
        return self._set_class(CssStylesPivot.CssPivotFilterBoxPopUpCheckLabel)

    def excel(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcel)

    def excel_header_cell(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelHeaderCell)

    def excel_row(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelTd)

    def excel_cell(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelCell)

    def excel_title(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelTitle)

    def excel_selected_row(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelSelectedRow)

    def excel_selected_cell(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableExcelSelected)

    def excel_red_cell(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableRedCells)

    def excel_red_cell_background(self):
        """  """
        return self._set_class(CssStylesTableExcel.CssTableBackGroundRedCells)

    def table_content(self):
        """ """
        return self._set_class(CssStylesDiv.CssDivTableContent)

    def ag_head(self):
        """
    Predefined CSS class for the AG Grid header.
    """
        return self._set_class(CssStylesTableAgGrid.CssAgHead)

    def ag_filter(self):
        """
    Predefined CSS Class for the AG Grid filter boxes.
    """
        return self._set_class(CssStylesTableAgGrid.CssAgFilter)

    def ag_popup(self):
        """
    Predefined CSS Class for the AG Grid Popup selection in the filter boxes.
    """
        return self._set_class(CssStylesTableAgGrid.CssAgMFilterPopup)

    def ag_menu(self):
        """
    Predefined CSS class for the AG Grid Menu.
    """
        return self._set_class(CssStylesTableAgGrid.CssAgHeaderLabel)

    def ag_row_odd(self):
        """  """
        return self._set_class(CssStylesTableAgGrid.CssAgOddRow)

    def ag_row_even(self, attrs: dict = None):
        """  """
        cls = self._set_class(CssStylesTableAgGrid.CssAgEvenRow)
        if attrs is not None:
            cls.css(attrs)
        return cls

    def ag_row(self):
        """  """
        return self._set_class(CssStylesTableAgGrid.CssAgRow)

    def ag_cell_focus(self):
        """  """
        return self._set_class(CssStylesTableAgGrid.CssAgCellFocus)

    def ag_cell(self):
        """  """
        return self._set_class(CssStylesTableAgGrid.CssAgCell)
