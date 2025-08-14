"""
epyk_export.exe
"""

import os
import sys
import argparse
import time
import traceback

from epyk.core.cli import utils

"""
Section dedicated to the various CLI entry points parsers
"""


def transpile_parser(subparser):
    subparser.set_defaults(func=transpile)
    subparser.add_argument('-n', '--name', help='''The name of the page to be transpiled (without the extension)''')
    subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
    subparser.add_argument('-s', '--split', help='''Y. N flag, Split the files to html, css and js''')
    subparser.add_argument('-o', '--output', help='''The output path''')
    subparser.add_argument('-c', '--colors', help='''The colors to the used for the theme''')


def html_parser(subparser):
    subparser.set_defaults(func=transpile)
    subparser.add_argument(
        '-n', '--name', required=True, help='''The name of the page to be transpiled (without the extension)''')
    subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')
    subparser.add_argument('-split', '--split', default="N", help='''Split the files: -split N''')


def page_parser(subparser):
    subparser.set_defaults(func=page)
    subparser.add_argument('-n', '--name', help='''The name of the page''')
    subparser.add_argument('-p', '--path', help='''The path where the new environment will be created: -p /foo/bar''')



"""
Section dedicated to the various CLI entry points.

Each of then will be linked to a dedicated parser method.
"""


def transpile(args):
    """ Transpile a specific report

    :param name: -p, The path where the new environment will be created: -p /foo/bar
    :param path: -n, The name of the page to be transpiled: -n home.
    :param split: -s, Y / N Flag, to specify if the files should be split input 3 modules.
    :param output: -0. String. Optional. The output destination path.
    :param output: -0. String. Optional. The output destination path.
    :param colors: String. Optional. The list of colors as string commas delimited.
    """
    project_path = args.path or os.getcwd()
    sys.path.append(project_path)
    report_path = utils.get_report_path(project_path, raise_error=False)
    sys.path.append(report_path)
    ui_setting_path = os.path.join(report_path, '..', 'ui_settings.py')
    install_modules, split_files, view_folder, settings = False, False, args.output or 'views', None
    if os.path.exists(ui_setting_path):
        settings = __import__('ui_settings')
        install_modules = settings.INSTALL_MODULES
        split_files = settings.SPLIT_FILES
        view_folder = settings.VIEWS_FOLDER
    if args.split is not None:
        split_files = args.split == "Y"
    views = []
    if args.name is None:
        for v in os.listdir(report_path):
            if v.endswith(".py"):
                views.append(v[:-3])
    else:
        if args.name.endswith(".py"):
            args.name = args.name[:-3]
        views = [args.name]
    for v in views:
        if v == "__init__":
            continue

        try:
            start = time.time()
            mod = __import__(v, fromlist=['object'])
            page = utils.get_page(mod, colors=args.colors)
            if settings is not None:
                page.node_modules(settings.PACKAGE_PATH, alias=settings.SERVER_PACKAGE_URL)
            output = page.outs.html_file(
                path=view_folder, name=v, options={"split": split_files, "css_route": 'css', "js_route": 'js'})
            print("File created in %sms, location: %s" % (round(time.time() - start, 4), output))
        except Exception as err:
            print("Error in file %s.py" % v, err)
            print(traceback.format_exc())


def html(args):
    """ Transpile a specific report.

    :param path: -p, The path where the new environment will be created: -p /foo/bar
    :param name: -n, The name of the page to be transpiled: -n home
    :param split: -split, Y / N Flag to specify if the result should be splitting in several files
    """
    project_path = args.path or os.getcwd()
    sys.path.append(project_path)
    report_path = utils.get_report_path(project_path, raise_error=False)
    sys.path.append(report_path)
    mod = __import__(args.name, fromlist=['object'])
    page = utils.get_page(mod)
    output = page.outs.html_file(path="", name=args.name, options={"split": False})
    print(output)


def page(args):
    """ Create a new page.

    :param args:
    """
    project_path = args.path or os.getcwd()
    if args.name is None:
        i = 0
        dfl_name = "epyk_page_%s.py" % i
        while os.path.exists(os.path.join(project_path, dfl_name)):
            i += 1
            dfl_name = "epyk_page_%s.py" % i
        name = dfl_name
    else:
        name = args.name
    if name.endswith(".py"):
        name = name[:-3]
    with open(os.path.join(project_path, "%s.py" % name), "w") as f:
        f.write('''
import epyk as pk

# Create a basic report object
page = pk.Page()

# the method get_page(page) can be used is the page object is created outside of the script
# This is quite useful with there is a backend to generate the response
# It can allow to start creating the page on the server side and just having to enrich it on the UI
''')
    print("Epyk page created %s" % os.path.join(project_path, "%s.py" % name))


def main():
    """ The main function for all the export CLI entry points. """
    parser_map = {
        'new': (page_parser, '''Create a new page'''),
        'transpile': (transpile_parser, '''Transpile a script to web objects'''),
        'html': (html_parser, '''Fast HTML transpilation'''),
    }
    arg_parser = argparse.ArgumentParser(prog='epyk')
    subparser = arg_parser.add_subparsers(title='Commands', dest='command')
    subparser.required = True
    for func, parser_init in parser_map.items():
        parser_obj = subparser.add_parser(func, help=parser_init[1])
        parser_init[0](parser_obj)
    args = arg_parser.parse_args(sys.argv[1:])
    return args.func(args)
