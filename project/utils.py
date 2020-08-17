import types
from functools import wraps


def get_extractor(func: types.FunctionType):
    print(func.__annotations__)
    return lambda request: {}


def decorator(func):
    extractor = get_extractor(func)

    @wraps(func)
    def handler(request):
        return func(*extractor(request))

    return handler
