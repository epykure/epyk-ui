from typing import Optional
from pathlib import Path
import configparser


def config_file() -> Optional[Path]:
    """ Get the configuration file if it exists """
    config_file = Path.cwd() / "epyk.ini"
    if config_file.exists():
        return config_file

    home = Path.home()
    config_file = home / ".epyk" / "epyk.ini"
    if config_file:
        return config_file


def get_config() -> dict:
    """ Return the init configuration """
    c_file = config_file
    config_options = {}
    if c_file:
        config = configparser.ConfigParser()
        config.read(str(config_file))
        config_options["extension"] = config.get("general", "extension", fallback=None)
    return config_options
