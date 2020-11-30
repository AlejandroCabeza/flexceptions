# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from flexceptions.core_exceptions import base_exceptions
from flexceptions.core_exceptions.wrapped_exceptions import WrappedFlexception


class TestBaseFlexception(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.DEFAULT_HANDLER = base_exceptions.BaseFlexception.DEFAULT_HANDLER

    def tearDown(self) -> None:
        base_exceptions.BaseFlexception.DEFAULT_HANDLER = self.DEFAULT_HANDLER

    def test_initialisation(self):
        def test_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception(
            handler=test_handler, data={}
        )
        self.assertIsNone(exception.DEFAULT_HANDLER)
        self.assertEqual(exception._handler, test_handler)
        self.assertEqual(exception.__dict__, {
          "_handler": test_handler,
          "data": {}
        })

    def test_handler_getter_only_default_defined(self):
        def test_default_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        base_exceptions.BaseFlexception.DEFAULT_HANDLER = test_default_handler
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception()

        self.assertEqual(exception.handler, test_default_handler)

    def test_handler_getter_only_member_defined(self):
        def test_member_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception(
            handler=test_member_handler
        )

        self.assertEqual(exception.handler, test_member_handler)

    def test_handler_getter_default_and_member_defined(self):
        def test_default_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        def test_member_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        base_exceptions.BaseFlexception.DEFAULT_HANDLER = test_default_handler
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception(
            handler=test_member_handler
        )

        self.assertEqual(exception.handler, test_member_handler)

    def test_handler_setter(self):
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception()
        self.assertIsNone(exception._handler)

        def test_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__
        exception.handler = test_handler

        self.assertEqual(exception._handler, test_handler)

    def test_transform_with_handler_as_parameter(self):
        def test_default_handler(_transformable_exception: base_exceptions.BaseFlexception) -> int:
            return 1

        def test_member_handler(_transformable_exception: base_exceptions.BaseFlexception) -> int:
            return 2

        def test_parameter_handler(
                _transformable_exception: base_exceptions.BaseFlexception
        ) -> int:
            return 3

        base_exceptions.BaseFlexception.DEFAULT_HANDLER = test_default_handler
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception(
            handler=test_member_handler
        )

        self.assertEqual(exception.handle(test_parameter_handler), 3)

    def test_transform_without_handler_as_parameter(self):
        def test_default_handler(_transformable_exception: base_exceptions.BaseFlexception) -> int:
            return 1

        def test_member_handler(_transformable_exception: base_exceptions.BaseFlexception) -> int:
            return 2

        base_exceptions.BaseFlexception.DEFAULT_HANDLER = test_default_handler
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception(
            handler=test_member_handler
        )

        self.assertEqual(exception.handle(), 2)

    def test_transform_without_handler_as_parameter_without_member_handler(self):
        def test_default_handler(_transformable_exception: base_exceptions.BaseFlexception) -> int:
            return 1

        base_exceptions.BaseFlexception.DEFAULT_HANDLER = test_default_handler
        exception: base_exceptions.BaseFlexception = base_exceptions.BaseFlexception()

        self.assertEqual(exception.handle(), 1)

    def test_transform_without_handlers(self):
        with self.assertRaises(base_exceptions.BaseFlexception) as error:
            base_exceptions.BaseFlexception().handle()
        self.assertIs(type(error.exception), WrappedFlexception)

    def test_str(self):
        def test_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        self.assertEqual(
            str(base_exceptions.BaseFlexception(handler=test_handler)),
            str({"handler": test_handler})
        )

    def test_repr(self):
        def test_handler(transformable_exception: base_exceptions.BaseFlexception) -> dict:
            return transformable_exception.__dict__

        self.assertEqual(
            repr(base_exceptions.BaseFlexception(handler=test_handler)),
            f"<BaseFlexception ({{'handler': {str(test_handler)}}})>"
        )
