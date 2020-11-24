# Python Imports
from typing import TypeVar, Callable, TYPE_CHECKING
# Third-Party Imports
# Project Imports
if TYPE_CHECKING:
    from core_exceptions.base_exceptions import BaseTransformableException


TransformType = TypeVar("TransformType")
TransformHandler = Callable[["BaseTransformableException"], TransformType]
