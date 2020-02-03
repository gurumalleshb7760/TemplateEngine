# -*-coding:Utf-8 -*
# --------------------------------------------------------
# module containing main class
#
# (C) 2020 Lea Banquart, Laurent Thiry, Mulhouse, France
# Released for a school project at ENSISA
# email lea.banquart@gmail.com
# --------------------------------------------------------
from flask import *
import static.modules.functions as func
from Classes.Template import Template
from Classes.Variable import Variable
from Classes.Constant import Constant
from Classes.Sequence import Sequence
from Classes.Test import Test
from Classes.Expression import Expression
from Classes.And import And
from Classes.Or import Or
from Classes.Different import Different
from Classes.Equal import Equal
from Classes.Inferior import Inferior
from Classes.Superior import Superior
from Classes.InfEqu import InfEqu
from Classes.SupEqu import SupEqu
from Classes.Loop import Loop
from Classes.MyList import MyList
from Classes.Iterator import Iterator

# --- calling Flask API ---
app = Flask(__name__)

# ------------ creating the dictionary with our data ------------
JSON_file_path = './static/data/Person.json'
TEMPLATES_file_path = './static/data/Templates.json'


# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_person_to_dictionary(JSON_file_path)

# reading the templates files
TEMPDict = func.other_json_person_to_dictionary(TEMPLATES_file_path)

# putting the dictionary in the JSON file
func.dictionary_to_json(JSON_file_path, JSONDict)

# ------------ Variables and constants ------------
# creating a list with all the names from the JSON file
names = func.get_surnames(JSONDict)


# -------------------- Routes ---------------------
@app.route('/')
def index(sort='INDEX'):
    """Creating the index page of our website."""
    infos = func.get_global_infos_except_template(JSONDict)
    parameters = func.get_parameters_names_except_template(JSONDict)
    return render_template("index.html", names=names, infos=infos, params=parameters, sort=sort)


@app.route('/redir_index', methods=['GET', 'POST'])
def redirect_index():
    """Creating redirection to sort the table of the index page."""
    sort = request.form['search-by']
    return redirect(url_for('index_sorted', sort=sort))


@app.route('/sorted_by_<sort>', methods=['GET', 'POST'])
def index_sorted(sort):
    """Creating the index page of our website."""
    infos = func.get_global_infos_except_template(JSONDict)
    infos_sorted = func.sort_by(infos, sort)
    parameters = func.get_parameters_names_except_template(JSONDict)
    return render_template("index.html", names=names, infos=infos_sorted, params=parameters, sort=sort)


@app.route('/redir_template', methods=['GET', 'POST'])
def redirect_to_template_from_index():
    """Creating redirection to the template from index page."""
    name = request.form['list_name']
    return redirect(url_for('template', name=name))


@app.route('/redir_template_from_table_<name>', methods=['GET', 'POST'])
def redirect_to_template_from_index_table(name):
    """Creating redirection to the template from table in index page."""
    return redirect(url_for('template', name=name))


@app.route('/template-instance_<name>/', methods=['GET', 'POST'])
def template(name):
    """Creating the introduction page."""
    all_info = func.get_all_info(JSONDict, name)
    name_template = all_info['TEMPLATE']
    temp = eval(TEMPDict[name_template])
    return render_template('welcome.html', all_info=all_info, template=temp, name=name)


@app.route('/template-instance_<name>/edit/', methods=['POST'])
def redirect_to_edit(name):
    """Creating the editing page."""
    all_info = func.get_all_info(JSONDict, name)
    name_template = all_info['TEMPLATE']
    temp = TEMPDict[name_template]
    temp = temp.replace('eval("Sequence(', '').replace(').HTML()")', '').replace('\\', '').replace('name,', '')
    temp = temp
    return render_template('edit.html', template=temp, name=name)


@app.route('/template-instance_<name>/edit/edition', methods=['GET', 'POST', 'PATCH'])
def edit(name):
    """Replacing the data in the json file."""
    new_template = request.form['template']
    dictionaries = func.edit_template(JSONDict, TEMPDict, name, new_template)
    func.dictionary_to_json(JSON_file_path, dictionaries[0])
    func.dictionary_to_json(TEMPLATES_file_path, dictionaries[1])
    return redirect(url_for('template', name=name))


if __name__ == '__main__':
    app.run()
