
from epyk.core.py import PyExt


pys = PyExt.PyExt()

print(pys.import_package("sqlalchemy").__name__)