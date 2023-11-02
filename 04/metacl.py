"""MetaClass put custom_ before attrs"""


class CustomMeta(type):
    """It is class docstring"""
    class Custom:
        def __setattr__(self, name, val):
            super().__setattr__("custom_" + name, val)

    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for nm in attrs:
            if nm.startswith('__') and nm.endswith('__'):
                new_attrs[nm] = attrs[nm]
            else:
                new_attrs["custom_" + nm] = attrs[nm]
        return super().__new__(mcs, name, bases + (mcs.Custom,), new_attrs)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
