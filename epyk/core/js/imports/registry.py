import logging
import json
from pathlib import Path
from urllib.request import urlopen, Request
from typing import Optional, Set, List, Tuple, Any
from epyk.conf.global_settings import IMPORT_JSDELIVER_URL, IMPORT_CDNJS_URL, IMPORTS_EXPR


_JS_IMPORTS = {
    #
    'intersection-observer': {
        "license": "W3C Software and Document License",
        "repository": "https://github.com/w3c/IntersectionObserver/tree/main/polyfill",
        "version": "0.12.0",
        "polyfill": True,
        'modules': [
            {'script': 'intersection-observer.js', 'path': 'intersection-observer@%(version)s/', "public": "jsdeliver"},
        ],
    },

    # numbers formatting
    'accounting': {
        "repository": "https://github.com/openexchangerates/accounting.js",
        "version": "0.4.1",
        "license": "MIT License",
        'register': {'alias': 'accounting', 'module': 'accounting.min', 'name': 'accounting'},
        'v_prefix': 'v',
        'modules': [
            {'script': 'accounting.min.js', "node_path": "", 'path': 'accounting.js/%(version)s/', "public": "cdnjs"},
        ],
        'website': 'https://openexchangerates.github.io/accounting.js/'},

    # QR Code
    'qrcodejs': {
        'version': '1.0.0',
        "license": "MIT License",
        'modules': [
            {'script': 'qrcode.min.js', 'path': 'qrcodejs/%(version)s/', "public": "cdnjs"},
        ],
        'repository': 'https://github.com/llyys/qrcodejs',
        'register': {'alias': 'Qrcode', 'module': 'qrcode.min', 'npm': 'qrcodejs'},
        'website': 'https://davidshimjs.github.io/qrcodejs/'},

    # data transformation
    'underscore': {
        'version': '1.13.6',
        'repository': 'https://github.com/jashkenas/underscore',
        "license": "MIT License",
        'modules': [
            {'script': 'underscore-min.js', 'path': 'underscore.js/%(version)s/', "public": "cdnjs"},
            {'script': 'underscore-min.js.map', 'path': 'underscore.js/%(version)s/', "public": "cdnjs"},
        ],
        'website': 'https://openexchangerates.github.io/accounting.js/'},

    # Plolyfill
    'promise-polyfill': {
        "license": "MIT License",
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {'script': 'polyfill.min.js', 'node_path': 'dist/', 'path': 'promise-polyfill@8/dist/',
             'cdnjs': 'https://cdn.jsdelivr.net/npm'},
        ],
        'version': '8.2.0',
        'repository': 'https://github.com/taylorhakes/promise-polyfill',
        'website': 'https://github.com/taylorhakes/promise-polyfill'},

    # Plolyfill for urlSearchParam for very old version of IE
    'url-search-params': {
        "license": "MIT License",
        "repository": "https://github.com/WebReflection/url-search-params",
        'version': '1.1.0',
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {
                'script': 'url-search-params.js', 'node_path': 'build/',
                'path': 'url-search-params/%(version)s/', "public": "cdnjs"},
        ],
        'website': 'https://github.com/taylorhakes/promise-polyfill'},

    # Common module for browser versions compatibilities
    'babel-polyfill': {
        'repository': 'https://github.com/babel/babel-polyfills',
        "license": "MIT License",
        'version': '7.4.4',
        'website': 'https://babeljs.io/',
        'register': {'alias': 'babel', 'module': 'polyfill', 'name': 'babel'},
        'modules': [
            {'script': 'polyfill.js', 'node_path': 'dist/', 'path': 'babel-polyfill/%(version)s/', "public": "cdnjs"},
        ]
    },

    # module are written from the first one to load to the last one
    'bootstrap': {
        'req': [{'alias': 'jquery'}, {'alias': '@popperjs/core'}],
        'v_prefix': 'v',
        'version': '4.6.0',
        'license': 'MIT license',
        'repository': 'https://github.com/twbs/bootstrap',
        'modules': [
            # Better to use the bundle version to avoid the import issue with popper.js
            {'script': 'bootstrap.min.js', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/',
             "public": "cdnjs"},
        ],
        'assets': [
            {'script': 'bootstrap.min.js.map', 'node_path': 'dist/js/', 'path': 'twitter-bootstrap/%(version)s/js/',
             "public": "cdnjs"},
        ],
        'website': 'https://getbootstrap.com/'},

    'moment': {
        "version": "2.29.4",
        'repository': 'https://github.com/moment/moment',
        'register': {'alias': 'moment', 'module': 'moment.min', 'npm': 'moment'},
        'license': 'MIT license',
        'modules': [
            {'script': 'moment.min.js', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', "public": "cdnjs"},
        ],
        'assets': [
            {'script': 'moment.min.js.map', 'node_path': 'min/', 'path': 'moment.js/%(version)s/', "public": "cdnjs"},
        ],
        'website': 'https://momentjs.com/',
    },

    # module for the awesome icons
    'font-awesome': {
        'version': '6.4.0',
        'unpkg': False,
        "license": "Free License",
        "pricing": "https://fontawesome.com/plans",
        "repository": "https://github.com/FortAwesome/Font-Awesome",
        'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free',
                     'npm_path': 'js'},
        'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
        'modules': [
            {'script': 'fontawesome.js', 'node_path': 'fontawesome-free/js/', 'path': 'releases/v%(version)s/js/',
             'cdnjs': 'https://use.fontawesome.com'}],
        'website': 'https://fontawesome.com/'},

    # gridstack Build interactive dashboards in minute
    'gridstack': {
        'unpkg': False,
        'version': '9.5.1',
        "license": "MIT license",
        "repository": "https://github.com/gridstack/gridstack.js",
        'website': 'https://gridstackjs.com/',
        'modules': [
            {'script': 'gridstack-all.min.js', 'path': 'gridstack.js/%(version)s/', "public": "cdnjs"}],
    },

    # jszip, Create, read and edit .zip files with Javascript http://stuartk.com/jszip
    'jszip': {
        'website': 'https://stuk.github.io/jszip/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library',
        'repository': 'https://github.com/Stuk/jszip',
        "license": "MIT license",
        'version': '3.10.1',
        'modules': [
            {'reqAlias': 'jszip', 'script': 'jszip.min.js', 'node_path': 'dist/', 'path': 'jszip/%(version)s/',
             "public": "cdnjs"},
        ]},

    # Reactive Extensions Library for JavaScript
    'rxjs': {
        'website': 'https://rxjs.dev/',
        "license": "Apache-2.0 license",
        "repository": "https://github.com/ReactiveX/rxjs",
        'version': '7.8.1',
        'modules': [
            {'reqAlias': 'jszip', 'script': 'rxjs.umd.min.js', 'node_path': 'dist/', 'path': 'rxjs/%(version)s/',
             "public": "cdnjs"},
        ]},

    #
    'json-formatter-js': {
        'website': 'https://azimi.me/json-formatter-js/',
        'version': '2.3.4',
        'repository': 'https://github.com/mohsen1/json-formatter-js',
        'register': {'alias': 'JSONFormatter', 'module': 'json-formatter.umd.min'},
        'modules': [
            {'script': 'json-formatter.umd.min.js', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"},
        ]},

    # require.js
    'requirejs': {
        'unpkg': False,
        'website': 'https://requirejs.org/',
        'version': '2.3.6',
        'repository': 'https://github.com/requirejs/r.js',
        'modules': [
            {'script': 'require.min.js', 'path': 'require.js/%(version)s/', "public": "cdnjs"}]},

    # topojson
    'topojson': {
        'website': 'https://requirejs.org/',
        'version': '3.0.2',
        'repository': 'https://github.com/requirejs/r.js',
        'register': {'alias': 'topojson', 'module': 'topojson.min'},
        'modules': [
            {'script': 'topojson.min.js', 'node_path': 'dist/', 'path': 'topojson/%(version)s/', "public": "cdnjs"}]},

    # Jquery package width CDN links
    'jquery': {
        'website': 'http://jquery.com/',
        "license": "MIT license",
        'repository': "https://github.com/jquery/jquery",
        'register': {'alias': '$', 'module': 'jquery.min', 'npm': 'jquery', 'npm_path': 'dist'},
        'version': '3.7.1',
        'modules': [
            {'script': 'jquery.min.js', 'node_path': 'dist/', 'path': 'jquery/%(version)s/', "public": "cdnjs"}
        ],
        'assets': [
            {'script': 'jquery.min.map', 'node_path': 'dist/', 'path': 'jquery/%(version)s/', "public": "cdnjs"}
        ]
    },

    # Jquery vector Maps
    'jqvmap': {
        'req': [{'alias': 'jquery'}],
        "license": "MIT license",
        'website': 'https://www.10bestdesign.com/jqvmap/',
        'repository': "https://github.com/10bestdesign/jqvmap/",
        'register': {'alias': 'jqvmap', 'module': 'jquery.vmap.min', 'npm': 'jqvmap', "init_fnc": 'jQuery = $'},
        'version': '1.5.1',
        'modules': [
            {'script': 'jquery.vmap.min.js', 'node_path': 'dist/', 'path': 'jqvmap/%(version)s/', "public": "cdnjs"},
        ],
    },

    # QUnit package width CDN links
    'qunit': {
        'website': 'https://qunitjs.com',
        "license": "MIT license",
        'version': '2.13.0',
        'modules': [
            {'script': 'qunit.js', 'node_path': 'qunit', 'path': 'qunit/%(version)s/', "public": "cdnjs"}]},

    # Used to produce sparkline charts in a document and in Tabulator
    'jquery-sparkline': {
        'req': [{'alias': 'jquery'}],
        'version': '2.1.2',
        'website': 'https://omnipotent.net/jquery.sparkline/#s-about',
        'register': {'alias': 'sparkline', 'module': 'jquery.sparkline.min', 'npm': 'jquery-sparkline', 'npm_path': ''},
        'modules': [
            {'script': 'jquery.sparkline.min.js', 'path': 'jquery-sparklines/%(version)s/', "public": "cdnjs"}
        ]
    },

    # Jquery UI package width CDN links
    'jqueryui': {
        'req': [{'alias': 'jquery'}, {'alias': '@popperjs/core'}],
        'website': 'http://jquery.com/',
        'repository': 'https://github.com/jquery/jqueryui.com',
        'version': '1.13.3',
        'register': {'alias': 'jqueryui', 'module': 'jquery-ui.min', 'npm': 'jquery-ui-dist', 'npm_path': ''},
        'modules': [
            {'script': 'jquery-ui.min.js', 'node_path': '', 'path': 'jqueryui/%(version)s/', "public": "cdnjs"}]},

    # Jquery-bracket package width CDN links
    'jquery-bracket': {
        'website': 'http://www.aropupu.fi/bracket/',
        'version': '0.11.1',
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'jquery.bracket.min.js', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/',
             "public": "cdnjs"}]},

    # Jquery timepicker width CDN links
    'timepicker': {
        'website': 'https://www.jonthornton.com/jquery-timepicker/',
        'version': '1.13.18',
        'register': {'alias': 'timepicker', 'module': 'jquery.timepicker.min'},
        'repository': 'https://github.com/jonthornton/jquery-timepicker',
        'req': [
            {'alias': 'jquery'},
            # {'alias': 'jqueryui'}
        ],
        'modules': [
            {'script': 'jquery.timepicker.min.js', 'path': 'jquery-timepicker/%(version)s/', "public": "cdnjs"}
        ]},

    # To display a context menu when right-click on an item
    'jquery-context-menu': {
        'unpkg': False,
        'website': 'http://swisnl.github.io/jQuery-contextMenu/demo.html',
        'register': {'alias': 'jQueryContext', 'module': 'jquery.contextMenu.min'},
        'req': [{'alias': 'jquery'}, {'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.contextMenu.min.js', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/',
             "public": "cdnjs"}]},

    # To customize the scrollbar width CDN links
    # https://github.com/malihu/malihu-custom-scrollbar-plugin
    # http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html
    'jquery-scrollbar': {
        'unpkg': False,
        'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
        'register': {'alias': 'jQueryScrollBar', 'module': 'jquery.mCustomScrollbar.concat.min'},
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'jquery.mCustomScrollbar.concat.min.js', 'version': '3.1.5',
             'path': 'malihu-custom-scrollbar-plugin/%(version)s/', "public": "cdnjs"}]},

    # Javascript packages for the PDF transformation width CDN links
    'pdfmake': {
        'website': '',
        'version': '0.1.70',
        'modules': [
            {'reqAlias': 'pdfmake', 'node_path': 'build/', 'script': 'pdfmake.min.js', 'path': 'pdfmake/%(version)s/',
             "public": "cdnjs"},
            {'reqAlias': 'vfs_fonts', 'node_path': 'build/', 'script': 'vfs_fonts.js', 'path': 'pdfmake/%(version)s/',
             "public": "cdnjs"}
        ],
        'assets': [
            {'node_path': 'build/', 'script': 'pdfmake.min.js.map', 'path': 'pdfmake/%(version)s/',
             "public": "cdnjs"},
        ]
    },

    # The script allows you to take "screenshots" of webpages or parts of it, directly on the users' browser.
    'html2canvas': {
        'version': '1.4.1',
        'website': 'https://html2canvas.hertzen.com/',
        'repository': 'https://github.com/niklasvh/html2canvas',
        'modules': [
            {'node_path': 'dist/', 'script': 'html2canvas.min.js', 'path': 'html2canvas/%(version)s/',
             "public": "cdnjs"},

        ]
    },

    # DOMPurify is a DOM-only, superfast, uber-tolerant XSS sanitizer for HTML, MathML and SVG.
    'dompurify': {
        'website': 'https://github.com/cure53/DOMPurify',
        'repository': 'https://github.com/cure53/DOMPurify',
        'version': '2.2.6',
        'modules': [
            {'node_path': 'dist/', 'script': 'purify.min.js', 'path': 'dompurify/%(version)s/', "public": "cdnjs"},
        ]
    },

    # Javascript packages for the PDF transformation width CDN links (Tabulator)
    'jspdf': {
        "unpkg": False,
        'req': [
            {'alias': 'dompurify'},
            {'alias': 'html2canvas'},
        ],
        'website': 'https://github.com/mrrio/jspdf',
        'repository': 'https://github.com/mrrio/jspdf',
        'version': '2.5.1',
        'modules': [
            {'reqAlias': 'jspdf', 'node_path': 'dist/', 'script': 'jspdf.umd.min.js', 'path': 'jspdf/%(version)s/',
             "public": "cdnjs"},
            {'script': 'polyfills.umd.min.js', 'path': 'jspdf/%(version)s/', "public": "cdnjs"},
        ]},

    # Clipboard features width CDN links
    'clipboard': {
        'website': 'https://clipboardjs.com/',
        "license": "MIT license",
        "repository": "https://github.com/zenorocha/clipboard.js",
        'version': '2.0.11',
        'modules': [
            {'reqAlias': 'clipboard', 'script': 'clipboard.min.js', 'node_path': 'dist/',
             'path': 'clipboard.js/%(version)s/',
             "public": "cdnjs"}]},

    'svgjs': {
        "license": "MIT License",
        'version': '2.6.2',
        "repository": "https://github.com/svgdotjs/svg.js",
        'register': {'alias': 'svg', 'module': 'svg.min', 'npm': 'svgjs',  # "init_fnc": "window.SVG = svg"
                     },
        'modules': [
            {'script': 'svg.min.js', 'node_path': 'dist/', 'path': 'svgjs@%(version)s/dist/', "public": "jsdeliver"}
        ]
    },

    # For ChartJs Zoom to get the gesture details.
    'hammer': {
        "license": "MIT license",
        "unpkg": False,
        'version': '2.0.8',
        "repository": "https://github.com/hammerjs/hammer.js",
        'website': 'http://hammerjs.github.io/',
        'modules': [
            {'script': 'hammer.min.js', 'path': 'hammer.js/%(version)s/', "public": "cdnjs"}
        ],
    },

    # Cannot add properly the dependency in this one as my algorithm does not work for shared dependencies ....
    # 'meter': {'req': ['d3'], 'modules': ['d3.meter.js'], 'website': '', 'version': '', "status": 'deprecated'},

    # Popper tooltips used by bootstrap in the dropdown components
    '@popperjs/core': {
        "license": "MIT license",
        'req': [{'alias': 'jquery'}],
        'v_prefix': 'v',
        'version': '2.11.8',
        'repository': 'https://github.com/popperjs/popper-core',
        'website': 'https://github.com/popperjs/popper-core',
        'modules': [
            {'reqAlias': 'popper', 'script': 'popper.min.js', 'node_path': 'dist/umd/',
             'path': 'popper.js/%(version)s/umd/',
             "public": "cdnjs"}
        ],
        'assets': [
            {'script': 'popper.min.js.map', 'node_path': 'dist/umd/', 'path': 'popper.js/%(version)s/umd/',
             "public": "cdnjs"}
        ]
    },

    # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
    'bootstrap-select': {
        "license": "MIT license",
        'website': 'http://silviomoreto.github.io/bootstrap-select/',
        'version': '1.13.18',
        'repository': 'https://github.com/snapappointments/bootstrap-select',
        'register': {'alias': 'selectBs', 'module': 'bootstrap-select.min', 'npm_path': 'dist/js'},
        'req': [
            {'alias': '@popperjs/core', 'version': '1.14.6'},  # Cannot be upgraded bug with bootstrap select
            {'alias': 'jquery'},
            {'alias': 'bootstrap'}],
        'modules': [
            {'reqAlias': 'selectBs', 'script': 'bootstrap-select.min.js', 'node_path': 'dist/js/',
             'path': 'bootstrap-select/%(version)s/js/', "public": "cdnjs"},
        ],
        'assets': [
            {'script': 'bootstrap-select.min.js.map', 'node_path': 'dist/js/',
             'path': 'bootstrap-select/%(version)s/js/',
             "public": "cdnjs"},
        ]
    },

    'ajax-bootstrap-select': {
        "license": "MIT license",
        'version': '1.4.5',
        'website': 'https://github.com/truckingsim/Ajax-Bootstrap-Select',
        'register': {'alias': 'selectAjax', 'module': 'ajax-bootstrap-select.min', 'npm_path': 'dist/js'},
        'req': [{"alias": 'bootstrap-select'}
                ],
        'modules': [
            {'script': 'ajax-bootstrap-select.min.js', 'node_path': 'dist/js/',
             'path': 'ajax-bootstrap-select/%(version)s/js/', "public": "cdnjs"}
        ]
    },

    # https://cdnjs.cloudflare.com/ajax/libs/ajax-bootstrap-select/1.4.5/js/ajax-bootstrap-select.min.js
    # javascript package for the Venn chart
    # 'venn': {'req': ['d3'], 'modules': ['venn.js'], 'website': '', 'version': '',},

    # Socket IO
    'socket.io': {
        'version': '3.0.4',
        "license": "MIT license",
        'website': 'https://github.com/socketio/socket.io',
        'repository': 'https://github.com/socketio/socket.io',
        'req': [{'alias': 'jquery'}],
        'modules': [
            {'script': 'socket.io.min.js', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/',
             "public": "cdnjs"}
        ],
        'assets': [
            {'script': 'socket.io.min.js.map', 'node_path': 'client-dist/', 'path': 'socket.io/%(version)s/',
             "public": "cdnjs"}
        ]
    },

    # highlight
    'highlight.js': {
        "license": "BSD-3-Clause license",
        'version': '11.9.0',
        'website': 'https://highlightjs.org/',
        'repository': 'https://github.com/highlightjs/highlight.js',
        # 'register': {'alias': 'hljs', 'npm': 'highlight.js', 'npm_path': 'lib/core'},
        'modules': [
            {'script': 'highlight.min.js', 'node_path': 'lib/', 'path': 'highlight.js/%(version)s/',
             "public": "cdnjs"}
        ]},

    # showdown
    'showdown': {
        'version': '2.1.0',
        "license": "MIT license",
        'website': 'https://github.com/showdownjs/showdown',
        'repository': 'https://github.com/showdownjs/showdown',
        'register': {'alias': 'showdown', 'module': 'showdown.min', 'npm': 'showdown', 'npm_path': 'dist'},
        'modules': [
            {'script': 'showdown.min.js', 'node_path': 'dist/', 'path': 'showdown/%(version)s/', "public": "cdnjs"}
        ]
    },

    # Sortable framework
    'sortablejs': {
        'register': {'alias': 'Sortable', 'npm': 'sortablejs'},
        "license": "MIT license",
        'repository': 'https://github.com/SortableJS/Sortable',
        'version': '1.15.1',
        'modules': [
            {'script': 'Sortable.min.js', 'path': 'Sortable/%(version)s/', "public": "cdnjs"},
        ],
        'website': 'https://github.com/SortableJS/Sortable'},

    'google-platform': {
        "unpkg": False,
        'website': 'https://apis.google.com/',
        'req': [],
        'modules': [
            {'script': 'platform.js', 'version': '', 'path': 'js/', 'cdnjs': 'https://apis.google.com'}]},

    'facebook-sdk': {
        "unpkg": False,
        'website': 'https://connect.facebook.net',
        'req': [],
        'version': '0.3.3',
        'modules': [
            {'script': 'sdk.js', 'path': 'en-GB/', 'cdnjs': 'https://connect.facebook.net'}]},

    # Date picker - tiny size, no dependencies
    '@easepick/bundle': {
        "unpkg": False,
        'version': "1.2.1",
        'modules': [
            {'script': 'index.umd.min.js', 'node_path': 'dist/',
             'path': '@easepick/bundle@%(version)s/dist/', "public": "jsdeliver"},
        ],
        'website': 'https://easepick.com/'
    },

    # A lightweight and elegant JavaScript color picker. Written in vanilla ES6, no dependencies. Accessible.
    '@melloware/coloris': {
        "unpkg": False,
        'version': "0.24.0",
        'modules': [
            {'script': 'coloris.min.js',
             'path': '@melloware/coloris@%(version)s/dist/umd/', "public": "jsdeliver"},
        ],
        'website': 'https://coloris.js.org/'
    },

    # JavaScript mangler and compressor toolkit
    'terser': {
        "unpkg": False,
        'version': "5.34.1",
        'modules': [
            {'script': 'bundle.min.js', "node_path": "dist/", 'path': 'terser@%(version)s/dist/',
             "public": "jsdeliver"},
        ],
        'website': 'https://terser.org/'
    },

    # Static analysis tool for JavaScript
    'jshint': {
        "unpkg": False,
        'version': "2.13.6",
        'modules': [
            {'script': 'jshint.min.js', "node_path": "dist/", 'path': 'jshint/%(version)s/'},
        ],
        'website': 'https://jshint.com/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library'
    }

}
""" """

