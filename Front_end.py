##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## Front_end
##

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect("Alpha_version/Base_de_donnée.db") #Car Flask est continu, alors que mon prog originel ne s'active qu'une fois.
    cursor = db.cursor()
    return cursor

@app.route("/")
def main():
    return "hello BIRTHDAY"

@app.route("/read")
def Show_all(): #Littéralement la même, sauf..
    cursor = get_db() #Je dois juste accéder à la DB
    cursor.execute("SELECT * FROM pc")
    rows = cursor.fetchall()
    return render_template("doc.html", info_table=rows)

if __name__ == "__main__":
    app.run(debug=True)