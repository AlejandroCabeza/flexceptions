# Python Imports
from functools import wraps
from typing import Callable, Optional
# Third-Party Imports
# Project Imports
from handlers.handlers_typing import Handler, HandlerReturn
from core_exceptions.base_exceptions import BaseFlexception


def handle_flexception(handler: Optional[Handler] = None) -> Callable:
    def function_wrapper(decorated_function: Callable) -> Callable:
        @wraps(decorated_function)
        def wrapper(*args, **kwargs) -> HandlerReturn:
            try:
                return decorated_function(*args, **kwargs)
            except BaseFlexception as error:
                return error.handle(handler)
        return wrapper
    return function_wrapper
