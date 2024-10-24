## [Unreleased]


## [1.11.9] - 2024-01-28

### Added
- Flag to ignore empty string in JavaScript conditions
- New features for rich components
- New shortcut for themes, colors and icons at package level

### Changed
- Changes in the doc string to reduce package footprint.
- Better SCSS export for icons / themes


## [1.11.8] - 2024-01-21

### Added
- More doc and type annotation
- Generic page function to build, refresh or define any components
- verbose to text component
- New JavaScript expression type.
- Align indent in modules.

### Fixed
- Fix bugs for NPM
- Fix bugs in the rest interface.
- remove duplicate internal icons mapping

### Changed
- Changes in the doc string to reduce package footprint.
- Better SCSS export for icons


## [1.11.7] - 2024-01-18

### Added
- New dictionary structure for requirements
- More success helper for REST calls.
- Component generic builder method
- New JavaScript Object / Objects features

### Changed
- Requirement management (CSS / JS filter available)
- Better requirements management for standalone components
- Align indent in modules.
- CSS reg exp parsing.
- Changes in the doc string to reduce package footprint.


## [1.11.6] - 2023-12-17

### Added
- Resources class to access methods from external packages.
- Better management for colors in the CSS
- Add class / pipe concept for Dataflows configuration

### Fixed
- Bug fix with CSS native definition
- Problem with js_code migration for some HTML components

### Changed
- Remove all CSS Python classes for table contents.
- Changes in the doc string to reduce package footprint.
- Align indent in modules.
- Improve features in Standalone components.


## [1.11.4] - 2023-12-11

### Added
- CSS external module (to replace the Python CSS framework)
- New specialized builders for Highcharts.
- Added More Highcharts extensions.

### Changed
- Changes in the doc string to reduce package footprint.
- Align indent in modules.

### Fixed
- Bug fix in chart reference for Frappe, Apex and ChartJs libraries


## [1.11.0] - 2023-12-06

Introduction of native CSS modules.

### Added
- js_code to replace all the different objects used to define Js reference within components.
- Ability to have JavaScript object for js_code.
- container_id used to replace the component reference.
- Add builder concept for Grids.

### Changed
- Replace of htmlCode to html_code in the HTML components (legacy)
- Upgrade SortableJs module
- Changes in the doc string to reduce package footprint.
- Align indent in modules.


## [1.10.42] - 2023-11-26

### Added
- New Charting libraries Chartist and Highcharts.


### Changed
- Changes in the doc string to reduce package footprint.
- Align indent in modules.


## [1.10.40] - 2023-11-17

### Changed
- Changes in the doc string to reduce package footprint.
- Align indent in modules.


## [1.10.38] - 2023-10-30

### Changed
- Changes in the doc string to reduce package footprint.
- Align indent in modules.


## [1.10.0] - 2023-05-02

Introduction of native JavaScript modules (with the standalone module).

### Changed
- Changes in the doc string to reduce package footprint.
- Align indent in modules.

### Added
- Standalone components introduction


## [1.9.32] - 2023-03-19

### Added
- More doc and type annotation
- More examples in functions
- Bootstrap icon library

### Fixed
- Use of different icon framework.

### Changed
- Jquery version


## [1.9.31] - 2023-03-15

### Added
- More doc and type annotation
- More examples in functions
- Add new Js helpers to replace internal builders
- Add css method to ease use of external classes

### Fixed
- Fixes for the icons modules.


## [1.9.30] - 2023-02-26


### Added
- More doc and type annotation
- New Aggrid options
- New ChartJs options
- ChartJs Hierarchy plugin support
- Add version setter for Aggrid enterprise

### Fixed
- Fix issue with import of Aggrid enterprise

### Changed
- Upgrade default community and enterprise version for Aggrid


## [1.9.28] - 2023-02-12

### Added
- More doc and type annotation
- Warning for deprecated modules
- Remote method for heavy tree components
- Add .js property for Accounting
- Add .js property for Moment 
- New method add_to_import for packages not directly used in components

### Fixed
- Problem type with js variable definition (js.getVar)
- Fix migration for ChartJs
- Add more features for datasets
- Align compatibility for plugin
- Fix definition for skillbar components (more options)
- Bug fix for primitive JsDate

