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
