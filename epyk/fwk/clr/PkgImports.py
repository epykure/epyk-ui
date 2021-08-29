
from epyk.core.js import Imports

VERSION = '5.5.2'

CLARITY = {
  '@cds/core': {
    'version': VERSION,
    'website': 'https://clarity.design/get-started/developing/',
    'modules': [
      {'script': 'global.min.css', 'path': '@cds/core@%(version)s/', 'cdnjs': Imports.JSDELIVER},
      {'script': 'module.shims.min.css', 'path': '@cds/core@%(version)s/styles/', 'cdnjs': Imports.JSDELIVER},
    ]
  },
  '@cds/button': {
    #'req': [{'alias': '@cds/core'}],
    'version': VERSION,
    'website': 'https://clarity.design/get-started/developing/',
    'modules': [
      {'script': 'index.min.js', 'path': '@cds/core@%(version)s/button/', 'cdnjs': Imports.JSDELIVER},
    ]
  },
  '@cds/city': {
    'version': "1.1.0",
    'website': 'https://nhn.github.io/tui.date-picker/latest/',
    'modules': [
      {'script': 'default.min.css', 'path': '@cds/city@%(version)s/css/bundles/', 'cdnjs': Imports.JSDELIVER},
    ]
  }

}