### Changed
- Update imports modules
- Update interface for web frameworks (in progress)

## [1.9.27] - 2023-01-30

### Added
- New features for charts and functions alignment
- More type annotation
- New options for Aggrid tables

### Fixed
- Bug fixes for ApexCharts

### Changed
- Review docstrings in functions
- Change stepper HTML component
- Extend internal Js DataClass to pick up JavaScript string automatically
- Change Database module (Mainly bug fixes)

## [1.9.21] - 2022-11-30

### Added
- Added documentation and type annotation
- New functions for underlying modules (Tabulator, ChartJs and AgGrid)
- New features for the Tree component.
- New standard features - active() and selection() dom (in progress)

### Fixed
- Fixed issues with REST 


## [1.9.12] - 2022-10-22

### Added
- Add components section in documentation
- Add JqueryUI varId property
- New features for Textarea
- More autocomplete features for Input

### Changed
- Change documentation in docstring
- Change slider default behaviour for output display
- Change type annotation
- Documentation reformatting


## [1.9.9] - 2022-09-25

### Added
- Add new icons
- Add more Jquery features for DOM object

### Changed
- Review Readme and documentation
- internal picture use (loaded from base64 string directly)
- Dev icons

### Fixed
- Fix Jquery shortcut
- Bug fix for Collab


## [1.9.7] - 2022-09-19

### Added
- New features for URL definition.
- Add extra AgGrid options.
- Extra CSS common properties

### Changed
- Functions documentation
- Some static types features

### Fixed

## [1.9.5] - 2022-08-21

### Added
- New features for Tabulator and Aggrid.
- new schema definition for component to allow definition from json configuration

### Changed
- Documentation and types definition.
- Aggrid default style.
- Align Tables components with common features.

### Fixed
- standalone mode for imports
- Remove configuration table component


## [1.9.2] - 2022-08-17

### Fixed
 - Bug fixes


## [1.9.0] - 2022-08-17

### Added
 - Mapbox as a dedicated charting library for Geo charts
 - Add New import features in the JavaScript internal import manager
 - Externalise the Icon modules to allow flexibility for web framework (v1)
 - Add queueMicrotasks
 - Add encoding features in options for text components

### Changed
 - Upgrade to new version of modules for Tabulator
 - Change input fields and encoding features
 - Add keep_attr to maintain CSS attributes in HTML components

### Fixed
 - Add more documentation and autocompletion features 
 - Small bug fixes on components


## [1.8.0] - 2022-07-03

### Added
 - new argument data_ref to change the javascript data variable
 - More types annotations
 - More documentation
 - Introduce _ property to get core modules from Js object
 
### Fixed
- Few bugs in modules for class definition


## [1.7.25] - 2022-06-26

### Added
- More documentation
- Add more type hints

### Changed
- Type argument name to category

### Fixed
- Menu issues

## [1.7.24] - 2022-06-16

### Added
- More documentation
- New tabulator features
- menu specific items for hierarchy tables

### Changed
- Tabulator style

### Fixed
- Fix nested enum in component options.
- add_event typo for js bindings


## [1.7.21] - 2022-06-12

### Added
- Add new Tabulator features
- Improve type hints and documentation
- New stringify for html components

### Fixed
- Bug fixes with dataclasses and Options


## [1.7.19] - 2022-05-30

### Added
- Add all REST keywords for calls.
- Function documentation

### Fixed
- Minor bug fixes
- Align types
- Improve autocompletion


## [1.7.15] - 2022-04-24

### Added
- Add IntersectionObserver
- Add js.delay
- New network components for impressions and votes
- internal types module to define complex ones.

### Fixed
- Improve documentation
- Better type hintings


## [1.7.14] - 2022-04-10

### Added
- Add pk.symbols shortcuts.
- Add dom focus feature.

### Changed
- Change popup to add tabIndex on inner window.
- Change Columns menu's closure for Tables.
- Change sub title style for menu.

### Fixed
- Bugfix on closure for popup.
- Improve types and documentation.


## [1.7.12] - 2022-04-07

### Added
- Change ColorRange to be iterable and subscriptable
- Add new List type - timeline.
- Add new dom functions for list of dynamic items.
- Create types.py for internal types.

