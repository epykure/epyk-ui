from typing import Union
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js.Imports import string_to_base64
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils


class JsHtmlPanel(JsHtml.JsHtml):

    def __init__(self, js_code: str = None, set_var: bool = False, is_py_data: bool = False,
                 page: primitives.PageModel = None, component=None):
        super(JsHtmlPanel, self).__init__(component, js_code, set_var, is_py_data, page)
        if js_code is not None:
            self.varName = js_code

    def select(self):
        return self.firstChild.events.trigger("click")


class JsHtmlSlidingPanel(JsHtml.JsHtml):

    def close(self):
        """ Close the sliding panel. """
        return JsFncs.JsFunctions([
            self.page.js.if_(self.component.icon.dom.content.toString().indexOf(
                self.component.options.icon_expanded.split(" ")[-1]) >= 0, [
                                 self.page.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle(),
                                 self.component.icon.dom.switchClass(self.component.options.icon_expanded,
                                                                     self.component.options.icon_closed)
                             ])
        ])

    def open(self):
        """ Open the sliding panel. """
        return JsFncs.JsFunctions([
            self.page.js.if_(self.component.icon.dom.content.toString().indexOf(
                self.component.options.icon_closed.split(" ")[-1]) >= 0, [
                                 self.page.js.getElementsByName("panel_%s" % self.htmlCode).first.toggle(),
                                 self.component.icon.dom.switchClass(self.component.options.icon_closed,
                                                                     self.component.options.icon_expanded)
                             ])
        ])

    def set_title(self, data, options: dict = None):
        """
        Set the component title.

        :param data: A String corresponding to a JavaScript object
        :param dict options: Optional. Specific Python options available for this component
        """
        return self.component.title[1].build(data, options=options)

    def set_icon(self, data: str, css: dict = None, options: dict = None):
        """
        Set the icon from Font-awesome options.

        :param data: A String corresponding to a JavaScript object
        :param css: Optional. The CSS attributes to be added to the HTML component
        :param options: Optional. Specific Python options available for this component
        """
        if css is not None:
            return self.component.title[0].build(data, options={"css": css})

        return self.component.title[0].build(data, options=options)


class JsHtmlTr(JsHtml.JsHtml):
    display_value = "table-row"


class JsHtmlRow(JsHtml.JsHtml):
    display_value = "flex"


class JsHtmlGrid(JsHtml.JsHtml):

    @property
    def val(self):
        """ Return the underlying input values. """
        return self.component.input.dom.val

    @property
    def content(self):
        """ Return the underlying input content. """
        return self.component.input.dom.content

    def panel(self, i: int):
        """
        Return the underlying panel object.

        :param i: The panel index
        """
        panel = JsHtmlPanel(self.component, page=self.page)
        panel.varName = "%s.querySelector('.row').querySelector('div:nth-child(%s)')" % (self.varId, i + 1)
        return panel

    @property
    def panels(self):
        """ Iterator on the various available panels. """
        for i, _ in enumerate(self.component.colsDim):
            yield self.panel(i)

        return ""

    def togglePanel(self, i: int):
        """
        Toggle the display of the column in a grid component.
        Thw other columns will be resized accordingly.

        :param i: The column number (start at 0)
        """
        return '''
if(%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display == 'none'){
  %(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'block'
} else {%(compId)s.querySelector('.row').querySelector('div:nth-child(%(i)s)').style.display = 'none'}
''' % {'compId': self.varId, 'i': i + 1}


