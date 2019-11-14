""" This module contains OptionsTemplate Class"""


class OptionTemplate(dict):

    """ This object allows each person to have his own options for his template"""

    def __init__(self, key="", value=""):
        super(OptionTemplate, self).__init__()
        self["GENDER"] = "Neutral"
        self["PRESENTATION_TEXT"] = ""
        if key != "" and value != "":
            self[key] = value

    def _get_options_names(self):
        return self.keys()

    options_names = property(_get_options_names)

