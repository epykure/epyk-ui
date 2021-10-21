
MATERIAL_DESIGN_COMPONENTS = {
  'material-design-icons': {
    'website': 'https://material.io/resources/icons/?style=baseline',
    'services': [
      {'type': 'css', 'url': 'https://fonts.googleapis.com/css2',
       'values': {
         'family': 'Material+Icons'}},
    ],
    'modules': []
  },

  'material-components-web': {
    'version': '10.0.0',
    'website': 'https://material.io/components',
    'register': {'alias': 'mdc', 'module': 'material-components-web.min', 'npm': 'mdc'},
    'modules': [
      {'script': 'material-components-web.min.js', 'path': 'material-components-web/%(version)s/'},
      {'script': 'material-components-web.min.css', 'path': 'material-components-web/%(version)s/'}
    ]},
}


# https://fonts.google.com/icons?selected=Material+Icons
ICON_MAPPINGS = {
  "danger": "warning",
  "error": "error",
  "search": "search",
  "save": "save",
  "excel": "table_view",
  "times": "close",
  "close": "cancel",
  "upload": "upload",
  "word": None,
  "csv": None,
  "code": "code",
  "download": "download",
  "info": "help",
  "edit": 'edit',
  "clock": "schedule",
  "lock_open": "lock_open",
  "compress": "compress",
  "calendar": "event_note",
  "spin": "autorenew",
  "next": "arrow_right",
  "previous": "arrow_left",
  "play": "play_arrow",
  "stop": "stop",
  "zoom_out": "zoom_out",
  "zoom_in": "zoom_in",
  "warning": "warning",
  "refresh": "sync",
  "pdf": "picture_as_pdf",
  "plus": "add_box",
  "delete": "delete",
  "zoom": "loupe",
  "capture": "content_paste",
  "remove": "highlight_off",
  "clear": "clear",
  "table": "table_view",
  "check": "check",
  "wrench": "build",
  "rss": "rss_feed",
  "facebook": None,
  "messenger": "textsms",
  "twitter": "forum",
  "twitch": "featured_video",
  "instagram": "textsms",
  "linkedIn": "textsms",
  "youtube": 'smart_display',
  "github": None,
  "python": None,
  "stackoverflow": None,
  "envelope": 'mail',
  "question": 'help',
  "google_plus": None,
  "circle": 'circle',
  'user': None
}
