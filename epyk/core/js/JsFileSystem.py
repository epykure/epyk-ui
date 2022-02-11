"""
Documentation:
    - https://www.html5rocks.com/en/tutorials/file/filesystem/
    - https://w3c.github.io/filesystem-api/
    - https://blog.teamtreehouse.com/building-an-html5-text-editor-with-the-filesystem-apis
"""

from typing import Optional
from epyk.core.py import primitives


class JsFileSystem:

  def __init__(self, page: Optional[primitives.PageModel] = None):
    self.page = page
    self._js = []

  def toStr(self):
    """

    :return:
    """
    return '''
      if (window.webkitRequestFileSystem !== undefined){
        console.log(window.webkitRequestFileSystem);
        window.webkitRequestFileSystem(window.TEMPORARY, 1024*1024, function(fs) {
          console.log(fs);
          fs.root.getFile('log.txt', {create: true}, function(fileEntry) {
              console.log(fileEntry);
          })
        })
      }'''
