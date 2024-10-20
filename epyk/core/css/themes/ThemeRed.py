"""
Theme module for the Red classes
"""

from epyk.core.css.themes import Theme


class Red(Theme.Theme):
    name = "red"
    _charts = [
        '#009999', '#336699', '#ffdcb9',
        '#cc99ff', '#b3d9ff', '#ffff99',
        '#000066', '#b2dfdb', '#80cbc4',
        '#e0f2f1', '#b2dfdb', '#80cbc4',  # teal
        '#ffebee', '#ffcdd2', '#ef9a9a',  # red
        '#f3e5f5', '#e1bee7', '#ce93d8',  # purple
        '#ede7f6', '#d1c4e9', '#b39ddb',  # deep purple
        '#e8eaf6', '#c5cae9', '#9fa8da',  # indigo
        '#fffde7', '#fff9c4', '#fff59d',  # yellow
        '#fff3e0', '#ffe0b2', '#ffcc80',  # orange
        '#efebe9', '#d7ccc8', '#bcaaa4',  # brown
    ]

    _colors = ["#FFEBEE", '#FFCDD2', '#EF9A9A', '#E57373', '#EF5350', '#F44336', '#E53935', '#D32F2F',
               '#C62828', '#B71C1C']
    _warning, _danger, _success = ['#FFF3CD', '#e2ac00'], ["#F8D7DA", "#C00000"], ['#e8f2ef', '#3bb194']


class Pink(Red):
    name = "pink"
    _colors = ["#ffffff", "#fff5f6", "#ffe9f4", "#ffdbe6", "#ffced9", "#ffc0cb", "#f1b3be", "#e3a5b0", "#d598a3"]
    _warning, _danger, _success = ['#FFF3CD', '#e2ac00'], ["#F8D7DA", "#C00000"], ['#e8f2ef', '#3bb194']
