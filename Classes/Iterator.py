# --------------------------------------------------------
# module containing Iterator class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Template import Template
from Classes.Expression import Expression
import static.modules.functions as func


class Iterator(Template):
    """This object allows to create an Iterator."""

    def __init__(self, iterator, *parameters):
        """Initiates the object with the field to search for and the different parameters we want with it."""
        self._iterator = str(iterator)
        self._parameters = parameters

    def get_iterator(self):
        """Returns the iterator."""
        return self._iterator

    def set_iterator(self, v):
        """Sets the iterator"""
        self._iterator = v

    iterator = property(get_iterator, set_iterator)

    def get_parameters(self):
        """Returns the parameters"""
        return self._parameters

    def set_parameters(self, v):
        """Sets the parameters"""
        self._parameters = v

    parameters = property(get_parameters, set_parameters)

    def HTML(self):
        """Returns the HTML representation of the iterator with is void since it just precise what we're looking for for the loop."""
        return str(self.iterator)

    def __repr__(self):
        """Returns the representation of the iterator, here just the iterator"""
        return str(self.iterator)

    def __str__(self):
        """Returns the string representation of the iterator"""
        return self.__repr__()
