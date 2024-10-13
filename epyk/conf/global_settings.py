import os
from pathlib import Path
from typing import List


DEBUG = False
""" Set the debug / verbose flag for the entire framework (if not specified) """
NATIVE_JS_PATH = os.environ.get("NATIVE_JS_PATH")
""" Override path for native internal Js and CSS resources """
NATIVE_CSS_PATH = os.environ.get("NATIVE_CSS_PATH")
""" Native CSS is used to override the style_urls defined for certain components """
PRIMARY_RESOURCE_PATHS = []
""" Multiple native path used for both CSS and JSS resources. Default NATIVE_ will be used as fallbacks """
THEME_SASS_PATH = os.environ.get("THEME_SASS_PATH")
"""Theme path will be used by colors and icons function to set default values.
This can be used to override paths for:
   - the css_map_files defined to the body
   - the SASS file for the color themes
   - the SASS file used to define the icon references
"""

PACKAGES_PATH = os.environ.get("PACKAGES_PATH")
""" Common path with a local copy for the external packages """

COMPONENTS_EXTENSION_PATH = os.environ.get("COMPONENTS_EXTENSION_PATH")
""" Used by standalone external component to load """

NPM_NODE_MODULES_PATH = os.environ.get("NPM_NODE_MODULES_PATH")
"""Used to replace internet retrieval for external resources.
This will rely on the full path definition to access the scripts.
"""

# Assets output settings
ASSETS_SPLIT = os.environ.get("ASSETS_SPLIT", 'N') == 'Y'
""" Flag to generate resources to dedicated files """
ASSETS_SPLIT_MINIFY = os.environ.get("ASSETS_SPLIT_MINIFY", 'Y') == 'Y'
""" Minify the various resources """
ASSETS_PRINT_PATHS = {"Y": True, "N": False}.get(
    os.environ.get("HTML_PRINT_PATH", None), os.environ.get("HTML_PRINT_PATH", None))
""" Print the full path for the various generated resources """
ASSETS_OUT_PATH = os.environ.get("HTML_OUT_PATH", os.path.join(os.getcwd(), "outs"))
""" Target output path in which all web assets will be generated """
ASSETS_STATIC_PATH = os.environ.get("ASSETS_STATIC_PATH", ASSETS_OUT_PATH)
""" Target output path for the HTML report resources """
ASSETS_STATIC_ROUTE = os.environ.get("ASSETS_STATIC_ROUTE", ".")
""" Url root on the server to access the attached resources """
ASSETS_STATIC_CONFIG = os.environ.get("ASSETS_STATIC_CONFIG", "configs")
""" Folder and url end route for configuration files """
ASSETS_STATIC_DATA = os.environ.get("ASSETS_STATIC_DATA", "data")
""" Folder and url end route for data files """
ASSETS_STATIC_CSS = os.environ.get("ASSETS_STATIC_CSS", "css")
""" Folder and url end route for CSS files """
ASSETS_STATIC_JS = os.environ.get("ASSETS_STATIC_JS", "js")
""" Folder and url end route for JavaScript files """
ASSETS_STATIC_PUBLIC = os.environ.get("ASSETS_STATIC_PUBLIC", "public")
""" Folder and url end route for other resources (images, icons...) """

# Icons global settings
ICONS_FAMILY = os.environ.get("ICONS_FAMILY", 'font-awesome')
""" Default family reference """

IMPORTS_EXPR = "%(cdnjs)s/%(path)s%(script)s"
""" Common path to build the external files url in the HTML header - Default case %(cdnjs)s/%(path)s%(script)s """


def add_static_sub_folders(names: List[str]):
    """Add sub folder to the static path.
    Using this method will update both ASSETS_STATIC_PATH and ASSETS_STATIC_ROUTE.
    ASSETS_STATIC_PATH is updated with the sub folders
    ASSETS_STATIC_ROUTE is extended with the extra folders in the url

    :param names: Sub folder and extra routes for the url
    """
    global ASSETS_STATIC_PATH, ASSETS_STATIC_ROUTE, ASSETS_SPLIT

    ASSETS_SPLIT = True
    ASSETS_STATIC_PATH = os.path.join(ASSETS_STATIC_PATH, *names)
    ASSETS_STATIC_ROUTE = "%s/%s" % (ASSETS_STATIC_ROUTE, "/".join(names))


def get_static_files(filenames: List[str], full_path: str = None) -> List[Path]:
    """Get the static files based on the configuration.
    This will try to get the files from the most appropriate folder in the following order:

     PRIMARY_RESOURCE_PATHS > NATIVE_XXX_PATH > Internal Module path

    :param filenames: List of file names
    :param full_path: Optional. Static path to use
    """
    if full_path is not None:
        return [Path(full_path) / f for f in filenames]

    results = []
    if PRIMARY_RESOURCE_PATHS:
        for f in filenames:
            for p in PRIMARY_RESOURCE_PATHS:
                file_path = Path(p) / f
                if file_path.exists():
                    results.append(file_path)
                    break

            else:
                file_ext = f.split(".")[-1].lower()
                native_path = NATIVE_CSS_PATH if file_ext == "css" else NATIVE_JS_PATH
                if native_path:
                    file_path = Path(p) / f
                    if file_path.exists():
                        results.append(file_path)
                else:
                    file_path = Path(__file__).parent.parent / "core" / file_ext / "native" / f
                    if file_path.exists():
                        results.append(file_path)
    else:
        for f in filenames:
            file_ext = f.split(".")[-1].lower()
            file_path = Path(__file__).parent.parent / "core" / file_ext / "native" / f
            if file_path.exists():
                results.append(file_path)
    return results
