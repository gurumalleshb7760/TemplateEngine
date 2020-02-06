# --------------------------------------------------------
# module containing Variable class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Template import Template
from Classes.Expression import Expression
import static.modules.functions as func

# -----------Importing the dictionary with the people's information---------------------
JSON_file_path = './static/data/Person.json'
# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_person_to_dictionary(JSON_file_path)


class Variable(Template, Expression):
    """ This object allows to create a variable."""

    def __init__(self, person, var):
        """Initiates the object with the person to look for and the field to look."""
        self._person = person
        self._var = str(var).upper()
        infos = func.get_all_info(JSONDict, self._person)
        if infos is not None:
            self._list = list(infos[self.var])
        else:
            self._list = []
        super(Variable, self).__init__(self._list)

    def get_person(self):
        """Returns the person."""
        return self._person

    def set_person(self, p):
        """Sets the person."""
        self._person = p

    person = property(get_person, set_person)

    def get_var(self):
        """Returns the field."""
        return self._var

    def set_var(self, v):
        """Sets the field."""
        self._var = v

    var = property(get_var, set_var)

    def get_list(self):
        """Returns the list created."""
        return self._list

    def set_list(self, p):
        """Sets the list created."""
        self._list = p

    list = property(get_list, set_list)

    def HTML(self):
        """Returns the HTML representation of the variable"""
        infos = func.get_all_info(JSONDict, self.person)
        return infos[self.var]

    def value(self):
        """Returns thr value of the field looked for for this person"""
        infos = func.get_all_info(JSONDict, self.person)
        return int(infos[self.var])

    def __repr__(self):
        """Returns the representation of the variable"""
        infos = func.get_all_info(JSONDict, self.person)
        if infos is not None:
            return str(infos[self.var])
        else:
            return ""

    def __str__(self):
        """Returns the string representation of the variable"""
        return self.__repr__()
