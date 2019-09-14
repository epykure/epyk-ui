"""
Module in charge of connecting all the Microsoft Office tools

"""

import os

from epyk.core.js.Imports import requires


class DataOffice(object):
  class __internal(object):
    _props = {}

  def __init__(self, report=None):
    self._report = report if report is not None else self.__internal()

  def word(self, filename, path=None):
    """
    Open a word file

    This module will use an external Python package: python-docx

    Example
    docx = rptObj.data.office.word("FX Sales Trainee.docx", path=r"")
    print(docx.paragraphs)

    Documentation
    https://python-docx.readthedocs.io/en/latest/

    :param filename: The filename with the extension
    :param path: The path of the file
    :return: A docx Python object
    """
    docx = requires("docx", reason='Missing Package', install='python-docx', source_script=__file__, raise_except=True)

    doc = open(os.path.join(path, filename), 'rb')
    document = docx.Document(doc)
    doc.close()
    return document

  def ppt(self, filename, path=None):
    """
    Open a power point file

    Example
    ppts = rptObj.data.office.ppt("diagramme.pptx", r"")
    print(ppts.slides)

    Documentation
    https://python-pptx.readthedocs.io/en/latest/user/quickstart.html

    :param filename: The filename with the extension
    :param path: The path of the file

    :return: A pptx Python object
    """
    pptx = requires("pptx", reason='Missing Package', install='python-pptx', source_script=__file__, raise_except=True)

    return pptx.Presentation(os.path.join(path, filename))

  def xls(self, filename, path=None):
    """
    Open an excel file

    Example
    data = rptObj.data.office.xls("Classeur1.xlsx", "")
    print(data.sheet_by_index(0) )

    Documentation
    https://www.geeksforgeeks.org/reading-excel-file-using-python/

    :param filename: The filename with the extension
    :param path: The path of the file

    :return: A xlrd Python object
    """
    xlrd = requires("xlrd", reason='Missing Package', install='xlrd', source_script=__file__, raise_except=True)

    return xlrd.open_workbook(os.path.join(path, filename))

  def mdb(self, filename, path=None):
    """
    Open an Access file

    :param filename: The filename
    :param path: The database full path
    :rtype: epyk.core.py.Sql.SqlConnOdbc

    :return:
    """
    return self._report.data.db.mdb(filename, path)

  def outlook(self):
    """

    :return:
    """
    win32com = requires("win32com.client", reason='Missing Package', install='pywin32', source_script=__file__, raise_except=True)
    raise Exception("To be implemented")
