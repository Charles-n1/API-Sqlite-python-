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
        (name,)
    )
    description = cursor.fetchone()
    print(description)

def Show_proprieties(name):
    cursor.execute("SELECT * FROM pc WHERE name = ?",
        (name,)
    )
    cols = cursor.description #pour récupérer
    print(f"Listes des propriétés de {name} : ", end="")
    for i in cols :
        print(f"[{i[0]}] ", end="")
    print("\n")


def Show_all():
    cursor.execute("SELECT * FROM pc")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def Erase_all():
    cursor.execute("DELETE FROM pc",)
    db.commit() #save
    print("Everything was deleted..")

def Update_function(): #Work ici, j'aimerais, savoir, comment je peux le faire pour le faire fonctionner..
    name = input("Quel est le nom à Mettre à jour ?: ")
    Show_proprieties(name)
    name_column = input("Quel est le nom de la colonne que tu veux Mettre à jour ?: ")
    new_value = input("Quel sera ça nouvelle valeur ?: ")
    cursor.execute(f"UPDATE pc SET {name_column} = ? WHERE name = ?",
        (new_value, name)
    )
    db.commit()

def user_input(string):
    if string == "0":
        Insert_function()
    if string == "1":
        Read_function()
    if string == "2":
        Supp_function()
    if string == "3":
        Update_function()
    if string == "4":
        Show_all()
    if string == "5":
        Erase_all()
    if string == "9":
        return -1
    else :
        Insert_function()

if __name__ == "__main__" :
    User_choice = input("Que voulez-vous ? Insérer une valeur parmi les actions associés: \nINSERT (0), READ (1), DELETE (2), UPDATE (3), SHOW_DB (4), ERASE_DB (5), EXIT (9)")
    while User_choice != "9" :
        if user_input(User_choice) == -1:
            break
