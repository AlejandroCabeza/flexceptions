# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from decorators import exceptions_decorators
from core_exceptions.base_exceptions import BaseFlexception
from core_exceptions.wrapped_exceptions import WrappedFlexception


class TestExceptionDecorators(TestCase):

    def test_handle_transformable_exception_without_exception(self):
        def transform_handler(_exception: BaseFlexception) -> bool:
            return False

        @exceptions_decorators.handle_flexception(transform_handler)
        def function():
            return True

        assert function() is True

    def test_handle_transformable_exception_with_exception_with_transform_handler(self):
        def transform_handler(_exception: BaseFlexception) -> bool:
            return False

        @exceptions_decorators.handle_flexception(transform_handler)
        def function():
            raise BaseFlexception()

        assert function() is False

    def test_handle_transformable_exception_with_exception_without_transform_handler(self):
        @exceptions_decorators.handle_flexception()
        def function():
            raise BaseFlexception()

        with self.assertRaises(WrappedFlexception) as error:
            function()
        assert isinstance(error.exception.wrapped_exception, TypeError)