_CSS_IMPORTS = {
    'jqueryui': {
        'modules': [
            {'script': 'jquery-ui.min.css', 'node_path': '', 'path': 'jqueryui/%(version)s/themes/base/',
             "public": "cdnjs"},
        ]
    },

    # fluent ui icons
    'office-ui-fabric-core': {
        "license": "MIT License",
        "repository": "https://github.com/OfficeDev/office-ui-fabric-core",
        'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
        'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/',
                     'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
        'website': 'https://developer.microsoft.com/en-us/fluentui#/styles/web/icons'},

    # fluent ui icons
    'office-ui-fabric-react': {
        "license": "MIT License",
        'register': {'alias': 'fluentui', 'module': 'fluentui', 'npm_path': 'dist/css'},
        'modules': [{'script': 'fabric.min.css', 'version': '11.0.0', 'path': 'office-ui-fabric-core/%(version)s/css/',
                     'cdnjs': "https://static2.sharepointonline.com/files/fabric"}],
        'website': 'https://developer.microsoft.com/en-us/fluentui#/styles/web/icons'},

    # QUnit package width CDN links
    'qunit': {
        'modules': [
            {'script': 'qunit.css', 'node_path': 'qunit', 'path': 'qunit/%(version)s/', "public": "cdnjs"}]},

    # jqvmap
    'jqvmap': {
        'modules': [
            {'script': 'jqvmap.min.css', 'node_path': 'dist', 'path': 'jqvmap/%(version)s/', "public": "cdnjs"}]},

    # Jquery-bracket package width CDN links
    'jquery-bracket': {
        'modules': [
            {'script': 'jquery.bracket.min.css', 'node_path': 'dist/', 'path': 'jquery-bracket/%(version)s/',
             "public": "cdnjs"}]},

    # To display a context menu when right-click on an item width CDN links
    # http://swisnl.github.io/jQuery-contextMenu/demo.html#jquery-context-menu-demo-gallery
    'jquery-context-menu': {
        'website': 'https://github.com/swisnl/jQuery-contextMenu/blob/master/dist/jquery.contextMenu.min.css.map',
        'req': [{'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.contextMenu.min.css', 'version': '2.6.4', 'path': 'jquery-contextmenu/%(version)s/',
             "public": "cdnjs"}]},

    # Jquery timepicker width CDN links
    'timepicker': {
        'modules': [
            {'script': 'jquery.timepicker.min.css', 'path': 'jquery-timepicker/%(version)s/', "public": "cdnjs"}]},

    # To customize the scrollbar width CDN links
    'jquery-scrollbar': {
        'website': 'http://manos.malihu.gr/jquery-custom-content-scroller/',
        'req': [{'alias': 'jqueryui'}],
        'modules': [
            {'script': 'jquery.mCustomScrollbar.min.css', 'version': '3.1.5',
             'path': 'malihu-custom-scrollbar-plugin/%(version)s/', "public": "cdnjs"}]},

    # Bootstrap style width CDN links
    'bootstrap': {
        'modules': [
            {'script': 'bootstrap.min.css', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/',
             "public": "cdnjs"}
        ],
        'assets': [
            {'script': 'bootstrap.min.css.map', 'node_path': 'dist/css/', 'path': 'twitter-bootstrap/%(version)s/css/',
             "public": "cdnjs"}
        ]
    },

    # Font awesome style width CDN links
    'font-awesome': {
        'register': {'alias': 'fontawesome', 'module': 'fontawesome', 'npm': '@fortawesome/fontawesome-free',
                     'npm_path': 'css'},
        'website': 'https://fontawesome.com/',
        'package': {'zip': 'https://use.fontawesome.com/releases/v%(version)s/fontawesome-free-%(version)s-web.zip',
                    'root': 'fontawesome-free-%(version)s-web', 'folder': 'releases', 'path': 'v%(version)s'},
        'modules': [
            {'script': 'all.css', 'version': '5.13.1', 'node_path': 'fontawesome-free/css/',
             'path': 'releases/v%(version)s/css/',
             'cdnjs': 'https://use.fontawesome.com'}],
        'assets': [
            {'script': 'fa-brands-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
            {'script': 'fa-regular-400.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
            {'script': 'fa-solid-900.woff2', 'version': '5.13.1', 'path': 'releases/v%(version)s/webfonts/',
             'cdnjs': 'https://use.fontawesome.com', 'npm_path': 'webfonts'},
        ]
    },

    # bootstrap icons
    'bootstrap-icons': {
        "license": "MIT license",
        "repository": "https://github.com/twbs/icons",
        'website': 'https://icons.getbootstrap.com/',
        'version': '1.10.3',
        'modules': [
            {'script': 'bootstrap-icons.min.css', 'path': 'bootstrap-icons/%(version)s/font/', "public": "cdnjs"}]},

    # Javascript module for the simple select component. issue with Bootstrap 4 width CDN links
    'bootstrap-select': {
        'modules': [
            {'script': 'bootstrap-select.min.css', 'node_path': 'dist/css/',
             'path': 'bootstrap-select/%(version)s/css/',
             "public": "cdnjs"}
        ],
        'assets': [
            {'script': 'bootstrap-select.css.map', 'node_path': 'dist/css/',
             'path': 'bootstrap-select/%(version)s/css/',
             "public": "cdnjs"}
        ]

    },

    'ajax-bootstrap-select': {
        'modules': [
            {'script': 'ajax-bootstrap-select.min.css', 'node_path': 'dist/css/', 'version': '1.4.5',
             'path': 'ajax-bootstrap-select/%(version)s/css/', "public": "cdnjs"}
        ]
    },

    # highlight
    'highlight.js': {
        'modules': [
            {'script': 'default.min.css', 'node_path': 'styles/', 'path': 'highlight.js/%(version)s/styles/',
             "public": "cdnjs"}
        ]},

    'json-formatter-js': {
        'modules': [
            {'script': 'json-formatter.css', 'node_path': 'dist/', 'path': 'json-formatter-js@%(version)s/dist/',
             'cdnjs': "https://cdn.jsdelivr.net/npm"},
        ]},

    # gridstack Build interactive dashboards in minute
    'gridstack': {
        'modules': [
            {'script': 'gridstack.min.css', 'node_path': 'dist/', 'path': 'gridstack.js/%(version)s/',
             "public": "cdnjs"},
        ],
    },

    # A lightweight and elegant JavaScript color picker. Written in vanilla ES6, no dependencies. Accessible.
    '@melloware/coloris': {
        'modules': [
            {'script': 'coloris.min.css', 'node_path': 'dist/',
             'path': '@melloware/coloris@%(version)s/dist/',
             "public": "jsdeliver"},
        ],
    }
}
""" """

_SERVICES = {}
""" """

GOOGLE_EXTENSIONS = {
    'charts': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['corechart']})}",
    },
    'geochart': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['geochart']})}",
    },
    'tables': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['table']})}",

    },
    'gauge': {'modules': [
        {'script': 'loader.js', 'version': '', 'path': '/', 'cdnjs': 'https://www.gstatic.com/charts'},
    ],
        'website': 'https://developers.google.com/chart/interactive/docs',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['gauge']})}",

    },
    'maps': {'modules': [
        {'script': 'js?v=3.exp', 'version': '', 'path': 'api/', 'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart'
    },
    'streetview': {'modules': [
        {'script': 'js?v=3.exp', 'version': '', 'path': 'api/', 'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart'
    },
    'visualization': {'modules': [
        {'script': 'js?key=%(api_key)s&libraries=visualization', 'version': '', 'path': 'api/',
         'cdnjs': 'https://maps.googleapis.com/maps'},
    ],
        'website': 'https://developers.google.com/chart',
        'launcher': "if(typeof google !== 'undefined'){google.charts.load('current', {'packages':['corechart']})}",
    },
    'captcha': {'modules': [
        {'script': 'api.js?render=%(site_key)s', 'version': '', 'path': '',
         'cdnjs': 'https://www.google.com/recaptcha'},
    ],
    }
}
""" """

PACKAGE_STATUS = {}
""" Module variable to be updated in environment to share info related to packages. """

NOTEBOOK_MAPPING = {
    'MathJax': 'mathjax',
    'jquery-ui': 'jqueryui',
}
""" """


def get_repo_path(module: dict, repo_path: Optional[str] = None) -> str:
    if repo_path is None:
        if module.get("public") == "cdnjs":
            return IMPORT_CDNJS_URL

        if module.get("public") == "jsdeliver":
            return IMPORT_JSDELIVER_URL

    return repo_path


def get_js(repo_path: Optional[str] = None) -> dict:
    """Get all JavaScript configurations defined in the Import.
    This function will format the raw configuration to a standard one.

    :param repo_path: Optional. The repo path. Default will use the defined public repository
    """
    results = {}
    for name, config in _JS_IMPORTS.items():
        results[name] = dict(config)
        if "from" in results[name]:
            results[name]["version"] = results[results[name]["from"]]['version']
            if "req" not in results[name]:
                results[name]['req'] = []
            results[name]['req'].append({'alias': results[name]["from"]})
        for module in results[name]["modules"]:
            if 'version' not in module and "version" in results[name]:
                module['version'] = results[name]['version']
            if repo_path is None:
                if module.get("public") == "cdnjs":
                    module["cdnjs"] = IMPORT_CDNJS_URL
                elif module.get("public") == "jsdeliver":
                    module["cdnjs"] = IMPORT_JSDELIVER_URL
            else:
                module["cdnjs"] = repo_path
    return results


def get_css(repo_path: Optional[str] = None) -> dict:
    """Get all CSS configurations defined in the Import.
    This function will format the raw configuration to a standard one.

    :param repo_path: Optional. The repo path. Default will use the defined public repository
    """
    results = {}
    for name, config in _CSS_IMPORTS.items():
        results[name] = dict(config)
        if "version" not in results[name]:
            if "version" in _JS_IMPORTS.get(name, {}):
                results[name]["version"] = _JS_IMPORTS[name]["version"]
            elif "from" in _JS_IMPORTS.get(name, {}):
                results[name]["version"] = _JS_IMPORTS[_JS_IMPORTS[name]["from"]]["version"]
        for module in results[name]["modules"]:
            if 'version' not in module and "version" in results[name]:
                module['version'] = results[name]['version']
            if repo_path is None:
                if module.get("public") == "cdnjs":
                    module["cdnjs"] = IMPORT_CDNJS_URL
                elif module.get("public") == "jsdeliver":
                    module["cdnjs"] = IMPORT_JSDELIVER_URL
            else:
                module["cdnjs"] = repo_path
    return results


def extend(packages: dict) -> Set[str]:
    """Extend configurations with extra packages.
    This could also change existing configurations.

    :return: Packages added to the configuration
    """
    global _CSS_IMPORTS, _JS_IMPORTS, _SERVICES
    mandatory_fields = ("modules", )
    results = set()
    for name, config in packages.items():
        for field in mandatory_fields:
            if field not in config:
                raise Exception("Missing field %s in import extension" % field)

        css_modules, js_modules = [], []
        for module in config.get("modules", []):
            if module["script"].endswith(".css"):
                css_modules.append(module)
            else:
                js_modules.append(module)

        if 'services' in config:
            for service in config['services']:
                service['pmts'] = ";".join(["%s=%s" % (k, v) for k, v in service['values'].items()])
                if service['type'] not in _SERVICES:
                    _SERVICES[name] = {}
                _SERVICES[name].setdefault(service['type'], []).append("%(url)s?%(pmts)s" % service)

        if css_modules:
            _CSS_IMPORTS[name] = dict(config)
            _CSS_IMPORTS[name]["modules"] = css_modules
        if js_modules:
            _JS_IMPORTS[name] = dict(config)
            _JS_IMPORTS[name]["modules"] = js_modules
    return results


def add(
        reference: str,
        module_path: List[Tuple[str, str]],
        version: Optional[str] = None,
        cdnjs_url: Optional[str] = None,
        required: Optional[list] = None,
        services: List[dict] = None
):
    """Function to extend the internal CSS and JS registered modules.

    :param reference: The internal reference in the framework
    :param module_path: The different modules and location from cdnjs root
    :param version: The version number. Can be an internal module reference to point to follow its version number
    :param cdnjs_url: The CDNJS reference path
    :param required: Optional. The list of dependency modules
    :param services: Optional.
    """
    global _CSS_IMPORTS, _JS_IMPORTS, _SERVICES
    for module, path in module_path:
        config = _JS_IMPORTS if module.endswith(".js") else _CSS_IMPORTS
        if reference not in config:
            config[reference] = {"modules": []}
            if required is not None:
                reqs = [{'alias': req} for req in required if req in config]
                if reqs:
                    config[reference]['req'] = reqs
        if version in config:
            version = config[version].get('version') or config[version]['modules'][0]['version']
        if cdnjs_url is None:
            config[reference]["modules"].append(
                {'script': module, 'version': version, 'path': path, 'public': "cdnjs"})
        else:
            config[reference]["modules"].append(
                {'script': module, 'version': version, 'path': path, 'cdnjs': cdnjs_url})
    if services:
        for service in services:
            service['pmts'] = ";".join(["%s=%s" % (k, v) for k, v in service['values'].items()])
            if service['type'] not in _SERVICES:
                _SERVICES[reference] = {}
            _SERVICES[reference].setdefault(service['type'], []).append("%(url)s?%(pmts)s" % service)


def remove(names: List[str]) -> Set[str]:
    """Remove some packages from the registry mapping.

    :param names: List of package names to be removed
    :return: Packages removed from the configuration
    """
    global _JS_IMPORTS, _CSS_IMPORTS
    packages = set()
    for name in names:
        if name in _JS_IMPORTS:
            packages.add(name)
            del _JS_IMPORTS[name]
        if name in _CSS_IMPORTS:
            packages.add(name)
            del _CSS_IMPORTS[name]
    return packages


def update(package: str, config: dict, remove_if_empty: bool = False) -> Tuple:
    """This will update a module in the internal mapping.
    This will not merge the new configuration with the existing one for modules in the internal mapping but replace it.

    :param package: Package alias to lookup in the internal mapping
    :param config: Package configuration
    :param remove_if_empty: Flag to remove from configuration is not file supplied
    """
    global _JS_IMPORTS, _CSS_IMPORTS

    js_files, css_files = [], []
    for module in config.get("modules", []):
        if module.get("script", "").endswith(".js"):
            js_files.append(module)
        elif module.get("script", "").endswith(".css"):
            css_files.append(module)
        else:
            logging.warning("File format not recognised - %s" % module.get("script", ""))
    for repo, modules in [(_JS_IMPORTS, js_files), (_CSS_IMPORTS, css_files)]:
        type_config = dict(repo.get(package, {}))
        type_config.update(config)
        type_config["modules"] = modules
        if package in _JS_IMPORTS and not type_config["modules"]:
            if remove_if_empty:
                del repo[package]

            continue

        repo[package] = type_config
    return _JS_IMPORTS.get(package), _CSS_IMPORTS.get(package)


def set_attr(package: str, attr: str, value: Any) -> bool:
    """

    :param package:
    :param attr:
    :param value:
    """

    global _JS_IMPORTS, _CSS_IMPORTS
    is_updated = False
    if attr == "modules":
        raise Exception("")

    if package in _JS_IMPORTS:
        _JS_IMPORTS[package][attr] = value
        if attr == "version":
            for module in _JS_IMPORTS[package].get("modules", []):
                module["version"] = value
        is_updated = True
    if package in _CSS_IMPORTS:
        _CSS_IMPORTS[package][attr] = value
        if attr == "version":
            for module in _CSS_IMPORTS[package].get("modules", []):
                module["version"] = value
        is_updated = True
    return is_updated


def reduce(packages: Set[str]) -> Set[str]:
    """Reduce list of external packages in the internal mapping.

    :param packages: List of packages to exclude
    """
    global _JS_IMPORTS, _CSS_IMPORTS
    removed_packages = set()
    for k in list(_JS_IMPORTS):
        if k not in packages:
            removed_packages.add(k)
            del _JS_IMPORTS[k]

    for k in list(_CSS_IMPORTS):
        if k not in packages:
            removed_packages.add(k)
            del _CSS_IMPORTS[k]

    return removed_packages


def clear():
    """Clear the entire registry mapping for JavaScript and CSS"""
    global _JS_IMPORTS, _CSS_IMPORTS
    _JS_IMPORTS = {}
    _CSS_IMPORTS = {}


def save_resources(out_path: str, aliases: List[str] = None, headers: dict = None, repo_path: Optional[str] = None):
    """Copy the external resources to an specific directory.

    :param out_path:
    :param aliases:
    :param headers:
    :param repo_path: Optional. The repo path. Default will use the defined public repository
    """
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    all_js = get_js(repo_path)
    all_css = get_css(repo_path)
    if aliases is None:
        aliases = set(all_js.keys()).union(set(all_css.keys()))
    for alias in aliases:
        for pkg_gro in [all_css, all_js]:
            if alias in pkg_gro:
                pkg_def = pkg_gro[alias]
                for f in pkg_def.get("modules", []):
                    f_path = IMPORTS_EXPR % f
                    if "version" in f:
                        r_path = f_path % f
                    elif "version" not in pkg_def and "version" in all_js.get(alias, {}):
                        r_path = f_path % all_js[alias]
                    else:
                        if "version" not in pkg_def:
                            continue

                        r_path = f_path % pkg_def
                    request = Request(r_path, None, headers)
                    try:
                        with urlopen(request) as response:
                            with open(r"%s\%s" % (out_path, f["script"]), "wb") as fp:
                                fp.write(response.read())
                    except Exception:
                        logging.warning("Error with %s: %s" % (alias, r_path))


def from_json(file_path: Optional[Path] = None):
    """

    :param file_path:
    """
    with open(file_path) as fp:
        extend(json.load(fp))