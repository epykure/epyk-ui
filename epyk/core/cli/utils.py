"""
Utilities for the various CLI
"""

import os

from epyk.core.css.themes.Theme import ThemeDefault


def get_report_path(project_path, raise_error=True, report=None):
  """
  Description:
  ------------
  Get the reports path from the command run.
  This function will try to either find the ui or the reports folder.

  Attributes:
  ----------
  :param project_path: String. The project path.
  :param raise_error. Boolean. Optional. Flag to raise an error.
  :param report: Page. Optional. The web page object.
  """
  ui_path, reports_path = os.path.join(project_path, 'ui'), None
  possible_structure = [("ui", ), ("ui", 'reports'), ("reports", )]
  if report is not None:
    if os.path.exists(os.path.join(project_path, report)):
      reports_path = project_path
    else:
      for k in possible_structure:
        t_path = os.path.join(project_path, *k)
        if os.path.exists(os.path.join(t_path, report)):
          reports_path = project_path
          break

  else:
    if not os.path.exists(ui_path):
      reports_path = os.path.join(project_path, 'reports')
    else:
      reports_path = os.path.join(project_path, 'ui', 'reports')

  if reports_path is None:
    reports_path = project_path

  if not os.path.exists(reports_path):
    if raise_error:
      raise ValueError("Cannot find ui or reports path in this project")

    return project_path

  return reports_path


def get_page(mod, template=False, colors=None):
  """
  Description:
  ------------
  Get the page object from the imported module.

  Attributes:
  ----------
  :param mod: Module. The Python imported module used to build the page.
  :param template: Boolean. Optional.
  :param colors: String. Optional. The list of colors as string commas delimited.
  """

  if colors is not None:
    old_colors = ThemeDefault._colors
    ThemeDefault._colors = colors.split(",")

  if hasattr(mod, 'get_page'):
    try:
      from epyk_studio.core.Page import Report

      page = Report()
      page.json_config_file = mod.__name__
    except Exception as err:
      from epyk.core.Page import Report

      page = Report()
      page.json_config_file = mod.__name__
    if template and hasattr(mod, 'INPUTS'):
      page.inputs = {i: "%%(%s)s" % i for i in mod.INPUTS}
    mod.get_page(page)

    if colors is not None:
      ThemeDefault._colors = old_colors
    return page

  if colors is not None:
    ThemeDefault._colors = old_colors
  return mod.page
