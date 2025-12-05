from variables import *

def name_already_exist(name):
    cursor.execute("SELECT * FROM pc WHERE name = ?", #On regarde, si le nom exsite déjà
        (name,)
    )
    if cursor.fetchone() == None:                     #Si, le nom n'a pas été trouvé, on renvoie faux (car le name n'existe pas), et true
        return False
    else :
        return True

def Is_binary(variable_input):                        #Vérifie, si la string input, est un 0 ou un 1.
    if variable_input != "0" and variable_input != "1":
        print("Caractère invalide : Vous n'avez pas écrit 0 ou 1..")
        return False
    return True

def Binary_to_string(état, type_experience, type_pc, portabilité):
    if état == "0": état = "Indisponible"
    else : état = "Disponible"
    if type_experience == "0": type_experience = "Non Expérience"
    else : type_experience = "Expérience"
    if type_pc == "0": type_pc = "Bureautique"
    else : type_pc = "Gamer"
    if portabilité == "0": portabilité = "Portable"
    else : portabilité = "Fixe"
    return état, type_experience, type_pc, portabilité

def Is_Good_input(name, état, type_experience, type_pc, portabilité):
    if name_already_exist(name) == True:              #Gestion d'erreur si, ça existe déjà
        print(f"{name} already exist")
        return -1
    if Is_binary(état) == False: return -1
    if Is_binary(type_experience) == False: return -1
    if Is_binary(type_pc) == False: return -1
    if Is_binary(portabilité) == False: return -1

def Insert_function():
    name = input("Donne lui un nom: ")                #Demande les inputs à rentrer
    état = input("Disponible (1) ou Indisponible (0) ?: ")
    type_experience = input("Expérience ? : (1) Oui (0) Non ?: ")
    type_pc = input("Pc Puissant (1) Pc de bureautique (0) ?: ")
    portabilité = input("Fixe (1) Ou Portable (0) ?: ")

    if Is_Good_input(name, état, type_experience, type_pc, portabilité) == -1: # Vérifie si les inputs sont bons
        return -1
    état, type_experience, type_pc, portabilité = Binary_to_string(état, type_experience, type_pc, portabilité) # Rendre les bonnes valeurs, aux valeurs entrées. (Pour facilité, l'entrée utilisateur)

    cursor.execute("INSERT INTO pc(name, état, type_experience, type_pc, portabilité) VALUES (?, ?, ?, ?, ?)", #Insère avec les valeurs données
        (name, état, type_experience, type_pc, portabilité)
    )
    db.commit() #save
    print(name, "a été ajouté !")