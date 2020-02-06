# -*-coding:Utf-8 -*
# --------------------------------------------------------
# module containing function class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
import json


def json_person_to_dictionary(path):
    """Function putting the file in a dictionary and adding the default template if there is no template."""
    with open(path, 'r') as JSONData:
        json_dict = json.load(JSONData)

    for key, value in json_dict.items():
        value_dict = dict(value)
        if 'TEMPLATE' not in value_dict.keys():
            value_dict['TEMPLATE'] = "default"
        json_dict[key] = value_dict
    return json_dict


def other_json_person_to_dictionary(path):
    """function allowing to put any file in a dictionary."""
    with open(path, 'r') as JSONData:
        json_dict = json.load(JSONData)
    return json_dict


def dictionary_to_json(path, dictionary):
    """Function saving our data in a json file."""
    with open(path, 'w') as JSONData:
        json.dump(dictionary, JSONData, indent=4, ensure_ascii=False)


def get_surnames(dictionary):
    """Function getting all the surnames in the dictionary."""
    names_list = []
    for val in dictionary.values():
        val_dict = dict(val)
        names_list.append(val_dict['SURNAME'])
    return names_list


def get_template(dictionary, name):
    """Function getting the template of a person from their name."""
    templates = {}
    for val in dictionary.values():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            templates = val_dict['TEMPLATE']
    return templates


def get_all_info(dictionary, name):
    """Function getting all the info of a person from their name."""
    for val in dictionary.values():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            return val_dict


def get_global_infos_except_template(dictionary):
    """Function getting all the info of a person, minus the template."""
    global_vals = dict()
    for index, val in dictionary.items():
        val_dict = dict(val)
        val_minus_template = dict()
        for key, value in val_dict.items():
            if key != 'TEMPLATE':
                val_minus_template[key] = value
        global_vals[index] = val_minus_template
    return global_vals


def get_parameters_names_except_template(dictionary):
    """Function getting all the parameters' names, minus the template."""
    parameters = list()
    val_dict = dict(dictionary["1"])
    for key in val_dict.keys():
        if key != 'TEMPLATE':
            parameters.append(key)
    return parameters


def find_index_from_surname(dictionary, name):
    """Function finding the index corresponding to a surname."""
    for index, val in dictionary.items():
        val_dict = dict(val)
        if val_dict['SURNAME'] == name:
            return index


def edit_template(dictionary1, dictionary2, name, template):
    """Function editing the dictionary."""
    person = get_all_info(dictionary1, name)
    index = find_index_from_surname(dictionary1, name)
    temp = template.replace('"', '\\"')
    temp = "eval(\"Sequence("+temp+").HTML()\")"
    person['TEMPLATE'] = "t_"+name+index
    dictionary1[index] = person
    dictionary2["t_"+name+index] = temp
    return [dictionary1, dictionary2]


def sort_by(dictionary, sort):
    """Function sorting a dictionary by the parameter sort."""
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


def find_specific_info(dictionary, index, info_title):
    """Function getting a specific information on a person thanks to their index."""
    for key, value in dictionary.items():
        if key == index:
            val_dict = dict(value)
            return val_dict[info_title]

