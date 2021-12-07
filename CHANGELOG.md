## [Unreleased]

### Added

### Changed

### Fixed

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
