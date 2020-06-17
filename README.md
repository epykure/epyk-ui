
![](https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_whole_big.png)

A module to link Python ecosystem to the JavaScript one.

Presentation
================================
The goal of Epyk is to ensure the implementation of a coherent system using a minimum of layers.
With Epyk the user stays in the Python layer to drive and optimize the data transformation.
This Framework also encourages the implementation of Micro services and cloud based architecture.

![](./epyk/static/images/concept.PNG)


Compatibility
================================

Epyk is compatible with the most common Web Python Frameworks (Flask and Django).
By default, the server package embeds a Flask app as it is easier to install and ready to use.

The Framework can be included within a Jupyter or JupyterLab project. But this will lead to some limitations - for example Ajax and Socket will not be available.

Web pages generated are compatible with the common modern web frameworks

![](./epyk/static/images/architecture.PNG)

But the target is to be full stack developers and be flexible enought to integrate our UI pages to any existing ecosystems.
Thus some outs features are available to wrap page to be visible on any server

This encourage the collaboration and break the IT silos. It can fully work in an Agile way of working as developers, business analysts, product owners and users can work on the same stack 
and improve directly the final product. Any work done on the side within Jupyter or standalone Python scripts can be easily integrated !

![](./epyk/static/images/benefits.PNG)

Usage
======

First install Epyk to your Python environment

```py
pip install epyk
```

Create a report and change CSS3 or add JavaScript events

```py
from epyk.core.Page import Report

page = Report()
page.headers.dev()

button = page.ui.button("Click me")
button.style.css.color = "red"
button.click([
    page.js.console.log("log message")
])
.... 

page.outs.html_file(path="/templates", name="test")
```

Go to the next level and add real time flux in few lines or code

```py
page = Report()

page.headers.dev()


page.outs.html_file(path="/templates", name="listener")
```

Export the result in a local HTML page.

More example are available on Github or in Jupyter

Please get in touch if there is any feature you feel Epyk-UI needs.
