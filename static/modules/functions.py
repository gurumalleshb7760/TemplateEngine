# -*-coding:Utf-8 -*
""" This module regroups several functions used by the main program"""
import json
from OptionsTemplate import OptionTemplate


# function putting the file in a dictionary and adding the default template if there is no template
def json_to_dictionary(path):
    with open(path, 'r') as JSONData:
        json_dict = json.load(JSONData)

    for key, value in json_dict.items():
        value_dict = dict(value)
        if 'TEMPLATE' not in value_dict.keys():
            value_dict['TEMPLATE'] = OptionTemplate()
        json_dict[key] = value_dict
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
