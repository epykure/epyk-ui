
![](https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_whole_big.png)

A module to link Python ecosystem to the JavaScript one.

**Epyk Studio is a wrapper to simplify the use of this module with bespoke configuration / styles. You can download it [here](https://pypi.org/project/epyk-studio/) 
or contribute to the project on the [Github repository](https://github.com/epykure/epyk-studio)**

Presentation
================================
The goal of Epyk is to ensure the implementation of a coherent system using a minimum of layers.
With Epyk the user stays in the Python layer to drive and optimize the data transformation.
This Framework also encourages the implementation of Micro services and cloud based architecture.

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-ui/raw/master/epyk/static/images/concept.PNG">
</div>

Quickstart
================================

For people impatient to inderstand the concept you test the below minimalist dashboard.

Install Epyk

> pip install epyk

The below code will write a simple interactive dashboard relying on internal mock data.

```py
from epyk.core.Page import Report

from epyk.tests import mocks


page = Report()
page.headers.dev()

js_data = page.data.js.record(data=mocks.languages)
filter1 = js_data.filterGroup("filter1")

select = page.ui.select([
  {"value": '', 'name': 'name'},
  {"value": 'type', 'name': 'code'},
])

bar = page.ui.charts.chartJs.bar(mocks.languages, y_columns=["rating", 'change'], x_axis='name')
pie = page.ui.charts.chartJs.pie(mocks.languages, y_columns=['change'], x_axis='name')
page.ui.row([bar, pie])

select.change([
  bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content, 'name')),
  pie.build(filter1.group().sumBy(['change'], select.dom.content, 'name')),
])
```

Compatibility
================================

Epyk is compatible with the most common Web Python Frameworks (Flask and Django).
By default, the server package embeds a Flask app as it is easier to install and ready to use.

The Framework can be included within a Jupyter or JupyterLab project. But this will lead to some limitations - for example Ajax and Socket will not be available.

Web pages generated are compatible with the common modern web frameworks

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-ui/raw/master/epyk/static/images/architecture.PNG">
</div>


But the target is to be full stack developers and be flexible enought to integrate our UI pages to any existing ecosystems.
Thus some outs features are available to wrap page to be visible on any server

This encourage the collaboration and break the IT silos. It can fully work in an Agile way of working as developers, business analysts, product owners and users can work on the same stack 
and improve directly the final product. Any work done on the side within Jupyter or standalone Python scripts can be easily integrated !

<div align="center" >
    <img width=600 src="https://github.com/epykure/epyk-ui/raw/master/epyk/static/images/benefits.PNG">
</div>

Examples are available for some web servers:

In Python
- [Tornado](https://github.com/epykure/epyk-tornado)
- [Flask](https://github.com/epykure/epyk-flask)
- [Django](https://github.com/epykure/epyk-django)
- [Uvicorn](https://github.com/marlyk/epyk-uvicorn)
- [FastAPI](https://github.com/epykure/epyk-fastapi)

In JavaScript, TypeScript or Rust
- [Angular](https://github.com/epykure/epyk-angular) 
- [Vue](https://github.com/epykure/epyk-vue)
- [React](https://github.com/epykure/epyk-react)
- [Node](https://github.com/epykure/epyk-nodejs)
- [Deno](https://github.com/epykure/epyk-deno)

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

Go to the next level and add real time flux in few lines or code. Epyk allows to integrate concepts of Reactive programming thanks
to Python 3 and asyncio. All the features available in JavaScript (socket, websocket, observable ...) can be used as long as the underlying webserver is compatible.

If the underlying web server is not compatible with those modern feature, Ajax (post, get...) are also available.
More examples are available in the []template / interactive](https://github.com/epykure/epyk-templates/tree/master/interactives) section.

<div align="center" >
    <img src="https://github.com/epykure/epyk-ui/blob/master/epyk/static/images/sockets.PNG?raw=true">
</div>

On the client side
```py
page = Report()
page.headers.dev()

socket.connect(url="127.0.0.1", port=3000, namespace="/news")
input = rptObj.ui.input()

pie = rptObj.ui.charts.chartJs.polar([], y_columns=[1], x_axis="x")

container.subscribe(socket, 'news received', data=socket.message['content'])
pie.subscribe(socket, 'news received', data=socket.message['pie'])

rptObj.ui.button("Send").click([
  socket.emit("new news", input.dom.content)
])

page.outs.html_file(path="/templates", name="socket_example")
```


On the server side (using socketio)
```py
from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

 
@socketio.on('new news', namespace='/news')
def new_news(message):
  values = getSeries(5, 100)
  result_pie = chart_data.chartJs.y(values, [1, 4, 5], 'g')
  emit('news received', {"content": message, 'pie': result_pie}, broadcast=True)

```

Export the result in a local HTML page. More example are available on the [official repository](https://github.com/epykure/epyk-templates)

More example are available on Github or in [Jupyter](https://nbviewer.jupyter.org/github/epykure/epyk-templates-notebooks/blob/master/index.ipynb)

Please get in touch if there is any feature you feel Epyk-UI needs.
