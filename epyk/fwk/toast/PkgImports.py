
TOAST = {
  'tui-date-picker': {
    'version': 'latest',
    'website': 'https://nhn.github.io/tui.date-picker/latest/',
    'register': {'variable': 'tuiDate', 'module': 'tui-date-picker'},
    'req_js': [  # depn only for requirejs
      {'alias': 'tui-time-picker'},
    ],
    'modules': [
      {'script': 'tui-date-picker.min.css', 'path': 'tui.date-picker/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'tui-date-picker.min.js', 'path': 'tui.date-picker/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]
  },
  'tui-time-picker': {
    'version': 'latest',
    'website': 'https://nhn.github.io/tui.date-picker/latest/',
    'register': {'variable': 'tuiTime', 'module': 'tui-time-picker'},
    'modules': [
      {'script': 'tui-time-picker.css', 'path': 'tui.time-picker/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'tui-time-picker.js', 'path': 'tui.time-picker/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]
  },
  'tui-code-snippet': {
    'version': 'latest',
    'website': 'https://nhn.github.io/tui.date-picker/latest/',
    'register': {'variable': 'tuiSnippet', 'module': 'tui-code-snippet.min'},
    'modules': [
      {'script': 'tui-code-snippet.min.js', 'path': 'tui.code-snippet/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]
  },
  'tui-calendar': {
    'req': [
      {'alias': 'tui-code-snippet'},
      {'alias': 'tui-date-picker'},
      {'alias': 'tui-time-picker'},
    ],
    'version': 'latest',
    'register': {'variable': 'tuiCalendar', 'module': 'tui-calendar'},
    'website': 'https://github.com/nhn/tui.calendar',
    'modules': [
      {'script': 'tui-calendar.min.js', 'path': 'tui-calendar/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'tui-calendar.min.css', 'path': 'tui-calendar/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]
  },
  '@toast-ui/chart': {
    'version': 'latest',
    'register': {'variable': 'tuiCharts', 'module': 'toastui-chart.min'},
    'website': 'https://github.com/nhn/tui.chart/tree/main/apps/chart',
    'modules': [
      {'script': 'toastui-chart.min.css', 'path': 'chart/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'toastui-chart.min.js', 'path': 'chart/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]
  },
  '@toast-ui/editor': {
    'version': 'latest',
    'website': 'https://github.com/nhn/tui.editor/tree/master/apps/editor',
    'modules': [
      {'script': 'toastui-editor.min.css', 'path': 'editor/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'toastui-editor-all.min.js', 'path': 'editor/%(version)s/',
       'cdnjs': 'https://uicdn.toast.com/'},
    ]

  },
  'tui-grid': {
    'version': 'latest',
    'website': 'https://github.com/nhn/tui.grid',
    'modules': [
      {'script': 'tui-grid.min.css', 'path': 'grid/%(version)s/', 'cdnjs': 'https://uicdn.toast.com/'},
      {'script': 'tui-grid.min.js', 'path': 'grid/%(version)s/', 'cdnjs': 'https://uicdn.toast.com/'},
    ]
  }
}
