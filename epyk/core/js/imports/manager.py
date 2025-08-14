import json
import re
import base64
import os
import logging
import traceback
import collections
from pathlib import Path
from typing import Optional, Dict, Union, List, Any, Tuple
from epyk.core.js.imports import registry
from epyk.conf.global_settings import IMPORT_PCK_REPO, IMPORTS_EXPR, PRIMARY_RESOURCE_PATHS, IMPORT_STATIC_PATH, \
    GOOGLE_SITE_KEY
from epyk.core.js.imports.utils import script_cdnjs_path, script_version
from epyk.core.js.imports.packages import ImportPackages

from urllib.request import urlopen, Request


_SERVICES = {}
""" """


class ImportManager:
    """
    The main class in charge of defining the order of the imports in the header.

    There is no check on the presence of the modules on the server. The only purpose of this module is to produce the
    string with the module names and the correct paths to your final HTML report.
    """

    online: bool = True
    self_contained: bool = False
    _static_path: Optional[str] = None
    set_exports: bool = False

    def __init__(self, page=None):
        """Load the hierarchy of modules.

        This module will define the import section in the header of the final HTML page.

        It will create links to the official online websites or link to an internal copy if no internet connection is
        available. To run a report using the online mode to False it is requires to get all the packages locally
        saved with the expected structured (basically the one of the CDNJS repository)

        :param page: Optional. The internal report object with all the required external modules
        """
        self.page, ovr_version, self.__pkgs = page, {}, None
        self.force_position = {}
        self.reload()

    def packages_from_json(self, dependency_file: str, ext_packages: Dict[str, dict]):
        """Reduce the list of packages to the ones defined in the packages.json.
        This will also add the requirements for those packages.

        Usage::
            page = ek.Page()
            page.imports.packages_from_json(r"./assets/package.json")

            # Loading external packages
            ext_pkgs = {
                "@eonasdan/tempus-dominus": {
                    'version': "6.7.7",
                    'req': [{'alias': '@popperjs/core'}, {'alias': 'bootstrap'}],
                    'modules': [
                      {'script': 'tempus-dominus.min.css', 'node_path': 'dist/css/', 'path': 'tempus-dominus/%(version)s/'},
                      {'script': 'tempus-dominus.min.js', 'node_path': 'dist/js/', 'path': 'tempus-dominus/%(version)s/'},
                    ]}}

            page.imports.packages_from_json(r"./assets/package.json", ext_pkgs)

        :param dependency_file: Path for the file packages.json
        :param ext_packages: A dictionary with all the external packages to add added to the internal imports
        """
        temp_js, temp_css = {}, {}
        for k, v in ext_packages.items():
            self.addPackage(k, v)
        all_js = registry.get_js(IMPORT_PCK_REPO)
        all_css = registry.get_css(IMPORT_PCK_REPO)
        packages = set()
        with open(dependency_file) as fp:
            package_json = json.load(fp)
            for dependency, version in package_json["dependencies"].items():
                packages.add(dependency)
                if dependency in all_js:
                    if version and "version" in all_js[dependency]:
                        if version.startswith("^"):
                            registry.set_attr(dependency, "version", version[1])
                        else:
                            registry.set_attr(dependency, "version", version)
                    for req in all_js[dependency].get("req", []):
                        packages.add(req["alias"])
                if dependency in all_css:
                    if version:
                        if version.startswith("^"):
                            registry.set_attr(dependency, "version", version[1])
                        else:
                            registry.set_attr(dependency, "version", version)
                    temp_css[dependency] = all_css[dependency]
                    for req in all_css[dependency].get("req", []):
                        packages.add(req["alias"])
        registry.reduce(packages)
        self.reload()

    def reload(self):
        ovr_version = {}
        if self.page is not None and self.page.ext_packages is not None:
            registry.extend(self.page.ext_packages)
        # if report is not None and self._report.run.report_name is not None and self._report.run.local_path is not None
        # and os.path.exists(os.path.join(self._report.run.local_path, '__init__.py')):
        # Force the version of some external Javascript or CSS packages
        #  packages = importlib.import_module("%s.__init__" % self._report.run.report_name)
        #  ovr_version = getattr(packages, 'MODULES', {})
        if self.page is not None:
            self.page._with_google_imports = False
            # Apply the different reports overrides on the packages versions
            ovr_version.update(self.page._props.get('packages', {}))
        self.jsImports, self.cssImports, self.moduleConfigs, self.reqVersion = {}, {}, {}, {}
        self.__add_imports([
            ('js', self.jsImports, registry.get_js(IMPORT_PCK_REPO)),
            ('css', self.cssImports, registry.get_css(IMPORT_PCK_REPO))
        ])

    def __add_imports(
            self,
            modules: List[Tuple[Optional[str], Optional[dict], Dict[str, dict]]],
            ovr_version: Optional[dict] = None
    ):
        for folder, import_dict, import_type in modules:
            if folder is None and import_type is None:
                continue

            if folder is None:
                for alias, definition in dict(import_type).items():
                    main_css = collections.OrderedDict()
                    main_js, main_js_types = collections.OrderedDict(), collections.OrderedDict()
                    for i, mod in enumerate(definition['modules']):
                        if ovr_version is not None and alias in ovr_version:
                            mod['version'] = ovr_version[alias]
                        else:
                            mod["version"] = definition["version"]
                        script_path = script_cdnjs_path(alias, mod)
                        if script_path.endswith(".js"):
                            main = main_js
                            main_js_types[script_path] = mod.get("type", 'text/javascript')
                        else:
                            main = main_css
                        if 'url' in definition:
                            main["%s%s" % (definition['url'], mod['script'])] = mod['version']
                        else:
                            main[script_path] = script_version(alias, mod)
                    modules = collections.OrderedDict()
                    self.getModules(modules, alias, folder, import_type)
                    if 'config' in definition:
                        self.moduleConfigs[alias] = definition['config']
                    if main_css:
                        self.cssImports[alias] = {'main': main_css, 'dep': list(modules.keys()),
                                                  'versions': list(main_css.values())}
                    if main_js:
                        self.jsImports[alias] = {'main': main_js, 'dep': list(modules.keys()),
                                                 'versions': list(main_js.values()),
                                                 "type": main_js_types}
            else:
                for alias, definition in dict(import_type).items():
                    main, main_types = collections.OrderedDict(), collections.OrderedDict()
                    for i, mod in enumerate(definition['modules']):
                        if ovr_version is not None and alias in ovr_version:
                            mod['version'] = ovr_version[alias]
                        script_path = script_cdnjs_path(alias, mod)
                        mod_type = "stylesheet" if script_path.endswith(".css") else 'text/javascript'
                        if 'url' in definition:
                            main["%s%s" % (definition['url'], mod['script'])] = mod['version']
                            main_types["%s%s" % (definition['url'], mod['script'])] = mod_type
                        else:
                            main[script_path] = script_version(alias, mod)
                            main_types[script_path] = mod_type
                    modules = collections.OrderedDict()
                    self.getModules(modules, alias, folder, import_type)
                    if 'config' in definition:
                        self.moduleConfigs[alias] = definition['config']
                    main_keys, versions = [], []
                    for k, v in main.items():
                        main_keys.append(k)
                        versions.append(v)
                    import_dict[alias] = {
                        'main': main, 'dep': list(modules.keys()), 'versions': versions, "type": main_types}

    @property
    def static_url(self) -> str:
        return self._static_path

    @static_url.setter
    def static_url(self, path: str):
        if path is not None:
            self.online = False
        self._static_path = path

    def add(self, alias: str, incl_css: bool = True, incl_js: bool = True):
        """Add package to the page external required modules.

        :param alias: The external module alias
        :param incl_css: Optional. Include CSS files
        :param incl_js: Optional. Include Js files
        """
        if alias in registry.get_js(IMPORT_PCK_REPO) and incl_js:
            self.page.jsImports.add(alias)
        if alias in registry.get_css(IMPORT_PCK_REPO) and incl_css:
            self.page.cssImport.add(alias)

    def extend(self, aliases: List[str]):
        """Add multiple aliases to the external requirements.

        :param aliases: The list of package aliases to be added
        """
        for alias in aliases:
            self.add(alias)

    @property
    def requirements(self) -> set:
        """Retrieve all the mandatory requirements required to display the final HTML page.

        Usage::
          print(page.imports().requirements)
        """
        module_alias = set(self.cleanImports(self.page.jsImports, registry.get_js(IMPORT_PCK_REPO)))
        for css in self.cleanImports(self.page.cssImport, registry.get_css(IMPORT_PCK_REPO)):
            module_alias.add(css)
        return module_alias

    def getModules(self, modules: dict, alias: Union[str, dict], folder: Optional[str] = None,
                   module_details: Optional[dict] = None) -> dict:
        """Return the list of modules for a given entry.
        This will be used recursively to resolve all the dependencies.

        Usage::
          modules = collections.OrderedDict()
          ImportManager().getModules(modules, 'c3')

        :param modules: The ordered definition of modules
        :param alias: The module reference in the above JS and CSS dictionaries
        :param folder: Optional. The folder name
        :param module_details: Optional. The module definition. Default check in the Javascript modules

        :return: The list of modules
        """
        if isinstance(alias, dict):
            alias = alias['alias']
        if module_details is None or alias not in module_details:
            module_details = registry.get_js(IMPORT_PCK_REPO)
        for mod in module_details[alias]['modules']:
            script = "".join([mod['path'] % mod, mod['script']])
            if 'url' in module_details[alias]:
                modules["%s/%s" % (module_details[alias]['url'], script)] = True
            else:
                modules[r"%s\%s" % (IMPORT_STATIC_PATH.replace("\\", "/"), script)] = True
        for req in module_details.get(alias, {}).get('req', []):
            self.getModules(modules, req, folder, module_details)
        return modules

    def getReq(self, mod: Union[str, dict], modules: List[dict], import_hierarchy: Optional[dict] = None,
               use_require_js: bool = False):
        """Set the list pf required modules for a given alias to the modules list.

        Usage::
          deps = []
          page.imports.getReq("c3", deps)
          print(deps)

        :param mod: The alias of the external package
        :param modules: The list of packages aliases in the inverse dependency order
        :param import_hierarchy: Optional. The package definition (Javascript | CSS) from the above import list
        :param use_require_js: Optional. Define if this is using requirejs to load imports. Default False
        """
        import_hierarchy = import_hierarchy or registry.get_js(IMPORT_PCK_REPO)
        if isinstance(mod, dict):
            # This will allow different versions of packages according to the modules
            # For example NVD3 cannot use any recent version of D3
            if 'version' in mod:
                if self.page is not None and self.page.verbose:
                    logging.warning("Setting %(alias)s to version %(version)s" % mod)
                if self.reqVersion.get(mod['alias']) is None or mod['version'] < self.reqVersion[mod['alias']]:
                    self.reqVersion[mod['alias']] = mod['version']
                new_main_for_alias, new_main_for_alias_css = collections.OrderedDict(), collections.OrderedDict()
                for path in self.jsImports[mod['alias']]['main']:
                    for v in self.jsImports[mod['alias']]['versions']:
                        new_main_for_alias[path.replace(v, self.reqVersion[mod['alias']])] = self.reqVersion[
                            mod['alias']]
                if mod['alias'] in self.cssImports:
                    for path in self.cssImports[mod['alias']]['main']:
                        for v in self.cssImports[mod['alias']]['versions']:
                            new_main_for_alias_css[path.replace(v, self.reqVersion[mod['alias']])] = self.reqVersion[
                                mod['alias']]
                    self.cssImports[mod['alias']]['main'] = new_main_for_alias_css
                # Store the new dictionary with the key and version updated for the module
                self.jsImports[mod['alias']]['main'] = new_main_for_alias
                for i, path in enumerate(self.jsImports[mod['alias']]['dep']):
                    for v in self.jsImports[mod['alias']]['versions']:
                        path = path.replace(v, self.reqVersion[mod['alias']])
                    self.jsImports[mod['alias']]['dep'][i] = path
            mod = mod['alias']
        modules.append(mod)
        # if self.page.ext_packages is not None and mod in self.page.ext_packages:
        #  import_hierarchy = self.page.ext_packages
        req_key = "req"
        if use_require_js:
            if "req_js" in import_hierarchy.get(mod, {}):
                req_key = "req_js"
        for req in import_hierarchy.get(mod, {}).get(req_key, []):
            self.getReq(req, modules, import_hierarchy, use_require_js=use_require_js)

    def cleanImports(self, imports: List[str], import_hierarchy: Optional[dict] = None, use_require_js: bool = False, verbose: bool = None):
        """Remove the underlying imports to avoid duplicated entries.

        Usage::
          >>> ImportManager().cleanImports(['c3'], JS_IMPORTS)
        ['jquery', 'd3', 'c3']

        :param imports: An array with the list of aliases for the external packages
        :param import_hierarchy: Optional. The package definition (Javascript | CSS) from the above import list
        :param use_require_js: Optional. Define if this is using requirejs to load imports. Default False
        :param verbose:

        :return: Return the list with the full list of aliases (including dependencies)
        """
        import_resolved, polyfills = [], []
        all_js = registry.get_js(IMPORT_PCK_REPO)
        for mod in imports:
            self.getReq(mod, import_resolved, import_hierarchy or all_js, use_require_js=use_require_js)
        for a in set(import_resolved):
            if a in registry.PACKAGE_STATUS:
                if not registry.PACKAGE_STATUS[a].get("allowed", True):
                    raise ValueError("Package %s not allowed" % a)

                if self.page is not None and "info" in registry.PACKAGE_STATUS[a]:
                    if verbose is None and self.page is not None:
                        verbose = self.page.verbose
                    if verbose:
                        # Change this to be info logs instead of warnings
                        logging.info("%s: %s" % (a, registry.PACKAGE_STATUS[a]["info"]))
            occurrences = [j for j, x in enumerate(import_resolved) if x == a]
            if len(occurrences) > 1:
                for j in occurrences[::-1][1:]:
                    import_resolved.pop(j)
            if all_js.get(a, {}).get("polyfill"):
                import_resolved.remove(a)
                polyfills.append(a)
        local_pkgs, ext_pkgs = [], []
        for pkg in import_resolved[::-1]:
          if pkg.startswith("local_"):
            local_pkgs.append(pkg)
          else:
            ext_pkgs.append(pkg)
        return polyfills + ext_pkgs + local_pkgs

    def cssResolve(self, css_aliases: List[str], local_css: Optional[dict] = None, excluded: List[str] = None):
        """Return the list of CSS modules to add to the header.

        Usage::
          >>> ImportManager().cssResolve(['c3'])
        '<link rel="stylesheet" href="/static/c3/0.6.12/c3.min.css" type="text/css">'

        :param css_aliases: An array with the list of aliases for the external packages
        :param local_css: Optional. The external file overrides with the full path
        :param excluded: Optional. Packages excluded from the result object (mandatory for some frameworks
          already onboarding modules).

        :return: The string to be added to the header.
        """
        css = []
        self.__add_imports([(None, None, self.page.ext_packages)])
        # Import hierarchy will rely on the internal JavaScript definition.
        css_aliases = [
            c for c in self.cleanImports(css_aliases, registry.get_js(IMPORT_PCK_REPO))
            if c in self.cssImports or c in _SERVICES]
        all_css = registry.get_css(IMPORT_PCK_REPO)
        for css_alias in css_aliases:
            if excluded is not None and css_alias in excluded:
                continue

            if not self.online:
                self.pkgs.get(css_alias).set_local(static_url=self.static_url)
            if css_alias in _SERVICES:
                # Add services url
                for service in _SERVICES[css_alias].get('css', []):
                    css.append('<link rel="stylesheet" href="%s">' % service)
                continue

            for urlModule in list(self.cssImports[css_alias]['main']):
                if self.page._node_modules is not None:
                    node_sub_path = all_css.get(css_alias, {}).get('register', {}).get('npm_path')
                    if node_sub_path is not None:
                        css_file = os.path.split(urlModule)[1]
                        npm_alias = all_css[css_alias]['register'].get('npm', css_alias)
                        package_path = os.path.join(
                            self.page._node_modules[0], "node_modules", npm_alias, node_sub_path, css_file)
                        if os.path.exists(package_path):
                            urlModule = os.path.join(
                                self.page._node_modules[1], npm_alias, node_sub_path, css_file).replace("\\", "/")
                if os.path.isabs(urlModule) and Path(urlModule).exists():
                    with open(urlModule, "rb") as fp:
                        base64_bytes = base64.b64encode(fp.read())
                        base64_message = base64_bytes.decode('ascii')
                        urlModule = "data:text/css;base64,%s" % base64_message
                elif self.self_contained:
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                            'Accept-Encoding': 'none',
                            'Accept-Language': 'en-US,en;q=0.8',
                            'Connection': 'keep-alive'}
                        request = Request(urlModule, None, headers)
                        with urlopen(request) as response:
                            base64_bytes = base64.b64encode(response.read())
                            base64_message = base64_bytes.decode('ascii')
                            urlModule = "data:text/css;base64,%s" % base64_message
                    except Exception as err:
                        print(urlModule)
                        print(traceback.format_exc())

                css.append('<link rel="stylesheet" href="%s" type="text/css">' % urlModule)
        if local_css is not None:
            for css_file in local_css:
                css.append('<link rel="stylesheet" href="%s" type="text/css">' % css_file)
        return "\n".join(css)

    def cssURLs(self, css_str: str):
        """Retrieve the list of CSS dependencies URL from a header.

        :param css_str: The CSS String in the page

        :return: A Python list with all the CSS external URL to be imported.
        """
        return re.findall('<link rel="stylesheet" href="(.*?)" type="text/css">', css_str)

    def jsResolve(self, js_aliases: List[str], local_js: Optional[dict] = None, excluded: Optional[List[str]] = None,
                  local_title: str = "", verbose: Optional[bool] = None):
        """Return the list of Javascript modules to add to the header.

        Usage::
          >>> ImportManager().jsResolve(['c3'])
        '<script language="javascript" type="text/javascript" src="/static/jquery/3.4.1/jquery.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/d3/5.9.7/d3.min.js"></script>\n<script language="javascript" type="text/javascript" src="/static/c3/0.6.12/c3.min.js"></script>'

        :param js_aliases: An array with the list of aliases for the external packages
        :param local_js: Optional. The external file overrides with the full path
        :param excluded: Optional. Packages excluded from the result object
           (mandatory for some frameworks already onboarding modules)
        :param local_title: Optional. Local JavaScript file title description
        :param verbose: Optional.

        :return: The string to be added to the header
        """
        from epyk.conf.global_settings import (ASSETS_SPLIT, ASSETS_SPLIT_MINIFY, ASSETS_PRINT_PATHS, ASSETS_OUT_PATH,
                                               ASSETS_STATIC_ROUTE, ASSETS_STATIC_PATH, ASSETS_STATIC_JS)

        js = []
        if verbose is None and self.page is not None:
            verbose = self.page.verbose
        if self.set_exports:
            # Fix for missing require function
            js.append("<script>var exports = {}; function require(a){return window[a]}</script>")
        # self.__add_imports([(None, None, self._report.ext_packages)])
        all_js = registry.get_js(IMPORT_PCK_REPO)
        js_aliases = self.cleanImports(js_aliases, all_js)
        for js_alias in js_aliases:
            if excluded is not None and js_alias in excluded:
                continue

            if not self.online:
                self.pkgs.get(js_alias).set_local(static_url=self.static_url)
            extra_configs = "?%s" % self.moduleConfigs[js_alias] if js_alias in self.moduleConfigs else ""
            for url_module in list(self.jsImports.get(js_alias, {}).get('main', [])):
                if self.page._node_modules is not None:
                    node_sub_path = all_js.get(js_alias, {}).get('register', {}).get('npm_path')
                    if node_sub_path is not None:
                        js_file = os.path.split(url_module)[1]
                        npm_alias = all_js[js_alias]['register'].get('npm', js_alias)
                        package_path = os.path.join(
                            self.page._node_modules[0], "node_modules", npm_alias, node_sub_path, js_file)
                        if os.path.exists(package_path):
                            url_module = os.path.join(
                                self.page._node_modules[1], npm_alias, node_sub_path, js_file).replace("\\", "/")

                # if '/mode/' in url_module:
                #  js.append('<script type="module" language="javascript" src="%s%s"></script>' % (url_module, extra_configs))
                mod_type = self.jsImports[js_alias]['type'].get(url_module, "text/javascript")
                mod_title = os.path.split(url_module)[-1]
                if os.path.isabs(url_module) and not url_module.startswith("/static"):
                    file_name, file_extension = os.path.splitext(url_module)
                    if not file_extension.endswith(".js"):
                        continue

                    self.jsImports[js_alias]['title'] = os.path.split(url_module)[-1]
                    module_exists = os.path.exists(url_module)
                    if module_exists:
                        with open(url_module, "rb") as fp:
                            if mod_type == "text/javascript":
                                # export cannot be used in javascript scripts not set as modules
                                tmp_file = []
                                for line in fp.readlines():
                                    for m_expr, m_rep in {b"^export ": b""}.items():
                                        line = re.sub(m_expr, m_rep, line)
                                    tmp_file.append(line)
                                js_content = b"".join(tmp_file)
                            else:
                                js_content = fp.read()
                            if ASSETS_SPLIT:
                                js_path = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_JS
                                if not js_path.exists():
                                    js_path.mkdir(parents=True, exist_ok=True)
                                with open(js_path / self.jsImports[js_alias]['title'], "wb") as fp:
                                    fp.write(js_content)
                                url_module = "%s/%s/%s" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_JS, self.jsImports[js_alias]['title'])
                            else:
                                base64_bytes = base64.b64encode(js_content)
                                base64_message = base64_bytes.decode('ascii')
                                url_module = "data:text/js;base64,%s" % base64_message
                    elif verbose:
                        logging.warning("Missing File: %s" % url_module)
                elif self.self_contained:
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                            'Accept-Encoding': 'none',
                            'Accept-Language': 'en-US,en;q=0.8',
                            'Connection': 'keep-alive'}
                        request = Request(url_module, None, headers)
                        with urlopen(request) as response:
                            base64_bytes = base64.b64encode(response.read())
                            base64_message = base64_bytes.decode('ascii')
                            url_module = "data:text/js;base64,%s" % base64_message
                    except Exception as err:
                        logging.error(url_module)
                        logging.error(traceback.format_exc())
                if self.pkgs.get(js_alias).defer:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s" defer></script>' % (
                            mod_title, mod_type, url_module, extra_configs))
                elif self.pkgs.get(js_alias).asynchrone:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s" async></script>' % (
                            mod_title, mod_type, url_module, extra_configs))
                else:
                    js.append(
                        '<script title="%s" language="javascript" type="%s" src="%s%s"></script>' % (
                        mod_title, mod_type, url_module, extra_configs))
        if local_js is not None and len(local_js) > 0:
            for local_js_file in local_js:
                js.append('<script title="%s" language="javascript" type="text/javascript" src="%s"></script>' % (
                    local_title, local_js_file))
        return "\n".join(js)

    def jsURLs(self, expr: str):
        """Retrieve the list of Javascript dependencies URL from a header.

        :param expr: The Javascript String in the page

        :return: A Python list with all the Javascript external URL to be imported.
        """
        return re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', expr)

    def getFiles(self, css_alias: List[str], js_alias: List[str]) -> dict:
        """Retrieve the package definition from the list of module aliases

        Usage::
          >>> ImportManager().getFiles(['c3'], ['c3'])
        f['css'][0]['file']['script']

        :param css_alias: An array with the list of aliases for the CSS external packages
        :param js_alias: An array with the list of aliases for the Js external packages

        :return: A dictionary with the CSS and JS files definition.
        """
        all_js = registry.get_js(IMPORT_PCK_REPO)
        all_css = registry.get_css(IMPORT_PCK_REPO)
        files = {'css': [], 'js': []}
        mod_css, mod_js = {}, {}
        for alias, details in all_css.items():
            mod_css[alias] = []
            for module in details['modules']:
                mod_css[alias].append(
                    {'version': module.get('version', ''), 'alias': alias, 'file': module,
                     'website': details.get('website', ''), 'status': details.get('status', '')})
        for alias, details in all_js.items():
            mod_js[alias] = []
            for module in details['modules']:
                mod_js[alias].append(
                    {'version': module.get('version', ''), 'alias': alias, 'file': module,
                     'website': details.get('website', ''), 'status': details.get('status', '')})
        for css_file in self.cleanImports(css_alias, all_css):
            files['css'].extend(mod_css[css_file])
        for js_file in self.cleanImports(js_alias, all_js):
            files['js'].extend(mod_js[js_file])
        return files

    def cssGetAll(self):
        """To retrieve the full list of available modules on the server.

        This will return the dependencies as they should be included in the HTML page.
        The order and the path resolution is already performed.

        If split is True the generated css file will be not included.

        Usage::
          print(page.imports.cssGetAll())
        """
        all_css = registry.get_css(IMPORT_PCK_REPO)
        return self.cssResolve(list(all_css.keys()))

    def jsGetAll(self):
        """To retrieve the full list of available modules on the server.

        This will return the dependencies as they should be included in the HTML page.
        The order and the path resolution is already performed.

        If split is True the generated JS file will be not included.

        Usage::
          print(page.imports.jsGetAll())
        """
        all_js = registry.get_js(IMPORT_PCK_REPO)
        return self.jsResolve(list(all_js.keys()))

    def getFullPackage(self, alias: str, version: Optional[str] = None, static_path: Optional[str] = None,
                       reload: bool = False):
        """Download a full package (CSS and JS) locally for a server or full offline mode.

        Usage::
          Imports.ImportManager(report=Report()).getFullPackage('font-awesome')

        :param alias: The package reference in the above list
        :param version: Optional. The package version to retrieve
        :param static_path: Optional. The path in which the files should be copied to
        :param reload: Optional. Flag to force the package reloading if the folder already exists. Default False

        :return: The Python Import manager.
        """

        import zipfile
        import shutil
        import io
        import os

        if not hasattr(self.page, "py"):
            from epyk.core.py.PyRest import PyRest
            webscrapper = PyRest().webscrapping
        else:
            webscrapper = self.page.py.requests.webscrapping
        all_js = registry.get_js(IMPORT_PCK_REPO)
        if 'package' in all_js[alias]:
            version_dict = {'version': all_js[alias]['modules'][0]['version'] if version is None else version}
            package_path = all_js[alias]['package']['zip'] % version_dict
            if static_path is None:
                static_path = os.path.join(
                    os.path.dirname(__file__), '..', '..', 'static', all_js[alias]['package']['folder'])
            else:
                static_path = os.path.join(static_path, "static")
            if not os.path.exists(static_path):
                # Create the destination folders if missing
                os.makedirs(static_path)
            dst_path = os.path.join(
                static_path, all_js[alias]['package'].get('folder', ''),
                all_js[alias]['package'].get('path', '%(version)s') % version_dict)
            v_reload_path = True
            if os.path.exists(dst_path):
                if not reload:
                    v_reload_path = False
                else:
                    shutil.rmtree(dst_path)

            if v_reload_path:
                logging.warning("  > Downloading package %s" % package_path)
                r = webscrapper(package_path)
                z = zipfile.ZipFile(io.BytesIO(r))
                z.extractall(static_path)
                if all_js[alias]['package']['root'] is not None:
                    root = all_js[alias]['package']['root'] % version_dict
                    shutil.copytree(os.path.join(static_path, root), dst_path)
                    shutil.rmtree(os.path.join(static_path, root))
                logging.warning("  < Package %s. Done ! " % alias)
            else:
                logging.warning("  < Package %s already loaded " % alias)
        return self

    def setVersion(self, alias: str, version: str, js: Optional[dict] = None, css: Optional[dict] = None,
                   verbose: bool = None) -> bool:
        """Allow the use of different version of a package.
        This will change the Import important to the Python env.

        Usage::
          page.imports.setVersion(page.imports.pkgs.popper_js.alias, "1.00.0")

        :param alias: The package reference in the above list
        :param version: The new version to be used globally
        :param js: Optional. The JavaScript packages to be added
        :param css: Optional. The CSS packages to be added
        :param verbose: Optional. Display version details (default True)
        """
        self.reqVersion[alias] = version
        all_js = registry.get_js(IMPORT_PCK_REPO)
        all_css = registry.get_css(IMPORT_PCK_REPO)
        current_version = all_js.get(alias, all_css.get(alias, {})).get('version')
        if version == current_version:
            return False

        if verbose:
            print("Moving %s from %s to %s" % (alias, current_version, version))
        registry.set_attr(alias, "version", version)
        all_js = registry.get_js(IMPORT_PCK_REPO)
        if js is not None:
            if not js:
                if alias in all_js:
                    del self.jsImports[alias]
                    del all_js[alias]

            else:
                self.jsImports[alias] = {'main': collections.OrderedDict(), 'dep': [], 'versions': version}
                for k, v in js.items():
                    all_js[alias][k] = v
                    for module in js["modules"]:
                        module["path"] = module["path"] % {"version": version}
                        self.jsImports[alias]['main'][IMPORTS_EXPR % module] = version
        all_css = registry.get_css(IMPORT_PCK_REPO)
        if css is not None:
            if not css:
                if alias in all_css:
                    del self.cssImports[alias]
                    del CSS_IMPORTS[alias]

            else:
                for k, v in css.items():
                    CSS_IMPORTS.setdefault(alias, {})[k] = v
                for module in css["modules"]:
                    module["path"] = module["path"] % {"version": version}
                    self.cssImports.setdefault(alias, {}).setdefault('main', {})[
                        IMPORTS_EXPR % module] = version
        return True

    def addPackage(self, alias: str, config: dict):
        """Add a new package or update an existing one with new parameters.
        Only few parameters are available here in order to limit the changes.

        Usage::
          i.addPackage('test',
          {
            'req': [{'alias': 'd3'}],
            'modules': [
              {'script': 'dc.min.css', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
              {'script': 'dc.min.js', 'version': '3.0.9', 'path': 'dc/%(version)s/', 'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs'},
            ]},
          )

        :param alias: The package alias
        :param config: The Python dictionary with the package details

        :return: The import Manager.
        """
        registry.extend({alias: config})
        all_css = registry.get_css(IMPORT_PCK_REPO)
        all_js = registry.get_js(IMPORT_PCK_REPO)
        if alias in all_css:
            self.cssImports[alias] = {
                "main": collections.OrderedDict(), 'versions': [config.get("version", "")], 'dep': [],
                "type": collections.OrderedDict()}
            for pkg in all_css[alias].get("modules", []):
                self.cssImports[alias]["main"][script_cdnjs_path(alias, pkg)] = pkg.get("version", config["version"])
                if "type" in pkg:
                    self.cssImports[alias]["type"][script_cdnjs_path(alias, pkg)] = pkg["type"]
                else:
                    self.cssImports[alias]["type"][script_cdnjs_path(alias, pkg)] = 'stylesheet'
        if alias in all_js:
            self.jsImports[alias] = {
                "main": collections.OrderedDict(), 'versions': [all_js[alias].get("version", "")], 'dep': [],
                "type": collections.OrderedDict()}
            for pkg in all_js[alias]["modules"]:
                self.jsImports[alias]["main"][script_cdnjs_path(alias, pkg)] = pkg.get("version", config.get("version", ''))
                if "type" in pkg:
                    self.jsImports[alias]["type"][script_cdnjs_path(alias, pkg)] = pkg["type"]
                else:
                    self.jsImports[alias]["type"][script_cdnjs_path(alias, pkg)] = 'text/javascript'
        return self

    def to_requireJs(self, data: dict, excluded_packages: Optional[list] = None) -> dict:
        """

        :param data: The Report modules to resolve
        :param excluded_packages: Optional. The packages to exclude
        """
        deps_level, alias_to_name, alias_to_var, name_to_alias, results = {}, {}, {}, {}, {
            'jsFrgs': data['jsFrgs'], 'paths': {}}
        m_versions = {}
        all_js = registry.get_js(IMPORT_PCK_REPO)
        # Check first if some specific versions are required for the packages
        for m in self.page.jsImports:
            import_ref = all_js
            if self.page.ext_packages is not None and m in self.page.ext_packages:
                import_ref = self.page.ext_packages
            req_alias = "req_js" if "req_js" in import_ref[m] else "req"
            for req in import_ref[m].get(req_alias, []):
                if 'version' in req:
                    m_versions[req['alias']] = req['version']
        # Produce the dependency tree for requirejs
        for m in self.cleanImports(self.page.jsImports, all_js, use_require_js=True):
            if m.startswith("local_") or (excluded_packages is not None and m in excluded_packages):
                continue

            if not self.online:
                self.pkgs.get(m).set_local(static_url=self.static_url)

            import_ref = all_js
            if self.page.ext_packages is not None and m in self.page.ext_packages:
                import_ref = self.page.ext_packages
            if 'register' in import_ref[m]:
                alias = import_ref[m]['register'].get('alias', m)
                first_module = import_ref[m]['modules'][0]
                if 'version' not in first_module:
                    first_module['version'] = import_ref[m]['version']
                if m in m_versions:
                    first_module['version'] = m_versions[m]
                if not self.online:
                    self.pkgs.get(m).set_local(static_url=self.static_url)
                    results['paths']["'%s'" % alias] = list(self.jsImports[m]["main"].keys())[0][:-3]
                else:
                    results['paths']["'%s'" % alias] = "%s/%s%s" % (
                        first_module["cdnjs"], first_module['path'] % first_module,
                        import_ref[m]['register'].get('module', first_module['script'][:-3]))
                alias_to_name[m] = alias
                alias_to_var[m] = import_ref[m]['register'].get('variable', alias)
                name_to_alias[alias] = m
                req_alias = 'req_js' if 'req_js' in import_ref[m] else "req"
                if req_alias in import_ref[m]:
                    req_levels = [deps_level.get(req_def["alias"], -1) for req_def in import_ref[m][req_alias]]
                    deps_level[m] = max(req_levels) + 1
                else:
                    deps_level[m] = 0
        # Create the chains of modules to be loaded
        level, group = None, []
        for k, v in sorted(deps_level.items(), key=lambda item: item[1])[::-1]:
            if level is None:
                level = v
            if level != v:
                for g, var in group:
                    if 'init_fnc' in all_js[name_to_alias[g]]['register']:
                        results['jsFrgs'] = "%s; %s" % (
                        all_js[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
                results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
                    "', '".join([g for g, _ in group]), ", ".join([g for _, g in group]), results['jsFrgs'])
                level, group = v, [(alias_to_name[k], alias_to_var[k])]
            else:
                group.append((alias_to_name[k], alias_to_var[k]))
        if group:
            for g, var in group:
                import_ref = all_js
                if self.page.ext_packages is not None and name_to_alias[g] in self.page.ext_packages:
                    import_ref = self.page.ext_packages
                if 'init_fnc' in import_ref[name_to_alias[g]]['register']:
                    results['jsFrgs'] = "%s; %s" % (
                    import_ref[name_to_alias[g]]['register']['init_fnc'], results['jsFrgs'])
            results['jsFrgs'] = "require(['%s'], function (%s) { %s })" % (
                "', '".join([g for g, _ in group]), ", ".join([g for _, g in group]), results['jsFrgs'])
        return results

    def show(self, all: bool = False) -> dict:
        """Show all the underlying packages used in a report or available in the framework.

        :param all: Optional. A flag to specify if only the one requested in the report should be displayed
        """
        all_js = registry.get_js(IMPORT_PCK_REPO)
        all_css = registry.get_css(IMPORT_PCK_REPO)
        packages = {}
        if not all:
            for imp, repo in [(self.page.cssImport, all_css), (self.page.jsImports, all_js)]:
                pkg = self.cleanImports(imp, repo)
                for c in pkg:
                    for s in repo[c].get('modules', []):
                        s['path'] = s['path'] % s
                        packages.setdefault(c, []).append({"script": IMPORTS_EXPR % s, 'version': s['version']})
        else:
            for mod in [all_css, all_js]:
                for c, pkg in mod.items():
                    for s in pkg.get('modules', []):
                        s['path'] = s['path'] % s
                        packages.setdefault(c, []).append({"script": IMPORTS_EXPR % s, 'version': s['version']})
        return packages

    def google_products(self, products: List[str], api_key: Optional[str] = None,
                        site_key: str = GOOGLE_SITE_KEY):
        """Enable the google predefined products.
        Those are by default disabled as they are sharing data with Google.

        TODO: Add the use of the API Key.

        Usage::
          page.imports.google_products(['charts'])
          page.imports.google_products(['maps'])
          page.imports.google_products(['tables'])

        :param products: The various Google products to enable in the report
        :param api_key: Optional. The Google developer API key
        :param site_key: Optional. The Google site key: https://developers.google.com/recaptcha/docs/v3
        """
        for p in products:
            for m in registry.GOOGLE_EXTENSIONS[p].get("modules", []):
                m["script"] = m["script"] % {"api_key": api_key, 'site_key': site_key}
            self.addPackage("google-%s" % p, registry.GOOGLE_EXTENSIONS[p])
            if 'launcher' in registry.GOOGLE_EXTENSIONS[p]:
                self.page.properties.js.add_builders(registry.GOOGLE_EXTENSIONS[p]['launcher'])
        self.page._with_google_imports = True

    def locals(self, aliases: List[str], end_points: Optional[str] = None):
        """Short circuit the import mechanism and retrieve the selected ones from a local static path.
        This could help on the debugging and the improvement of the packages before submitting them for review.

        :param aliases: The list of aliases
        :param end_points: Optional. The end point on the server (The module static_path as default)
        """
        all_js = registry.get_js(IMPORT_PCK_REPO)
        logging.warning("Routing packages %s locally this should not be put on a server !" % aliases)
        for alias in aliases:
            if alias in all_js:
                for m in all_js[alias]['modules']:
                    m.update({'path': '', 'cdnjs': end_points or self.static_url})
        all_css = registry.get_css(IMPORT_PCK_REPO)
        for alias in aliases:
            if alias in all_css:
                for m in all_css[alias]['modules']:
                    m.update({'path': '', 'cdnjs': end_points or self.static_url})

    @property
    def pkgs(self) -> ImportPackages:
        """Shortcut properties to the various package definitions.
        This can be used in the script in order to change the path of the version of any external modules used.
        """
        return ImportPackages(self.jsImports, self.cssImports, page=self.page)

    def website(self, alias: str) -> str:
        """Get the official website for a JavaScript library.

        :param alias: The JavaScript module alias (usually the one used by npm)
        """
        return registry.get_js(IMPORT_PCK_REPO).get(alias, {}).get('website', "")

    def append_to(self, alias: str, js_modules: List[dict] = None, css_modules: List[dict] = None, version: str = None):
        """Update an existing configuration by adding addon scripts or styles.

        :param alias: NPM package alias
        :param js_modules: JavaScript modules extension
        :param css_modules: CSS styles extension
        :param version: The package version (if different)
        """
        all_js = registry.get_js(IMPORT_PCK_REPO)
        all_css = registry.get_css(IMPORT_PCK_REPO)
        if js_modules is not None:
            version = version or all_js[alias]["version"]
            for js_module in js_modules:
                js_module["cdnjs"] = registry.get_repo_path(js_module)
                self.jsImports[alias]["main"][script_cdnjs_path(alias, js_module)] = version
                self.jsImports[alias]["type"][script_cdnjs_path(alias, js_module)] = 'text/javascript'
        if css_modules is not None:
            version = version or all_css.get(alias, {}).get("version") or all_js[alias]["version"]
            for css_module in css_modules:
                css_module["cdnjs"] = registry.get_repo_path(css_module)
                self.jsImports[alias]["main"][script_cdnjs_path(alias, css_module)] = version
                self.jsImports[alias]["type"][script_cdnjs_path(alias, css_module)] = 'stylesheet'

    def attach_data(self, name: str, data: Any, **kwargs):
        """Attach data to a common data.

        :param name: Main JavaScript variable name
        :param data: JavaScript Data written to the file
        :param kwargs: Optional. Other key / values data to register to the file
        """
        from epyk.conf.global_settings import ASSETS_SPLIT, ASSETS_STATIC_DATA, ASSETS_STATIC_PATH, ASSETS_STATIC_ROUTE

        main_data = ["var %s = %s;" % (name.upper(), json.dumps(data))]
        for k, v in kwargs.items():
            main_data.append("var %s = %s;" % (k.upper(), json.dumps(v)))
        if ASSETS_SPLIT:
            data_path = Path(ASSETS_STATIC_PATH) / ASSETS_STATIC_DATA
            if not data_path.exists():
                data_path.mkdir(parents=True, exist_ok=True)
            with open(data_path / ("%s.js" % name), "w") as fp:
                fp.write("\n".join(main_data))
            self.page.headers.add_script(
                "%s/%s/%s.js" % (ASSETS_STATIC_ROUTE, ASSETS_STATIC_DATA, name), {"title": "static data"})
        else:
            self.page.properties.js.add_constructor(name, "\n".join(main_data))
        return self.page.js.getVar(name.upper())

    def insert_path(self, path: str, n: int = 0) -> bool:
        """Add a path to the global path.

        :param path: Path to add
        :param n: Position in the resources list
        """
        if not Path(path).exists():
            return False

        for p in PRIMARY_RESOURCE_PATHS:
            if p == path:
                return False

        PRIMARY_RESOURCE_PATHS.insert(n, path)
        return True


class Package:

    @property
    def all(self):
        """Get the definition of the package defined in this version of the package.
        This will simplify the compatibility with the interface.
        """
        return ImportManager().pkgs

    @classmethod
    def avoid_cache(cls, name: str) -> str:
        """This will allow the creation and the change of external packages usually cached by the browser.
        It will add a unique ID to make sure the browser will always try to reload it.

        Usage::
          return jsonify({
            "import_pkg": pk.package.avoid_cache(r"/static/formatters-numbers-new.js")})

        :param name: The package name
        """
        import random
        return "%s?version=%s" % (name, random.random())
