"""
Default parameters for the HTML components.

This can be overridden by the server setting or even locally in the report
"""

COMP_PREFIX = 'epyk'

SERVER_PATH = "/img"

CHART_FAMILY = "chartJs"
TABLE_FAMILY = "tabulator"

#
ENTITIES_ADD_ON = ""

# Constant for all the input components
LINE_HEIGHT = 20
BIG_ICONS = 15

#
HTML_HIGHLIGHT = {"border": {'attr': "1px solid %(color)s", 'color': ("success", 1)}}

FAVICON_URL = "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo.ico"
FAVICON_DEV_URL = 'https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_dev.ico'

# Component defaults
BUTTONS_CHECK_HEIGHT = 20
INPUTS_MIN_WIDTH = 140
INPUTS_TOGGLE_WIDTH = 40
LABEL_WIDTH = 100
INPUTS_POSITION = "center"
INPUTS_RANGE_THUMB = 10
TEXTS_SPAN_WIDTH = 100
TEXTS_SPAN_HEIGHT = 100

SVGNS = 'http://www.w3.org/2000/svg'

CHARTS_HEIGHT_PX = 330


# templates for the different states of a component
TEMPLATE_LOADING_ONE_LINE = "`<i class='fas fa-cog fa-spin' style='margin-right:5px'></i>Loading....`"
TEMPLATE_LOADING_ICON = "`<i class='fas fa-cog fa-spin' style='margin-right:5px'></i>`"
TEMPLATE_ERROR_ONE_LINE = "`<i class='fas fa-exclamation-triangle' style='margin-right:5px;color:red'></i>Error during the processing`"
TEMPLATE_ERROR_ICON = "`<i class='fas fa-exclamation-triangle' style='margin-right:5px;color:red'></i>`"
TEMPLATE_LOADING_LINE = ""
TEMPLATE_ERROR_LINE = ""
