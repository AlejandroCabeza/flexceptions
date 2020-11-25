# Python Imports
from typing import TypeVar, Callable, TYPE_CHECKING
# Third-Party Imports
# Project Imports
if TYPE_CHECKING:
    from core_exceptions.base_exceptions import BaseFlexception


HandlerReturn = TypeVar("HandlerReturn")
Handler = Callable[["BaseFlexception"], HandlerReturn]
