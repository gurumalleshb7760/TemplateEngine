""" This module contains Different Class"""
from Classes.Expression import Expression


class Different(Expression):

    """ This object allows to compare if an object is different to an other"""
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def _get_value1(self):
        return self._value1

    def _set_value1(self, value):
        self._value1 = value

    value1 = property(_get_value1, _set_value1)

    def _get_value2(self):
        return self._value2

    def _set_value2(self, value):
        self._value2 = value

    value2 = property(_get_value2, _set_value2)

    def value(self):
        if self.value1.__str__() != self.value2.__str__():
            return 1
        else:
            return 0
