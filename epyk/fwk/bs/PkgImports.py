

BOOTSTRAP = {
  'tempusdominus-bootstrap-4': {
    'version': '5.39.0',
    'req': [
      {'alias': 'font-awesome'},
      {'alias': 'bootstrap'},
      {'alias': 'moment'},
      {'alias': 'jquery'}],
    'website': 'https://getdatepicker.com/5-4/Installing/',
    'register': {'alias': 'datetimepicker', 'module': 'bootstrap-datetimepicker.min', 'npm': 'datetimepicker'},
    'modules': [
      {'script': 'tempusdominus-bootstrap-4.min.js', 'path': 'tempusdominus-bootstrap-4/%(version)s/js/'},
      {'script': 'tempusdominus-bootstrap-4.min.css', 'path': 'tempusdominus-bootstrap-4/%(version)s/css/'},
    ]},
  'bootstrap-datetimepicker': {
    'version': '4.17.47',
    'req': [
      {'alias': 'moment'},
      {'alias': 'bootstrap', 'version': '3.4.1'}],
    'website': 'https://material.io/components',
    'register': {'alias': 'datetimepicker', 'module': 'bootstrap-datetimepicker.min', 'npm': 'datetimepicker'},
    'modules': [
      {'script': 'bootstrap-datetimepicker.min.js', 'path': 'bootstrap-datetimepicker/%(version)s/js/'},
      {'script': 'bootstrap-datetimepicker.min.css', 'path': 'bootstrap-datetimepicker/%(version)s/css/'},
    ]},
  'bootstrap-icons': {
    'version': '1.5.0',
    'website': 'https://icons.getbootstrap.com/',
    'modules': [
      {'script': 'bootstrap-icons.css', 'path': 'bootstrap-icons@%(version)s/font/',
       'cdnjs': 'https://cdn.jsdelivr.net/npm/'},
    ]
  },
  'bootstrap-autocomplete': {
    'version': '2.3.7',
    'website': 'https://bootstrap-autocomplete.readthedocs.io/en/latest/',
    'modules': [
      {'script': 'bootstrap-autocomplete.min.js', 'path': 'bootstrap-icons@%(version)s/font/',
       'cdnjs': 'https://cdn.jsdelivr.net/npm/'},
    ]
  }
}


# https://icons.getbootstrap.com/
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
  "square_plus": None,
  "square_minus": None,
  "minus": None,
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
  'user': None,
  'chevron_up': None,
  'chevron_down': None,
  'folder_open': None,
  'folder_close': None,
  'show': None,
  'hide': None,
  'star': None,
  'arrow_right': None,
  'arrow_left': None,
}