### Changed
- Change message status behaviour for empty messages.
- Documentation & type hints

### Fixed
- Fix external Tabulator Formattor / Editor
- Fix issue with Update object.

## [1.7.11] - 2022-04-04

### Added
- New chartJs features / plugins.
- Add tabulator column formatter.
- Wrap new tabulator options.
- Add CSS formatter for tabulator columns.

### Changed
- Add more flexibility to change the loading component.
- Change the secondary colors definition.

### Fixed
- Better documentation & type hinting.
- Bug fix on loading Tabulator extensions.

## [1.7.9] - 2022-03-26

### Added
- New features for the table menu with column filtering.
- Add filename for the json configuration (template mode).
- Add js features for popup components.
- Add no_tag component to .tags property.
- Add new pyks components (Gauge and Circular progress bar).

### Changed
- Improve color conversion for the dark mode.

### Fixed
- Some bugs on colors.
- Missing documentation or examples.
- Fix list checks component.


## [1.7.8] - 2022-03-21

### Added
- Add new icon aliases for components.
- Add insert method for any HTML component.
- Add new features for the tree component.
- Add filter_on options for tree.
- Add isJsData features in the JsUtils toolbox.
- Add new parameters to the icons.
- New more component in Navigations.

### Changed
- Change icon default style for buttons.
- Change number of digits for percent component.

### Fixed
- Fix margin_h CSS property.
- Fix options when JavaScript object added.
- Fix Tabulator type hints.


## [1.7.6] - 2022-03-13

### Added
- Add enter shortcut to textarea
- Add readonly dom shortcut property for textarea
- Add add_command function to the menu component to add more icons.
- Add mouse loading animation.
- Add JavaScript samples module.

### Changed
- Extend menu component to accept list of components.
- Change color module to allow the transparentize and transparentize_all functions.
- Documentation and examples.
- Version of ChartJs to the latest.
- [ChartJs] change new_dataset and add_dataset to accept any optional parameters.
- [ChartJs] Change option to allow the data definition from a dict.
- Change page.ui.texts.references.website component default style.

### Fixed
- Documentation and Types definition.
- [ChartJs] Add new options for the various charts.
- [ChartJs] Fix on the load js wrapper for Pie and Polar charts.
- Fix margin_h shortcut CSS property with components with width in %.

## [1.7.4] - 2022-03-04

### Added
- New module for loading animations.
- Add auto option to the menu (test).
- Add run_on_start option for setInterval function.
- Bug fixes on the type definition.

### Changed
- Changes in the menu wrapper for components.
- Change the badge component with better JavaScript integration.
- Minor changes on the style of few components.

### Fixed
- Fix the update component.
- Fix badge display.


## [1.7.3] - 2022-03-04

### Added
- Add get to retrieve custom Aria.
- Show percentage in JqueryUI progressBar component.
- Add network logs interactive component.
- Add timelines issues interactive component.

### Changed
- Improve way width and height are defined to accept string with unit.
- No change menu by default for the status component.
- Input for title and accept dictionaries.

### Fixed
- Fix chartJs color definition.
- Improve way fixed columns width are defined with row & grid components.
- Bugfix in JavaScript input text components.
- Improve the menu wrapper for components.


## [1.7.2] - 2022-02-23

### Added
- Documentation.
- testing framework.
- mocks module to test without data.

### Changed
- varName argument and property replaced to js_code.
- HtmlCode replaced by html_code.
- Remove generic attribute ._src and replaced by component and page.
- jsData, jsValue replaced by data and value.
- jsId, varId, varName replaced by js_code.
- jsFnc replaced by js_funcs.

### Fixed
- propagate correctly both component and page in page components.


## [1.7.1] - 2022-01-22

### Fixed
- Type annotation issue with python 3.6


## [1.7.0] - 2022-01-22

### Added
- Type annotation in most of the modules.
- Speech recognition module.
- new primitive module to allow static typing.

### Changed
- Remove compatibility with python 2.7
- [in progress] standardise the use of _ in the function arguments

### Fixed
- Autocompletion issue with decorator
- Fix self contained feature for JavaScript modules.
- Improve documentation 


