#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.html import Defaults
from epyk.core.html.options import OptButton

# The list of JSS modules
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class Source(Html.Html):
    name = 'Source'
    tag = "source"

    def __init__(self, page: primitives.PageModel, path: str, video: str):
        super(Source, self).__init__(page, "")
        self.path = path
        self.video = video

    def __str__(self):
        self.attr["src"] = os.path.join(self.path, self.video)
        attrs = " ".join(['%s="%s"' % (k, v) for k, v in self.attr.items() if k not in ("class", 'css', 'id')])
        return "<%s %s></%s>" % (self.tag, attrs, self.tag)


class Media(Html.Html):
    name = 'Video'
    tag = "video"
    _option_cls = OptButton.OptMedia
    mime_mapping = {
        ".avi": "video/x-msvideo",
        ".mpeg": "video/mpeg",
        ".ogv": "video/ogg",
        ".webm": "video/webm",
        ".3gp": "video/3gpp",
        ".3g2": "video/3gpp2",
        ".mp4": "video/mp4",
    }

    def __init__(self, page: primitives.PageModel, video: str, path: str, width: tuple, height: tuple, html_code: str,
                 profile: Union[bool, dict], options: Optional[dict]):
        if path is None:
            path = Defaults.SERVER_PATH or os.path.split(video)[0]
        super(Media, self).__init__(page, {'path': path, 'video': video}, html_code=html_code, options=options,
                                    css_attrs={"width": width, 'height': height}, profile=profile)
        extension = video.split(".")[-1].lower()
        self._vals = Source(page, path, video)
        if ".%s" % extension in self.mime_mapping:
            self.add_options(name="type", value=self.mime_mapping[".%s" % extension])
            self._vals.attr["type"] = self.mime_mapping[".%s" % extension]
        else:
            if options.get("verbose", False):
                logging.warning("Missing MIME Type extension %s" % extension)
            self.add_options(name="type", value='%s/%s' % (self.name.lower(), extension))
            self._vals.attr["type"] = extension
        self.options.controls = True

    @property
    def options(self) -> OptButton.OptMedia:
        """ Property to set all the possible object for a Media (video and audio). """
        return super().options

    def __str__(self):
        if self.options.autoplay:
            self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self.options.autoplay, None))
        self.set_attrs(name="src", value=os.path.join(self.val.path, self.val.video))
        if self.options.controls:
            self.attr["controls"] = True
        return '<%s %s>%s</%s>' % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str(self._vals), self.tag)


class Audio(Media):
    name = 'Audio'
    tag = "audio"
    mime_mapping = {
        ".aac": "audio/aac",
        ".midi": "audio/midi",
        ".mp3": "audio/mp3",
        ".mid": "audio/midi",
        ".oga": "audio/ogg",
        ".weba": "audio/webm",
        ".wav": "audio/x-wav",
        ".3gp": "audio/3gpp",
        ".3g2": "audio/3gpp2",
    }

    def __str__(self):
        if self.options.autoplay:
            self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self.options.autoplay, None))
        self.set_attrs(name="src", value=os.path.join(self.val.path, self.val.video))
        return '<%(tag)s %(attrs)s>%(source)s</%(tag)s>' % {
            'attrs': self.get_attrs(css_class_names=self.style.get_classes()), "source": self.val, "tag": self.tag}


class Youtube(Html.Html):
    name = 'Youtube Video'
    tag = "div"

    EMBED_URL = "https://www.youtube.com/embed"

    def __init__(self, page: primitives.PageModel, link: str, width: tuple, height: tuple, html_code: str,
                 profile: Union[bool, dict], options: Optional[dict]):
        super(Youtube, self).__init__(
            page, link, css_attrs={"width": width, 'height': height}, html_code=html_code, profile=profile,
            options=options)
        self.video = page.ui.layouts.iframe(link)
        self.video.options.managed = False

    def __str__(self):
        return '''<%(tag)s %(attrs)s>%(iframe)s</%(tag)s>''' % {
            "tag": self.tag, 'attrs': self.get_attrs(css_class_names=self.style.get_classes()), "iframe": self.video.html()}

    @staticmethod
    def get_embed_link(youtube_link: str) -> str:
        """Simple function to convert a youtube link to the embedded version.

        Usage::

          html.HtmlMedia.Youtube.get_embed_link('https://www.youtube.com/watch?v=iPGgnzc34tY')

        :param youtube_link: The Youtube link of the online video.
        """
        return '%s/%s' % (Youtube.EMBED_URL, youtube_link.split('=')[-1])


class Camera(Html.Html):
    name = 'Camera'
    tag = "video"
    _option_cls = OptButton.OptMedia

    def __init__(self, page: primitives.PageModel, width: tuple, height: tuple, html_code: str,
                 profile: Union[bool, dict], options: Optional[dict]):
        super(Camera, self).__init__(
            page, "", html_code=html_code, css_attrs={"width": width, 'height': height}, profile=profile,
            options=options)
        self.options.controls = True
        self.options.autoplay = True

    @property
    def options(self) -> OptButton.OptMedia:
        """Property to set all the possible object for a Media (video and audio). """
        return super().options

    @property
    def dom(self) -> JsHtml.JsMedia:
        """The Javascript Dom object. """
        if self._dom is None:
            self._dom = JsHtml.JsMedia(self, page=self.page)
        return self._dom

    def __str__(self):
        if self.options.autoplay:
            self.set_attrs(name="autoplay", value=JsUtils.jsConvertData(self.options.autoplay, None))
        return '<%(tag)s %(attrs)s></%(tag)s><img src="">' % {
            "tag": self.tag, "attrs": self.get_attrs(css_class_names=self.style.get_classes())}
