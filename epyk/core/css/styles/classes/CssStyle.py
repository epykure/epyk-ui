
from epyk.core.css import Properties


class Data(Properties.CssMixin):
  def __init__(self, css_ovrs, selector):
    self.htmlObj = self
    self._content = css_ovrs or {}
    self.__selector = selector
    self.has_changed = False

  def css(self, k, v=None, important=False, change=True):
    """

    :param k:
    :param v:
    :param important:
    :param change:

    :return:
    """
    if change:
      self.has_changed = True
    if not isinstance(k, dict) and v is not None:
      k = {k: v}
    for attr, val in k.items():
      if important:
        val = "%s !IMPORTANT" % val
      self._content[attr] = val
    return self

  def clear(self):
    """
    Clear all the CSS attributes defined for this class

    :return: Self to allow the chaining
    """
    self.has_changed = True
    self._content = {}
    return self

  @property
  def selector(self):
    return self.__selector

  def __str__(self):
    if self._content:
      return "{%s;}" % ";".join(["%s: %s " % (k, v) for k, v in self._content.items()])

    return ""


class Selector(object):
  def __init__(self, selector_ovrs):
    map_fncs = {"parent": "parent_element", "child": "sub_element"}
    self.__this = selector_ovrs["classname"]
    del selector_ovrs["classname"]
    for k, v in selector_ovrs.items():
      getattr(self, map_fncs.get(k, k))(v)
    self.__element = False

  def elements(self, element_types):
    """
    Selects all <div> elements and all <p> elements

    Documentation
    https://www.w3schools.com/cssref/sel_element_comma.asp

    :param element_types:
    :return:
    """
    if not isinstance(element_types, list):
      element_types = [element_types]
    if self.__element:
      self.__this = "%s,%s" % (",".join(element_types), self.__this)
    else:
      self.__this = "%s%s" % (",".join(element_types), self.__this)
      self.__element = True
    return self

  def sub_element(self, element, direct_parent=False, class_name=None):
    """
    Selects all <p> elements inside <div> elements

    Documentation
    https://www.w3schools.com/cssref/sel_element_element.asp

    :param element:
    :return:
    """
    if direct_parent:
      self.__this = "%s > %s" % (self.__this, element)
    else:
      self.__this = "%s %s" % (self.__this, element)
    return self

  def parent_element(self, element, direct_parent=False, class_name=None):
    """
    Selects all <p> elements inside <div> elements

    Documentation
    https://www.w3schools.com/cssref/sel_element_element.asp

    :param element:
    :return:
    """
    if direct_parent:
      self.__this = "%s > %s" % (element, self.__this)
    else:
      self.__this = "%s %s" % (element, self.__this)
    return self

  def with_next_element(self, element, class_name=None):
    """
    Selects all <p> elements that are placed immediately after <div> elements

    Documentation
    https://www.w3schools.com/cssref/sel_element_pluss.asp

    :param element:
    :return:
    """
    self.__this = "%s + %s" % (self.__this, element)
    return self

  def with_prev_element(self, element, class_name=None):
    """
    Selects every <ul> element that are preceded by a <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_gen_sibling.asp

    :param element:
    :return:
    """
    self.__this = "%s ~ %s" % (self.__this, element)
    return self

  def join_class(self, class_name):
    """
    Selects all elements with both name1 and name2 set within its class attribute

    Documentation

    :param class_name:
    :return:
    """
    self.__this = "%s.%s" % (self.__this, class_name)
    return self

  def add_class(self, class_name):
    """
    Selects all elements with name2 that is a descendant of an element with name1

    :param class_name:
    :return:
    """
    self.__this = "%s .%s" % (self.__this, class_name)
    return self

  def sub_class(self, class_name, direct_parent=False):
    """
    Selects all <p> elements inside <div> elements

    Documentation
    https://www.w3schools.com/cssref/sel_element_element.asp

    :param class_name:
    :return:
    """
    if direct_parent:
      self.__this = "%s > .%s" % (self.__this, class_name)
    else:
      self.__this = "%s .%s" % (self.__this, class_name)
    return self

  def element(self, bool=None):
    """

    :param element:
    :return:
    """
    if bool is None:
      return self.__element

    self.__element = bool
    return self

  def add_element_id(self, htmlObj):
    """
    Selects the element with id="firstname"

    Documentation
    https://www.w3schools.com/cssref/sel_id.asp

    :param htmlObj:
    :return:
    """
    self.__this = "%s%s" % (htmlObj.htmlCode, self.__this)
    return self

  def not_element(self, element):
    """
    Selects every element that is not a <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_not.asp

    :param element:
    :return:
    """
    self.__this = "%s:not(%s)" % (self.__this, element)
    return self

  def first_child(self):
    """
    Selects every <p> element that is the first child of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_firstchild.asp

    :return:
    """
    self.__this = "%s:first-child" % self.__this
    return self

  def first_letter(self):
    """
    Selects the first letter of every <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_firstletter.asp

    :return:
    """
    self.__this = "%s::first-letter" % self.__this
    return self

  def first_line(self):
    """
    Selects the first line of every <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_firstline.asp

    :return:
    """
    self.__this = "%s::first-line" % self.__this
    return self

  def first_of_type(self):
    """
    Selects every <p> element that is the first <p> element of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_first-of-type.asp

    :return:
    """
    self.__this = "%s:first-of-type" % self.__this
    return self

  def in_range(self):
    """
    Selects input elements with a value within a specified range

    Documentation
    https://www.w3schools.com/cssref/sel_in-range.asp

    :return:
    """
    self.__this = "%s:in-range" % self.__this
    return self

  def last_child(self):
    """
    Selects every <p> element that is the last child of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_last-child.asp

    :return:
    """
    self.__this = "%s:last-child" % self.__this
    return self

  def last_of_type(self):
    """
    Selects every <p> element that is the last <p> element of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_last-of-type.asp

    :return:
    """
    self.__this = "%s:last-of-type" % self.__this
    return self

  def link(self):
    """
    Selects all unvisited links

    Documentation
    https://www.w3schools.com/cssref/sel_link.asp

    :return:
    """
    self.__this = "%s:link" % self.__this
    return self

  def nth_child(self, n):
    """
    Selects every <p> element that is the second child of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_nth-child.asp

    :param n:
    :return:
    """
    self.__this = "%s:nth-child(%s)" % (self.__this, n)
    return self

  def nth_last_child(self, n):
    """
    Selects every <p> element that is the second child of its parent, counting from the last child

    Documentation
    https://www.w3schools.com/cssref/sel_nth-last-child.asp

    :param n:
    :return:
    """
    self.__this = "%s:nth-last-child(%s)" % (self.__this, n)
    return self

  def nth_last_of_type(self, n):
    """
    Selects every <p> element that is the second <p> element of its parent, counting from the last child

    Documentation
    https://www.w3schools.com/cssref/sel_nth-last-of-type.asp

    :param n:
    :return:
    """
    self.__this = "%s:nth-last-of-type(%s)" % (self.__this, n)
    return self

  def nth_of_type(self, n):
    """
    Selects every <p> element that is the second <p> element of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_nth-of-type.asp

    :param n:
    :return:
    """
    self.__this = "%s:nth-of-type(%s)" % (self.__this, n)
    return self

  def only_of_type(self):
    """
    Selects every <p> element that is the only <p> element of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_only-of-type.asp

    :return:
    """
    self.__this = "%s:only-of-type" % self.__this
    return self

  def only_child(self):
    """
    Selects every <p> element that is the only child of its parent

    Documentation
    https://www.w3schools.com/cssref/sel_only-child.asp

    :return:
    """
    self.__this = "%s:only-child" % self.__this
    return self

  def placeholder(self):
    """
    Selects input elements with placeholder text

    Documentation
    https://www.w3schools.com/cssref/sel_placeholder.asp

    :return:
    """
    self.__this = "%s::placeholder" % self.__this
    return self

  def read_only(self):
    """
    Selects input elements with the "readonly" attribute specified

    Documentation
    https://www.w3schools.com/cssref/sel_read-only.asp

    :return:
    """
    self.__this = "%s:read-only" % self.__this
    return self

  def read_write(self):
    """
    Selects input elements with the "readonly" attribute NOT specified

    Documentation
    https://www.w3schools.com/cssref/sel_read-write.asp

    :return:
    """
    self.__this = "%s:read-write" % self.__this
    return self

  def __str__(self):
    return self.__this


