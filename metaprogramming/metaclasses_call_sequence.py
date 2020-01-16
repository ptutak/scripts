from pprint import PrettyPrinter
pprint = PrettyPrinter().pprint


class Meta(type):
    _instances = {}

    def __call__(metacls, *args, **kwargs):
        print('Meta.__call__')
        print(metacls)
        pprint(args)
        pprint(kwargs)
        print(super(Meta, metacls).__call__)
        return super(Meta, metacls).__call__(*args, **kwargs)

    def __new__(metacls, *args, **kwargs):
        print('Meta.__new__')
        print(metacls)
        pprint(args)
        pprint(kwargs)
        print(super(Meta, metacls).__call__)
        print(type.__call__)
        return type(*args, **kwargs)


class Foo:
    pass


class Base(Foo, metaclass=Meta):
    def __init__(self, arg1, kwarg1='value1'):
        print('Base.__init__')

    def __new__(cls, *args, **kwargs):
        print('Base.__new__')
        pprint(cls)
        pprint(args)
        pprint(kwargs)
        return super().__new__(cls)

    def __call__(self):
        print('Base.__call__')


x = Base(1, kwarg1='value2')
print(x)
