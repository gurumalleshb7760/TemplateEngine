# --------------------------------------------------------
# module containing Sequence class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Constant import Constant
from Classes.Variable import Variable
from Classes.Template import Template
from Classes.Test import Test
from Classes.Loop import Loop
from Classes.MyList import MyList
from Classes.Iterator import Iterator


class Sequence(Template):
    """ This object allows to create a sequence of constants, variables, tests, loops or other sequences."""

    def __init__(self, *args):
        """Initiates with all the arguments of the sequence."""
        seq = {}
        for i in range(len(args)):
            seq[i] = args[i]
        self._sequence = seq

    def get_sequence(self):
        """Returns the sequence as a dictionary"""
        return self._sequence

    def set_sequence(self, s):
        """Sets the sequence"""
        self._sequence = s

    sequence = property(get_sequence, set_sequence)

    def HTML(self):
        """ Returns the HTML representation of this sequence, which is the HTML representation of all its arguments"""
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
        """Returns the representation of the sequence"""
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
                result += Iterator(arg.iterator, arg.parameters).__str__()
            else:
                raise TypeError(" Your object has to be a Sequence, a Test, a Loop, a MyList, an Iterator, a Constant or a Variable")
        return result

    def __str__(self):
        """Returns the string representation of the sequence"""
        return self.__repr__()


