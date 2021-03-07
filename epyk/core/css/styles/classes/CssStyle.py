#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Properties


class Data(Properties.CssMixin):

  def __init__(self, css_ovrs, selector):
    self._content = css_ovrs or {}
    self.__selector = selector
    self.has_changed = False

  def css(self, k, v=None, important=False, change=True):
    """
    Description:
    ------------
    Set multiple CSS attributes to the HTML component.

    Attributes:
    ----------
    :param k: Dictionary | String. optional. The attributes to be added.
    :param v: String. Optional. The value for a given item.
    :param important: Boolean. Optional. Specify if the style is important.
    :param change: Boolean. Optional. State of the CSS group from the creation.
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
    Description:
    ------------
    Clear all the CSS attributes defined for this class.

    :return: Self to allow the chaining.
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


class Selector:

  def __init__(self, selector_ovrs):
    map_fncs = {"parent": "parent_element", "child": "sub_element"}
    self.__this, self._suffix = selector_ovrs["classname"], ''
    del selector_ovrs["classname"]
    for k, v in selector_ovrs.items():
      getattr(self, map_fncs.get(k, k))(v)
    self.__element = False

  def elements(self, element_types):
    """
    Description:
    ------------
    Selects all <div> elements and all <p> elements.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_comma.asp

    Attributes:
    ----------
    :param element_types: List. All the element tags.
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
    Description:
    ------------
    Selects all <p> elements inside <div> elements.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_element.asp

    Attributes:
    ----------
    :param element: String. The element tag.
    :param direct_parent: Boolean. Optional. the link with the main component.
    :param class_name: String. Optional. The CSS class name.
    """
    if direct_parent:
      self.__this = "%s > %s" % (self.__this, element)
    else:
      self.__this = "%s %s" % (self.__this, element)
    return self

  def parent_element(self, element, direct_parent=False, class_name=None):
    """
    Description:
    ------------
    Selects all <p> elements inside <div> elements.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_element.asp

    Attributes:
    ----------
    :param element: String. The element tag.
    :param direct_parent: Boolean. Optional. the link with the main component.
    :param class_name: String. Optional. The CSS class name.
    """
    if direct_parent:
      self.__this = "%s > %s" % (element, self.__this)
    else:
      self.__this = "%s %s" % (element, self.__this)
    return self

  def with_next_element(self, element, class_name=None):
    """
    Description:
    ------------
    Selects all <p> elements that are placed immediately after <div> elements

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_pluss.asp

    Attributes:
    ----------
    :param element: The element tag.
    :param class_name: String. Optional. The CSS class name.
    """
    self.__this = "%s + %s" % (self.__this, element)
    return self

  def with_prev_element(self, element, class_name=None):
    """
    Description:
    ------------
    Selects every <ul> element that are preceded by a <p> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_gen_sibling.asp

    Attributes:
    ----------
    :param element: String. The element tag.
    :param class_name: String. Optional. The CSS class name.
    """
    self.__this = "%s ~ %s" % (self.__this, element)
    return self

  def join_class(self, class_name):
    """
    Description:
    ------------
    Selects all elements with both name1 and name2 set within its class attribute.

    Attributes:
    ----------
    :param class_name: String. Optional. The CSS class name.
    """
    self.__this = "%s.%s" % (self.__this, class_name)
    return self

  def add_class(self, class_name):
    """
    Description:
    ------------
    Selects all elements with name2 that is a descendant of an element with name.

    Attributes:
    ----------
    :param class_name: String. Optional. The CSS class name.
    """
    self.__this = "%s .%s" % (self.__this, class_name)
    return self

  def sub_class(self, class_name, direct_parent=False):
    """
    Description:
    ------------
    Selects all <p> elements inside <div> elements.

    Related Pages:

      https://www.w3schools.com/cssref/sel_element_element.asp

    Attributes:
    ----------
    :param class_name: String. Optional. The CSS class name.
    :param direct_parent: Boolean. Optional. the link with the main component.
    """
    if direct_parent:
      self.__this = "%s > .%s" % (self.__this, class_name)
    else:
      self.__this = "%s .%s" % (self.__this, class_name)
    return self

  def element(self, flag=None):
    """
    Description:
    ------------
    Add a flag to put the element tag when the CSS class will be built.

    Attributes:
    ----------
    :param flag: Boolean. Optional. Define if the element tag needs to be added.
    """
    if flag is None:
      return self.__element

    self.__element = flag
    return self

  def add_element_id(self, component):
    """
    Description:
    ------------
    Selects the element with id="firstname".

    Related Pages:

      https://www.w3schools.com/cssref/sel_id.asp

    Attributes:
    ----------
    :param component: HTML. The component.
    """
    self.__this = "%s%s" % (component.htmlCode, self.__this)
    return self

  def not_element(self, element):
    """
    Description:
    ------------
    Selects every element that is not a <p> element.

    Related Pages:

       https://www.w3schools.com/cssref/sel_not.asp

    Attributes:
    ----------
    :param element: String. The element reference (tag).
    """
    self.__this = "%s:not(%s)" % (self.__this, element)
    return self

  def first_child(self):
    """
    Description:
    ------------
    Selects every <p> element that is the first child of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_firstchild.asp
    """
    self.__this = "%s:first-child" % self.__this
    return self

  def first_letter(self):
    """
    Description:
    ------------
    Selects the first letter of every <p> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_firstletter.asp
    """
    self.__this = "%s::first-letter" % self.__this
    return self

  def first_line(self):
    """
    Description:
    ------------
    Selects the first line of every <p> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_firstline.asp
    """
    self.__this = "%s::first-line" % self.__this
    return self

  def first_of_type(self):
    """
    Description:
    ------------
    Selects every <p> element that is the first <p> element of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_first-of-type.asp
    """
    self.__this = "%s:first-of-type" % self.__this
    return self

  def in_range(self):
    """
    Description:
    ------------
    Selects input elements with a value within a specified range.

    Related Pages:

      https://www.w3schools.com/cssref/sel_in-range.asp
    """
    self.__this = "%s:in-range" % self.__this
    return self

  def last_child(self):
    """
    Description:
    ------------
    Selects every <p> element that is the last child of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_last-child.asp
    """
    self.__this = "%s:last-child" % self.__this
    return self

  def last_of_type(self):
    """
    Description:
    ------------
    Selects every <p> element that is the last <p> element of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_last-of-type.asp
    """
    self.__this = "%s:last-of-type" % self.__this
    return self

  def link(self):
    """
    Description:
    ------------
    Selects all unvisited links.

    Related Pages:

      https://www.w3schools.com/cssref/sel_link.asp
    """
    self.__this = "%s:link" % self.__this
    return self

  def nth_child(self, n):
    """
    Description:
    ------------
    Selects every <p> element that is the second child of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_nth-child.asp

    Attributes:
    ----------
    :param n:
    """
    self.__this = "%s:nth-child(%s)" % (self.__this, n)
    return self

  def nth_last_child(self, n):
    """
    Description:
    ------------
    Selects every <p> element that is the second child of its parent, counting from the last child.

    Related Pages:

      https://www.w3schools.com/cssref/sel_nth-last-child.asp

    Attributes:
    ----------
    :param n: Integer. The index from the end for a list of elements.
    """
    self.__this = "%s:nth-last-child(%s)" % (self.__this, n)
    return self

  def nth_last_of_type(self, n):
    """
    Description:
    ------------
    Selects every <p> element that is the second <p> element of its parent, counting from the last child.

    Related Pages:

      https://www.w3schools.com/cssref/sel_nth-last-of-type.asp

    Attributes:
    ----------
    :param n: Integer. The index from the end for a list of element types.
    """
    self.__this = "%s:nth-last-of-type(%s)" % (self.__this, n)
    return self

  def nth_of_type(self, n):
    """
    Description:
    ------------
    Selects every <p> element that is the second <p> element of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_nth-of-type.asp

    Attributes:
    ----------
    :param n: Integer. The index from the start for a list of element types.
    """
    self.__this = "%s:nth-of-type(%s)" % (self.__this, n)
    return self

  def only_of_type(self):
    """
    Description:
    ------------
    Selects every <p> element that is the only <p> element of its parent.

    Related Pages:

      https://www.w3schools.com/cssref/sel_only-of-type.asp
    """
    self.__this = "%s:only-of-type" % self.__this
    return self

  def only_child(self):
    """
    Description:
    ------------
    Selects every <p> element that is the only child of its parent.

    Related Pages:

      ttps://www.w3schools.com/cssref/sel_only-child.asp
    """
    self.__this = "%s:only-child" % self.__this
    return self

  def placeholder(self):
    """
    Description:
    ------------
    Selects input elements with placeholder text.

    Related Pages:

      https://www.w3schools.com/cssref/sel_placeholder.asp
    """
    self.__this = "%s::placeholder" % self.__this
    return self

  def read_only(self):
    """
    Description:
    ------------
    Selects input elements with the "readonly" attribute specified.

    Related Pages:

      https://www.w3schools.com/cssref/sel_read-only.asp
    """
    self.__this = "%s:read-only" % self.__this
    return self

  def read_write(self):
    """
    Description:
    ------------
    Selects input elements with the "readonly" attribute NOT specified.

    Related Pages:

      https://www.w3schools.com/cssref/sel_read-write.asp
    """
    self.__this = "%s:read-write" % self.__this
    return self

  def suffix(self, data):
    """
    Description:
    ------------
    Add a bespoke prefix to a class name.

    Attributes:
    ----------
    :param data: String. The class name reference.
    """
    self._suffix = "%s " % data.strip()

  def __str__(self):
    return self.__this


class Style:
  classname, classnames, is_class = None, None, True

  def __init__(self, page, css_ovrs=None, selector_ovrs=None, html_id=None):
    self.html_id, self.cls_ref, self.__has_changed = html_id, None, False
    self.page = page
    css_ovrs = css_ovrs or {}
    self.__keyframes, self.__media = {}, {}
    selector_ids = dict(getattr(self, '_selectors', {}))
    if self.classname is None:
      self.classname = self.__class__.__name__.lower()
    if self.classnames is not None:
      self.classname = " .".join(self.classnames)
    if not self.is_class:
      selector_ids["classname"], self.classname = ("%s", self.classname)
    else:
      if self.classname == False:
        selector_ids["classname"], self.classname = ("%s", "")
      elif self.classname.startswith('['):
        selector_ids["classname"], self.classname = ("%s", self.classname)
      elif self.classname.startswith('::'):
        selector_ids["classname"], self.classname = ("%s", self.classname)
      else:
        selector_ids["classname"], self.classname = (".%s", self.classname)
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
    self.__internal_props = ["attrs", "hover", "focus", "checked", "valid", "disabled", "empty", "enabled",
                             "invalid", "active"]
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
    """
    Description:
    ------------

    """
    pass

  def transition(self, attribute, duration=2, delay=None, iteration=None, timing_fnc=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param attribute:
    :param duration:
    :param delay:
    :param iteration:
    :param timing_fnc:
    """
    timing_fncs = ("ease", "linear", "ease-in", "ease-out", "ease-in-out")
    css_transition = {"transition-property": attribute, "transition-duration": "%ss" % duration}
    if delay:
      css_transition["transition-delay"] = "%ss" % delay
    if iteration:
      css_transition["transition-iteration-count"] = iteration
    if timing_fnc is not None:
      if timing_fnc not in timing_fncs and not timing_fnc.startswith("cubic-bezier"):
        raise Exception("%s missing from the list" % timing_fnc)

      css_transition["transition-timing-function"] = timing_fnc
    # Add the -webkit- prefix for compatibility with some browsers
    safari_css = dict([("-webkit-%s" % k, v) for k, v in css_transition.items()])
    css_transition.update(safari_css)
    self.css(css_transition, change=False)
    return self

  def animation(self, name=None, attrs=None, duration=2, delay=None, iteration='infinite', timing_fnc=None,
                effect=None, fill_mode=None):
    """
    Description:
    ------------
    The @keyframes rule specifies the animation code.

    The animation is created by gradually changing from one set of CSS classes to another.

    Usage:
    -----

      page.ui.button("Ok").style.css_class.animation('test', {
        "from": {"border-color": "white"},
        "to": {"border-color": "red"},
      })

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-keyframes.asp
      https://www.w3schools.com/css/css3_animations.asp

    Attributes:
    ----------
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
    Description:
    ------------
    Selects links on mouse over.

    Related Pages:

      https://www.w3schools.com/cssref/sel_hover.asp
    """
    if self.__hover is None or isinstance(self.__hover, dict):
      self.__hover = Data(self.__hover or {}, self.selector)
    return self.__hover

  @property
  def checked(self):
    """
    Description:
    ------------
    Selects every checked <input> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_checked.asp
    """
    if self.__checked is None or isinstance(self.__checked, dict):
      self.__checked = Data(self.__checked or {}, self.selector)
    return self.__checked

  @property
  def disabled(self):
    """
    Description:
    ------------
    Selects every disabled <input> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_disabled.asp
    """
    if self.__disabled is None or isinstance(self.__disabled, dict):
      self.__disabled = Data(self.__disabled or {}, self.selector)
    return self.__disabled

  @property
  def focus(self):
    """
    Description:
    ------------
    Selects the input element which has focus.

    Related Pages:

      https://www.w3schools.com/cssref/sel_focus.asp
    """
    if self.__focus is None or isinstance(self.__focus, dict):
      self.__focus = Data(self.__focus or {}, self.selector)
    return self.__focus

  @property
  def empty(self):
    """
    Description:
    ------------
    Selects every <p> element that has no children (including text nodes).

    Related Pages:

      https://www.w3schools.com/cssref/sel_empty.asp
    """
    if self.__empty is None or isinstance(self.__empty, dict):
      self.__empty = Data(self.__empty or {}, self.selector)
    return self.__empty

  @property
  def enabled(self):
    """
    Description:
    ------------
    Selects every enabled <input> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_enabled.asp
    """
    if self.__enabled is None or isinstance(self.__enabled, dict):
      self.__enabled = Data(self.__enabled or {}, self.selector)
    return self.__enabled

  @property
  def invalid(self):
    """
    Description:
    ------------
    Selects all input elements with an invalid value.

    Related Pages:

      https://www.w3schools.com/cssref/sel_invalid.asp
    """
    if self.__invalid is None or isinstance(self.__invalid, dict):
      self.__invalid = Data(self.__invalid or {}, self.selector)
    return self.__invalid

  @property
  def valid(self):
    """
    Description:
    ------------
    Selects all input elements with a valid value.

    Related Pages:

      https://www.w3schools.com/cssref/sel_valid.asp
    """
    if self.__valid is None or isinstance(self.__valid, dict):
      self.__valid = Data(self.__valid or {}, self.selector)
    return self.__valid

  @property
  def visited(self):
    """
    Description:
    ------------
    Selects all visited links.

    Related Pages:

      https://www.w3schools.com/cssref/sel_visited.asp
    """
    if self.__visited is None or isinstance(self.__visited, dict):
      self.__visited = Data(self.__visited or {}, self.selector)
    return self.__visited

  @property
  def before(self):
    """
    Description:
    ------------
    Insert something before the content of each <p> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_before.asp
    """
    if self.__before is None or isinstance(self.__before, dict):
      self.__before = Data(self.__before or {}, self.selector)
    return self.__before

  @property
  def after(self):
    """
    Description:
    ------------
    Insert something after the content of each <p> element.

    Related Pages:

      https://www.w3schools.com/cssref/sel_after.asp
    """
    if self.__after is None or isinstance(self.__after, dict):
      self.__after = Data(self.__after or {}, self.selector)
    return self.__after

  @property
  def webkit_slider_thumb(self):
    """
    Description:
    ------------
    """
    if self.__webkit_slider_thumb is None or isinstance(self.__webkit_slider_thumb, dict):
      self.__webkit_slider_thumb = Data(self.__webkit_slider_thumb or {}, self.selector)
    return self.__webkit_slider_thumb

  @property
  def active(self):
    """
    Description:
    ------------
    Selects the active link.

    Related Pages:

      https://www.w3schools.com/cssref/sel_active.asp
    """
    if self.__active is None or isinstance(self.__active, dict):
      self.__active = Data(self.__active or {}, self.selector)
    return self.__active

  @property
  def has_changed(self):
    """
    Description:
    ------------
    Set an internal flag to specify if the class has changed from the creation in the framework.

    If the state of the class has changed, the class will not be generic anymore so it will change the CSS class
    reference by adding the Component id in order to make it specific.

    This is a trick in order to be able to change common CSS classes for a specific component without impacting
    the other ones in the page.
    """
    for e in self.__internal_props:
      s = getattr(self, e)
      self.__has_changed |= s.has_changed
    return self.__has_changed

  def css(self, key, value=None, important=False, change=True):
    """
    Description:
    ------------
    Add a CSS attribute to a class.

    Attributes:
    ----------
    :param key: String. The CSS attribute.
    :param value: String. Optional. The CSS value.
    :param important: Boolean. Optional. The level of priority for this attribute.
    :param change: Boolean. Optional. A flag to specify the state of the CSS class.
    """
    return self.attrs.css(key, value, important, change)

  def media(self, attrs, rule=None, media_type=None, media_feature=None, change=True, this_class=False):
    """
    Description:
    ------------
    The @media is used in media queries to apply different styles for different media types/devices.

    Usage:
    -----

      page.style.media({"body": {"background-color": "lightblue"}}, "only", "screen",
    {'and': [{'height': '100px'}, {'min-width': '600px'}]})

    The first key of the attributes can be an Epyk html object.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_mediaquery.asp

    Attributes:
    ----------
    :param attrs: String. Required. Percentage of the animation duration.
    :param rule: String. Optional. not or only or and see documentation for more info.
    :param media_type: String. Optional. the media to which the rule will need to be applied.
    :param media_feature: String. Optional. Media features provide more specific details to media queries.
    :param change: Boolean. Optional. A flag to specify the state of the CSS class.
    :param this_class: Boolean. Optional. Specify if this should be applied to this class only.
    """
    if this_class:
      attrs = {".%s" % self.classname: attrs}

    if change:
      self.__has_changed = True
    media_props = []
    if rule is not None:
      if rule in ['only', 'not'] and not media_type:
        raise Exception('You need to specify a mediatype when using rules not or only')

      media_props.extend([rule, media_type])
      if media_feature:
        for op, m_features in media_feature.items():
          for feature in m_features:
            features = ['(%s: %s)' % (k, v) for k, v in feature.items()]
          media_props.extend([op, ('%s ' % op).join(features)])
    name = ' '.join(media_props)
    self.__media[name] = attrs
    return name

  def keyframes(self, name, attrs, effects=None, change=True):
    """
    Description:
    ------------
    The @keyframes rule specifies the animation code.

    The animation is created by gradually changing from one set of CSS styles to another.

    Usage:
    -----

      page.style.keyframes("test", {
        "50%": {"transform": "scale(1.5, 1.5)", "opacity": 0},
        "99%": {"transform": "scale(0.001, 0.001)", "opacity": 0},
        "100%": {"transform": "scale(0.001, 0.001)", "opacity": 1},
      })

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_animation-keyframes.asp

    Attributes:
    ----------
    :param effects: String. Effect Class.
    :param name: String. Required. Defines the name of the animation.
    :param attrs: String. Required. Percentage of the animation duration.
    :param change: Boolean. Optional. A flag to specify the state of the CSS class.
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
    Description:
    ------------

    :return:
    """
    # dedicated unique ID if it is not the original style
    if self.has_changed and self.cls_ref in [None, self.classname]:
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
          style.append("%s %s%s" % (css_id.strip(), s.selector._suffix, s))
        else:
          style.append("%s:%s %s%s" % (css_id.strip(), e, s.selector._suffix, s))
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
    if self.__media:
      for name, m_attrs in self.__media.items():
        style.append("@media %s {" % name)
        for k, v_dict in m_attrs.items():
          if not type(k) == str:
            k = '.%s' % k.style.css_class.get_ref()
          style.append("  %s {%s; }" % (k, "; ".join(["%s: %s" % (i, ", ".join(j)) if isinstance(j, list) else "%s: %s" % (i, j) for i, j in v_dict.items()])))
        style.append("}")
    return "\n".join(style)

  def _repr_html_(self):
    """
    Description:
    ------------
    Display for Jupyter.
    """
    value = str(self)
    return value.replace(" ;", " ;\n  ").replace(" {", " {\n  ").replace("  }", "}")
