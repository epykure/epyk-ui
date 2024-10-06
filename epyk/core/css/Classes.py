#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import os
from pathlib import Path

from epyk.core.js import Imports

from epyk.core.css.catalogs import CatalogButton
from epyk.core.css.catalogs import CatalogInput
from epyk.core.css.catalogs import CatalogChart
from epyk.core.css.catalogs import CatalogDiv
from epyk.core.css.catalogs import CatalogTree
from epyk.core.css.catalogs import CatalogIcons
from epyk.core.css.catalogs import CatalogLayout
from epyk.core.css.catalogs import CatalogLink
from epyk.core.css.catalogs import CatalogRadio
from epyk.core.css.catalogs import CatalogSelect
from epyk.core.css.catalogs import CatalogTable
from epyk.core.css.catalogs import CatalogText
from epyk.core.css.catalogs import CatalogMedia
from epyk.core.css.catalogs import CatalogImg
from epyk.core.css.catalogs import CatalogStd

# Change predefined CSS classes.
# This will allow to fully change the framework in order to align with other CSS classes and attributes.
OVERRIDES = None


def get_class_override(css_cls):
    """Hook to override predefined CSS classes for all the reports in the project.

    :param css_cls: Style. The CSS Class in the framework
    """
    if OVERRIDES is None:
        return css_cls

    if css_cls.classname in OVERRIDES:
        css_ovr_def = OVERRIDES[css_cls.classname]
        if not css_ovr_def:
            return False

        if isinstance(css_ovr_def, dict):
            if "css" in css_ovr_def:
                css_cls.css(css_ovr_def["css"])
            if "hover" in css_ovr_def:
                css_cls.hover.css(css_ovr_def["hover"])
            if "name" in css_ovr_def:
                css_cls.classname = css_ovr_def["name"]
                css_cls.cls_ref = css_ovr_def["name"]
            css_cls.is_page_scope = css_ovr_def.get("defined", True)
        else:
            css_cls.classname = css_ovr_def
    return css_cls


