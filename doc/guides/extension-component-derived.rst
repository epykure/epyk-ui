Derived component
=================

The notion of derived component or configuration is heavily used in the framework to provide multiple predefined
options to the user.

Thus instead of always using a standard button and then having to update the style every time::

    class Buttons:

        def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):

            ...

        def large(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
            tooltip=None, profile=None, options=None):
            ...


        def normal(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", html_code=None,
             tooltip=None, profile=None, options=None):
            ...

        def run(self, text="", width=(None, "%"), height=(None, "px"), align="left", html_code=None, tooltip=None,
          profile=None, options=None):

Those configurations are coming from bespoke CSS style which have been added as shortcut to assist the creation of
rich web page. This can be seen as a toolbox with shortcut to help the web development.

As a general rule derived component have always the same signature to make easy the migration from one to another within the
same component category.

.. note::
    Do not hesitate to propose your configuration to be added as derived components to the framework.
