#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.css import Defaults as Defaults_css


class News(object):
  def __init__(self, context):
    self.parent = context

  def miniature(self, title, url, image, category="", align="left", width=(100, '%'), height=(None, "px"), options=None):
    """

    :param title:
    :param url:
    :param image:
    :param category:
    :param align:
    :param width:
    :param height:
    :param options:
    :return:
    """
    container = self.parent.context.rptObj.ui.col(align=align, width=width, height=height, position="top")
    container.style.css.margin = "20px auto"
    container.style.css.padding = "5px"
    if not hasattr(category, 'options'):
      category = self.parent.context.rptObj.ui.text(category)
      category.style.css.display = "block"
    if not hasattr(title, 'options'):
      title = self.parent.context.rptObj.ui.link(self.parent.context.rptObj.py.encode_html(title), url)
      title.style.css.display = "block"
      title.style.css.color = self.parent.context.rptObj.theme.greys[-1]
      title.style.css.bold()
      title.style.css.text_decoration = None
    if image is not None:
      if not hasattr(image, 'options'):
        split_url = os.path.split(image)
        container.image = self.parent.context.rptObj.ui.img(split_url[1], path=split_url[0])
        container.image.style.css.margin_bottom = "10px"
        container.add(container.image)
    container.add(self.parent.context.rptObj.ui.col([category, title]))
    return container
