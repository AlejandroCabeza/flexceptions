# Python Imports
from typing import Optional
# Third-Party Imports
# Project Imports
from handlers.handlers_typing import Handler, HandlerReturn


class BaseFlexception(Exception):

    DEFAULT_HANDLER: Handler = None

    def __init__(self, *, handler: Optional[Handler] = None, **kwargs) -> None:
        super().__init__()
        self._handler: Optional[Handler] = handler
        self.__dict__.update(**kwargs)

    @property
    def handler(self) -> Handler:
        return self._handler or self.__class__.DEFAULT_HANDLER

    @handler.setter
    def handler(self, handler: Optional[Handler]) -> None:
        self._handler = handler

    def handle(self, handler: Optional[Handler] = None) -> HandlerReturn:
        handler: Handler = handler or self.handler
        try:
            return handler(self)
        except TypeError as error:
            from core_exceptions.wrapped_exceptions import WrappedFlexception
            raise WrappedFlexception(wrapped_exception=error)

    def __str__(self) -> str:
        return str({"handler": self.handler})

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self})>"
