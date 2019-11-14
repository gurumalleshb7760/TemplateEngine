# -*-coding:Utf-8 -*
from flask import *
import static.modules.functions as func

# --- calling Flask API ---
app = Flask(__name__)

# ------------ creating the dictionary with our data ------------

JSON_file_path = './static/data/Person.json'

# reading the data and putting it in a dictionary, adding default template if no template already there
JSONDict = func.json_to_dictionary(JSON_file_path)

# putting the dictionary in the JSON file
func.dictionary_to_json(JSON_file_path, JSONDict)

# ------------ Variables and constants ------------
# creating a list with all the names from the JSON file
names = func.get_surnames(JSONDict)


# ------------ Routes ------------
# creating the index page of our website
@app.route('/')
def index():
    return render_template("index.html", names=names)


# creating redirection to the template
@app.route('/', methods=['POST'])
def redirect_to_template():
    name = request.form['list_name']
    return redirect(url_for('template', name=name))


# creating the introduction page
@app.route('/template_<name>', methods=['GET', 'POST'])
def template(name):
    all_info = func.get_all_info(JSONDict, name)
    temp = func.get_template(JSONDict, name)
    return render_template('welcome.html', all_info=all_info, template=temp)


if __name__ == '__main__':
    app.run()
