# Python Imports
from typing import Optional
# Third-Party Imports
# Project Imports
from handlers.handlers_typing import TransformHandler
from exceptions.base_exceptions import BaseTransformableException


class BuiltinTransformableException(BaseTransformableException):

    def __init__(self, *, transform_handler: Optional[TransformHandler] = None, builtin_exception: Exception) -> None:
        super().__init__(transform_handler=transform_handler, builtin_exception=builtin_exception)
