# -*-coding:Utf-8 -*
""" This module regroups several functions used by the main program"""
import json
from OptionsTemplate import OptionTemplate


# function putting the file in a dictionary and adding the default template if there is no template
def json_person_to_dictionary(path):
    with open(path, 'r') as JSONData:
        json_dict = json.load(JSONData)

    for key, value in json_dict.items():
        value_dict = dict(value)
        if 'TEMPLATE' not in value_dict.keys():
            value_dict['TEMPLATE'] = OptionTemplate()
        json_dict[key] = value_dict
    return json_dict


# function allowing to put any file in a dictionary
def other_json_person_to_dictionary(path):
    with open(path, 'r') as JSONData:
        json_dict = json.load(JSONData)
    return json_dict


# function saving our data in a json file
def dictionary_to_json(path, dictionary):
    with open(path, 'w') as JSONData:
        json.dump(dictionary, JSONData, indent=4, ensure_ascii=False)


# function getting all the surnames in the dictionary
def get_surnames(dictionary):
    names_list = []
    for val in dictionary.values():
        val_dict = dict(val)
        names_list.append(val_dict['SURNAME'])
    return names_list


def get_template(dictionary, name):
    templates = {}
    for val in dictionary.values():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            templates = val_dict['TEMPLATE']
    return templates


# function getting all the info of a person from their name
def get_all_info(dictionary, name):
    for val in dictionary.values():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            return val_dict


# function getting all the info of a person, minus the template
def get_global_infos_except_template(dictionary):
    global_vals = dict()
    for index, val in dictionary.items():
        val_dict = dict(val)
        val_minus_template = dict()
        for key, value in val_dict.items():
            if key != 'TEMPLATE':
                val_minus_template[key] = value
        global_vals[index] = val_minus_template
    return global_vals


# function getting all the parameters' names, minus the template
def get_parameters_names_except_template(dictionary):
    parameters = list()
    val_dict = dict(dictionary["1"])
    for key in val_dict.keys():
        if key != 'TEMPLATE':
            parameters.append(key)
    return parameters


# function finding the index corresponding to a surname
def find_index_from_surname(dictionary, name):
    for index, val in dictionary.items():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            return index


# function editing the dictionnary
def edit_options(dictionary, name, options):
    person = get_all_info(dictionary, name)
    template = get_template(dictionary, name)
    index = find_index_from_surname(dictionary, name)
    for old_option, old_value in template.items():
        for new_option, new_value in options.items():
            if old_option == new_option:
                template[old_option] = new_value
    person['TEMPLATE'] = template
    dictionary[index] = person
    return dictionary


# function sorting a dictionary by the parameter sort
def sort_by(dictionary, sort):
    sorted_dict = dict()
    if sort == "INDEX":
        sorted_dict = dictionary
    else:
        list_to_sort = list()
        for value in dictionary.values():
            val_dict = dict(value)
            for key, val in val_dict.items():
                if key == sort:
                    list_to_sort.append(val)
        sorted_list = sorted(list_to_sort)
        for i in range(len(sorted_list)):
            for key, value in dictionary.items():
                val_dict = dict(value)
                if val_dict[sort] == sorted_list[i]:
                    sorted_dict[key] = val_dict
    return sorted_dict
