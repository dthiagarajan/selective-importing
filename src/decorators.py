import functools

from .settings import develop as is_development_environment


class ImportedClass(type):
    def __repr__(cls):
        return cls._class.__name__


class UnimportedClass(type):
    def __repr__(cls):
        return f'{cls._class.__name__} [Unimported]'


def development(cls):
    if is_development_environment:
        class ClassWrapper(metaclass=ImportedClass):
            _class = cls

            def __init__(self, *args, **kwargs):
                self.other_class = self._class(*args, **kwargs)

            def __call__(self, *cls_args):
                other = self.other_class(*cls_args)
                return other

    else:
        class ClassWrapper(metaclass=UnimportedClass):
            _class = cls

            def __init__(self, *args, **kwargs):
                raise ImportError(f'{self._class.__name__} was not imported as development flag is False.')

    ClassWrapper.__name__ = cls.__name__
    return ClassWrapper


class development_function:
    def __init__(self, wrapped):
        self._wrapped = wrapped
        functools.update_wrapper(self, wrapped)

    def __call__(self, *args, **kwargs):
        if is_development_environment:
            return self._wrapped(*args, **kwargs)
        else:
            raise ImportError(f'{self._wrapped.__name__} was not imported as development flag is False.')

    def __repr__(self):
        if is_development_environment:
            return repr(self._wrapped)
        else:
            return f'{repr(self._wrapped)} [Unimported]'
