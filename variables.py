##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## variables
##

import sqlite3

db = sqlite3.connect("Base_de_donnée.db")
cursor = db.cursor()

cursor.execute( # Le type de variable PC
    """CREATE TABLE IF NOT EXISTS pc (
        id INTEGER PRIMARY KEY,
        name TEXT,
        état INTEGER,
        type_experience INTEGER,
        type_pc INTEGER,
        portabilité INTEGER
    )
    """
)

cursor.execute( # Le type de variable Image
    """CREATE TABLE IF NOT EXISTS image (
        id INTEGER PRIMARY KEY,
        name TEXT,
        path TEXT,
    )
    """
)