Component style
===============

Any component in Epyk can be fully changed and the style can be entirely updated.
First to mention that everything done in this library has been achieved thanks to the good quality of the tutorials in `w3schools <https://www.w3schools.com/>`_

By default, all the components come with predefined CSS styles and CSS classes.
Usually the CSS properties are set in the component functions available in the Interface section.

For example for the ``page.ui.buttons.colored``::

    @html.Html.css_skin()
      def colored(self, text="", icon=None, color=None, width=(None, "%"), height=(None, "px"), align="left",
                  html_code=None, tooltip=None, profile=None, options=None):

        component = self.button(text, icon, width, height, align, html_code, tooltip, profile, options)
        component.style.css.background = color or self.page.theme.colors[-1]
        component.style.css.border = "1px solid %s" % (color or self.page.theme.colors[-1])
        component.style.css.color = self.page.theme.colors[0]
        component.style.css.margin_top = 5
        component.style.css.margin_bottom = 5
        component.style.css.padding_left = 10
        component.style.css.padding_right = 10
        return component

All CSS inline properties are available in any components from the ``component.style.css`` property

Using CSS inline
****************

The above example can be changed by using the below lines of code for example to make it fixed to the page::

    button = page.ui.buttons.colored("Test")
    button.style.css.color = "yellow" # Change the text color
    button.style.css.position = "fixed"
    button.style.css.bottom = 10 # Default will use px
    button.style.css.right = 10 # Default will use px

This will then render the page the HTML tag::

    <button data-count="0" id="button_2561249251968" style="font-size:14px;margin:0;padding:0px;padding-left:10px;padding-right:10px;line-height:23px;background:#263238;border:1px solid #263238;color:yellow;margin-top:5px;margin-bottom:5px;position:fixed;bottom:0px;right:0px" class="cssbuttonbasic">Test</button>


Using CSS Inline object
***********************

If it possible to do the same thing by using the CssInline shortcut::

    import epyk as pk

    inline = pk.CssInline()
    inline.color = "yellow"
    inline.position = "fixed"
    inline.bottom = 0
    inline.right = 0

    page = pk.Page()

    button = page.ui.buttons.colored("Test")
    button.css(inline.to_dict())


Using CSS classes
*****************

It is also possible to move away from inline and to use CSS classes instead.
CSS classes from a CSSInline object can be done::

    inline = pk.CssInline()
    inline.background_color = "yellow"
    inline.position = "fixed"
    inline.bottom = 0
    inline.right = 0
    inline.important(["background_color"])

    myClass = inline.to_class("MyClass")

    page = pk.Page()

    button = page.ui.buttons.colored("Test")
    button.style.classList['main'].add(myClass)

It is also possible to create an internal CSS class using the below. In this example if it possible to add more information
to the CSS class as it is generated from a inline structure::

    from epyk.core.css.styles.classes import CssStyle

    class CssHoverColor(CssStyle.Style):
      _attrs = {'color': 'blue', 'cursor': 'pointer'}
      _hover = {'color': 'orange'}

    div1 = page.ui.div("This is a text")
    # Attach the class to the component
    div1.style.add_classes.custom(CssHoverColor)


Using external CSS
************************

In order to facilitation the use of external data Epyk has multiple ways to integrate external styles.

From text
_________

It is also possible to add a bespoke CSS text manually and then to add your CSS class to the component::

    page.properties.css.add_text('''
    .MyClass {
        ...
    }
    ''')

    button = page.ui.buttons.colored("Test")
    button.attr["class"].add("MyClass")

From file
_________

But is can also be done using a CSS file. This time it is required to register the file::

    page.css.customFile("animate.min.css", path="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2")

    button = page.ui.buttons.colored("Test")
    button.attr["class"].add("MyClass")

.. note::
    Do not forget that Epyk is a collaborative library so do not hesitate to share your improvements to ensure
    other people will benefit from your knowledge.
