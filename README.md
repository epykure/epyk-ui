<div align="center" >
    <img src="https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epykIcon.PNG">
<br/><i>A single module to link Python ecosystem to the Web.</i>

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/epykure/epyk-ui/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/epyk.svg)](https://pypi.python.org/pypi/epyk/)
[![Documentation Status](https://readthedocs.org/projects/epyk-ui/badge/?version=latest)](http://epyk-ui.readthedocs.io/?badge=latest)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/epykure/epyk-ui/issues)
[![Donate](https://img.shields.io/badge/Bitcoin-000?style=for-the-badge&logo=bitcoin&logoColor=white)](https://www.blockchain.com/btc/address/bc1qjhlke0q8g4sk9hdza2afx3ytwp7tmlagsjq9sq)  

</div>

This project is in active and constant improvement so do not forget to run the below command to always get the latest version install.

```
pip install epyk --upgrade
```

## Presentation

### About the project

We started the implementation of Epyk already few years ago in order to help Python developers (from beginner to advanced) to present their work to clients or colleagues. At this time there were only few packages in Python available and it was quite difficult for people to move to web technologies like JS, HTML and CSS.

With this idea we started to create Epyk, a kind of transpiler which is dedicated to assist from Python the developers to develop rich web UI. 
It will try, thanks to the autocompletion provided by the library, to familiarise the developer / data scientist in the wording of web technologies. Indeed we tried as much as possible to keep the same naming convention for CSS attributes and Javascript function to simplify the review of the transpiled HTML page if needed.

Today Epyk is a bit more than a transpiler as it will encompass more than [**100** JavaScript](https://epyk-ui.readthedocs.io/en/latest/report/supported_ext.html#libraries) and CSS modules.

Most of the popular web libraries (JQuery, Bootstrap, ApexCharts, ChartJs, Tabulator, AgGrid...) are available from the Epyk components. The resulting page transpiled will only import the ones needed for the selected components.


## Quickstart

For people impatient to understand the concept, you can test the below minimalist dashboard.

Install Epyk

> pip install epyk

The below code will create a simple interactive dashboard relying on internal mock data.

```py
import epyk as pk

# Just to get mock data to test
from epyk.mocks import randoms

page = pk.Page()
page.headers.dev()

js_data = page.data.js.record(data=randoms.languages)
filter1 = js_data.filterGroup("filter1")

select = page.ui.select([
  {"value": '', 'name': 'name'},
  {"value": 'type', 'name': 'code'},
])

bar = page.ui.charts.chartJs.bar(randoms.languages, y_columns=["rating", 'change'], x_axis='name')
pie = page.ui.charts.chartJs.pie(randoms.languages, y_columns=['change'], x_axis='name')
page.ui.row([bar, pie])

select.change([
  bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content, 'name')),
  pie.build(filter1.group().sumBy(['change'], select.dom.content, 'name')),
])
```

More information in the doc [Getting started with Epyk](https://epyk-ui.readthedocs.io/en/latest/intro/getting-started-with-epyk.html)

## Usage

First install Epyk to your Python environment

### From static pages

```py
pip install epyk
```

Create a report and change CSS3 or add JavaScript events.

```py
import epyk as pk

page = pk.Page()
page.headers.dev()

button = page.ui.button("Click me")
button.style.css.color = "red"
button.click([
    page.js.console.log("log message")
])
.... 

# Then to produce the html page
page.outs.html_file(path="/templates", name="test")
```

### Using a web server

Go to the next level and add real time flux in few lines or code. Epyk allows to integrate concepts of Reactive programming thanks
to Python 3 and asyncio. All the features available in JavaScript (socket, websocket, observable ...) can be used as long as the underlying webserver is compatible.

If the underlying web server is not compatible with those modern features, Ajax (post, get...) are also available.
More examples are available in the []template / interactive](https://github.com/epykure/epyk-templates/tree/master/interactives) section.


On the client side
```py
import epyk as pk

page = pk.Page()
page.headers.dev()

socket.connect(url="127.0.0.1", port=3000, namespace="/news")
input = page.ui.input()

pie = page.ui.charts.chartJs.polar([], y_columns=[1], x_axis="x")

container.subscribe(socket, 'news received', data=socket.message['content'])
pie.subscribe(socket, 'news received', data=socket.message['pie'])

page.ui.button("Send").click([
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

### From Notebooks

We maintain a separate Github repository of Jupyter Notebooks that contain an
interactive tutorial and examples:

https://nbviewer.jupyter.org/github/epykure/epyk-templates-notebooks/

To launch a live notebook server with those notebook using [binder](https://mybinder.org/) click on one of the following badge:

[![Binder](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/epykure/epyk-templates-notebooks/master)


More examples are available on the [official repository](https://github.com/epykure/epyk-templates)


## Compatibility / Open Source Stack

**No dependency hence  the library can be integrated to any existing Python project**

Epyk is compatible with the most common Web Python Frameworks (Flask and Django).
By default, the server package embeds a Flask app as it is easier to install and ready to use.

The Framework can be included within a Jupyter or JupyterLab project. But this will lead to some limitations - for example Ajax and Socket will not be available.

The generated Web pages are compatible with the common modern web frameworks.

[<img src="resources/python.svg" alt="python" height=40>](https://www.python.org)
[<img src="resources/flask.png" alt="flask" height=40>](https://flask.palletsprojects.com/en/2.2.x/)
[<img src="resources/tornado.png" alt="tornad0" height=40>](https://www.tornadoweb.org/en/stable/)
[<img src="resources/django.png" alt="django" height=40>](https://www.djangoproject.com/)
[<img src="resources/fastapi.svg" alt="fastapi" height=40>](https://fastapi.tiangolo.com)
[<img src="resources/jupyter.png" alt="jupyter" height=40>](https://nbviewer.org/github/epykure/epyk-templates-notebooks/blob/master/tutorials/components/00_components.ipynb)
[<img src="resources/collab.png" alt="collab" height=40>](https://colab.research.google.com/drive/12ZL_PHDItSvfILi5akyUc-thd4J8dx6J)
[<img src="resources/react.png" alt="react" height=40>](https://reactjs.org/)
[<img src="resources/angular.png" alt="angular" height=40>](https://angularjs.org/)
[<img src="resources/vue.png" alt="vue">](https://vuejs.org/)
[<img src="resources/svelte.svg" alt="svelte" height=40>](https://svelte.dev)


## Resources

- [Documentation](https://epyk-ui.readthedocs.io/en/latest/)
- [Changelog](CHANGELOG.md)
- [Templates](https://github.com/epykure/epyk-templates/tree/master/tutos)
- [Gallery](https://epykure.github.io/demos/)
- [Collab & Jupyter](https://epykure.github.io/demos/)
- [Stackoverflow](https://stackoverflow.com/search?q=epyk)

## Coming soon

**Epyk Studio** is a rich and collaborative framework to simplify the use of this library with bespoke configuration / styles. You can start downloading it [here](https://pypi.org/project/epyk-studio/) 
or contribute to the project on the [Github repository](https://github.com/epykure/epyk-studio). This is still under development hence it is not yet official released


# Feedback and Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md)

Please get in touch if there is any feature you feel Epyk-UI needs.


# Donate

Want to donate? Feel free. Send to [blockchain](https://www.blockchain.com/btc/address/bc1qjhlke0q8g4sk9hdza2afx3ytwp7tmlagsjq9sq)

[<img src="resources/blockchain_qrcode.PNG" alt="Donate" height=40>](https://www.blockchain.com/btc/address/bc1qjhlke0q8g4sk9hdza2afx3ytwp7tmlagsjq9sq)


