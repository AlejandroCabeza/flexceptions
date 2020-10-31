# Python Imports
from json import dumps as json_dumps
# Third-Party Imports
# Project Imports
from exceptions.base_exceptions import BaseTransformableException


def json_dumps_transform_handler(transformable_exception: BaseTransformableException) -> str:
    return json_dumps(transformable_exception.__dict__)
