"""
Documentation:
    - https://www.html5rocks.com/en/tutorials/file/filesystem/
    - https://w3c.github.io/filesystem-api/
    - https://blog.teamtreehouse.com/building-an-html5-text-editor-with-the-filesystem-apis
"""

from epyk.core.js import JsUtils


class JsFileSystem:
  class __internal:
    _context = {}

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
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
