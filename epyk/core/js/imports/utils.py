import importlib
import logging
import json
import sys
import base64
from typing import Optional
from pathlib import Path

from .registry import get_js, get_css
from ....conf.global_settings import (IMPORT_PROXY, IMPORT_PCK_REPO, IMPORT_AUTOLOAD, IMPORT_USE_NPM_UNPK,
                                      PACKAGES_PATH, IMPORTS_EXPR, IMPORT_JSDELIVER_URL, IMPORT_CDNJS_URL,
                                      IMPORT_UNPKG_URL)


def requires(name: str, reason: str = 'Missing Package', install=None, package=None, raise_except: bool = False,
             source_script=None, pip_attrs=None):
    """Import the necessary external packages and provide explicit message to find a way to solve this error message.
    This method should also explain why this module is required to make sure this is really expected to get an error.

    :param name:
    :param reason:
    :param install:
    :param package:
    :param raise_except:
    :param source_script:
    :param pip_attrs: Optional. The pip attributes  https://packaging.python.org/tutorials/installing-packages/

    return: The python module
    """
    if install is None:
        install = name
    try:
        mod = importlib.import_module(name)
        if package is not None:
            return getattr(mod, package)

        return mod

    except Exception as err:
        if pip_attrs is None:
            pip_attrs = []
        if IMPORT_PROXY:
            pip_attrs.extend(['--proxy', IMPORT_PROXY])
        if IMPORT_PCK_REPO:
            pip_attrs.extend(['--no-index', '--find-links', IMPORT_PCK_REPO])

        if str(err).startswith("Missing required dependencies") and IMPORT_AUTOLOAD:
            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, IMPORT_AUTOLOAD))
            deps = json.loads(
                str(err).replace("Missing required dependencies ", "").replace("'", '"'))
            import subprocess
            for d in deps:
                exe_out = subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [d])
                logging.warning(exe_out)
            return requires(name, reason, install, package=package, raise_except=raise_except)

        if IMPORT_AUTOLOAD:
            if isinstance(IMPORT_AUTOLOAD, dict) and not IMPORT_AUTOLOAD.get(install, False):
                # Module not set in the configuration to be automatically loaded
                raise ValueError(err)

            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, IMPORT_AUTOLOAD))
            import subprocess
            subprocess.call([sys.executable, '-m', "pip", 'install'] + pip_attrs + [install])
            return requires(name, reason, install, package=package, raise_except=raise_except)

        if raise_except:
            logging.warning("Error with %s in script %s, autoload set to %s" % (name, source_script, IMPORT_AUTOLOAD))
            logging.warning("*** Module %s required ***" % name)
            logging.warning(reason)
            if install:
                logging.warning("Command to fix this error:")
                logging.warning(">>> pip install %s" % install)
            raise ValueError(err)


def load_package(package_name: str, pip_attrs: Optional[list] = None, action: str = 'install'):
    """Force the package to be installed manually to the current python distribution.
    This will run a pip command to the running python set up.

    Usage::
      load_package("pandas")

    `PYPI <https://pypi.org/>`_

    :param package_name: The external package reference (e.g. pandas)
    :param pip_attrs: Optional. The pip attributes  https://packaging.python.org/tutorials/installing-packages/
    :param action: Optional. The pip command (default install)
    """
    import subprocess

    if pip_attrs is None:
        pip_attrs = ['--ignore-installed', '--upgrade'] if action == 'install' else []
    if IMPORT_PROXY is not None:
        subprocess.call(
            [sys.executable, '-m', "pip", action, '--proxy="%s"' % IMPORT_PROXY] + pip_attrs + [package_name])
    else:
        subprocess.call([sys.executable, '-m', "pip", action] + pip_attrs + [package_name])


def installed_packages():
    """Returns the list of packages installed on the running Python distribution.
    This will require an internet connection as it will run the pip command behind the scene.
    It will return to the console a table with the status of the obsolescence of all the python packages.

    Usage::
      installed_packages()
    """
    import subprocess
    subprocess.call(["pip", 'list', '-o'])