class Style(object):
  classname, classnames = None, None

  def __init__(self, rptObj, css_ovrs=None, selector_ovrs=None, html_id=None):
    self.rptObj, self.html_id, self.cls_ref = rptObj, html_id, None
    css_ovrs = css_ovrs or {}
    self.__keyframes = {}
    selector_ids = dict(getattr(self, '_selectors', {}))
    if self.classname is None:
      self.classname = self.__class__.__name__.lower()
    if self.classnames is not None:
      self.classname = " .".join(self.classnames)
    selector_ids["classname"], self.classname = ("%s", "") if self.classname == False else (".%s", self.classname)
    if getattr(self, '_selector', None) is not None:
      self.classname = self._selector
    if selector_ovrs is not None:
      self.__has_changed = True
      selector_ids.update(selector_ovrs)
    self.__selector = Selector(selector_ids)

    self.__attrs, self.__hover, self.__focus = dict(getattr(self, '_attrs', {})), dict(getattr(self, '_hover', {})), dict(getattr(self, '_focus', {}))
    self.__checked, self.__disabled, self.__empty = dict(getattr(self, '_checked', {})), dict(getattr(self, '_disabled', {})), dict(getattr(self, '_empty', {}))
    self.__enabled, self.__invalid, self.__valid = dict(getattr(self, '_enabled', {})), dict(getattr(self, '_invalid', {})), dict(getattr(self, '_valid', {}))
    self.__visited, self.__after, self.__before = dict(getattr(self, '_visited', {})), dict(getattr(self, '_after', {})), dict(getattr(self, '_before', {}))
    self.__active = dict(getattr(self, '_active', {}))

    # More bespoke items
    self.__webkit_slider_thumb = dict(getattr(self, '_webkit_slider_thumb', {}))
    self.__internal_props = ["attrs", "hover", "focus", "checked", "valid", "disabled", "empty", "enabled", "invalid"]
    self.customize()
    for k in self.__internal_props:
      s = getattr(self, k)
      s.has_changed = False
    self.__has_changed = False
    if css_ovrs:
      for k, v in css_ovrs.items():
        if k in self.__internal_props:
          getattr(self, k).css(k, v)
        else:
          self.attrs.css(k, v)

  def customize(self):
    pass

  def transition(self, attribute, duration=2, delay=None, iteration=None, timing_fnc=None):
    """

    :param attribute:
    :param duration:
    :param delay:
    :param iteration:
    :param timing_fnc:
    """
    css_transition = {"transition-property": attribute, "transition-duration": "%ss" % duration}
    if delay:
      css_transition["transition-delay"] = "%ss" % delay
    if iteration:
      css_transition["transition-iteration-count"] = iteration
    if timing_fnc is not None:
      if timing_fnc not in ["ease", "linear", "ease-in", "ease-out", "ease-in-out"] and not timing_fnc.startswith("cubic-bezier"):
        raise Exception("%s missing from the list" % timing_fnc)

      css_transition["transition-timing-function"] = timing_fnc
    # Add the -webkit- prefix for compatibility with some browsers
    safari_css = dict([("-webkit-%s" % k, v) for k, v in css_transition.items()])
    css_transition.update(safari_css)
    self.css(css_transition, change=False)
    return self

  def animation(self, name=None, attrs=None, duration=2, delay=None, iteration='infinite', timing_fnc=None, effect=None, fill_mode=None):
    """
    The @keyframes rule specifies the animation code.

    The animation is created by gradually changing from one set of CSS classes to another.

    Example
    rptObj.ui.button("Ok").style.css_class.animation('test', {
      "from": {"border-color": "white"},
      "to": {"border-color": "red"},
    })

    Documentation
    https://www.w3schools.com/cssref/css3_pr_animation-keyframes.asp
    https://www.w3schools.com/css/css3_animations.asp

    :param effect: Effect Class.
    :param name: String. Required. Defines the name of the animation.
    :param attrs: String. Required. Percentage of the animation duration.
    :param duration:
    :param delay:
    :param iteration:
    :param timing_fnc:
    :param fill_mode: String Specify the fill mode (whether the style should go back to its original position or something else etc...
    """
    name = self.keyframes(name, attrs, effect)
    css_animation = {"animation-name": name, "animation-duration": "%ss" % duration}
    if delay:
      css_animation["animation-delay"] = "%ss" % delay
    if iteration:
      css_animation["animation-iteration-count"] = iteration
    if fill_mode:
      css_animation['animation-fill-mode'] = fill_mode
    if timing_fnc is not None:
      if timing_fnc not in ["ease", "linear", "ease-in", "ease-out", "ease-in-out"] and not timing_fnc.startswith(
        "cubic-bezier"):
        raise Exception("%s missing from the list" % timing_fnc)

      css_animation["animation-timing-function"] = timing_fnc
    # Add the -webkit- prefix for compatibility with some browsers
    safari_css = dict([("-webkit-%s" % k, v) for k, v in css_animation.items()])
    css_animation.update(safari_css)
    self.css(css_animation, change=False)
    return self

  @property
  def selector(self):
    return self.__selector

  @property
  def attrs(self):
    if self.__attrs is None or isinstance(self.__attrs, dict):
      self.__attrs = Data(self.__attrs or {}, self.__selector)
    return self.__attrs

  @property
  def hover(self):
    """
    Selects links on mouse over

    Documentation
    https://www.w3schools.com/cssref/sel_hover.asp

    :return:
    """
    if self.__hover is None or isinstance(self.__hover, dict):
      self.__hover = Data(self.__hover or {}, self.selector)
    return self.__hover

  @property
  def checked(self):
    """
    Selects every checked <input> element

    Documentation
    https://www.w3schools.com/cssref/sel_checked.asp

    :return:
    """
    if self.__checked is None or isinstance(self.__checked, dict):
      self.__checked = Data(self.__checked or {}, self.selector)
    return self.__checked

  @property
  def disabled(self):
    """
    Selects every disabled <input> element

    Documentation
    https://www.w3schools.com/cssref/sel_disabled.asp

    :return:
    """
    if self.__disabled is None or isinstance(self.__disabled, dict):
      self.__disabled = Data(self.__disabled or {}, self.selector)
    return self.__disabled

  @property
  def focus(self):
    """
    Selects the input element which has focus

    Documentation
    https://www.w3schools.com/cssref/sel_focus.asp

    :return:
    """
    if self.__focus is None or isinstance(self.__focus, dict):
      self.__focus = Data(self.__focus or {}, self.selector)
    return self.__focus

  @property
  def empty(self):
    """
    Selects every <p> element that has no children (including text nodes)

    Documentation
    https://www.w3schools.com/cssref/sel_empty.asp

    :return:
    """
    if self.__empty is None or isinstance(self.__empty, dict):
      self.__empty = Data(self.__empty or {}, self.selector)
    return self.__empty

  @property
  def enabled(self):
    """
    Selects every enabled <input> element

    Documentation
    https://www.w3schools.com/cssref/sel_enabled.asp

    :return:
    """
    if self.__enabled is None or isinstance(self.__enabled, dict):
      self.__enabled = Data(self.__enabled or {}, self.selector)
    return self.__enabled

  @property
  def invalid(self):
    """
    Selects all input elements with an invalid value

    Documentation
    https://www.w3schools.com/cssref/sel_invalid.asp

    :return:
    """
    if self.__invalid is None or isinstance(self.__invalid, dict):
      self.__invalid = Data(self.__invalid or {}, self.selector)
    return self.__invalid

  @property
  def valid(self):
    """
    Selects all input elements with a valid value

    Documentation
    https://www.w3schools.com/cssref/sel_valid.asp

    :return:
    """
    if self.__valid is None or isinstance(self.__valid, dict):
      self.__valid = Data(self.__valid or {}, self.selector)
    return self.__valid

  @property
  def visited(self):
    """
    Selects all visited links

    Documentation
    https://www.w3schools.com/cssref/sel_visited.asp

    :return:
    """
    if self.__visited is None or isinstance(self.__visited, dict):
      self.__visited = Data(self.__visited or {}, self.selector)
    return self.__visited

  @property
  def before(self):
    """
    Insert something before the content of each <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_before.asp

    :return:
    """
    if self.__before is None or isinstance(self.__before, dict):
      self.__before = Data(self.__before or {}, self.selector)
    return self.__before

  @property
  def after(self):
    """
    Insert something after the content of each <p> element

    Documentation
    https://www.w3schools.com/cssref/sel_after.asp

    :return:
    """
    if self.__after is None or isinstance(self.__after, dict):
      self.__after = Data(self.__after or {}, self.selector)
    return self.__after

  @property
  def webkit_slider_thumb(self):
    """
    :return:
    """
    if self.__webkit_slider_thumb is None or isinstance(self.__webkit_slider_thumb, dict):
      self.__webkit_slider_thumb = Data(self.__webkit_slider_thumb or {}, self.selector)
    return self.__webkit_slider_thumb

  @property
  def active(self):
    """
    Selects the active link

    Documentation
    https://www.w3schools.com/cssref/sel_active.asp

    :return:
    """
    if self.__active is None or isinstance(self.__active, dict):
      self.__active = Data(self.__active or {}, self.selector)
    return self.__active

  @property
  def has_changed(self):
    """

    :return:
    """
    for e in self.__internal_props:
      s = getattr(self, e)
      self.__has_changed |= s.has_changed
    return self.__has_changed

  def css(self, key, value=None, important=False, change=True):
    """

    :param key:
    :param value:
    :param important:
    :param change:
    :return:
    """
    return self.attrs.css(key, value, important, change)

  def media(self, attrs, rule=None, media_type=None, mediafeature=None):
    """
    The @media is used in media queries to apply different styles for different media types/devices.

    Example
    rptObj.style.media('only', 'screen', {body {
        background-color: lightblue;
        }
    })

    Documentation
    https://www.w3schools.com/cssref/css3_pr_mediaquery.asp
    :param rule: not or only or and see documentation for more inf
    :param media_type:
    :param mediafeature:
    :return:
    """

  def keyframes(self, name, attrs, effects=None, change=True):
    """
    The @keyframes rule specifies the animation code.

    The animation is created by gradually changing from one set of CSS styles to another.

    Example
    rptObj.style.keyframes("test", {
      "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
      "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
      "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
    })

    Documentation
    https://www.w3schools.com/cssref/css3_pr_animation-keyframes.asp

    :param effects: Effect Class.
    :param name: String. Required. Defines the name of the animation.
    :param attrs: String. Required. Percentage of the animation duration.
    """
    if change:
      self.__has_changed = True
    if effects is not None:
      name = effects.__class__.__name__
      attrs = effects.get_attrs()
    self.__keyframes[name] = attrs
    return name

  def get_ref(self):
    """

    :return:
    """
    if self.has_changed and self.cls_ref in [None, self.classname]:
      # dedicated unique ID if it is not the original style
      if self.html_id is not None:
        self.cls_ref = "%s_%s" % (self.classname, self.html_id)
      else:
        self.cls_ref = self.classname
    elif not self.has_changed:
      self.cls_ref = self.classname
    return self.cls_ref

  def __str__(self):
    style = []
    cls_reference = self.get_ref()
    for e in self.__internal_props:
      s = getattr(self, e)
      css_id = str(s.selector) % cls_reference
      if str(s):
        if e == "attrs":
          style.append("%s %s" % (css_id.strip(), s))
        else:
          style.append("%s:%s %s" % (css_id.strip(), e, s))
    map_cls_ref = {'-webkit-slider-thumb': 'webkit_slider_thumb'}
    for e in ['after', 'before', '-webkit-slider-thumb']:
      s = getattr(self, map_cls_ref.get(e, e))
      css_id = str(s.selector) % cls_reference
      if str(s):
        style.append("%s::%s %s" % (css_id.strip(), e, s))
    if self.__keyframes:
      for name, k_attrs in self.__keyframes.items():
        style.append("@keyframes %s {" % name)
        for k, v_dict in k_attrs.items():
          style.append("  %s {%s; }" % (k, "; ".join(["%s: %s" % (i, ", ".join(j)) if isinstance(j, list) else "%s: %s" % (i, j) for i, j in v_dict.items()])))
        style.append("}")
    return "\n".join(style)

  def _repr_html_(self):
    """ Display for Jupyter """
    value = str(self)
    return value.replace(" ;", " ;\n  ").replace(" {", " {\n  ").replace("  }", "}")