## [1.6.17] - 2021-12-06

### Added
- Add bottomCalc / topCalc to tabulator wrapper.
- Add addTreeChildren event.
- Link external lib interface.
- Add object format function.

### Changed
- review common component export function

### Fixed
- Tabulator formatter definition.
- Issue in Tabulator hierarchy tables.
- Bug fix in the import manager.


## [1.6.10] - 2021-11-18

### Fixed
- Plotly wrapper enhancements
- Bug fix in NVD3 date conversion
- Bug fix in NVD£ candle chart
- Review Tabulator hierarchy tables (bug https://github.com/olifolkerd/tabulator/issues/3271)


## [1.6.7] - 2021-11-01

### Fixed
Few bug fixes and improvements.


## [1.6.6] - 2021-10-29

### Fixed
Few bug fixes and improvements.


## [1.6.5] - 2021-10-21

### Added
- Add popular pyks components from Epyk Studio.
- Add more icons to the transversal configuration.

### Changed
- Change way color is managed for Buttons.

### Fixed
- Fix Plotly and some features in Tabulator wrappers.

## [1.6.4] - 2021-10-21

### Added
- Popper package upgrade.
- Change Div container tag.
- Extra DOM functions
- First version for the integration of the external frameworks Fluent UI, Toast UI, BootStrap and Material UI

### Changed
- Improve BS components.
- New Icon setup to allow different Icon families.


## [1.6.3] - 2021-09-12

### Added
- Integrate Moment library to the ase Javascript features.
- Improve overall framework documentation.
- Add packages white / black lists shortcuts.
- Add defer, async property for external packages.
- add_style function to all components.

### Changed
- Improved Bootstrap 5 integration.
- DOM object for basic tables.

### Fixed
- Fix Bootstrap reference in Image component.
- Bug fix in the Option base class.


## [1.6.2] - 2021-09-05

### Fixed
- Bug fix for Python 3.7.


## [1.6.1] - 2021-09-05

### Added
- Better integration of the Bootstrap CSS classes.
- Jquery UI shortcut in the Web frameworks.

### Changed

### Fixed
- Fix header duplicated stylesheets in the HTML page.


## [1.6.0] - 2021-09-02

### Added
- Toast Framework (first version).
- Add Toast DatePicker.
- Add Toast Editor.
- Add Toast Calendar.
- Add Toast Charts.
- Add Toast Grid.
- Add option for C3 y transformation.
- Add column style for fields.
- Add Bootstrap Dominus Tempus.
- Add Component class for Framework integration.
- UI - Add new list item period.
- Add size and width cols options for row container.
- Add check / radio events.

### Changed
- Bootstrap Framework (first version using v5).
- Change config predefined styles.
- Change button style (default height).
- Improve data transformation for x, y and r charts (bubble ones) .
- Add scroll option to the navbar to hide it when scroll down.
- Change color management in titles.

### Fixed
- Fix ImportManager CSS package version override.
- Fix axes label for ChartJs.
- Import manager for extensions.
- Review builder for Countdown component.


## [1.5.25] - 2021-08-03

### Fixed
- Pivot data transformation bug fix.
- Slider event bug fixes.


## [1.5.24] - 2021-08-03

### Added
- Add select button style definition.
- doc in the datapy shortcuts.
- Add component argument to the paste function.
- Improve slider and range slider display.
- Add composite setbuilder method.
- Improve network dropfile component.
- Add field component slider and filter.
- Add List component filter.
- Add Toast packages.
= Add HTML pages external configuration.
- Add Panel js features.
- Add Jupyter structure for widgets (Draft)

### Changed
- Label Rich dom definition.
- New parameter for line-height to CSS middle function.
- Change multi selectPicker icon base default.
- Tabulator add layouts options.
- Add options to the JavaScript pivot function.
- Set font size in the nav bar.
- Migration from _report to page property.

### Fixed
- CHartJs donut charts.
- DataPy str conversion from list for select input component.
- NVD3 colors function for all charts.
- Doc link bug fixes for autocompletion.
- Fix selected CSS style conflicts.
- Bug fixes in the Import manager for extensions.


## [1.5.23] - 2021-07-05

### Added
- Add new entry for packages to the __init__
- Improve Options with an Enums which can be extended thanks to _add_value.
- new class variable for the Enums delimiter and js_conversion to always consider values as Js.
- Create Options modules for Tables libraries.
- Migration of the Tabulator and DataTable extension to the Options framework.
- Add hot_imports to the js function to load JavaScript module from an event._
- Apex charts add activePoints.
- Create NVD3 dedicated options module.
- Add packages definition in Imports.py

### Changed
- ChartJs's options migrated to the standard framework,
- Migration of ChartJs extensions to the Options framework
- Improve modules documentation for options.
- Change ChartJs function to align with ChartJs v3.

### Fixed
- Bug fix in data transformation from Charts.
- Fix C3 and Billboards options.


## [1.5.22] - 2021-06-21

### Added
- New vega chart libs.
- Add leaflet event object.
- Add SVG style properties to CssInline.
- Add __str__ method to options objects.
- Add charts categories.
- Add default chart family to Apex Charts.
- Create Enum class.
- Add first implementation of Vega Lite charts wrapper.
- Add req_js entry in Imports for requireJs.

### Changed
- Change default padding for C3 and billboard.
- Clean up billboard module.
- Change register keywords in Imports new variable one.
- Improve leaflet.

### Fixed
- Bug fix for D3 word cloud init func.
- bug fix end range color function.
- Fix issue with requireJs links
- Add SVG underlying for ApexCharts (to be confirmed).


## [1.5.21] - 2021-06-09

### Added
- Add JavaScript Fetch API.
- Add Logging service with page.js.console.service.
- Add POST and GET async flag.
- Add width to base charts options.
- Add concept of cell for outs.jupyter().
- Add new Jupyter apps features (draft).
- Add play and stop icons shortcuts.
- Add depth for JavaScript variable serialisation.
- Improve D3 charts interface with more entries.
- Geo charts: Add Colors and predefined Palettes.
- Geo charts: Add leaflet map (in progress)
- Geo charts: Add D3

### Changed
- New youtube component.
- Add try except to the pyNpm package.
- Change name js_wrap to js_callback.
- Improve the JQVMap interface with more options.
- Add chart container for the chartJs charts.

### Fixed
- QRCode Jupyter style (padding issue).
- Align media options.
- Register more modules to Imports.py for Jupyter.
- Fix D3 charts.
- Upgrade ChartJs version (and backward compatibility with the function set_version()). (in progress)

## [1.5.20] - 2021-05-29

### Added
- Options to display matplotlib figures.
- Add bugs and todo section in the doc.
- Add skillbar options.
- Add skillbar javascript events.
- Add headers argument to js.post and js.get.
- Add progressbar add js function.
- Add outs options for Jupyter.
- first version of the page.apps.juputer extension.


### Changed
- Change text builder filter.
- Jupyter HTML template for cells.
- Extend div operator for contentFormatters.
- Update DC charts.
- Add list to Python Markdown module.

### Fixed
- Bug fixes for NVD3, C3 and DC in Jupyter.
- Fix mathJax display for Jupyter.
- Fix use of !IMPORTANT in CSS property setters.
- Fix Jqv Map display property.
- Bug fix on the use of the get method for options.
- Fix pivotTable.


## [1.5.19] - 2021-05-22

### Added
- Add gallery for images and icons
- Add option for colors to the transpile CLIs.
- Add shortcut to change the OVERRIDES method in the CSS Classes module.
- Add new pk. method links.
- Introduce the async option for builders (for potential promise)

### Changed
- Improve documentation.
- Input background default color.
- Adjust skins background position.
- Remove the dependency on Jquery UI for Jquery TimePicker.
- Change the content of field.number to return a float.

### Fixed
- Fix bug on some predefined icons.
- Fix effects.
- Fix Plotly data processing on Python.
- Fix the TimePicker object.
- Fix to make web workers available in Jupyter.
- Fix data input for Histogram for Plotly.


## [1.5.18] - 2021-05-14

### Added
- Documentation sections.
- Add Frappe Charts.
- Add ChartCss.

### Changed
- Online documentation
- Structure and documentation for the CLI.

### Fixed
- Some CLI entry points.
- Improve wrapper to RoughViz.
- Fix NPM CLI.


## [1.5.17] - 2021-05-09

### Added
- from_plot() to the image and animated image components to load from a plot object.
- from_base64() to load 
- add from_plots to carousel, tiny slider
- Add tiny slider pre defined styles.
- Add output path option to the transpile CLI.
- Add 3 new Charting libraries.
- Add inline() css shortcut for display = inline-block
- Add page.apps.jupyter to get information related to the Jupyter instance (new web/jupyter.py module).

### Changed
- Add stacktrace in transpile error.
- Change tranpile and add -o for destination folder.
- Some improvements on a few CSS style.

### Fixed
- Fix style for tiny slider.
- Bug fixes for Billboard and C3.
- Fix input range field style.
- Fix height definition in the Code component.
- Fix Imports module to work with Jupyter.
- Bug fixes in the Jquery wrapper.


## [1.5.16] - 2021-05-02

### Added
- Add Read the docs documentation first version.
- Add CLI commands for demo and new page.
- Add Tabs getitems feature.
- Common charts shortcuts.
- Add Epyk settings shortcut for Chart and Table default families.


### Changed
- Review docstrings in the framework.
- Move Tabulator configs to options to align with other components.
- Stepper default width auto.
- Add comment to the deprecated decorator.

### Fixed
- Fix steppers features.
- Fix JsDom firstchild, parentNode reference.
- Add JsDom events.
- Fix button toggle underlying input access.
- Review Tabulator CSS classes.


## [1.5.15] - 2021-04-24

### Added

- Add the shortcut properties margin_h, margin_v, padding_h, padding_h
- Add the CssLine to CssClass conversion.
- Add the style.clear_class() method.
- Add the important method to CSSInline object.
- Add leave function to the input component to map the onBlur event.

### Changed

- Change the nav interface argument with components.
- Change the Autocomplete style and add the borders property.
- Change JsHtml content function to return string from Markdown.

### Fixed
- Fix update component.
- Link Update component to the JsHtmlRich dom definition.
- Link Markdown component to the JsHtmlRich dom definition.
- Minor fix on some JsSelect features.


## [1.5.14] - 2021-04-21

### Added
- Add CSS Inline shortcut.
- Add body.template property to easy the configuration.
- Add pulse icon dom event.
- Add new button refresh.
- Add borders option for Input components.
- Add style.shadows various flavours.
- Add profile to post request (first version).

### Changed
- Components minor still improvements.

### Fixed
- Components documentation.
- Fix icon.date and remove the input text.
- Fix Markdown display  in Console component.


## [1.5.13] - 2021-04-18

### Added
- DatePicker component option.
- String primitive functions padStart, padEnd...
- Component texts.date
- interface cob entry point.
- New components class in the base HTML class.

### Changed
- Button colored padding.
- SelectPicker dom content value.
- Tabulator wrapper Documentation.
- Some improvements in the documentation formatting.
- Align interface builder attributes.

### Fixed
- Bug fix datePicker JavaScript Options.
- Tabulator tree management.
- Fix shortcut bar components management
- Fix icon CSS color management.


## [1.5.12] - 2021-04-16

### Added
- Add gradient_text function to CSS properties.
- Add rotate function to CSS properties.
- Add margins shortcut for template configs.
- Add width parameter for the powered by component.
- Add dark mode to color themes.
- Introduce position to div
- Add options for navigation points.

### Changed
- Add the template attribute for the body component to the __init__.
- Change the parameters for div and introduce the position to align with row.
- Change some icons component styles.

### Fixed
- Change color for hover on button icons.
- Add the start event for the countdown component.
- Consider the template of the body for navigation components (side panels)
- Bug fix for the texts.button component.
- Fix options for Images and Carousels.
- Fix html_code issue for content tables in text components.


## [1.5.11] - 2021-04-11

### Added
- Add plot shortcut with kind to align with matplotlib.
- Add plot function to the base property charts to switch chart families.
- Add slider javascript functions.
- Add hamburger Icon.
- Add hamburger Panel.
- New slider max and min component for range.
- Introduce Charts google options module.
- Create a palette internal module to manage color changes for charts.

### Changed
- Change records name to record in all charts.
- Change slider style.
- Remove label from core switch component. 
- Set code from texts as readonly.
- Full revamping of C3 and Billboard options management.

### Fixed
- Fix data transformation for scatter charts (with distinct agg)
- Fix color definition for charts. Always rely on theme.charts list.
- FIx bug when using page.imports.google_products(['charts']) without google packages.
- Fix the way slider ranges are handled.
- Improve way columns and data are defaulted for charts interfaces.


## [1.5.10] - 2021-04-07

### Added
- Add ek shortcut for Page and events.

### Changed

### Fixed
- Fix chartsJs tooltips.
- Fix chartsJs Scatter


## [1.5.9] - 2021-04-05

### Added
- Add input number styles.
- Add fields.number interface.
- Add XMLHttpRequest timeout.
- Add data apexCharts shortcut for events.
- Add new input data in data_urls (owid repo)
- Add trigger shortcut to dom property.
- Add Poller components.
- Add CSS calc for width.
- Add more and filter button.
- Add Github standard text reference component.
- New Apex Gauge component.

### Changed
- Change button live style.
- Change Rich, Vignets and number interfaces.
- Change data default values for Sparkline interfaces.
- Add nowrap style to list of links.
- Include the color reference for the standard color names in charts.
- Fix toMoney formatter for ApexCharts (to be done for other charts).

### Fixed
- Link builder function.
- Extensible search class width.
- List tag position.
- Fix jqueryui dependency with popperjs.
- Handle not checked state for radio.
- Height for the chart.
- Update ApexChart package version.


## [1.5.8] - 2021-03-28

### Added
- New CSS Style configs with predefined CSS inline configurations.
- Add a themes property to change the themes with auto completion.
- Add Index and step to be able to create custom themes from the available ones.
- Add predefined CSS classes overrides.
- Add white and black themes properties.
- Introduce first version of skins for websites.
- data ListItems (first version).

### Changed
- Default behaviour for icons application links.
- Rename module GrpChart to GrpClsChart to follow the naming convention.
- Use of notch to get the main color used instead of an index in the CSS predefined classes.
- Remove Default.font() function from css.

### Fixed
- Fix the Input options.
- Remove the use of the static default CSS module for sizes.
- Review all the existing themes.
- Centralise the charts colors codes for themes.
- Create dark mode and align grey color codes.


## [1.5.7] - 2021-03-19

### Added

- Add standard menu bar for HTML components 
- Add the options to get all the components in powered.
- Add standard function for copy, download and clear.
- Add url JavaScript attribute.
- Add options in the Item list add() method.
- Add getUrlFromData() method in the Js core module to convert variable to url.
- Add URL property to window JS core module.
- Add Stringify function for objects.
- Add predefined fixed icon component.
- Add predefined left input component.
- Add align argument to formula component.

### Changed

- Change color allocation for powered by component.
- Change List menu component.

### Fixed

- Fix ChartJs builder function names.
- Fix context menu for Lists.
- Fix add JavaScript function for Items list.


## [1.5.6] - 2021-03-16

### Added

- Add better management of the Interfaces skins
- Add min-height to the Highlight component
- Add is_true options to the automatic import manager

### Changed

- Change icon colors for input fields.

### Fixed

- Fix slider component.
- Align slider with the new options model.
- fix external JavaScript text injection.


## [1.5.5] - 2021-03-15

### Added

- Markdown Python conversion function.

### Changed

- markdown all check.

### Fixed

- Highlights builder improvement.
- Highlights Options definition.
- Fix the CSS style of the print component.

## [1.5.4] - 2021-03-15

### Added

- Icons menu.
- Add Bootstrap icon family from standard components.
- Add paragraph as an Interface shortcut.
- Add Texts menu.
- Add Items lists menu.
- Add copyToClipboard DOM shortcut to components.

### Changed

- ChartJs JavaScript data() interface => align with build method.
- ChartJs common series attributes.
- Changed the Paragraph Markdown display

### Fixed

- Fixed PivotTableJs component renderers.
- Fixed Icon family use.
- Fixed color for content editable.

## [1.5.3] - 2021-03-12

### Changed

- Improved ChartJsGeo interface.

### Fixed

- Fixed webworkers integration from Flask.
