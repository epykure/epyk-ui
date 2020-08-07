#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import json


RULES = {
  '\!\[(.*)\]\((.*)\)': {'cls': 'page.ui.img', 'attrs': ["tooltip", "text"], 'pattern': "![%s](%s)"},
  '\[(.*)\]\((.*)\)': {'cls': 'page.ui.link', 'attrs': ["text", "url"], 'pattern': "[%s](%s)"},
  '\*\*\((.*)\)\*\*': {'cls': 'page.ui.tags.i', 'attrs': ["text"], 'pattern': "**%s**"},
  '\_\_\((.*)\)\_\_': {'cls': 'page.ui.tags.b', 'attrs': ["text"], 'pattern': "__%s__"},
  '^## (.*)(.*)$': {'cls': 'page.ui.subtitle', 'attrs': ["text"], 'pattern': "## %s%s"},
  '^# (.*)(.*)$': {'cls': 'page.ui.title', 'attrs': ["text"], 'pattern': "# %s%s"},
  '^___$': {'cls': 'page.ui.layouts.hr', 'attrs': [], 'pattern': "___"},
}


class MarkDown(object):

  def __init__(self, page):
    self.page = page

  @classmethod
  def translate(cls, data):
    """

    :param data:
    """
    convert_data = data
    count, map_objs = 0, {}
    for r, interface in RULES.items():
      m = re.findall(r, data, re.MULTILINE)
      if m is not None:
        for g in m:
          attrs = dict(zip(interface['attrs'], g))
          map_objs["%s_%s" % (interface['cls'], count)] = "%s(%s)" % (interface['cls'], ", ".join(["%s=%s" % (k, json.dumps(v)) for k, v in attrs.items()]))
          if "%s" in interface['pattern']:
            convert_data = convert_data.replace(interface['pattern'] % g, "||%s_%s||" % (interface['cls'], count))
          else:
            convert_data = convert_data.replace(interface['pattern'], "||%s_%s||" % (interface['cls'], count))
          count += 1
    resolved_data = []
    for rec in convert_data.split("||"):
      resolved_data.append(map_objs.get(rec, rec))
    return resolved_data

  def resolve(self, data, css_attrs=None):
    """

    :param data:
    """
    CLS_MAPPING = {
      '\[(.*)\]\((.*)\)': self.page.ui.link,
      '^## (.*)(.*)$': self.page.ui.subtitle,
      '^# (.*)(.*)$': self.page.ui.title,
    }
    convert_data = data
    count, map_objs = 0, {}
    for r, cls in RULES.items():
      m = re.findall(r, data, re.MULTILINE)
      if m is not None:
        for g in m:
          attrs = dict(zip(cls['attrs'], g))
          interface = CLS_MAPPING[r]
          map_objs["%s_%s" % (interface.__name__, count)] = interface(**attrs)
          if css_attrs is not None and map_objs["%s_%s" % (interface.__name__, count)].name in css_attrs:
            map_objs["%s_%s" % (interface.__name__, count)].css(css_attrs[map_objs["%s_%s" % (interface.__name__, count)].name])
          convert_data = convert_data.replace(cls['pattern'] % g, "||%s_%s||" % (interface.__name__, count))
          count += 1
    resolved_data = []
    for rec in convert_data.split("||"):
      resolved_data.append(map_objs.get(rec, rec))
    return resolved_data


if __name__ == '__main__':
  data = '''
![rgrhr](rhrhr)
[rgrhr](rhrhr)
# This is a title
___
This is a text **with an extra** on this 

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
'''

  trans_data = MarkDown.translate(data)
  print(trans_data)
