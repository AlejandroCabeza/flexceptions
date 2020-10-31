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
    def transform_handler(self, transform_handler: Optional[TransformHandler]):
        self._transform_handler = transform_handler

    def transform(self, transform_handler: Optional[TransformHandler] = None) -> TransformType:
        handler: TransformHandler = transform_handler or self.transform_handler
        try:
            return handler(self)
        except TypeError as error:
            from exceptions.builtin_exceptions import BuiltinTransformableException
            raise BuiltinTransformableException(builtin_exception=error)

    def __str__(self) -> str:
        instance_string_representation: dict = {"transform_handler": self.transform_handler}
        return str(instance_string_representation)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self})>"
