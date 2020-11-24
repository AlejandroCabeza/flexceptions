# Python Imports
from typing import Optional
# Third-Party Imports
# Project Imports
from handlers.handlers_typing import TransformHandler, TransformType


class BaseTransformableException(Exception):

    DEFAULT_TRANSFORM_HANDLER: TransformHandler = None

    def __init__(self, *, transform_handler: Optional[TransformHandler] = None, **kwargs) -> None:
        super().__init__()
        self._transform_handler: Optional[TransformHandler] = transform_handler
        self.__dict__.update(**kwargs)

    @property
    def transform_handler(self) -> TransformHandler:
        return self._transform_handler or self.__class__.DEFAULT_TRANSFORM_HANDLER

    @transform_handler.setter
    def transform_handler(self, transform_handler: Optional[TransformHandler]) -> None:
        self._transform_handler = transform_handler

    def transform(self, transform_handler: Optional[TransformHandler] = None) -> TransformType:
        handler: TransformHandler = transform_handler or self.transform_handler
        try:
            return handler(self)
        except TypeError as error:
            from core_exceptions.wrapped_exceptions import WrappedTransformableException
            raise WrappedTransformableException(wrapped_exception=error)

    def __str__(self) -> str:
        return str({"transform_handler": self.transform_handler})

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self})>"
