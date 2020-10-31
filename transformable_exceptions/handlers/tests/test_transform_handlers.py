# Python Imports
from unittest import TestCase
# Third-Party Imports
# Project Imports
from handlers import transform_handlers
from exceptions.base_exceptions import BaseTransformableException


class TestTransformHandlers(TestCase):

    def test_json_dumps_transform_handler(self):
        exception: BaseTransformableException = BaseTransformableException(a="a", b=2, c=True)
        self.assertEqual(
            transform_handlers.json_dumps_transform_handler(exception),
            '{"_transform_handler": null, "a": "a", "b": 2, "c": true}'
        )
