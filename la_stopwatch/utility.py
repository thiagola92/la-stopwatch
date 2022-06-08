from inspect import signature
from typing import Callable


def get_arguments(func: Callable, args: tuple, kwargs: dict) -> tuple[tuple, dict]:
    """
    Get function arguments, including default values

    It's important to generate the default values
    before passing to callback function.
    Because you can't extract the default values from
    the callback (only if the user did declare the
    default values in the callback).
    """

    sign = signature(func)
    bound_arguments = sign.bind(*args, **kwargs)
    bound_arguments.apply_defaults()
    args = bound_arguments.args
    kwargs = bound_arguments.kwargs

    return args, kwargs
