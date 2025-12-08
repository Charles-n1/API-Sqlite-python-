from variables import *
from Instructions.Insert_Function import Is_binary

def Filt_function():
    print("===========================================================")
    print("Il y a 3 principaux filtres : \n1) En fonction de la valeur de la propriété (Example : état : disponible)")
    print("2) En fonction, de l'ordre de output (décroissant / croissant)")
    print("3) Et en fonction, du nombre de résultat que vous voulez voir affiché")
    print("===========================================================\n")
    Query = "SELECT * FROM pc"

    name_col = input("Quel est le nom de propriété que vous cherchez à manipuler ?: ")
    Access_1 = input("Vous-voulez trier en fonction d'une valeur spécifique à une propriété ? Oui (1) Non (0): ")
    if Is_binary(Access_1) == False: return -1
    if Access_1 == "1":
        Answer_1 = input("Quelles est la valeur que vous cherchez ?: ")
        Query += f" WHERE {name_col} = '{Answer_1}'"

    Access_2 = input("Vous-voulez en plus de ça, y mettre un ordre d'affichage (Croissant/décroissant) ? Oui (1) Non (0): ")
    if Is_binary(Access_2) == False: return -1
    if Access_2 == "1":
        Answer_2 = input("Plutôt, Croissant (1) ou Décroissant (0) ?: ")
        if Answer_2 == "1":
            Answer_2 = "ASC"
        else :
            Answer_2 = "DESC"
        Query += f" ORDER BY name {Answer_2}"

    Access_3 = input("Vous-voulez en plus (une dernière fois), afficher un nombre limité de cet recherche ? Oui (1) Non (0): ")
    if Is_binary(Access_3) == False: return -1
    if Access_3 == "1":
        Answer_3 = input("Combien de résultat vous voulez voir afficher ?: ")
        Query += f" LIMIT {Answer_3}"

    # print(f"{Query}")
    cursor.execute(f"{Query}")
    rows = cursor.fetchall()
    for row in rows:                                         #On affiche tous colonne par colonne
        print(row)



# if Option_1 == 1 and Option_2 == 1 and Option_3 == 1: #Dans le cas où tout est activé
#     cursor.execute("SELECT * FROM pc WHERE ? = ? ORDER BY ? LIMIT ?",
#         (name_col, Answer_1, Answer_2, Answer_3,)
#     )
# if Option_1 == 1 and Option_2 == 0 and Option_3 == 0: #Dans le cas où tout est activé
#     cursor.execute("SELECT * FROM pc WHERE ? = ? ORDER BY ? LIMIT ?",
#         (name_col, Answer_1, Answer_2, Answer_3,)
#     )

#SELECT * FROM pc WHERE name = valeur ORDER BY ? LIMIT ?
