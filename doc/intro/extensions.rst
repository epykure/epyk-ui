Library extensions
==================

Anything in Epyk can be customized. The style and the final page layout can be fully changed.

Styles & configurations
***********************

Add CSS Inline to a type of components::

  page.ui.components_skin = {
      "title": {"css": {"color": "#A89A37"}},
      "layouts.hr": {"css": {"background-color": "#f0db4f", "margin-bottom": "10px"}},
      "button": {"css": {"background": "#323330", "color": "#f0db4f", "border-color": "#323330"}}}

This will automatically add the a ``TestClass`` to any component button::

  page = pk.Page()
  page.ui.components_skin = {
        "button": {"cls": ["TestClass"]}
  }
  page.ui.button("Test")

Also the framework is using some internal names for the CSS classes based on the internal Python classes.

For example, the below base classes used for button::

  class CssButtonBasic(CssStyle.Style):
      _attrs = {'font-weight': 'bold', 'padding': '2px 20px', 'margin': '2px 0 2px 0', 'text-decoration': 'none',
                'border-radius': '4px', 'white-space': 'nowrap', 'display': 'inline-block', 'line-height': '30px',
                '-webkit-appearance': 'none', '-moz-appearance': 'none'}
      _hover = {'text-decoration': 'none', 'cursor': 'pointer'}
      _focus = {'outline': 0}
      _disabled = {'cursor': 'none'}

will be referenced with the below names in the CSS section::

    .cssbuttonbasic {font-weight: bold ;padding: 2px 20px ;margin: 2px 0 2px 0 ;text-decoration: none ;border-radius: 4px ;white-space: nowrap ;display: inline-block ;line-height: 30px ;-webkit-appearance: none ;-moz-appearance: none ;border: 1px solid #f4f9fc ;color: inherit ;background-color: #FFFFFF ;}
    .cssbuttonbasic:hover {text-decoration: none ;cursor: pointer ;background-color: #f4f9fc !IMPORTANT ;color: #607d8b !IMPORTANT ;border: 1px solid #607d8b !IMPORTANT ;}
    .cssbuttonbasic:focus {outline: 0 ;}
    .cssbuttonbasic:disabled {cursor: none ;background-color: #263238 ;color: #455a64 ;font-style: italic ;}

It is possible to remove or rename this by using shortcut ``rename_css_cls`` as shown below::

    pk.rename_css_cls({"cssbuttonbasic": "cssNewName"})

To get more details on CSS configurations and the way it is managed for components and the pages use the below lines.

.. toctree::
    :maxdepth: 1

    /../guides/extension-component-css.rst
    /../guides/extension-component-derived.rst
    /../guides/extension-component-package.rst
    /../guides/extension-page-skin.rst