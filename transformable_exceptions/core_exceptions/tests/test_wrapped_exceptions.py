# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from core_exceptions import wrapped_exceptions


class TestWrappedTransformableException(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.DEFAULT_TRANSFORM_HANDLER = wrapped_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER

    def tearDown(self) -> None:
        wrapped_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = self.DEFAULT_TRANSFORM_HANDLER

    def test_initialisation(self):
        def test_transform_handler(transformable_exception: wrapped_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        type_error: Exception = TypeError("error-message")
        exception: wrapped_exceptions.BaseTransformableException = wrapped_exceptions.WrappedTransformableException(
            transform_handler=test_transform_handler, wrapped_exception=type_error
        )
        self.assertIsNone(exception.DEFAULT_TRANSFORM_HANDLER)
        self.assertEqual(exception._transform_handler, test_transform_handler)
        self.assertEqual(exception.__dict__, {
            "_transform_handler": test_transform_handler,
            "wrapped_exception": type_error
        })
