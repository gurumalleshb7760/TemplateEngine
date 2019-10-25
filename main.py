from flask import Flask
from flask import request
from flask import render_template
import pandas as pd

# calling Flask API
app = Flask(__name__)

file_path = './static/data/Nom_Prenom_Age_Ville_Metier.csv'

CSVFile = pd.read_csv(file_path, index_col="ID")  # stocking the data

# print(CSVFile)

names = [name for name in CSVFile.get('NOM')] # creating a list with all the names from the CSV file

# print(names)


def get_all_info(name):
    name_index = CSVFile[CSVFile['NOM'] == name].index.values.astype(int)[0]
    return CSVFile.loc[name_index]


# creating the index page of our website
@app.route('/')
def index():
    return render_template("index.html", message=names)


# creating the introduction page
@app.route('/', methods=['POST'])
def text_box():
    text = request.form['list_name']
    all_info = get_all_info(text)
    return render_template("welcome.html", message=all_info)


if __name__ == '__main__':
    app.run()
