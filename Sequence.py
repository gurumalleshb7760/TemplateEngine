""" This module contains Sequence Class"""
from Constant import Constant
from Variable import Variable
from Template import Template


class Sequence(Template):

    """ This object allows to create a sequence of constants and variables"""

    def __init__(self, *args):
        super(Template)
        seq = {}
        for i in range(len(args)):
            seq[i] = args[i]
        self._sequence = seq

    def get_sequence(self):
        return self._sequence

    def set_sequence(self, s):
        self._sequence = s

    sequence = property(get_sequence, set_sequence)

    def HTML(self):
        result = ""
        for arg in self.sequence.values():
            if type(arg) == Constant:
                result += Constant(arg).HTML()
            elif type(arg) == Variable:
                result += Variable(arg.person, arg.var).HTML()
            else:
                raise TypeError(" Your object has to be a Sequence, a Constant or a Variable")
        return result

    def __repr__(self):
        result = "<p>"
        for arg in self.sequence.values():
            if type(arg) == Constant:
                result += Constant(arg).__str__()
            elif type(arg) == Variable:
                result += Variable(arg.person, arg.var).__str__()
            else:
                raise TypeError(" Your object has to be a Sequence, a Constant or a Variable")
        result += "</p>"
        return result

    def __str__(self):
        return self.__repr__()


