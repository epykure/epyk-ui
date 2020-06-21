"""
## Markdown Framework

This framework is following the Markdown standard in order to write static documentation.
As part of the creation of the different components some extended rules have been added in order to ensure the use of very bespoke components and also allow a great flexibility.
This documentation will show you the different markdowns rules already in place.

If you have any questions regarding the principle of Markdowns, please have a quick look at the [wikipage](https://fr.wikipedia.org/wiki/Markdown)
Also the below link could be quite interesting to get more examples:
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Markdown syntax is a standard used in many programming language but also by website to make the first implementation much easier
"""

import re
import os
import json
import sys
import inspect
import importlib
import logging


class DocCollection(list):
  def __init__(self, report):
    self._report = report

  def breadcrumb(self, paths, options=None, lang="eng"):
    """

    :return:
    """
    bubbles = []
    rows = ["<a href='/api'>Framework</a> / <a href='/api?module=local'>Scripting API</a>"]
    if len(paths) > 1:
      rows[0] = "%s / ... <a href=''>%s</a>" % (rows[0], paths[0])
    if options is not None:
      for key, val in options.items():
        if paths[-1] == key:
          bubbles.append(
            "<div title='%s' style='cursor:pointer;padding:1px 5px;border:1px solid black;display:inline-block;margin:0 2px;border-radius:5px;color:white;background-color:%s'>%s</div>" % (val[lang], self._report.getColor("colors", 5), key))
        else:
          bubbles.append("<a href='/api?enum=%s' title='%s' style='cursor:pointer;padding:1px 5px;border:1px solid black;display:inline-block;margin:0 2px;border-radius:5px;color:black;text-decoration:none'>%s</a>" % (key, val[lang], key) )
      rows.append("<div style='margin:3px 0'>%s</div>" % "".join(bubbles))
    self.append("<div>%s</div>" % "".join(rows))

  def breadcrumb2(self, levels, select_path):
    """

    :param levels:
    :param select_path:

    :return:
    """
    rows = []
    for i, vals in enumerate(levels):
      bubbles = []
      for val in vals:
        if val.lower() == select_path[i].lower():
          bubbles.append("<div style='cursor:pointer;padding:1px 5px;border:1px solid black;display:inline-block;color:white;background-color:%s;margin:0 2px;border-radius:5px'>%s</div>" % (self._report.getColor("greys", 9), val) )
        else:
          bubbles.append("<div style='cursor:pointer;padding:1px 5px;border:1px solid black;display:inline-block;margin:0 2px;border-radius:5px'>%s</div>" % val)
      rows.append("<div style='margin:3px 0'>%s</div>" % "".join(bubbles))
    self.append("<div>%s</div>" % "".join(rows))
    return self

  def title(self, val, level=1, css_pmts=None):
    """

    :param val:
    :param level:
    :param css_pmts:

    :return:
    """
    if val != '':
      self.append("%s %s" % ("".join(['#'] * level), val), css_pmts)
    return self

  def formula(self, val):
    """

    :param val:
    :return:
    """
    if val != '':
      self.append('$$ %s $$' % val)
    return self

  def link(self, val, url, icon='fas fa-chevron-circle-right', cssPmts=None):
    """

    :param val:
    :param url:
    :param icon:
    :param cssPmts:

    :return:
    """
    self.append("&nbsp;&nbsp;[!(%s) %s](%s)" % (icon, val, url), cssPmts)
    return self

  def hr(self):
    """

    :return:
    """
    self.append("***")
    return self

  def table(self, header, records, category='base', cssPmts=None, pmts=None):
    """

    :param header:
    :param records:
    :param category:
    :param cssPmts:
    :param pmts:

    :return:
    """
    data = ["|".join(header)]
    for rec in records:
      if isinstance(rec, dict):
        row = [rec[h] for h in header]
      else:
        row = rec
      data.append("|".join(row))
    if pmts is not None:
      data.append("--%s" % ";".join(["%s:%s" % (k, v) for k, v in pmts.items()]))
    if cssPmts is not None:
      data.append("@%s" % ";".join(["%s:'%s'" % (k, v)   for k, v in cssPmts.items()]))
    self.append("\n".join(["---Table:%s" % category] + data + ["---"]))
    return self

  def append(self, val, css_pmts=None):
    """

    :param val:
    :param css_pmts:

    :return:
    """
    if isinstance(val, list):
      val= "\n".join(val)
    if css_pmts is not None:
      val = "%s css%s" % (val, json.dumps(css_pmts).replace('"', ''))
    for v in val.split("\n\n"):
      super(DocCollection, self).append("%s\n" % v)
    return self

  def add(self, doc_obj, key):
    """

    :param doc_obj:
    :param key:

    :return:
    """
    self.append(doc_obj.getAttr(key))
    if doc_obj.source is not None:
      self.src(doc_obj.source)
    return self

  def src(self, source):
    """

    :param source:

    :return:
    """
    self.append("<div style='width:100%%;color:%s;font-style:italic;text-align:right;font-size:12px;padding-right:5px'>Source: %s</div>" % (self._report.getColor('greys', 4), source))
    return self

  def code(self, vals, language='python'):
    """

    :param vals:
    :param language:

    :return:
    """
    if isinstance(vals, list):
      vals= "\n".join(vals)
    if vals != '':
      match = re.search(">>>\((.*)\)", vals)
      if match:
        vals = vals.replace(match.group(0), '')
        vals = "%s\n>>> %s" % (vals, match.group(1))
      self.append("\n".join(["```%s" % language, vals.strip(), "```"]))
    return self


