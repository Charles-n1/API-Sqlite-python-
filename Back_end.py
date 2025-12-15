import sqlite3

db = sqlite3.connect("Base_de_donnée.db")
cursor = db.cursor()

def name_already_exist(name): #On regarde, si le nom exsite déjà
    cursor.execute("SELECT * FROM pc WHERE name = ?",
        (name,)
    )
    if cursor.fetchone() == None:                     #Si, le nom n'a pas été trouvé, on renvoie faux (car le name n'existe pas), et true
        return False
    else :
        return True