# Python Imports
# Third-Party Imports
# Project Imports
from core_exceptions.base_exceptions import BaseTransformableException


class WrappedTransformableException(BaseTransformableException):

    def __init__(self, *, wrapped_exception: Exception, **kwargs) -> None:
        super().__init__(**kwargs)
        self.wrapped_exception: Exception = wrapped_exception
