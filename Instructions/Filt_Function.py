from variables import *
from Instructions.Insert_Function import Is_binary

def Filt_function():
    """
    Elle permet de filtrer les informations de manières différentes en fonction de 3 paramètres :
    1) Quelle valeur de la propriété de pc chercher ?
    2) Quelle Ordre ? (Croissant décroissant)
    3) Avec une limite d'affichage ? (2 par exemples)

    Args:
        "Input 1": la propriété cherché
        "Input 2": 0/1 (Non/Oui) Veux-tu trier en fonction de la valeur de la propriété ?
        "Input 3": Si Oui : Valeur de la propriété ?
        "Input 4": 0/1 (Non, Oui) (veux-tu un ordre ?)
        "Input 5": Si Oui : Décroissant ou Croissant ?
        "Input 6": 0/1 (Non/Oui) Imposer une limite d'affichage ?
        "Input 7": Si Oui : Nombre d'éléments à afficher ?

    Returns:
        Les informations filtrées.
    """
    print("===========================================================")
    print("Il y a 3 principaux filtres : \n1) En fonction de la valeur de la propriété (Example : état : disponible)")
    print("2) En fonction, de l'ordre de output (décroissant / croissant)")
    print("3) Et en fonction, du nombre de résultat que vous voulez voir affiché")
    print("===========================================================\n")
    Query = "SELECT * FROM pc"

    input("Vous-voulez trier dans l'odre des dates ? Non (0) Croissant (1) Décroissant (2)")
    cursor.execute("SELECT * FROM pc ORDER BY date(date) DESC")
    rows = cursor.fetchall()
    for row in rows:                                         #On affiche tous colonne par colonne
        print(row)
    # name_col = input("Quel est le nom de propriété que vous cherchez à manipuler ?: ")
    # Access_1 = input("Vous-voulez trier en fonction d'une valeur spécifique à une propriété ? Oui (1) Non (0): ")
    # if Is_binary(Access_1) == False: return -1
    # if Access_1 == "1":
    #     Answer_1 = input("Quelles est la valeur que vous cherchez ?: ")
    #     Query += f" WHERE {name_col} = '{Answer_1}'"

    # Access_2 = input("Vous-voulez en plus de ça, y mettre un ordre d'affichage (Croissant/décroissant) ? Oui (1) Non (0): ")
    # if Is_binary(Access_2) == False: return -1
    # if Access_2 == "1":
    #     Answer_2 = input("Plutôt, Croissant (1) ou Décroissant (0) ?: ")
    #     if Answer_2 == "1":
    #         Answer_2 = "ASC"
    #     else :
    #         Answer_2 = "DESC"
    #     Query += f" ORDER BY name {Answer_2}"

    # Access_3 = input("Vous-voulez en plus (une dernière fois), afficher un nombre limité de cet recherche ? Oui (1) Non (0): ")
    # if Is_binary(Access_3) == False: return -1
    # if Access_3 == "1":
    #     Answer_3 = input("Combien de résultat vous voulez voir afficher ?: ")
    #     Query += f" LIMIT {Answer_3}"

    # # print(f"{Query}")
    # cursor.execute(f"{Query}")
    # rows = cursor.fetchall()
    # for row in rows:                                         #On affiche tous colonne par colonne et on stocke dans rows
    #     print(row)

# Afficher les résultats des propriétés ? Pour bien les tapers ?
# Message d'erreur quand mauvais input