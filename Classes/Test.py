""" This module contains Test Class"""
from Classes.Template import Template


class Test(Template):

    """ This object allows to create a test comparting two elements"""
    
    def __init__(self, condition, ifTrue, ifFalse):
        self._condition = condition
        self._ifTrue = ifTrue
        self.ifFalse = ifFalse

    def _get_condition(self):
        return self._condition

    def _set_condition(self, value):
        self._condition = value

    condition = property(_get_condition, _set_condition)

    def _get_ifTrue(self):
        return self._ifTrue

    def _set_ifTrue(self, value):
        self._ifTrue = value

    ifTrue = property(_get_ifTrue, _set_ifTrue)

    def _get_ifFalse(self):
        return self._ifFalse

    def _set_ifFalse(self, value):
        self._ifFalse = value

    ifFalse = property(_get_ifFalse, _set_ifFalse)

    def HTML(self):
        if self.condition.value() == 1:
            return self.ifTrue.HTML()
        else:
            return self.ifFalse.HTML()

    def __repr__(self):
        return "if ("+self.condition.__str__()+") "+self.ifTrue.__str__()+" else "+self.ifFalse.__str__()

    def __str__(self):
        return self.__repr__()
