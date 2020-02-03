# --------------------------------------------------------
# module containing Constant class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Template import Template
from Classes.Expression import Expression


class Constant(Template, Expression):
    """This object allows to create a constant."""

    def __init__(self, const):
        """Initiates the object with the constant."""
        self._const = const

    def get_const(self):
        """Returns the constant."""
        return self._const

    def set_const(self, c):
        """Sets the constant"""
        self._const = c

    const = property(get_const, set_const)

    def HTML(self):
        """Returns the HTML representation of the constant"""
        return str(self.const)

    def value(self):
        """Returns thr value of the constant"""
        return int(self.const)

    def __repr__(self):
        """Returns the representation of the constant"""
        return str(self.const)

    def __str__(self):
        """Returns the string representation of the constant"""
        return self.__repr__()
