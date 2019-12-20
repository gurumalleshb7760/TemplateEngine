""" This module contains And Class"""
from Classes.Expression import Expression


class And(Expression):

    """ This object allows to create an "and" condition """
    def __init__(self, condition1, condition2):
        self._condition1 = condition1
        self._condition2 = condition2

    def _get_condition1(self):
        return self._condition1

    def _set_condition1(self, value):
        self._condition1 = value

    condition1 = property(_get_condition1, _set_condition1)

    def _get_condition2(self):
        return self._condition2

    def _set_condition2(self, value):
        self._condition2 = value

    condition2 = property(_get_condition2, _set_condition2)

    def value(self):
        if self.condition1.value() and self.condition2.value():
            return 1
        else:
            return 0

    def __repr__(self):
        return self.condition1.__str__()+" and "+self.condition2.__str__()

    def __str__(self):
        return self.__repr__()
