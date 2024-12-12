

BOOTSTRAP = {
  'tempus-dominus': {
    'req': [
      {'alias': 'bootstrap'},
      {'alias': '@popperjs/core'}
    ],
    'version': '6.7.13',
    'website': 'https://getdatepicker.com/6/',
    'register': {'alias': 'datetimepicker', 'module': 'tempusdominus-bootstrap-4.min', 'npm': 'datetimepicker'},
    'modules': [
      {'script': 'tempus-dominus.min.js', 'path': 'tempus-dominus/%(version)s/js/'},
      {'script': 'tempus-dominus.min.css', 'path': 'tempus-dominus/%(version)s/css/'},
    ]},
  'tempusdominus-bootstrap-5': {
    'version': '5.39.0',
    'req': [
      {'alias': 'bootstrap'},
      {'alias': 'jquery'},
      {'alias': 'moment', "version": "2.29.0"}
    ],
    'website': 'https://getdatepicker.com/5-4/Installing/',
    'register': {'alias': 'datetimepicker', 'module': 'tempusdominus-bootstrap-4.min', 'npm': 'datetimepicker'},
    'modules': [
      {'script': 'tempusdominus-bootstrap-4.min.js', 'path': 'tempusdominus-bootstrap-4/%(version)s/js/'},
      {'script': 'tempusdominus-bootstrap-4.min.css', 'path': 'tempusdominus-bootstrap-4/%(version)s/css/'},
    ]},
  'tempusdominus-bootstrap-4': {
    'version': '5.39.0',
    'req': [
      {'alias': 'bootstrap'},
      {'alias': 'jquery'},
      {'alias': 'moment', "version": "2.29.0"}
    ],
    'website': 'https://getdatepicker.com/5-4/Installing/',
    'register': {'alias': 'datetimepicker', 'module': 'tempusdominus-bootstrap-4.min', 'npm': 'datetimepicker'},
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
    'version': '1.10.3',
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
  "time": None,
  "time": "bi bi-clock-fill",
  "close": "bi bi-x",
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
  "calendar": "bi bi-calendar-week",
  "spin": None,
  "next": "bi bi-arrow-right-short",
  "previous": "bi bi-arrow-left-short",
  "play": None,
  "stop": None,
  "today": "bi bi-calendar2-check",
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