def string_to_base64(content: str, is_binary: bool = False) -> str:
    """Format a String content to a base64 object.

    :param content: String content
    :param is_binary: Optional. Flag to specify if content need to be encoded
    """
    if not is_binary:
        content = content.encode()
    base64_bytes = base64.b64encode(content)
    return base64_bytes.decode('ascii')


def script_version(alias: str, script_details: dict, with_prefix: bool = False):
    """Return the script version number with or without prefix.
    This will ensure a standard way to get the version number for a given CSS or JavaScript script in the framework.

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    """
    all_js = get_js(IMPORT_PCK_REPO)
    all_css = get_css(IMPORT_PCK_REPO)
    if "version" in script_details:
        if with_prefix:
            if 'v_prefix' in all_js[alias]:
                return "%s%s" % (all_js[alias]['v_prefix'], script_details["version"])

        return script_details["version"]

    if with_prefix:
        if 'v_prefix' in all_js[alias]:
            return "%s%s" % (all_js[alias]['v_prefix'], all_js[alias]["version"])

    if alias in all_js:
        if 'node_folder' in all_js[alias]:
            # use the version of the node folder
            all_js[alias]["version"] = all_js[all_js[alias]['node_folder']]['version']
        return all_js[alias]["version"]

    if alias in all_css:
        return all_css[alias].get("version")


def script_cdnjs_path(
        alias: str,
        script_details: dict,
        with_prefix: bool = False,
        verbose: Optional[bool] = None
) -> str:
    """Get the script path to retrieve the content locally.
    This is mainly used by PyNpm package in order to retrieve the content of the script to produce local copies of them.
    Having script copied locally will speed up the loading of the page and also will ensure a run offline.

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    :param verbose:
    """
    all_js = get_js(IMPORT_PCK_REPO)
    details = dict(script_details)
    if PACKAGES_PATH is not None:
        local_path = Path(PACKAGES_PATH) / details['script']
        if local_path.exists() and verbose:
            logging.debug("IMPORTS | Package | file %s used from %s" % (
                details['script'], PACKAGES_PATH))
            return str(local_path)

    details["version"] = script_version(alias, script_details, with_prefix)
    details["path"] = details["path"] % details
    if "public" in details:
        if details["public"] == "cdnjs":
            details["cdnjs"] = IMPORT_CDNJS_URL
        elif details["public"] == "jsdeliver":
            details["cdnjs"] = IMPORT_JSDELIVER_URL
    elif "cdnjs" not in details:
        details["cdnjs"] = IMPORT_CDNJS_URL
    if IMPORT_USE_NPM_UNPK and all_js.get(alias, {}).get("unpkg", True):
        if "node_path" not in details:
            details["node_path"] = ""
        return IMPORT_UNPKG_URL + alias + "@latest/%(node_path)s%(script)s" % details

    try:
        return IMPORTS_EXPR % details

    except:
        return "%(cdnjs)s/%(path)s%(script)s" % details


def script_npm_path(alias: str, script_details: dict, static_path: str, with_prefix: bool = False) -> str:
    """

    :param alias: The package reference alias in the framework and in NPM
    :param script_details: The script definition in the framework
    :param static_path:
    :param with_prefix: Optional. Flag to specify if the full version number is required (with the prefix)
    """
    all_js = get_js(IMPORT_PCK_REPO)
    details = dict(script_details)
    details["version"] = script_version(alias, script_details, with_prefix)
    details["node_path"] = str(details.get("node_path", "\\") % details).replace("/", "\\")
    details["alias"] = all_js[alias].get("node_folder", alias)
    details["static"] = static_path
    if not details["node_path"].endswith("\\"):
        details["node_path"] += "\\"
    return r"%(static)s\%(alias)s\%(node_path)s%(script)s" % details
