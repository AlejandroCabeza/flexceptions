# Overview

Flexceptions (Flexible Exceptions) is an error handling library for Python3.

### Description
Flexceptions provides a hierarchy of exceptions with a handling mechanism. This allows defining a specific "handling" behaviour for the exception and delegating the execution of that behaviour to a later point.

A handler is no more than any function conforming to the `Handler` typing.
```python
from flexceptions import Handler
# Handler = Callable[["BaseFlexception"], HandlerReturn]
```

You can store a handler to be executed upon calling the public `handle` method. There are three ways to set a handler in a flexception:
```python
from flexceptions import BaseFlexception, Handler

def my_callback(_exception: BaseFlexception) -> None:
    ...

# Class
class MyFlexception(BaseFlexception):
    DEFAULT_HANDLER: Handler = my_callback

# Instance
flexception: BaseFlexception = BaseFlexception(handler=my_callback)

# Call
BaseFlexception().handle(my_callback)
```

There's a priority hierarchy to know what handler to use:
* If the handler parameter is passed when calling the `handle` method, it takes priority over the rest.
* If the handler parameter is not passed when calling the `handle` method:
  * If a handler was passed on exception instantiation, that's the one that will be used.
  * Otherwise, it will default to the class' default handler.

# Requirements

* Python (>=3.8)

# Installation

`pip install flexceptions`

# Usage Examples

### API Error Handling
One use case I like abstracting with this library is an exception hierarchy system that is castable to an HTTP Response object. Then, by decorating views with `handle_flexception`, every raised Flexception will have its `handle` method called, ensuring a proper object is sent back.

It's also worth to mention that the `handle_flexception` decorator accepts a `handler` that is passed on to the `handle` method. 
```python
from typing import Dict
from flexceptions import BaseFlexception, Handler, handle_flexception


class Request:
  ...

class Response:
  ...


def _transform_to_http_response(exception: "MyApiException") -> Response:
  return Response(status_code=exception.status_code, json=exception.json)


class MyApiException(BaseFlexception):
    DEFAULT_HANDLER: Handler = _transform_to_http_response

    def __init__(self, status_code: int = 400, json: Dict = None) -> None:
        self.status_code: int = status_code
        self.json: Dict = json or dict()


@handle_flexception
def view(request: Request) -> Response:
    ...
```
