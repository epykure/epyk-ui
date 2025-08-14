import logging
from typing import Optional
from epyk.core.py import primitives
from epyk.core.js.imports.registry import get_js, get_css


class Required:
    js, css = None, None

    def __init__(self, page: primitives.PageModel):
        self.js, self.css = {}, {}
        self._page = page

    def add(
            self,
            package: str,
            version: Optional[str] = None,
            verbose: Optional[bool] = None,
            incl_css: bool = True,
            incl_js: bool = True
    ):
        """Add the package to the main page context. TODO: Use the version number

        :param package: The package alias
        :param version: Optional. The package version number
        :param verbose: Optional. Display version details (default True)
        :param incl_css: Optional. Include CSS files
        :param incl_js: Optional. Include Js files
        """
        html_types = set()
        if package in get_js() and incl_js:
            self.js[package] = version or '*'
            self._page.jsImports.add(package)
            html_types.add('js')
        if package in get_css() and incl_css:
            self.css[package] = version or '*'
            self._page.cssImport.add(package)
            html_types.add('css')
        if self._page.ext_packages is not None and package in self._page.ext_packages:
            for mod in self._page.ext_packages[package]['modules']:
                if mod['script'].endswith(".css"):
                    self._page.cssImport.add(package)
                    html_types.add('css')
                elif mod['script'].endswith(".js"):
                    self._page.jsImports.add(package)
                    html_types.add('js')
            if "services" in self._page.ext_packages[package]:
                self._page.cssImport.add(package)
        if not html_types and verbose and package != "other-icons":
            logging.warning("%s - Not defined in neither JS nor CSS configurations" % str(package))
        if version:
            if self._page.imports.setVersion(package, version, verbose=verbose):
                self._page.imports.reload()
