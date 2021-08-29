from epyk.core.js import Imports

VERSION = "6.4.0"

EVERGREEN = {
  'evergreen-ui': {
    'version': VERSION,
    'website': 'https://evergreen.segment.com/components',
    'modules': [
      {'script': 'index.js', "type": "module", 'path': 'evergreen-ui@%(version)s/commonjs/', 'cdnjs': Imports.JSDELIVER},
    ]
  },
}