class DocString(dict):
  source = None

  def getAttr(self, dsc):
    return "\n".join(self.get(dsc, ['']))


class Convertor(object):
  def __init__(self, src=None):
    self.__src = src

  def icon(self, val):
    """

    :param val:
    :return:
    """
    pattern = re.compile("!\((.*)\)")
    res = pattern.search(val)
    if res is not None:
      for grp in res.groups():
        i = self.__src.ui.tags.i("")
        i.options.managed = False
        i.attr["class"] = [grp]
        val = val.replace("!(%s)" % grp, i.html())
    return val

  def link(self, val):
    """

    :param val:
    :return:
    """
    pattern = re.compile("\[(.*)\]\((.*)\)")
    res = pattern.search(val)
    if res is not None:
      results = res.groups()
      for i in range(len(results)//2):
        text = results[2*i]
        url = results[2*i + 1]
        l = self.__src.ui.link(text, url)
        l.options.managed = False
        val = val.replace("[%s](%s)" % (text, url), l.html())
    return val

  def bold(self, val):
    """
    Add the bold HTML tags to a string is ** markdown

    :param val: String. The text
    :return: String. The converted text
    """
    res = str(val).split("**")
    if len(res) > 1:
      tmp = []
      for i, r in enumerate(res):
        if i % 2 == 1:
          b = self.__src.ui.tags.b(r)
          b.options.managed = False
          tmp.append(b.html())
        else:
          tmp.append(r)
      return "".join(tmp)

    return val

  def italic(self, val):
    """
    Add the Italic HTML tags to a string is * markdown

    :param val: String. The text
    :return: String. The converted text
    """
    res = val.split("*")
    if len(res) > 1:
      tmp = []
      for i, r in enumerate(res):
        if i % 2:
          i = self.__src.ui.tags.i(r)
          i.options.managed = False
          tmp.append(i.html())
        else:
          tmp.append(r)
      return "".join(tmp)

    return val

  def highlighted(self, val):
    """
    Add the u HTML tags to a string is __ markdown

    :param val: String. The text
    :return: String. The converted text
    """
    res = str(val).split("__")
    if len(res) > 1:
      tmp = []
      for i, r in enumerate(res):
        if i % 2:
          u = self.__src.ui.tags.u(r)
          u.options.managed = False
          tmp.append(u.html())
        else:
          tmp.append(r)
      return "".join(tmp)

    return val

  def deleted(self, val):
    """
    Add the deleted HTML tags to a string is -- markdown

    :param val: String. The text
    :return: String. The converted text
    """
    res = str(val).split("--")
    if len(res) > 1:
      tmp = []
      for i, r in enumerate(res):
        if i % 2:
          i = self.__src.ui.tags.delete(r)
          i.options.managed = False
          tmp.append(i.html())
        else:
          tmp.append(r)
      return "".join(tmp)

    return val

  def all(self, val):
    """

    :param val:
    :return:
    """
    val = self.bold(str(val))
    val = self.highlighted(val)
    val = self.deleted(val)
    val = self.icon(val)
    val = self.link(val)
    val = self.italic(val)
    return val


class MarkDown(object):
  markDownMappings, markDownBlockMappings = None, None

  def __init__(self, full_path=None, report=None):
    self._report = report
    sys.path.append(os.path.join(os.getcwd(), 'epyk', 'core'))
    if full_path is not None:
      content = ""
      if full_path.endswith('amd'):
        py_file = open(full_path)
        content = py_file.read()
        py_file.close()
      self.content = content.split("\n\n")
    self.load_modules()

  def load_modules(self):
    """
    Fabric to load all the components in memory and use the match logic
    """
    # Store the modules
    from epyk.core import html
    from epyk.core.html import graph
    from epyk.core.html import tables

    self.markDownMappings, self.markDownBlockMappings = [], []
    for alias, mod in [('html', html), ('tables', tables), ('graph', graph)]:
      for script in os.listdir(os.path.dirname(mod.__file__)):
        if script.endswith(".py"):
          if alias in ['tables', 'graph']:
             mod_path = "epyk.core.html.%s.%s" % (alias, script.replace(".py", ""))
          else:
             mod_path = "epyk.core.html.%s" % script.replace(".py", "")
          for name, obj in inspect.getmembers(importlib.import_module(mod_path), inspect.isclass):
            try:
              if inspect.isclass(obj):
                if hasattr(obj, 'matchMarkDown'):
                  self.markDownMappings.append({'match': obj.matchMarkDown, 'convert': obj.convertMarkDown, 'name': name})
                elif hasattr(obj, 'matchMarkDownBlock'):
                  self.markDownBlockMappings.append({'match': obj.matchMarkDownBlock, 'convert': obj.convertMarkDownBlock, 'name': name, 'endBlock': obj.matchEndBlock})
            except Exception as err:
              logging.warning("%s, error %s" % (script, err))

  def find_block(self, block_split):
    """
    Function used to recognize block component

    :param block_split: The list of line which represents a component

    :return: The Ares Object
    """
    for blockMapping in self.markDownBlockMappings:
      if blockMapping['match'](block_split) is not None:
        return blockMapping

  def find_line(self, line, report):
    """

    :param line:
    :param report:

    :return:
    """
    for line_mapping in self.markDownMappings:
      reg_exp_result = line_mapping['match'](line)
      if reg_exp_result:
        return line_mapping['convert'](line, reg_exp_result, report)

  def convert(self, out_file_path):
    """

    :param out_file_path:

    :return:
    """
    out_file = open(out_file_path, 'w')
    converted_data = self.parse(self.content)
    for line in converted_data:
      out_file.write("%s\n" % line)
    for block in self.content:
      lines = block.split("\n")
    out_file.close()

  def load(self, report, data):
    """
    Convert the markdown static string to Python object.

    :param report:
    :param data:

    :return:
    """
    htmlObjs, j, spare_lines = [], 0, []
    if not isinstance(data, list):
      data = data.strip().split("\n\n")
    for i, block in enumerate(data):
      if j > 0:
        j -= 1
        continue

      lines = block.strip().split("\n")
      convert_block = self.find_block(lines)
      if convert_block is None:
        j = 0
        convert_line = self.find_line(lines[0].strip(), report)
        if convert_line is None:
          htmlObjs.append(report.ui.texts.paragraph(block))
        else:
          htmlObjs.append(report.components[report.content[-1]])
      else:
        block_data = lines
        for j, block in enumerate(data[i+1:]):
          if convert_block['endBlock'](lines[-1].strip()):
            break

          block_data.append("")
          lines = block.strip().split("\n")
          block_data.extend(lines)

        for v in convert_block['convert'](block_data, report):
          block_data.append(v)
        htmlObjs.append(report.components[report.content[-1]])
    return htmlObjs

  def parse(self, data, report=None, title=''):
    """

    :param data:
    :param report:
    :param title:

    :return:
    """
    if data is None:
      return ""

    out_file, j = ["TITLE='%s'" % title, "def report(rptObj):"], 0
    if not isinstance(data, list):
      data = data.split("\n\n")
    for i, block in enumerate(data):
      if j > 0:
        j -= 1
        continue

      lines = block.strip().split("\n")
      convert_block = self.find_block(lines)
      if convert_block is None:
        j = 0
        convertLine = self.find_line(lines[0], report)
        if convertLine is None:
          out_file.append("  rptObj.ui.texts.paragraph(%s)" % (json.dumps(block)))
          if report is not None:
            report.ui.texts.paragraph(block)
        else:
          for v in convertLine:
            out_file.append("  %s" % v)
      else:
        block_data = lines
        for j, block in enumerate(data[i+1:]):
          if convert_block['endBlock'](lines[-1].strip()):
            break

          block_data.append("")
          lines = block.strip().split("\n")
          block_data.extend(lines)
        complex_component = convert_block['convert'](block_data, report)
        for v in complex_component:
          block_data.append(v)
        out_file.append("  %s" % "".join(complex_component))
    return out_file

  @classmethod
  def parse_restructured_text(cls, text, report=None, lang='eng'):
    """
    Parse a reStructured type Documentation string
    This function will both:
      - return the string corresponding to the internal Markdown definition
      - Add the components to the report object (if defined)

    Example
    MarkDown.parse_restructured_text(MarkDown.loadsDsc.__doc__)

    Related Pages:

      https://en.wikipedia.org/wiki/ReStructuredText
    https://mail.python.org/pipermail/python-dev/2002-April/022131.html

    :param report: The report object
    :param text: The doc string to be parsed
    :param lang: The code for the language

    :return: A python dictionary with the documentation
    """
    doc_keywords = [("Documentation", 'documentation'), ("Example", 'examples')]
    ide_keywords = {'returns': re.compile(":return: (.*)"), 'params': re.compile(":param (.*): (.*)"),
                    'types': re.compile(":type (.*): (.*)")}
    section = 'desc'
    result = {'examples': [], 'documentation': [], 'desc': []}
    if text is None:
      return result

    for l in text.strip().split("\n"):
      line, is_section = l.strip(), False
      for doc_keyword, doc_tag in doc_keywords:
        if line == doc_keyword:
          section, is_section = doc_tag, True

      if not is_section:
        for reg_type, reg_keyword in ide_keywords.items():
          groups = reg_keyword.match(line)
          if groups is not None:
            if len(groups.groups()) > 1:
              result.setdefault(reg_type, {})[groups.group(1)] = groups.group(2)
            else:
              result.setdefault(reg_type, []).append(groups.group(1))
            break

        else:
          result.setdefault(section, []).append(line)
    return result

  def parse_module(self, module, report=None, lang='eng'):
    """
    Parse the documentation in the module

    Example
    md = PyMarkdown.MarkDown(report=Ares.Report()).parse_module(Js)

    :param module: An imported Python module
    :param report: The report object
    :param lang: The code for the language

    :return: A python dictionary with the module documentation
    """
    if report is None:
      report = self._report
    if report is not None:
      report.ui.title(module.__name__, level=1)
      self.parse(module.__doc__, report=report)
    result = {"classes": {}, "functions": {}, "content": module.__doc__}
    for name, obj in inspect.getmembers(module):
      if inspect.isfunction(obj):
        if report is not None:
          report.ui.title(name, level=3)

        fncDoc = self.parse_restructured_text(obj.__doc__, report, lang)
        self.parse(fncDoc['desc'], report=report)
        if len(fncDoc['examples']) > 0:
          report.ui.title("Examples", level=4)
          self.parse(fncDoc['examples'], report=report)
        result["functions"][name] = fncDoc
      elif inspect.isclass(obj):
        if obj.__module__ == module.__name__:
          if report is not None:
            report.ui.title(name, level=2)
          result["classes"][name] = self.parse_class(obj, report, lang)
    return result

  def parse_class(self, className, report=None, lang='eng'):
    """

    :param className:
    :param report:
    :param lang:

    :return: A python dictionary with the class documentation
    """
    result = {"properties": {}, "functions": {}}
    for name, obj in inspect.getmembers(className):
      if report is not None:
        report.ui.title(name, level=2)
      if inspect.isfunction(obj) and obj.__doc__ is not None:
        fnc_doc = self.parse_restructured_text(obj.__doc__, report, lang)
        self.parse(fnc_doc['desc'], report=report)
        if len(fnc_doc['examples']) > 0:
          report.ui.title("Examples", level=4)
          self.parse(fnc_doc['examples'], report=report)
        result["functions"][name] = fnc_doc
        #result["functions"][name] = cls.parse_restructured_text(obj.__doc__, report, lang)
      elif inspect.isdatadescriptor(obj) and obj.__doc__ is not None:
        result["properties"][name] = self.parse_restructured_text(obj.__doc__, report, lang)
    return result

  @classmethod
  def loads_dsc(cls, module_name, lang='eng'):
    """
    Load the documentation from the DSC variable of a given module.

    :param module_name: The Python Module Name
    :param lang: The code for the language

    :return: The docString object
    """
    if hasattr(module_name, 'DSC'):
      docStrObj = cls.loads(module_name.DSC.get(lang, module_name.DSC['eng']))
    else:
      docStrObj = cls.loads("")
    docStrObj.source = "/%s.py" % module_name.__name__.replace(".", "/")
    return docStrObj

  @staticmethod
  def loads(doc_string, section=None):
    """
    Load the documentation from a bespoke String variable.
    The string variable should have the expected labels in order to be correctly loaded and then parsed as a Markdown string

    :return: The docString object

    :param doc_string:
    :param section:
    :return:
    """
    if doc_string is None:
      return DocString()

    doc_string = doc_string.replace("https:", "https\\:").replace("http:", "http\\:")
    data, category = {}, None
    for com in doc_string.split("\n"):
      line = com.strip()
      if line.startswith(":"):
        match = re.search(":([a-zA-Z 0-9]*):(.*)", line)
        if match is not None:
          results = match.groups()
          category = results[0]
          if not category in data:
            data[category] = []
          doc_line = results[1].strip()
      else:
        doc_line = line
      if category is not None:
        data[category].append(doc_line)
    if section is not None:
      return DocString(data).getAttr(section)

    return DocString(data)

