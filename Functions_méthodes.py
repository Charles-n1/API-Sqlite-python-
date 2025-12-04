from variables import *

def name_already_exist(name):
    cursor.execute("SELECT * FROM pc WHERE name = ?",
        (name,)
    )
    existing_name = cursor.fetchone()
    if existing_name[1] == None:
        print("\n\nVide")
    # if name == existing_name[1] :
    #     return True
    # else :
    #     return False

def Insert_function():
    name = input("Donne lui un nom: ") #Demande les inputs à rentrer
    if name_already_exist(name) == True:
        print(f"{name} already exist")
        return -1
    # état = input("Disponible (1) ou Indisponible (0) ?: ")
    # if état != "0" and état != "1":
    #     print("Caractère invalide")
    #     return -1
    # type_experience = input("Expérience ? (1) Oui (0) Non ?: ")
    # if type_experience != "0" and type_experience != "1":
    #     print("Caractère invalide")
    #     return -1
    # type_pc = input("Pc Puissant (1) Pc de bureautique (0) ?: ")
    # if type_pc != "0" and type_pc != "1":
    #     print("Caractère invalide")
    #     return -1
    # portabilité = input("Fixe (1) Ou Portable (0) ?: ")
    # if portabilité != "0" and portabilité != "1":
    #     print("Caractère invalide")
    #     return -1
    # cursor.execute("INSERT INTO pc(name, état, type_experience, type_pc, portabilité) VALUES (?, ?, ?, ?, ?)", #Insère avec les valeurs données
    #     (name, état, type_experience, type_pc, portabilité)
    # )
    cursor.execute("INSERT INTO pc(name) VALUES (?)", #Insère avec les valeurs données
        (name,)
    )
    db.commit() #save
    print(name, "a été ajouté !")

def Dele_function():
    name = input("Quel est le nom de l'objet à supprimer ?: ") #Quel est le nom de la valeur à supprimer ?
    cursor.execute("DELETE FROM pc WHERE name = ?",            #Delete en fonction du nom
        (name,)
    )
    db.commit() #save
    print(name, "a été supprimé !")

def Read_function():
    name = input("Quel est le nom de l'objet à lire ?: ")      #Quel est le nom de la valeur à lire ?
    cursor.execute("SELECT * FROM pc WHERE name = ?",          #Liste, avec SELECT, toutes ses données.
        (name,)
    )
    description = cursor.fetchone()
    print(description)

def Show_proprieties(name):
    cursor.execute("SELECT * FROM pc WHERE name = ?",         #On entre, un nom dedans. Et on prends ses métadonnées
        (name,)
    )
    cols = cursor.description #pour récupérer
    print(f"Listes des propriétés de {name} : ", end="")     #On affiche, le nom de la propriété (colonne 0, de chacun)
    for i in cols :
        print(f"[{i[0]}] ", end="")
    print("\n")


def Show_all():
    cursor.execute("SELECT * FROM pc")                       #On prends tous
    rows = cursor.fetchall()

    for row in rows:                                         #On affiche colonne par colonne
        print(row)

def Erase_all():
    cursor.execute("DELETE FROM pc",)
    db.commit() #save
    print("Everything was deleted..")

def Update_function():
    name = input("Quel est le nom à Mettre à jour ?: ")            #On entre, un nom dedans.
    Show_proprieties(name)
    name_column = input("Quel est le nom de la colonne que tu veux Mettre à jour ?: ")        #On Dmd une colonne à rentrer
    new_value = input("Quel sera ça nouvelle valeur ?: ")                                     #On Dmd une valeur à rentrer
    cursor.execute(f"UPDATE pc SET {name_column} = ? WHERE name = ?",           #On remplace, depuis le nom, la valeur de la colonne, par la nouvelle
        (new_value, name)
    )
    db.commit()