"""

TODO: add the is_secured logic in this module
TODO: Check Neo4J
"""

import os

from epyk.core.py import primitives
from epyk.core.js.Imports import requires
from epyk.core.py import PySql

MISSING_PACKAGE = 'Missing Package'


class NoSql:

  def __init__(self, page: primitives.PageModel = None):
    self.page = page

  def mongo(self, host="localhost", port=5000, is_secured=False):
    """   

    Related Pages:

      https://www.w3schools.com/python/python_mongodb_getstarted.asp
      https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-4.0.3-signed.msi/download

    :param host: String. Optional. Database hostname. Default localhost
    :param port: Integer. Optional. Database port. Default 5000
    :param is_secured: Boolean. Optional.
    """
    py_mongo = requires(
      "pyMongo", reason=MISSING_PACKAGE, install="pyMongo", source_script=__file__, raise_except=True)
    return py_mongo.MongoClient("mongodb://%s:%s/" % (host, port))

  def neo4j(self, host="localhost", port=5000, is_secured=False):
    """   

    Related Pages:

      https://neo4j.com/developer/python/
      https://community.neo4j.com/?_ga=2.69585106.394662973.1539480121-615400289.1539480121

    :param host: String. Optional. Database hostname. Default localhost.
    :param port: Integer. Optional. Database port. Default 5000.
    :param is_secured: Boolean. Optional.

    :return: A Python SQL connection for Neo4J
    """
    if 'neo4j' not in self.pkgs:
      requires("neo4j", reason=MISSING_PACKAGE, install='neo4j-driver', source_script=__file__, raise_except=True)
    return PySql.SqlConnNeo4j(host, port)


