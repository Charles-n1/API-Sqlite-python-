from variables import *

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

def Dele_function():
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