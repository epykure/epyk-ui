Bugs & ToDo
===========

For the ones interested in participating there is a list of improvements to be done to the framework.
Those bugs are all defined in the code and they are either known bugs or extensions which need to be added.

Style
_____

Global CSS
**********

- Extend the ``.globals`` in **GrpCls.py** property to update more than the font and few properties.
- Improve ``custom_class`` in **GrpCls.py** to propagate the important attribute
- Improve way colors are defined for Charts in **Theme.py**.


Data
_____

- Create a dedicated data core package with the input data definition for the components.
- Full revamping of the module PyMarkdown.py.

JavaScript
__________

Obviously some work is still needed to fully wrap all the external packages.
There are some but do not hesitate to add more issues there: https://github.com/epykure/epyk-ui/issues, we will try to tackle them)

Packages
________

PivotTable
**********

- Fix the column initial selections for custom aggregators.

Sparklines
**********

- Fix display tooltips in Jupyter
- Add event and tooltip style
