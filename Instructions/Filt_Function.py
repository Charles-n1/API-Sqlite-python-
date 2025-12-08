from variables import *
from Insert_Function import Is_binary

def Filt_function():
    print("===========================================================")
    print("Il y a 3 principaux filtres : \n1) En fonction de la valeur de la propriété (Example : état : disponible)")
    print("En fonction, de l'ordre de output (décroissant / croissant)")
    print("Et en fonction, du nombre de résultat que vous voulez voir affiché")
    print("===========================================================\n")
    Option_1 = 0
    Option_2 = 0
    Option_3 = 0

    name_col = input("Quel est le nom de propriété que vous cherchez à manipuler ?\n(Example, je veux filtrer en fonction des états..)(Du coup ce sera 'état')")
    Access_1 = input("Vous-voulez trier en fonction d'une valeur spécifique à une propriété ? Oui (1) Non (0)")
    if Is_binary(Access_1) == False: return -1
    if Access_1 == "1":
        Answer_1 = input("Quelles est la valeur que vous cherchez ?")
        Option_1 += 1

    Access_2 = input("Vous-voulez en plus de ça, d'y mettre un ordre d'affichage (Croissant/décroissant) ? Oui (1) Non (0)")
    if Is_binary(Access_2) == False: return -1
    if Access_2 == "1":
        Answer_2 = input("Plutôt, Croissant (1) ou Décroissant (0) ?")
        if Answer_2 == "1":
            Answer_2 = "ASC"
        else :
            Answer_2 = "DESC"
        Option_2 += 1

    Access_3 = input("Vous-voulez en plus (une dernière fois), afficher un nombre limité de cet recherche ? Oui (1) Non (0)")
    if Is_binary(Access_3) == False: return -1
    if Access_3 == "1":
        Answer_3 = input("Combien de résultat vous voulez voir afficher ?")
        Option_3 += 1

    if Option_1 == 1 and Option_2 == 1 and Option_3 == 1: #Dans le cas où tout est activé
        cursor.execute("SELECT * FROM pc WHERE ? = ? ORDER BY ? LIMIT ?",
            (name_col, Answer_1, Answer_2, Answer_3,)
        )
    if Option_1 == 1 and Option_2 == 0 and Option_3 == 0: #Dans le cas où tout est activé
        cursor.execute("SELECT * FROM pc WHERE ? = ? ORDER BY ? LIMIT ?",
            (name_col, Answer_1, Answer_2, Answer_3,)
        )



#SELECT * FROM pc WHERE name = valeur ORDER BY ? LIMIT ?
