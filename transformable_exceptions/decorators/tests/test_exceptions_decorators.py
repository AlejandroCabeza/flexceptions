# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from decorators import exceptions_decorators
from core_exceptions.base_exceptions import BaseTransformableException
from core_exceptions.wrapped_exceptions import WrappedTransformableException


class TestExceptionDecorators(TestCase):

    def test_handle_transformable_exception_without_exception(self):
        def transform_handler(_exception: BaseTransformableException) -> bool:
            return False

        @exceptions_decorators.handle_transformable_exception(transform_handler)
        def function():
            return True

        assert function() is True

    def test_handle_transformable_exception_with_exception_with_transform_handler(self):
        def transform_handler(_exception: BaseTransformableException) -> bool:
            return False

        @exceptions_decorators.handle_transformable_exception(transform_handler)
        def function():
            raise BaseTransformableException()

        assert function() is False

    def test_handle_transformable_exception_with_exception_without_transform_handler(self):
        @exceptions_decorators.handle_transformable_exception()
        def function():
            raise BaseTransformableException()

        with self.assertRaises(WrappedTransformableException) as error:
            function()
        assert isinstance(error.exception.wrapped_exception, TypeError)
