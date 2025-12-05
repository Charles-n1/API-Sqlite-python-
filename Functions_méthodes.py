from variables import *
import os
from Instructions.Insert_Function import name_already_exist

#Gestion d'erreur
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def Dele_function():
    name = input("Quel est le nom de l'objet à supprimer ?: ") #Quel est le nom de la valeur à supprimer ?
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1  #Gestion d'erreur
    cursor.execute("DELETE FROM pc WHERE name = ?",            #Delete en fonction du nom
        (name,)
    )
    db.commit() #save
    print(name, "a été supprimé !")

def Read_function():
    name = input("Quel est le nom de l'objet à lire ?: ")      #Quel est le nom de la valeur à lire ?
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1   #Gestion d'erreur
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
    print(f"Listes des propriétés de {name} : ", end="")      #On affiche, le nom de la propriété (colonne 0, de chacun)
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
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1  #Gestion d'erreur
    Show_proprieties(name)                                         #Montre les propriétés.. de l'objet (pour éviter que, il tape n'impore quoi)
    name_column = input("Quel est le nom de la colonne que tu veux Mettre à jour ?: ")        #On Dmd une colonne à rentrer
    new_value = input("Quel sera ça nouvelle valeur ?: ")                                     #On Dmd une valeur à rentrer
    cursor.execute(f"UPDATE pc SET {name_column} = ? WHERE name = ?",           #On remplace, depuis le nom, la valeur de la colonne, par la nouvelle
        (new_value, name)
    )
    db.commit()