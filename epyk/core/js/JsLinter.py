#!/usr/bin/python
# -*- coding: utf-8 -*-


def parse(data, prettify=None):
  frgs, spaces = [], 2
  if prettify:
    line = data.strip()
    in_brackets = line.split("{")
    row = []
    for r in in_brackets[0].split(";"):
      if r:
        row.append("%s%s" % ("".join(spaces * [" "]), r.strip()))
    frgs.append(";\n".join(row))
    for in_bracket in in_brackets[1:]:
      frgs.append("\n%s{\n" % "".join(spaces * [" "]))
      spaces += 2
      out_brackets = in_bracket.strip().split("}")
      row = []
      for r in out_brackets[0].split(";"):
        if r:
          row.append("%s%s" % ("".join(spaces * [" "]), r.strip()))
      frgs.append(";\n".join(row))
      for out_bracket in out_brackets[1:]:
        if out_bracket:
          row = []
          for r in out_bracket.split(";"):
            if r:
              row.append("%s%s" % ("".join(spaces * [" "]), r.strip()))
          frgs.append(";\n".join(row))
        spaces -= 2
        frgs.append("\n%s}\n" % "".join(spaces * [" "]))
  else:
    for l in data.split("\n"):
      frgs.append(l.strip())
  return "".join(frgs)
