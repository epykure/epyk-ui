#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


class MarkDown(object):
  def __init__(self, page):
    self.page = page

  def resolve(self, data, css_attrs=None):
    """

    :param data:
    """
    RULES = {
      '\[(.*)\]\((.*)\)': {'cls': self.page.ui.link, 'attrs': ["text", "url"], 'pattern': "[%s](%s)"},
      '^## (.*)(.*)$': {'cls': self.page.ui.subtitle, 'attrs': ["text"], 'pattern': "## %s%s"},
      '^# (.*)(.*)$': {'cls': self.page.ui.title, 'attrs': ["text"], 'pattern': "# %s%s"},
    }
    convert_data = data
    count, map_objs = 0, {}
    for r, cls in RULES.items():
      m = re.findall(r, data, re.MULTILINE)
      if m is not None:
        for g in m:
          attrs = dict(zip(cls['attrs'], g))
          map_objs["%s_%s" % (cls['cls'].__name__, count)] = cls['cls'](**attrs)
          if css_attrs is not None and map_objs["%s_%s" % (cls['cls'].__name__, count)].name in css_attrs:
            map_objs["%s_%s" % (cls['cls'].__name__, count)].css(css_attrs[map_objs["%s_%s" % (cls['cls'].__name__, count)].name])
          convert_data = convert_data.replace(cls['pattern'] % g, "||%s_%s||" % (cls['cls'].__name__, count))
          count += 1
    resolved_data = []
    for rec in convert_data.split("||"):
      resolved_data.append(map_objs.get(rec, rec))
    return resolved_data

