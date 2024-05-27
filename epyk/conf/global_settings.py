import os

# Set the debug / verbose flag for the entire framework (if not specified)
DEBUG = False

# Override path for native internal Js and CSS resources
NATIVE_JS_PATH = os.environ.get("NATIVE_JS_PATH")
NATIVE_CSS_PATH = os.environ.get("NATIVE_CSS_PATH")

# Theme path will be used by colors and icons function to set default values.
THEME_SASS_PATH = os.environ.get("THEME_SASS_PATH")

# Common path with a local copy for the external packages
PACKAGES_PATH = os.environ.get("PACKAGES_PATH")

# Used by standalone external component to load.
COMPONENTS_EXTENSION_PATH = os.environ.get("COMPONENTS_EXTENSION_PATH")


# Used to replace internet retrieval for external resources.
# This will rely on the full path definition to access the scripts.
NPM_NODE_MODULES_PATH = os.environ.get("NPM_NODE_MODULES_PATH")
