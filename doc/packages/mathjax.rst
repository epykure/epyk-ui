Mathjax
=======

- Documentation: https://www.mathjax.org
- NPM alias: ``mathjax``
- Package Type: JavaScript


---------------------

The package **mathjax** is available in the framework by using the following component::

   formulas = page.ui.texts.formula("$$ E=mc^2 $$", helper="This is a formula")

The above will display a maths formulas. More details available on the website: https://www.mathjax.org
The content is expecting a LaTeX format.

Style
*****

This component will have some predefined CSS class in order to change the nav bar and the button but it is possible
as any other component to change the style by using the ``style.css`` property.

The below will add a border to the component::

    formulas.style.css.color = "green"
