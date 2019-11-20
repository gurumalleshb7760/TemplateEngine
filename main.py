# -*-coding:Utf-8 -*
from flask import *
import static.modules.functions as func

# --- calling Flask API ---
app = Flask(__name__)

# ------------ creating the dictionary with our data ------------

JSON_file_path = './static/data/Person.json'
OPTION_file_path = './static/data/List_Option.json'

# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_person_to_dictionary(JSON_file_path)

# putting the dictionary in the JSON file
func.dictionary_to_json(JSON_file_path, JSONDict)

# ------------ Variables and constants ------------
# creating a list with all the names from the JSON file
names = func.get_surnames(JSONDict)


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


# creating the introduction page
@app.route('/template_<name>/', methods=['GET', 'POST'])
def template(name):
    all_info = func.get_all_info(JSONDict, name)
    temp = func.get_template(JSONDict, name)
    return render_template('welcome.html', all_info=all_info, template=temp, name=name)


# creating the editing page
@app.route('/template_<name>/edit/', methods=['POST'])
def redirect_to_edit(name):
    all_info = func.get_all_info(JSONDict, name)
    temp = func.get_template(JSONDict, name)
    options_static = func.other_json_person_to_dictionary(OPTION_file_path)
    gender_static = options_static['GENDER']
    return render_template('edit.html', info=all_info, template=temp, gender=gender_static, name=name)


# replacing the data in the json file
@app.route('/template_<name>/edit/edition', methods=['GET', 'POST', 'PATCH'])
def edit(name):
    gender = request.form['list_gender']
    pres_text = request.form['pres_text']
    options = {'GENDER': gender, "PRESENTATION_TEXT": pres_text}
    dictionary = func.edit_options(JSONDict, name, options)
    func.dictionary_to_json(JSON_file_path, dictionary)
    return redirect(url_for('template', name=name))


if __name__ == '__main__':
    app.run()
