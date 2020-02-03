# --------------------------------------------------------
# module containing SupEqu class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Expression import Expression


class SupEqu(Expression):
    """ This object allows to compare if an object is superior or equal to an other."""

    def __init__(self, value1, value2):
        """Initiates the object with the two values to compare."""
        self._value1 = value1
        self._value2 = value2

    def _get_value1(self):
        """Returns the first value."""
        return self._value1

    def _set_value1(self, value):
        """Sets the first value."""
        self._value1 = value

    value1 = property(_get_value1, _set_value1)

    def _get_value2(self):
        """Returns the second value."""
        return self._value2

    def _set_value2(self, value):
        """Sets the second value."""
        self._value2 = value

    value2 = property(_get_value2, _set_value2)

    def value(self):
        """Returns the result of the different operation : 1 if it's true and 0 if it's false."""
        if self.value1.__str__() >= self.value2.__str__():
            return 1
        else:
            return 0

    def __repr__(self):
        """Returns the representation of the expression"""
        return self.value1.__str__()+" and "+self.value2.__str__()

    def __str__(self):
        """Returns the string representation of the expression"""
        return self.__repr__()
