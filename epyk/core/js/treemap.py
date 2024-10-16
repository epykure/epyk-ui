import logging

from pathlib import Path
from typing import List

from epyk.conf import global_settings

# Returns the js location base on current file path
PACKAGE_PATH = Path(__file__).parent

# Required extra functions for build-in components' builders
_BUILDERS_MAP = {
    "alert": ["setCss", "getHtmlData"],
    "audio": ["setCss"],
    "badge": ["setCss"],
    "blockQuote": ["setCss", "getHtmlData"],
    "button": ["getDataFromTemplate", "setCss"],
    "buttonData": ["setCss"],
    "chat": ["setCss", "getHtmlData"],
    "codeEditor": ["setCss"],
    "colorsPicker": ["setCss"],
    "contextMenu": ["setCss"],
    "countDownDate": ["setCss"],
    "datalink": ["getDataFromTemplate", "setCss"],
    "datePicker": ["setCss"],
    "datesRange": ["setCss"],
    "elapsed": ["getDataFromTemplate", "setCss"],
    "emoji": ["setCss"],
    "externallink": ["getDataFromTemplate", "setCss"],
    "fieldset": ["getDataFromTemplate", "setCss"],
    "genericTag": ["getDataFromTemplate", "setCss"],
    "help": ["setCss"],
    "highlights": ["getDataFromTemplate", "getHtmlData"],
    "htmlIcon": ["setCss"],
    "input": ["setCss"],
    "inputCheckbox": ["setCss"],
    "label": ["getDataFromTemplate", "setCss"],
    "lastUpdate": ["setCss"],
    "listBrackets": ["setCss"],
    "listStandard": ["setCss"],
    "markdownReader": ["setCss", "getHtmlData"],
    "media": ["setCss"],
    "numeric": ["getDataFromTemplate", "setCss"],
    "paragraph": ["getDataFromTemplate", "setCss"],
    "pre": ["setCss"],
    "qRCode": ["setCss"],
    "radio": ["setCss"],
    "textArea": ["setCss"],

    # Echarts
    "ekECharts": ["getChartContext"],
    "ekMapECharts": ["getChartContext"],
    "ekPieECharts": ["getChartContext"],
    "ekRadarECharts": ["getChartContext"],
    "ekScatterECharts": ["getChartContext"],
    "ekTreeECharts": ["getChartContext"],
}

# Internal definition with the resources mapping
_FUNCTIONS_MAP = {
    "createStyleElement": {
        "folder": "utils",
        "file": "StyleCreateElement.js"
    },
    "setCss": {
        "folder": "utils",
        "file": "StyleCss.js"
    },
    "getChartContext": {
        "folder": "utils",
        "file": "ContextCharts.js"
    },
    "getDataFromTemplate": {
        "folder": "utils",
        "file": "TemplateData.js"
    },
    "getHtmlData": {
        "folder": "utils",
        "file": "MarkdownData.js",
        "packages": ["showdown"],
    },
    "buildContextMenu": {
        "folder": "utils",
        "file": "ContextMenu.js",
        "css": {
            "file_name": "html-menu-context.css",
        }
    }
}


_ITEMS_MAP = {
    "badge": {
        "folder": "items",
        "file": "ItemBadge.js",
        "css": {
            "file": "html-items-badge.css",
            "folder": "items",
        }
    },
    "box": {
        "folder": "items",
        "file": "ItemBox.js",
        "css": {
            "file": "html-items-box.css",
            "folder": "items",
        }
    },
    "button": {
        "folder": "items",
        "file": "ItemButton.js",
        "css": {
            "file": "html-items-button.css",
            "folder": "items",
        }
    },
    "check": {
        "folder": "items",
        "file": "ItemCheck.js",
        "css": {
            "file": "html-items-check.css",
            "folder": "items",
        }
    },
    "icon": {
        "folder": "items",
        "file": "ItemIcon.js",
        "css": {
            "file": "html-items-icon.css",
            "folder": "items",
        }
    },
    "link": {
        "folder": "items",
        "file": "ItemLink.js",
        "css": {
            "file": "html-items-link.css",
            "folder": "items",
        }
    },
    "logs": {
        "folder": "items",
        "file": "ItemLogs.js",
        "css": {
            "file": "html-items-logs.css",
            "folder": "items",
        }
    },
    "period": {
        "folder": "items",
        "file": "ItemPeriod.js",
        "css": {
            "file": "html-items-period.css",
            "folder": "items",
        }
    },
    "radio": {
        "folder": "items",
        "file": "ItemRadio.js",
        "css": {
            "file": "html-items-radio.css",
            "folder": "items",
        }
    },
    "status": {
        "folder": "items",
        "file": "ItemStatus.js",
        "css": {
            "file": "html-items-status.css",
            "folder": "items",
        }
    },
    "text": {
        "folder": "items",
        "file": "ItemText.js"
    },
    "timeline": {
        "folder": "items",
        "file": "ItemTimeline.js",
        "css": {
            "file": "html-items-timeline.css",
            "folder": "items",
        }
    },
    "tweet": {
        "folder": "items",
        "file": "ItemTweet.js",
        "css": {
            "file": "html-items-tweet.css",
            "folder": "items",
        }
    },

}


def add(func: str, full_path: str = None, override: bool = False) -> bool:
    """Add resource to the global definition.
    Those JavaScript will be ordered and added to a external JavaScript resource.

    :param func: JavaScript file with the extension (or the mapping)
    :param full_path: Optional. The file full path
    :param override: Optional. Flag to override if already exists)
    """
    global _FUNCTIONS_MAP

    is_added = False
    f_path = Path(full_path)
    if f_path.exists():
        if func in _FUNCTIONS_MAP:
            if override:
                _FUNCTIONS_MAP[func] = {"path": f_path.parent, "file": f_path.name}
                is_added = True
        else:
            _FUNCTIONS_MAP[func] = {"path": f_path.parent, "file": f_path.name}
            is_added = True
    return is_added


def get(required_funcs: List[str], raise_error: bool = True) -> List[Path]:
    """Get list of files to add first.

    :param required_funcs: List of required functions
    :param raise_error: Optional. Flag to raise an exception if function not defined
    """
    results = []
    for func in required_funcs:
        if func in _FUNCTIONS_MAP:
            script_path = _FUNCTIONS_MAP[func]["path"] / _FUNCTIONS_MAP[func]["file"]
            if script_path.exists():
                results.append(script_path)
        elif raise_error:
            raise Exception("JS | MAP_FUNCTION | %s Missing from treemap definition" % func)

        else:
            logging.warning("JS | MAP_FUNCTION | %s Missing from treemap definition" % func)
    return results
