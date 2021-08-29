
MATERIAL_DESIGN_COMPONENTS = {
  'material-icons': {
    'website': 'https://material.io/resources/icons/?style=baseline',
    'services': [
      {'type': 'css', 'url': 'https://fonts.googleapis.com/icon',
       'values': {
         'family': 'Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp'}},
    ]
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