class DataDb:

  def __init__(self, page: primitives.PageModel = None):
    self.page = page
    self._db_bindings, self.pkgs = {}, {}
    self.no_sql = NoSql(page)
    self.table_names = None   # create the unique set of tables to be loaded

  def __settings(self):
    """   Retrieve the database settings based on the environment configuration.

    Settings are used in the context of generic private and public databases.
    If SQLite is used, the database will be automatically generated.

    :return: The database settings
    """
    db_settings = {"family": 'sqlite'} if self.page._dbSettings is None else dict(self.page._dbSettings)
    if not "family" in db_settings:
      db_settings["family"] = 'sqlite'
    if 'names' in db_settings:
      db_settings['public'] = db_settings['names']['public']['name']
      if db_settings['names']['private'].get("fixed", False):
        db_settings['private'] = db_settings['names']['private']['name']
      else:
        db_settings['private'] = "%s_%s" % (
          db_settings['names']['private']['name'], self.page.py.hash(self.page.run.current_user))
    elif 'name' in db_settings:
      # In this context there is no unique database per user and all the users will use a different
      # DB when they are in a private mode
      db_settings['private'] = db_settings['name']
      db_settings['public'] = db_settings['name']
      del db_settings['name']

    else:
      if 'path' not in db_settings:
        db_settings['path'] = self.page.run.local_path
      db_settings['private'] = '%s_%s' % (
        self.page.run.report_name, self.page.py.hash(self.page.run.current_user))
      db_settings['public'] = self.page.run.report_name
    if 'model_path' not in db_settings:
      db_settings['model_path'] = os.path.join(self.page.run.local_path, 'model', 'tables')
    return db_settings

  @property
  def names(self):
    """   Returns the different database names to be used by the user in a public or private context.

    Generally the public database is shared by all the users whereas the private one is only dedicated to a user and
    data can be granted to some external users.

    Related Pages:

      https://www.sqlalchemy.org/

    :return: A dictionary with the database names in each context
    """
    settings = self.__settings()
    return {"public": settings['public'], "private": settings['private']}

  @property
  def private(self):
    """   Return the private database from the family defined in the environment.

    It is not possible to specify the type of DB for an environment at this level.
    This should be done either in the server configuration or in the report configuration.

    This module rely on SQLAlchemy for the query generation

    Related Pages:

      https://www.sqlalchemy.org/

    :rtype: epyk.core.py.PySql.SqlConn
    """
    settings = self.__settings()
    database = "%(path)s/%(private)s" % settings if settings.get("path") is not None else settings['private']
    if database not in self._db_bindings:
      model_path = os.path.join(self.page.run.local_path, 'model', 'tables')
      if settings["family"] == "sqlite":
        db = self.sqlite(settings["private"], settings.get("path"), model_path, tables_scope=self.table_names)
      elif settings["family"] == "mssql":
        db = self.mssql(
          settings["private"], settings["host"], driverName=settings["driverName"], model_path=model_path,
          tables_scope=self.table_names)
      elif settings["family"] == "oracle":
        db = self.oracle(
          settings["private"], settings["host"], settings["port"], model_path=model_path, tables_scope=self.table_names)
      elif settings["family"] == "postgres":
        db = self.postgres(
          settings["private"], settings["host"], settings["port"], model_path=model_path, tables_scope=self.table_names)
      elif settings["family"] == "mysql":
        db = self.mysql(
          settings["private"], settings["host"], settings["port"], model_path=model_path, tables_scope=self.table_names)
      elif settings["family"] == "mariadb":
        db = self.mariadb(
          settings["private"], settings["host"], settings["port"], model_path=model_path, tables_scope=self.table_names)
      elif settings["family"] == "mdb":
        db = self.mdb(settings["private"], settings.get("path"), model_path)
      elif settings["family"] == "accdb":
        db = self.accdb(settings["private"], settings.get("path"), model_path)
      self._db_bindings[database] = db
    return self._db_bindings[database]

  @property
  def public(self):
    """   Return the public shared database from the family defined in the environment.

    It is not possible to specify the type of DB for an environment at this level.
    This should be done either in the server configuration or in the report configuration.

    This module rely on SQLAlchemy for the query generation

    Related Pages:

      https://www.sqlalchemy.org/

    :rtype: epyk.core.py.PySql.SqlConn

    :return: A Sql object
    """
    settings = self.__settings()
    database = "%(path)s/%(public)s" % settings if settings.get("path") is not None else settings['public']
    if database not in self._db_bindings:
      model_path = os.path.join(self.page.run.local_path, 'model', 'tables')
      if settings["family"] == "sqlite":
        db = self.sqlite(settings["public"], settings.get("path"), model_path)
      elif settings["family"] == "mssql":
        db = self.mssql(settings["public"], settings["host"], driverName=settings["driverName"], model_path=model_path)
      elif settings["family"] == "oracle":
        db = self.oracle(settings["public"], settings["host"], settings["port"], model_path=model_path)
      elif settings["family"] == "postgres":
        db = self.postgres(settings["public"], settings["host"], settings["port"], model_path=model_path)
      elif settings["family"] == "mysql":
        db = self.mysql(settings["public"], settings["host"], settings["port"], model_path=model_path)
      elif settings["family"] == "mariadb":
        db = self.mariadb(settings["public"], settings["host"], settings["port"], model_path=model_path)
      elif settings["family"] == "mdb":
        db = self.mdb(settings["public"], settings.get("path"), model_path)
      elif settings["family"] == "accdb":
        db = self.accdb(settings["public"], settings.get("path"), model_path)
      self._db_bindings[database] = db
    return self._db_bindings[database]

  def reflect(self, table_names: list):
    """   Reduce the scope of database tables to be loaded by SQLAchemy.

    Related Pages:

      https://docs.sqlalchemy.org/en/13/core/metadata.html

    :param table_names:
    """
    if self.table_names is None:
      self.table_names = set(table_names)
    else:
      self.table_names |= set(table_names)
    return self

  def sqlite(self, name, db_path=None, model_path=None, db_settings=None, tables_scope=None):
    """   Create a bespoke SQLite database.

    By default the database will be in the current folder.
    The table definition will not be done automatically for this database and this should be created in a
    external manner

    :param name: The database name
    :param db_path: Optional, the database path
    :param model_path: Optional, the model with the tables definition. The filename must be unique in the project
    :param db_settings:
    :param tables_scope:

    :rtype: epyk.core.py.PySql.SqlConn

    :return: The SQL object
    """
    if db_path is None:
      db_path = self.page.run.local_path
    database = "%s/%s.db" % (db_path, name)
    data_settings = {"loadModel": model_path is not None, 'model_path': model_path or False}
    if db_settings is not None:
      data_settings.update(db_settings)
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn(
        'sqlite', database=database, tables_scope=tables_scope, **data_settings)
    return self._db_bindings[database]

  def oracle(self, name, host, port, model_path=None, is_secured=False, tables_scope=None):
    """   

    :param name: Database name
    :param host: Optional, Database hostname. Default localhost
    :param port: Optional, Database port. Default 5432
    :param model_path: Optional, Database model path with the python scripts of the tables
    :param is_secured: If credentials required. Default False
    :param tables_scope:

    :rtype: epyk.core.py.PySql.SqlConn
    """
    if 'oracle' not in self.pkgs:
      self.pkgs[name] = requires(name, reason='Missing Package', install="cx_Oracle", source_script=__file__)

    database = name
    db_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                   "username": "postgres", "password": "240985", "host": host, "port": port}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn('oracle', database=database, tables_scope=tables_scope, **db_settings)
    return self._db_bindings[database]

  def mssql(self, name, host="localhost", driver_name="{ODBC Driver 17 for SQL Server}",
            model_path=None, tables_scope=None):
    """   

    :param name: The database name
    :param host: The database host name
    :param driver_name: Optional, The
    :param model_path: Optinal, The database model path

    :rtype: epyk.core.py.PySql.SqlConn
    """
    if 'mssql' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="mssql", source_script=__file__, raise_except=True)
    if 'pyodbc' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="pyodbc", source_script=__file__, raise_except=True)
    database = name
    data_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                     "driver": 'mssql+pyodbc', "driverName": driver_name, 'host': host}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn(
        'mssql+pyodbc', database=database, tables_scope=tables_scope, **data_settings)
    return self._db_bindings[database]

  def mdb(self, name, db_path, model_path=None):
    """   Get a Access (.mdb) Database query object using ODBC driver.

    :param name: The filename
    :param db_path: The database full path
    :param model_path: Optional, Database model path with the python scripts of the tables.

    :rtype: epyk.core.py.PySql.SqlConnOdbc
    """
    if 'pyodbc' not in self.pkgs:
      self.pkgs[name] = requires(name, reason='Missing Package', install="pyodbc", source_script=__file__)
    database = "%s/%s.mdb" % (db_path, name)
    data_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                     "driver": "{Microsoft Access Driver (*.mdb, *.accdb)}"}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConnOdbc(database=database, **data_settings)
    return self._db_bindings[database]

  def accdb(self, name, db_path, model_path=None):
    """   Get a Access (.accdb) Database query object using ODBC driver.

    Related Pages:

      https://www.599cd.com/access/studentdatabases/

    :param name: The filename
    :param db_path: The database full path
    :param model_path: Optional, Database model path with the python scripts of the tables

    :rtype: epyk.core.py.PySql.SqlConnOdbc
    """
    if 'pyodbc' not in self.pkgs:
      self.pkgs[name] = requires(name, reason='Missing Package', install="pyodbc", source_script=__file__)
    database = "%s/%s.accdb" % (db_path, name)
    data_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                     "driver": "{Microsoft Access Driver (*.mdb, *.accdb)}"}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConnOdbc(database=database, **data_settings)
    return self._db_bindings[database]

  def postgres(self, name, host="localhost", port=5432, model_path=None, is_secured=False, tables_scope=None):
    """   Get a PostgreSql Database query object using SQLAlchemy.

    Related Pages:

      https://www.postgresql.org/
      https://docs.sqlalchemy.org/en/13/dialects/postgresql.html#sqlalchemy.dialects.postgresql.dml.Insert.on_conflict_do_update.params.where

    :param name: Database name
    :param host: Optional, Database hostname. Default localhost
    :param port: Optional, Database port. Default 5432
    :param model_path: Optional, Database model path with the python scripts of the tables
    :param is_secured: If credentials required. Default False
    :param tables_scope:

    :rtype: epyk.core.py.PySql.SqlConn
    """
    if 'postgresql' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="postgresql", source_script=__file__, raise_except=True)
    if 'psycopg2' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="psycopg2", source_script=__file__, raise_except=True)
    database = name
    db_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                   "username": "postgres", "password": "240985", "host": host, "port": port}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn(
        'postgresql+psycopg2', database=database, tables_scope=tables_scope, **db_settings)
    return self._db_bindings[database]

  def mysql(self, name, host="localhost", port=3306, model_path=None, is_secured=False, tables_scope=None):
    """   Get a MySql Database query object using SQLAlchemy.

    Usage::

      page.data.db.mysql("MySQL", port=3333)

    Related Pages:

      https://dev.mysql.com/

    :param name: Database name
    :param host: Optional, Database hostname. Default localhost
    :param port: Optional, Database port. Default 3306
    :param model_path: Optional, Database model path with the python scripts of the tables
    :param is_secured: If credentials required. Default False

    :rtype: epyk.core.py.PySql.SqlConn
    """
    if 'pymysql' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="pymysql", source_script=__file__, raise_except=True)
    database = name
    db_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                   "username": "root", "password": "240985", "host": host, "port": port}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn(
        'mysql+pymysql', database=database, tables_scope=tables_scope, **db_settings)
    return self._db_bindings[database]

  def mariadb(self, name, host="localhost", port=3306, model_path=None, is_secured=False, tables_scope=None):
    """   Get a MariaDB Database query object using SQLAlchemy.

    Usage::

      page.data.db.mariadb("MySQL", port=3333)

    Related Pages:

      https://mariadb.org/

    :param name: Database name
    :param host: Optional, Database hostname. Default localhost
    :param port: Optional, Database port. Default 3306
    :param model_path: Optional, Database model path with the python scripts of the tables
    :param is_secured: If credentials required. Default False
    :param tables_scope:

    :rtype: epyk.core.py.PySql.SqlConn
    """
    if 'pymysql' not in self.pkgs:
      self.pkgs[name] = requires(
        name, reason='Missing Package', install="pymysql", source_script=__file__, raise_except=True)
    database = name
    db_settings = {"loadModel": model_path is not None, 'model_path': model_path or False,
                   "username": "root", "password": "240985", "host": host, "port": port}
    if database not in self._db_bindings:
      self._db_bindings[database] = PySql.SqlConn(
        'mysql+pymysql', database=database, tables_scope=tables_scope, **db_settings)
    return self._db_bindings[database]
