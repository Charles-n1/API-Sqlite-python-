from flask import Flask, render_template, jsonify
import sqlite3


app = Flask(__name__)
db = sqlite3.connect("Base_de_donnée.db")
cursor = db.cursor()

@app.route("/")
def insert_test():
    return 
