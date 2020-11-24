# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from core_exceptions import base_exceptions
from core_exceptions.wrapped_exceptions import WrappedTransformableException


class TestBaseTransformableException(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.DEFAULT_TRANSFORM_HANDLER = base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER

    def tearDown(self) -> None:
        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = self.DEFAULT_TRANSFORM_HANDLER

    def test_initialisation(self):
        def test_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException(
            transform_handler=test_transform_handler, data={}
        )
        self.assertIsNone(exception.DEFAULT_TRANSFORM_HANDLER)
        self.assertEqual(exception._transform_handler, test_transform_handler)
        self.assertEqual(exception.__dict__, {
          "_transform_handler": test_transform_handler,
          "data": {}
        })

    def test_transform_handler_getter_only_default_defined(self):
        def test_default_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = test_default_transform_handler
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException()

        self.assertEqual(exception.transform_handler, test_default_transform_handler)

    def test_transform_handler_getter_only_member_defined(self):
        def test_member_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException(
            transform_handler=test_member_transform_handler
        )

        self.assertEqual(exception.transform_handler, test_member_transform_handler)

    def test_transform_handler_getter_default_and_member_defined(self):
        def test_default_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        def test_member_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = test_default_transform_handler
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException(
            transform_handler=test_member_transform_handler
        )

        self.assertEqual(exception.transform_handler, test_member_transform_handler)

    def test_transform_handler_setter(self):
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException()
        self.assertIsNone(exception._transform_handler)

        def test_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__
        exception.transform_handler = test_transform_handler

        self.assertEqual(exception._transform_handler, test_transform_handler)

    def test_transform_with_handler_as_parameter(self):
        def test_default_transform_handler(_transformable_exception: base_exceptions.BaseTransformableException) -> int:
            return 1

        def test_member_transform_handler(_transformable_exception: base_exceptions.BaseTransformableException) -> int:
            return 2

        def test_parameter_transform_handler(
                _transformable_exception: base_exceptions.BaseTransformableException
        ) -> int:
            return 3

        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = test_default_transform_handler
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException(
            transform_handler=test_member_transform_handler
        )

        self.assertEqual(exception.transform(test_parameter_transform_handler), 3)

    def test_transform_without_handler_as_parameter(self):
        def test_default_transform_handler(_transformable_exception: base_exceptions.BaseTransformableException) -> int:
            return 1

        def test_member_transform_handler(_transformable_exception: base_exceptions.BaseTransformableException) -> int:
            return 2

        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = test_default_transform_handler
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException(
            transform_handler=test_member_transform_handler
        )

        self.assertEqual(exception.transform(), 2)

    def test_transform_without_handler_as_parameter_without_member_transform_handler(self):
        def test_default_transform_handler(_transformable_exception: base_exceptions.BaseTransformableException) -> int:
            return 1

        base_exceptions.BaseTransformableException.DEFAULT_TRANSFORM_HANDLER = test_default_transform_handler
        exception: base_exceptions.BaseTransformableException = base_exceptions.BaseTransformableException()

        self.assertEqual(exception.transform(), 1)

    def test_transform_without_transform_handlers(self):
        with self.assertRaises(base_exceptions.BaseTransformableException) as error:
            base_exceptions.BaseTransformableException().transform()
        self.assertIs(type(error.exception), WrappedTransformableException)

    def test_str(self):
        def test_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        self.assertEqual(
            str(base_exceptions.BaseTransformableException(transform_handler=test_transform_handler)),
            str({"transform_handler": test_transform_handler})
        )

    def test_repr(self):
        def test_transform_handler(transformable_exception: base_exceptions.BaseTransformableException) -> dict:
            return transformable_exception.__dict__

        self.assertEqual(
            repr(base_exceptions.BaseTransformableException(transform_handler=test_transform_handler)),
            f"<BaseTransformableException ({{'transform_handler': {str(test_transform_handler)}}})>"
        )
