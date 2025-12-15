##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## Front_end
##

from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/read", methods=["POST"])
def read():
    db = sqlite3.connect("Alpha_version/Base_de_donnée.db")
    cursor = db.cursor()

    name = request.form["Quel est le nom à lire ?: "]
    cursor.execute("SELECT * FROM pc WHERE name = ?",          #SELECT toutes les doonées
        (name,)
    )
    return jsonify(cursor.fetchone())
