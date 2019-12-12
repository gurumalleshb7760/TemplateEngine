# -*-coding:Utf-8 -*
from flask import *
import static.modules.functions as func
from Sequence import Sequence
from Constant import Constant
from Variable import Variable

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
test2 = "My name is $FIRST_NAME $SURNAME, I am $AGE and I live in $CITY."

# ------------ Routes ------------
# creating the index page of our website
@app.route('/')
def index(sort='INDEX'):
    infos = func.get_global_infos_except_template(JSONDict)
    parameters = func.get_parameters_names_except_template(JSONDict)
    return render_template("index.html", names=names, infos=infos, params=parameters, sort=sort)


# creating redirection to sort the table of the index page
@app.route('/redir_index', methods=['GET', 'POST'])
def redirect_index():
    sort = request.form['search-by']
    return redirect(url_for('index_sorted', sort=sort))


# creating the index page of our website
@app.route('/sorted_by_<sort>', methods=['GET', 'POST'])
def index_sorted(sort):
    infos = func.get_global_infos_except_template(JSONDict)
    infos_sorted = func.sort_by(infos, sort)
    parameters = func.get_parameters_names_except_template(JSONDict)
    return render_template("index.html", names=names, infos=infos_sorted, params=parameters, sort=sort)


# creating redirection to the template from index page
@app.route('/redir_template', methods=['GET', 'POST'])
def redirect_to_template_from_index():
    name = request.form['list_name']
    return redirect(url_for('template', name=name))


# creating redirection to the template from table in index page
@app.route('/redir_template_from_table_<name>', methods=['GET', 'POST'])
def redirect_to_template_from_index_table(name):
    return redirect(url_for('template', name=name))


# creating the introduction page
@app.route('/template-instance_<name>/', methods=['GET', 'POST'])
def template(name):
    all_info = func.get_all_info(JSONDict, name)
    name_template = all_info['TEMPLATE']
    temp = eval(TEMPDict[name_template])
    return render_template('welcome.html', all_info=all_info, template=temp, name=name)


# creating the editing page
@app.route('/template-instance_<name>/edit/', methods=['POST'])
def redirect_to_edit(name):
    all_info = func.get_all_info(JSONDict, name)
    name_template = all_info['TEMPLATE']
    temp = TEMPDict[name_template]
    temp = temp.replace('eval("Sequence(', '').replace(').HTML()")', '').replace('\\', '').replace('name,', '')
    temp = temp
    return render_template('edit.html', template=temp, name=name)


# replacing the data in the json file
@app.route('/template-instance_<name>/edit/edition', methods=['GET', 'POST', 'PATCH'])
def edit(name):
    new_template = request.form['template']
    dictionaries = func.edit_template(JSONDict, TEMPDict, name, new_template)
    func.dictionary_to_json(JSON_file_path, dictionaries[0])
    func.dictionary_to_json(TEMPLATES_file_path, dictionaries[1])
    return redirect(url_for('template', name=name))


if __name__ == '__main__':
    app.run()
