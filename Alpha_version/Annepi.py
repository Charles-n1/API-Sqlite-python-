##
## EPITECH PROJECT, 2025
## Stage : EMC
## File description:
## Annepi
##


from Instructions.Functions_méthodes import *
from variables import *
from Instructions.Insert_Function import *
from Instructions.Filt_Function import *
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def redirect_function(string):  # En fonction de l'input (0,1,2,3,4,5,9) on éxécute la fonction associée
    if string == "0":
        Insert_function()
    elif string == "1":
        Read_function()
    elif string == "2":
        Dele_function()
    elif string == "3":
        Update_function()
    elif string == "4":
        Show_all()
    elif string == "5":
        Erase_all()
    elif string == "6":
        Filt_function()
    elif string == "9":
        return -1
    else :
        print("Le programme n'a pas compris ce que vous avez entrée.")
        print("Est-ce que vous êtes sûr que vous avez entrée un chiffre ?")

if __name__ == "__main__" :


    cursor.execute("INSERT INTO image(name, path) VALUES (?, ?)", #INSERTION D'image ici
        ("hello", "Images/hello.jpeg",)
    )


    User_choice = input("Que voulez-vous ? Insérer une valeur parmi les actions associés: \nINSERT (0), READ (1), DELETE (2), UPDATE (3), SHOW_DB (4), ERASE_DB (5), FILTRATE (6), EXIT (9)\n:")
    while User_choice != "9" :
        clear()
        if redirect_function(User_choice) == -1:
            break
        User_choice = input("Que voulez-vous faire ensuite ?\nINSERT (0), READ (1), DELETE (2), UPDATE (3), SHOW_DB (4), ERASE_DB (5), FILTRATE (6), EXIT (9)\n:")

