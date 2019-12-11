""" This module contains Constant Class"""
from Template import Template


class Constant(Template):

    """ This object allows to create a constant"""

    def __init__(self, const):
        super(Template)
        self._const = const

    def get_const(self):
        return self._const

    def set_const(self, c):
        self._const = c

    const = property(get_const, set_const)

    def HTML(self):

        return str(self.const)

    def __repr__(self):
        return str(self.const)

    def __str__(self):
        return self.__repr__()
