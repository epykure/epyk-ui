

FLUENTUI = {
  'fabric-ui': {
    'version': "",
    'website': 'https://developer.microsoft.com/en-us/fabric-js',
    'modules': [
      {'script': 'fabric.min.css', 'path': '', 'cdnjs': "https://cdn.graph.office.net/prod/css/fabric-js"},
      {'script': 'fabric.min.js', 'path': '', 'cdnjs': "https://cdn.graph.office.net/prod/Scripts/fabric-js"},
    ]
  },
  'fabric-ui/components': {
    'version': "",
    'req': [{'alias': 'fabric-ui'}],
    'website': 'https://developer.microsoft.com/en-us/fabric-js',
    'modules': [
      {'script': 'fabric.components.min.css', 'path': '', 'cdnjs': "https://cdn.graph.office.net/prod/css/fabric-js"},
    ]
  },
  'fabric-ui/PickaDate': {
    'version': "",
    'req': [{'alias': 'fabric-ui'}],
    'website': 'https://developer.microsoft.com/en-us/fabric-js',
    'modules': [
      {'script': 'PickaDate.js', 'path': '', 'cdnjs': "https://cdn.graph.office.net/prod/Scripts/fabric-js"},
    ]
  },
}


# https://developer.microsoft.com/en-us/fluentui#/controls/web/icon
ICON_MAPPINGS = {
  "danger": None,
  "error": None,
  "search": None,
  "save": None,
  "excel": None,
  "times": None,
  "close": None,
  "upload": None,
  "word": None,
  "csv": None,
  "code": None,
  "download": None,
  "info": None,
  "edit": None,
  "clock": None,
  "lock_open": None,
  "compress": None,
  "calendar": None,
  "spin": None,
  "next": None,
  "previous": None,
  "play": None,
  "stop": None,
  "zoom_out": None,
  "zoom_in": None,
  "warning": None,
  "refresh": None,
  "pdf": None,
  "plus": None,
  "delete": None,
  "zoom": None,
  "capture": None,
  "remove": None,
  "clear": None,
  "table": None,
  "check": None,
  "wrench": None,
  "rss": None,
  "facebook": None,
  "messenger": None,
  "twitter": None,
  "twitch": None,
  "instagram": None,
  "linkedIn": None,
  "youtube": None,
  "github": None,
  "python": None,
  "stackoverflow": None,
  "envelope": None,
  "question": None,
  "google_plus": None,
  "circle": None,
  'user': None
}
