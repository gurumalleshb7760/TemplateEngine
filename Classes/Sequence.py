""" This module contains Sequence Class"""
from Classes.Constant import Constant
from Classes.Variable import Variable
from Classes.Template import Template
from Classes.Test import Test
from Classes.Loop import Loop
from Classes.MyList import MyList
from Classes.Iterator import Iterator


class Sequence(Template):

    """ This object allows to create a sequence of constants and variables"""

    def __init__(self, *args):
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
            elif type(arg) == Test:
                result += Test(arg.condition, arg.ifTrue, arg.ifFalse).HTML()
            elif type(arg) == Loop:
                result += Loop(arg.object, arg.list, arg.todo).HTML()
            elif type(arg) == MyList:
                result += MyList(arg.list).HTML()
            elif type(arg) == Iterator:
                result += ""
            else:
                raise TypeError(" Your object has to be a Sequence, a Test, a Loop, a MyList, an Iterator, a Constant or a Variable")
        return result

    def __repr__(self):
        result = ""
        for arg in self.sequence.values():
            if type(arg) == Constant:
                result += Constant(arg).__str__()
            elif type(arg) == Variable:
                result += Variable(arg.person, arg.var).__str__()
            elif type(arg) == Test:
                result += Test(arg.condition, arg.ifTrue, arg.ifFalse).__str__()
            elif type(arg) == Loop:
                result += Loop(arg.object, arg.list, arg.todo).__str__()
            elif type(arg) == MyList:
                result += MyList(arg.list).__str__()
            elif type(arg) == Iterator:
                result += Iterator(arg).__str__()
            else:
                raise TypeError(" Your object has to be a Sequence, a Test, a Loop, a MyList, an Iterator, a Constant or a Variable")
        return result

    def __str__(self):
        return self.__repr__()


