##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## Front_end
##
from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect("Alpha_version/Base_de_donnée.db")
    db.row_factory = sqlite3.Row  # ← Nécessaire pour dict(row)
    return db

@app.route("/")
def main():
    return "hello BIRTHDAY"

@app.route("/read")
def test():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pc")
    rows = cursor.fetchall()
    db.close()
    result = [dict(row) for row in rows]
    return result

if __name__ == "__main__":
    app.run(debug=True)