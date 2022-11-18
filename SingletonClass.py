
class Singleton(object):
    """
    One method to create a singleton instance is this:

    def __new__(cls):
        try:
            it = cls.__it__
        except AttributeError:
            it = cls.__it__ = object.__new__(cls)
        return it

    def __repr__(self):
        return '<{}>'. format(self.__class__.__name__.upper())

    def __eq__(self, other):
        return other is self
    """


    """Another method is this"""
    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError("Singleton method must be accessed with Instance()")

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Single(object):
    def __init__(self):
        self.name = None
        self.val = 0

    def getName(self):
        print(self.name)


a = Single.Instance()
b = Single.Instance()

print(a.getName())
print(b.getName())
    

    

