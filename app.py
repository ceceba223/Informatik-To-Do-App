from flask import Flask, render_template
from classes import Task_DB

app = Flask(__name__)

Database = Task_DB()

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/tasks")
def tasks():
    return render_template("task_list.html")

#@app.teardown_appcontext
#def close_connection(exception):
#    Database.close_connection()