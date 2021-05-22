Javascript Built-Ins
====================

Most of the JavaScript features are wrapped in Epyk in order to be able to use the auto completion to write JavaScript code.
By design this framework is not dedicated to write thousand of lines of JavaScript. It has been implemented in order to help
link components and modules with the Python object.

This module can be split into 4 main items:

- JavaScript core features.
- JavaScript Primitives.
- JavaScript HTML wrappers.
- JavaScript Packages wrappers.


Core Modules
*************

.. autoclass:: epyk.core.js.Js.JsBase
  :members:


JavaScript features
*******************

Console
-------

.. autoclass:: epyk.core.js.Js.JsConsole
  :members:

Json
----

.. autoclass:: epyk.core.js.Js.JsJson
  :members:

BreadCrumb
------------

.. autoclass:: epyk.core.js.Js.JsBreadCrumb
  :members:

Screen
------

.. autoclass:: epyk.core.js.Js.JsScreen
  :members:

Maths
------

.. autoclass:: epyk.core.js.Js.JsMaths.JsMaths
  :members:

Location
---------

.. autoclass:: epyk.core.js.Js.JsLocation.JsLocation
  :members:

.. autoclass:: epyk.core.js.Js.JsLocation.URLSearchParams
  :members:

Navigator
---------

.. autoclass:: epyk.core.js.Js.JsMaths.JsNavigator
  :members:

.. autoclass:: epyk.core.js.Js.JsMaths.JsGeolocation
  :members:

Window
------

.. autoclass:: epyk.core.js.Js.JsWindow
  :members:

.. autoclass:: epyk.core.js.Js.JsWindowEvent
  :members:

.. autoclass:: epyk.core.js.Js.JsHistory
  :members:

.. autoclass:: epyk.core.js.Js.JsSessionStorage
  :members:

.. autoclass:: epyk.core.js.Js.JsLocalStorage
  :members:

.. autoclass:: epyk.core.js.Js.JsUrl
  :members:

WebWorkers
---------

Web Workers are a simple means for web content to run scripts in background threads.
The worker thread can perform tasks without interfering with the user interface.

It is possible to create and to use web worker with Epyk. To do so it is possible to use them in a dedicated page or
in a Jupyter Notebook::

    w2 = page.js.worker()
    w2.connect(content='''
    self.addEventListener('message', function(e) {
      var data = e.data; console.log(data);
      switch (data.cmd) {
        case 'add':
          self.postMessage('Result: ' + (data.value1 + data.value2 + data.value3)); break;
        case 'mult':
          self.postMessage('Result: ' + (data.value1 * data.value2 * data.value3)); break;
        case 'stop':
          self.postMessage('WORKER STOPPED: ' + data.msg + '. (buttons will no longer work)');
          self.close(); break;
        default:
          self.postMessage('Unknown command: ' + data.msg);
      };
    }, false);
    ''')

    slider = page.ui.slider()
    number = page.ui.fields.number()

    div = page.ui.div()
    page.ui.button("Add").click([w2.postMessage({'cmd': 'add', 'value1': 2}, components=[(slider, "value2"), (number, "value3")])])
    page.ui.button("Mult").click([w2.postMessage({'cmd': 'mult', 'value1': 5}, components=[(slider, "value2"), (number, "value3")])])

    page.ui.button("Stop worker").click([w2.postMessage({'cmd': 'stop'})])

More details on the web workers are available in the functions documentation.

Websocket
---------

.. autoclass:: epyk.core.js.Js.JsWebSocket.WebSocket
  :members:

Performance
-----------

.. autoclass:: epyk.core.js.Js.JsPerformance.JsPerformance
  :members:
