# --------------------------------------------------------
# module containing Expression class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------


class Expression(list):
    """ This object allows to create an expression to be analyzed (abstract class)."""

    def value(self):
        """Returns the value of the expression."""
        pass
