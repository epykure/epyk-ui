from typing import Dict


# Global name on the JavaScript side
EXPORT_INIT_OPTIONS = "INIT_OPTIONS"


def set_global_options(builders: Dict[str, str], init_options: Dict[str, str]):
    """
    Set the global scope for all components in the reports.
    This will be used when building the report in a static manner.

    :param builders: Common object with all components builders definition
    :param init_options: Common object with all the components init options
    """
    js_builders = []
    for c, d in builders.items():
        if d is not None:
            js_frgs = []
            for l in d.split("\n"):
                js_frgs.append(l.strip())
            js_builders.append("".join(js_frgs))
    str_options = ["%s:%s" % (k, v) for k, v in init_options.items()]
    return "%s;%s={%s}" % (";".join(js_builders), EXPORT_INIT_OPTIONS, ",".join(str_options))
