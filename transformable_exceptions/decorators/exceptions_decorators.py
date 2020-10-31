# Python Imports
from typing import Callable, Optional
# Third-Party Imports
# Project Imports
from exceptions.base_exceptions import BaseTransformableException
from handlers.handlers_typing import TransformHandler, TransformType


def handle_transformable_exception(transform_handler: Optional[TransformHandler] = None) -> Callable:
    def function_wrapper(decorated_function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> TransformType:
            try:
                return decorated_function(*args, **kwargs)
            except BaseTransformableException as error:
                return error.transform(transform_handler)
        return wrapper
    return function_wrapper
