""" This module contains Constant Class"""
from Classes.Template import Template
from Classes.Expression import Expression


class Constant(Template, Expression):

    """ This object allows to create a constant"""

    def __init__(self, const):
        self._const = const

    def get_const(self):
        return self._const

    def set_const(self, c):
        self._const = c

    const = property(get_const, set_const)

    def HTML(self):
        return str(self.const)

    def value(self):
        return int(self.const)

    def __repr__(self):
        return str(self.const)

    def __str__(self):
        return self.__repr__()
