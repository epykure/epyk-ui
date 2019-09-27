"""

"""

from epyk.core.py import PyRest


pyrest = PyRest.PyRest()
# content = pyrest.webscrapping(r"https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.theme.mjin.css")
# print(dir(content))
# print(content.code)

import xml.dom.minidom

content = pyrest.webscrapping(r"https://stackoverflow.com/feeds/tag/tabulator")
dom_obj = xml.dom.minidom.parseString(content)

for entry in dom_obj.getElementsByTagName("entry"):
  t = entry.getElementsByTagName("title")[0]
  print(t._get_firstChild().nodeValue)
