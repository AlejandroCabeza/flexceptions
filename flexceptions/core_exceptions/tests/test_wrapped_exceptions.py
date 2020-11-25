# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from core_exceptions import wrapped_exceptions


class TestWrappedFlexception(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.DEFAULT_HANDLER = wrapped_exceptions.BaseFlexception.DEFAULT_HANDLER

    def tearDown(self) -> None:
        wrapped_exceptions.BaseFlexception.DEFAULT_HANDLER = self.DEFAULT_HANDLER

    def test_initialisation(self):
        def test_handler(transformable_exception: wrapped_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        type_error: Exception = TypeError("error-message")
        exception: wrapped_exceptions.BaseFlexception = wrapped_exceptions.WrappedFlexception(
            handler=test_handler, wrapped_exception=type_error
        )
        self.assertIsNone(exception.DEFAULT_HANDLER)
        self.assertEqual(exception._handler, test_handler)
        self.assertEqual(exception.__dict__, {
            "_handler": test_handler,
            "wrapped_exception": type_error
        })
