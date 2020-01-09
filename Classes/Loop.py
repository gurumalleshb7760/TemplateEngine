""" This module contains Loop Class"""
from Classes.Template import Template
import static.modules.functions as func

# -----------Importing the dictionary with the people's information---------------------
JSON_file_path = './static/data/Person.json'
# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_person_to_dictionary(JSON_file_path)


class Loop(Template):

    """ This object allows to create a Loop on an element"""

    def __init__(self, object, list, todo):
        self._object = object
        self._list = list
        self._todo = todo

    def _get_object(self):
        return self._object

    def _set_object(self, value):
        self._object = value

    object = property(_get_object, _set_object)

    def _get_list(self):
        return self._list

    def _set_list(self, value):
        self._list = value

    list = property(_get_list, _set_list)

    def _get_todo(self):
        return self._todo

    def _set_todo(self, value):
        self._todo = value

    todo = property(_get_todo, _set_todo)

    def HTML(self):
        result = ""
        if len(self.list) == 0:
            return result
        else:
            for i in self.list:
                result += str(self.todo)
                name = func.find_specific_info(JSONDict, i, "FIRST_NAME")
                result = result.replace(str(self.object), name)
            return result

    def __repr__(self):
        return "for "+str(self.object)+" in "+str(self.list)+" do : "+str(self.todo)

    def __str__(self):
        return self.__repr__()
