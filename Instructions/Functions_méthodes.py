from variables import *
from Instructions.Insert_Function import name_already_exist



#Gestion d'erreur

def Dele_function(): #Supprimer la donnée en fonction du nom
    name = input("Quel est le nom de l'objet à supprimer ?: ") #Demande du nom ?
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1  #Gestion d'erreur, si le nom n'existe pas
    cursor.execute("DELETE FROM pc WHERE name = ?",            #Delete
        (name,)
    )
    db.commit() #save
    print(name, "a été supprimé !")

def Read_function():  # Read la donnée en fonction du nom
    name = input("Quel est le nom de l'objet à lire ?: ")      #Demande le nom ?
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1   #Gestion d'erreur, si le nom n'existe pas
    cursor.execute("SELECT * FROM pc WHERE name = ?",          #SELECT toutes les doonées
        (name,)
    )
    print(cursor.fetchone())                                  #Imprime la donnée (en une ligne)

def Show_proprieties(name):  # Montre les propriété (à l'aide des métadonnées) On y rentre un nom directement
    cursor.execute("SELECT * FROM pc WHERE name = ?",         # Recherche des infos
        (name,)
    )
    cols = cursor.description #pour récupérer
    print(f"Listes des propriétés de {name} : ", end="")      #On affiche le nom de la propriété : (colonne 0, de chacun)
    for i in cols :
        print(f"[{i[0]}] ", end="")
    print("\n")

def Show_all():  # Montre toute la base de donnée
    cursor.execute("SELECT * FROM pc")                       #On prends tous
    rows = cursor.fetchall()
    for row in rows:                                         #On affiche tous colonne par colonne
        print(row)

def Erase_all():
    cursor.execute("DELETE FROM pc",)
    db.commit() #save
    print("Everything was deleted..")

def Update_function():  # Update la donnée
    name = input("Quel est le nom à Mettre à jour ?: ")            # Demande un nom
    if name_already_exist(name) == False: print(f"{name} n'existe pas"); return -1  #Gestion d'erreur, si le nom n'existe pas
    Show_proprieties(name)                                         # Montre les propriétés (pour éviter que, il tape n'impore quoi)
    name_column = input("Quel est le nom de la colonne que tu veux Mettre à jour ?: ")        #On Dmd une colonne à choisir
    new_value = input("Quel sera ça nouvelle valeur ?: ")                                     #On Dmd une valeur à rentrer
    cursor.execute(f"UPDATE pc SET {name_column} = ? WHERE name = ?",           #On remplace, depuis le nom, la valeur de la colonne, par la nouvelle
        (new_value, name)
    )
    db.commit()