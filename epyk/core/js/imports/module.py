import collections
import os
from typing import Optional
from epyk.core.js.imports.registry import get_js, get_css, update
from epyk.conf.global_settings import IMPORT_PCK_REPO, IMPORT_JSDELIVER_URL, IMPORT_STATIC_PATH


class ImportModule:
    """

    """
    overridden: bool = False

    def __init__(self, name: str, js: dict, css: dict, links: Optional[dict] = None, page=None):
        self._name = name
        self.page = page
        self.community_version = True
        self._defer, self._async, self.attrs = False, False, {}
        if page is not None and name not in js and name.startswith("local_"):
            # In this case the configuration needs to be retrieved from the page context instead
            self._js = self.page.imports.jsImports[name]
        else:
            self._js = js[name]
        self._css = css.get(name, {})
        if links is not None:
            links[self._name] = self

    @property
    def name(self):
        return self._name

    @property
    def alias(self) -> str:
        """Get the NPM alias name."""
        return self._name

    @property
    def defer(self) -> bool:
        """If the defer attribute is set, it specifies that the script is downloaded in parallel to parsing the page,
        and executed after the page has finished parsing.

        `Defer <https://www.w3schools.com/tags/att_script_defer.asp>`_
        """
        return self._defer

    @defer.setter
    def defer(self, flag: bool):
        self._defer = flag

    @property
    def asynchrone(self) -> bool:
        """Specifies that the script is downloaded in parallel to parsing the page, and executed as soon as it is
        available (before parsing completes) (only for external scripts).

        `Defer <https://www.w3schools.com/tags/att_script_defer.asp>`_
        """
        return self._async

    @asynchrone.setter
    def asynchrone(self, flag: bool):
        self._async = flag

    @property
    def nomodule(self) -> bool:
        """Specifies that the script should not be executed in browsers supporting ES2015 modules.

        `Tag Script <https://www.w3schools.com/tags/tag_script.asp>`_
        """
        return self.attrs.get("nomodule")

    @nomodule.setter
    def nomodule(self, flag: bool):
        self.attrs["nomodule"] = flag

    @property
    def eferrerpolicy(self) -> str:
        """Specifies which referrer information to send when fetching a script.

        `w3schools <https://www.w3schools.com/tags/att_script_referrepolicy.asp>`_
        """
        return self.attrs.get("eferrerpolicy")

    @eferrerpolicy.setter
    def eferrerpolicy(self, value: str):
        self.attrs["eferrerpolicy"] = value

    @property
    def version(self):
        """Return the package version number defined in the framework. """
        return self._js["versions"]

    @version.setter
    def version(self, val: str):
        new_js = collections.OrderedDict()
        for k, v in self._js["main"].items():
            new_js[k.replace(v, val)] = val
        self._js["versions"] = [val]
        self._js["main"] = new_js
        # Change the package for ChartJs versions above 4
        # https://www.chartjs.org/docs/latest/migration/v4-migration.html
        if self.alias == "chart.js" and int(val.split(".")[0]) > 3:
            new_js = collections.OrderedDict()
            for k, v in self._js["main"].items():
                new_js[k.replace(v, val).replace("chart.min.js", "chart.umd.min.js")] = val
            self._js["main"] = new_js
        if self._css:
            new_css = collections.OrderedDict()
            for k, v in self._css["main"].items():
                new_css[k.replace(v, val)] = val
            self._css["versions"] = [val]
            self._css["main"] = new_css

    @property
    def path(self) -> str:
        """Get the package path used to retrieve the various modules. """
        mod = get_js(IMPORT_PCK_REPO)[self._name]['modules'][0]
        mod["version"] = self.version[0]
        mod["path"] = mod["path"] % mod
        return "%(cdnjs)s/%(path)s" % mod

    @path.setter
    def path(self, full_path: str):
        if full_path.endswith("/"):
            full_path = full_path[:-1]
        for mod in get_js(IMPORT_PCK_REPO)[self._name]['modules']:
            mod["cdnjs"] = full_path
            mod["path"] = ""
        if self._name in get_css(IMPORT_PCK_REPO):
            for mod in get_css(IMPORT_PCK_REPO)[self._name]['modules']:
                mod["cdnjs"] = full_path
                mod["path"] = ""

    @property
    def scripts(self):
        """Get the list of external files used for this package.

        Usage::
          pkgs = page.imports().pkgs
          pkgs.tabulator.version = "4.8.7"
          print(pkgs.tabulator.scripts)
        """
        return self._js["main"].keys() | self._css["main"].keys()

    @property
    def js(self) -> list:
        return list(self._js["main"].keys())

    @property
    def css(self) -> list:
        return list(self._css["main"].keys())

    def add(self):
        """Force a package to be added to the external requirements."""
        if self._name in get_js(IMPORT_PCK_REPO):
            self.page.jsImports.add(self._name)
        if self._name in get_css(IMPORT_PCK_REPO):
            self.page.cssImport.add(self._name)

    def from_cdnjs(self):
        """Just change the overridden flag of this package to ensure it will not be changed by the set_local method.
        Indeed, this method will not impact any modules with this flag set to True.
        """
        self.overridden = True

    def set_local(self, static_url: Optional[str] = None):
        """Route the package to the local path.
        Check first of the modules exist and raise an error otherwise.

        :param static_url: Optional. The static root on the server. (default value /static/)
        """
        if self.overridden:
            return

        if static_url is None:
            static_url = IMPORT_STATIC_PATH
        # TODO Find way to fix the change of name in a better way
        mapped_name = self._name
        if not self.community_version and self._name == "ag-grid-community":
            mapped_name = "ag-grid-enterprise"
        new_js = collections.OrderedDict()
        for v in get_js(IMPORT_PCK_REPO)[self._name]["modules"]:
            if os.path.exists(v['cdnjs']):
                continue

            node_path = v.get("node_path", "")
            if not node_path.endswith("/"):
                node_path += "/"
            new_js["%s/%s/%s%s" % (static_url, mapped_name, node_path, v["script"])] = self.version
        if new_js:
            self._js["main"] = new_js
        if self._css:
            new_css = collections.OrderedDict()
            for v in get_css(IMPORT_PCK_REPO)[self._name]["modules"]:
                if os.path.exists(v['cdnjs']):
                    continue

                node_path = v.get("node_path", "")
                if not node_path.endswith("/"):
                    node_path += "/"
                new_css["%s/%s/%s%s" % (static_url, mapped_name, node_path, v["script"])] = self.version
            if new_css:
                self._css["main"] = new_css
        self.overridden = True

    def set_enterprise(self, version: Optional[str] = None, license_key: Optional[str] = None):
        """Change the package to the enterprise version. This feature will only work for few modules like AGGrid.

        Usage::
          page = pk.Page()
          page.imports.pkgs.ag_grid.set_enterprise()

        :param version: Optional. Set the package version number
        :param license_key: Optional. The license key
        """
        pgks = ("ag-grid-community", 'ag-charts-community')
        if self._name not in pgks:
            raise NotImplementedError("Noting implemented for this package %s, please contact epyk team" % self._name)

        self.community_version = False
        self.page.imports.add(self._name)
        js_resources = get_js(IMPORT_PCK_REPO)
        if self._name == 'ag-charts-community':
            version = version or js_resources[self._name]["enterprise"]
        if self._name == 'ag-grid-community':
            version = version or js_resources['ag-grid-community']["enterprise"]
            update('ag-grid-community', {
                "version": version,
                "register": {"module": "ag-grid-enterprise.min", "npm": "ag-grid-enterprise"},
                "modules": [
                    {
                        'script': 'ag-grid-enterprise.min.js', 'node_path': 'dist/',
                        'path': 'ag-grid-enterprise@%(version)s/dist/',
                        "public": "jsdeliver"},
                    {
                        'script': 'ag-grid.min.css', 'node_path': 'styles/',
                        'path': 'ag-grid-enterprise@%(version)s/styles/',
                        'cdnjs': IMPORT_JSDELIVER_URL}
                ]
            })
            self._js["main"] = {
                "%s/ag-grid-enterprise@%s/dist/ag-grid-enterprise.min.js" % (IMPORT_JSDELIVER_URL, version): version}
            self._js["type"] = {
                "%s/ag-grid-enterprise@%s/dist/ag-grid-enterprise.min.js" % (IMPORT_JSDELIVER_URL, version): 'text/javascript'}
            self._js["dep"] = ["/static\\ag-grid/%s/ag-grid-enterprise.min.js" % version]
            self._js["versions"] = [version]
            self._css["main"] = {
                "%s/ag-grid-enterprise@%s/styles/ag-grid.min.css" % (IMPORT_JSDELIVER_URL, version): version}
            self._css["type"] = {
                "%s/ag-grid-enterprise@%s/styles/ag-grid.min.css" % (IMPORT_JSDELIVER_URL, version): 'text/javascript'}
            self._css["dep"] = ["/static\\ag-grid/%s/styles/ag-theme-alpine.min.css" % version]
            self._css["versions"] = [version]
            if license_key is not None:
                self.page.properties.js.add_text("if(window['agGrid']){agGrid.LicenseManager.setLicenseKey('%s')}" % license_key)

    def set_access_token(self, value: Optional[str] = None, name: str = ""):
        """Set an access token to use this package

        `mapbox <https://docs.mapbox.com/mapbox-gl-js/example/globe/>`_

        Usage::
          page = pk.Page()
          page.imports.pkgs.mapbox.set_access_token("XXXXXX", "mapboxgl.accessToken")

        :param value: Optional. The access token to set to use the library
        :param name: Optional. The access token variable name
        """
        self.page.imports.add(self._name)
        self.page.properties.js.add_text("%s = '%s'" % (name, value))
