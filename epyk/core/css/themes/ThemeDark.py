"""
Theme module for the Dark classes

All the themes are following the same structure and the are all inheriting from Theme
this will allow them to be converted to HTML to be able to check the colors.

A theme class must have the below class variables defined

  name    : The name of the theme to displayed in the navbar
  charts  : A list with the colors used for the series in the charts
  colors  : A list with the colors used for the HTML components
  greys   : A list with the shade of greys to be used within this theme
  warning : A tuple with the two colours used for warning (light, dark)
  danger  : A tuple with the two colours used for danger (light, dark)
  success : A tuple with the two colours used for success (light, dark)
"""

from epyk.core.css.themes import Theme


class Dark(Theme.Theme):
  _charts = [
    '#009999', '#336699', '#ffdcb9',
    '#cc99ff', '#b3d9ff', '#ffff99',
    '#000066', '#b2dfdb', '#80cbc4',
    '#e8f5e9', '#c8e6c9', '#a5d6a7', # green
    '#ffebee', '#ffcdd2', '#ef9a9a', # red
    '#f3e5f5', '#e1bee7', '#ce93d8', # purple
    '#ede7f6', '#d1c4e9', '#b39ddb', # deep purple
    '#e8eaf6', '#c5cae9', '#9fa8da', # indigo
    '#fffde7', '#fff9c4', '#fff59d', # yellow
    '#fff3e0', '#ffe0b2', '#ffcc80', # orange
    '#efebe9', '#d7ccc8', '#bcaaa4', # brown
  ]

  _colors = ['#263238', '#37474f', '#455a64', '#546e7a', '#607d8b', '#78909c','#90a4ae', '#b0bec5', '#cfd8dc', '#eceff1']
  _greys = ['#000000', '#212121', '#424242', '#616161', '#757575', '#9e9e9e', '#bdbdbd', '#e0e0e0', '#eeeeee',
            '#f5f5f5', '#FFFFFF']
  _warning, _danger, _success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#3bb194')


class Grey(Theme.Theme):
  _colors = ['#263238', '#37474f', '#455a64', '#546e7a',
            '#607d8b', '#78909c', '#90a4ae', '#b0bec5',
            '#cfd8dc', '#eceff1']

  _greys = ['#273037', '#212121', '#273037', '#3F484D',
           '#757575', '#9e9e9e', '#bdbdbd', '#e0e0e0',
           '#eeeeee', '#f5f5f5', '#FFFFFF']

  _charts = ['#009999', '#336699', '#ffdcb9',
            '#cc99ff', '#b3d9ff', '#ffff99',
            '#000066', '#b2dfdb', '#80cbc4',
            '#ffebee', '#ffcdd2', '#ef9a9a', '#f3e5f5',
            '#e1bee7', '#ce93d8', '#ede7f6', '#d1c4e9',
            '#b39ddb', '#e8eaf6', '#c5cae9', '#9fa8da', '#fffde7', '#fff9c4', '#fff59d', '#fff3e0', '#ffe0b2',
            '#ffcc80', '#efebe9', '#d7ccc8', '#bcaaa4']

  _warning = ('#FFF3CD', '#e2ac00')
  _danger = ('#F8D7DA', '#C00000')
  _success = ('#e8f2ef', '#3bb194')

