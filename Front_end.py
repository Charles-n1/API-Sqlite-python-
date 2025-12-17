##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## Front_end
##

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def mod_db():
    db = sqlite3.connect("Alpha_version/Base_de_donnée.db") #Car Flask est continu, alors que mon prog originel ne s'active qu'une fois.
    cursor = db.cursor()
    return cursor

def get_db():
    db = sqlite3.connect("Alpha_version/Base_de_donnée.db") #Car Flask est continu, alors que mon prog originel ne s'active qu'une fois.
    return db

@app.route("/")
def main():
    return "hello BIRTHDAY"

@app.route("/show_all")
def Show_all(): #Littéralement la même, sauf..
    cursor = mod_db() #Je dois juste accéder à la DB
    cursor.execute("SELECT * FROM pc")
    rows = cursor.fetchall()
    return render_template("doc.html", info_table=rows)

@app.route("/erase_all")
def Erase_all(): #Littéralement la même, sauf..
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM pc",)
    db.commit() #save
    return jsonify("Everything was deleted..")

@app.route("/read", methods=["GET", "POST"])
def Read_function():
    if request.method == "POST":
        name = request.form.get("nom")
        cursor = mod_db()
        cursor.execute("SELECT * FROM pc WHERE name = ?",          #SELECT toutes les doonées
            (name,)
        )
        return jsonify(cursor.fetchone())
    return render_template("read.html")

@app.route("/delete", methods=["GET", "POST"])
def Dele_function():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        name = request.form.get("nom")
        cursor.execute("DELETE FROM pc WHERE name = ?",
            (name,)
        )
        db.commit()
        db.close()
        return jsonify(f"{name} was deleted")
    return render_template("dele.html")

@app.route("/insert", methods=["GET", "POST"])
def Insert_function(): #Insertion des données
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        name = request.form.get("nom")
        état = request.form.get("état")
        type_experience = request.form.get("type_experience")
        type_pc = request.form.get("type_pc")
        portabilité = request.form.get("portabilité")
        date = request.form.get("date")

        cursor.execute("INSERT INTO pc(name, état, type_experience, type_pc, portabilité, date) VALUES (?, ?, ?, ?, ?, ?)",
            (name, état, type_experience, type_pc, portabilité, date)
        )
        db.commit()
        db.close()
        return jsonify(f"{name} has been added to the db")
    return render_template("insert.html")

@app.route("/filter", methods=["GET", "POST"])
def Filt_function():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM pc"
        name = request.form.get("nom_propriété")
        value = request.form.get("valeur_propriété")
        if value != "" and name != "":
            query += f" WHERE {name} = '{value}'"

        order_suff = ""
        ordre = request.form.get("ordre")
        if ordre != "":
            if ordre == "Alphabétique":
                order_suff = "name ASC"
            elif ordre == "Antéalphabétique":
                order_suff = "name DESC"
            elif ordre == "Date Croissant":
                order_suff = "datetime(date) ASC"
            elif ordre == "Date Décroissant":
                order_suff = "datetime(date) DESC"
        if order_suff != "":
            query += f" ORDER BY {order_suff}"

        limit_suff = ""
        limit = request.form.get("limit")
        if limit != "":
            limit_suff = limit
        if limit_suff != "":
            query += f" LIMIT {limit_suff}"

        cursor.execute(f"{query}")
        results = cursor.fetchall()
        db.close()
        return jsonify(results)
    return render_template("filter.html")

if __name__ == "__main__":
    app.run(debug=True)