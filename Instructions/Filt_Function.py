from variables import *

def Filt_function():
    print("Vous rentrez dans le filtrage..\n=========================================\n")
    print("Vous voulez voir un résultat d'un type de colonne spécifique ? (0)\n Ou voulez vous voir en fonction de plusieurs résultats de plusieurs colonnes ? (1)\nExample : Vous ne voulez voir que les ordinateurs disponibles..")













# Lobjectif, c'est de demander, Oui, il veut ça, non il veut pas ça. Et en fonction de ses réponses, on va le rediriger vers une fonction préfaites : 
#     cursor.execute("SELECT * FROM pc WHERE état = ?",          #Si il cherche unique en fonction du l'état (une colonne)
#           (état,)
#       )

#       cursor.execute("SELECT type_pc, COUNT(*) FROM pc GROUP BY type_pc",          #Si il cherche plus complexe
#           (état,)
#       )

# En gros, le truc, ce sera un gros QCM. Où on devra dissocier, les résultats qu'apporte les filtres de SELECT. Avec, en fonction de ce que les mortels touchent
# Example : La fonction read, elle read pas réellement, elle sélectionne, puis on l'affiche, pour faire semblant de..
# C'est la même chose, ici, y'a des filtres, ils sont pas spécialmeent compréhensible, mais en fonction de ce que l'on va résulté. On va dire à l'user : 
# Voulez-vous trier la chose ? Alors que c'est pas du tout ça, la fonction SELECT de base.

# Les données, on va les stoquer dans une variable pour l'instant (si j'ai bien compris, ce que Arnaud m'a demandé)

