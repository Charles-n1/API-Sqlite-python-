from flask import Flask, render_template, jsonify, request
import sqlite3


app = Flask(__name__)

def get_db_connection(): #Pour récupérer les informations dynamiquement
    conn = sqlite3.connect("BDD2.db")
    conn.row_factory = sqlite3.Row
    return conn

def name_already_exist(name): #On regarde, si le nom exsite déjà
    conn = get_db_connection()
    conn.execute("SELECT * FROM pc WHERE name = ?",
        (name,)
    )
    if conn.fetchone() == None:                     #Si, le nom n'a pas été trouvé, on renvoie faux (car le name n'existe pas), et true
        return False
    else :
        return True

@app.route("/init") #Hm, just a way to do.
def init():
    conn = get_db_connection()
    conn.execute( # Le type de variable PC
        """CREATE TABLE IF NOT EXISTS pc (
            id INTEGER PRIMARY KEY,
            name TEXT,
            état TEXT,
            type_experience TEXT,
            type_pc TEXT,
            portabilité TEXT,
            date TEXT
        )
        """
    )
    conn.commit()
    conn.close()
    return jsonify("Database completed") #print

@app.route("/insert", methods=["POST"])
def insert():
    conn = get_db_connection()
    name = request.form["Nom"]
    état = request.form["Disponible ou Indisponible"]
    type_experience = request.form["Expérience ou Non expérience"]
    type_pc = request.form["Pc Gamer ou Pc bureau"]
    portabilité = request.form["Fix ou Portable"]
    date = request.form["Donne moi une date: YYYY-MM-DD HH:mm:ss"]

    conn.execute("INSERT INTO pc(name, état, type_experience, type_pc, portabilité, date) VALUES (?, ?, ?, ?, ?, ?)", #4) Insère avec les valeurs données
        (name, état, type_experience, type_pc, portabilité, date)
    )
    conn.commit() #save
    conn.close()
    return jsonify(f"{name} a été ajouté") #print

@app.route("/read", methods=["POST"])
def read():
    conn = get_db_connection()
    name = request.form["Quel est nom à lire ?: "]
    if name_already_exist(name) == False: return jsonify(f"{name} n'existe pas")
    conn.cursor.execute("SELECT * FROM pc WHERE name = ?",          #SELECT toutes les doonées
        (name,)
    )
    cursor = conn.execute("SELECT * FROM pc WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()

    # Convertir Row en dict pour JSON
    return jsonify(dict(row))
