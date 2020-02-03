# --------------------------------------------------------
# module containing Loop class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from Classes.Template import Template
from Classes.Iterator import Iterator
import static.modules.functions as func

# -----------Importing the dictionary with the people's information---------------------
JSON_file_path = './static/data/Person.json'
# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_person_to_dictionary(JSON_file_path)


class Loop(Template):
    """This object allows to create a Loop on an element/"""

    def __init__(self, object, list, todo):
        """Initiates the object with the object of the loop (generally an iterator), the list to iterate and the thing to do"""
        self._object = object
        self._list = list
        self._todo = todo

    def _get_object(self):
        """Returns the object of the loop."""
        return self._object

    def _set_object(self, value):
        """Sets the object of the loop."""
        self._object = value

    object = property(_get_object, _set_object)

    def _get_list(self):
        """Return the list to iterate."""
        return self._list

    def _set_list(self, value):
        """Sets the list to iterate."""
        self._list = value

    list = property(_get_list, _set_list)

    def _get_todo(self):
        """Returns the thing to do each iteration"""
        return self._todo

    def _set_todo(self, value):
        """Sets the thing to do each iteration"""
        self._todo = value

    todo = property(_get_todo, _set_todo)

    def HTML(self):
        """ Returns the HTML representation of this loop, which is the result"""
        result = ""
        if len(self.list) == 0:  # if there is nothing in the list, it returns an empty string
            return result
        else:
            for i in self.list:  # for each element in the searched field
                result += str(self.todo)  # we add the thing to do
                # then we search in this result if there is any occurrences of the iterator
                # if there is, we replace it by the searched thing
                if type(self.object) == Iterator:
                    to_replace = ""
                    for param in self.object.parameters:  # since severals parameters can be searched, we search for each of them
                        specific_info = func.find_specific_info(JSONDict, i, param)
                        to_replace += specific_info + " "
                    result = result.replace(str(self.object.iterator), to_replace)
            return result

    def __repr__(self):
        """Returns the representation of the loop"""
        return "for "+str(self.object)+" in "+str(self.list)+" do : "+str(self.todo)

    def __str__(self):
        """Returns the string representation of the loop"""
        return self.__repr__()