class Catalog:

    def __init__(self, page, classList):
        self.page, self.__class_list = page, classList
        self.__ctx = {}

    def font_face(self, font_family: str, src: str, stretch: str = "normal", style: str = "normal",
                  weight: str = "normal"):
        """With the @font-face rule, web designers do not have to use one of the "web-safe" fonts anymore.

        In the @font-face rule you must first define a name for the font (e.g. myFirstFont), and then point to
        the font file.

        Entry to get a font family from a local file to avoid loading it online.
        This is safer but also improve the speed of the website.

        `w3schools <https://www.w3schools.com/cssref/css3_pr_font-face_rule.asp>`_

        :param font_family: Defines the name of the font
        :param src: Defines the URL(s) where the font should be downloaded from
        :param stretch: Optional. Defines how the font should be stretched. Default value is "normal"
        :param style: Optional. Defines how the font should be styled. Default value is "normal"
        :param weight: Optional. Defines the boldness of the font. Default value is "normal"
        """
        self.page.properties.css.font_face(font_family, src, stretch, style, weight)
        return self

    def _class_type(self, cls_type: str):
        """Change the current class type to the one defined and return the internal class object.

        :param cls_type: The alias of the class other or main
        """
        self.__class_list_type = self.__class_list[cls_type]
        return self

    @property
    def other(self):
        """Get the list of CSS Classes impacting to the component but not added to the class tag of the HTML component.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.other)
        """
        self.__class_list_type = self.__class_list['other']
        return self.__class_list_type

    @property
    def main(self):
        """Get the list of CSS Classes added to the component and to the class tag of the component.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.main)
        """
        self.__class_list_type = self.__class_list['main']
        return self.__class_list_type

    @property
    def std(self) -> CatalogStd.CatalogStd:
        """Shortcut to standard CSS classes (for layout purposes like margin, padding...).

        Usage::

          t1 = page.ui.title("Templates structure")
          t1.style.add_classes.std.margin(7)

        `getbootstrap <https://getbootstrap.com/docs/4.0/utilities/spacing/>`_
        """
        if "std" not in self.__ctx:
            self.__ctx['std'] = CatalogStd.CatalogStd(self.page, self.__class_list)
        return self.__ctx['std']

    @property
    def button(self) -> CatalogButton.CatalogButton:
        """CSS Classes specific to the buttons components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.button)
        """
        if "button" not in self.__ctx:
            self.__ctx['button'] = CatalogButton.CatalogButton(self.page, self.__class_list_type)
        return self.__ctx['button']

    @property
    def select(self) -> CatalogSelect.CatalogSelect:
        """CSS Classes specific to the select compatibility components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.select)
        """
        if "select" not in self.__ctx:
            self.__ctx['select'] = CatalogSelect.CatalogSelect(self.page, self.__class_list_type)
        return self.__ctx['select']

    @property
    def screens(self) -> CatalogMedia.CatalogMedia:
        """CSS Classes specific to the screen compatibility components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.screens)
        """
        if "screens" not in self.__ctx:
            self.__ctx['screens'] = CatalogMedia.CatalogMedia(self.page, self.__class_list_type)
        return self.__ctx['screens']

    @property
    def icon(self) -> CatalogIcons.CatalogIcon:
        """CSS Classes specific to the Icon components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.icon)
        """
        if "icon" not in self.__ctx:
            self.__ctx['icon'] = CatalogIcons.CatalogIcon(self.page, self.__class_list_type)
        return self.__ctx['icon']

    @property
    def layout(self) -> CatalogLayout.CatalogLayout:
        """CSS Classes specific to Layout / Container components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.layout)
        """
        if "layout" not in self.__ctx:
            self.__ctx['layout'] = CatalogLayout.CatalogLayout(self.page, self.__class_list_type)
        return self.__ctx['layout']

    @property
    def dropdown(self) -> CatalogTree.CssStyleDropdown:
        """CSS Classes specific to the DropDown components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.dropdown)
        """
        if "dropdown" not in self.__ctx:
            self.__ctx['dropdown'] = CatalogTree.CatalogDropDown(self.page, self.__class_list_type)
        return self.__ctx['dropdown']

    @property
    def table(self) -> CatalogTable.CatalogTable:
        """CSS Classes specific to the Table components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.table)
        """
        if "table" not in self.__ctx:
            self.__ctx['table'] = CatalogTable.CatalogTable(self.page, self.__class_list_type)
        return self.__ctx['table']

    @property
    def chart(self) -> CatalogButton.CatalogButton:
        """CSS Classes specific to Chart components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.chart)
        """
        if "chart" not in self.__ctx:
            self.__ctx['chart'] = CatalogChart.CatalogChart(self.page, self.__class_list_type)
        return self.__ctx['chart']

    @property
    def link(self) -> CatalogLink.CatalogLink:
        """CSS Classes specific to Link components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.link)
        """
        if "link" not in self.__ctx:
            self.__ctx['link'] = CatalogLink.CatalogLink(self.page, self.__class_list_type)
        return self.__ctx['link']

    @property
    def date(self) -> CatalogInput.CatalogDate:
        """CSS Classes specific to Date components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.date)
        """
        if "date" not in self.__ctx:
            self.__ctx['date'] = CatalogInput.CatalogDate(self.page, self.__class_list_type)
        return self.__ctx['date']

    @property
    def text(self) -> CatalogText.CatalogText:
        """CSS Classes specific to Text components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.text)
        """
        if "text" not in self.__ctx:
            self.__ctx['text'] = CatalogText.CatalogText(self.page, self.__class_list_type)
        return self.__ctx['text']

    @property
    def input(self) -> CatalogInput.CatalogInput:
        """CSS Classes specific to Input components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.input)
        """
        if "inputs" not in self.__ctx:
            self.__ctx['inputs'] = CatalogInput.CatalogInput(self.page, self.__class_list_type)
        return self.__ctx['inputs']

    @property
    def image(self) -> CatalogImg.CatalogImg:
        """CSS Classes specific to Image components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.image)
        """
        if "image" not in self.__ctx:
            self.__ctx['image'] = CatalogImg.CatalogImg(self.page, self.__class_list_type)
        return self.__ctx['image']

    @property
    def div(self) -> CatalogDiv.CatalogDiv:
        """CSS Classes specific to Div / Container components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.div)
        """
        if "div" not in self.__ctx:
            self.__ctx['div'] = CatalogDiv.CatalogDiv(self.page, self.__class_list_type)
        return self.__ctx['div']

    @property
    def shapes(self) -> CatalogDiv.CatalogShapes:
        """CSS Classes specific to Div / Container components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.shapes)
        """
        if "shapes" not in self.__ctx:
            self.__ctx['shapes'] = CatalogDiv.CatalogShapes(self.page, self.__class_list_type)
        return self.__ctx['shapes']

    @property
    def radio(self) -> CatalogRadio.CatalogRadio:
        """CSS Classes specific to Radio button components.

        Usage::

          t1 = page.ui.title("Templates structure")
          print(t1.style.add_classes.radio)
        """
        if "radio" not in self.__ctx:
            self.__ctx['radio'] = CatalogRadio.CatalogRadio(self.page, self.__class_list_type)
        return self.__ctx['radio']

    def custom(self, css_cls):
        """Register a bespoke external class to the report object.

        :param css_cls: Class. The python class to be used as a CSS Class in the framework

        :return: self for the chaining.
        """
        css_cls_obj = css_cls(self.page)
        css_cls_obj.customize()
        self.__class_list_type.add(css_cls_obj)
        return self

    def customFile(self, filename: str, path: str = None):
        """Add an external CSS file to the final HTML report.
        If the file is defined with a local absolute path the content will be encoded and included to the page.

        :param filename: The file name
        :param path: Optional. The full path of the external CSS file. If None the user part in Imports.STATIC_PATH
                     will be used

        :return: self for the chaining.
        """
        from epyk.conf.global_settings import ASSETS_STATIC_CSS, ASSETS_SPLIT, ASSETS_STATIC_ROUTE, ASSETS_STATIC_PATH, ASSETS_SPLIT_MINIFY
        if path is None:
            self.page.cssLocalImports.add("%s/%s/%s" % (Imports.STATIC_PATH.replace("\\", "/"), ASSETS_STATIC_CSS, filename))
        else:
            file_path = os.path.join(path, filename)
            if os.path.exists(file_path):
                if not ASSETS_SPLIT:
                    with open(file_path, "rb") as fp:
                        base64_bytes = base64.b64encode(fp.read())
                        base64_content = base64_bytes.decode("ascii")
                    self.page.cssLocalImports.add("data:text/css;base64,%s" % base64_content)
                else:
                    with open(file_path, "r") as fp:
                        content = fp.read()
                    css_target_folder = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_CSS
                    if not css_target_folder.exists():
                        css_target_folder.mkdir(parents=True, exist_ok=True)
                    if ASSETS_SPLIT_MINIFY and not ".min." in filename:
                        filename = filename[:-4] + ".min.css"
                    css_target_file = css_target_folder / filename
                    with open(str(css_target_file), "w") as fp:
                        if ASSETS_SPLIT_MINIFY:
                            # TODO Improve CSS minifying
                            fp.write("".join([line.strip() for line in content.split("\n")]))
                        else:
                            fp.write(content)
                    self.page.cssLocalImports.add("%s/%s/%s" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_CSS, filename))
            else:
                self.page.cssLocalImports.add("%s/%s" % (path, filename))
        return self

    def customText(self, text: str):
        """Add a bespoke CSS fragment.

        :param text: The CSS fragment to be added to the HTML report. This can be a class or a group of class

        :return: self for the chaining.
        """
        self.page.properties.css.add_text(text)
        return self

    def anonymous_cls(self, attrs: dict):
        """Create a bespoke class based on the various attributes.
        This will internal build the class and return it.

        Usage::

          t1 = page.ui.title("Templates structure")
          v_cls = t1.style.add_classes.anonymous_cls({
            '_attrs': {'color': 'green', 'cursor': 'pointer'},
            '_hover': {'color': 'red'}})

        :param attrs: The expected class attributes

        :return: The Python class
        """
        import hashlib

        from epyk.core.css.styles.classes import CssStyle

        has_style = str(hashlib.sha1(str(attrs).encode()).hexdigest())
        attrs['classname'] = "style_%s" % has_style
        meta_cls = type('Style%s' % has_style, (CssStyle.Style,), attrs)
        return meta_cls

    def external(self, classname: str):
        """Add external CSS classes to a component.

        Usage::

          t1 = page.ui.title("Templates structure")
          t1.style.add_classes.external("cssClassReference")

        :param classname: The external class name to be added

        :return: self for the chaining.
        """
        if isinstance(classname, list):
            classname = " ".join(classname)
        self.__class_list_type.add(classname)
        return self
