"""
Utilities for the various CLI
"""

import os
from epyk.core.Page import Report


def get_report_path(project_path, raise_error=True):
  """
  Description:
  ------------
  Get the reports path from the command run.
  This function will try to either find the ui or the reports folder.

  Attributes:
  ----------
  :param project_path: String. The project path
  """
  ui_path = os.path.join(project_path, 'ui')
  if not os.path.exists(ui_path):
    reports_path = os.path.join(project_path, 'reports')
  else:
    reports_path = os.path.join(project_path, 'ui', 'reports')
  if not os.path.exists(reports_path):
    if raise_error:
      raise Exception("Cannot find ui or reports path in this project")

    return project_path

  return reports_path


def get_page(mod):
  """
  Description:
  ------------
  Get the page object from the imported module

  Attributes:
  ----------
  :param mod: Module. The Python imported module used to build the page
  """
  if hasattr(mod, 'get_page'):
    page = Report()
    mod.get_page(page)
    return page

  return mod.page
