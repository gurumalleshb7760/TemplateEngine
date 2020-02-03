# --------------------------------------------------------
# module containing Test class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Template import Template


class Test(Template):
    """ This object allows to create a test comparting two elements"""
    
    def __init__(self, condition, ifTrue, ifFalse):
        """Initiates the object with the object of the condition, the thing to do if it's true and the one to do if it's false"""
        self._condition = condition
        self._ifTrue = ifTrue
        self.ifFalse = ifFalse

    def _get_condition(self):
        """Returns the condition"""
        return self._condition

    def _set_condition(self, value):
        """Sets the condition"""
        self._condition = value

    condition = property(_get_condition, _set_condition)

    def _get_ifTrue(self):
        """Returns the thing to do if the condition is true"""
        return self._ifTrue

    def _set_ifTrue(self, value):
        """Sets the thing to do if the condition is true"""
        self._ifTrue = value

    ifTrue = property(_get_ifTrue, _set_ifTrue)

    def _get_ifFalse(self):
        """Returns the thing to do if the condition is false"""
        return self._ifFalse

    def _set_ifFalse(self, value):
        """Sets the thing to do if the condition is false"""
        self._ifFalse = value

    ifFalse = property(_get_ifFalse, _set_ifFalse)

    def HTML(self):
        """Returs the HTML representation of the test, which is the thing to do depending of the result"""
        if self.condition.value() == 1:
            return self.ifTrue.HTML()
        else:
            return self.ifFalse.HTML()

    def __repr__(self):
        """Returns the representation of the test"""
        return "if ("+self.condition.__str__()+") "+self.ifTrue.__str__()+" else "+self.ifFalse.__str__()

    def __str__(self):
        """Returns the string representation of the test"""
        return self.__repr__()
