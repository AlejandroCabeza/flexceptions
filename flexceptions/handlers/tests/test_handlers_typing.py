# Python Imports
from typing import TypeVar, Callable
from unittest import TestCase
# Framework Imports
# Third-Party Imports
# Project Imports
from flexceptions import HandlerReturn, Handler


class TestHandlersTyping(TestCase):

    def test_handler_return(self):
        assert isinstance(HandlerReturn, TypeVar)

    def test_handler(self):
        assert isinstance(Handler, Callable)
