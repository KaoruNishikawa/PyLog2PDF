__all__ = ["LoggedClass", "LoggedFunction"]

import pylog2pdf


def LoggedClass(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            base_name = self.__class__.__mro__[-2].__name__
            pylog2pdf.LOG[base_name] = self.__class__.__mro__[0].__name__
            super().__init__(*args, **kwargs)

    return Wrapped


def LoggedFunction(func):
    def wrapped(*args, **kwargs):
        pylog2pdf.LOG["function"].append(func.__name__)
        return func(*args, **kwargs)

    return wrapped
