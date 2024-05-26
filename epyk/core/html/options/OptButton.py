#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from typing import List, Optional, Dict, Union
from epyk.core.html.options import Options, OptionsWithTemplates
from epyk.core.html import Defaults as html_defaults


class OptionsButton(Options):
    component_properties = ("category",)

    @property
    def category(self):
        """ Button category to specify the style. """
        return self.get("validate")

    @category.setter
    def category(self, value: str):
        self.set(value)

    @property
    def multiple(self):
        """
        Property to define if multiple buttons can be selected at the same time.
        Default value is false.

        Usage::

          but = page.ui.button("Click Me")
          but.options.multiple = False

        :prop bool: Boolean. To be used if multiple buttons are grouped.
        """
        return self.get(False)

    @multiple.setter
    def multiple(self, flag: bool):
        self.set(flag)

    @property
    def group(self):
        """
        Property to set the group name of a button.

        Usage::

          but = page.ui.button("Click Me")
          but.options.group = "buttons"

        :prop val: String. The group name for several buttons.
        """
        return self.component.attr.get('name')

    @group.setter
    def group(self, val: str):
        self.component.set_attrs(name='name', value=val)

    @property
    def templateLoading(self):
        return self._config_get(None)

    @templateLoading.setter
    def templateLoading(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateError(self):
        return self._config_get(None)

    @templateError.setter
    def templateError(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)


class OptionsBadge(Options):
    component_properties = ("show_empty", "zeros_as_empty")

    @property
    def badge_css(self):
        """ """
        return self.get()

    @badge_css.setter
    def badge_css(self, css: dict):
        if hasattr(self, 'page') and hasattr(self.page, 'link'):
            self.page.link.css(css)
        css_opts = self.get({})
        css_opts.update(css)
        self.set(css_opts)

    @property
    def badge_position(self):
        """ """
        return self.get()

    @badge_position.setter
    def badge_position(self, position: str):
        if position == 'left':
            self.set({"position": 'relative'}, name='badge_css')
        else:
            self.set({"position": 'relative', "top": "-4px", "right": "11px"}, name='badge_css')
        self.set(position)

    @property
    def show_empty(self):
        """If True display the empty badge"""
        return self._config_get(True)

    @show_empty.setter
    def show_empty(self, flag: bool):
        self._config(flag)

    @property
    def zeros_as_empty(self):
        """if True consider zero values as empty (so follow the same display rules)"""
        return self._config_get(False)

    @zeros_as_empty.setter
    def zeros_as_empty(self, flag: bool):
        self._config(flag)


class OptMedia(Options):

    @property
    def controls(self):
        """
        Specifies that video controls should be displayed (such as a play/pause button etc).

        Related Pages:

          https://www.w3schools.com/tags/tag_video.asp
          https://www.w3schools.com/tags/att_video_controls.asp

        :prop bool: Optional. Default value is false.
        """
        return self.get(True)

    @controls.setter
    def controls(self, flag: bool):
        self.set(flag)

    @property
    def loop(self):
        """
        Specifies that the video will start over again, every time it is finished.

        Related Pages:

          https://www.w3schools.com/tags/tag_video.asp
          https://www.w3schools.com/tags/att_video_loop.asp

        :prop bool: Optional. Default value is false.
        """
        return self.get(False)

    @loop.setter
    def loop(self, flag: bool):
        self.set(flag)

    @property
    def preload(self):
        """
        Specifies if and how the author thinks the video should be loaded when the page loads.

        Related Pages:

          https://www.w3schools.com/tags/tag_video.asp
          https://www.w3schools.com/tags/att_video_preload.asp

        :prop value: Optional. The preload attribute specifies if and how the author thinks that the video
        should be loaded when the page loads.
        """
        return self.get('none')

    @preload.setter
    def preload(self, value: str = "auto"):
        value = value or "none"
        if self.options.verbose and value not in ("none", "auto", "metadata"):
            logging.warning("Not defined preload value %s" % value)
        self.set(value)

    @property
    def muted(self):
        """
        Specifies that the audio output of the video should be muted.

        The muted attribute is a boolean attribute.

        When present, it specifies that the audio output should be muted.

        Related Pages:

          https://www.w3schools.com/tags/tag_video.asp
          https://www.w3schools.com/tags/att_audio_muted.asp

        :prop flag: Optional. Default value is false.
        """
        return self.get(False)

    @muted.setter
    def muted(self, flag: bool):
        self.set(flag)

    @property
    def poster(self):
        """
        Specifies an image to be shown while the video is downloading, or until the user hits the play button.

        The poster attribute specifies an image to be shown while the video is downloading,
        or until the user hits the play button.

        Related Pages:

          https://www.w3schools.com/tags/tag_video.asp
          https://www.w3schools.com/tags/att_video_poster.asp

        :prop url: Url path for the image. Specifies the URL of the image file.
        """
        return self.get()

    @poster.setter
    def poster(self, url: str):
        self.set(url)

    @property
    def autoplay(self):
        """
        Set the autoplay flag.

        Specifies that the video will start playing as soon as it is ready.

        Usage::

        :prop flag: Optional. Default value is true.
        """
        return self.get(True)

    @autoplay.setter
    def autoplay(self, flag: bool):
        self.set(flag)


class OptCheckboxes(Options):
    component_properties = ("icon", "all_selected", "tooltip")

    @property
    def icon(self):
        """ The font-awesome icon reference. """
        return self._config_get("fas fa-check")

    @icon.setter
    def icon(self, value: str):
        self._config(value)

    @property
    def all_selected(self):
        return self._config_get(False)

    @all_selected.setter
    def all_selected(self, flag: bool):
        self._config(flag)

    @property
    def tooltip(self):
        return self._config_get("")

    @tooltip.setter
    def tooltip(self, value: str):
        self._config(value)

    @property
    def tooltip_options(self):
        return self._config_get({})

    @tooltip_options.setter
    def tooltip_options(self, values):
        self._config(values)


class OptCheck(Options):

    @property
    def icon_check(self):
        return self._config_get("fas fa-check")

    @icon_check.setter
    def icon_check(self, icon: str):
        self._config(icon)

    @property
    def icon_not_check(self):
        """ """
        return self._config_get("fas fa-times")

    @icon_not_check.setter
    def icon_not_check(self, icon: str):
        self._config(icon)

    @property
    def disable(self):
        """ """
        return self._config_get(False)

    @disable.setter
    def disable(self, flag: bool):
        self._config(flag)

    @property
    def green(self):
        """ """
        return self._config_get(self.page.theme.success[1])

    @green.setter
    def green(self, values):
        self._config(values)

    @property
    def red(self):
        """ """
        return self._config_get(self.page.theme.danger.base)

    @red.setter
    def red(self, values):
        self._config(values)


class OptionsButtonFilter(Options):
    component_properties = ("icon", "icon_filer")

    @property
    def is_number(self):
        return self.get(False)

    @is_number.setter
    def is_number(self, flag: bool):
        self.set(flag)

    @property
    def icon(self):
        return self.get("fas fa-align-center")

    @icon.setter
    def icon(self, value: str):
        self.set(value)

    @property
    def icon_filer(self):
        return self.get("fas fa-filter")

    @icon_filer.setter
    def icon_filer(self, value: str):
        self.set(value)


class OptionsButtonMenu(Options):
    component_properties = ("css_child", )

    @property
    def css_child(self):
        """ CSS Style for the sub menu """
        return self.get({"padding": "5px", "cursor": "pointer", "display": "block", "white-space": "nowrap",
                         "line-height": "%spx" % html_defaults.LINE_HEIGHT})

    @css_child.setter
    def css_child(self, values: dict):
        self._config(values)

    @property
    def css_cls_child(self) -> Optional[List[str]]:
        """ Add class to sub menu """
        return self.get(None)

    @css_cls_child.setter
    def css_cls_child(self, values: List[str]):
        self._config(values)


class OptionsButtons(OptionsWithTemplates):
    component_properties = ("value", "css", "selected", "delimiter", "classes", "disabled")

    @property
    def attributes(self) -> dict:
        """Add Other any HTML attributes for sub buttons"""
        return self._config_get()

    @attributes.setter
    def attributes(self, values: dict):
        self._config(values)

    @property
    def classes(self) -> Optional[List[str]]:
        """ Add CSS Classes for buttons """
        return self._config_get([self.component.style_refs["html-button"]])

    @classes.setter
    def classes(self, values: List[str]):
        self._config(values)

    @property
    def css(self) -> Optional[Dict[str, str]]:
        """Add CSS Classes for buttons """
        return self._config_get({})

    @css.setter
    def css(self, values: Dict[str, str]):
        self._config(values)

    @property
    def delimiter(self) -> str:
        """Add content delimiter to generate a string """
        return self._config_get(",")

    @delimiter.setter
    def delimiter(self, values: str):
        self._config(values)

    @property
    def disabled(self) -> str:
        """ASet the disable flag """
        return self._config_get("disabled")

    @disabled.setter
    def disabled(self, values: str):
        self._config(values)

    @property
    def max(self) -> str:
        """Set the maximum value to be selected"""
        return self._config_get()

    @max.setter
    def max(self, value: int):
        self._config(value)

    @property
    def selected(self) -> str:
        """Define the seleted flag from the record """
        return self._config_get("selected")

    @selected.setter
    def selected(self, value: str):
        self._config(value)

    @property
    def style(self) -> Union[str, dict]:
        """Field from record for CSS Style of classes """
        return self._config_get()

    @style.setter
    def style(self, values: Union[str, dict]):
        self._config(values)

    @property
    def title(self) -> str:
        """Define field for the component tooltip value"""
        return self._config_get()

    @title.setter
    def title(self, value: str):
        self._config(value)

    @property
    def value(self) -> str:
        """The value tag from the button definition """
        return self._config_get("value")

    @value.setter
    def value(self, values: str):
        self._config(values)