""" This module contains MyList Class"""
from Classes.Template import Template
from Classes.Expression import Expression
import static.modules.functions as func

JSON_file_path = './static/data/Person.json'
JSONDict = func.json_person_to_dictionary(JSON_file_path)


class MyList(Template, Expression, list):

    """ This object allows to create a list from the Person.json"""

    def __init__(self, person, var):
        self._person = person
        self._var = var
        infos = func.get_all_info(JSONDict, self.person)
        self.list = list(infos[self.var])
        super(MyList, self).__init__(self.list)

    def get_person(self):
        return self._person

    def set_person(self, p):
        self._person = p

    person = property(get_person, set_person)

    def get_var(self):
        return self._var

    def set_var(self, p):
        self._var = p

    var = property(get_var, set_var)

    def get_list(self):
        return self._list

    def set_list(self, p):
        self._list = p

    list = property(get_list, set_list)

