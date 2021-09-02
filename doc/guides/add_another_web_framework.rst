How to add another web framework
================================

It is easy to create a bespoke interface for any external package.
The package will have to follow the below rules in order to be easily added to the code package.

.. note::
    A future implementation will allow the framework extensions to be installed using the ``epyk install`` command line.

Package structure
-----------------

Two file will be needed ``PkgImports.py`` and ``UI.py``. Those two files will respectively defined the external modules to be
attached to the package and the python interface for the external package.

For example in order to integrate the Bootstrap components to the framewor, in PkgImports.py::

    BOOTSTRAP = {
      'tempusdominus-bootstrap-4': {
        'version': '5.39.0',
        'req': [
          {'alias': 'font-awesome'},
          {'alias': 'bootstrap'},
          {'alias': 'moment'},
          {'alias': 'jquery'}],
        'website': 'https://getdatepicker.com/5-4/Installing/',
        'register': {'alias': 'datetimepicker', 'module': 'bootstrap-datetimepicker.min', 'npm': 'datetimepicker'},
        'modules': [
          {'script': 'tempusdominus-bootstrap-4.min.js', 'path': 'tempusdominus-bootstrap-4/%(version)s/js/'},
          {'script': 'tempusdominus-bootstrap-4.min.css', 'path': 'tempusdominus-bootstrap-4/%(version)s/css/'},
        ]},
    }

And then in UI.py, you can find the definition of the API with the documentation::

    class Components:

      def __init__(self, page):
        self.page = page
        if self.page.ext_packages is None:
          self.page.ext_packages = {}
        self.page.ext_packages.update(PkgImports.BOOTSTRAP)
        self.page.imports.pkgs.bootstrap.version = "5.1.0"
        self.page.jsImports.add("bootstrap")
        self.page.cssImport.add("bootstrap")

      def check(self, flag=False, width=(None, "px"), height=(None, "px"), label=None, html_code=None, profile=None,
                options=None):

        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        html_but = HtmlBsForms.BsCheck(
          self.page, {"checked": flag, "label": label or "", "type": "checkbox"}, html_code, options or {}, profile,
          {"width": width, "height": height})
        return html_but

..note::
    As a general rule the definition of the interface is close to the one defined for the standard core components in order
    to easy the migration. Indeed to move to from a core chart module to the one defined in TOAST ui the change is relatively
    simple::

        #from
        page.ui.chart.pie()

        # to
        page.web.tui.chart.pie()

Core Integration
----------------

Once the package is correctly structure all components can be derived from the base class ``Component`` in ``epyk.core.html.Html``.
Then it is possible to add to this subclass some Js, DOM and Options properties to make it behave the expected way.

For example the Bootstrap Select interface is quite well defined and the options, js features are based on the original component
definition::

    class BsCheck(Component):
      css_classes = ["form-check-input"]
      name = "Bootstrap Check"
      _option_cls = OptBsForms.Check

      str_repr = '''
    <div class="{container_class}">
      <input type="{type}" value="" {attrs}>
      <label class="form-check-label" for="{for}">{text}</label>
    </div>'''

      def write_values(self):
        if self._vals['checked']:
          self.attr["checked"] = None
        if self.options.disabled:
          self.attr["disabled"] = None

        return {"container_class": " ".join(self.options.container_class), "text": self._vals['label'],
                "for": self.htmlCode, "type": self._vals['type']}

      @property
      def dom(self):
        """
        Description:
        -----------
        The common DOM properties.

        :rtype: DomBsForms.DomCheck
        """
        if self._dom is None:
          self._dom = DomBsForms.DomCheck(self, report=self.page)
        return self._dom

      @property
      def options(self):
        """
        Description:
        -----------
        The component options.

        :rtype: OptBsForms.Check
        """
        return super().options

