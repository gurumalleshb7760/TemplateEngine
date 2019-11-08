from flask import *
import pandas as pd

# calling Flask API
app = Flask(__name__)

file_path = './static/data/Surname_FirstName_Age_City_Work.csv'

CSVFile = pd.read_csv(file_path, index_col="ID")  # stocking the data

# print(CSVFile)

names = [name for name in CSVFile.get('SURNAME')]  # creating a list with all the names from the CSV file

# print(names)


def get_all_info(name):
    name_index = CSVFile[CSVFile['SURNAME'] == name].index.values.astype(int)[0]
    return CSVFile.loc[name_index]


# creating the index page of our website
@app.route('/')
def index():
    return render_template("index.html", message=names)


# creating redirection to the template
@app.route('/', methods=['POST'])
def redirect_to_template():
    name = request.form['list_name']
    return redirect(url_for('template', name=name))


# creating the introduction page
@app.route('/template_<name>', methods=['GET', 'POST'])
def template(name):
    all_info = get_all_info(name)
    return render_template(all_info.get('TEMPLATE'), message=all_info)


if __name__ == '__main__':
    app.run()