class JsHtmlTabs(JsHtml.JsHtml):

    def __getitem__(self, i: int):
        return JsHtmlPanel(
            self, component=self.component,
            js_code="%s.firstChild.querySelector('div:nth-child('+ (parseInt(%s)+1) + ')')" % (
                self.varId, i), page=self.page)

    def add_tab(self, name: str):
        """
        Add a tab to the panel.

        :param name: The name of the new tab
        """
        return JsFncs.JsFunctions([
            JsObjects.JsNodeDom.JsDoms.new("div", js_code="new_table"),
            JsObjects.JsNodeDom.JsDoms.new("div", js_code="new_table_content"),
            JsObjects.JsNodeDom.JsDoms.get("new_table").css({
                "width": "100px", "display": 'inline-block', "vertical-align": "middle", "box-sizing": 'border-box',
                'text-align': 'left'}),
            JsObjects.JsNodeDom.JsDoms.get("new_table_content").innerText(name),
            JsObjects.JsNodeDom.JsDoms.get("new_table_content").setAttribute("name", self.component.tabs_name),
            JsObjects.JsNodeDom.JsDoms.get("new_table_content").css({"width": "100px"}),
            JsObjects.JsNodeDom.JsDoms.get("new_table_content").css(self.component.options.css_tab),
            JsObjects.JsNodeDom.JsDoms.get("new_table_content").css({"padding": '5px 0'}),
            JsObjects.JsNodeDom.JsDoms.get("new_table").appendChild(JsObjects.JsObjects.get("new_table_content")),
            JsObjects.JsNodeDom.JsDoms.new("div", js_code="tab_container"),
            self.querySelector("div").appendChild(JsObjects.JsObjects.get("new_table")),
        ])

    def tab(self, i: int):
        """
        Return the Javascript tab object.

        Usage::

          tab.dom.tab(3).firstChild.css({"color": 'red'})

        :param i: Starting from 0 as we keep the Python indexing as reference
        """
        return JsObjects.JsNodeDom.JsDoms.get("%s.firstChild.querySelector('div:nth-child(%s)')" % (self.varId, i + 1))

    def set_tab_name(self, i: int, name: Union[str, primitives.JsDataModel]):
        """
        Change the name for a specific panel.

        :param i: The panel index
        :param name: The panel name
        """
        name = JsUtils.jsConvertData(name, None)
        return JsObjects.JsNodeDom.JsDoms.get(
            "%s.firstChild.querySelector('div:nth-child(%s)').querySelectorAll('[name=%s]')[0].innerHTML = %s" % (
                self.varId, i + 1, self.component.tabs_name, name))

    @property
    def selected_index(self):
        """
        Return the index of the selected tab.

        :return: The index or -1
        """
        return JsObjects.JsObjects.get('''
(function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
  if(selectedTab == null){ return -1 }
  else{ return selectedTab.getAttribute('data-index')}
})(%s)''' % self.varId)

    @property
    def selected_name(self):
        """
        Return the name of the selected tab.

        :return: The HTML content or an emtpy string.
        """
        return JsObjects.JsObjects.get('''
(function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
  if(selectedTab == null){ return "" }
  else{ return selectedTab.innerHTML }
})(%s)''' % self.varId)

    @property
    def content(self):
        """   Standard property to get the component value.  """
        return JsHtml.ContentFormatters(self.page, '''
(function(node){ var selectedTab = node.querySelector('div[data-selected=true'); 
  if(selectedTab == null){ return ""; }
  else{ var attrVal = null;
    if(typeof selectedTab.firstChild.getAttribute !== 'undefined'){ 
        attrVal = selectedTab.firstChild.getAttribute("data-value")} 
    if(attrVal != null){ return attrVal}
    else{return selectedTab.innerText}}
})(%s)''' % self.varId)

    def deselect_tabs(self, name: str = None):
        """ Deselect all the tabs in the component. """
        return JsFncs.JsFunctions([
            self.page.js.getElementsByName(self.component.tabs_name).all([
                self.page.js.data.all.element.setAttribute("data-selected", False),
                self.page.js.getElementsByName(self.component.tabs_name).all([
                    self.page.js.data.all.element.css(self.component.options.tab_not_clicked_style(name))])
            ])
        ])


class JsHtmlIFrame(JsHtml.JsHtml):

    def src(self, src: Union[str, primitives.JsDataModel]):
        """The src attribute specifies the address of the document to embed in an iframe.

        :param src: Specifies the URL of the document to embed in the iframe.
        """
        return self.setAttribute("src", src)

    def srcdoc(self, content: Union[str, primitives.JsDataModel]):
        """The srcdoc attribute specifies the HTML content of the page to show in the inline frame.
        Tip: This attribute is expected to be used together with the sandbox and seamless attributes.

        :param content: HTML content
        """
        return self.setAttribute("srcdoc", content)

    def add_style(self, content: Union[str, primitives.JsDataModel]):
        """Add CSS Style from String content in the JavaScript section

        :param content: CSS Fragment as a String
        """
        content = JsUtils.jsConvertData(content, None)
        return JsUtils.jsWrap('document.head.appendChild(document.createElement("style")).innerHTML= %s' % content)

    def get_doc(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None
                ) -> JsObjects.JsObject.JsObject:
        """Return the HTML doc to feed the iFrame.

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        content = []
        if self.component.options.exts:
            self.component.to_header('<script title="customResource" language="javascript" type="text/javascript" src="data:text/js;base64,%s"></script>' % (
                string_to_base64(";".join(self.component.options.exts))), force=True)
        if self.component.headers:
            content.append("<head>%s</head>" % "".join(self.component.headers))
        if self.component.body:
            _html_comps = []
            for comp in self.component.body:
                _html_comps.append(str(comp))
            content.append("<body>%s</body>" % "".join(_html_comps))
        if js_funcs:
            self.component.scripts.append(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        if self.component.scripts:
            content.append("<script>%s</script>" % ";".join(self.component.scripts))
        if content:
            return JsObjects.JsObject.JsObject.get("".join(content))

        return JsObjects.JsObject.JsObject.get("")
