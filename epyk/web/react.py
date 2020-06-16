
from epyk.core import Page
from epyk.web import node


JS_MODULES_IMPORTS = {
  'showdown': '''
import Showdown from 'showdown';
var showdown = Showdown;
'''
}


class React(node.Node):
  pass
