"""

"""

import datetime

from epyk.core.html import Html
from epyk.core.js.Imports import requires

sqlalchemy = requires("sqlalchemy", reason='Missing Package', install='sqlalchemy', source_script=__file__)


def system_user_configuration():
  return [sqlalchemy.Column('row_id', sqlalchemy.Integer, autoincrement=True, primary_key=True),
    sqlalchemy.Column('html_code', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('report_name', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('env', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('data', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('username', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('type', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('active_flag', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, default=datetime.datetime.utcnow(), nullable=True)]


class ConfigTable(Html.Html):
  name, category, callFnc = 'Config Table', 'Tables', 'config'
  __reqCss, __reqJs = ['tabulator'], ['tabulator']

  def __init__(self, report, htmlCode, visible, profile):
    pass

  def load(self):
    """

    :return:
    """

  def get(self):
    """

    :param htmlCode:
    :return:
    """