"""
Base Class to create a database and perform SQL operations using the sqlalchemy interface

Documentation
https://www.pythonsheets.com/notes/python-sqlalchemy.html#join-joined-two-tables-via-join-statement

"""

import json
import inspect
import urllib
import importlib
import logging
import sys
import os
import datetime
import traceback

# Check if pandas is available in the current environment
# if it is the case this module can handle Dataframe directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core.js.Imports import requires

# Will automatically add the external library to be able to use this module
sqlalchemy = requires("sqlalchemy", reason='Missing Package', install='sqlalchemy', source_script=__file__)

DATABASE_AUTOSYNC = False


class SqlConn(object):
  def __init__(self, family, database=None, filename=None, model_path=None, reset=False, migrate=True, tables_scope=None, **kwargs):
    """
    Here we try to setup as generic as we can all the variable environment variables for the DB.
    We try to not rely on the rptObj in order to be able to use this interface for various usage
    """
    import sqlalchemy.orm

    self.query = None  # In this design we decided to go to a route where each user will manage his database and also the person who can look at the data
    # This will simplify a lot the permissionning (we consider the storage not a problem at this stage as we split per user
    # Also this could be interesting to check the user data use
    # Some reports can get centralised databases using the module variable SINGLEDB
    dbConfig = {'drivername': kwargs["driver"] if "driver" in kwargs else family, 'username': kwargs.get('username'),
                'password': kwargs.get('password'), 'host': kwargs.get('host'),
                'port': kwargs.get('port'), 'query': kwargs.get('query'), 'database': database}
    self.dbPath = database
    self.username = kwargs.get('username')
    self.userhost = kwargs.get('userhost')
    if kwargs.get('driver', '') == "mssql+pyodbc":
      # Special logic to create a connection to a MS SQl database
      # https://www.linkedin.com/pulse/connecting-sql-database-python-patrick-j-ryan
      try:
        params = urllib.parse.quote_plus('DRIVER=' + kwargs.get('driverName', "{ODBC Driver 17 for SQL Server}") + ';SERVER=' + kwargs['host'] + ';DATABASE=' + database + ';Trusted_Connection=yes;')
      except:
        params = urllib.quote_plus('DRIVER=' + kwargs.get('driverName', "{ODBC Driver 17 for SQL Server}") + ';SERVER=' + kwargs['host'] + ';DATABASE=' + database + ';Trusted_Connection=yes;')
      # echo is dedicated to keep track of changes and store those to logs files
      self.engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect=%s' % params, echo=kwargs.get('echo', False))
    else:
      self.engine = sqlalchemy.create_engine(sqlalchemy.engine.url.URL(**dbConfig), echo=kwargs.get('echo', False))
    self.metadata = sqlalchemy.MetaData(bind=self.engine)
    self.session = sqlalchemy.orm.sessionmaker(bind=self.engine)()
    # The database reflection is only used in some special cases by default (internally for private en public db)
    if tables_scope is None:
      self.metadata.reflect(bind=self.engine)
    else:
      self.metadata.reflect(only=list(tables_scope), bind=self.engine)
    if kwargs.get('reflect', DATABASE_AUTOSYNC):
      self.metadata.create_all(self.engine)
      if model_path:
        self.load_schema(filename=filename, model_path=model_path, reset=reset)

  def _load_sql_file(self, filename, reset):
    """
    Load a database schema from a python file.
    This will use the dialect available from SQLAlchemy

    Documentation
    https://www.sqlalchemy.org/

    :param filename: The database schema python file name
    :param reset: Boolean, flag to specify is the schema needs to be fully reloaded

    :return:
    """
    on_init_fnc = None
    model_mod = importlib.import_module(filename.replace('.py', ''))
    for table_name, table in inspect.getmembers(model_mod):
      if table_name == 'on_init':
        on_init_fnc = table
      elif '__' not in table_name and inspect.isroutine(table) and table.__module__ in filename:
        table_def = getattr(model_mod, table_name)()
        table_def.append(sqlalchemy.Column('lst_mod_dt', sqlalchemy.DateTime, default=datetime.datetime.utcnow, nullable=True))
        if not self.engine.has_table(table_name):
          new_table = sqlalchemy.Table(table_name, self.metadata, *table_def)
          new_table.create(self.engine, checkfirst=True)
        else:
          # Compare the two schema and add the columns if necessary
          # TO DO: Find a way to drop a column without removing the data in the database
          new_cols = set([c.key for c in table_def])
          curr_cols = set([c.key for c in self.metadata.tables[table_name].columns])
          for cn in new_cols.difference(curr_cols):
            for c in table_def:
              if c.key == cn:
                if c.default is not None:
                  self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s DEFAULT %s' % (table_name, cn, c.type.compile(self.engine.dialect), json.dumps(c.default.arg)))
                else:
                  self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, cn, c.type.compile(self.engine.dialect)))
          if reset or table_name in getattr(model_mod, 'RESET_TABLES', []):
            #self.metadata.tables[tableName].drop(self.engine, checkfirst=False)
            new_table = sqlalchemy.Table(table_name, self.metadata, *table_def, extend_existing=True)
            new_table.drop(self.engine, checkfirst=True)
            if not table_name in getattr(model_mod, 'RESET_TABLES', []):
              new_table.create(self.engine, checkfirst=True)
    #We do the part where we run default that need to happen on database creation
    if on_init_fnc:
      on_init_fnc(self)

  def table(self, table_name):
    """
    Return a sqlAlchemy table object. This can be useful in the where clauses

    Example
    db.table('table1')

    :param table_name:
    :return: Python table object
    """
    if self.engine.has_table(table_name):
      return sqlalchemy.Table(table_name, self.metadata)

    raise Exception('Table %s does not exist in the schema' % table_name)

  def load_schema(self, filename=None, model_path=None, reset=False):
    """
    Function that takes care of initialising the DB
    Please note that some column names are prohibited such as lst_mod_dt

    Example

    :param filename: The python module used to get the database schema
    :param model_path: The python path with the model
    :param reset: Boolean, Flag to reset the database. THis will emtpy the tables
    :return:
    """
    if not filename and not model_path:
      raise Exception("You need to specify at least a file name or a model path")

    if model_path:
      sys.path.append(model_path)
      for pyFile in os.listdir(model_path):
        if not pyFile.endswith('.py') or pyFile == '__init__.py':
          continue

        if filename and filename != pyFile:
          continue

        self._load_sql_file(pyFile, reset)
    elif filename:
      self._load_sql_file(filename, reset)

  def table_clone(self, old_table, new_table, mapping=None):
    """
    Helps to migrate between two tables.
    The mapping argument is used in case the column names differ between the two tables

    :param old_table: A SQLAlchemy table class in the current database model
    :param new_table: A SQLAlchemy table class
    :param mapping: Optional, A dictionary for the column names

    :return:
    """
    old_schema = sqlalchemy.Table(old_table, self.metadata)
    new_schema = sqlalchemy.Table(new_table, self.metadata)
    if self.engine.has_table(new_table):
      new_schema.drop(self.engine, checkfirst=True)
    for column in old_schema.columns:
      column.name = mapping.get(column.name, column.name) if mapping else column.name
      new_schema.append_column(column)
    new_schema.create(self.engine, checkfirst=True)
    return self

  def table_migrate(self, from_table, to_table):
    """
    Copy data from one table to another

    :param from_table:
    :param to_table:

    :return: The Python SQL object
    """
    data = list(self.select([from_table]).data())
    self.insert(to_table, data.to_dict('records'), commit=True)
    return self

  def table_create(self, table_name, table_def, reset=False):
    """

    Example
      db = rptObj.db(database=r"newTest.db")
      tableDef = [sqlalchemy.Column('environment', sqlalchemy.String, nullable=False),
                  sqlalchemy.Column('report', sqlalchemy.String, nullable=False),]
      db.createTable('newTable', tableDef)

    :param table_name:
    :param table_def:
    :param reset:

    """
    if not self.engine.has_table(table_name):
      new_table = sqlalchemy.Table(table_name, self.metadata, *table_def)
      new_table.create(self.engine, checkfirst=True)
    else:
      if reset:
        new_table = sqlalchemy.Table(table_name, self.metadata, *table_def)
        new_table.drop(self.engine, checkfirst=True)
        new_table.create(self.engine, checkfirst=True)
    return self

  def table_empty(self, table_name):
    """
    This function will empty an existing table

    Example
    db.emptyTable('test')

    :param table_name: A string with the datable name

    :return: self
    """
    self.delete(table_name)
    logging.info('Content of table %s deleted' % table_name)
    self.commit()
    return self

  def table_create_from_file(self, filename, table_name, records=None, path=None, reset=False, commit=True):
    """

    Example
    df = rptObj.file(htmlCode=r"IBRD_Balance_Sheet__FY2010.csv").read()
    db = rptObj.db(database=r"newTest.db").forceCreate()
    dbObj.createTable('myschema.py', 'mytable', records=df)

    :param filename:
    :param table_name:
    :param records:
    :param path:
    :param reset:
    :param commit:

    :return: The Python SQL object
    """
    self.load_schema(model_path=path, filename=filename, reset=reset)
    if records:
      self.insert(records=records.records(), commit=commit, table_name=table_name)
    return self

  def force_create(self):
    """
    Force the creation of the database in the given project

    :return: The python Sql object
    """
    from sqlalchemy.ext.declarative import declarative_base

    declarative_base().metadata.create_all(self.engine)
    return self

  def load_data_file(self, filename, path, reset=False, new_tables=None):
    """
    Load a python sql file to the local database.
    This will only add records and then commit the changes.

    Those data should not be sensitive ones if they are store and committed to the folder.

    :param filename:
    :param path:
    :param reset:
    :param new_tables:

    :return: The Python SQL object
    """
    sys.path.append(path)
    py_mod = importlib.import_module(filename.replace(".py", ""))
    if hasattr(py_mod, 'data') and hasattr(py_mod, 'target'):
      conn = self.engine.connect()
      header = py_mod.data[0]
      sql_target = self.table(py_mod.target)
      if reset:
        conn.execute(sql_target.delete())
      if py_mod.target in new_tables or new_tables is None:
        if isinstance(header, list):
          for rec in py_mod.data[1:]:
            conn.execute(sql_target.insert().values(dict(zip(header, rec))))
        else:
          for rec in py_mod.data:
            conn.execute(sql_target.insert().values(rec))
    return self

  def where(self, stmts):
    """
    Add a where clause to the SqlAlchemy query.

    Examples
    db.select().where([db.column("table", 'column') == 'X')
    db.select( ['BNP'] ).where([ db.column('BNP', 'date') == '22/04/2013 00:00'] ).toDf()

    :param stmts: The SQL where statement

    :return: The python object itself
    """
    for stmt in stmts:
      self.query = self.query.where(stmt)
    return self

  def select(self, table_name=None, columns=None):
    """
    Create a SQL statement

    Example
    rptObj.db().select(["worldcup_teams"])

    Documentation
    http://docs.sqlalchemy.org/en/latest/core/selectable.html
    http://docs.sqlalchemy.org/en/latest/core/sqlelement.html

    :param table_name: Optional, The database table name
    :param columns: Optional, The list of columns

    :return: self
    """
    if table_name is not None:
      if not isinstance(table_name, list):
        table_name = [table_name]
      tables = [sqlalchemy.Table(table, self.metadata, autoload=True) for table in table_name]
      self.query = sqlalchemy.sql.select(tables)
    elif columns:
      self.query = sqlalchemy.sql.select(columns)
    return self

  def delete(self, table_name):
    """
    Create a SQL delete SQL statement

    Example
    rptObj.db().delete('table1')

    Documentation
    https://docs.sqlalchemy.org/en/13/core/dml.html

    :param table_name: Optional, The database table name
    :return: self
    """
    self.query = sqlalchemy.Table(table_name, self.metadata, autoload=True).delete()
    return self

  def or_(self, *args):
    return sqlalchemy.sql.or_(*args)

  def and_(self, *args):
    return sqlalchemy.sql.and_(*args)

  def order_by(self, col):
    self.query = self.query.order_by(col)
    return self

  def desc(self, val):
    return sqlalchemy.desc(val)

  def asc(self, val):
    return sqlalchemy.asc(val)

  def update(self, table_name, values):
    """
    Create a delete SQL statment

    Example
    rptObj.db().update('table1', {db.column('test', 'name'): 'user'})

    Documentation
    http://docs.sqlalchemy.org/en/latest/core/selectable.html
    http://docs.sqlalchemy.org/en/latest/core/sqlelement.html
    https://docs.sqlalchemy.org/en/13/core/dml.html

    :param table_name:
    :param values:
    :return: self
    """
    self.query = sqlalchemy.Table(table_name, self.metadata, autoload=True).update(values=values)
    return self

  def distinct(self, columns=None):
    """

    :param columns:
    :return:
    """
    if columns is None:
      self.query = self.query.distinct()
    else:
      self.query = self.query.distinct(columns)
    return self

  def get_last_id(self, table_name):
    """
    Return the table last primary key ID.
    This will return an error if the table does not have a primary key defined in its schema

    Example
    db.get_last_id("table")

    :param table_name: The table name
    :return: Returh the last row ID or -1
    """
    table = sqlalchemy.Table(table_name, self.metadata)
    try:
      row = self.session.query(table).order_by(list(table.primary_key.columns)[0].desc()).first()
    except:
      raise Exception("No primary key defined for the table %s - db: %s" % (table_name, self.dbPath))

    if row is None:
      return -1

    rec = dict(zip(row.keys(), row))
    return rec[list(table.primary_key.columns)[0].key]

  def insert(self, table_name, records, commit=False, col_user_name=None, clean_rec=False, getIdCol=False):
    """
    insert a list of records to a table

    Example
    db.insert('table1',[{'name': 'test'}], commit=True)
    db.insert("table", {"user_name": "Test", "data": "test"}, commit=True)

    Documentation
    https://docs.sqlalchemy.org/en/13/core/dml.html
    https://docs.sqlalchemy.org/en/13/core/dml.html

    :param table_name: The database table name
    :param records: The list of dictionaries with the data to inserts
    :param commit: Optional, Boolean to commit the insert. Set to False by default
    :param col_user_name:
    :param clean_rec: Optional, remove the key in the dictionaries which are not related to the table. Set to False
    :param getIdCol:

    :return: The python object itself
    """
    dflt = {'lst_mod_dt': datetime.datetime.utcnow()}
    error_count, error_log, last_id = 0, [], None
    table = sqlalchemy.Table(table_name, self.metadata)
    if not self.engine.has_table(table.name):
      raise Exception("Table %s does not exist" % table.name)

    if col_user_name is not None:
      dflt[col_user_name] = self.username
    if 'hostname' in self.columns(table_name):
      dflt['hostname'] = self.userhost
    if isinstance(records, dict):
      records = [records]
    if clean_rec:
      # This is done to remove the extra columns in the rec before creating the SQL statement
      tableCols = [str(col).split(".")[1] for col in table.columns]
      for rec in records:
        try:
          row = {}
          for c in tableCols:
            if c in rec:
              row[c] = rec[c]
          row.update(dflt)
          result = self.session.execute(table.insert().values(row))
          last_id = result.inserted_primary_key
        except Exception as err:
          logging.warning(traceback.format_exc())
          error_count += 1
          error_log.append(str(traceback.format_exc()).strip().split('\n')[-1])
    else:
      for rec in records:
        try:
          tmpRec = dict(rec)
          tmpRec.update(dflt)
          result = self.session.execute(table.insert().values(tmpRec))
          last_id = result.inserted_primary_key
        except Exception as err:
          logging.warning(traceback.format_exc())
          error_count += 1
          error_log.append(str(traceback.format_exc()).strip().split('\n')[-1])
    if commit:
      self.session.commit()
    if error_count:
      return (False, error_count, error_log, last_id)

    return (True, 0, [], last_id)

  def data(self, limit=None):
    """
    Returns the results of the select statement previously instantiated in a pandas dataframe

    Example
    rptObj.db().getData()

    :param limit: Optional. The number of records to be returned

    :return: A pandas dataframe
    """
    if self.query is None:
      return None

    try:
      import pandas

      if limit:
        return pandas.read_sql(self.query, self.query.bind).head(limit)

      return pandas.read_sql(self.query, self.query.bind)
    except:
      # No pandas installed
      return list(self.execute())

  @property
  def records(self):
    """
    Return the records

    Example
    for rec in db.select("table").records:
      print(rec)

    :return: A iterator for the SQL result
    """
    if has_pandas:
      for rec in self.data().to_dict('records'):
        yield rec

    else:
      for rec in self.data():
        yield dict(rec.items())

  @property
  def count(self):
    """
    Return the number of records

    Example
    print(db.select("table").count)

    :return: The number of records
    """
    results = self.data()
    if has_pandas:
      return results.count

    return len(results)

  def limit(self, n):
    """
    Limit the number of records returned

    :param n: Integer, the number of records
    :return: The SQL Query object
    """
    if self.query is None:
      return None

    self.query = self.query.limit(n)
    return self

  def first(self, items=False):
    """
    Return only the first items from the SQL query

    Example
    print(db.first())
    print(db.first(items=True))

    :param items: Return a dictionary or a list of data
    :return: None or the first record
    """
    self.limit(1)
    try:
      if items:
        row = self.engine.connect().execute(self.query).next()
        return dict(row.items())

      return self.engine.connect().execute(self.query).next()

    except StopIteration:
      return None

  def fetch(self, limit=None):
    """
    Similar to getData but return an iterator over a list instead of using pandas

    Example
    rptObj.db().fetch()

    :param limit: The maximum number of data returned in the SQL query
    :return: An iterator over the result of the query
    """
    if self.query is None:
      yield None

    counter = 0
    if not limit:
      limit = -1
    for row in self.engine.connect().execute(self.query):
      if limit == -1 or counter < limit:
        counter += 1
        yield row

      else:
        raise StopIteration

  @property
  def tables(self):
    """
    Return the list of tables defined in the selected database

    Example
    rptObj.db().tables()

    :return: A python object with the list of tables
    """
    return self.engine.table_names()

  def columns(self, table_name):
    """
    Return the list of columns defined in the selected database

    Example
    rptObj.db().columns("table_name")

    :param table_name:
    :return: A python object with the list of tables
    """
    table = sqlalchemy.Table(table_name, self.metadata)
    if self.engine.has_table(table.name):
      return table.columns

    raise Exception('Table does not exist')

  def column(self, table_name, column_name):
    """
    Return a sqlAlchemy column object. This can be useful in the where clauses

    Example
    select('table').where([db.column("table", 'column') == 'X')

    :param table_name: The database table name
    :param column_name: The column name
    :return: Python column object
    """
    table = sqlalchemy.Table(table_name, self.metadata, autoload=True)
    if self.engine.has_table(table.name):
      return getattr(table.c, column_name)

  def drop(self, table_name, validate=True):
    """
    Delete the table from the database.
    The pre check can be disabled and the table will be automatically created again when the report will be triggered again.
    No extra function to create a table in the framework this is done by the SQL framework itself

    Example
    rptObj.db().drop('test')
    rptObj.db().drop('test', withCheck=False)

    Documentation
    https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.ResultProxy

    :param table_name: The database table name
    :param validate: Boolean, Validation check before dropping the table
    :return: Python column object
    """
    if validate:
      try:
        name = input("Are you sure to delete the table %s (Y/N)? " % table_name)
      except:
        name = raw_input("Are you sure to delete the table %s (Y/N)? " % table_name)
      if name == 'Y':
        sqlalchemy.Table(table_name, self.metadata, autoload=True).drop()
        logging.info("Table %s deleted" % table_name)
    else:
      sqlalchemy.Table(table_name, self.metadata, autoload=True).drop()
      logging.info("Table %s deleted" % table_name)

  def execute(self):
    """
    Execute the current SQL query

    Documentation
    https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.ResultProxy

    :return: The SQL Result proxy
    """
    return self.engine.execute(self.query)

  def commit(self):
    """
    Commit the current transaction.

    THis will save the results in the database

    :return: The SQL object
    """
    self.session.commit()
    return self


