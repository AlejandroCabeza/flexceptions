# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from exceptions import builtin_exceptions


class TestBuiltinTransformableException(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.DEFAULT_TRANSFORM_HANDLER = builtin_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER

    def tearDown(self) -> None:
        builtin_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = self.DEFAULT_TRANSFORM_HANDLER

    def test_initialisation(self):
        def test_transform_handler(transformable_exception: builtin_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        exception: builtin_exceptions.BaseTransformableException = builtin_exceptions.BaseTransformableException(
            transform_handler=test_transform_handler, data={}
        )
        self.assertIsNone(exception.DEFAULT_TRANSFORM_HANDLER)
        self.assertEqual(exception._transform_handler, test_transform_handler)
        self.assertEqual(exception.__dict__, {
            "_transform_handler": test_transform_handler,
            "data": {}
        })
