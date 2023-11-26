
from epyk.core.py import types

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class GS(JsPackage):
  lib_alias = {"js": 'gridstack', 'css': 'gridstack'}

  def added(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """Called when widgets are being added to a grid

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('added', function(event, items){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def change(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """Occurs when widgets change their position/size due to constrain or direct change

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('change', function(event, items){let data = items; %s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def disable(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """
    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('disable', function(event){let grid = event.target.gridstack; %s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def dragstart(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called when grid item is starting to be dragged.

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('dragstart', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def drag(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called when grid item is starting to be dragged.

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('drag', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def dragstop(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called after the user is done moving the item, with updated DOM attributes.

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('dragstop', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def dropped(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called when an item has been dropped and accepted over a grid. If the item came from another grid, the
    previous widget node info will also be sent (but dom item long gone).

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('dropped', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def enable(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """
    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('enable', function(event){let grid = event.target.gridstack; %s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def removed(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('removed', function(event, items){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def resizestart(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called before the user starts resizing an item

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('resizestart', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def resize(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called while grid item is being resized, for each new row/column value (not every pixel)

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('resize', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def resizestop(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
    """called after the user is done resizing the item, with updated DOM attributes.

    `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#addedevent-items>`_
    """
    return JsObjects.JsVoid("%s.on('resizestop', function(event, el){%s})" % (
      self.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def init_(self, attrs: dict = None, html_code: str = None):
    return JsObjects.JsVoid("var %s = GridStack.init(%s, '%s')" % (
      html_code or self.component.html_code, self.component.options.config_js(attrs),
      html_code or self.component.html_code))

  def initAll(self, attrs: dict = None, selectpr: str = '.grid-stack'):
    return JsObjects.JsVoid("GridStack.init(%s, '%s')" % (
      self.component.options.config_js(attrs), selectpr))

  def addComponent(self, component):
    component.options.managed = False
    return JsObjects.JsVoid("%s.addWidget('%s')" % (self.varName, component.html()))
