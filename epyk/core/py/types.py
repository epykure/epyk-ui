
import datetime
from typing import Optional, Union, List
from epyk.core.py import primitives


PROFILE_TYPE = Optional[Union[bool, dict]]
HELPER_TYPE = Union[primitives.HtmlModel, str]
SIZE_TYPE = Optional[Union[tuple, int, str]]

JS_FUNCS_TYPES = Union[List[Union[str, primitives.JsDataModel]], str, dict]
JS_DATA_TYPES = Union[str, primitives.JsDataModel, float, dict, list, bool]
JS_DATA_BOOLEAN_TYPES = Union[bool, primitives.JsDataModel]
JS_EXPR_TYPES = Union[str, primitives.JsDataModel]

DATE_TYPES = Union[datetime.datetime, str]
OPTION_TYPE = Optional[Union[dict, bool]]
