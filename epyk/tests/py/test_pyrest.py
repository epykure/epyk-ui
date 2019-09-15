"""

"""

from epyk.core.py import PyRest


pyrest = PyRest.PyRest()
content = pyrest.webscrapping(r"https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.theme.mjin.css")
print(dir(content))
print(content.code)
