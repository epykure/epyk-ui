"""
Module in charge of the testing of the different CSS features
"""

from epyk.core.Page import Report


# Create a basic report object
rptObj = Report()

# Create a text component on the page
text = rptObj.ui.text("test")

# Change the CSS Style
# Add the no_border style (ctrl + q) for the style documentation
text.style.div.no_border()
print(text.style.list)

# Remove the class from the list
text.style.div.no_border().remove()
print(text.style.list)

# create an anonymous class
cls_name = rptObj.style.anonymous_cls({"color": "red"})
# Add the class to the class list
text.style.addCls(cls_name)
print(text.style.list)


