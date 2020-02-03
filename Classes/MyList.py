# --------------------------------------------------------
# module containing MyList class
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


class MyList(list):
    """This object allows to create a list from the data."""

    def __init__(self, person, var):
        """Initiates the object with the person we look for and the variable we look for too"""
        self._person = person
        self._var = var
        infos = func.get_all_info(JSONDict, self._person)
        self._list = list(infos[self.var])
        super(MyList, self).__init__(self.list)

    def get_person(self):
        """Returns the person."""
        return self._person

    def set_person(self, p):
        """Sets the person."""
        self._person = p

    person = property(get_person, set_person)

    def get_var(self):
        """Returns the variable."""
        return self._var

    def set_var(self, p):
        """Sets the variable."""
        self._var = p

    var = property(get_var, set_var)

    def get_list(self):
        """Returns thr list created."""
        return self._list

    def set_list(self, p):
        """Sets the list created."""
        self._list = p

    list = property(get_list, set_list)

