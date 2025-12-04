##
## EPITECH PROJECT, 2025
## Stage : EMC
## File description:
## Annepi
##


from Functions_méthodes import *
from variables import *

def redirect_function(string):
    if string == "0":
        Insert_function()
    if string == "1":
        Read_function()
    if string == "2":
        Dele_function()
    if string == "3":
        Update_function()
    if string == "4":
        Show_all()
    if string == "5":
        Erase_all()
    if string == "9":
        return -1
    else :
        print("Le programme n'a pas compris ce que vous avez entrée.")
        print("Est-ce que vous êtes sûr que vous avez entrée un chiffre ?")

if __name__ == "__main__" :
    User_choice = input("Que voulez-vous ? Insérer une valeur parmi les actions associés: \nINSERT (0), READ (1), DELETE (2), UPDATE (3), SHOW_DB (4), ERASE_DB (5), EXIT (9)\n:")
    while User_choice != "9" :
        if redirect_function(User_choice) == -1:
            break
        User_choice = input("Que voulez-vous faire ensuite ?\nINSERT (0), READ (1), DELETE (2), UPDATE (3), SHOW_DB (4), ERASE_DB (5), EXIT (9)\n:")

