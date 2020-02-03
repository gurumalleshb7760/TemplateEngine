# --------------------------------------------------------
# module containing Or class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Expression import Expression


class Or(Expression):
    """This object allows to create a "or" condition;"""

    def __init__(self, condition1, condition2):
        """Initiates the object with two conditions."""
        self._condition1 = condition1
        self._condition2 = condition2

    def _get_condition1(self):
        """Returns the first condition."""
        return self._condition1

    def _set_condition1(self, condition):
        """Sets the first condition."""
        self._condition1 = condition

    condition1 = property(_get_condition1, _set_condition1)

    def _get_condition2(self):
        """Returns the second condition."""
        return self._condition2

    def _set_condition2(self, condition):
        """Sets the second condition."""
        self._condition2 = condition

    condition2 = property(_get_condition2, _set_condition2)

    def value(self):
        """Returns the result of the and operation : 1 if it's true and 0 if it's false."""
        if self.condition1.value() or self.condition2.value():
            return 1
        else:
            return 0

    def __repr__(self):
        """Returns the representation of the expression"""
        return self.condition1.__str__()+" or "+self.condition2.__str__()

    def __str__(self):
        """Returns the string representation of the expression"""
        return self.__repr__()
