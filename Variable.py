""" This module contains Variable Class"""
from Template import Template
import static.modules.functions as func

JSON_file_path = './static/data/Person.json'
JSONDict = func.json_person_to_dictionary(JSON_file_path)


class Variable(Template):

    """ This object allows to create a variable"""

    def __init__(self, person, var):
        super(Template)
        self._person = person
        self._var = str(var).upper()

    def get_person(self):
        return self._person

    def set_person(self, p):
        self._person = p

    person = property(get_person, set_person)

    def get_var(self):
        return self._var

    def set_var(self, v):
        self._var = v

    var = property(get_var, set_var)

    def HTML(self):
        infos = func.get_all_info(JSONDict, self.person)
        return infos[self.var]

    def __repr__(self):
        infos = func.get_all_info(JSONDict, self.person)
        return str(infos[self.var])

    def __str__(self):
        return self.__repr__()
