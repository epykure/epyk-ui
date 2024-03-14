#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List

from epyk.core import html
from epyk.core.py import primitives, types
from epyk.core.html import Defaults
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Lists:

  def __init__(self, ui):
    self.page = ui.page

  def select(self, records=None, html_code: str = None, selected: Union[str, List[str]] = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None, multiple: bool = False,
             options: dict = None) -> html.HtmlSelect.Select:
    """  
    HTML Select component.

    Usage::

      records = [
        {"text": 'Text 1', "value": "text 1"},
        {"text": 'Text 2', "value": "text 2"},
        {"text": 'Text 3', "value": "text 3"},
      ]

      select = page.ui.select(records)


    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlSelect.Select`

    Related Pages:

      https://silviomoreto.github.io/bootstrap-select/examples/
      https://www.npmjs.com/package/bootstrap-select-v4
      https://www.jqueryscript.net/form/Bootstrap-4-Dropdown-Select-Plugin-jQuery.html

    :param records: Optional. The list of dictionaries with the input data.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param selected: Optional. The selected value or values.
    :param width: Optional. Integer for the component width.
    :param height: Optional. Integer for the component height.
    :param profile: Optional. A flag to set the component performance storage.
    :param multiple: Optional. To set if the component can handle multiple selections.
    :param options: The select options as defined https://developer.snapappointments.com/bootstrap-select/options/
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    records = records or []
    if not isinstance(records, list):
      records = [{'text': v, 'value': v, "selected": True} for v in records.split(",")]
    options = options or {}
    options['selected'] = selected
    if multiple:
      if not isinstance(multiple, dict):
        multiple = {"max": 2}
      if selected is not None:
        for rec in records:
          if rec["value"] in selected:
            rec["selected"] = True
      icon_details = self.page.icons.get("check")
      options["iconBase"] = "iconBase"
      options["tickIcon"] = icon_details["icon"]
      html_select = html.HtmlSelect.Select(self.page, records, html_code, width, height, profile, multiple, options)
      html.Html.set_component_skin(html_select)
      return html_select

    if selected is not None:
      for rec in records:
        if rec["value"] == selected:
          rec["selected"] = True
    html_select = html.HtmlSelect.Select(self.page, records, html_code, width, height, profile, multiple, options)
    html.Html.set_component_skin(html_select)
    return html_select

  def lookup(self, lookup=None, html_code: str = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "%"), profile: types.PROFILE_TYPE = None, multiple: bool = False,
             options: dict = None) -> html.HtmlSelect.Lookup:
    """  
    HTML Select component.

    Usage::

      select1 = page.ui.select([
        {"value": "value 1", "text": "value 1"},
        {"value": "value 2", "text": "value 2"},
      ])
      lookupData = {"value 1": [
        {"value": "A", 'text': "Example 1"},
        {"value": "B", 'text': "Example 2"}
      ]}
      select2 = page.ui.lookup(lookupData)
      select1.change([
        select2.build(select1.dom.content)
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlSelect.Lookup`

    Related Pages:

      https://silviomoreto.github.io/bootstrap-select/examples/
      https://www.npmjs.com/package/bootstrap-select-v4
      https://www.jqueryscript.net/form/Bootstrap-4-Dropdown-Select-Plugin-jQuery.html

    :param lookup: Dictionary. Optional. The mapping to the list of recs to be loaded.
    :param html_code: Optional. The component identifier code (for bot
    :param width: Tuple. Optional. Integer for the component width
    :param height: Tuple. Optional. Integer for the component height
    :param profile: Optional. A flag to set the component performance storage
    :param multiple: Boolean. To set if the component can handle multiple selections
    :param options: The select options as defined https://developer.snapappointments.com/bootstrap-select/options/
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    options = {} if options is None else options
    html_select = html.HtmlSelect.Lookup(
      self.page, lookup, html_code, width, height, profile, multiple, options)
    html.Html.set_component_skin(html_select)
    return html_select

  def item(self, text: str = None, tag: str = None, options: dict = None) -> html.HtmlList.Li:
    """  
    Add a dynamic and configurable list component.

    Usage::

      l = page.ui.lists.list(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    :param text:
    :param tag:
    :param options:
    """
    options = options or {}
    if tag is not None:
      options["item_type"] = tag
    html_item = html.HtmlList.Li(self.page, text, options=options)
    html.Html.set_component_skin(html_item)
    return html_item

  def list(self, data=None, color: str = None, width: types.SIZE_TYPE = ('auto', ""),
           height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None, options: dict = None,
           profile: types.PROFILE_TYPE = None):
    """  
    Add a static list component.

    Usage::

      l = page.ui.lists.list(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      http://astronautweb.co/snippet/font-awesome/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list_dragdrop.py

    :param data: List. Optional. The list items.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"item_type": 'li'}
    if options is not None:
      dfl_options.update(options)
    html_list = html.HtmlList.List(
      self.page, data or [], color, width, height, html_code, helper, dfl_options, profile)
    html_list.css({"list-style": 'none'})
    html.Html.set_component_skin(html_list)
    return html_list

  def drop(self, data=None, color=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, 'px'),
           html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      cols_keys = page.ui.lists.drop(html_code="cols_agg_keys")
      cols_keys.style.css.min_height = 20
      cols_keys.items_style(style_type="bullets")
      cols_keys.drop()

    :param data:
    :param color:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    component = self.list(data, color, width, height, html_code, helper, options, profile)
    component.style.css.min_height = 40
    component.css({"display": "inline-block", "margin-top": '5px',
                   'border': "1px dashed %s" % self.page.theme.greys[4]})
    if component.style.css.width.endswith("%") and component.style.css.margin.endswith("px"):
      component.style.css.width = "calc({} - {}px)".format(
        component.style.css.width,  2 * int(component.style.css.margin[:-2]))
    component.style.css.padding = 5
    html.Html.set_component_skin(component)
    return component

  def items(self, records: list = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = ("auto", ""),
            options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None, helper: str = None
            ) -> html.HtmlList.Items:
    """  
    Add a JavaScript based list component.

    Usage::

      c = page.ui.lists.items([
        {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 8000},
        {"text": 'value 1', 'icon': 'fas fa-times', 'checked': True, 'value': 50000},
      ], options={"style": {"background": 'green', 'color': 'white'}})

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/list_custom.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/list_filter.py

    :param records: Optional. The list of dictionaries with the input data.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"items_type": 'text'}
    if options is not None:
      dft_options.update(options)
    dft_options["li_height"] = Defaults_css.Font.header_size
    html_item = html.HtmlList.Items(self.page, records or [], width, height, dft_options, html_code, profile, helper)
    html_item.css({"list-style-type": 'none'})
    if height[0] is not None and height[1] == "px":
      html_item.css({"overflow-y": 'auto'})
    html.Html.set_component_skin(html_item)
    return html_item

  def links(self, records=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = ("auto", ""),
            options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    component = self.items(records, width, height, options, html_code, profile, helper)
    component.options.items_type = "link"
    html.Html.set_component_skin(component)
    return component

  def icons(self, records=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = ("auto", ""),
            options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    component = self.items(records, width, height, options, html_code, profile, helper)
    component.options.items_type = "icon"
    html.Html.set_component_skin(component)
    return component

  def pills(self, records=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "%"),
            options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    """  

    Usage::

      page.ui.lists

    :param records:
    :param width:
    :param height:
    :param options:
    :param html_code:
    :param profile:
    :param helper:
    """
    html_item = self.items(records, width, height, options, html_code, profile, helper)
    html_item.options.li_style = {
      "display": "inline-block", "margin": "0 2px", "padding": "1px 4px", "border-radius": "10px",
      "background": self.page.theme.greys[2]}
    html.Html.set_component_skin(html_item)
    return html_item

  def box(self, records: list = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "%"),
          options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    """  
    Special list configuration for a list of box with a title with a text and a list of icons

    Usage::

      page.ui.lists

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list_box.py

    :param records:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dflt_options = {"items_type": 'box'}
    if options is not None:
      dflt_options.update(options)
    html_item = html.HtmlList.Items(self.page, records, width, height, dflt_options, html_code, profile, helper)
    html_item.css({"list-style-type": 'none'})
    html_item.style.css.padding_left = '15px'
    html.Html.set_component_skin(html_item)
    return html_item

  def numbers(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
              html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    """  

    Usage::

      page.ui.lists.numbers(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/html/html_lists.asp
      https://www.w3.org/wiki/CSS/Properties/list-style-type

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "decimal"
    html_list.style.css.margin_left = 20
    html.Html.set_component_skin(html_list)
    return html_list

  def alpha(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
            html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    """  

    Usage::

      page.ui.lists

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "lower-alpha"
    html_list.style.css.margin_left = 20
    html.Html.set_component_skin(html_list)
    return html_list

  def roman(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
            html_code: str = None, options: str = None, profile: types.PROFILE_TYPE = None, helper: str = None):
    """  

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Usage::

      page.ui.lists

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "lower-roman"
    html_list.style.css.margin_left = 20
    html.Html.set_component_skin(html_list)
    return html_list

  def points(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
             align: str = None, html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None,
             helper: str = None):
    """  

    Usage::

      page.ui.lists

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/html/html_lists.asp

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align:
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "circle"
    html_list.style.css.margin_left = 20
    if align == "center":
      html_list.style.css.margin = "auto"
      html_list.style.css.display = "block"
    html.Html.set_component_skin(html_list)
    return html_list

  def disc(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
           html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      page.ui.lists

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/cssref/pr_list-style-type.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "disc"
    html_list.style.css.margin_left = 20
    html.Html.set_component_skin(html_list)
    return html_list

  def squares(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
              html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      page.ui.lists.squares(["A", "B"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.List`

    Related Pages:

      https://www.w3schools.com/cssref/pr_list-style-type.asp

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_list = self.items(data, width, height, options, html_code, profile, helper)
    html_list.style.css.list_style_type = "square"
    html_list.style.css.margin_left = 20
    html.Html.set_component_skin(html_list)
    return html_list

  def groups(self, data=None, categories=None, color: str = None, width: types.SIZE_TYPE = ('auto', ""),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
             options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      l = page.ui.lists.groups(["AWW", "B"])
      l.add_list(["D", "E"], category="Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.Groups`

    Related Pages:

      http://designbump.com/create-a-vertical-accordion-menu-using-css3-tutorial/
      http://thecodeplayer.com/walkthrough/vertical-accordion-menu-using-jquery-css3

    :param data:
    :param categories:
    :param color:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    data = data or []
    categories = categories or [""]
    if len(data) > 0:
      if isinstance(data[0], list):
        categories = [""] * len(data)
      else:
        # This object is expecting a list of lists
        data = [data]
    html_obj = html.HtmlList.Groups(
      self.page, data, None, categories, color, width, height, html_code, helper, options, profile)
    html.Html.set_component_skin(html_obj)
    return html_obj

  def tree(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
           html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None
           ) -> html.HtmlTrees.Tree:
    """  

    Usage::

      data = [{"label": 'test', 'items': [{"label": 'child 1', 'color': 'red'}]}]
      page.ui.lists.tree(data)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.Tree`

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_tree = html.HtmlTrees.Tree(self.page, data or [], width, height, html_code, helper, options, profile)
    html.Html.set_component_skin(html_tree)
    return html_tree

  def dropdown(self, records=None, text: str = "", width: types.SIZE_TYPE = ('auto', ""),
               height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
               options: dict = None, profile: types.PROFILE_TYPE = None):
    """ Create a dropdown item.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTrees.DropDown`

    Related Pages:

      http://getbootstrap.com/docs/4.0/components/dropdowns/
      https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_ref_js_dropdown_multilevel_css&stacked=h
      https://codepen.io/svnt/pen/beEgre

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dropdown.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/tree.py

    :param records: Optional. The list of dictionaries with the input data.
    :param text: Optional. The value to be displayed to the component.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dftl_options = {"width": 90}
    dftl_options.update(options or {})
    html_d = html.HtmlTrees.DropDown(
      self.page, records, text, width, height, html_code, helper, dftl_options, profile)
    html_d.style.css.display = 'inline-block'
    html.Html.set_component_skin(html_d)
    return html_d

  def checks(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
             html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """ Add a list component with checkbox items.

    Usage::

      data = [{"label": "python", "value": False}, {"label": "Java", "value": 5}]
      checks = page.ui.lists.checklist(data)

      ts = page.ui.lists.items(["menu %s" % i for i in range(10)])
      its.options.checked_key = "selected"
      #its.options.max_selected = 2
      its.options.items_type = "check"
      its.options.checked_key = "selected"
      its.options.text_click = True

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.Checks`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"checked": False, "items_type": 'check'}
    if options is not None:
      dft_options.update(options)
    html_list = html.HtmlList.Items(self.page, data or [], width, height, dft_options, html_code, profile, helper)
    html_list.css({"list-style": 'none'})
    html.Html.set_component_skin(html_list)
    return html_list

  def badges(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
             html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      page.ui.lists.badges([{'label': 'Python', 'value': 12}, {'label': 'R', 'value': 3}])

      i = page.ui.lists.badges([
        {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 8},
        {"text": 'text', 'icon': 'fas fa-times', 'checked': True, 'value': 5},
      ], options={"badge": {"background": 'green'}})
      i.click([page.js.console.log(i.dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.Badges`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      https://v4-alpha.getbootstrap.com/components/list-group/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"badge": {"background": 'red', 'color': 'white', "items_type": 'badge'}}
    if options is not None:
      dft_options.update(options)
    html_list = html.HtmlList.Items(self.page, data or [], width, height, dft_options, html_code, profile, helper)
    html_list.css({"list-style": 'none'})
    html.Html.set_component_skin(html_list)
    return html_list

  def icons(self, data=None, width: types.SIZE_TYPE = ('auto', ""), height: types.SIZE_TYPE = (None, 'px'),
            html_code: str = None, helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      page.ui.lists.badges([{'label': 'Python', 'value': 12}, {'label': 'R', 'value': 3}])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlList.Badges`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_list_groups.asp
      https://v4-alpha.getbootstrap.com/components/list-group/

    :param data:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    icon_details = self.page.icons.get("check")
    dft_options = {"icon": icon_details["icon"], 'markdown': True, "items_type": 'icon'}
    if options is not None:
      dft_options.update(options)
    html_list = html.HtmlList.Items(self.page, data or [], width, height, dft_options, html_code, profile, helper)
    html_list.css({"list-style": 'none'})
    html.Html.set_component_skin(html_list)
    return html_list

  def radios(self, data=None, group_name: str = 'group', width: types.SIZE_TYPE = ('auto', ""),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             helper: str = None, options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

      page.ui.lists

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlInput.Radio`

    :param data:
    :param group_name:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dft_options = {"items_type": 'radio'}
    if options is not None:
      dft_options.update(options)
    html_list = html.HtmlList.Items(self.page, data or [], width, height, dft_options, html_code,  profile, helper)
    html_list.options.group = group_name
    html_list.css({"list-style": 'none'})
    html.Html.set_component_skin(html_list)
    return html_list

  def brackets(self, records=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (550, 'px'),
               options: dict = None, profile: types.PROFILE_TYPE = None):
    """  

    Usage::

        minimalData = {
          "teams": [
            ["Team 1", "Team 2"],
            ["Team 3", "Team 4"]
        ],
          "results": [
            [[1, 2], [3, 4]],
            [[4, 6], [2, 1]]]
        }

        bt = page.ui.lists.brackets(minimalData)

    :param records:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfp_options = {}
    if options is not None:
      dfp_options.update(options)
    component = html.HtmlList.ListTournaments(self.page, records, width, height, dfp_options, profile)
    html.Html.set_component_skin(component)
    return component

  def chips(self, items=None, category: str = 'group', placeholder: str = "", width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (60, "px"), html_code: str = None, helper: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None):
    """  
    Add a chip (filter) html component

    Usage::

      chips = page.ui.chips([])
      chips2 = page.ui.chips(["example", {"value": 'test', 'name': 'group 2'}], options={"visible": True})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Filters`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_contact_chips.asp

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/chips.py
        https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py

    :param items: Selected items
    :param category: Optional. The group of the items.
    :param placeholder: Optional. The input field placeholder
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"item_css": {"padding": '5px', 'border': '1px solid %s' % self.page.theme.success.light,
                                'border-radius': '5px', 'margin': '2px', "width": 'auto', 'display': 'inline-block',
                                'background': 'inherit', 'white-space': 'nowrap'},
                   'category': category, 'visible': True,
                   'value_css': {'font-size': self.page.body.style.globals.font.normal(),
                                 'font-weight': 'bold', 'vertical-align': 'bottom'},
                   'category_css': {'display': 'inline', 'margin-right': '2px', 'vertical-align': 'top',
                                    'font-size': self.page.body.style.globals.font.normal(-3)},
                   'icon_css': {'color': self.page.theme.success.base, 'margin-left': '5px',
                                'cursor': 'pointer'}}
    if not hasattr(category, 'toStr') and category == 'group':
      dfl_options['visible'] = False
    if options is not None:
      dfl_options.update(options)
    html_f = html.HtmlEvent.Filters(
      self.page, items or [], width, height, html_code, helper, dfl_options, profile)
    html_f.input.attr['placeholder'] = placeholder
    html.Html.set_component_skin(html_f)
    return html_f

  def menu(self, component, title: Union[str, dict] = None, add: bool = False, height=(18, 'px'), save_funcs=None,
           update_funcs=None, editable: bool = False, options: dict = None, profile: types.PROFILE_TYPE = None,
           checks: tuple = ("fas fa-check-square", "far fa-square")):

    commands = [("Add&nbsp;", "fas fa-plus")] if add else []
    if getattr(component.options, 'items_type', "") in ('check',):
      commands.append(("Check", checks))
    options = options or {}
    menu_items = []
    for typ, icon in commands:
      if icon:
        if isinstance(icon, tuple):
          icon = icon[0]
        r = self.page.ui.icons.awesome(
          icon, text=typ, align="center", height=height, width=(35, 'px'), options=options, profile=profile)
        r.span.style.css.line_height = r.style.css.height
        r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        r.span.style.css.margin = "0 0 -3px -3px"
        r.icon.style.add_classes.div.color_hover()
        if typ == "Add&nbsp;":
          r.click([
            component.dom.add(""),
            r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
            self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
          ])
        if typ == "Check":
          r.click([
            r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
            self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
            self.page.js.if_(r.span.dom.innerText() == "Check", [
              r.span.build("None"), component.dom.selectAll(),
              r.icon.build(checks[1])]).else_([
              r.span.build("Check"), component.dom.unSelectAll(),
              r.icon.build(checks[0]),
            ]),
          ], profile=profile)
        menu_items.append(r)
    if save_funcs is not None:
      r = self.page.ui.icons.awesome(
        "save", align="center", text="Save", height=height, width=(35, 'px'), options=options, profile=profile)
      r.span.style.css.line_height = r.style.css.height
      r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
      r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
      r.span.style.css.margin = "0 2px -3px -3px"
      r.icon.style.add_classes.div.color_hover()
      r.click([
        r.dom.css({"background": self.page.theme.success.light, "border-radius": "10px"}).r,
        self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
      ] + save_funcs, profile=profile)
      menu_items.append(r)
    if not editable:
      container = self.page.ui.menu(component, update_funcs=update_funcs, title=title, menu_items=menu_items, editable=editable, options=options)
    elif editable is True:
      container = self.page.ui.menu(component, update_funcs=update_funcs, title=title, menu_items=menu_items, options=options)
    else:
      container = self.page.ui.menu(component, update_funcs=update_funcs, title=title, menu_items=menu_items, editable=editable, options=options)
    html.Html.set_component_skin(container)
    return container

  def filters(self, items=None, button=None, width=("auto", ""), height=(60, "px"), html_code: str = None,
              helper: str = None, options: dict = None, autocomplete: bool = False, profile: Union[bool, dict] = None):

    options = options or {}
    container = self.page.ui.div(width=width)
    container.select = self.page.ui.select(
      html_code="%s_select" % html_code if html_code is not None else html_code)
    container.select.attr['data-width'] = '%spx' % options.get('width', Defaults.TEXTS_SPAN_WIDTH)
    container.select.options.liveSearch = True
    if autocomplete:
      container.input = self.page.ui.inputs.autocomplete(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    else:
      container.input = self.page.ui.input(
        html_code="%s_input" % html_code if html_code is not None else html_code,
        width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
    container.input.style.css.text_align = 'left'
    container.input.style.css.padding_left = 5
    container.input.style.css.margin_left = 10
    if button is None:
      button = self.page.ui.buttons.colored("add")
      button.style.css.margin_left = 10
    container.button = button
    container.clear = self.page.ui.icon("times")
    container.clear.style.css.color = self.page.theme.danger.base
    container.clear.style.css.margin_left = 20
    container.clear.tooltip("Clear all filters")
    container.add(self.page.ui.div([container.select, container.input, container.button, container.clear]))
    container.filters = self.page.ui.panels.filters(
      items, container.select.dom.content, (100, '%'), height, html_code, helper, options, profile)
    container.add(container.filters)
    container.clear.click([
      container.filters.dom.clear()
    ])
    container.button.click([
      container.filters.dom.add(container.input.dom.content, container.select.dom.content),
      container.input.js.empty()
    ])
    container.input.enter(container.button.dom.events.trigger("click"))
    html.Html.set_component_skin(container)
    return container
