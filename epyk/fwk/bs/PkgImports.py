

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
