##
## EPITECH PROJECT, 2025
## Stage : EMC
## File description:
## Annepi
##

import sqlite3

db = sqlite3.connect("Base_de_donnée.db")
cursor = db.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS pc (
        id INTEGER PRIMARY KEY,
        name TEXT,
        état INTEGER,
        type_experience INTEGER,
        type_pc INTEGER,
        portabilité INTEGER
    )
    """
)

def Insert_function():
    name = input("Donne lui un nom: ")
    état = input("Disponible (1) ou Indisponible (0) ?: ")
    type_experience = input("Expérience ? (1) Oui (0) Non ?: ")
    type_pc = input("Pc Puissant (1) Pc de bureautique (0) ?: ")
    portabilité = input("Fixe (1) Ou Portable (0) ?: ")

    cursor.execute("INSERT INTO pc(name, état, type_experience, type_pc, portabilité) VALUES (?, ?, ?, ?, ?)",
        (name, état, type_experience, type_pc, portabilité)
    )
    db.commit() #save
    print(name, "a été ajouté !")

def Supp_function():
    name = input("Quel est le nom de l'objet à supprimer ?: ")
    cursor.execute("DELETE FROM pc WHERE name = ?",
        (name,)
    )
    db.commit() #save
    print(name, "a été supprimé !")

def Read_function():
    name = input("Quel est le nom de l'objet à lire ?: ")
    cursor.execute("SELECT * FROM pc WHERE name = ?",
        (name)
    )
    colonnes = cursor.description[0]
    for i in colonnes :
        print(colonnes, "\n")

def Update_function(): #Work ici, j'aimerais, savoir, comment je peux le faire pour le faire fonctionner..
    cursor.execute("PRAGMA table_info(pc)")
    cursor.fetchall()
    db.commit()

if __name__ == "__main__" :
    print(cursor.fetchall())
    Insert_function()
    Update_function()
    Read_function()
