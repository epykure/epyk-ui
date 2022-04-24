
from typing import Optional, Union, List
from epyk.core.py import primitives


PROFILE_TYPE = Optional[Union[bool, dict]]
HELPER_TYPE = Union[primitives.HtmlModel, str]
SIZE_TYPE = Union[tuple, int]
JS_FUNCS_TYPES = Union[List[Union[str, primitives.JsDataModel]], str]