class SqlConnOdbc(object):
  """
  Connector to Access databases. This connector will allow you to create, store and retrieve data from any MS Access Database.
  This will return the SQL database object. It will be possible to reuse the same syntax to then interact with it.

  This would need the ODBC driver available here: https://www.microsoft.com/en-us/download/confirmation.aspx?id=13255
  """

  def __init__(self, database=None, **kwargs):
    self.query = {}
    pyodbc = requires("pyodbc", reason='Missing Package', install='sqlalchemy', source_script=__file__)
    dbAttr = {'Driver': kwargs['driver'], 'DBQ': database}
    for opt in [('password', 'PWD'), ('username', 'UID')]:
      if kwargs.get(opt[0]) is not None:
        dbAttr[opt[1]] = kwargs[opt[0]]
    dbStr = []
    for k in ['Driver', 'DBQ', 'PWD', 'UID']:
      if k in dbAttr:
        dbStr.append("%s=%s" % (k, dbAttr[k]))
    self.conn = pyodbc.connect(";".join(dbStr))

  def select(self, tableNames):
    if not isinstance(tableNames, list):
      tableNames = [tableNames]
    self.query = {'tables': tableNames}
    return self

  def columns(self, tableName, columnName):
    if 'columns' not in self.query:
      self.query['columns'] = []
    self.query['columns'].append(self.column(tableName, columnName))
    return self

  def where(self, stmts):
    self.query['wheres'] = []
    for stmt in stmts:
      self.query['wheres'].append(stmt)
    return self

  def column(self, tableName, columnName):
    return "%s.%s" % (tableName, columnName)

  @property
  def sql(self):
    strSql = "SELECT %s FROM %s" % (", ".join(self.query.get('columns', ['*'])), ", ".join(self.query['tables']))
    if len(self.query.get('wheres', [])) > 0:
      strSql = "%s WHERE %s" % (strSql, " and ".join(self.query['tables']))
    return strSql

  def insert(self, tableName, records, commit=False, colUserName=None):
    for rec in records:
      row = "(%s" % json.dumps(rec[0]).replace('"', "'")
      for r in rec[1:]:
        row = "%s,%s" % (row, json.dumps(r).replace('"', "'"))
      row = "%s)" % row
      cursor = self.conn.execute('insert into %s values%s' % (tableName, row))
      if commit:
        cursor.commit()

  def data(self, limit=None):
    cursor = self.conn.cursor()
    return [rec for rec in cursor.execute(self.sql())]

  @property
  def tables(self):
    """

    :return:
    """
    cursor = self.conn.cursor()
    return [row.table_name for row in cursor.tables()]


class SqlConnNeo4j(object):
  def __init__(self, host=None, port=None, usr=None, pwd=None):
    import neo4j
    self.driver = neo4j.GraphDatabase.driver('bolt://%s:%s' % (host, port), auth=(usr, pwd))
    self.query = []

  def raw_query(self, query):
    try:
      with self.driver.session() as session:
        for rec in session.run(query):
          yield rec

    except:
      raise StopIteration

  def create(self):
    self.query.append('CREATE')
    return self

  def match(self):
    self.query.append('MATCH')
    return self

  def foreach(self, conditions):
    """

    """
    raise NotImplemented

  def where(self, condition):
    return self

  def delete(self, node_names, detach=False):

    if detach:
      self.query.append('DETACH')
    self.query.append('DELETE %s' % ','.join(node_names))
    try:
      with self.driver.session() as session:
        session.run(self.compose(self.query))
        self.query = []
        return True

    except:
      print(traceback.format_exc())
      self.query = []
      return False

  def retrieve(self, names):
    self.query.append('RETURN')
    self.query.append(','.join(names))
    return self

  def clear(self):
    """
    :dsc: Clears all nodes and edges from the Database
    """
    return self.match().node('n').delete(['n'], detach=True)

  def node(self, name='', labels=None, attr=None):
    """
    :dsc: adds the node patern to the query
    """
    if not labels:
      labels = []
    else:
      labels[0] = ':%s' % labels[0]
    if not attr:
      attr = ''
    else:
      tmp_attr_list = []
      for attr_key, attr_value in attr.items():
        tmp_attr_list.append('%s: "%s"' % (attr_key, attr_value))
      attr = '{%s}' % ','.join(tmp_attr_list)
    self.query.append("(%s%s %s)" % (name, ':'.join(labels), attr))
    return self

  def link(self, labels='', attr=None, direction="from"):
    """
    :dsc: adds the edge definition to the query
    """
    if direction == 'from':
      self.query.append('-[%s]->' % labels)
    else:
      self.query.append('<-[%s]-' % labels)
    return self

  def alias(self, aliases):
    """
    :dsc: defines a set of aliases that will appear as WITH a, b, c, d as count(id)
    The aliases argument will be defined as follows: ['a', 'b', 'c', {'d': 'count(id)'}]
    """
    self.query.append('WITH')
    tmp_query = []
    for expression in aliases:
      if isinstance(expression, dict):
        for expr, alias in expression.items():
          tmp_query.append('%s as %s' % (expr, alias))
      else:
        tmp_query.append(expression)
    self.query.append(', '.join(tmp_query))
    return self

  def compose(self, query):
    """
    :dsc: Simply joins the query clauses all together
    """
    return ' '.join(query)

  def execute(self):
    try:
      with self.driver.session() as session:
        for rec in session.run(self.compose(self.query)):
          yield rec

    except Exception as err:
      print(traceback.format_exc())
      raise StopIteration



